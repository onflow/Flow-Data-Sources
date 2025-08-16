# Source: https://developers.flow.com/tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor

Use Flow MCP in Cursor | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [Flow Actions](/tutorials/defi)
* [Flow Blockchain 101](/tutorials/flow-101)
* [Use AI To Build On Flow](/tutorials/use-AI-to-build-on-flow)

  + [Use Cursor AI](/tutorials/use-AI-to-build-on-flow/cursor)
  + [Flow MCP](/tutorials/use-AI-to-build-on-flow/mcp)

    - [Use Flow MCP in Cursor](/tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor)
    - [Contribute to Flow MCP](/tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp)
  + [Use ChatGPT](/tutorials/use-AI-to-build-on-flow/chatgpt)
  + [Flow Data Sources](/tutorials/use-AI-to-build-on-flow/flow-data-sources)
  + [Using AgentKit on Flow](/tutorials/use-AI-to-build-on-flow/agentkit-flow-guide)
  + [Cadence Rules](/tutorials/use-AI-to-build-on-flow/cadence-rules)
  + [Eliza on Flow](/tutorials/use-AI-to-build-on-flow/eliza)
  + [Claude Code Flow Guide](/tutorials/use-AI-to-build-on-flow/claude-code)
* [Gasless Transactions](/tutorials/gasless-transactions)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [Native VRF](/tutorials/native-vrf)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Integrations](/tutorials/integrations/crossmint)

* [Use AI To Build On Flow](/tutorials/use-AI-to-build-on-flow)
* [Flow MCP](/tutorials/use-AI-to-build-on-flow/mcp)
* Use Flow MCP in Cursor

On this page

# Use Flow MCP in Cursor

Adding Flow MCP to Cursor gives you powerful AI-driven tools directly inside your code editor. It allows Cursor's AI to understand, query, and interact with Flow blockchain data and smart contracts through a standard protocol called the Model Context Protocol (MCP).

Specifically, it enables you to:

* Ask the AI in Cursor to fetch on-chain data such as account balances, account information, or contract source code without leaving your editor.
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor.md)

Last updated on **Aug 11, 2025** by **0xLisanAlGaib**

[Previous

Flow MCP](/tutorials/use-AI-to-build-on-flow/mcp)[Next

Contribute to Flow MCP](/tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [How to use Flow MCP in Cursor](#how-to-use-flow-mcp-in-cursor)
  + [Checking Flow Balance](#checking-flow-balance)
  + [Viewing Account Information](#viewing-account-information)
  + [Getting Contract Source Code](#getting-contract-source-code)
* [Troubleshooting](#troubleshooting)
* [Additional Resources](#additional-resources)
* [Support](#support)

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
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.