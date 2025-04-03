# Source: https://developers.flow.com/tools/flow-cli/dependency-manager

Dependency Manager | Flow Developer Portal



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
* [Use Cursor AI](/tools/cursor)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
* Dependency Manager

On this page

# Dependency Manager

The Dependency Manager in the Flow CLI streamlines the development process when you use contracts from outside your project. It eliminates the manual tasks of copying, pasting, and updating contracts that you use or build upon, such as core contracts or any other ecosystem contracts.

For example, if you wanted to build a new application using the `FlowToken` contract, you would traditionally need to locate the contract on the network, copy it into your local project, and add it to your `flow.json`. You would repeat this process for each import (dependency) it relies on, like the `NonFungibleToken` contract. The Dependency Manager simplifies this process with a few straightforward commands.

## `install`[​](#install "Direct link to install")

The `install` command allows you to install dependencies and all their sub-dependencies with ease. You can use it to install specific dependencies or to install all dependencies listed in your `flow.json`.

### Installing Specific Dependencies[​](#installing-specific-dependencies "Direct link to Installing Specific Dependencies")

If you know the address and name of the contract you want to install (which can often be found via the [Contract Browser](https://contractbrowser.com/)), you can use the following syntax:

`_10

flow dependencies install testnet://7e60df042a9c0868.FlowToken`

In this command, the string `testnet://7e60df042a9c0868.FlowToken` used as the `source` in the `flow.json` is broken down as:

* **Network:** `testnet`
* **Address:** `7e60df042a9c0868`
* **Contract Name:** `FlowToken`

This specifies the remote source of the contract on the network that will be used as the source of truth.

### Installing Core Contracts Using Simplified Syntax[​](#installing-core-contracts-using-simplified-syntax "Direct link to Installing Core Contracts Using Simplified Syntax")

For core contracts, you can use a simplified syntax that defaults to the Flow Mainnet:

`_10

flow dependencies install FlowToken`

This command is functionally equivalent to:

`_10

flow dependencies install mainnet://1654653399040a61.FlowToken`

### Installing Multiple Dependencies[​](#installing-multiple-dependencies "Direct link to Installing Multiple Dependencies")

You can also install multiple dependencies at once. For example:

`_10

flow dependencies install testnet://7e60df042a9c0868.FlowToken NonFungibleToken`

This command installs both the `FlowToken` contract from Testnet and the `NonFungibleToken` contract from Mainnet.

### Installing All Dependencies From an Address[​](#installing-all-dependencies-from-an-address "Direct link to Installing All Dependencies From an Address")

Sometimes you may want to install all the contracts that exist at a particular address, rather than specifying each contract name individually. You can do this by omitting the contract name in the dependency source. For example:

`_10

flow dependencies install testnet://7e60df042a9c0868`

This tells the Dependency Manager to fetch every contract deployed at the `7e60df042a9c0868` address on `testnet` and store them in your `imports` folder. You can later import these contracts in your code or use them in your deployments as needed.

### Installing Dependencies from `flow.json`[​](#installing-dependencies-from-flowjson "Direct link to installing-dependencies-from-flowjson")

If you run the `install` command without specifying any dependencies, it will install all the dependencies listed in your `flow.json` file and ensure they are up to date:

`_10

flow dependencies install`

This command checks all the dependencies specified in your `flow.json`, installs them, and updates them if there have been changes on the network.

### Example `flow.json` Entry[​](#example-flowjson-entry "Direct link to example-flowjson-entry")

After installing, your `flow.json` might include an entry like:

`_10

{

_10

"dependencies": {

_10

"FlowToken": {

_10

"source": "testnet://7e60df042a9c0868.FlowToken",

_10

"aliases": {

_10

"emulator": "0ae53cb6e3f42a79"

_10

}

_10

}

_10

}

_10

}`

### Other Things to Note[​](#other-things-to-note "Direct link to Other Things to Note")

* After installation, a local folder named `imports` will be created. It's recommended to add this folder to your `.gitignore`, as it stores your dependencies locally.
* If the contracts change on the network, the Dependency Manager will prompt you to update the local dependencies in your `imports` folder. The hash saved in the dependency object is used for this check, so avoid removing it.
* Dependencies function just like local contracts. You can add them to [`deployments` in your `flow.json`](/tools/flow-cli/deployment/deploy-project-contracts) and run `flow project deploy`. You can also import them in your scripts, transactions, and contracts (e.g., `import "FlowToken"`).
* Core contract aliases are automatically added for you across all networks.

## `discover`[​](#discover "Direct link to discover")

The `discover` command helps you interactively find and install core contracts for your project. Core contracts are standard smart contracts maintained by the Flow Foundation and are commonly used across the Flow ecosystem (learn more about core contracts [here](/build/core-contracts)).

To use the `discover` command, run:

`_10

flow dependencies discover`

You'll be presented with a list of available core contracts to install:

`_15

Select any core contracts you would like to install or skip to continue.

_15

Use arrow keys to navigate, space to select, enter to confirm or skip, q to quit:

_15

_15

> [ ] FlowEpoch

_15

[ ] FlowIDTableStaking

_15

[ ] FlowClusterQC

_15

[ ] FlowDKG

_15

[ ] FlowServiceAccount

_15

[ ] NodeVersionBeacon

_15

[ ] RandomBeaconHistory

_15

[ ] FlowStorageFees

_15

[ ] FlowFees

_15

[ ] FungibleTokenSwitchboard

_15

[ ] EVM

_15

[ ] Crypto`

After selecting the contracts, press `enter` to confirm. The selected contracts will be added to your `flow.json` file and will be accessible in your project.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/dependency-manager.md)

Last updated on **Mar 28, 2025** by **Brian Doyle**

[Previous

Development Tools](/tools/flow-cli/utils/tools)[Next

Running Cadence Tests](/tools/flow-cli/tests)

###### Rate this page

😞😐😊

* [`install`](#install)
  + [Installing Specific Dependencies](#installing-specific-dependencies)
  + [Installing Core Contracts Using Simplified Syntax](#installing-core-contracts-using-simplified-syntax)
  + [Installing Multiple Dependencies](#installing-multiple-dependencies)
  + [Installing All Dependencies From an Address](#installing-all-dependencies-from-an-address)
  + [Installing Dependencies from `flow.json`](#installing-dependencies-from-flowjson)
  + [Example `flow.json` Entry](#example-flowjson-entry)
  + [Other Things to Note](#other-things-to-note)
* [`discover`](#discover)

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