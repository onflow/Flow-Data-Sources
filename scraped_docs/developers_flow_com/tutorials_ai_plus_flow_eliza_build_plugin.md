# Source: https://developers.flow.com/tutorials/ai-plus-flow/eliza/build-plugin

Eliza Plugin Guide | Flow Developer Portal



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
* [Eliza on Flow](/tutorials/ai-plus-flow/eliza)
* Eliza Plugin Guide

On this page

# Eliza Plugin Development Guide

Plugins are a powerful way to extend the functionality of your Eliza AI agents. This guide will walk you through the process of creating custom plugins that can enhance your agent's capabilities, from simple utilities to complex integrations with external services. You'll learn how to leverage the plugin system to create modular and reusable components for your AI agents.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

By the end of this tutorial, you will be able to:

* Create a new plugin repository from the template
* Understand the plugin development workflow
* Implement custom actions and services
* Integrate plugins with your Eliza agent
* Register and publish plugins to the Eliza Plugin Registry
* Use dependency injection for better plugin architecture

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before getting started with Eliza, ensure you have:

* [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (using [nvm](https://github.com/nvm-sh/nvm) is recommended)
* [pnpm 9+](https://pnpm.io/installation)
* Git for version control
* A code editor ([VS Code](https://code.visualstudio.com/), [Cursor](https://cursor.com/) or [VSCodium](https://vscodium.com) recommended)
* [Flow-cli](https://developers.flow.com/tools/flow-cli) for Flow blockchain interaction.

> **Note for Windows Users:** [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual) is required.

## Quickstart[​](#quickstart "Direct link to Quickstart")

Please follow the [Quickstart Guide](/tutorials/ai-plus-flow/eliza) to set up your development environment.

## Plugin Development[​](#plugin-development "Direct link to Plugin Development")

### Create a Plugin repository from Template[​](#create-a-plugin-repository-from-template "Direct link to Create a Plugin repository from Template")

Visit [Eliza Plugin Template](https://github.com/onflow/eliza-plugin-template) and click on the "Use this template" button to create a new repository.

Or you can create a new empty repository and copy the files from some examples at [Eliza Plugins](https://github.com/elizaos-plugins) organization.

> Note: Flow's Eliza plugin template is using Dependency Injection(`@elizaos-plugins/plugin-di`), you can learn more about the Dependency Injection in the [plugin's README.md](https://github.com/fixes-world/plugin-di). It allows you can use `Class` instead of `Object` for your `Actions`, `Providers`, `Services`, and etc. **If you don't want to use it, you can follow the other examples in Eliza Plugins organiazation.**

### Add the Plugin repository to your Eliza project[​](#add-the-plugin-repository-to-your-eliza-project "Direct link to Add the Plugin repository to your Eliza project")

Let's say you created a repository named `username/plugin-foo`.

Use submodules to add the plugin repository to your Eliza project.

`_10

git submodule add https://github.com/username/plugin-foo.git packages/plugin-foo`

Change the package's name in the plugin's `package.json` to `@elizaos-plugins/plugin-foo`.

`_10

{

_10

"name": "@elizaos-plugins/plugin-foo",

_10

}`

Add the plugin to agent's `package.json`

`_10

pnpm add @elizaos-plugins/plugin-foo@'workspace:*' --filter ./agent`

Check the `agent/package.json` to ensure the plugin is added, you should see something like this:

`_10

{

_10

"dependencies": {

_10

"@elizaos-plugins/plugin-foo": "workspace:*"

_10

}

_10

}`

### Build the Plugin[​](#build-the-plugin "Direct link to Build the Plugin")

Build the plugin using the following command:

`_10

pnpm build --filter ./packages/plugin-foo

_10

_10

# Or build all packages

_10

pnpm build`

### Add Plugin to the `character.json` you want to use[​](#add-plugin-to-the-characterjson-you-want-to-use "Direct link to add-plugin-to-the-characterjson-you-want-to-use")

Let's say you want to add the plugin to the `sample` character which is `characters/sample.character.json`.

`_10

{

_10

"name": "Sample",

_10

"plugins": [

_10

"@elizaos-plugins/plugin-foo"

_10

]

_10

}`

warning

If you are using Dependency Injection(`@elizaos-plugins/plugin-di`) in your plugin, remember to add it to the `postProcessors` field. And **`clients` field is deprecated** in the latest version of Eliza, so if you want to add clients you also need to use `plugins` field.

`_10

{

_10

"name": "Sample",

_10

"plugins": [

_10

"@elizaos-plugins/plugin-foo",

_10

"@elizaos-plugins/client-discord"

_10

],

_10

"postProcessors": [

_10

"@elizaos-plugins/plugin-di"

_10

]

_10

}`

### Run the Eliza Agent with your Plugin[​](#run-the-eliza-agent-with-your-plugin "Direct link to Run the Eliza Agent with your Plugin")

Run the Eliza agent to test the plugin.

`_10

pnpm start --character="characters/sample.character.json"

_10

_10

# Or with more debug logs

_10

pnpm start:debug --character="characters/sample.character.json"`

### Interact with the Agent[​](#interact-with-the-agent "Direct link to Interact with the Agent")

Now, you're ready to start a conversation with your agent.

Open a new terminal window and run the client's http server.

`_10

pnpm start:client`

## Plugin Registration[​](#plugin-registration "Direct link to Plugin Registration")

You need to register your plugin in the [Eliza Plugin Registry](https://github.com/elizaos-plugins/registry) to make it available for other users.

Please follow the guide there, modify the [index.json](https://github.com/elizaos-plugins/registry/blob/main/index.json) and submit a PR to the registry repository.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you've learned how to develop custom plugins for Eliza. You've gained experience with creating plugin repositories, implementing custom actions and services, integrating plugins with agents, and using dependency injection for better architecture.

Eliza's plugin system provides a powerful way to extend the functionality of your AI agents. With the knowledge gained from this tutorial, you can now develop more sophisticated plugins, create reusable components, and share your work through the plugin registry.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/ai-plus-flow/eliza/build-plugin.md)

Last updated on **Apr 8, 2025** by **BT.Wood(Tang Bo Hao)**

[Previous

Eliza on Flow](/tutorials/ai-plus-flow/eliza)[Next

Token Launch](/tutorials/token-launch)

###### Rate this page

😞😐😊

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Quickstart](#quickstart)
* [Plugin Development](#plugin-development)
  + [Create a Plugin repository from Template](#create-a-plugin-repository-from-template)
  + [Add the Plugin repository to your Eliza project](#add-the-plugin-repository-to-your-eliza-project)
  + [Build the Plugin](#build-the-plugin)
  + [Add Plugin to the `character.json` you want to use](#add-plugin-to-the-characterjson-you-want-to-use)
  + [Run the Eliza Agent with your Plugin](#run-the-eliza-agent-with-your-plugin)
  + [Interact with the Agent](#interact-with-the-agent)
* [Plugin Registration](#plugin-registration)
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