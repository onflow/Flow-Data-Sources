# Source: https://developers.flow.com/build/tools/flow-cli/generate

Generating Cadence Boilerplate | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/super-commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)
    - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)
    - [Utils](/build/tools/flow-cli/utils/signature-generate)
    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)
    - [Running Cadence Tests](/build/tools/flow-cli/tests)
    - [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)
    - [Cadence Linter](/build/tools/flow-cli/lint)
    - [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)
    - [Data Collection](/build/tools/flow-cli/data-collection)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Flow CLI](/build/tools/flow-cli)
* Generating Cadence Boilerplate

On this page

# Generating Cadence Boilerplate

The `flow generate` command provides a convenient way to create boilerplate template files for common Cadence code components. This command streamlines the development process by automatically generating properly structured files with the correct syntax and organization.

## Overview[​](#overview "Direct link to Overview")

`_10

flow generate [command]`

**Aliases:** `generate`, `g`

The generate command supports four main subcommands for creating different types of Cadence files:

* **contract** - Generate Cadence smart contract templates
* **script** - Generate Cadence script templates
* **test** - Generate Cadence test templates
* **transaction** - Generate Cadence transaction templates

## Generate Contract[​](#generate-contract "Direct link to Generate Contract")

Creates a new Cadence smart contract with a basic template structure.

### Usage[​](#usage "Direct link to Usage")

`_10

flow generate contract <name> [flags]`

### Example[​](#example "Direct link to Example")

`_10

flow generate contract HelloWorld`

This command creates a file `cadence/contracts/HelloWorld.cdc` with the following content:

`_10

access(all) contract HelloWorld {

_10

init() {}

_10

}`

info

When generating a contract, a corresponding test file will also be created automatically (unless `--skip-tests` is used). For example, generating `HelloWorld` contract will also create `cadence/tests/HelloWorld.test.cdc`.

### Flags[​](#flags "Direct link to Flags")

* `--dir string` - Directory to generate files in (defaults to `cadence/contracts/`)
* `--skip-tests` - Skip generating test files
* `-h, --help` - Help for contract command

## Generate Transaction[​](#generate-transaction "Direct link to Generate Transaction")

Creates a new Cadence transaction with a basic template structure.

### Usage[​](#usage-1 "Direct link to Usage")

`_10

flow generate transaction <name> [flags]`

### Example[​](#example-1 "Direct link to Example")

`_10

flow generate transaction TransferTokens`

This command creates a file `cadence/transactions/TransferTokens.cdc` with the following content:

`_10

transaction() {

_10

prepare() {}

_10

_10

execute {}

_10

}`

### Flags[​](#flags-1 "Direct link to Flags")

* `--dir string` - Directory to generate files in (defaults to `cadence/transactions/`)
* `--skip-tests` - Skip generating test files
* `-h, --help` - Help for transaction command

## Generate Script[​](#generate-script "Direct link to Generate Script")

Creates a new Cadence script with a basic template structure.

### Usage[​](#usage-2 "Direct link to Usage")

`_10

flow generate script <name> [flags]`

### Example[​](#example-2 "Direct link to Example")

`_10

flow generate script GetBalance`

This command creates a file `cadence/scripts/GetBalance.cdc` with the following content:

`_10

access(all) fun main() {}`

### Flags[​](#flags-2 "Direct link to Flags")

* `--dir string` - Directory to generate files in (defaults to `cadence/scripts/`)
* `--skip-tests` - Skip generating test files
* `-h, --help` - Help for script command

## Generate Test[​](#generate-test "Direct link to Generate Test")

Creates a new Cadence test file with a basic template structure.

### Usage[​](#usage-3 "Direct link to Usage")

`_10

flow generate test <name> [flags]`

### Example[​](#example-3 "Direct link to Example")

`_10

flow generate test MyToken`

This command creates a file `cadence/tests/MyToken.test.cdc` with a basic test structure.

After generating a test, you can run it using `flow test`. For more information about writing and running Cadence tests, see the [Cadence Tests documentation](/build/tools/flow-cli/tests).

### Flags[​](#flags-3 "Direct link to Flags")

* `--dir string` - Directory to generate files in (defaults to `cadence/tests/`)
* `--skip-tests` - Skip generating test files
* `-h, --help` - Help for test command

## Custom Directory Usage[​](#custom-directory-usage "Direct link to Custom Directory Usage")

All generate commands support the `--dir` flag to specify a custom directory for the generated files. This is useful when your project requires a different organizational structure than the default.

### Examples[​](#examples "Direct link to Examples")

`_11

# Generate contract in a custom directory

_11

flow generate contract MyToken --dir=src/contracts

_11

_11

# Generate transaction in a custom directory

_11

flow generate transaction Transfer --dir=src/transactions

_11

_11

# Generate script in a custom directory

_11

flow generate script GetData --dir=src/scripts

_11

_11

# Generate test in a custom directory

_11

flow generate test MyToken --dir=src/tests`

## Project Structure[​](#project-structure "Direct link to Project Structure")

When using the default directories, the generate command creates the following structure:

`_10

cadence/

_10

├── contracts/

_10

│ └── MyToken.cdc

_10

├── scripts/

_10

│ └── GetBalance.cdc

_10

├── transactions/

_10

│ └── TransferTokens.cdc

_10

└── tests/

_10

└── MyToken.test.cdc`

The generate command is an essential tool for accelerating Flow development by providing standardized, well-structured boilerplate code for all common Cadence components.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/generate.md)

Last updated on **Aug 26, 2025** by **Chase Fleming**

[Previous

Running Cadence Tests](/build/tools/flow-cli/tests)[Next

Cadence Linter](/build/tools/flow-cli/lint)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)
* [Generate Contract](#generate-contract)
  + [Usage](#usage)
  + [Example](#example)
  + [Flags](#flags)
* [Generate Transaction](#generate-transaction)
  + [Usage](#usage-1)
  + [Example](#example-1)
  + [Flags](#flags-1)
* [Generate Script](#generate-script)
  + [Usage](#usage-2)
  + [Example](#example-2)
  + [Flags](#flags-2)
* [Generate Test](#generate-test)
  + [Usage](#usage-3)
  + [Example](#example-3)
  + [Flags](#flags-3)
* [Custom Directory Usage](#custom-directory-usage)
  + [Examples](#examples)
* [Project Structure](#project-structure)

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
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.