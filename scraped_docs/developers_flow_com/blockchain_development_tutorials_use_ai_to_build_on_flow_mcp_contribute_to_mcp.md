# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp

Contribute to Flow MCP | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

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

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* Contribute to Flow MCP

On this page

# Contribute to Flow MCP

This tutorial will guide you through the process of contributing to the Flow MCP server. The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open standard developed by Anthropic that allows AI applications to interact seamlessly with external tools, systems, and data sources.

## Learning objectives[​](#learning-objectives "Direct link to Learning objectives")

After you complete this tutorial, you should be able to:

* Set up and build the Flow MCP server development environment.
* Create and register a new Action Tool, including schema, handler, and tests.
* Test and validate the functionality of a new Action Tool within the MCP system.
* Submit a complete pull request that follows Flow MCP contribution guidelines.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Bun](https://bun.sh/) - the JavaScript runtime.
* [Flow MCP server](https://github.com/outblock/flow-mcp) - the Flow MCP server repository.

## Installation[​](#installation "Direct link to Installation")

1. Fork the [Flow MCP server](https://github.com/outblock/flow-mcp) repository.
2. Clone the repository:

   `_10

   git clone https://github.com/your-username/flow-mcp.git`
3. Install the dependencies:

   `_10

   bun install`
4. Build the project:

   `_10

   bun build`

## Create new action tool for Flow MCP[​](#create-new-action-tool-for-flow-mcp "Direct link to Create new action tool for Flow MCP")

1. Create a new folder in the `src/tools` directory:

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

   And we recommended that you add a test for your new tool in the `src/tools/your-tool-name/your-tool.test.ts` file.
3. Add a prompt export in the `src/prompts` directory which is used to confirm that MCP clients can understand the new tool. You can refer to the existing tools for examples.
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
5. Run the test to confirm your new tool works as expected:

   `_10

   bun test`
6. Commit and push your changes to your forked repository, and create a pull request.

We will review your pull request and merge it if it's ready.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/contribute-to-mcp.md)

Last updated on **Oct 30, 2025** by **cshannon1218**

[Previous

Use Flow MCP in Cursor](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp/use-mcp-in-cursor)[Next

Cadence Tutorials](/blockchain-development-tutorials/cadence)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Installation](#installation)* [Create new action tool for Flow MCP](#create-new-action-tool-for-flow-mcp)

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