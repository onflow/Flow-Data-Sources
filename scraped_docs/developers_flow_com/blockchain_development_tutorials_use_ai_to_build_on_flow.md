# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow

Use AI To Build On Flow | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

          + [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

            + [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)

              + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * Use AI To Build On Flow

On this page

# Use AI To Build On Flow

Artificial Intelligence (AI) tools can significantly enhance your Flow development experience with intelligent assistance, code generation, and documentation access. This tutorial series will guide you through how to integrate various AI tools with Flow development to boost your productivity and code quality.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

In this tutorial series, you'll discover how to:

* Configure AI-powered development environments for Flow.
* Access Flow documentation directly from AI assistants.
* Generate Cadence and Solidity code with AI assistance.
* Debug and troubleshoot Flow applications with AI support.
* Leverage AI for testing and optimization.
* Build AI agents that interact with Flow using AgentKit.

# AI tutorials for Flow

## Use Claude Code with Flow[​](#use-claude-code-with-flow "Direct link to Use Claude Code with Flow")

Master systematic AI-powered Flow development with Claude Code, a terminal-integrated coding assistant designed for iterative blockchain development. This comprehensive guide teaches you to implement a four-stage development methodology (Idea → Visualization → Planning → Build) while you leverage unlimited context windows, subagent capabilities, and persistent project memory. Learn to configure `CLAUDE.md` files for Flow-specific instructions, integrate MCP servers for blockchain interactions, and implement checkpoint-based workflows that ensure reliable smart contract development from emulator to mainnet deployment.

Tutorial: [Claude Code for Flow Development](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)

## Use Cursor with Flow[​](#use-cursor-with-flow "Direct link to Use Cursor with Flow")

This guide details how you can set up the Cursor AI code editor with custom Flow knowledge bases, which transforms it into a specialized assistant to build powerful applications on the Flow network. When you provide the AI with direct access to the official Flow documentation, Cadence language references, and best-practice examples, you unlock a new tier of intelligent assistance that goes far beyond simple autocompletion

Tutorial: [Use Flow Knowledge Base in Cursor](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

## Use ChatGPT with Flow[​](#use-chatgpt-with-flow "Direct link to Use ChatGPT with Flow")

Build your own expert AI assistant and create a custom GPT specifically engineered to master the Flow blockchain and its Cadence smart contract language. This specialized tool will act as your personal pair programmer and provide highly accurate and context-aware answers to your most challenging development questions. By doing this, you don't just use a generic AI, you create a specialist trained on the exact documentation, code patterns, and best practices relevant to your work.

Tutorial: [Use Flow Knowledge Base in ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)

## Flow Data Sources[​](#flow-data-sources "Direct link to Flow Data Sources")

Learn about Flow Data Sources, a meticulously curated library designed to autonomously gather and structure information from the entire Flow ecosystem. This project systematically transforms a wide array of content into clean, AI-ready Markdown files, which establishes a unified source of truth. This collection acts as a foundational knowledge base, perfectly suited to power advanced applications such as custom chatbots and sophisticated Retrieval-Augmented Generation (RAG) systems.

Tutorial: [Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources)

## Eliza integration[​](#eliza-integration "Direct link to Eliza integration")

Learn about how to use Eliza on Flow, a versatile framework you can use to construct sophisticated AI agents that communicate with users through natural language. This guide walks you through how to configure and launch an AI agent built with Eliza directly onto the Flow blockchain. You'll discover how to engineer intelligent agents that can comprehend and address user prompts, all while you harness the power of Flow's inherently secure and scalable onchain infrastructure.

Tutorial: [Eliza on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza)

## Build AI agents with AgentKit[​](#build-ai-agents-with-agentkit "Direct link to Build AI agents with AgentKit")

Learn how to build AI agents on Flow with AgentKit, a versatile and modular developer toolkit that is not tied to any single platform. It's engineered to dramatically accelerate the process of building, deploying, and refining AI agents by supplying pre-configured environments and a library of ready-to-use templates. This guide walks you through how to launch your own custom agent on Flow's EVM-compatible testnet, which lets you leverage the powerful combination of the Langchain framework and Anthropic's Claude large language model.

Tutorial: [Build AI Agents with AgentKit](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/agentkit-flow-guide)

## MCP guides[​](#mcp-guides "Direct link to MCP guides")

Learn how to construct a custom Flow MCP (Model Context Protocol) server or use a current one to empower your AI tools. These tutorials guide you through how to equip your AI applications with the unique capability to directly interact with the Flow blockchain, which allows them to perform onchain operations and access real-time data.

Tutorial: [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)

## Cadence rules[​](#cadence-rules "Direct link to Cadence rules")

Learn how to establish and use Cursor Rules to transform your AI assistant into a dedicated Flow development expert. This process embeds your AI with persistent, foundational knowledge of essential topics, such as proper Cadence syntax, official NFT standards, project-specific configurations, and established development methodologies.

Tutorial: [Cadence Rules](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/cadence-rules)

## Best practices[​](#best-practices "Direct link to Best practices")

When you use AI tools with Flow development:

* Always verify AI-generated code against Flow documentation.
* Use specific prompts that reference Flow concepts and terminology.
* Combine AI assistance with your own knowledge of Flow architecture.
* Keep your AI tools updated with the latest Flow documentation.
* Test AI-generated code thoroughly before you deploy to production.
* Consider the security implications of AI agents that interact with your contracts.

## Next steps[​](#next-steps "Direct link to Next steps")

After you complete these tutorials, you'll be equipped to leverage AI tools effectively in your Flow development workflow. We recommend that you explore our other tutorial series to deepen your knowledge of Flow development:

* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps/introduction) - Build applications that integrate Flow EVM and Cadence.
* [Native VRF](/blockchain-development-tutorials/native-vrf) - Implement verifiable random functions in your applications.
* [Token Launch](/blockchain-development-tutorials/tokens) - Create and launch tokens on Flow.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Flow is the ideal platform for AI-enhanced blockchain development. The combination of Cadence's resource-oriented programming model, comprehensive AI ingestable documentation, and growing AI tooling support creates an unparalleled development experience. With tools like AgentKit, MCP servers, and AI-powered development environments, developers can build consumer applications faster than ever. This is why many believe that Flow is the best Blockchain to build on with AI.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/index.md)

Last updated on **Nov 20, 2025** by **cshannon1218**

[Previous

DeFi Math Utils](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)[Next

Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)* [Use Claude Code with Flow](#use-claude-code-with-flow)* [Use Cursor with Flow](#use-cursor-with-flow)* [Use ChatGPT with Flow](#use-chatgpt-with-flow)* [Flow Data Sources](#flow-data-sources)* [Eliza integration](#eliza-integration)* [Build AI agents with AgentKit](#build-ai-agents-with-agentkit)* [MCP guides](#mcp-guides)* [Cadence rules](#cadence-rules)* [Best practices](#best-practices)* [Next steps](#next-steps)* [Conclusion](#conclusion)

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