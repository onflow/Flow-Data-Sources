# Source: https://developers.flow.com/tools/flow-cli/boilerplate

Cadence Boilerplate Generation | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)

  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
* Cadence Boilerplate

On this page

# Cadence Boilerplate Generation

## Introduction[​](#introduction "Direct link to Introduction")

Flow CLI now includes a feature to automatically generate boilerplate code for contracts, transactions, and scripts. This feature enhances the development experience by simplifying the initial setup of various components in Flow.

`_11

> flow generate

_11

Usage:

_11

flow generate [command]

_11

_11

Aliases:

_11

generate, g

_11

_11

Available Commands:

_11

contract Generate a new contract

_11

script Generate a new script

_11

transaction Generate a new transaction`

## Generate Contract[​](#generate-contract "Direct link to Generate Contract")

To create a new contract with basic structure, use the `contract` command. It creates a new Cadence file with a template contract definition.

`_10

flow generate contract [ContractName]`

### Usage Example[​](#usage-example "Direct link to Usage Example")

`_10

> flow generate contract HelloWorld`

This command creates a file `cadence/contracts/HelloWorld.cdc` with the following content:

`_10

access(all) contract HelloWorld {

_10

init() {}

_10

}`

## Generate Transaction[​](#generate-transaction "Direct link to Generate Transaction")

For initializing a transaction, use the `transaction` command. It sets up a new Cadence file with a template transaction structure.

`_10

flow generate transaction [TransactionName]`

### Usage Example[​](#usage-example-1 "Direct link to Usage Example")

`_10

> flow generate transaction SayHello`

This command creates a file `cadence/transactions/SayHello.cdc` with the following content:

`_10

transaction() {

_10

prepare() {}

_10

_10

execute {}

_10

}`

## Generate Script[​](#generate-script "Direct link to Generate Script")

Similarly, to start a new script, the `script` command generates a Cadence file with a basic script structure.

`_10

flow generate script [ScriptName]`

### Usage Example[​](#usage-example-2 "Direct link to Usage Example")

`_10

> flow generate script ReadHello`

This command creates a file `cadence/scripts/ReadHello.cdc` with the following content:

`_10

access(all) fun main() {}`

## Optional `--dir` Flag[​](#optional---dir-flag "Direct link to optional---dir-flag")

The `--dir` flag is an optional feature in the Flow CLI `generate` commands, allowing you to specify a custom directory for the generated contract, transaction, or script files. If this flag is not provided, the CLI adheres to the recommended project setup:

* Contracts are generated in the `cadence/contracts` directory.
* Transactions are generated in the `cadence/transactions` directory.
* Scripts are generated in the `cadence/scripts` directory.
* **Usage**: `--dir=<directory_name>`
* **Example**: `flow generate contract HelloWorld --dir=custom_contracts`

Use the `--dir` flag only if your project requires a different organizational structure than the default.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/boilerplate.md)

Last updated on **Apr 1, 2025** by **Brian Doyle**

[Previous

Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)[Next

Data Collection](/tools/flow-cli/data-collection)

###### Rate this page

😞😐😊

* [Introduction](#introduction)
* [Generate Contract](#generate-contract)
  + [Usage Example](#usage-example)
* [Generate Transaction](#generate-transaction)
  + [Usage Example](#usage-example-1)
* [Generate Script](#generate-script)
  + [Usage Example](#usage-example-2)
* [Optional `--dir` Flag](#optional---dir-flag)

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