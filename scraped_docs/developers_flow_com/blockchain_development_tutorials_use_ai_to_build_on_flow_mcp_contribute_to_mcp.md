# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp

Contribute to Flow MCP | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Flow Actions](/blockchain-development-tutorials/flow-actions)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

  + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)
  + [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)
  + [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)
  + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)

    - [Use Flow MCP in Cursor](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor)
    - [Contribute to Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)
* Contribute to Flow MCP

On this page

# Contribute to Flow MCP

This tutorial will guide you through the process of contributing to the Flow MCP server. The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open standard developed by Anthropic that enables AI applications to interact seamlessly with external tools, systems, and data sources.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After completing this tutorial, you should be able to:

* Set up and build the Flow MCP server development environment.
* Create and register a new Action Tool, including schema, handler, and tests.
* Test and validate the functionality of a new Action Tool within the MCP system.
* Submit a complete pull request that follows Flow MCP contribution guidelines.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Bun](https://bun.sh/) - the JavaScript runtime
* [Flow MCP server](https://github.com/outblock/flow-mcp) - the Flow MCP server repository

## Installation[​](#installation "Direct link to Installation")

1. Fork the [Flow MCP server](https://github.com/outblock/flow-mcp) repository
2. Clone the repository

   `_10

   git clone https://github.com/your-username/flow-mcp.git`
3. Install the dependencies

   `_10

   bun install`
4. Build the project

   `_10

   bun build`

## Create new Action Tool for Flow MCP[​](#create-new-action-tool-for-flow-mcp "Direct link to Create new Action Tool for Flow MCP")

1. Create a new folder in the `src/tools` directory

   `_10

   mkdir src/tools/your-tool-name`
2. Create and implement the `index.ts`, `schema.ts`, and `your-tool.test.ts` files, which is the entry point, schema, and test file for the new tool respectively.

   The `export` of `index.ts` file should be a `ToolRegistration` object, which is the registration of the new tool.

   `_10

   type ToolRegistration<T> = {

   _10

   name: string;

   _10

   description: string;

   _10

   inputSchema: z.ZodSchema;

   _10

   handler: (args: T) => CallToolResult | Promise<CallToolResult>;

   _10

   };`

   If you want to add new Cadence files for your new tool, you can add them in the `src/cadence` directory. The `bun` will compile the Cadence files into `String`, so the dedicated Cadence files will help the project to be more organized.

   And it is recommended to add a test for your new tool in the `src/tools/your-tool-name/your-tool.test.ts` file.
3. Add a prompt export in the `src/prompts` directory which is used to ensure MCP client can understand the new tool. You can refer to the existing tools for examples.
4. Add your new tool to the `src/tools/index.ts` file.

   `_10

   export const createTools = (): ToolRegistration<any>[] => {

   _10

   return [

   _10

   // ... other tools

   _10

   yourTool,

   _10

   ];

   _10

   };`
5. Run the test to ensure your new tool works as expected

   `_10

   bun test`
6. Commit and push your changes to your forked repository, and create a pull request.

We will review your pull request and merge it if it is ready.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Use Flow MCP in Cursor](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor)[Next

Flow EVM Guides](/blockchain-development-tutorials/evm)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Create new Action Tool for Flow MCP](#create-new-action-tool-for-flow-mcp)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
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
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.