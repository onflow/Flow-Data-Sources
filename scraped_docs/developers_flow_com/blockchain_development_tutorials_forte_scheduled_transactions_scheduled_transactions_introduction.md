# Source: https://developers.flow.com/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction

Introduction to Scheduled Transactions | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      + [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)

        + [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)

          - [Introduction to Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction)+ [DeFi Math Utils](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Forte Network Upgrade](/blockchain-development-tutorials/forte)* [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)* Introduction to Scheduled Transactions

On this page

# Introduction to Scheduled Transactions

warning

Scheduled transactions are a new feature that is under development and is a part of [FLIP 330](https://github.com/onflow/flips/pull/331/files). Currently, they only work in the emulator and testnet. We're close to finishing the specific implementation, but it but may change during the development process.

We will update these tutorials, but you may need to refactor your code if the implementation changes.

# Overview

Flow, EVM, and other blockchains are a form of a **single** shared computer that anyone can use, with no admin privileges, super user roles, or complete control. For this to work, it must be impossible for any user to freeze the computer, on purpose or by accident.

As a result, most blockchain computers, including EVM and Solana, aren't [Turing Complete](https://en.wikipedia.org/wiki/Turing_completeness), because they can't run an unbounded loop. Each transaction must occur within one block, and can't consume more gas than the limit.

While this limitation prevents infinite loops, it makes it so that you can't do anything 100% onchain if you need it to happen at a later time or after a trigger. As a result, developers must often build products that involve a fair amount of traditional infrastructure and requires users to give those developers a great amount of trust that their backend will execute the promised task.

Flow fixes this problem with *scheduled transactions*. Scheduled Transactions let smart contracts execute code at, or after, a chosen time without an external transaction. You schedule work now and the network executes it later. This allows recurring jobs, deferred actions, and autonomous workflows.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After you complete this tutorial, you will be able to:

* Understand the concept of scheduled transactions and how they solve blockchain limitations.
* Explain the key components of the `FlowTransactionScheduler` system.
* Implement a basic scheduled transaction using the provided scaffold.
* Analyze the structure and flow of scheduled transaction transactions.
* Create custom scheduled transaction contracts and handlers.
* Evaluate the benefits and use cases of scheduled transactions in DeFi applications.

# Prerequisites

## Cadence Programming Language[​](#cadence-programming-language "Direct link to Cadence Programming Language")

This tutorial assumes you have a modest knowledge of [Cadence](https://cadence-lang.org/docs). If you don't, you can follow along, but you'll get more out of it if you complete our series of [Cadence](https://cadence-lang.org/docs) tutorials. Most developers find it more pleasant than other blockchain languages, and it's not hard to pick up.

## Getting Started[​](#getting-started "Direct link to Getting Started")

To start, run `flow init` and select `Scheduled Transactions project`. Open the project.

The `readme` file has a robust getting started guide. Complete that to set up and run the demo scheduled transaction. It doesn't seem like much at first. The counter was at `0`, you ran a transaction, now it's at `1`. What's the big deal?

Let's try again to make it clearer what's happening. Open `cadence/transactions/ScheduleIncrementIn.cdc` and look at the arguments for the transaction:

`_10

transaction(

_10

delaySeconds: UFix64,

_10

priority: UInt8,

_10

executionEffort: UInt64,

_10

transactionData: AnyStruct?

_10

)`

The first parameter is the delay in seconds for the scheduled transaction. Let's try running it again. You'll need to be quick on the keyboard, so feel free to use a higher number of `delaySeconds` if you need to. You're going to:

1. Call the script to view the counter.
2. Call the transaction to schedule the counter to increment after 10 seconds.
3. Call the script to view the counter again and verify that it hasn't changed yet.
4. Wait 10 seconds, call it again, and confirm the counter incremented.

For your convenience, the updated transaction call is:

`_10

flow transactions send cadence/transactions/ScheduleIncrementIn.cdc \

_10

--network emulator --signer emulator-account \

_10

--args-json '[

_10

{"type":"UFix64","value":"20.0"},

_10

{"type":"UInt8","value":"1"},

_10

{"type":"UInt64","value":"1000"},

_10

{"type":"Optional","value":null}

_10

]'`

And the call to run the script to get the count is:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc --network emulator`

The result in your terminal should be similar to:

`_37

briandoyle@Mac scheduled-transactions-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 2

_37

_37

briandoyle@Mac scheduled-transactions-scaffold % flow transactions send cadence/transactions/ScheduleIncrementIn.cdc \

_37

--network emulator --signer emulator-account \

_37

--args-json '[

_37

{"type":"UFix64","value":"10.0"},

_37

{"type":"UInt8","value":"1"},

_37

{"type":"UInt64","value":"1000"},

_37

{"type":"Optional","value":null}

_37

]'

_37

Transaction ID: 61cc304cee26ad1311cc1b0bbcde23bf2b3a399485c2b6b8ab621e429abce976

_37

Waiting for transaction to be sealed...⠹

_37

_37

Block ID 6b9f5138901cd0d299adea28e96d44a6d8b131ef58a9a14a072a0318da0ad16b

_37

Block Height 671

_37

Status ✅ SEALED

_37

ID 61cc304cee26ad1311cc1b0bbcde23bf2b3a399485c2b6b8ab621e429abce976

_37

Payer f8d6e0586b0a20c7

_37

Authorizers [f8d6e0586b0a20c7]

_37

_37

# Output omitted for brevity

_37

_37

briandoyle@Mac scheduled-transactions-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 2

_37

_37

_37

briandoyle@Mac scheduled-transactions-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 2

_37

_37

_37

briandoyle@Mac scheduled-transactions-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 3`

### Review of the Existing Contract and Transactions[​](#review-of-the-existing-contract-and-transactions "Direct link to Review of the Existing Contract and Transactions")

If you're not familiar with `cadence/contracts/Counter.cdc` review it. This is the standard contract created by default when you run `flow init`. It's very simple, with a counter and public functions to increment or decrement it.

### Transaction Handler[​](#transaction-handler "Direct link to Transaction Handler")

Next, open `cadence/contracts/CounterTransactionHandler.cdc`

`_34

import "FlowTransactionScheduler"

_34

import "Counter"

_34

_34

access(all) contract CounterTransactionHandler {

_34

_34

/// Handler resource that implements the Scheduled Transaction interface

_34

access(all) resource Handler: FlowTransactionScheduler.TransactionHandler {

_34

access(FlowTransactionScheduler.Execute) fun executeTransaction(id: UInt64, data: AnyStruct?) {

_34

Counter.increment()

_34

let newCount = Counter.getCount()

_34

log("Transaction executed (id: ".concat(id.toString()).concat(") newCount: ").concat(newCount.toString()))

_34

}

_34

_34

access(all) view fun getViews(): [Type] {

_34

return [Type<StoragePath>(), Type<PublicPath>()]

_34

}

_34

_34

access(all) fun resolveView(_ view: Type): AnyStruct? {

_34

switch view {

_34

case Type<StoragePath>():

_34

return /storage/CounterTransactionHandler

_34

case Type<PublicPath>():

_34

return /public/CounterTransactionHandler

_34

default:

_34

return nil

_34

}

_34

}

_34

}

_34

_34

/// Factory for the handler resource

_34

access(all) fun createHandler(): @Handler {

_34

return <- create Handler()

_34

}

_34

}`

This contract is simple. It contains a [resource](https://cadence-lang.org/docs/language/resources) that has a function with the `FlowTransactionScheduler.Execute` [entitlement](https://cadence-lang.org/docs/language/access-control#entitlements). This function contains the code that the scheduled transaction calls. It:

1. Calls the `increment` function in the `Counter` contract.
2. Fetches the current value in the counter.
3. Logs that value to the console **for the emulator**.

It also contains functions to get metadata about the handler and a function, `createHandler`, which creates and returns an instance of the `Handler` resource. There are other metadata views that could be good to include in your Handler, but we're sticking to the basic ones for now.

### Initializing the Transaction Handler[​](#initializing-the-transaction-handler "Direct link to Initializing the Transaction Handler")

Next, take a look at `cadence/transactions/InitCounterTransactionHandler.cdc`:

`_23

import "CounterTransactionHandler"

_23

import "FlowTransactionScheduler"

_23

_23

transaction() {

_23

prepare(signer: auth(Storage, Capabilities) &Account) {

_23

// Save a handler resource to storage if not already present

_23

if signer.storage.borrow<&AnyResource>(from: /storage/CounterTransactionHandler) == nil {

_23

let handler <- CounterTransactionHandler.createHandler()

_23

signer.storage.save(<-handler, to: /storage/CounterTransactionHandler)

_23

}

_23

_23

// Validation/example that we can create an issue a handler capability with correct entitlement for FlowTransactionScheduler

_23

let _ = signer.capabilities.storage

_23

.issue<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>(/storage/CounterTransactionHandler)

_23

_23

// Issue a non-entitled public capability for the handler that is publicly accessible

_23

let publicCap = signer.capabilities.storage

_23

.issue<&{FlowTransactionScheduler.TransactionHandler}>(/storage/CounterTransactionHandler)

_23

_23

// publish the capability

_23

signer.capabilities.publish(publicCap, at: /public/CounterTransactionHandler)

_23

}

_23

}`

This transaction saves an instance of the `Handler` resource to the user's [storage](https://cadence-lang.org/docs/language/accounts/storage). It also tests out/demonstrates how to issue the handler [capability] with the `FlowTransactionScheduler.Execute` [entitlement](https://cadence-lang.org/docs/language/access-control#entitlements) and how to publish an un-entitled capability to the handler so it can be publicly accessible. The use of the name `_` is convention to name a variable we don't intend to use for anything.

### Scheduling the Transaction[​](#scheduling-the-transaction "Direct link to Scheduling the Transaction")

Finally, open `cadence/transactions/ScheduleIncrementIn.cdc` again. This is the most complicated transaction, so we'll break it down. The final call other than the `log` is what actually schedules the transaction:

`_10

manager.schedule(

_10

handlerCap: handlerCap,

_10

data: transactionData,

_10

timestamp: future,

_10

priority: pr,

_10

executionEffort: executionEffort,

_10

fees: <-fees

_10

)`

It calls the `schedule` function from the `FlowTransactionSchedulerUtils.Manager` contract. This function has parameters for:

* `handlerCap`: The handler [capability] for the code that should execute.

This was created above during the previous transaction with:

`_10

let handlerCap = signer.capabilities.storage

_10

.issue<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>(/storage/CounterTransactionHandler)`

That line creates a capability with the `FlowTransactionScheduler.Execute` entitlement. That entitlement permits calling the function (`executeTransaction()`) from the `Handler` resource in `CounterTransactionHandler.cdc` that you created and stored an instance of in the `InitCounterTransactionHandler` transaction.

Then, in the schedule transaction, we retrieve the handler capability that we created before.
We created two separate handlers, a public and a private one, so we have to make sure we're getting the private one:

`_13

// Get the entitled capability that will be used to create the transaction

_13

// Need to check both controllers because the order of controllers is not guaranteed

_13

var handlerCap: Capability<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>? = nil

_13

_13

if let cap = account.capabilities.storage

_13

.getControllers(forPath: /storage/CounterTransactionHandler)[0]

_13

.capability as? Capability<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}> {

_13

handlerCap = cap

_13

} else {

_13

handlerCap = account.capabilities.storage

_13

.getControllers(forPath: /storage/CounterTransactionHandler)[1]

_13

.capability as! Capability<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>

_13

}`

* `data`: The arguments required by the transaction function.

In this example, `transactionData` is passed in as a prop on the transaction and is `null`.

* `timestamp`: The timestamp for the time in the `future` that this transaction should be run.

The transaction call has an argument for `delaySeconds`, which is then converted to a `future` timestamp:

`_10

let future = getCurrentBlock().timestamp + delaySeconds`

* `priority`: The priority this transaction is given in the event of network congestion. A higher priority means a higher fee for higher precedence.

The `priority` argument is supplied in the transaction as a `UInt8` for convenience, then converted into the appropriate [enum](https://cadence-lang.org/docs/language/enumerations) type:

`_10

let pr = priority == 0

_10

? FlowTransactionScheduler.Priority.High

_10

: priority == 1

_10

? FlowTransactionScheduler.Priority.Medium

_10

: FlowTransactionScheduler.Priority.Low`

The `executionEffort` is also supplied as an argument in the transaction. This represents the gas limit for your transaction and used to prepare the estimate for the gas fees that must be paid for the transaction, and directly in the call to `schedule()` the transaction.

* `fees`: A [vault](https://developers.flow.com/build/cadence/guides/fungible-token#vaults-on-flow) containing the appropriate amount of gas fees needed to pay for the execution of the scheduled transaction.

To create the vault, the `estimate()` function calculates the amount needed:

`_10

let est = FlowTransactionScheduler.estimate(

_10

data: transactionData,

_10

timestamp: future,

_10

priority: pr,

_10

executionEffort: executionEffort

_10

)`

Then, an [authorized reference](https://cadence-lang.org/docs/language/references#authorized-references) to the signer's vault is created and used to `withdraw()` the needed funds and [move](https://cadence-lang.org/docs/language/operators/assign-move-force-swap#move-operator--) them into the `fees` variable, which is then sent in the `schedule()` function call.

Finally, we also `assert` that some minimums are met to ensure the transaction will be called:

`_10

assert(

_10

est.timestamp != nil || pr == FlowTransactionScheduler.Priority.Low,

_10

message: est.error ?? "estimation failed"

_10

)`

## Using the FlowTransactionSchedulerUtils.Manager[​](#using-the-flowtransactionschedulerutilsmanager "Direct link to Using the FlowTransactionSchedulerUtils.Manager")

The `FlowTransactionSchedulerUtils.Manager` resource provides a safer and more convenient way to manage scheduled transactions. Instead of directly calling the `FlowTransactionScheduler` contract,
you can use the Manager resource that manages all your scheduled transactions from a single place and handles many of the common patterns to reduce boilerplate code.
It also provides many convenient functions to get detailed information about all the transactions you have scheduled by timestamp, handler, and so on.
When setting up a manager, you also publish a capability for it so it is easy for scripts
to query your account and also see what transactions are scheduled!

### Setting Up the Manager[​](#setting-up-the-manager "Direct link to Setting Up the Manager")

First, you need to create and store a Manager resource in your account:

`_16

import "FlowTransactionSchedulerUtils"

_16

import "FlowToken"

_16

import "FungibleToken"

_16

_16

transaction() {

_16

prepare(signer: auth(Storage, Capabilities) &Account) {

_16

// Create and save the Manager resource

_16

let manager <- FlowTransactionSchedulerUtils.createManager()

_16

signer.storage.save(<-manager, to: FlowTransactionSchedulerUtils.managerStoragePath)

_16

_16

// Create a capability for the Manager

_16

let managerCap = signer.capabilities.storage.issue<&FlowTransactionSchedulerUtils.Manager>(FlowTransactionSchedulerUtils.managerStoragePath)

_16

_16

signer.capabilities.publish(managerCap, at: FlowTransactionSchedulerUtils.managerPublicPath)

_16

}

_16

}`

### Scheduling Transactions with the Manager[​](#scheduling-transactions-with-the-manager "Direct link to Scheduling Transactions with the Manager")

The Manager provides a `schedule` method that simplifies the scheduling process:

`_10

manager.schedule(

_10

handlerCap: handlerCap,

_10

data: transactionData,

_10

timestamp: future,

_10

priority: priority,

_10

executionEffort: executionEffort,

_10

fees: <-fees

_10

)`

The Manager also provides utility methods for:

* Scheduling another transaction with a previously used handler.
* Getting scheduled transaction information in many different ways.
* Canceling scheduled transactions.
* Managing transaction handlers.
* Querying transaction status.

## Writing a New Scheduled Transaction[​](#writing-a-new-scheduled-transaction "Direct link to Writing a New Scheduled Transaction")

With this knowledge, we can create our own scheduled transaction. For this demo, we'll simply display a hello from an old friend in the emulator's console logs.

### Creating the Contracts[​](#creating-the-contracts "Direct link to Creating the Contracts")

To start, use the [Flow CLI](https://developers.flow.com/tools/flow-cli) to create a new contract called `RickRoll.cdc` and one called `RickRollTransactionHandler.cdc`:

`_10

flow generate contract RickRoll

_10

flow generate contract RickRollTransactionHandler`

Open the `RickRoll` contract and add functions to log a fun message to the emulator console, and a variable to track which message to call:

`_29

access(all)

_29

contract RickRoll {

_29

_29

access(all) var messageNumber: UInt8

_29

_29

init() {

_29

self.messageNumber = 0

_29

}

_29

_29

// Reminder: Anyone can call these functions!

_29

access(all) fun message1() {

_29

log("Never gonna give you up")

_29

self.messageNumber = 1

_29

}

_29

_29

access(all) fun message2() {

_29

log("Never gonna let you down")

_29

self.messageNumber = 2

_29

}

_29

_29

access(all) fun message3() {

_29

log("Never gonna run around and desert you")

_29

self.messageNumber = 3

_29

}

_29

_29

access(all) fun resetMessageNumber() {

_29

self.messageNumber = 0

_29

}

_29

}`

Next, open `RickRollTransactionHandler.cdc`. Import the `RickRoll` contract, `FlowToken`, `FungibleToken`, and `FlowTransactionScheduler`, and stub out the `Handler` and factory:

`_17

import "FlowTransactionScheduler"

_17

import "RickRoll"

_17

import "FlowToken"

_17

import "FungibleToken"

_17

_17

access(all)

_17

contract RickRollTransactionHandler {

_17

/// Handler resource that implements the Scheduled Transaction interface

_17

access(all) resource Handler: FlowTransactionScheduler.TransactionHandler {

_17

// TODO

_17

}

_17

_17

/// Factory for the handler resource

_17

access(all) fun createHandler(): @Handler {

_17

return <- create Handler()

_17

}

_17

}`

Next, add a switch to call the appropriate function based on what the current `messageNumber` is and add the metadata getters:

`_31

access(all) resource Handler: FlowTransactionScheduler.TransactionHandler {

_31

access(FlowTransactionScheduler.Execute) fun executeTransaction(id: UInt64, data: AnyStruct?) {

_31

switch (RickRoll.messageNumber) {

_31

case 0:

_31

RickRoll.message1()

_31

case 1:

_31

RickRoll.message2()

_31

case 2:

_31

RickRoll.message3()

_31

case 3:

_31

return

_31

default:

_31

panic("Invalid message number")

_31

}

_31

}

_31

_31

access(all) view fun getViews(): [Type] {

_31

return [Type<StoragePath>(), Type<PublicPath>()]

_31

}

_31

_31

access(all) fun resolveView(_ view: Type): AnyStruct? {

_31

switch view {

_31

case Type<StoragePath>():

_31

return /storage/RickRollTransactionHandler

_31

case Type<PublicPath>():

_31

return /public/RickRollTransactionHandler

_31

default:

_31

return nil

_31

}

_31

}

_31

}`

We could move forward with this, but it would be more fun to have each transaction schedule the follow transaction to share the next message. To do this, move most of the code found in the transaction to the handler. Start with configuring the `delay`, `future`, `priority`, and `executionEffort`. We'll hardcode these for simplicity:

`_10

var delay: UFix64 = 5.0

_10

let future = getCurrentBlock().timestamp + delay

_10

let priority = FlowTransactionScheduler.Priority.Medium

_10

let executionEffort: UInt64 = 1000`

Next, create the `estimate` and `assert` to validate minimums are met, and that the `Handler` exists:

`_24

let estimate = FlowTransactionScheduler.estimate(

_24

data: data,

_24

timestamp: future,

_24

priority: priority,

_24

executionEffort: executionEffort

_24

)

_24

_24

assert(

_24

estimate.timestamp != nil || priority == FlowTransactionScheduler.Priority.Low,

_24

message: estimate.error ?? "estimation failed"

_24

)

_24

_24

// Ensure a handler resource exists in the contract account storage

_24

if RickRollTransactionHandler.account.storage.borrow<&AnyResource>(from: /storage/RickRollTransactionHandler) == nil {

_24

let handler <- RickRollTransactionHandler.createHandler()

_24

RickRollTransactionHandler.account.storage.save(<-handler, to: /storage/RickRollTransactionHandler)

_24

_24

// Issue a non-entitled public capability for the handler that is publicly accessible

_24

let publicCap = RickRollTransactionHandler.account.capabilities.storage

_24

.issue<&{FlowTransactionScheduler.TransactionHandler}>(/storage/RickRollTransactionHandler)

_24

_24

// publish the capability

_24

RickRollTransactionHandler.capabilities.publish(publicCap, at: /public/RickRollTransactionHandler)

_24

}`

Then withdraw the necessary funds:

`_10

let vaultRef = CounterLoopTransactionHandler.account.storage

_10

.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)

_10

?? panic("missing FlowToken vault on contract account")

_10

let fees <- vaultRef.withdraw(amount: estimate.flowFee ?? 0.0) as! @FlowToken.Vault`

Finally, schedule the transaction:

`_16

_16

// borrow a reference to the scheduled transaction manager

_16

let manager = RickRollTransactionHandler.account.storage.borrow<auth(FlowTransactionSchedulerUtils.Owner) &{FlowTransactionSchedulerUtils.Manager}>(from: FlowTransactionSchedulerUtils.managerStoragePath)

_16

?? panic("Could not borrow a Manager reference from \(FlowTransactionSchedulerUtils.managerStoragePath)")

_16

_16

let handlerTypeIdentifier = manager.getHandlerTypes().keys[0]!

_16

_16

manager.scheduleByHandler(

_16

handlerTypeIdentifier: handlerTypeIdentifier,

_16

handlerUUID: nil,

_16

data: data,

_16

timestamp: future,

_16

priority: priority,

_16

executionEffort: executionEffort,

_16

fees: <-fees

_16

)`

As you can see, this time, we didn't have to get the handler capability.
This is because the manager stores a history of handlers that you have used in the past
so that you can easily just specify the type of the handler that you want to schedule for
and it will schedule it for you.

### Setting Up the Transactions[​](#setting-up-the-transactions "Direct link to Setting Up the Transactions")

Next, you need to add transactions to initialize the new transaction handler, and another to fire off the sequence.

Start by adding `InitRickRollHandler.cdc`:

`_10

flow generate transaction InitRickRollHandler`

The transaction itself is nearly identical to the one we reviewed:

`_24

import "RickRollTransactionHandler"

_24

import "FlowTransactionScheduler"

_24

_24

transaction() {

_24

prepare(signer: auth(Storage, Capabilities) &Account) {

_24

// Save a handler resource to storage if not already present

_24

if signer.storage.borrow<&AnyResource>(from: /storage/RickRollTransactionHandler) == nil {

_24

let handler <- RickRollTransactionHandler.createHandler()

_24

signer.storage.save(<-handler, to: /storage/RickRollTransactionHandler)

_24

_24

// Validation/example that we can create an issue a handler capability with correct entitlement for FlowTransactionScheduler

_24

signer.capabilities.storage

_24

.issue<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>(/storage/RickRollTransactionHandler)

_24

_24

// Issue a non-entitled public capability for the handler that is publicly accessible

_24

let publicCap = signer.capabilities.storage

_24

.issue<&{FlowTransactionScheduler.TransactionHandler}>(/storage/RickRollTransactionHandler)

_24

_24

// publish the capability

_24

signer.capabilities.publish(publicCap, at: /public/RickRollTransactionHandler)

_24

_24

}

_24

}

_24

}`

Next, add `ScheduleRickRoll`:

`_10

flow generate transaction ScheduleRickRoll`

This transaction is essentially identical as well, it just uses the `handlerCap` stored in `RickRollTransaction`:

`_78

import "FlowTransactionScheduler"

_78

import "FlowToken"

_78

import "FungibleToken"

_78

_78

/// Schedule a Rick Roll with a delay of delaySeconds

_78

transaction(

_78

delaySeconds: UFix64,

_78

priority: UInt8,

_78

executionEffort: UInt64,

_78

transactionData: AnyStruct?

_78

) {

_78

prepare(signer: auth(Storage, Capabilities) &Account) {

_78

let future = getCurrentBlock().timestamp + delaySeconds

_78

_78

let pr = priority == 0

_78

? FlowTransactionScheduler.Priority.High

_78

: priority == 1

_78

? FlowTransactionScheduler.Priority.Medium

_78

: FlowTransactionScheduler.Priority.Low

_78

_78

let est = FlowTransactionScheduler.estimate(

_78

data: transactionData,

_78

timestamp: future,

_78

priority: pr,

_78

executionEffort: executionEffort

_78

)

_78

_78

assert(

_78

est.timestamp != nil || pr == FlowTransactionScheduler.Priority.Low,

_78

message: est.error ?? "estimation failed"

_78

)

_78

_78

let vaultRef = signer.storage

_78

.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)

_78

?? panic("missing FlowToken vault")

_78

let fees <- vaultRef.withdraw(amount: est.flowFee ?? 0.0) as! @FlowToken.Vault

_78

_78

// if a transaction scheduler manager has not been created for this account yet, create one

_78

if !signer.storage.check<@{FlowTransactionSchedulerUtils.Manager}>(from: FlowTransactionSchedulerUtils.managerStoragePath) {

_78

let manager <- FlowTransactionSchedulerUtils.createManager()

_78

signer.storage.save(<-manager, to: FlowTransactionSchedulerUtils.managerStoragePath)

_78

_78

// create a public capability to the scheduled transaction manager

_78

let managerRef = signer.capabilities.storage.issue<&{FlowTransactionSchedulerUtils.Manager}>(FlowTransactionSchedulerUtils.managerStoragePath)

_78

signer.capabilities.publish(managerRef, at: FlowTransactionSchedulerUtils.managerPublicPath)

_78

}

_78

_78

// Get a capability to the handler stored in this contract account

_78

// Get the entitled capability that will be used to create the transaction

_78

// Need to check both controllers because the order of controllers is not guaranteed

_78

var handlerCap: Capability<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>? = nil

_78

_78

if let cap = signer.capabilities.storage

_78

.getControllers(forPath: /storage/RickRollTransactionHandler)[0]

_78

.capability as? Capability<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}> {

_78

handlerCap = cap

_78

} else {

_78

handlerCap = signer.capabilities.storage

_78

.getControllers(forPath: /storage/RickRollTransactionHandler)[1]

_78

.capability as! Capability<auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}>

_78

}

_78

_78

// borrow a reference to the scheduled transaction manager

_78

let manager = signer.storage.borrow<auth(FlowTransactionSchedulerUtils.Owner) &{FlowTransactionSchedulerUtils.Manager}>(from: FlowTransactionSchedulerUtils.managerStoragePath)

_78

?? panic("Could not borrow a Manager reference from \(FlowTransactionSchedulerUtils.managerStoragePath)")

_78

_78

manager.schedule(

_78

handlerCap: handlerCap,

_78

data: transactionData,

_78

timestamp: future,

_78

priority: pr,

_78

executionEffort: executionEffort,

_78

fees: <-fees

_78

)

_78

_78

log("Scheduled transaction at \(future)")

_78

}

_78

}`

### Deployment and Testing[​](#deployment-and-testing "Direct link to Deployment and Testing")

It's now time to deploy and test the new scheduled transaction! First, add the new contracts to the emulator account in `flow.json` (other contracts may be present):

`_10

"deployments": {

_10

"emulator": {

_10

"emulator-account": [

_10

"RickRoll",

_10

"RickRollTransactionHandler"

_10

]

_10

}

_10

}`

Then, deploy the contracts to the emulator:

`_10

flow project deploy --network emulator`

Next, execute the transaction to initialize the new scheduled transaction handler:

`_10

flow transactions send cadence/transactions/InitRickRollHandler.cdc \

_10

--network emulator --signer emulator-account`

Finally, **get ready to quickly switch to the emulator console** and call the transaction to schedule the transaction:

`_10

flow transactions send cadence/transactions/ScheduleRickRoll.cdc \

_10

--network emulator --signer emulator-account \

_10

--args-json '[

_10

{"type":"UFix64","value":"2.0"},

_10

{"type":"UInt8","value":"1"},

_10

{"type":"UInt64","value":"1000"},

_10

{"type":"Optional","value":null}

_10

]'`

In the logs, you'll see content similar to:

`_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "Scheduled transaction at 1755099632.00000000"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.execute_transaction] executing transaction 4"

_26

11:40AM INF LOG: "Never gonna give you up"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.execute_transaction] executing transaction 5"

_26

11:40AM INF LOG: "Never gonna let you down"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.execute_transaction] executing transaction 6"

_26

11:40AM INF LOG: "Never gonna run around and desert you"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"

_26

11:40AM INF LOG: "[system.process_transactions] processing transactions"`

The last case `return`s the function, so it doesn't set a new scheduled transaction.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned about scheduled transactions, a powerful feature that enables smart contracts to execute code at future times without external transactions. You explored how scheduled transactions solve the fundamental limitation of blockchain computers being unable to run unbounded loops or execute time-delayed operations.

Now that you have completed this tutorial, you should be able to:

* Understand the concept of scheduled transactions and how they solve blockchain limitations.
* Explain the key components of the FlowTransactionScheduler system.
* Understand the benefits of the Transaction Scheduler Manager.
* Implement a basic scheduled transaction using the provided scaffold.
* Analyze the structure and flow of scheduled transaction transactions.
* Create custom scheduled transaction contracts and handlers.
* Evaluate the benefits and use cases of scheduled transactions in DeFi applications.

Scheduled transactions open up new possibilities for DeFi applications, enabling recurring jobs, deferred actions, and autonomous workflows that were previously impossible on blockchain. This feature represents a significant step forward in making blockchain more practical for real-world applications that require time-based execution.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction.md)

Last updated on **Oct 27, 2025** by **Brian Doyle**

[Previous

Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)[Next

DeFi Math Utils](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)* [Cadence Programming Language](#cadence-programming-language)* [Getting Started](#getting-started)
      + [Review of the Existing Contract and Transactions](#review-of-the-existing-contract-and-transactions)+ [Transaction Handler](#transaction-handler)+ [Initializing the Transaction Handler](#initializing-the-transaction-handler)+ [Scheduling the Transaction](#scheduling-the-transaction)* [Using the FlowTransactionSchedulerUtils.Manager](#using-the-flowtransactionschedulerutilsmanager)
        + [Setting Up the Manager](#setting-up-the-manager)+ [Scheduling Transactions with the Manager](#scheduling-transactions-with-the-manager)* [Writing a New Scheduled Transaction](#writing-a-new-scheduled-transaction)
          + [Creating the Contracts](#creating-the-contracts)+ [Setting Up the Transactions](#setting-up-the-transactions)+ [Deployment and Testing](#deployment-and-testing)* [Conclusion](#conclusion)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.