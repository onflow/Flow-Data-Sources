# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Codex, Cursor, Copilot, and others)
when working in this repository. It is loaded into agent context automatically — keep it concise.

## Overview

Flow-Data-Sources is a Python scraper that crawls Flow ecosystem documentation sites, GitHub
repositories, and GitHub org discussions, converting them to Markdown for use in RAG pipelines,
chatbots, and other AI knowledge bases. A GitHub Actions workflow runs the scraper daily at
00:00 UTC and commits the refreshed output back to the repo.

## Build and Test Commands

Setup (Python 3.7+ per README; CI uses 3.9 in `.github/workflows/scrape-and-push.yml`):

- `pip install requests beautifulsoup4 markdownify` — install the three runtime dependencies

Run:

- `python scraper.py` — crawl every URL in `SITES` (scraper.py:12) and write Markdown to `scraped_docs/`
- `python merge.py` — produce three files in `merged_docs/`: `all_merged.md`, `essentials_merged.md`, `cadence_docs_merged.md`

There is no Makefile, no test suite, and no linter configured.

## Architecture

- `scraper.py` — single-file crawler with three modes, dispatched by `crawl_site()` (scraper.py:392):
  - Normal sites (non-GitHub): domain-limited BFS, HTML stripped of `<script>/<style>/<noscript>`, converted via `markdownify`
  - GitHub repos: walks `/tree/(main|master)/...` and `/blob/(main|master)/...`, downloads files via `raw.githubusercontent.com`, wraps non-Markdown files in triple backticks
  - GitHub org discussions (`/orgs/<org>/discussions`): paginates listing, scrapes each thread to `discussion_<id>.md`
- `merge.py` — walks `scraped_docs/` and produces three merged outputs; folder allowlists `CADENCE_DOCS` (merge.py:11) and `ESSENTIALS` (merge.py:70) control which dirs feed the filtered merges
- `scraped_docs/` — per-site output directories named by `sanitize_folder_name()` (scraper.py:95) (e.g., `github_com_onflow_flow_ft/`)
- `merged_docs/` — final merged artifacts consumed downstream
- `.github/workflows/scrape-and-push.yml` — daily cron (`0 0 * * *`) that installs deps, runs `scraper.py` then `merge.py`, and `git add -A && git push`

## Conventions and Gotchas

- Edit the site list in `scraper.py` at the `SITES` constant (scraper.py:12). Watch the trailing entries: `"https://github.com/fixes-world/fixes"` at scraper.py:67 is missing a trailing comma, so Python implicitly concatenates it with the discussions URL on scraper.py:71 — fix this before adding new entries between them
- `scrape_github_file_blob()` (scraper.py:210) only saves files whose extension is in `ALLOWED_EXTENSIONS = {".cdc", ".md", ".sol"}` (scraper.py:81) or whose basename contains `readme`; the filter itself is at scraper.py:223
- BFS is bounded: `MAX_PAGES_PER_SITE = 200` per site (scraper.py:75) and `MAX_DISCUSSION_THREADS = 500` for the discussions crawl (scraper.py:85)
- Non-`.md` files are wrapped in triple backticks before being saved (scraper.py:234) so merged output keeps code blocks intact; do not double-wrap when adding new handlers
- `merge.py` emits a literal `------------ FILE_DIVIDER ------------` separator between files (merge.py:97); downstream consumers rely on this marker
- `merge.py` `CADENCE_DOCS` / `ESSENTIALS` lists use sanitized folder names (lowercase, non-alphanumerics collapsed to `_`, per `sanitize_folder_name()` at scraper.py:95). When adding a site to `SITES`, run the scraper once and copy the exact folder name from `scraped_docs/` before adding it to these lists
- The daily workflow runs `git add -A` on `ubuntu-latest` — any untracked file in the repo root will be committed by CI

## Files Not to Modify

- `scraped_docs/` — regenerated every run of `scraper.py`
- `merged_docs/` — regenerated every run of `merge.py`
