# Source: https://developers.flow.com/build/tools/flow-cli/deployment/project-contracts

Add Project Contracts | Flow Developer Portal



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
* [Solidity (EVM)](/build/evm/about)

  + [Why EVM on Flow](/build/evm/about)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [EVM Quickstart](/build/evm/quickstart)
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

      * [Start Emulator](/build/tools/flow-cli/deployment/start-emulator)
      * [Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)
      * [Deploy a Project](/build/tools/flow-cli/deployment/deploy-project-contracts)
      * [Create Emulator Snapshot](/build/tools/flow-cli/deployment/emulator-snapshot)
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
* Deploy Project
* Add Project Contracts

On this page

# Add Project Contracts

## Add a Contract[​](#add-a-contract "Direct link to Add a Contract")

To add a contract to your project, update the `"contracts"` section of your `flow.json` file.

Contracts are specified as key-value pairs, where the key is the contract name,
and the value is the location of the Cadence source code.

For example, the configuration below will register the
contract `Foo` from the `FooContract.cdc` file.

`_10

{

_10

"contracts": {

_10

"Foo": "./cadence/contracts/FooContract.cdc"

_10

}

_10

}`

## Define Contract Deployment Targets[​](#define-contract-deployment-targets "Direct link to Define Contract Deployment Targets")

Once a contract is added, it can then be assigned to one or more deployment targets.

A deployment target is an account to which the contract will be deployed.
In a typical project, a contract has one deployment target per network (e.g. Emulator, Testnet, Mainnet).

Deployment targets are defined in the `"deployments"` section of your `flow.json` file.

Targets are grouped by their network, where each network is a mapping from target account to contract list.
Multiple contracts can be deployed to the same target account.

For example, here's how we'd deploy contracts `Foo` and `Bar` to the account `my-testnet-account`:

`_11

{

_11

"contracts": {

_11

"Foo": "./cadence/contracts/FooContract.cdc",

_11

"Bar": "./cadence/contracts/BarContract.cdc"

_11

},

_11

"deployments": {

_11

"testnet": {

_11

"my-testnet-account": ["Foo", "Bar"]

_11

}

_11

}

_11

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/deployment/project-contracts.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Start Emulator](/build/tools/flow-cli/deployment/start-emulator)[Next

Deploy a Project](/build/tools/flow-cli/deployment/deploy-project-contracts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Add a Contract](#add-a-contract)
* [Define Contract Deployment Targets](#define-contract-deployment-targets)

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
* [EVM](/build/evm/about)

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