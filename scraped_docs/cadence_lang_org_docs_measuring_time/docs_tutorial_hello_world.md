# Source: https://cadence-lang.org/docs/tutorial/hello-world




Hello World | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

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
* Hello World
On this page
# Hello World

It's time to write your own "Hello World" contract. In this instance, the contract will:

1. Create and initialize a smart contract with a single field of type `String`.
2. Initialize the field with the phrase "Hello, World!".
3. Create a function in the contract that returns our greeting.

We will deploy this contract in an account, use a transaction to interact with the contract, and finally, explore the role of signers in a transaction.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Declare a public Cadence smart contract.
* Initialize a public `String` variable.
* Write simple transactions and scripts in Cadence.
* Describe the role of signers in a Cadence transaction.

## Implementing Hello World[​](#implementing-hello-world "Direct link to Implementing Hello World")

Action

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/e559739d-603e-40d5-b2f1-b9957051cdc4>](https://play.flow.com/e559739d-603e-40d5-b2f1-b9957051cdc4)

It's empty!

Action

Begin by declaring your contract.


 `_10access(all) contract HelloWorld {_10 // Todo_10}`
### Declare a Contract-Level Constant[​](#declare-a-contract-level-constant "Direct link to Declare a Contract-Level Constant")

The line `access(all) contract HelloWorld`  declares a contract with [Access Control](/docs/language/access-control) that is accessible in all scopes - or public.

Action

Add a public constant `String` field to store your greeting.


 `_10// Incomplete code example_10// An error is expected here, see below_10_10// Declare a public (access(all)) field of type String._10access(all) let greeting: String`
warning

Cadence follows the same pattern as Swift where the `let` keyword is used to declare a constant. The `var` keyword is used to declare a variable.

As before, you're using the `access` keyword to set the scope to `all` and make the constant public. The `let` keyword declares a state constant named `greeting`, and the [type annotation](/docs/language/type-annotations) declares it as a `String`.

You've probably noticed the error that your code is `missing initializer for field `greeting` in type `HelloWorld``

[Composite Types](/docs/language/composite-types), which includes contracts, have a special initializer function that is run exactly once, upon object creation. It's optional, but constants declared at the contract level must have a value set in the initializer.

Action

Add an initializer and initialize your `greeting`.


 `_10// The initializer is required if the contract contains any fields._10init() {_10 self.greeting = "Hello, World!"_10}`
### Add a View Function[​](#add-a-view-function "Direct link to Add a View Function")

You've created a contract and initialized the `"Hello, World!"` `String`. The next step is to:

Action

Implement a `view` function to return the `greeting` constant.


 `_10// Public function that returns our friendly greeting!_10access(all) view fun hello(): String {_10 return self.greeting_10}`

Once again, the access level is public. Anyone who imports this contract into their own contract, transaction, or script can read the public fields, use the public types, and call the public contract functions - the ones that have `access(all)` specified.

The `view` annotation indicates that the function is permitted to view, but not modify blockchain state.

## Accounts[​](#accounts "Direct link to Accounts")

Each user has an account controlled by one or more private keys with configurable weight. This means that support for accounts/wallets with [multiple controllers](https://www.coindesk.comwhat-is-a-multisignature-crypto-wallet) is built into the protocol by default.

An account is divided into several areas:

* *Contracts*
* *Account Storage*
* *Capabilities*
* *Keys*

### Contract Area[​](#contract-area "Direct link to Contract Area")

The first area is the [contract area](/docs/language/accounts/contracts), or `account.contracts`.

This is the area that stores smart contracts deployed to the account. These contracts contain type definitions, fields, and functions that relate to common functionality. There is no limit to the number of smart contracts an account can store.

tip

Much of the functionality that you'd find in a Solidity smart contract is instead written in [transactions](/docs/language/transactions) or scripts for Cadence apps. These exist outside the smart contract, which means you don't need to anticipate absolutely everything you might want to do or view before deploying the contract.

The information in the contract area cannot be directly accessed in a transaction unless the transaction imports the contract or returns (reads) a copy of the code deployed to an account.

The owner of an account can directly add or update contracts that are deployed to it.

Important

On Flow Cadence, **smart contracts *are* upgradeable**. If you make a mistake, you can often [update](/docs/language/contract-updatability) it, constrained by some rules, in a public and transparent manner.

### Account Storage[​](#account-storage "Direct link to Account Storage")

The second area is where you'll find [account storage](/docs/language/accounts/storage), or `account.storage`. This area is where an account stores the objects that it owns. This is an important differentiator between Cadence and other languages, because in other languages, assets that accounts own are usually stored in the centralized smart contract ledger that defines the assets.

Important

In Cadence, **each account stores its assets as objects directly in its own account storage, like how you store your own possessions in your own house in real life**!

The account storage section also stores code that declares the capabilities for controlling how these stored objects can be accessed. We'll cover account storage and capabilities in more detail in a later tutorial.

In this tutorial, we'll use the account with the address `0x06` to store our `HelloWorld` contract.

### Capabilities[​](#capabilities "Direct link to Capabilities")

[Capabilities](/docs/language/capabilities), or `account.capabilities`, are a part of the security model in Cadence. They represent the right to access parts or all of an object and perform operations on it. For example, a user might possess a vault that holds fungible tokens. For it, they'll have a capability that allows anyone to deposit tokens into the vault, and may choose to grant the capability to withdraw tokens to their broker's account.

### Keys[​](#keys "Direct link to Keys")

[Keys](/docs/language/accounts/keys), or `account.keys`, are used to sign [transactions](/docs/language/transactions). In Cadence, an account can have many keys. These keys can be shared or revoked, providing native version of [account abstraction](https://ethereum.org/en/roadmap/account-abstraction) that is extremely powerful. For example, you can use it [build an app](https://developers.flow.com/build/guides/account-linking-with-dapper) that pulls NFTs in an embedded wallet in one app into that user's browser wallet and use them in your app.

## Deploying the HelloWorld Contract[​](#deploying-the-helloworld-contract "Direct link to Deploying the HelloWorld Contract")

Action

Make sure that the account `0x06` tab is selected and that the
`HelloWorld.cdc` file is in the editor.

Click the deploy button to deploy the contents of the editor to account `0x06`.

![Deploy Contract](/assets/images/deploybox-15c80d99bfacdb110394351320484810.png)

You should see a log in the output area indicating that the deployment succeeded.

 `_10Deployed Contract To: 0x06`

You'll also see the name of the contract in the selected account tab underneath the number for the account. This indicates that the `HelloWorld` contract has been deployed to the account.

You can always look at this tab to verify which contracts are in which accounts.

## Transactions[​](#transactions "Direct link to Transactions")

A [Transaction](/docs/language/transactions) in Flow is defined as an arbitrary-sized block of Cadence code that is authorized by one or more accounts.

When an account authorizes a transaction, the code in that transaction has access to the authorizers' private storage.

An account authorizes a transaction by performing a cryptographic signature on the transaction with the account's private key, which should only be accessible to the account owner.

In addition to being able to access the authorizer's private assets, transactions can also read and call functions in public contracts, and access public functions in other users' accounts.

For this tutorial, we'll use a transaction to call our `hello()` function.

Action

Open the `CallHello` file in the `Transactions` folder.

First, you'll need to import the **deployed instance** of `HelloWorld` from account `0x06`. If you haven't deployed the smart contract from the account, the transaction won't have access to it and the import will fail.

Action

Add an `import` at the top of the file.


 `_10import HelloWorld from 0x06`

This imports the entire contract code from `HelloWorld`, including type definitions and public functions, so that the transaction can use them to interact with the `HelloWorld` contract in account `0x06`.

To import any smart contract from any account, you can use this format:

 `_10// Replace {ContractName} with the name of the contract you want to import_10// and {Address} with the account you want to import it from_10import {ContractName} from {Address}`

Transactions are written in Cadence and are declared with the `transaction` keyword.

Action

Declare an empty `transaction`.


 `_10transaction {_10 // TODO_10}`
### Transaction Process[​](#transaction-process "Direct link to Transaction Process")

Transactions are divided into two main phases, `prepare` and `execute`.

The [`prepare`](/docs/language/transactions#prepare-phase) phase is required and is used to identify the account(s) that will sign the transaction. It's also used when the transaction needs to access the account(s) that signed the transaction. The latter is not needed for this simple transaction.

Action

Add an empty `prepare` statement to your transaction.


 `_10prepare(acct: &Account) {_10 // Nothing is needed here for now_10}`

The `execute` phase is the main body of a transaction. It can call functions on external contracts and objects and perform operations on data that was initialized in the transaction.

Action

Add an `execute` block to your transaction and use it to `log` the output of the `hello()` function from the imported `HelloWorld` contract to the console.


 `_10execute {_10 log(HelloWorld.hello())_10}`

In this example, the `execute` phase calls `HelloWorld.hello()`. This executes the `hello()` function in the `HelloWorld` contract
and logs the result(`log(HelloWorld.hello())`) to the console.

Action

In the box at the bottom right of the editor, select Account `0x06` as the transaction signer.

Click the `Send` button to submit the transaction

You should see something like this in the transaction results at the bottom of the screen:

 `_1016:46:56_10Simple Transaction_10[1]_10Cadence log: "Hello, World!"`

Congratulations, you just executed your first Cadence transaction with the account `0x06` as the signer!

In this tutorial, you'll get the same result if you use different signers for the transaction but later tutorials will use more complex examples that have different results depending on the signer.

## Conclusion[​](#conclusion "Direct link to Conclusion")

This tutorial covered an introduction to Cadence, including terms like accounts, transactions, and signers. We implemented a smart contract that is accessible in all scopes. The smart contract had a `String` field initialized with the value `Hello, World!` and a function to return (read) this value.

Next, we deployed this contract in an account and implemented a transaction to call the function in the smart contract and log the result to the console. Finally, we used the account `0x06` as the signer for this transaction.

Now that you have completed the tutorial, you can:

* Declare a public Cadence smart contract.
* Initialize a public `String` variable.
* Write simple transactions in Cadence.
* Describe the role of signers in a Cadence transaction.
**Tags:**

* [reference](/docs/tags/reference)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/02-hello-world.md)[PreviousFirst Steps](/docs/tutorial/first-steps)[NextResources and the Move (<-) Operator](/docs/tutorial/resources)
###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Implementing Hello World](#implementing-hello-world)
  + [Declare a Contract-Level Constant](#declare-a-contract-level-constant)
  + [Add a View Function](#add-a-view-function)
* [Accounts](#accounts)
  + [Contract Area](#contract-area)
  + [Account Storage](#account-storage)
  + [Capabilities](#capabilities)
  + [Keys](#keys)
* [Deploying the HelloWorld Contract](#deploying-the-helloworld-contract)
* [Transactions](#transactions)
  + [Transaction Process](#transaction-process)
* [Conclusion](#conclusion)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

