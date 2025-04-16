# Source: https://developers.flow.com/tools/flow-cli/deployment/project-contracts

Add Project Contracts | Flow Developer Portal



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

    - [Start Emulator](/tools/flow-cli/deployment/start-emulator)
    - [Add Project Contracts](/tools/flow-cli/deployment/project-contracts)
    - [Deploy a Project](/tools/flow-cli/deployment/deploy-project-contracts)
    - [Create Emulator Snapshot](/tools/flow-cli/deployment/emulator-snapshot)
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
* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/deployment/project-contracts.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

[Previous

Start Emulator](/tools/flow-cli/deployment/start-emulator)[Next

Deploy a Project](/tools/flow-cli/deployment/deploy-project-contracts)

###### Rate this page

😞😐😊

* [Add a Contract](#add-a-contract)
* [Define Contract Deployment Targets](#define-contract-deployment-targets)

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