# Source: https://developers.flow.com/tutorials/ai-plus-flow/eliza

Eliza on Flow | Flow Developer Portal



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
  + [Eliza on Flow](/tutorials/ai-plus-flow/eliza)

    - [Eliza Plugin Guide](/tutorials/ai-plus-flow/eliza/build-plugin)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

* [AI Plus Flow](/tutorials/ai-plus-flow)
* Eliza on Flow

On this page

# Quickstart Guide to build AI Agent on Flow with Eliza

Eliza is a powerful framework for building AI agents that can interact with users through natural language. This tutorial will guide you through setting up and deploying an AI agent on the Flow blockchain using Eliza. You'll learn how to create intelligent agents that can understand and respond to user queries, while leveraging Flow's secure and scalable infrastructure.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

By the end of this tutorial, you will be able to:

* Set up the Eliza development environment
* Configure and deploy an AI agent on Flow
* Create and customize character configurations
* Integrate different AI models with your agent
* Interact with your AI agent through a web interface
* Add and develop custom plugins for extended functionality

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before getting started with Eliza, ensure you have:

* [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (using [nvm](https://github.com/nvm-sh/nvm) is recommended)
* [pnpm 9+](https://pnpm.io/installation)
* Git for version control
* A code editor ([VS Code](https://code.visualstudio.com/), [Cursor](https://cursor.com/) or [VSCodium](https://vscodium.com) recommended)
* [Flow-cli](https://developers.flow.com/tools/flow-cli) for Flow blockchain interaction.

> **Note for Windows Users:** [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual) is required.

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

Or, If you want to use the origin Eliza, please run:

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

If you already cloned without submodules, please run:

`_10

# Fetch submodules

_10

git submodule update --init --recursive`

Install dependencies

`_10

pnpm install --no-frozen-lockfile`

warning

Please only use the `--no-frozen-lockfile` option when you're initially instantiating the repo or are bumping the version of a package or adding a new package to your package.json. This practice helps maintain consistency in your project's dependencies and prevents unintended changes to the lockfile.

If you are using ElizaOnFlow, you need to install Flow Cadence contracts dependencies to ensure `*.cdc` be correctly linted by Cadence extension.

Install Flow Cadence contracts dependencies:

`_10

flow deps install`

Build all packages:

`_10

pnpm build`

## Configure Environment[​](#configure-environment "Direct link to Configure Environment")

Copy .env.example to .env and fill in the appropriate values.

`_10

cp .env.example .env`

danger

In normal development, it's a best practice to use a `.env` to protect API keys and other sensitive information. When working with crypto, it's **critical** to be disciplined and always use them, even in test projects or tutorials. If you expose a wallet key, you might lose everything in that wallet immediately, or someone might watch it for years and rug you the day you put something valuable there.

Edit `.env` and add your values. Do NOT add this file to version control.

### Choose Your Model[​](#choose-your-model "Direct link to Choose Your Model")

Eliza supports multiple AI models and you set which model to use inside the character JSON file.
But remember, once you chosed a model, you need to set up the relevant configuration.

Check full list of supported LLMs in origin Eliza: [Models.ts](https://github.com/elizaOS/eliza/blob/main/packages/core/src/models.ts)

Suggested models:

* Use API to access LLM providers
  + OpenAI: set modelProvider as `openai`, and set `OPENAI_API_KEY` in `.env`
  + Deepseek: set modelProvider as `deepseek`, and set `DEEPSEEK_API_KEY` in `.env`
  + Grok: set modelProvider as `grok`, and set `GROK_API_KEY` in `.env`
* Use local inference
  + Ollama: set modelProvider as `ollama`, and set `OLLAMA_MODEL` in `.env` to the model name you are using in ollama.

> To choose model, you need to set in charactor configuration. For example: OPENAI, please set `modelProvider: "openai"` in charactor JSON file or `modelProvider: ModelProviderName.OPENAI` in `charactor.ts`

### Setup Agent's Flow Account[​](#setup-agents-flow-account "Direct link to Setup Agent's Flow Account")

Create a new Flow account for the Agent. Learn more: [doc](https://developers.flow.com/tools/flow-cli/accounts/create-accounts)

`_10

flow accounts create`

> If you are using Testnet, you can get free tokens from [Flow Faucet](https://faucet.flow.com/)

Set Flow blockchain configuration in `.env` with new generated Flow account.

`_10

FLOW_ADDRESS=

_10

FLOW_PRIVATE_KEY=

_10

FLOW_NETWORK= # Default: mainnet

_10

FLOW_ENDPOINT_URL= # Default: <https://mainnet.onflow.org>`

For testnet, please check Flow's [Networks](https://developers.flow.com/networks/flow-networks) for more information.

## Create Your First Agent[​](#create-your-first-agent "Direct link to Create Your First Agent")

### Create a Character File[​](#create-a-character-file "Direct link to Create a Character File")

Check out the `deps/eliza/characters/` directory for a number of character files to try out.
Additionally you can override Eliza's `defaultCharacter` by editting `charactor.ts` which will be default used if no character json provided.

Copy one of the example character files and make it your own

`_10

cp characters/scooby.character.json characters/sample.character.json`

📝 [Character Documentation](https://elizaos.github.io/eliza/docs/core/characterfile/)

### **Start the Agent**[​](#start-the-agent "Direct link to start-the-agent")

Inform it which character you want to run:

`_10

pnpm start --character="characters/sample.character.json"`

Or you can use `pnpm start:debug` for more debugging logs:

`_10

pnpm start:debug --character="characters/sample.character.json"`

You can load multiple characters with a comma-separated list:

`_10

pnpm start --characters="characters/sample.character.json, characters/scooby.character.json"`

### Add / Develop Plugins[​](#add--develop-plugins "Direct link to Add / Develop Plugins")

run `npx elizaos plugins list` to get a list of available plugins or visit [Eliza Plugins Registry](https://elizaos.github.io/registry)

run `npx elizaos plugins add @elizaos-plugins/plugin-NAME` to install the plugin into your instance

To create a new plugin **for your own business**, you can refer to the [plugin development guide](/tutorials/ai-plus-flow/eliza/build-plugin).

#### Additional Requirements[​](#additional-requirements "Direct link to Additional Requirements")

You may need to install Sharp. If you see an error when starting up, try installing it with the following command:

`_10

pnpm install --include=optional sharp`

### **Interact with the Agent**[​](#interact-with-the-agent "Direct link to interact-with-the-agent")

Now you're ready to start a conversation with your agent.

Open a new terminal window and run the client's http server.

`_10

pnpm start:client`

Once the client is running, you'll see a message like this:

`_10

➜ Local: http://localhost:5173/`

Simply click the link or open your browser to `http://localhost:5173/`. You'll see the chat interface connect to the system, and you can begin interacting with your character.

## Common Issues & Solutions[​](#common-issues--solutions "Direct link to Common Issues & Solutions")

Please check the orgin Eliza's [Common Issues & Solutions](https://elizaos.github.io/eliza/docs/quickstart/#common-issues--solutions)

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you've learned how to build and deploy an AI agent on the Flow blockchain using Eliza. You've gained hands-on experience with setting up the development environment, configuring agents, creating character configurations, integrating AI models, and developing custom plugins.

The Eliza framework provides a powerful way to create intelligent agents that can understand and respond to user queries while leveraging Flow's secure and scalable infrastructure. By completing this tutorial, you now have the foundation to build more sophisticated AI agents and create unique user experiences through character customization and plugin development.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/ai-plus-flow/eliza/index.md)

Last updated on **Apr 16, 2025** by **leopardracer**

[Previous

Using AgentKit on Flow](/tutorials/ai-plus-flow/agentkit-flow-guide)[Next

Eliza Plugin Guide](/tutorials/ai-plus-flow/eliza/build-plugin)

###### Rate this page

😞😐😊

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configure Environment](#configure-environment)
  + [Choose Your Model](#choose-your-model)
  + [Setup Agent's Flow Account](#setup-agents-flow-account)
* [Create Your First Agent](#create-your-first-agent)
  + [Create a Character File](#create-a-character-file)
  + [**Start the Agent**](#start-the-agent)
  + [Add / Develop Plugins](#add--develop-plugins)
  + [**Interact with the Agent**](#interact-with-the-agent)
* [Common Issues & Solutions](#common-issues--solutions)
* [Conclusion](#conclusion)

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