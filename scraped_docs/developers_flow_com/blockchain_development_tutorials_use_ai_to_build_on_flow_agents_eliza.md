# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza

Eliza on Flow | Flow Developer Portal



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

              - [Eliza on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza)

                * [Eliza Plugin Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/build-plugin)- [Using AgentKit on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/agentkit-flow-guide)+ [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)* Eliza on Flow

On this page

# Quickstart Guide to build AI Agent on Flow with Eliza

Eliza is a powerful framework you can use to build AI agents that interact with users through natural language. This tutorial will guide you through how to set up and deploy an AI agent on the Flow blockchain with Eliza. You'll learn how to create intelligent agents that can understand and respond to user queries, and leverage Flow's secure and scalable infrastructure.

## Learning objectives[​](#learning-objectives "Direct link to Learning objectives")

After you complete this tutorial, you will be able to:

* Set up the Eliza development environment.
* Configure and deploy an AI agent on Flow.
* Create and customize character configurations.
* Integrate different AI models with your agent.
* Interact with your AI agent through a web interface.
* Add and develop custom plugins for extended functionality.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you get started started with Eliza, make sure you have:

* [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (we recommend that you use [nvm](https://github.com/nvm-sh/nvm))
* [pnpm 9+](https://pnpm.io/installation)
* Git for version control
* A code editor (we recommend [VS Code](https://code.visualstudio.com/), [Cursor](https://cursor.com/) or [VSCodium](https://vscodium.com))
* [Flow-cli](https://developers.flow.com/tools/flow-cli) for Flow blockchain interaction.

> **Note for Windows Uuers:** [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual) is required.

## Installation[​](#installation "Direct link to Installation")

ElizaOnFlow is a Flow-dedicated Eliza wrapper, so:

* The plugins from this repository are also compatible with the origin [Eliza](https://github.com/elizaOs/eliza).
* You can also use any plugins from original Eliza in this repository.

Clone the repository

`_10

# The ElizaOnFlow is a wrapper with origin Eliza as submodule

_10

git clone --recurse-submodules https://github.com/onflow/elizaOnFlow.git

_10

_10

# Enter directory

_10

cd elizaOnFlow

_10

_10

# Please checkout the main branch which is using the latest release of origin Eliza

_10

git checkout main`

Or, If you want to use the origin Eliza, run:

`_10

# Eliza's characters folder is a submodule

_10

git clone --recurse-submodules https://github.com/elizaOs/eliza.git

_10

_10

# Enter directory

_10

cd eliza

_10

_10

# Checkout the latest release

_10

git checkout $(git describe --tags --abbrev=0)`

If you already cloned without submodules, run:

`_10

# Fetch submodules

_10

git submodule update --init --recursive`

Install dependencies

`_10

pnpm install --no-frozen-lockfile`

warning

Only use the `--no-frozen-lockfile` option when you initially instantiate the repo or bump the version of a package or add a new package to your `package.json` file. This practice helps maintain consistency in your project's dependencies and prevents unintended changes to the lockfile.

If you use ElizaOnFlow, you need to install Flow Cadence contracts dependencies to ensure that the Cadence extension correctly lints `*.cdc`.

Install Flow Cadence contracts dependencies:

`_10

flow deps install`

Build all packages:

`_10

pnpm build`

## Configure environment[​](#configure-environment "Direct link to Configure environment")

Copy `.env.example` to `.env` and fill in the appropriate values.

`_10

cp .env.example .env`

danger

In normal development, it's a best practice to use a `.env` to protect API keys and other sensitive information. When you work with crypto, it's **critical** to always use them, even in test projects or tutorials. If you expose a wallet key, you might lose everything in that wallet immediately, or someone might watch it for years and rob you the day you put something valuable there.

Edit `.env` and add your values. Do **NOT** add this file to version control.

### Choose Your model[​](#choose-your-model "Direct link to Choose Your model")

Eliza supports multiple AI models and you set which model to use inside the character JSON file.
But remember, after you choose a model, you need to set up the relevant configuration.

Check the full list of supported LLMs in origin Eliza: [Models.ts](https://github.com/elizaOS/eliza/blob/main/packages/core/src/models.ts)

Suggested models:

* Use API to access LLM providers:
  + OpenAI: set modelProvider as `openai`, and set `OPENAI_API_KEY` in `.env`.
  + Deepseek: set modelProvider as `deepseek`, and set `DEEPSEEK_API_KEY` in `.env`.
  + Grok: set modelProvider as `grok`, and set `GROK_API_KEY` in `.env`.
* Use local inference
  + Ollama: set modelProvider as `ollama`, and set `OLLAMA_MODEL` in `.env` to the model name you use in ollama.

> To choose a model, you need to set in charactor configuration. For example: OPENAI, set `modelProvider: "openai"` in charactor JSON file or `modelProvider: ModelProviderName.OPENAI` in `charactor.ts`

### Setup Agent's Flow account[​](#setup-agents-flow-account "Direct link to Setup Agent's Flow account")

Create a new Flow account for the Agent. Learn more: [doc](https://developers.flow.com/tools/flow-cli/accounts/create-accounts)

`_10

flow accounts create`

> If you use Testnet, you can get free tokens from [Flow Faucet](https://faucet.flow.com/)

Set the Flow blockchain configuration in `.env` with a newly-generated Flow account.

`_10

FLOW_ADDRESS=

_10

FLOW_PRIVATE_KEY=

_10

FLOW_NETWORK= # Default: mainnet

_10

FLOW_ENDPOINT_URL= # Default: <https://mainnet.onflow.org>`

For testnet, check Flow's [Networks](https://developers.flow.com/protocol/flow-networks) for more information.

## Create your first agent[​](#create-your-first-agent "Direct link to Create your first agent")

### Create a character file[​](#create-a-character-file "Direct link to Create a character file")

View the `deps/eliza/characters/` directory for a number of character files to try out.
Additionally, you can edit `charactor.ts` to override Eliza's `defaultCharacter` file, which is the default character file used if no character json files are provided.

Copy one of the example character files and make it your own:

`_10

cp characters/scooby.character.json characters/sample.character.json`

📝 [Character Documentation](https://elizaos.github.io/eliza/docs/core/characterfile/)

### **Start the Agent**[​](#start-the-agent "Direct link to start-the-agent")

Tell it which character you want to run:

`_10

pnpm start --character="characters/sample.character.json"`

Or, you can use `pnpm start:debug` for more debugging logs:

`_10

pnpm start:debug --character="characters/sample.character.json"`

You can load multiple characters with a comma-separated list:

`_10

pnpm start --characters="characters/sample.character.json, characters/scooby.character.json"`

### Add and develop plugins[​](#add-and-develop-plugins "Direct link to Add and develop plugins")

Run `npx elizaos plugins list` to get a list of available plugins or visit [Eliza Plugins Registry](https://elizaos.github.io/registry)

Run `npx elizaos plugins add @elizaos-plugins/plugin-NAME` to install the plugin into your instance

To create a new plugin **for your own business**, refer to the [plugin development guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/build-plugin).

#### Additional requirements[​](#additional-requirements "Direct link to Additional requirements")

You may need to install Sharp. If you see an error when you start it up, install it with the following command:

`_10

pnpm install --include=optional sharp`

### **Interact with the agent**[​](#interact-with-the-agent "Direct link to interact-with-the-agent")

Now you're ready to start a conversation with your agent.

Open a new terminal window and run the client's http server.

`_10

pnpm start:client`

After the client is running, you'll see a message like this:

`_10

➜ Local: http://localhost:5173/`

Click the link or open your browser to `http://localhost:5173/`. You'll see the chat interface connect to the system, and you can now interact with your character.

## Common issues and solutions[​](#common-issues-and-solutions "Direct link to Common issues and solutions")

Check the orgin Eliza's [Common Issues & Solutions](https://elizaos.github.io/eliza/docs/quickstart/#common-issues--solutions)

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you've learned how to build and deploy an AI agent on the Flow blockchain using Eliza. You've gained hands-on experience with setting up the development environment, configuring agents, creating character configurations, integrating AI models, and developing custom plugins.

The Eliza framework provides a powerful way to create intelligent agents that can understand and respond to user queries while leveraging Flow's secure and scalable infrastructure. Now taht you've completed this tutorial, you now have the foundation to build more sophisticated AI agents and create unique user experiences through character customization and plugin development.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/index.md)

Last updated on **Nov 20, 2025** by **cshannon1218**

[Previous

AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)[Next

Eliza Plugin Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/build-plugin)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Installation](#installation)* [Configure environment](#configure-environment)
        + [Choose Your model](#choose-your-model)+ [Setup Agent's Flow account](#setup-agents-flow-account)* [Create your first agent](#create-your-first-agent)
          + [Create a character file](#create-a-character-file)+ [**Start the Agent**](#start-the-agent)+ [Add and develop plugins](#add-and-develop-plugins)+ [**Interact with the agent**](#interact-with-the-agent)* [Common issues and solutions](#common-issues-and-solutions)* [Conclusion](#conclusion)

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