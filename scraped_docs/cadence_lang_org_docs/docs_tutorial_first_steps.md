# Source: https://cadence-lang.org/docs/tutorial/first-steps

First Steps | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)

  + [First Steps](/docs/tutorial/first-steps)
  + [Hello World](/docs/tutorial/hello-world)
  + [Resources and the Move (<-) Operator](/docs/tutorial/resources)
  + [Capabilities](/docs/tutorial/capabilities)
  + [Basic NFT](/docs/tutorial/non-fungible-tokens-1)
  + [Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)
  + [Fungible Tokens](/docs/tutorial/fungible-tokens)
  + [7. Marketplace Setup](/docs/tutorial/marketplace-setup)
  + [8. Marketplace](/docs/tutorial/marketplace-compose)
  + [9. Voting Contract](/docs/tutorial/voting)
  + [10. Composable Resources](/docs/tutorial/resources-compose)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Tutorial
* First Steps

On this page

# First Steps

Welcome to our series of guides that get you up to speed on [Cadence](/docs/) as quickly as possible! In this program, we jump right into making meaningful projects. Don't worry, we'll point you to the important parts of the language reference as each concept is introduced.

This series makes use of the [Flow Playground](https://play.flow.com), an online IDE that enables you to easily write and test Cadence code in a simulated environment.

tip

If you already know Solidity, you might want to review the [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence). It compares the two languages and points out the most impactful differences from the perspective of a Solidity dev.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Write, deploy, and interact with Cadence code in the Flow Playground.
* Select and utilize accounts in the Flow Playground.
* Run Cadence transactions and scripts from the playground.
* Explore the contracts and storage associated with test accounts.

## The Flow Developer Playground[​](#the-flow-developer-playground "Direct link to The Flow Developer Playground")

![Flow Playground](/assets/images/flow-playground-d8e582729bd65805261fb268e0cbcd24.png)

The [Flow Playground](https://play.flow.com) includes an in-browser editor and Flow emulator that you can use to experiment with Flow Cadence. Using the Flow Playground, you can write Cadence smart contracts, deploy them to a local Flow emulated blockchain, and submit transactions.

It has been primarily tested and optimized for Google Chrome, but other browsers should also work.

The playground comes pre-loaded with contract and transaction templates that correspond to each of the tutorials in this series. The tutorials also include a link (e.g., [play.flow.com/367d1462-f291-481f-aa14-02bb5ce3e897](https://play.flow.com/367d1462-f291-481f-aa14-02bb5ce3e897)), which opens the tutorial code in a new tab. The contracts, transactions, and scripts are loaded into the templates in the Playground for you to use.

You'll need to navigate between the editor and this tutorial to read the instructions and make changes to your code.

## What is a smart contract?[​](#what-is-a-smart-contract "Direct link to What is a smart contract?")

In regular terms, a contract is an agreement between two parties to exchange information or assets. Normally, the terms of a contract are supervised and enforced by a trusted and empowered third party, such as a bank or a lawyer.

A smart contract is a computer program stored in a blockchain that verifies and executes the performance of a contract without the need for any trusted third party. The code itself is public and will perform all operations in an open, repeatable, and testable manner.

Programs that run on blockchains are commonly referred to as smart contracts because they facilitate important functions, such as managing digital currency, without relying on a central authority like a bank.

Flow can run smart contracts written in [Cadence](/docs/). It can also run contracts written in Solidity on [Flow EVM](https://developers.flow.com/evm/about). These guides focus on learning Cadence.

## Accounts[​](#accounts "Direct link to Accounts")

Accounts are the primary conduit for user interaction with on-chain code and assets. Users authorize transactions with their accounts and store their owned assets in their account storage.

warning

Flow is different from other blockchains in that contracts, assets, and information owned by a user or associated with their wallet address **are stored in the user's account**.

We use the `warning` label above to get your attention, but this is a **good thing**! In most other chains, a coding error that accidentally changes a single number in a ledger can destroy, change, or duplicate ownership of an asset or assets. It's like a medieval shop with a bunch of paper IOUs having a gust of wind blow through vs. having the gold in your pocket.

The model of ownership in Cadence makes this kind of loss nearly impossible.

The Flow playground comes with pre-created accounts that you can use for testing and experimentation.

They're listed in the `Accounts` section on the bottom left part of the playground window.

![Playground Intro](/assets/images/playground-intro-bcac060064d5516b7003ab27799b858d.png)

Click on a few of the accounts. They're empty when first created, but you'll see contracts and storage data here as you go through the tutorials.

![Account View](/assets/images/playground-account-view-0641f931973d84f8edbf916c566fbcdc.png)

## Contracts[​](#contracts "Direct link to Contracts")

The playground organizes contract source files under the `Contracts` folder in the nav panel on the left side of the window. Until deployed, these are source files not associated with an account or address.

### Deploying a contract[​](#deploying-a-contract "Direct link to Deploying a contract")

The default contract in a new playground session is a simple `HelloWorld` contract. To deploy:

1. Open the Cadence code in the account editor that contains a contract.
2. Click the `Deploy` button in the bottom-right of the screen to deploy that contract to the currently selected account.
   ![Deploy Contract](/assets/images/deploybox-15c80d99bfacdb110394351320484810.png)

   :   *The contract deploys after a few seconds.*
3. Select `0x06-Default` in the **ACCOUNTS** list.

Here's what happens:

* The name of the contract and the block height it was deployed at appear in the list of `Deployed Contracts`.
* `FlowToken` objects are listed in the `Account Storage` section.
* Every Flow account is created with the ability to manage Flow Tokens.

![Full Storage View](/assets/images/full-storage-8cef94047c943e06ba94e2fcc5def2f9.png)

## Scripts[​](#scripts "Direct link to Scripts")

In Cadence, scripts are simple, transaction-like snippets of code that you can use to **read** onchain data that is public.

Open the `GetGreeting` script and `Execute` it.

This script loads the instance of the `HelloWorld` contract you deployed with account `0x06` and returns the result of calling the `hello` function, which is the value stored onchain in the contract's `greeting` field.

You'll see the `result` logged in the console.

## Transactions[​](#transactions "Direct link to Transactions")

Cadence transactions are also written in Cadence.

### Executing a transaction[​](#executing-a-transaction "Direct link to Executing a transaction")

In the `Transactions` folder, you'll find an example of one:

1. Open the `ChangeGreeting` transaction.
2. Enter a new `greeting` and `Send` it.
   * This executes a transaction to call `changeGreeting` and update the value in `greeting` for this specific instance of `HelloWorld`, deployed by address `0x06`.
   * Once the transaction completes, you'll see the output in the `Log` at the bottom of the window.
3. Open the `GetGreeting` script and `Execute` it again.

You'll now see your new greeting returned in the log!

## Say Hello, World![​](#say-hello-world "Direct link to Say Hello, World!")

You're now ready to write your own contract and say "Hello World!"

Now that you have completed the tutorial, you can:

* Write, deploy, and interact with Cadence code in the Flow Playground.
* Select and utilize accounts in the Flow Playground.
* Run Cadence transactions and scripts from the playground.
* Explore the contracts and storage associated with test accounts.

**Tags:**

* [reference](/docs/tags/reference)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/01-first-steps.md)

[Previous

Why Use Cadence?](/docs/why)[Next

Hello World](/docs/tutorial/hello-world)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [The Flow Developer Playground](#the-flow-developer-playground)
* [What is a smart contract?](#what-is-a-smart-contract)
* [Accounts](#accounts)
* [Contracts](#contracts)
  + [Deploying a contract](#deploying-a-contract)
* [Scripts](#scripts)
* [Transactions](#transactions)
  + [Executing a transaction](#executing-a-transaction)
* [Say Hello, World!](#say-hello-world)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.