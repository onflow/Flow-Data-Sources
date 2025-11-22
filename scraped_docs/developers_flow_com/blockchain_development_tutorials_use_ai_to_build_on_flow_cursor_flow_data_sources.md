# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources

Flow Data Sources | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)* Flow Data Sources

On this page

# Flow Data Sources

Flow Data Sources is a comprehensive repository that automatically aggregates and formats Flow ecosystem content into Markdown files optimized for AI ingestion. This resource serves as a centralized knowledge base for AI tools, chatbots, and RAG (Retrieval-Augmented Generation) pipelines. It contains the most current documentation, examples, and best practices for Flow blockchain development.

## Overview[​](#overview "Direct link to Overview")

The repository contains Python scripts that:

* Crawl Flow-related documentation sites, GitHub repositories, and discussions.
* Convert HTML content to Markdown format.
* Extract code examples from GitHub repositories.
* Capture community discussions and Q&A content.
* Merge all content into consolidated files for easy consumption.

Flow Data Sources automatically pulls content from:

* Official Flow documentation
* Cadence language documentation
* Flow CLI guides
* FCL (Flow Client Library) documentation
* Smart contract examples and tutorials
* Best practices and development patterns
* Community discussions and Q&A content

## Key features[​](#key-features "Direct link to Key features")

* **Daily Updates**: Content is automatically refreshed to ensure the latest information.
* **Structured Format**: All content is converted to Markdown for consistent processing.
* **Comprehensive Coverage**: Includes official documentation, code examples, and community discussions.
* **Optimized for AI**: Designed specifically for AI tools, chatbots, and RAG pipelines.

## Available files[​](#available-files "Direct link to Available files")

The repository provides several merged documentation files optimized for different use cases:

**Output options:**

* [All Merged Content](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md): Complete content
* [Essentials Only](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md): Streamlined version that only include official documentation and sample codes
* [Cadence Only](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/cadence_docs_merged.md): Streamlined version that only includex Cadence related documentation and sample codes

### All merged documentation[​](#all-merged-documentation "Direct link to All merged documentation")

* **File**: `all_merged.md`
* **Content**: Complete comprehensive documentation that covers all aspects of Flow development.
* **Use Case**: Most comprehensive knowledge base for AI tools and complex development questions.
* **Size**: Very large file - may require powerful systems to process.
* **Documentation**: [All Merged Content](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md)

### Essentials merged documentation[​](#essentials-merged-documentation "Direct link to Essentials merged documentation")

* **File**: `essentials_merged.md`
* **Content**: Core Flow and Cadence development essentials.
* **Use Case**: Lighter alternative for systems with resource constraints.
* **Size**: Smaller, more focused content for essential development needs.
* **Documentation**: [Essentials Only](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md)

### Cadence only documentation[​](#cadence-only-documentation "Direct link to Cadence only documentation")

* **File**: `cadence_docs_merged.md`
* **Content**: Streamlined version that only includes Cadence related documentation and sample codes.
* **Use Case**: Focused on Cadence language development and smart contracts.
* **Size**: Cadence-specific content for specialized development needs.
* **Documentation**: [Cadence Only](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/cadence_docs_merged.md)

## How to use[​](#how-to-use "Direct link to How to use")

You can integrate Flow Data Sources with:

* **ChatGPT Plugins**: Enhance Q&A capabilities with Flow-specific knowledge.
* **Custom Chatbots**: Power Discord and Telegram bots with accurate Flow information.
* **RAG Systems**: Index content in vector databases for semantic search.
* **Development Tools**: Provide context-aware assistance in IDEs like Cursor.

## Integration with AI tools[​](#integration-with-ai-tools "Direct link to Integration with AI tools")

Flow Data Sources is specifically designed to work seamlessly with various AI development tools:

### [Cursor Integration](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs)[​](#cursor-integration "Direct link to cursor-integration")

To add Flow Data Sources to your Cursor documentation, reference the GitHub URL directly. This provides your AI assistant with up-to-date Flow knowledge.

### [ChatGPT Custom GPTs](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)[​](#chatgpt-custom-gpts "Direct link to chatgpt-custom-gpts")

Upload the merged documentation files to create specialized Flow development assistants that can answer complex questions about Cadence, Flow CLI, and ecosystem tools.

### [Claude Code Integration](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)[​](#claude-code-integration "Direct link to claude-code-integration")

Reference Flow Data Sources in your CLAUDE.md files to ensure persistent, comprehensive Flow knowledge across all development sessions.

## Key Benefits[​](#key-benefits "Direct link to Key Benefits")

**Always Current**: Automatically updated to reflect the latest Flow ecosystem changes and documentation updates.

**Comprehensive Coverage**: Includes documentation from all major Flow development tools and resources in one place.

**AI-Optimized Format**: Structured specifically for optimal AI processing and accurate response generation.

**Multiple Formats**: Different file sizes to accommodate various system requirements and use cases.

**Community Driven**: Benefits from contributions across the entire Flow developer ecosystem.

## Best Practices[​](#best-practices "Direct link to Best Practices")

**Choose the Right File**: Use `all_merged.md` for comprehensive coverage or `essentials_merged.md` for lighter integration.

**Regular Updates**: Since the files are continuously updated, refresh your AI tool's knowledge base periodically.

**Combine with Live Docs**: Use Flow Data Sources alongside live documentation links for the most complete development assistance.

**Verify Critical Information**: While highly accurate, always verify critical implementation details against official sources.

## Accessing the Content[​](#accessing-the-content "Direct link to Accessing the Content")

The merged documentation files are available at:

* [All Merged Content](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md)
* [Essentials Only](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md)
* [Cadence Only](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/cadence_docs_merged.md)

For integration with AI tools like Cursor or ChatGPT, use the appropriate URL as described in the respective tutorials.

## Get Started[​](#get-started "Direct link to Get Started")

1. **Identify Your Use Case**: Determine whether you need comprehensive or essential documentation coverage
2. **Choose Your AI Tool**: Select the AI platform you want to integrate with Flow Data Sources
3. **Follow Integration Guides**: Use the specific tutorial for your chosen AI tool (ChatGPT, Gemini, Cursor, Claude Code, and so on.)
4. **Test and Validate**: Ask Flow-specific development questions to verify that the integration works.

The Flow Data Sources repository represents a powerful resource to enhance AI-assisted Flow development, and provides comprehensive and current knowledge that adapts to the rapidly evolving Flow ecosystem.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources.md)

Last updated on **Nov 20, 2025** by **cshannon1218**

[Previous

Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)[Next

Indexing Documentation](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/indexing-docs)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Key features](#key-features)* [Available files](#available-files)
      + [All merged documentation](#all-merged-documentation)+ [Essentials merged documentation](#essentials-merged-documentation)+ [Cadence only documentation](#cadence-only-documentation)* [How to use](#how-to-use)* [Integration with AI tools](#integration-with-ai-tools)
          + [Cursor Integration](#cursor-integration)+ [ChatGPT Custom GPTs](#chatgpt-custom-gpts)+ [Claude Code Integration](#claude-code-integration)* [Key Benefits](#key-benefits)* [Best Practices](#best-practices)* [Accessing the Content](#accessing-the-content)* [Get Started](#get-started)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.