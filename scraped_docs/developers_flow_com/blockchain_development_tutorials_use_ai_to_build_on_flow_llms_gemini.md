# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini

Use Flow Knowledge Base in Gemini AI | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Forte Network Upgrade](/blockchain-development-tutorials/forte)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

  + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

    - [Use ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)
    - [Use Gemini AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini)
    - [Claude Code Flow Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)
  + [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)
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
* [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)
* Use Gemini AI

On this page

# Use Flow Knowledge Base in Gemini AI

[Gemini AI](https://gemini.google.com/) is Google's AI assistant that can help with tasks such as writing, coding, and answering questions. It adapts to context and user input to provide relevant, conversational responses. Gemini AI can be integrated into developer workflows to assist with documentation, debugging, and productivity.

This guide walks you through creating a **Custom GEM** using Gemini AI that can reference the [Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources) file to answer questions.

warning

You'll need a [Gemini Advanced subscription](https://gemini.google.com/advanced) to use the **Custom GEM** feature.

## Step 1: Access Gem Manager[​](#step-1-access-gem-manager "Direct link to Step 1: Access Gem Manager")

1. Log in to [Gemini AI](https://gemini.google.com/)
2. In the sidebar on the left click on **Explore Gems**

---

## Step 2: Create a New Gem[​](#step-2-create-a-new-gem "Direct link to Step 2: Create a New Gem")

1. In the **Gem Manager** screen, click the **"New Gem"** button.

---

## Step 3: Configure Your Gem[​](#step-3-configure-your-gem "Direct link to Step 3: Configure Your Gem")

Gemini AI will now guide you through setting up your custom Gem. Configure the name, description and instructions for your GEM to follow.

### Suggested Configuration[​](#suggested-configuration "Direct link to Suggested Configuration")

**Name**: FlowGem

**Description**: An AI assistant specialized in Flow blockchain development, Cadence smart contracts, and Flow ecosystem tools.

**Instructions**:

`_11

_11

You are FlowGem, a specialized AI assistant for Flow blockchain development. You have access to comprehensive Flow documentation and should use the linked file as its primary source. This file changes, so it should reference the live file at least once a day: https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md

_11

_11

Key behaviors:

_11

- Always reference the uploaded Flow documentation when answering questions

_11

- Provide practical, actionable advice for Flow developers

_11

- Include relevant code examples when applicable

_11

- Stay up-to-date with the latest Flow ecosystem developments

_11

- Be eager to help and imagine you are a knowledgeable Flow developer

_11

_11

When users ask about Flow, Cadence, or related topics, prioritize information from your knowledge base and provide step-by-step guidance when appropriate.`

You can further customize your personalized agent by providing more files and determining the actions it can do.

---

## Step 4: Upload Knowledge Base[​](#step-4-upload-knowledge-base "Direct link to Step 4: Upload Knowledge Base")

1. In the **Knowledge** section, upload the [Flow Data Sources All Merged](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md) file
2. Configure the Gem to reference this file as its primary knowledge source

---

## Step 5: Test Your Gem[​](#step-5-test-your-gem "Direct link to Step 5: Test Your Gem")

Once the Gem is configured, test it by asking Flow-related questions:

* "How do I deploy a smart contract to Flow Testnet?"
* "What's the syntax for Cadence resources?"
* "How do I set up Flow CLI?"

---

## Step 6: Save and Deploy[​](#step-6-save-and-deploy "Direct link to Step 6: Save and Deploy")

When you're satisfied with the performance:

* Click **"Create Gem"** to finalize
* Your Gem will be available in your Gem Manager
* You can share it with your team or keep it private

---

## Conclusion[​](#conclusion "Direct link to Conclusion")

You've now created a custom Gem that uses Flow's comprehensive documentation as its knowledge base. Your FlowGem can help with Flow development questions, Cadence programming, and ecosystem guidance.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Use ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)[Next

Claude Code Flow Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)

###### Rate this page

😞😐😊

Copy as Markdown

* [Step 1: Access Gem Manager](#step-1-access-gem-manager)
* [Step 2: Create a New Gem](#step-2-create-a-new-gem)
* [Step 3: Configure Your Gem](#step-3-configure-your-gem)
  + [Suggested Configuration](#suggested-configuration)
* [Step 4: Upload Knowledge Base](#step-4-upload-knowledge-base)
* [Step 5: Test Your Gem](#step-5-test-your-gem)
* [Step 6: Save and Deploy](#step-6-save-and-deploy)
* [Conclusion](#conclusion)

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