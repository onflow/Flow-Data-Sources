import os
import re
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from markdownify import markdownify as md

##############################################################################
# CONFIG
##############################################################################

SITES = [
    # Normal docs sites
    "https://developers.flow.com/",
    "https://academy.ecdao.org/en/cadence-by-example",
    "https://academy.ecdao.org/en/snippets",
    "https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner",
    "https://academy.ecdao.org/en/catalog/courses/beginner-dapp",

    # GitHub repos
    "https://github.com/onflow/cadence-lang.org/",
    "https://github.com/onflow/flips"
    "https://github.com/onflow/flow-ft/",
    "https://github.com/onflow/flow-core-contracts/",
    "https://github.com/onflow/flow-nft/",
    "https://github.com/onflow/nft-storefront/",
    "https://github.com/onflow/flow-evm-bridge",
    "https://github.com/dapperlabs/nba-smart-contracts",
    "https://github.com/dapperlabs/nfl-smart-contracts",

    # GitHub Discussions:
    "https://github.com/orgs/onflow/discussions" 
]

OUTPUT_DIR = "scraped_docs"
MAX_PAGES_PER_SITE = 200  # BFS limit for normal sites & repos
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; FlowDocsScraper/1.0; +https://github.com/YourUser/YourRepo)"
}

# For GitHub repos: only store code files with these extensions or readme
ALLOWED_EXTENSIONS = {".cdc", ".md", ".json", ".yaml", ".yml", ".toml", ".js", ".ts"}

# For Discussions: how many total discussion threads to scrape
MAX_DISCUSSION_THREADS = 500

##############################################################################
# UTILS
##############################################################################

def ensure_dir_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def sanitize_folder_name(url: str) -> str:
    without_protocol = re.sub(r'^https?:\/\/', '', url)
    sanitized = re.sub(r'[^0-9a-zA-Z]+', '_', without_protocol)
    return sanitized.lower().strip('_')

def sanitize_file_name(path: str) -> str:
    """If empty, return index.md, else convert path to safe filename with .md suffix."""
    path = path.strip('/')
    if not path:
        return "index.md"
    name = re.sub(r'[^0-9a-zA-Z]+', '_', path)
    return name.lower() + ".md"

def get_extension(filepath: str) -> str:
    _, ext = os.path.splitext(filepath)
    return ext.lower()

##############################################################################
# DETECTING MODES
##############################################################################

def is_normal_site(url: str) -> bool:
    """Return True if it's not GitHub or special case."""
    parsed = urlparse(url)
    if "github.com" in parsed.netloc.lower():
        return False
    return True

def is_github_repo(url: str) -> bool:
    """
    Check if URL is a standard GitHub repo URL, e.g. https://github.com/onflow/flow-ft
    i.e. domain = github.com and path has at least /user/repo
    Exclude /orgs/onflow/discussions from being detected as a repo.
    """
    parsed = urlparse(url)
    if "github.com" not in parsed.netloc.lower():
        return False
    # If it's /orgs/<org>/discussions, we want a separate approach
    if re.search(r'^/orgs/[^/]+/discussions', parsed.path):
        return False

    # If it has at least /user/repo
    path_parts = parsed.path.strip("/").split("/")
    return len(path_parts) >= 2

def is_github_discussions(url: str) -> bool:
    """
    Check if it's a GitHub 'orgs/<org>/discussions' URL.
    Example: https://github.com/orgs/onflow/discussions
    """
    parsed = urlparse(url)
    if "github.com" not in parsed.netloc.lower():
        return False
    # Must match /orgs/<org>/discussions...
    return re.search(r'^/orgs/[^/]+/discussions', parsed.path) is not None

##############################################################################
# GITHUB REPO SCRAPING
##############################################################################

def parse_github_blob_url(url: str):
    """
    Convert /blob/<branch>/<path> to raw.githubusercontent.com link.
    Example:
      https://github.com/onflow/flow-ft/blob/master/contracts/ExampleToken.cdc
      => https://raw.githubusercontent.com/onflow/flow-ft/master/contracts/ExampleToken.cdc
    """
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")  # e.g. ['onflow','flow-ft','blob','master','contracts','ExampleToken.cdc']
    if len(parts) < 4:
        return None, None
    user = parts[0]
    repo = parts[1]
    branch = parts[3]  # 'master' or 'main'
    file_path_list = parts[4:]  # remainder
    file_path_str = "/".join(file_path_list)
    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{file_path_str}"
    return raw_url, file_path_str

def should_follow_github_link(base_repo_url: str, new_url: str) -> bool:
    """Skip commits, pulls, etc. Only keep root, /tree/(main|master)/..., /blob/(main|master)/..."""
    new_parsed = urlparse(new_url)
    if "github.com" not in new_parsed.netloc.lower():
        return False
    skip_keywords = ["/commit/", "/pull/", "/pulls/", "/compare/", "/issues/", "/blame/"]
    if any(k in new_parsed.path for k in skip_keywords):
        return False

    base_parsed = urlparse(base_repo_url)
    base_path = base_parsed.path.rstrip("/")
    if new_parsed.path.rstrip("/") == base_path:
        return True
    if re.search(r'/tree/(main|master)(/|$)', new_parsed.path):
        return True
    if re.search(r'/blob/(main|master)(/|$)', new_parsed.path):
        return True
    return False

def scrape_github_directory_page(url: str):
    """Fetch a directory (root or /tree/main), return (None, child_links). We don't store HTML for directories."""
    print(f"Scraping GitHub directory (no file saved): {url}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching directory page {url}: {e}")
        return None, []

    soup = BeautifulSoup(resp.text, "html.parser")
    links = []
    for a_tag in soup.find_all("a", href=True):
        abs_link = urljoin(url, a_tag["href"]).split('#')[0]
        links.append(abs_link)
    return None, list(set(links))

def scrape_github_file_blob(url: str):
    """
    Build raw.githubusercontent link, fetch raw text if extension is allowed (or readme).
    Return the content as triple-backtick text or None if skipping.
    """
    raw_url, file_path_in_repo = parse_github_blob_url(url)
    if not raw_url:
        print(f"Failed to parse blob URL: {url}")
        return None

    # If extension not in ALLOWED_EXTENSIONS and not a 'readme'
    filename_lower = file_path_in_repo.lower()
    ext = get_extension(filename_lower)
    if "readme" not in os.path.basename(filename_lower) and ext not in ALLOWED_EXTENSIONS:
        print(f"Skipping file (unsupported extension): {file_path_in_repo}")
        return None

    # Fetch raw content
    try:
        resp = requests.get(raw_url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        code_text = resp.text
        return f"```\n{code_text}\n```"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching raw content {raw_url}: {e}")
        return None

##############################################################################
# GITHUB DISCUSSIONS SCRAPING
##############################################################################

def scrape_github_discussion_page(url: str) -> (str, list):
    """
    Scrape one discussion thread page (like /orgs/onflow/discussions/1330).
    Return (markdown_of_entire_thread_page, no_child_links).
    """
    print(f"Scraping discussion thread: {url}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching discussion page {url}: {e}")
        return "", []

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove scripts/styles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    md_content = md(str(soup), heading_style="ATX")
    return md_content, []

def scrape_github_discussions_listing(url: str) -> (list, str):
    """
    Scrape a listing page for GitHub org discussions, return:
      - list of absolute discussion-thread URLs found
      - next_page_url or None
    We specifically look for 'a' links to /orgs/<org>/discussions/#### 
    and a link rel="next" for pagination.
    """
    print(f"Scraping discussions listing page: {url}")
    discussion_links = []
    next_page = None

    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching discussions listing {url}: {e}")
        return [], None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Each discussion row is often <article class="DiscussionListItem"> or <div class="js-organization-discussions-list-item">
    # but more reliably, we want /orgs/<org>/discussions/<number>
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if re.search(r'/orgs/[^/]+/discussions/\d+', href):
            abs_link = urljoin(url, href)
            discussion_links.append(abs_link)

    # Attempt to find next-page link by rel="next"
    next_link = soup.find("a", attrs={"rel": "next"})
    if next_link and next_link.has_attr("href"):
        next_page = urljoin(url, next_link["href"])

    return list(set(discussion_links)), next_page

def crawl_github_discussions(base_url: str):
    """
    Specialized approach for https://github.com/orgs/onflow/discussions (or any org).
    We'll parse listing pages, find all discussion links, fetch each thread page as Markdown.
    We'll also follow 'next' listing pages if available, up to MAX_DISCUSSION_THREADS threads.
    """
    folder_name = sanitize_folder_name(base_url)
    site_folder = os.path.join(OUTPUT_DIR, folder_name)
    ensure_dir_exists(site_folder)

    visited_listings = set()
    to_visit_listings = [base_url]

    visited_threads = set()
    threads_count = 0

    while to_visit_listings:
        listing_url = to_visit_listings.pop()
        if listing_url in visited_listings:
            continue
        visited_listings.add(listing_url)

        # 1) Scrape listing for threads + next link
        discussion_links, next_page = scrape_github_discussions_listing(listing_url)

        # 2) If there's a next page, queue it
        if next_page and next_page not in visited_listings:
            to_visit_listings.append(next_page)

        # 3) Scrape each discussion thread
        for dlink in discussion_links:
            if dlink in visited_threads:
                continue
            visited_threads.add(dlink)
            threads_count += 1
            if threads_count > MAX_DISCUSSION_THREADS:
                print(f"Reached MAX_DISCUSSION_THREADS={MAX_DISCUSSION_THREADS}")
                return

            md_content, _ = scrape_github_discussion_page(dlink)
            if md_content:
                # We store each discussion in, for example, discussion_1330.md
                # Extract the numeric ID from the URL
                match = re.search(r'/discussions/(\d+)', dlink)
                thread_id = match.group(1) if match else "unknown"
                file_name = f"discussion_{thread_id}.md"
                file_path = os.path.join(site_folder, file_name)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# Source: {dlink}\n\n")
                    f.write(md_content)

##############################################################################
# GENERIC SITE SCRAPING
##############################################################################

def scrape_generic_site(url: str) -> (str, list):
    """For normal websites, BFS same domain, store HTML->Markdown."""
    print(f"Scraping generic site page: {url}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return "", []

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    md_content = md(str(soup), heading_style="ATX")

    base_parsed = urlparse(url)
    base_domain = base_parsed.netloc
    child_links = []
    for a_tag in soup.find_all("a", href=True):
        abs_link = urljoin(url, a_tag['href']).split('#')[0]
        if abs_link.startswith("mailto:") or abs_link.startswith("javascript:"):
            continue
        p = urlparse(abs_link)
        if p.netloc == base_domain:
            child_links.append(abs_link)

    child_links = list(set(child_links))
    return md_content, child_links

##############################################################################
# MAIN BFS
##############################################################################

def crawl_site(base_url: str):
    """Entry point for each site URL. Determine which mode to run."""
    folder_name = sanitize_folder_name(base_url)
    site_folder = os.path.join(OUTPUT_DIR, folder_name)
    ensure_dir_exists(site_folder)

    if is_github_discussions(base_url):
        # Special approach
        print(f"=== Starting specialized crawl for GitHub Discussions: {base_url} ===")
        crawl_github_discussions(base_url)
        return

    if is_github_repo(base_url):
        print(f"=== Starting GitHub Repo Scrape for {base_url} ===")
        visited = set()
        to_visit = [base_url]
        page_count = 0

        base_parsed = urlparse(base_url)
        while to_visit:
            current_url = to_visit.pop()
            if current_url in visited:
                continue
            visited.add(current_url)

            new_parsed = urlparse(current_url)
            # Is it a file (blob)?
            if re.search(r'/blob/(main|master)/', new_parsed.path):
                content = scrape_github_file_blob(current_url)
                child_links = []
                if content:
                    # Store the raw code
                    rel_path = new_parsed.path.strip("/")
                    file_name = sanitize_file_name(rel_path)
                    file_path = os.path.join(site_folder, file_name)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(f"# Source: {current_url}\n\n")
                        f.write(content)
                    page_count += 1

            elif re.search(r'/tree/(main|master)/', new_parsed.path) or new_parsed.path.rstrip("/") == base_parsed.path.rstrip("/"):
                # It's a directory or the repo root
                _, links = scrape_github_directory_page(current_url)
                child_links = [ln for ln in links if should_follow_github_link(base_url, ln)]
            else:
                # Possibly the exact base path, or something else
                if new_parsed.path.rstrip("/") == base_parsed.path.rstrip("/"):
                    # BFS sub-links
                    _, links = scrape_github_directory_page(current_url)
                    child_links = [ln for ln in links if should_follow_github_link(base_url, ln)]
                else:
                    child_links = []

            # BFS limit
            if page_count >= MAX_PAGES_PER_SITE:
                print(f"Reached MAX_PAGES_PER_SITE={MAX_PAGES_PER_SITE} for {base_url}")
                break

            for ln in child_links:
                if ln not in visited:
                    to_visit.append(ln)

        return

    # Otherwise it's a normal site
    print(f"=== Starting Generic Site BFS for {base_url} ===")
    visited = set()
    to_visit = [base_url]
    page_count = 0

    base_parsed = urlparse(base_url)
    base_domain = base_parsed.netloc
    base_path = base_parsed.path.rstrip("/")

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue
        visited.add(current_url)

        md_content, child_links = scrape_generic_site(current_url)
        if md_content:
            # store it
            curr_parsed = urlparse(current_url)
            rel_path = curr_parsed.path
            if curr_parsed.query:
                rel_path += "?" + curr_parsed.query
            file_name = sanitize_file_name(rel_path)
            file_path = os.path.join(site_folder, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# Source: {current_url}\n\n")
                f.write(md_content)
            page_count += 1

            if page_count >= MAX_PAGES_PER_SITE:
                print(f"Reached MAX_PAGES_PER_SITE={MAX_PAGES_PER_SITE} for {base_url}")
                break

        for ln in child_links:
            if ln not in visited:
                to_visit.append(ln)

##############################################################################
# MAIN
##############################################################################

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for site_url in SITES:
        print("="*70)
        print(f"Starting crawl for {site_url}")
        crawl_site(site_url)
        print(f"Completed crawl for {site_url}")

    print("\nAll sites crawled.")

if __name__ == "__main__":
    main()
