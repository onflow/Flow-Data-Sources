# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/build-plugin

Eliza Plugin Guide | Flow Developer Portal



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

              - [Eliza on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza)

                * [Eliza Plugin Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/build-plugin)- [Using AgentKit on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/agentkit-flow-guide)+ [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)* [Eliza on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza)* Eliza Plugin Guide

On this page

# Eliza Plugin Development Guide

## Overview[​](#overview "Direct link to Overview")

Plugins are a powerful way to extend the functionality of your Eliza AI agents. This guide will walk you through the process of how to create custom plugins that can enhance your agent's capabilities, from simple utilities to complex integrations with external services. You'll learn how to leverage the plugin system to create modular and reusable components for your AI agents.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After you complete this tutorial, you will be able to:

* Create a new plugin repository from the template.
* Understand the plugin development workflow.
* Implement custom actions and services.
* Integrate plugins with your Eliza agent.
* Register and publish plugins to the Eliza Plugin Registry.
* Use dependency injection for better plugin architecture.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you get started with Eliza, make sure you have:

* [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (using [nvm](https://github.com/nvm-sh/nvm) is recommended)
* [pnpm 9+](https://pnpm.io/installation)
* Git for version control
* A code editor ([VS Code](https://code.visualstudio.com/), [Cursor](https://cursor.com/) or [VSCodium](https://vscodium.com) recommended)
* [Flow-cli](https://developers.flow.com/tools/flow-cli) for Flow blockchain interaction.

> **Note for Windows Users:** [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual) is required.

## Quickstart[​](#quickstart "Direct link to Quickstart")

Follow the [Quickstart Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza) to set up your development environment.

## Plugin Development[​](#plugin-development "Direct link to Plugin Development")

### Create a Plugin repository from Template[​](#create-a-plugin-repository-from-template "Direct link to Create a Plugin repository from Template")

Visit [Eliza Plugin Template](https://github.com/onflow/eliza-plugin-template) and click "Use this template" to create a new repository.

Or, you can create a new empty repository and copy the files from some examples at the [Eliza Plugins](https://github.com/elizaos-plugins) organization.

note

Flow's Eliza plugin template uses Dependency Injection(`@elizaos-plugins/plugin-di`). You can learn more about the Dependency Injection in the [plugin's README.md](https://github.com/fixes-world/plugin-di). It allows you can use `Class` instead of `Object` for your `Actions`, `Providers`, `Services`, and so on. **If you don't want to use it, you can follow the other examples in Eliza Plugins organiazation.**

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

Check the `agent/package.json` to make sure the plugin is added. You'll see something like this:

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

Build the plugin with the following command:

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

If you use Dependency Injection(`@elizaos-plugins/plugin-di`) in your plugin, remember to add it to the `postProcessors` field. And **`clients` field is deprecated** in the latest version of Eliza, so if you want to add clients, you also need to use `plugins` field.

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

Follow the guide there, modify the [index.json](https://github.com/elizaos-plugins/registry/blob/main/index.json) file, and submit a pull request (PR) to the registry repository.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you've learned how to develop custom plugins for Eliza. You've gained experience with creating plugin repositories, implementing custom actions and services, integrating plugins with agents, and using dependency injection for better architecture.

Eliza's plugin system provides a powerful way to extend the functionality of your AI agents. With the knowledge gained from this tutorial, you can now develop more sophisticated plugins, create reusable components, and share your work through the plugin registry.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza/build-plugin.md)

Last updated on **Oct 28, 2025** by **cshannon1218**

[Previous

Eliza on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/eliza)[Next

Using AgentKit on Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents/agentkit-flow-guide)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Learning Objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Quickstart](#quickstart)* [Plugin Development](#plugin-development)
          + [Create a Plugin repository from Template](#create-a-plugin-repository-from-template)+ [Add the Plugin repository to your Eliza project](#add-the-plugin-repository-to-your-eliza-project)+ [Build the Plugin](#build-the-plugin)+ [Add Plugin to the `character.json` you want to use](#add-plugin-to-the-characterjson-you-want-to-use)+ [Run the Eliza Agent with your Plugin](#run-the-eliza-agent-with-your-plugin)+ [Interact with the Agent](#interact-with-the-agent)* [Plugin Registration](#plugin-registration)* [Conclusion](#conclusion)

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