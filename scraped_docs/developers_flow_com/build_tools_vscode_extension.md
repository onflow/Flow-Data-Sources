# Source: https://developers.flow.com/build/tools/vscode-extension

Cadence VS Code Extension | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [@onflow/react-sdk](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* Cadence VS Code Extension

On this page

# Cadence VS Code Extension

This extension integrates [Cadence](https://cadence-lang.org/docs), the resource-oriented smart contract programming language of [Flow](https://www.onflow.org/), into [Visual Studio Code](https://code.visualstudio.com/).
It provides features like syntax highlighting, type checking, code completion, etc.

Note that most editing features (type checking, code completion, etc.) are implemented in the [Cadence Language Server](https://github.com/onflow/cadence-tools/tree/master/languageserver).

## Features[​](#features "Direct link to Features")

* Syntax highlighting (including in Markdown code fences)
* Run the emulator, submit transactions, scripts from the editor

## Installation[​](#installation "Direct link to Installation")

To install the extension, ensure you have the [VS Code IDE installed](https://code.visualstudio.com/docs/setup/mac).  
Then, you can install the Cadence extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=onflow.cadence).

## Developing the Extension[​](#developing-the-extension "Direct link to Developing the Extension")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Must have Typescript installed globally: `npm i -g typescript`

### Getting Started[​](#getting-started "Direct link to Getting Started")

* Run the Typescript watcher: `tsc -watch -p ./`
* Launch the extension by pressing `F5` in VSCode
* Manually reload the extension host when you make changes to TypeScript code

### Configuration for Extension Host if Missing (`launch.json`):[​](#configuration-for-extension-host-if-missing-launchjson "Direct link to configuration-for-extension-host-if-missing-launchjson")

`_13

{

_13

"version": "0.2.0",

_13

"configurations": [

_13

{

_13

"type": "extensionHost",

_13

"request": "launch",

_13

"name": "Launch Extension",

_13

"runtimeExecutable": "${execPath}",

_13

"args": ["--extensionDevelopmentPath=${workspaceFolder}"],

_13

"outFiles": ["${workspaceFolder}/out/**/*.js"]

_13

}

_13

]

_13

}`

### Building[​](#building "Direct link to Building")

If you are building the extension from source, you need to build both the
extension itself and the Flow CLI (if you don't already have a version installed).
Unless you're developing the extension or need access to unreleased features,
you should use the Flow CLI install option (above). It's much easier!

If you haven't already, install dependencies.

script

`_10

npm install`

Next, build and package the extension.

script

`_10

npm run package`

This will result in a `.vsix` file containing the packaged extension.

Install the packaged extension.

script

`_10

code --install-extension cadence-*.vsix`

Restart VS Code and the extension should be installed!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/vscode-extension/index.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Data Collection](/build/tools/flow-cli/data-collection)[Next

Flow Dev Wallet](/build/tools/flow-dev-wallet)

###### Rate this page

😞😐😊

Copy as Markdown

* [Features](#features)* [Installation](#installation)* [Developing the Extension](#developing-the-extension)
      + [Prerequisites](#prerequisites)+ [Getting Started](#getting-started)+ [Configuration for Extension Host if Missing (`launch.json`):](#configuration-for-extension-host-if-missing-launchjson)+ [Building](#building)

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