# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor

Use Flow MCP in Cursor | Flow Developer Portal



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

When you add Flow MCP to Cursor, it gives you powerful AI-driven tools directly inside your code editor. It allows Cursor's AI to understand, query, and interact with Flow blockchain data and smart contracts through a standard protocol called the Model Context Protocol (MCP).

Specifically, it lets you:

* Ask the AI in Cursor to fetch onchain data such as account balances, account information, or contract source code without the need to leave your editor.
* Speed up development when you have AI perform blockchain queries that would normally require manual steps.
* Improve context for AI assistance if you let Cursor to pull real blockchain data when needed.
* Automate routine Flow tasks with tools exposed by the MCP server.
* Prototype and debug faster with direct access to live blockchain information.

This tutorial will guide you through setting up and using Flow MCP in [Cursor](https://www.cursor.com/) to enhance your Flow blockchain development experience with AI assistance.

## Learning objectives[​](#learning-objectives "Direct link to Learning objectives")

After you complete this tutorial, you should be able to:

* Configure Cursor to connect with the Flow MCP server with the MCP protocol.
* Install and launch the Flow MCP server locally through Cursor.
* Identify when Flow MCP tools successfully load and are ready inside Cursor.
* Use Flow MCP tools to retrieve blockchain data such as account balances, account details, and contract source code.
* Troubleshoot common setup and connectivity issues between Cursor and Flow MCP.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Cursor](https://www.cursor.com/) - the AI code editor.
* [Flow MCP GitHub Repository](https://github.com/outblock/flow-mcp) - the Flow MCP server repository.

## Installation[​](#installation "Direct link to Installation")

1. Open Cursor Settings and go to the "MCP" tab.

   ![Cursor Settings](/assets/images/mcp-settings-in-curosr-992c67311acc63125a862081ae6dcdd2.png)
2. Configure the MCP configuration file in Cursor:

   The MCP configuration file resides at this location based on your operating system:

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

   You need to wait for the MCP server to start. After it's ready, a green spot appears in the left side of `flow-mcp` server name label, and all tools for Flow MCP display.

   ![Flow MCP server ready](/assets/images/flow-mcp-enabled-58b9ed77b93836e1fc1cc077d0367c50.png)

## How to use Flow MCP in Cursor[​](#how-to-use-flow-mcp-in-cursor "Direct link to How to use Flow MCP in Cursor")

### Check Flow balance[​](#check-flow-balance "Direct link to Check Flow balance")

![Sample Image 1](/assets/images/sample-1-e626610744a305d993e0689b51025213.png)

### View account information[​](#view-account-information "Direct link to View account information")

![Sample Image 2](/assets/images/sample-2-e3f080df0c2de4c123e01ea7ce123401.png)

### Get contract source code[​](#get-contract-source-code "Direct link to Get contract source code")

![Sample Image 3](/assets/images/sample-3-3a0d098a17c974fff8e5ab528fb41eef.png)

## Troubleshoot[​](#troubleshoot "Direct link to Troubleshoot")

If you encounter any issues:

1. Ensure the MCP server is properly installed.
2. Verify the configuration file is in the correct location.
3. Check that the paths in the configuration are correct.
4. Try to restart Cursor.
5. Check the console for any error messages.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

* [Flow MCP GitHub Repository](https://github.com/outblock/flow-mcp)
* [Cursor Documentation](https://cursor.sh/docs)
* [Flow Documentation](https://developers.flow.com/)

## Support[​](#support "Direct link to Support")

For issues or questions:

* Open an issue on the [Flow MCP GitHub Repository](https://github.com/outblock/flow-mcp).
* Join the [Flow Discord](https://discord.gg/flow) community.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor.md)

Last updated on **Nov 20, 2025** by **cshannon1218**

[Previous

Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)[Next

Contribute to Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Installation](#installation)* [How to use Flow MCP in Cursor](#how-to-use-flow-mcp-in-cursor)
        + [Check Flow balance](#check-flow-balance)+ [View account information](#view-account-information)+ [Get contract source code](#get-contract-source-code)* [Troubleshoot](#troubleshoot)* [Additional resources](#additional-resources)* [Support](#support)

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