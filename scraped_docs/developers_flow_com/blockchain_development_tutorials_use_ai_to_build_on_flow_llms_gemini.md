# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini

Use Flow Knowledge Base in Gemini AI | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

          - [Use ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)- [Use Gemini AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini)- [Claude Code Flow Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)+ [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

            + [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)

              + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)* Use Gemini AI

On this page

# Use Flow Knowledge Base in Gemini AI

[Gemini AI](https://gemini.google.com/) is Google's AI assistant that can help with tasks such as writing, coding, and answering questions. It adapts to context and user input to provide relevant, conversational responses. You can integrate Gemini AI into developer workflows to assist with documentation, debugging, and productivity.

This guide walks you through creating a **Custom GEM** with Gemini AI that can reference the [Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor/flow-data-sources) file to answer questions.

warning

You'll need a [Gemini Advanced subscription](https://gemini.google.com/advanced) to use the **Custom GEM** feature.

## Step 1: Access Gem Manager[​](#step-1-access-gem-manager "Direct link to Step 1: Access Gem Manager")

1. Log in to [Gemini AI](https://gemini.google.com/).
2. In the sidebar on the left, click **Explore Gems**.

---

## Step 2: Create a new Gem[​](#step-2-create-a-new-gem "Direct link to Step 2: Create a new Gem")

1. In the **Gem Manager** screen, click **"New Gem"**.

---

## Step 3: Configure your Gem[​](#step-3-configure-your-gem "Direct link to Step 3: Configure your Gem")

Gemini AI will now guide you through setting up your custom Gem. Configure the name, description and instructions for your GEM to follow.

### Suggested configuration[​](#suggested-configuration "Direct link to Suggested configuration")

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

- Always reference the uploaded Flow documentation when answering questions.

_11

- Provide practical, actionable advice for Flow developers.

_11

- Include relevant code examples when applicable.

_11

- Stay up-to-date with the latest Flow ecosystem developments.

_11

- Be eager to help and imagine you are a knowledgeable Flow developer.

_11

_11

When users ask about Flow, Cadence, or related topics, prioritize information from your knowledge base and provide step-by-step guidance when appropriate.`

You can further customize your personalized agent by providing more files and determining the actions it can do.

---

## Step 4: Upload Knowledge Base[​](#step-4-upload-knowledge-base "Direct link to Step 4: Upload Knowledge Base")

1. In the **Knowledge** section, upload the [Flow Data Sources All Merged](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md) file.
2. Configure the Gem to reference this file as its primary knowledge source.

---

## Step 5: Test your Gem[​](#step-5-test-your-gem "Direct link to Step 5: Test your Gem")

After you configure the Gem, ask it Flow-related questions to test it:

* "How do I deploy a smart contract to Flow Testnet?"
* "What's the syntax for Cadence resources?"
* "How do I set up Flow CLI?"

---

## Step 6: Save and deploy[​](#step-6-save-and-deploy "Direct link to Step 6: Save and deploy")

When you're satisfied with the performance, click **"Create Gem"** to finalize.

* Your Gem will be available in your Gem Manager.
* You can share it with your team or keep it private.

---

## Conclusion[​](#conclusion "Direct link to Conclusion")

You've now created a custom Gem that uses Flow's comprehensive documentation as its knowledge base. Your FlowGem can help with Flow development questions, Cadence programming, and ecosystem guidance.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini.md)

Last updated on **Oct 30, 2025** by **cshannon1218**

[Previous

Use ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)[Next

Claude Code Flow Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)

###### Rate this page

😞😐😊

Copy as Markdown

* [Step 1: Access Gem Manager](#step-1-access-gem-manager)* [Step 2: Create a new Gem](#step-2-create-a-new-gem)* [Step 3: Configure your Gem](#step-3-configure-your-gem)
      + [Suggested configuration](#suggested-configuration)* [Step 4: Upload Knowledge Base](#step-4-upload-knowledge-base)* [Step 5: Test your Gem](#step-5-test-your-gem)* [Step 6: Save and deploy](#step-6-save-and-deploy)* [Conclusion](#conclusion)

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