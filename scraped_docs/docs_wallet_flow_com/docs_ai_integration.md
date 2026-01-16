# Source: https://docs.wallet.flow.com/docs/ai-integration

🤖 AI Integration

[![Flow Wallet](/assets/logo.png?dpl=dpl_CvQvGN9652mUUTFzXgb4u7nfv4PK)Flow Wallet](/)

[![Flow Wallet](/assets/logo.png?dpl=dpl_CvQvGN9652mUUTFzXgb4u7nfv4PK)Flow Wallet](/)

Search

`⌘``K`

[👋 Welcome to Flow Wallet](/docs)

Ecosystem Primers

[📘 Flow Reference Wallet Primer](/docs/flow-reference-wallet-primer)

FAQ

[❓ FAQ](/docs/faq)

Features

Features

Ecosystem Development

Ecosystem Development

Download

[📲 Download](/docs/download)

Open Source

[💽 Open Source](/docs/open-source)

Tutorial

Tutorial

AI Integration

[🤖 AI Integration](/docs/ai-integration)

Other

[🔐 Wallet Revoke key guide](/docs/wallet-revoke-key-guide)

🤖 AI Integration

# 🤖 AI Integration

Documentation integration for AI assistants and language models

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ai-integration.mdx)

## [LLMs Integration](#llms-integration)

This documentation provides a special endpoint designed for AI assistants and large language models (LLMs) to easily discover and access our documentation.

### [AI-Friendly Documentation Index](#ai-friendly-documentation-index)

We provide a text-based index of all documentation pages that AI tools can fetch to understand the structure and content of this documentation.

**Endpoint:** [`/llms-full.txt`](/llms-full.txt)

This endpoint returns a plain text file containing:

* Page titles
* Page descriptions (when available)
* Direct URLs to each documentation page

### [How AI Assistants Use This](#how-ai-assistants-use-this)

AI assistants like Claude, ChatGPT, and other language models can:

1. Fetch the `/llms-full.txt` endpoint
2. Parse the list of available documentation pages
3. Direct users to relevant pages based on their questions
4. Provide accurate information about Flow Wallet features

### [Example Usage](#example-usage)

When a user asks an AI assistant about Flow Wallet features, the assistant can:

```
1. Check /llms-full.txt for available documentation
2. Find relevant pages (e.g., Account Linking, WalletConnect)
3. Provide direct links to specific documentation
4. Quote accurate information from the docs
```

### [For Developers](#for-developers)

If you're building an AI-powered tool or chatbot that needs to reference Flow Wallet documentation:

```
# Fetch the documentation index
curl https://your-docs-domain.com/llms-full.txt

# Or locally during development
curl http://localhost:3000/llms-full.txt
```

The format is simple and easy to parse:

```
# Page Title

Description (if available)

URL: /docs/page-path

---

# Next Page Title
...
```

### [Edit on GitHub](#edit-on-github)

All documentation pages include an "Edit on GitHub" button at the bottom, making it easy to contribute improvements or corrections to the documentation.

**Repository:** [github.com/Outblock/FRW-Doc](https://github.com/Outblock/FRW-Doc)

[📤 Mobile Wallet Export Log Guide

Previous Page](/docs/tutorial/mobile-wallet-export-log-guide)[🔐 Wallet Revoke key guide

Next Page](/docs/wallet-revoke-key-guide)

### On this page

[LLMs Integration](#llms-integration)[AI-Friendly Documentation Index](#ai-friendly-documentation-index)[How AI Assistants Use This](#how-ai-assistants-use-this)[Example Usage](#example-usage)[For Developers](#for-developers)[Edit on GitHub](#edit-on-github)