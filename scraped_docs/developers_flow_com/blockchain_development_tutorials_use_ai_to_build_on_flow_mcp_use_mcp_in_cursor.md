# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor

Use Flow MCP in Cursor | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

          + [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

            + [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)

              + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)

                - [Use Flow MCP in Cursor](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor)- [Contribute to Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* Use Flow MCP in Cursor

On this page

# Use Flow MCP in Cursor

Adding Flow MCP to Cursor gives you powerful AI-driven tools directly inside your code editor. It allows Cursor's AI to understand, query, and interact with Flow blockchain data and smart contracts through a standard protocol called the Model Context Protocol (MCP).

Specifically, it enables you to:

* Ask the AI in Cursor to fetch onchain data such as account balances, account information, or contract source code without leaving your editor.
* Speed up development by letting AI perform blockchain queries that would normally require manual steps.
* Improve context for AI assistance by allowing Cursor to pull real blockchain data when needed.
* Automate routine Flow tasks using tools exposed by the MCP server.
* Prototype and debug faster with direct access to live blockchain information.

This tutorial will guide you through setting up and using Flow MCP in [Cursor](https://www.cursor.com/) to enhance your Flow blockchain development experience with AI assistance.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After completing this tutorial, you should be able to:

* Configure Cursor to connect with the Flow MCP server using the MCP protocol.
* Install and launch the Flow MCP server locally through Cursor.
* Identify when Flow MCP tools are successfully loaded and ready inside Cursor.
* Use Flow MCP tools to retrieve blockchain data such as account balances, account details, and contract source code.
* Troubleshoot common setup and connectivity issues between Cursor and Flow MCP.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Cursor](https://www.cursor.com/) - the AI code editor
* [Flow MCP GitHub Repository](https://github.com/outblock/flow-mcp) - the Flow MCP server repository

## Installation[​](#installation "Direct link to Installation")

1. Open Cursor Settings and go to the "MCP" tab.

   ![Cursor Settings](/assets/images/mcp-settings-in-curosr-992c67311acc63125a862081ae6dcdd2.png)
2. Configure the MCP configuration file in Cursor:

   The MCP configuration file is located at the following location based on your operating system:

   * macOS: `~/Library/Application Support/Claude/mcp.json`
   * Windows: `%APPDATA%/Claude/mcp.json`
   * Linux: `~/.config/Claude/mcp.json`

   Add the following configuration:

   `_10

   {

   _10

   "mcpServers": {

   _10

   "flow-mcp": {

   _10

   "command": "npx",

   _10

   "args": ["-y", "@outblock/flow-mcp"]

   _10

   }

   _10

   }

   _10

   }`
3. Restart Cursor to load the new MCP configuration.

   You need to wait for the MCP server to start. Once it's ready, you will see there will be a green spot in the left side of `flow-mcp` server name label and all tools for Flow MCP will be displayed.

   ![Flow MCP server ready](/assets/images/flow-mcp-enabled-58b9ed77b93836e1fc1cc077d0367c50.png)

## How to use Flow MCP in Cursor[​](#how-to-use-flow-mcp-in-cursor "Direct link to How to use Flow MCP in Cursor")

### Checking Flow Balance[​](#checking-flow-balance "Direct link to Checking Flow Balance")

![Sample Image 1](/assets/images/sample-1-e626610744a305d993e0689b51025213.png)

### Viewing Account Information[​](#viewing-account-information "Direct link to Viewing Account Information")

![Sample Image 2](/assets/images/sample-2-e3f080df0c2de4c123e01ea7ce123401.png)

### Getting Contract Source Code[​](#getting-contract-source-code "Direct link to Getting Contract Source Code")

![Sample Image 3](/assets/images/sample-3-3a0d098a17c974fff8e5ab528fb41eef.png)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

If you encounter any issues:

1. Ensure the MCP server is properly installed
2. Verify the configuration file is in the correct location
3. Check that the paths in the configuration are correct
4. Try restarting Cursor
5. Check the console for any error messages

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

* [Flow MCP GitHub Repository](https://github.com/outblock/flow-mcp)
* [Cursor Documentation](https://cursor.sh/docs)
* [Flow Documentation](https://developers.flow.com/)

## Support[​](#support "Direct link to Support")

For issues or questions:

* Open an issue on the [Flow MCP GitHub Repository](https://github.com/outblock/flow-mcp)
* Join the [Flow Discord](https://discord.gg/flow) community

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)[Next

Contribute to Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Installation](#installation)* [How to use Flow MCP in Cursor](#how-to-use-flow-mcp-in-cursor)
        + [Checking Flow Balance](#checking-flow-balance)+ [Viewing Account Information](#viewing-account-information)+ [Getting Contract Source Code](#getting-contract-source-code)* [Troubleshooting](#troubleshooting)* [Additional Resources](#additional-resources)* [Support](#support)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.