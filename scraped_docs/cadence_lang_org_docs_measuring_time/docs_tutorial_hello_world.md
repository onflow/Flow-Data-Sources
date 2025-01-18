# Source: https://cadence-lang.org/docs/tutorial/hello-world




2. Hello World | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
  + [1. First Steps](/docs/tutorial/first-steps)
  + [2. Hello World](/docs/tutorial/hello-world)
  + [3. Resource Contract Tutorial](/docs/tutorial/resources)
  + [4. Capability Tutorial](/docs/tutorial/capabilities)
  + [5.1 Non-Fungible Token Tutorial Part 1](/docs/tutorial/non-fungible-tokens-1)
  + [5.2 Non-Fungible Token Tutorial Part 2](/docs/tutorial/non-fungible-tokens-2)
  + [6. Fungible Token Tutorial](/docs/tutorial/fungible-tokens)
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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Tutorial
* 2. Hello World
On this page
# 2. Hello World

In this tutorial, we'll write and deploy our first smart contract!

tip

Open the starter code for this tutorial in the Flow Playground:   


[<https://play.flow.com/483b2f33-9e71-40aa-924a-2c5f0ead77aa>](https://play.flow.com/483b2f33-9e71-40aa-924a-2c5f0ead77aa)

The tutorial will ask you to take various actions to interact with this code.


Action

Instructions that require you to take action are always included in a callout
box like this one. These highlighted actions are all that you need to do to
get your code running, but reading the rest is necessary to understand the
language's design.

This tutorial will walk you through an example of a smart contract that implements basic Cadence features,
including accounts, transactions, and signers.

Our "Hello World" smart contract will:

1. Create and initialize a smart contract with a single field of type `String`
2. Initialize the field with the phrase "Hello, World!"
3. Create a function in the contract that returns our greeting

We will deploy this contract in an account, then use a transaction to interact with the contract,
and finally discuss the role of signers in the transaction.

## How to Use Playground[​](#how-to-use-playground "Direct link to How to Use Playground")

For this tutorial, you'll be using the [Flow Playground](https://play.flow.com),
an interactive web interface that lets you write and run smart contracts in a test environment.
It also allows you to save and share your work with others so that you can test smart contracts collaboratively.

When you work with accounts in the Flow Playground, you start with five default accounts that you can change and reconfigure.
Each account in your environment has a unique address, and you can select an account in the bottom left toolbar,
which will open up the contracts that are saved for that account.
The `HelloWorld` contracts are loaded by default for each account
unless you load an existing playground project with other saved contracts.

For this tutorial, you'll be working with only the first account `0x06`

## Implementing Hello World[​](#implementing-hello-world "Direct link to Implementing Hello World")

---

You will start by using a smart contract that contains a public function that returns `"Hello World!"`.

Like most other blockchains, the programming model in Flow is centered around accounts and transactions.
All state that persists permanently is stored in [accounts](/docs/language/accounts)
and all accounts have the same core functionality. (users, smart contracts, data storage).
This is unlike other blockchains like Ethereum where there are two types of accounts
(smart contract accounts and user accounts).

The interfaces to this state (the ways to interact with it, otherwise known as methods or functions) are also stored in accounts.
All code execution takes place within [transactions](/docs/language/transactions),
which are blocks of code that are authorized and submitted by external users
to interact with the persistent state, which includes directly modifying account storage.

A smart contract is a collection of code (its functions) and data (its state) that lives in the contract area of an account in Flow.
Each account can have zero or more contracts and/or contract interfaces.
A contract can be freely added, removed, or updated (with some restrictions) by the owner of the account.
Now let's look at the `HelloWorld` contract that you'll be working through in this tutorial.

Action

If you haven't already, you'll need to follow this link to open a playground session with the Hello World contracts, transactions, and scripts pre-loaded:

[<https://play.flow.com/483b2f33-9e71-40aa-924a-2c5f0ead77aa>](https://play.flow.com/483b2f33-9e71-40aa-924a-2c5f0ead77aa)

![Playground Intro](/assets/images/playground-intro-514e99da776669e9dbe1f4375dad280a.png)

Action

Open the Account `0x06` tab with the file called
`HelloWorld.cdc` in the Contract 1 space.   

`HelloWorld.cdc` should contain this code:


HelloWorld.cdc `_19// HelloWorld.cdc_19//_19access(all) contract HelloWorld {_19_19 // Declare a public (access(all)) field of type String._19 //_19 // All fields must be initialized in the initializer._19 access(all) let greeting: String_19_19 // The initializer is required if the contract contains any fields._19 init() {_19 self.greeting = "Hello, World!"_19 }_19_19 // Public function that returns our friendly greeting!_19 access(all) view fun hello(): String {_19 return self.greeting_19 }_19}`

The line `access(all) contract HelloWorld`  declares a contract
that is accessible in all scopes (`access(all)`, typically known as public).
It's followed by `access(all) let greeting: String` which declares a state constant (`let`) of type `String` that is accessible in all scopes(`access(all)`).

You would have used `var` to declare a variable, which means that the value
can be changed later on by code in the contract instead of remaining constant like with `let`.

They are both examples of an access control specification that means an interface can be accessed in all scopes, but not written to in all scopes.
For more information about the different levels of access control permitted in Cadence, refer to the [Access Control section of the language reference](/docs/language/access-control).

The `init()` section is called the initializer. It is a special function that only runs when the contract is first created.
Objects similar to contracts, such as other [composite types like structs or resources](/docs/language/composite-types),
require that the initializer initializes all fields that are declared in a composite type.
In the above example, the initializer sets the `greeting` field to `"Hello, World!"` when the contract is initialized.

The last part of our `HelloWorld` contract is a public function called `hello()`.
This declaration returns a value of type `String`.
Anyone who imports this contract in their transaction or script can read the public fields,
use the public types, and call the public contract functions; i.e. the ones that have `access(all)` or `access(all)` specified.

Soon you'll deploy this contract to your account and run a transaction that calls its function, but first, let's look at what accounts and transactions are.

### Accounts and Transactions[​](#accounts-and-transactions "Direct link to Accounts and Transactions")

---

#### What is an Account?[​](#what-is-an-account "Direct link to What is an Account?")

Each user has an account controlled by one or more private keys with configurable weight.
This means that support for accounts/wallets with [multiple controllers](https://www.coindesk.com/what-is-a-multisignature-crypto-wallet)
is built into the protocol by default.

An account is divided into two main areas:

1. The first area is the [contract area](/docs/language/accounts/contracts).
   This is the area that stores smart contracts containing type definitions, fields, and functions that relate to common functionality.
   There is no limit to the number of smart contracts an account can store.
   This area cannot be directly accessed in a transaction unless the transaction is just returning (reading) a copy of the code deployed to an account.
   The owner of an account can directly add or update contracts that are deployed to it.
2. The second area is the [account storage](/docs/language/accounts/storage).
   This area is where an account stores the objects that they own.
   This is an important differentiator between Cadence and other languages,
   because in other languages, assets that accounts own are always stored in the centralized
   smart contract that defines the assets. In Cadence, each account stores its assets
   as objects directly in its own account storage.
   The account storage section also stores code that declares the capabilities
   for controlling how these stored objects can be accessed.
   We'll cover account storage and capabilities in more detail in a later tutorial.

In this tutorial, we use the account with the address `0x06` to store our `HelloWorld` contract.

### Deploying Code[​](#deploying-code "Direct link to Deploying Code")

---

Now that you know what an account is in a Cadence context, you can deploy the `HelloWorld` contract to your account.

Action

Make sure that the account `0x06` tab is selected and that the
`HelloWorld.cdc` file is in the editor.   

Click the deploy button to deploy the contents of the editor to account `0x06`.

![Deploy Contract](/assets/images/deploybox-23f3152e93e6cd42c99adec556cebd6c.png)

You should see a log in the output area indicating that the deployment succeeded.

`Deployed Contract To: 0x06`

You'll also see the name of the contract show up in the selected account tab underneath the number for the account.
This indicates that the `HelloWorld` contract has been deployed to the account.
You can always look at this tab to verify which contracts are in which accounts.
In the Flow Playground environment there can be any number of contracts for each account.
To create an additional contract, either open up one of the other ones or click the plus (+)
button next to the contracts section in the playground.

### Creating a Transaction[​](#creating-a-transaction "Direct link to Creating a Transaction")

---

A [Transaction](/docs/language/transactions) in Flow is defined as an arbitrary-sized block of Cadence code that is authorized by one or more accounts.
When an account authorizes a transaction, the code in that transaction has access to the authorizers' private storage.
An account authorizes a transaction by performing a cryptographic signature on the transaction with the account's private key,
which should only be accessible to the account owner.
In addition to being able to access the authorizer's private assets,
transactions can also read and call functions in public contracts, and access public functions in other users' accounts.
For this tutorial, we use a transaction to call our `hello()` function.

Action

Open the transaction named `Simple Transaction`   

`Simple Transaction` should contain this code:


SayHello.cdc `_10import HelloWorld from 0x06_10_10transaction {_10_10 prepare(acct: &Account) {}_10_10 execute {_10 log(HelloWorld.hello())_10 }_10}`

This transaction first imports our `HelloWorld` smart contract from the account `0x06`.
If you haven't deployed the smart contract from the account, the transaction won't have access to it and the import will fail.
This imports the entire contract code from `HelloWorld`, including type definitions and public functions,
so that the transaction can use them to interact with the `HelloWorld` contract in account `0x06`.

To import a smart contract from any other account, type this line at the top of your transaction:

 `_10// Replace {ContractName} with the name of the contract you want to import_10// and {Address} with the account you want to import it from_10import {ContractName} from {Address}`

Transactions are divided into two main phases, `prepare` and `execute`.

1. The `prepare` phase is required but we don't use it in this tutorial.
   We'll cover this phase in a later tutorial.
2. The `execute` phase is the main body of a transaction.
   It can call functions on external contracts and objects and perform operations on data that was initialized in the transaction.
   In this example, the `execute` phase calls `HelloWorld.hello()`.
   This executes the `hello()` function in the `HelloWorld` contract
   and logs the result(`log(HelloWorld.hello())`) to the console.

Action

In the box at the bottom right of the editor, select Account `0x06` as the transaction signer.   

Click the `Send` button to submit the transaction

You should see something like this in the transaction results at the bottom of the screen:

 `_10Simple Transaction "Hello, World!"`

Congratulations, you just executed your first Cadence transaction with the account `0x06` as the signer.

In this tutorial, you'll get the same result if you use different signers for the transaction
but later tutorials will use more complex examples that have different results depending on the signer.

## Reviewing HelloWorld[​](#reviewing-helloworld "Direct link to Reviewing HelloWorld")

This tutorial covered an introduction to Cadence, including terms like accounts, transactions, and signers.
We implemented a smart contract that is accessible in all scopes.
The smart contract had a `String` field initialized with the value `Hello, World!` and a function to return (read) this value.
Next, we deployed this contract in an account and implemented a transaction to call the function in the smart contract and log the result to the console.
Finally, we used the account `0x06` as the signer for this transaction.

Now that you have completed the tutorial, you have the basic knowledge to write a simple Cadence program that can:

* Deploy a basic smart contract in an account
* Interact with the smart contract using a transaction
* Sign the transaction with one or multiple signers

Feel free to modify the smart contract to implement different functions,
experiment with the available [Cadence types](/docs/language/values-and-types),
and write new transactions that execute multiple functions from your `HelloWorld` smart contract.

**Tags:**

* [reference](/docs/tags/reference)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/02-hello-world.md)[Previous1. First Steps](/docs/tutorial/first-steps)[Next3. Resource Contract Tutorial](/docs/tutorial/resources)
###### Rate this page

😞😐😊

* [How to Use Playground](#how-to-use-playground)
* [Implementing Hello World](#implementing-hello-world)
  + [Accounts and Transactions](#accounts-and-transactions)
  + [Deploying Code](#deploying-code)
  + [Creating a Transaction](#creating-a-transaction)
* [Reviewing HelloWorld](#reviewing-helloworld)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

