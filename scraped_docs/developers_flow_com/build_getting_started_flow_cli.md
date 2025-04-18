# Source: https://developers.flow.com/build/getting-started/flow-cli

Local Development with Flow CLI | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)

  + [Contract Interaction](/build/getting-started/contract-interaction)
  + [Local Development](/build/getting-started/flow-cli)
  + [Simple Frontend](/build/getting-started/fcl-quickstart)
* [Flow Protocol](/build/basics/network-architecture)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Getting Started
* Local Development

On this page

# Local Development

The [Flow Command Line Interface](/tools/flow-cli) (CLI) is a set of tools that developers can use to interact with the Flow blockchain by managing accounts, sending transactions, deploying smart contracts, running the emulator, and more. This quickstart will get you familiar with its main concepts and functionality.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Create a Flow project using the [Flow Command Line Interface](/tools/flow-cli)
* Run tests for a smart contract
* Add an already-deployed contract to your project with the [Dependency Manager](/tools/flow-cli/dependency-manager)
* Deploy a smart contract locally to the Flow Emulator
* Write and execute scripts to interact with a deployed smart contract

## Installation[​](#installation "Direct link to Installation")

The first thing you'll need to do is install the Flow CLI. If you have [homebrew](https://brew.sh/) installed you can run:

`_10

brew install flow-cli`

For other ways of installing, please refer to the [installation guide](/tools/flow-cli/install).

## Creating a New Project[​](#creating-a-new-project "Direct link to Creating a New Project")

To create a new project, navigate to the directory where you want to create your project and run:

`_10

flow init`

Upon running this command, you'll be prompted to enter a project name. Enter a name and press `Enter`.

You'll also be asked if you'd like to install any core contracts (such as `FungibleToken`, `NonFungibleToken`, etc.) using the [Dependency Manager](/tools/flow-cli/dependency-manager). For this tutorial, you can select `No`.

The `init` command will create a new directory with the project name and the following files:

* `flow.json`: This file contains the configuration for your project.
* `emulator-account.pkey`: This file contains the private key for the default emulator account.
* `flow.json`: This file contains the configuration for your project.
* `cadence/`: This directory contains your Cadence code. Inside there are subdirectories for contracts, scripts, transactions, and tests.

Inside the `cadence/contracts` directory, you'll find a `Counter.cdc` file. This is the same as the `Counter` contract in the previous step.

Next, `cd` into your new project directory.

info

For additional details on how `flow.json` is configured, review the [configuration docs](/tools/flow-cli/flow.json/configuration).

### Running the Tests[​](#running-the-tests "Direct link to Running the Tests")

To run the example test for the `Counter` contract located in `cadence/tests`, you can run:

`_10

flow test`

tip

For a more detailed guide on running Cadence tests, check out the [tests documentation](/tools/flow-cli/tests).

## Deploying the Contract to Emulator[​](#deploying-the-contract-to-emulator "Direct link to Deploying the Contract to Emulator")

The emulator is a local version of the Flow blockchain that you can use to test your contracts and scripts. It's a great way to develop and test your contracts locally - before you try them on the `testnet` or `mainnet`.

Before we deploy, let's open a new terminal window and run the emulator. From the root of your project directory, where your `emulator-account.pkey` and `flow.json` files are located, run:

`_10

flow emulator start`

Your emulator will now be running.

### Deploying a Contract[​](#deploying-a-contract "Direct link to Deploying a Contract")

#### Creating an Account[​](#creating-an-account "Direct link to Creating an Account")

When you created a project you'll see that a `Counter` contract was added to your `flow.json` configuration file, but it's not set up for deployment yet. We could deploy it to the automatically created `emulator-account`, but for this example lets also create a new account on the emulator to deploy it to.

info

**Reminder**: On Flow Cadence, contracts are deployed to the storage of the account that deploys them.

Leave your emulator running, and open a second terminal. Run the following command:

`_10

flow accounts create`

When prompted, give your account the name `test-account` and select `Emulator` as the network. You'll now see this account in your `flow.json`.

#### Configuring the Deployment[​](#configuring-the-deployment "Direct link to Configuring the Deployment")

To deploy the `Counter` contract to the emulator, you'll need to add it to your project configuration. You can do this by running:

`_10

flow config add deployment`

First, pick `emulator` as the network for deployment. Select your `test-account` as the account to deploy to. Next, pick `Counter` as the contract to deploy. Finally, choose `no` when asked if you wish to deploy more contracts.

#### Deploying the Contract[​](#deploying-the-contract "Direct link to Deploying the Contract")

To deploy the `Counter` contract to the emulator, run:

`_10

flow project deploy`

You'll see something similar to:

`_10

Deploying 1 contracts for accounts: test-account

_10

_10

Counter -> 0x179b6b1cb6755e31 (a98c155fe7afc8eb2af5551748759b08a80a0ae85d1b09f92f1afc293c61ca98)

_10

_10

🎉 All contracts deployed successfully`

That's it! You've just deployed your first contract to the Flow Emulator.

You can't deploy the same contract to multiple accounts at the same time with the `deploy` command. If you've experimented with the above, you may need to manually edit the `"deployments"` property in `flow.json` to remove extra deployments.

:::

## Running Scripts[​](#running-scripts "Direct link to Running Scripts")

Scripts are used to read data from the Flow blockchain. There is no state modification. In our case, we are going to read a greeting from the `HelloWorld` contract.

If we wanted to generate a new script, we could run:

`_10

flow generate script ScriptName`

But the default project already has a `GetCounter` script for reading the count of the `Counter` contract. Open `cadence/scripts/GetCounter.cdc` in your editor to see the script.

To run the script, you can run:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc`

You should see zero as the result since the `Counter` contract initializes the count to zero and we haven't run any transactions to increment it.

`_10

Result: 0`

tip

If you'll like to learn more about writing scripts, please check out the docs for [basic scripts](/build/basics/scripts).

## Executing Transactions[​](#executing-transactions "Direct link to Executing Transactions")

Transactions are used to modify the state of the blockchain. In our case, we want to increment the count of the `Counter` contract. Luckily, we already have a transaction for that in the project that was generated for us. Open `cadence/transactions/IncrementCounter.cdc` in your editor to see the transaction.

To run the transaction, you can run:

`_10

flow transactions send cadence/transactions/IncrementCounter.cdc`

By default, this uses the `emulator-account` to sign the transaction and the emulator network. If you want to use your `test-account` account, you can specify the `--signer` flag with the account name.

`_33

Transaction ID: 9cc7ac4d3d5239016965aba89b9692d3401a48a090d1ad1a8d9ef9cfca685e6e

_33

_33

Block ID b8537860b0fc9ca8b3195b121e762502f9a220874b605d6a810998e8b62321a3

_33

Block Height 3

_33

Status ✅ SEALED

_33

ID 9cc7ac4d3d5239016965aba89b9692d3401a48a090d1ad1a8d9ef9cfca685e6e

_33

Payer f8d6e0586b0a20c7

_33

Authorizers [f8d6e0586b0a20c7]

_33

_33

Proposal Key:

_33

Address f8d6e0586b0a20c7

_33

Index 0

_33

Sequence 1

_33

_33

No Payload Signatures

_33

_33

Envelope Signature 0: f8d6e0586b0a20c7

_33

Signatures (minimized, use --include signatures)

_33

_33

Events:

_33

Index 0

_33

Type A.179b6b1cb6755e31.Counter.CounterIncremented

_33

Tx ID 9cc7ac4d3d5239016965aba89b9692d3401a48a090d1ad1a8d9ef9cfca685e6e

_33

Values

_33

- newCount (Int): 1

_33

_33

_33

_33

Code (hidden, use --include code)

_33

_33

Payload (hidden, use --include payload)

_33

_33

Fee Events (hidden, use --include fee-events)`

Run the script to check the counter again. You'll see that it has incremented:

`_10

Result: 0`

tip

If you want to learn more about writing transactions, please read the docs for [basic transactions](/build/basics/transactions).

## Installing & Interacting With External Dependencies[​](#installing--interacting-with-external-dependencies "Direct link to Installing & Interacting With External Dependencies")

In addition to creating your own contracts, you can also install contracts that have already been deployed to the network by using the [Dependency Manager](/tools/flow-cli/dependency-manager). This is useful for interacting with contracts that are part of the Flow ecosystem or that have been deployed by other developers.

For example, let's say we want to format the result of our `GetCounter` script so that we display the number with commas if it's greater than 999. To do that we can install a contract called [`NumberFormatter`](https://contractbrowser.com/A.8a4dce54554b225d.NumberFormatter) from `testnet` that has a function to format numbers.

To grab it, run:

`_10

flow dependencies install testnet://8a4dce54554b225d.NumberFormatter`

When prompted for the account to deploy the contract to, select any account and ignore the prompt for an alias. This is if you wanted to configure a `mainnet` address for the contract.

This will add the `NumberFormatter` contract and any of its dependencies to an `imports` directory in your project. It will also add any dependencies to your `flow.json` file. In addition, the prompt will configure the deployment of the contract to the account you selected. Make sure to select the `emulator-account` account to deploy the contract to the emulator.

You'll then see the `NumberFormatter` in your deployments for emulator in your `flow.json`.

Now we can deploy the `NumberFormatter` contract to the emulator by running:

`_10

flow project deploy`

`_10

Deploying 2 contracts for accounts: test-account

_10

_10

Counter -> 0x179b6b1cb6755e31 [skipping, no changes found]

_10

NumberFormatter -> 0x179b6b1cb6755e31 (f8ce6dfa1771c7bad216e72e7f7aac7f1987c4261d425d27e689c701b9ec69cd)

_10

_10

🎉 All contracts deployed successfully`

Now that we have the `NumberFormatter` contract deployed, we can update our `GetCounter` script to format the result. Open `cadence/scripts/GetCounter.cdc` and update it to use the following code:

`_14

import "Counter"

_14

import "NumberFormatter"

_14

_14

access(all)

_14

fun main(): String {

_14

// Retrieve the count from the Counter contract

_14

let count: Int = Counter.getCount()

_14

_14

// Format the count using NumberFormatter

_14

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_14

_14

// Return the formatted count

_14

return formattedCount

_14

}`

The things to note here are:

* We import the `NumberFormatter` contract.
* We call the `formatWithCommas` function from the `NumberFormatter` contract to format the count.
* We return the formatted count as a `String`.

warning

Do **not** simply add a new file. Use `flow generate transaction IncrementBy1000.cdc`

Add a new transaction called `IncrementBy1000.cdc`. Fill it with a variant of `IncrementCounter.cdc` that instead loops through the `increment` function 1000 times.

`_21

import "Counter"

_21

_21

transaction {

_21

_21

prepare(acct: &Account) {

_21

// Authorizes the transaction

_21

}

_21

_21

execute {

_21

// Increment the counter 1000 times

_21

var i = 0

_21

while i < 1000 {

_21

Counter.increment()

_21

i = i + 1

_21

}

_21

_21

// Retrieve the new count and log it

_21

let newCount = Counter.getCount()

_21

log("New count after incrementing: ".concat(newCount.toString()))

_21

}

_21

}`

Try out your new transaction with:

`_10`

Finally, to test the updated script, you can run:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc`

You should now see the result with commas.

info

If you're a Solidity developer, did you catch what we just did here? We updated the features and functionality available in the smart contract **without updating the contract itself!**

Even more importantly, we did this **without needing access or permission.** You can use the power of composability in Flow Cadence to add new features to contracts you don't own.

## More[​](#more "Direct link to More")

If you want to continue on generating your own contracts, you can also use the the `generate` subcommand to create a new contract file. See more in the [`generate` documentation](/tools/flow-cli/boilerplate).

After that, it's easy to add your contract to your project configuration using the Flow CLI [`config` commands](/tools/flow-cli/flow.json/manage-configuration).

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, we've accomplished all of our learning objectives:

1. ✅ Created a Flow project using the Flow CLI

   * Initialized a new project with `flow init`
   * Set up the project structure with contracts, scripts, and tests
   * Configured the project using `flow.json`
2. ✅ Ran tests for a smart contract

   * Executed the example test for the `Counter` contract
   * Learned about the testing capabilities of the Flow CLI
3. ✅ Added an already-deployed contract to your project

   * Used the Dependency Manager to install the `NumberFormatter` contract
   * Configured the contract deployment in `flow.json`
   * Deployed the contract to the emulator
4. ✅ Deployed a smart contract locally to the Flow Emulator

   * Started the Flow Emulator
   * Created a test account
   * Deployed the `Counter` contract to the emulator
   * Deployed the `NumberFormatter` contract
5. ✅ Wrote and executed scripts to interact with deployed contracts

   * Created and executed the `GetCounter` script
   * Modified the script to use the `NumberFormatter` contract
   * Created and executed the `IncrementBy1000` transaction
   * Demonstrated the power of Cadence's composability

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/getting-started/flow-cli.md)

Last updated on **Apr 16, 2025** by **Brian Doyle**

[Previous

Contract Interaction](/build/getting-started/contract-interaction)[Next

Simple Frontend](/build/getting-started/fcl-quickstart)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Installation](#installation)
* [Creating a New Project](#creating-a-new-project)
  + [Running the Tests](#running-the-tests)
* [Deploying the Contract to Emulator](#deploying-the-contract-to-emulator)
  + [Deploying a Contract](#deploying-a-contract)
* [Running Scripts](#running-scripts)
* [Executing Transactions](#executing-transactions)
* [Installing & Interacting With External Dependencies](#installing--interacting-with-external-dependencies)
* [More](#more)
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