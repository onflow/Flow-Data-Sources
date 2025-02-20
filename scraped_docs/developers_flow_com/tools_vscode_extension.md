# Source: https://developers.flow.com/tools/vscode-extension




Cadence VS Code Extension | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
  + [Use Cursor AI](/tools/vscode-extension/cursor)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* Cadence VS Code Extension
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

 `_13{_13 "version": "0.2.0",_13 "configurations": [_13 {_13 "type": "extensionHost",_13 "request": "launch",_13 "name": "Launch Extension",_13 "runtimeExecutable": "${execPath}",_13 "args": ["--extensionDevelopmentPath=${workspaceFolder}"],_13 "outFiles": ["${workspaceFolder}/out/**/*.js"]_13 }_13 ]_13}`
### Building[​](#building "Direct link to Building")

If you are building the extension from source, you need to build both the
extension itself and the Flow CLI (if you don't already have a version installed).
Unless you're developing the extension or need access to unreleased features,
you should use the Flow CLI install option (above). It's much easier!

If you haven't already, install dependencies.

script `_10npm install`

Next, build and package the extension.

script `_10npm run package`

This will result in a `.vsix` file containing the packaged extension.

Install the packaged extension.

script `_10code --install-extension cadence-*.vsix`

Restart VS Code and the extension should be installed!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/vscode-extension/index.md)Last updated on **Feb 6, 2025** by **Brian Doyle**[PreviousFlow Dev Wallet](/tools/flow-dev-wallet)[NextUse Cursor AI](/tools/vscode-extension/cursor)
###### Rate this page

😞😐😊

* [Features](#features)
* [Installation](#installation)
* [Developing the Extension](#developing-the-extension)
  + [Prerequisites](#prerequisites)
  + [Getting Started](#getting-started)
  + [Configuration for Extension Host if Missing (`launch.json`):](#configuration-for-extension-host-if-missing-launchjson)
  + [Building](#building)
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
* [Flowscan Mainnet](https://flowdscan.io/)
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

