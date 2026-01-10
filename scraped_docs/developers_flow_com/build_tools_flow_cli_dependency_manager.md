# Source: https://developers.flow.com/build/tools/flow-cli/dependency-manager

Dependency Manager | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                      - [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Dependency Manager

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

For core contracts (and [DeFiActions](https://github.com/onflow/FlowActions/tree/main?tab=readme-ov-file#deployments)), you can use a simplified syntax that defaults to the Flow Mainnet:

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
* Dependencies function just like local contracts. You can add them to [`deployments` in your `flow.json`](/build/tools/flow-cli/deployment/deploy-project-contracts) and run `flow project deploy`. You can also import them in your scripts, transactions, and contracts (e.g., `import "FlowToken"`).
* Core contract aliases are automatically added for you across all networks.

## `discover`[​](#discover "Direct link to discover")

The `discover` command helps you interactively find and install core contracts for your project. Core contracts are standard smart contracts maintained by the Flow Foundation and are commonly used across the Flow ecosystem (learn more about core contracts [here](/build/cadence/core-contracts)).

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

## `list`[​](#list "Direct link to list")

The `list` command displays all the dependencies currently installed in your project. This is useful for reviewing what contracts your project depends on and their sources.

To list your installed dependencies, run:

`_10

flow dependencies list`

This command will show you all the dependencies from your `flow.json` file along with their source information, helping you keep track of what external contracts your project is using.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/dependency-manager.md)

Last updated on **Sep 22, 2025** by **Chase Fleming**

[Previous

Development Tools](/build/tools/flow-cli/utils/tools)[Next

Running Cadence Tests](/build/tools/flow-cli/tests)

###### Rate this page

😞😐😊

Copy as Markdown

* [`install`](#install)
  + [Installing Specific Dependencies](#installing-specific-dependencies)+ [Installing Core Contracts Using Simplified Syntax](#installing-core-contracts-using-simplified-syntax)+ [Installing Multiple Dependencies](#installing-multiple-dependencies)+ [Installing All Dependencies From an Address](#installing-all-dependencies-from-an-address)+ [Installing Dependencies from `flow.json`](#installing-dependencies-from-flowjson)+ [Example `flow.json` Entry](#example-flowjson-entry)+ [Other Things to Note](#other-things-to-note)* [`discover`](#discover)* [`list`](#list)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.