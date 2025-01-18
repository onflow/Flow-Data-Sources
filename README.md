# Flow Data Sources

This repository contains a Python script that updates daily a list of Flow-related sites, GitHub repositories, and GitHub discussions and converts them into **Markdown** files. The resulting `.md` files are intended for **AI ingestion**, **Retrieval-Augmented Generation (RAG)** pipelines, chatbots, or any other knowledge base platform that benefits from structured text.

---

## Table of Contents

- [Purpose](#purpose)
- [How It Works](#how-it-works)
  - [1. Normal Docs Sites (HTML → MD)](#1-normal-docs-sites-html--md)
  - [2. GitHub Repos (Raw Code)](#2-github-repos-raw-code)
  - [3. GitHub Discussions (Q&A Text Only)](#3-github-discussions-qa-text-only)
- [Usage](#usage)
  - [Requirements](#requirements)
  - [Running the Scraper](#running-the-scraper)
- [Modifying the List of Sites](#modifying-the-list-of-sites)
- [Output Structure](#output-structure)
- [Scheduling & Automation](#scheduling--automation)
- [FAQ](#faq)

---

## Purpose

We want a single repository that **periodically crawls** all relevant Flow ecosystem content—**documentation**, **code examples**, and **community discussions**—and stores them in a consolidated **Markdown** format. You can then feed these files into:

- **ChatGPT plugins** (for enhanced Q&A)
- **Retrieval-Augmented Generation** (indexing and searching them in a vector database)
- **Discord/Telegram bots** that cite official doc sections
- **Any** other knowledge base for advanced Q&A or search.

---

## How It Works

The Python script performs **domain-limited BFS** (Breadth-First Search) and specialized scraping logic based on each URL:

### 1. Normal Docs Sites (HTML → MD)

- **Non-GitHub** URLs are treated as “normal” websites.  
- The script fetches each page and removes `<script>`, `<style>`, `<noscript>` tags.
- Then it uses [`markdownify`](https://pypi.org/project/markdownify/) to convert the **remaining HTML** into **Markdown**.  
- It recurses only within the **same domain** to avoid crawling unrelated pages.

### 2. GitHub Repos (Raw Code)

- For **GitHub repo** links like `https://github.com/onflow/flow-ft/`, the script visits:
  - The **repo root**
  - `tree/(main|master)/...` subdirectories
  - `blob/(main|master)/...` file pages
- **Files** with certain extensions (like `.cdc`, `.md`, `.json`, etc.) or **any** `README` are downloaded in their **raw** form from `raw.githubusercontent.com`.  
- The file contents are saved in a `.md` file, wrapped in triple backticks for easy code parsing.

### 3. GitHub Discussions (Q&A Text Only)

- For `https://github.com/orgs/onflow/discussions`, the script:
  - Crawls the **listing** pages, discovers discussion links like `/orgs/onflow/discussions/1330`
  - For each thread, it extracts **only** the text from user posts (skipping the GitHub UI) and converts it to Markdown.
- This yields `.md` files containing the **original question** and **comments/replies**.

---

## Usage

### Requirements

1. **Python 3.7+**  
2. [`requests`](https://pypi.org/project/requests/), [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/), [`markdownify`](https://pypi.org/project/markdownify/)

Install all dependencies:

pip install requests beautifulsoup4 markdownify


### Running the Scraper
Clone or download this repo locally.

In the repo directory, run:

python scraper.py

The script will crawl each site listed in SITES (inside scraper.py) and output the results under scraped_docs/.

Modifying the List of Sites
Inside scraper.py, near the top, you’ll see:

python

SITES = [
    "https://developers.flow.com/",
    "https://academy.ecdao.org/en/cadence-by-example",
    ...
    "https://github.com/onflow/flow-ft/",
    ...
    "https://github.com/orgs/onflow/discussions"
]

Add a docs site by appending its URL if it’s not on GitHub.
Add a GitHub repo by appending the base URL (e.g. "https://github.com/onflow/another-repo").
Add another GitHub Discussions page if needed.
Remove any site by deleting or commenting out its line.
For private sites or repos, you may need authentication tokens/cookies to see content that’s not public.

Output Structure
After a successful run, you’ll see:


scraped_docs/
  ├─ developers_flow_com/
  │   ├─ index.md
  │   ├─ docs_tutorial_somepage.md
  │   └─ ...
  ├─ github_com_onflow_flow_ft/
  │   ├─ blob_main_contracts_exampletoken_cdc.md
  │   ├─ ...
  ├─ github_com_orgs_onflow_discussions/
  │   ├─ discussion_1330.md
  │   ├─ discussion_1514.md
  │   └─ ...
  └─ ...

Docs directories for each site
Repos with code files in .md (wrapped code blocks)
Discussions as discussion_<id>.md, each containing Q&A text.

