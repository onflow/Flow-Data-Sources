# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs

Indexing Flow Documentation in Cursor | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Forte Network Upgrade](/blockchain-development-tutorials/forte)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

  + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)
  + [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

    - [Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources)
    - [Indexing Documentation](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs)
    - [Cadence Rules](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/cadence-rules)
  + [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)
  + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)
* Indexing Documentation

On this page

# Indexing Flow Documentation in Cursor

[Cursor](https://www.cursor.com/) is an AI code editor that makes it easy to write code while building Flow apps. To get the most accurate and helpful responses when developing Flow applications, you need to index the relevant Flow documentation within Cursor. This guide walks you through setting up comprehensive Flow knowledge in your Cursor environment.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Cursor](https://www.cursor.com/) installed on your system
* Active internet connection for documentation indexing
* Cursor Pro subscription (recommended for full documentation access)

## Documentation Sources[​](#documentation-sources "Direct link to Documentation Sources")

For optimal Flow development assistance, you'll want to index three key documentation sources:

1. **Flow Developer Documentation** - Official Flow blockchain and tooling documentation
2. **Cadence Language Documentation** - Complete Cadence programming language reference
3. **Flow Data Sources** - Comprehensive, auto-generated knowledge base with current practices

## Installation Steps[​](#installation-steps "Direct link to Installation Steps")

### Step 1: Access Documentation Settings[​](#step-1-access-documentation-settings "Direct link to Step 1: Access Documentation Settings")

1. Open Cursor and navigate to **Settings** (or press `Cmd/Ctrl + ,`)
2. Go to **Features > Docs**
3. Click **"+ Add new doc"** to begin adding documentation sources

![Cursor Settings](/assets/images/use-cursor-1-4c5b9bc11a4106f1ca259b60faa6e871.png)

### Step 2: Add Flow Developer Documentation[​](#step-2-add-flow-developer-documentation "Direct link to Step 2: Add Flow Developer Documentation")

1. In the URL field, enter: `https://developers.flow.com/tools`
   * **Note**: Use the `/tools` endpoint as it properly indexes all Flow documentation
   * Cursor will automatically detect and crawl the entire Flow documentation site
2. Set the name as **"Flow"**
3. Click **"Confirm"** to add the documentation
4. Wait for the indexing process to complete

![Cursor Settings](/assets/images/use-cursor-2-40225d578bab288f66abe1221315b89d.png)

### Step 3: Add Cadence Language Documentation[​](#step-3-add-cadence-language-documentation "Direct link to Step 3: Add Cadence Language Documentation")

1. Click **"+ Add new doc"** again
2. Enter the Cadence documentation URL: `https://cadence-lang.org/docs/`
3. Set the name as **"Cadence"**
4. Click **"Confirm"** to add the documentation
5. Allow time for indexing to complete

### Step 4: Add Flow Data Sources[​](#step-4-add-flow-data-sources "Direct link to Step 4: Add Flow Data Sources")

1. Click **"+ Add new doc"** once more
2. Enter the Flow Data Sources URL: `https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md`
3. Set the name as **"Flow Data Sources"**
4. Click **"Confirm"** to add the documentation

Resource Requirements

The Flow Data Sources file is very large and comprehensive. For older development machines or those with limited resources, consider using the [essentials merged file](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md) instead:
`https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md`

### Step 5: Verify Indexing[​](#step-5-verify-indexing "Direct link to Step 5: Verify Indexing")

1. Monitor the indexing progress in the **Docs** section of Cursor settings
2. Wait for all three documentation sources to show as "Indexed" or "Ready"
3. Indexing time varies depending on your internet connection and system performance

## Using Indexed Documentation[​](#using-indexed-documentation "Direct link to Using Indexed Documentation")

Once indexing is complete, you can reference the documentation in your Cursor prompts:

### Reference Syntax[​](#reference-syntax "Direct link to Reference Syntax")

* `@Flow` - Reference Flow developer documentation
* `@Cadence` - Reference Cadence language documentation
* `@Flow Data Sources` - Reference the comprehensive Flow knowledge base

![Cursor Settings](/assets/images/use-cursor-3-ee338cc36953ea4ae1fe236ba9c1a9a5.png)

### Example Usage[​](#example-usage "Direct link to Example Usage")

`_10

@Flow How do I deploy a contract to Flow Testnet?

_10

_10

@Cadence What's the syntax for creating a resource in Cadence?

_10

_10

@Flow Data Sources How do I implement a marketplace for NFTs with royalties?`

## Best Practices[​](#best-practices "Direct link to Best Practices")

### When to Use Each Source[​](#when-to-use-each-source "Direct link to When to Use Each Source")

* **@Flow**: Use for Flow-specific concepts, tools, CLI commands, network information, and ecosystem questions
* **@Cadence**: Use for Cadence programming language syntax, features, patterns, and code examples
* **@Flow Data Sources**: Use for complex questions, advanced patterns, comprehensive tutorials, or when other sources don't provide satisfactory results

### Prompt Optimization[​](#prompt-optimization "Direct link to Prompt Optimization")

* **Be Specific**: Detailed prompts yield more accurate and relevant responses
* **Combine Sources**: Use multiple references for cross-VM applications (`@Flow` and `@Cadence`)
* **Context Matters**: Include relevant project context in your prompts
* **Verify Results**: Use documentation to validate AI-generated code and ensure best practices

### Example Combined Usage[​](#example-combined-usage "Direct link to Example Combined Usage")

`_10

Using @Flow and @Cadence, help me create a transaction that deploys an NFT contract and mints the first token, then show me how to call this from a React app using FCL.`

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Common Issues and Solutions[​](#common-issues-and-solutions "Direct link to Common Issues and Solutions")

**Documentation Not Indexed**:

* Verify all URLs are correct and accessible
* Check your internet connection stability
* Try re-adding the documentation source

**Outdated Information**:

* Refresh documentation by removing and re-adding sources
* Clear Cursor's cache if available in settings
* Update to the latest version of Cursor

**Slow or Failed Indexing**:

* Ensure stable internet connection
* Try indexing during off-peak hours
* For Flow Data Sources, switch to the essentials merged file if needed

**Inaccurate AI Responses**:

* Verify the documentation sources are properly indexed
* Try more specific prompts with clear context
* Cross-reference responses with official documentation

### Getting Help[​](#getting-help "Direct link to Getting Help")

If you continue experiencing issues:

1. Check the [Cursor documentation](https://docs.cursor.com/) for additional troubleshooting steps
2. Verify that all documentation URLs are accessible in your browser
3. Contact Cursor support through their official channels
4. Consider using alternative documentation sources if specific URLs are problematic

## Maintaining Your Setup[​](#maintaining-your-setup "Direct link to Maintaining Your Setup")

### Regular Maintenance[​](#regular-maintenance "Direct link to Regular Maintenance")

* **Refresh Periodically**: Re-index documentation monthly to ensure current information
* **Monitor Updates**: Stay aware of major Flow or Cadence documentation updates
* **Clean Up**: Remove unused documentation sources to improve performance

### Team Collaboration[​](#team-collaboration "Direct link to Team Collaboration")

For development teams:

* Share the same documentation configuration across team members
* Document your specific setup in your project README
* Consider creating team-specific documentation sources for internal patterns and practices

By following this setup guide, you'll have comprehensive Flow and Cadence documentation available directly within Cursor, enabling more accurate AI assistance and faster development workflows.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources)[Next

Cadence Rules](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/cadence-rules)

###### Rate this page

😞😐😊

Copy as Markdown

* [Prerequisites](#prerequisites)
* [Documentation Sources](#documentation-sources)
* [Installation Steps](#installation-steps)
  + [Step 1: Access Documentation Settings](#step-1-access-documentation-settings)
  + [Step 2: Add Flow Developer Documentation](#step-2-add-flow-developer-documentation)
  + [Step 3: Add Cadence Language Documentation](#step-3-add-cadence-language-documentation)
  + [Step 4: Add Flow Data Sources](#step-4-add-flow-data-sources)
  + [Step 5: Verify Indexing](#step-5-verify-indexing)
* [Using Indexed Documentation](#using-indexed-documentation)
  + [Reference Syntax](#reference-syntax)
  + [Example Usage](#example-usage)
* [Best Practices](#best-practices)
  + [When to Use Each Source](#when-to-use-each-source)
  + [Prompt Optimization](#prompt-optimization)
  + [Example Combined Usage](#example-combined-usage)
* [Troubleshooting](#troubleshooting)
  + [Common Issues and Solutions](#common-issues-and-solutions)
  + [Getting Help](#getting-help)
* [Maintaining Your Setup](#maintaining-your-setup)
  + [Regular Maintenance](#regular-maintenance)
  + [Team Collaboration](#team-collaboration)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.