# Source: https://developers.flow.com/tutorials/ai-plus-flow/cursor

Use Flow Knowledge Base in Cursor | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [AI Plus Flow](/tutorials/ai-plus-flow)

  + [Use Cursor AI](/tutorials/ai-plus-flow/cursor)
  + [Use ChatGPT](/tutorials/ai-plus-flow/chatgpt)
  + [Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources)
  + [Using AgentKit on Flow](/tutorials/ai-plus-flow/agentkit-flow-guide)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

* [AI Plus Flow](/tutorials/ai-plus-flow)
* Use Cursor AI

On this page

# Use Flow Knowledge Base in Cursor

[Cursor](https://www.cursor.com/) is an AI code editor that makes it easy to write code while building Flow apps. Let's walk through how to setup Cursor for the best possible experience when writing applications on Flow.

## Installation[​](#installation "Direct link to Installation")

Adding Flow docs lets you interact with our docs directly and get the most accurate answers to your questions.

1. Go to Cursor Settings > Features > Docs and click "+ Add new doc".

![Cursor Settings](/assets/images/use-cursor-1-4c5b9bc11a4106f1ca259b60faa6e871.png)

1. Set Flow Docs:

* Enter the URL of the Flow docs: `https://developers.flow.com/tools` and press Enter.
  + Note: This **will index all** the docs. We're investigating why you need `/tools`
  + Cursor will automatically detect the Flow docs and index them for you.
  + Ensure the name is `Flow`, and click "Confirm" to add the docs.

![Cursor Settings](/assets/images/use-cursor-2-40225d578bab288f66abe1221315b89d.png)

1. Set Cadence Docs:

* Click "+ Add new doc" again, now enter the URL of the Cadence docs: `https://cadence-lang.org/docs/` and press Enter.
* Same process as before, ensure the name is `Cadence`, and click "Confirm" to add the docs.

1. Add [Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources):
   Click "+ Add new doc" one more time and enter the URL of our massive, auto-generated file with the most current data and practices for Flow and Cadence: `https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/all_merged.md` and press Enter.

* Enter `Flow Data Sources`, and click "Confirm" to add the doc.
* **Caution**: This file is very large. For older development machines, you may wish to use the [essentials merged](https://github.com/onflow/Flow-Data-Sources/blob/main/merged_docs/essentials_merged.md) file instead.

1. Now wait for Cursor to index the docs. You can check the progress in the Docs section of the settings. After the indexing is complete, you can start using the docs in Cursor.

## Using Flow Docs in Cursor[​](#using-flow-docs-in-cursor "Direct link to Using Flow Docs in Cursor")

You can then reference the Flow docs in your prompt with the `@Flow`, `@Cadence`or `@Flow Data Sources` docs.

![Cursor Settings](/assets/images/use-cursor-3-ee338cc36953ea4ae1fe236ba9c1a9a5.png)

## Best Practices[​](#best-practices "Direct link to Best Practices")

When using Cursor with Flow documentation:

* Use `@Flow` when asking questions about Flow-specific concepts, tools, or ecosystem
* Use `@Cadence` when asking questions about Cadence programming language syntax or features
* Use `@Flow Data Sources` when asking about complex questions, difficult tasks, or anything that the first two sources didn't provide a satisfactory result
* Be specific in your prompts to get more accurate and relevant answers
* Combine both `@Flow` and `@Cadence` when working on cross-VM applications
* Use the documentation to verify AI-generated code and ensure best practices

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

If you encounter any issues:

1. Ensure all three sources are properly indexed
2. Try refreshing the documentation if answers seem outdated
3. Check your internet connection as Cursor needs to access the documentation
4. Verify the URLs are correct in your settings
5. Contact Cursor support if issues persist

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/ai-plus-flow/cursor/index.md)

Last updated on **Apr 3, 2025** by **Brian Doyle**

[Previous

AI Plus Flow](/tutorials/ai-plus-flow)[Next

Use ChatGPT](/tutorials/ai-plus-flow/chatgpt)

###### Rate this page

😞😐😊

* [Installation](#installation)
* [Using Flow Docs in Cursor](#using-flow-docs-in-cursor)
* [Best Practices](#best-practices)
* [Troubleshooting](#troubleshooting)

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
* [Flowscan Mainnet](https://flowscan.io/)
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