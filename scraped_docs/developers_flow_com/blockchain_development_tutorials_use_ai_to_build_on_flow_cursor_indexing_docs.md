# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs

Indexing Flow Documentation in Cursor | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

          + [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

            - [Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources)- [Indexing Documentation](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs)- [Cadence Rules](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/cadence-rules)+ [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)

              + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)* Indexing Documentation

On this page

# Indexing Flow Documentation in Cursor

[Cursor](https://www.cursor.com/) is an AI code editor that makes it easy to write code while building Flow apps. To get the most accurate and helpful responses when developing Flow applications, you need to index the relevant Flow documentation within Cursor. This guide walks you through how to set up comprehensive Flow knowledge in your Cursor environment.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Cursor](https://www.cursor.com/) installed on your system.
* Active internet connection for documentation indexing.
* Cursor Pro subscription (recommended for full documentation access).

## Documentation sources[​](#documentation-sources "Direct link to Documentation sources")

For optimal Flow development assistance, you'll want to index three key documentation sources:

1. **Flow Developer Documentation** - Official Flow blockchain and tooling documentation.
2. **Cadence Language Documentation** - Complete Cadence programming language reference.
3. **Flow Data Sources** - Comprehensive, auto-generated knowledge base with current practices.

## Installation steps[​](#installation-steps "Direct link to Installation steps")

### Step 1: Access documentation settings[​](#step-1-access-documentation-settings "Direct link to Step 1: Access documentation settings")

1. Open Cursor and navigate to **Settings** (or press `Cmd/Ctrl + ,`).
2. Go to **Features > Docs**.
3. Click **"+ Add new doc"** to add documentation sources.

![Cursor Settings](/assets/images/use-cursor-1-4c5b9bc11a4106f1ca259b60faa6e871.png)

### Step 2: Add Flow developer documentation[​](#step-2-add-flow-developer-documentation "Direct link to Step 2: Add Flow developer documentation")

1. In the URL field, enter: `https://developers.flow.com/tools`
   * **Note**: Use the `/tools` endpoint as it properly indexes all Flow documentation.
   * Cursor will automatically detect and crawl the entire Flow documentation site.
2. Set the name as **"Flow"**.
3. Click **"Confirm"** to add the documentation.
4. Wait for the indexing process to complete.

![Cursor Settings](/assets/images/use-cursor-2-40225d578bab288f66abe1221315b89d.png)

### Step 3: Add Cadence language documentation[​](#step-3-add-cadence-language-documentation "Direct link to Step 3: Add Cadence language documentation")

1. Click **"+ Add new doc"** again.
2. Enter the Cadence documentation URL: `https://cadence-lang.org/docs/`
3. Set the name as **"Cadence"**.
4. Click **"Confirm"** to add the documentation.
5. Allow time for indexing to complete.

### Step 4: Add Flow data sources[​](#step-4-add-flow-data-sources "Direct link to Step 4: Add Flow data sources")

1. Click **"+ Add new doc"** again.
2. Enter the Flow Data Sources URL: `https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md`
3. Set the name as **"Flow Data Sources"**.
4. Click **"Confirm"** to add the documentation.

caution

Resource Requirements

The Flow Data Sources file is very large and comprehensive. For older development machines or those with limited resources, we recommend you use the [essentials merged file](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md) instead:
`https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md`

### Step 5: Verify indexing[​](#step-5-verify-indexing "Direct link to Step 5: Verify indexing")

1. Monitor the indexing progress in the **Docs** section of Cursor settings.
2. Wait for all three documentation sources to show as "Indexed" or "Ready."
3. Indexing time varies, and depends on your internet connection and system performance.

## Use indexed documentation[​](#use-indexed-documentation "Direct link to Use indexed documentation")

After indexing finishes, you can reference the documentation in your Cursor prompts:

### Reference syntax[​](#reference-syntax "Direct link to Reference syntax")

* `@Flow` - Reference Flow developer documentation.
* `@Cadence` - Reference Cadence language documentation.
* `@Flow Data Sources` - Reference the comprehensive Flow knowledge base.

![Cursor Settings](/assets/images/use-cursor-3-ee338cc36953ea4ae1fe236ba9c1a9a5.png)

### Example usage[​](#example-usage "Direct link to Example usage")

`_10

@Flow How do I deploy a contract to Flow Testnet?

_10

_10

@Cadence What's the syntax for how to create a resource in Cadence?

_10

_10

@Flow Data Sources How do I implement a marketplace for NFTs with royalties?`

## Best practices[​](#best-practices "Direct link to Best practices")

### When to use each source[​](#when-to-use-each-source "Direct link to When to use each source")

* **@Flow**: Use for Flow-specific concepts, tools, CLI commands, network information, and ecosystem questions.
* **@Cadence**: Use for Cadence programming language syntax, features, patterns, and code examples.
* **@Flow Data Sources**: Use for complex questions, advanced patterns, comprehensive tutorials, or when other sources don't provide satisfactory results.

### Prompt optimization[​](#prompt-optimization "Direct link to Prompt optimization")

* **Be Specific**: Detailed prompts yield more accurate and relevant responses.
* **Combine Sources**: Use multiple references for cross-VM applications (`@Flow` and `@Cadence`).
* **Context Matters**: Include relevant project context in your prompts.
* **Verify Results**: Use documentation to validate AI-generated code and ensure best practices.

### Example combined usage[​](#example-combined-usage "Direct link to Example combined usage")

`_10

Using @Flow and @Cadence, help me create a transaction that deploys an NFT contract and mints the first token, then show me how to call this from a React app using FCL.`

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Common issues and solutions[​](#common-issues-and-solutions "Direct link to Common issues and solutions")

**Documentation Not Indexed**:

* Verify all URLs are correct and accessible.
* Check your internet connection stability.
* Try to re-add the documentation source.

**Outdated Information**:

* Remove and re-add sources to refresh documentation.
* Clear Cursor's cache if available in settings.
* Update to the latest version of Cursor.

**Slow or Failed Indexing**:

* Verify stable internet connection.
* Try to index during off-peak hours.
* For Flow Data Sources, switch to the essentials merged file if needed.

**Inaccurate AI Responses**:

* Verify the documentation sources are properly indexed.
* Try more specific prompts with clear context.
* Cross-reference responses with official documentation.

### Get Help[​](#get-help "Direct link to Get Help")

If you continue to experience issues:

1. Check the [Cursor documentation](https://docs.cursor.com/) for additional troubleshooting steps.
2. Verify that all documentation URLs are accessible in your browser.
3. Contact Cursor support through their official channels.
4. Consider an alternative documentation sources if specific URLs are problematic.

## Maintain your setup[​](#maintain-your-setup "Direct link to Maintain your setup")

### Regular maintenance[​](#regular-maintenance "Direct link to Regular maintenance")

* **Refresh Periodically**: Re-index documentation monthly to ensure current information.
* **Monitor Updates**: Stay aware of major Flow or Cadence documentation updates.
* **Clean Up**: Remove unused documentation sources to improve performance.

### Team collaboration[​](#team-collaboration "Direct link to Team collaboration")

For development teams:

* Share the same documentation configuration across team members.
* Document your specific setup in your project README.
* Consider creating team-specific documentation sources for internal patterns and practices.

If you follow this setup guide, you'll have comprehensive Flow and Cadence documentation available directly within Cursor, which allows more accurate AI assistance and faster development workflows.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs.md)

Last updated on **Nov 20, 2025** by **cshannon1218**

[Previous

Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources)[Next

Cadence Rules](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/cadence-rules)

###### Rate this page

😞😐😊

Copy as Markdown

* [Prerequisites](#prerequisites)* [Documentation sources](#documentation-sources)* [Installation steps](#installation-steps)
      + [Step 1: Access documentation settings](#step-1-access-documentation-settings)+ [Step 2: Add Flow developer documentation](#step-2-add-flow-developer-documentation)+ [Step 3: Add Cadence language documentation](#step-3-add-cadence-language-documentation)+ [Step 4: Add Flow data sources](#step-4-add-flow-data-sources)+ [Step 5: Verify indexing](#step-5-verify-indexing)* [Use indexed documentation](#use-indexed-documentation)
        + [Reference syntax](#reference-syntax)+ [Example usage](#example-usage)* [Best practices](#best-practices)
          + [When to use each source](#when-to-use-each-source)+ [Prompt optimization](#prompt-optimization)+ [Example combined usage](#example-combined-usage)* [Troubleshooting](#troubleshooting)
            + [Common issues and solutions](#common-issues-and-solutions)+ [Get Help](#get-help)* [Maintain your setup](#maintain-your-setup)
              + [Regular maintenance](#regular-maintenance)+ [Team collaboration](#team-collaboration)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.