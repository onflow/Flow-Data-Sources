# Source: https://developers.flow.com/tutorials/ai-plus-flow/chatgpt

Use Flow Knowledge Base in ChatGPT | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [AI Plus Flow](/tutorials/ai-plus-flow)

  + [Use Cursor AI](/tutorials/ai-plus-flow/cursor)
  + [Use ChatGPT](/tutorials/ai-plus-flow/chatgpt)
  + [Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)
* [AI Guides](/tutorials/AI Guides/agentkit-flow-guide)

* [AI Plus Flow](/tutorials/ai-plus-flow)
* Use ChatGPT

On this page

# Use Flow Knowledge Base in ChatGPT

[ChatGPT](https://chatgpt.com/) is an AI assistant developed by [OpenAI](https://openai.com/) that can help with tasks such as writing, coding, and answering questions. It adapts to context and user input to provide relevant, conversational responses. ChatGPT can be integrated into developer tools or workflows to assist with documentation, debugging, and productivity.

This guide walks you through creating a **Custom GPT** using ChatGPT that can reference the [Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources) file to answer questions.

warning

You'll need a [ChatGPT Plus subscription](https://chat.openai.com) to use the **Custom GPT** feature.

## 📍 Step 1: Open the "Explore GPTs" Section[​](#-step-1-open-the-explore-gpts-section "Direct link to 📍 Step 1: Open the \"Explore GPTs\" Section")

1. Log in to [ChatGPT](https://chatgpt.com/).
2. In the sidebar on the left, click **Explore GPTs**.

![explore gpts](/assets/images/explore-gpts-561d873a639fdf85eef2e6e1846bf7e6.png)

---

## 📍 Step 2: Click "Create a GPT"[​](#-step-2-click-create-a-gpt "Direct link to 📍 Step 2: Click \"Create a GPT\"")

1. In the **Explore GPTs** screen, click the **"Create"** button in the top-right corner.

![create](data:image/png;base64,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)

---

## 📍 Step 3: Walk Through the GPT Builder[​](#-step-3-walk-through-the-gpt-builder "Direct link to 📍 Step 3: Walk Through the GPT Builder")

ChatGPT will now guide you through a conversation to set up your custom GPT. First, drag and drop the [Flow Data Sources All Merged](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md) file into the prompt.

### Suggested Prompt[​](#suggested-prompt "Direct link to Suggested Prompt")

`_10

I want to make a GPT called FlowGPT that uses the linked file as it's primary source. This file changes, so it should reference the live file at least once a day: https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md`

---

## 📍 Step 4: Configure the GPT's Name and Instructions[​](#-step-4-configure-the-gpts-name-and-instructions "Direct link to 📍 Step 4: Configure the GPT's Name and Instructions")

ChatGPT may ask you to customize or verify:

* **Name and description** of your GPT
* **Instructions**: Tell it how to behave and what to prioritize (e.g., always reference the uploaded document)
* **Capabilities**: Enable file browsing, code interpreter, or DALL·E if needed

We've found it helpful to suggest:

`_10

Please imagine you are a fast and smart junior developer who is eager to help and has memorized all the information in the linked file`

Please let us know if you find any other useful customization prompts!

---

## 📍 Step 5: Test Your GPT[​](#-step-5-test-your-gpt "Direct link to 📍 Step 5: Test Your GPT")

Once the GPT is built, you'll be taken to a preview chat window. Test it by asking a few questions based on your uploaded document.

---

## 📍 Step 6: Save and Publish (Optional)[​](#-step-6-save-and-publish-optional "Direct link to 📍 Step 6: Save and Publish (Optional)")

When you're ready:

* Click **"Update & Save"** to finalize
* You can choose to keep it **private** or make it **public**

---

## ✅ That's it![​](#-thats-it "Direct link to ✅ That's it!")

You've now created a custom GPT that references your uploaded file as a primary source. You can update the file or instructions later if needed.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/ai-plus-flow/chatgpt/index.md)

Last updated on **Apr 3, 2025** by **Brian Doyle**

[Previous

Use Cursor AI](/tutorials/ai-plus-flow/cursor)[Next

Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources)

###### Rate this page

😞😐😊

* [📍 Step 1: Open the "Explore GPTs" Section](#-step-1-open-the-explore-gpts-section)
* [📍 Step 2: Click "Create a GPT"](#-step-2-click-create-a-gpt)
* [📍 Step 3: Walk Through the GPT Builder](#-step-3-walk-through-the-gpt-builder)
  + [Suggested Prompt](#suggested-prompt)
* [📍 Step 4: Configure the GPT's Name and Instructions](#-step-4-configure-the-gpts-name-and-instructions)
* [📍 Step 5: Test Your GPT](#-step-5-test-your-gpt)
* [📍 Step 6: Save and Publish (Optional)](#-step-6-save-and-publish-optional)
* [✅ That's it!](#-thats-it)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.