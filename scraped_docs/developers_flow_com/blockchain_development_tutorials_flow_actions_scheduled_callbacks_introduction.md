# Source: https://developers.flow.com/blockchain-development-tutorials/flow-actions/scheduled-callbacks-introduction

Introduction to Scheduled Callbacks | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Flow Actions](/blockchain-development-tutorials/flow-actions)

  + [Introduction to Flow Actions](/blockchain-development-tutorials/flow-actions/intro-to-flow-actions)
  + [Flow Actions Transaction](/blockchain-development-tutorials/flow-actions/flow-actions-transaction)
  + [Connectors](/blockchain-development-tutorials/flow-actions/connectors)
  + [Basic Combinations](/blockchain-development-tutorials/flow-actions/basic-combinations)
  + [Introduction to Scheduled Callbacks](/blockchain-development-tutorials/flow-actions/scheduled-callbacks-introduction)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Flow Actions](/blockchain-development-tutorials/flow-actions)
* Introduction to Scheduled Callbacks

On this page

# Introduction to Scheduled Callbacks

warning

Scheduled callbacks are a new feature that is under development and is a part of [FLIP 330](https://github.com/onflow/flips/pull/331/files). Currently, they only work in the emulator. The specific implementation may change as a part of the development process.

These tutorials will be updated, but you may need to refactor your code if the implementation changes.

Flow, EVM, and other blockchains are a form of a **single** shared computer that anyone can use and no one has admin privileges, super user roles, or complete control. For this to work, one of the requirements is that it needs to be impossible for any user to freeze the computer, on purpose or by accident.

As a result, most blockchain computers, including EVM and Solana, are not [Turing Complete](https://en.wikipedia.org/wiki/Turing_completeness), because they can't run an unbounded loop. Each transaction must take place within one block, and cannot consume more gas than the limit.

While this limitation prevents infinite loops, it makes it so that you can't do anything 100% onchain if you need it to happen at a later time or after a trigger. As a result, developers must often build products that involve a fair amount of traditional infrastructure and requires users to give those developers a great amount of trust that their backend will execute the promised task.

Flow fixes this problem with **scheduled callbacks**. Scheduled Callbacks let smart contracts execute code at (or after) a chosen time without an external transaction. You schedule work now; the network executes it later. This enables recurring jobs, deferred actions, and autonomous workflows.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After completing this tutorial, you will be able to:

* Understand the concept of scheduled callbacks and how they solve blockchain limitations
* Explain the key components of the FlowCallbackScheduler system
* Implement a basic scheduled callback using the provided scaffold
* Analyze the structure and flow of scheduled callback transactions
* Create custom scheduled callback contracts and handlers
* Evaluate the benefits and use cases of scheduled callbacks in DeFi applications

# Prerequisites

## Cadence Programming Language[​](#cadence-programming-language "Direct link to Cadence Programming Language")

This tutorial assumes you have a modest knowledge of [Cadence](https://cadence-lang.org/docs). If you don't, you'll be able to follow along, but you'll get more out of it if you complete our series of [Cadence](https://cadence-lang.org/docs) tutorials. Most developers find it more pleasant than other blockchain languages and it's not hard to pick up.

## Getting Started[​](#getting-started "Direct link to Getting Started")

Begin by creating a new repo using the [Scheduled Callbacks Scaffold](https://github.com/onflow/scheduledcallbacks-scaffold) as a template.

This repository has a robust quickstart in the readme. Complete that first. It doesn't seem like much at first. The counter was at `0`, you ran a transaction, now it's at `1`. What's the big deal?

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

callbackData: AnyStruct?

_10

)`

The first parameter is the delay in seconds for the callback. Let's try running it again. You'll need to be quick on the keyboard, so feel free to use a higher number of `delaySeconds` if you need to. You're going to:

1. Call the script to view the counter
2. Call the transaction to schedule the counter to increment after 10 seconds
3. Call the script to view the counter again and verify that it hasn't changed yet
4. Wait 10 seconds, call it again, and confirm the counter incremented

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

briandoyle@Mac scheduled-callbacks-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 2

_37

_37

briandoyle@Mac scheduled-callbacks-scaffold % flow transactions send cadence/transactions/ScheduleIncrementIn.cdc \

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

briandoyle@Mac scheduled-callbacks-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 2

_37

_37

_37

briandoyle@Mac scheduled-callbacks-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 2

_37

_37

_37

briandoyle@Mac scheduled-callbacks-scaffold % flow scripts execute cadence/scripts/GetCounter.cdc --network emulator

_37

_37

Result: 3`

### Review of the Existing Contract and Transactions[​](#review-of-the-existing-contract-and-transactions "Direct link to Review of the Existing Contract and Transactions")

If you're not familiar with it, review `cadence/contracts/Counter.cdc`. This is the standard contract created by default when you run `flow init`. It's very simple, with a counter and public functions to increment or decrement it.

### Callback Handler[​](#callback-handler "Direct link to Callback Handler")

Next, open `cadence/contracts/CounterCallbackHandler.cdc`

`_19

import "FlowCallbackScheduler"

_19

import "Counter"

_19

_19

access(all) contract CounterCallbackHandler {

_19

_19

/// Handler resource that implements the Scheduled Callback interface

_19

access(all) resource Handler: FlowCallbackScheduler.CallbackHandler {

_19

access(FlowCallbackScheduler.Execute) fun executeCallback(id: UInt64, data: AnyStruct?) {

_19

Counter.increment()

_19

let newCount = Counter.getCount()

_19

log("Callback executed (id: ".concat(id.toString()).concat(") newCount: ").concat(newCount.toString()))

_19

}

_19

}

_19

_19

/// Factory for the handler resource

_19

access(all) fun createHandler(): @Handler {

_19

return <- create Handler()

_19

}

_19

}`

This contract is simple. It contains a [resource](https://cadence-lang.org/docs/language/resources) that has a function with the `FlowCallbackScheduler.Execute` [entitlement](https://cadence-lang.org/docs/language/access-control#entitlements). This function contains the code that will be called by the callback. It:

1. Calls the `increment` function in the `Counter` contract
2. Fetches the current value in the counter
3. Logs that value to the console **for the emulator**

It also contains a function, `createHandler`, which creates and returns an instance of the `Handler` resource.

### Initializing the Callback Handler[​](#initializing-the-callback-handler "Direct link to Initializing the Callback Handler")

Next, take a look at `cadence/transactions/InitCounterCallbackHandler.cdc`:

`_16

import "CounterCallbackHandler"

_16

import "FlowCallbackScheduler"

_16

_16

transaction() {

_16

prepare(signer: auth(Storage, Capabilities) &Account) {

_16

// Save a handler resource to storage if not already present

_16

if signer.storage.borrow<&AnyResource>(from: /storage/CounterCallbackHandler) == nil {

_16

let handler <- CounterCallbackHandler.createHandler()

_16

signer.storage.save(<-handler, to: /storage/CounterCallbackHandler)

_16

}

_16

_16

// Validation/example that we can create an issue a handler capability with correct entitlement for FlowCallbackScheduler

_16

let _ = signer.capabilities.storage

_16

.issue<auth(FlowCallbackScheduler.Execute) &{FlowCallbackScheduler.CallbackHandler}>(/storage/CounterCallbackHandler)

_16

}

_16

}`

This transaction saves an instance of the `Handler` resource to the user's [storage](https://cadence-lang.org/docs/language/accounts/storage). It also tests out/demonstrates how to issue the handler [capability] with the `FlowCallbackScheduler.Execute` [entitlement](https://cadence-lang.org/docs/language/access-control#entitlements). The use of the name `_` is convention to name a variable we don't intend to use for anything.

### Scheduling the Callback[​](#scheduling-the-callback "Direct link to Scheduling the Callback")

Finally, open `cadence/transactions/ScheduleIncrementIn.cdc` again. This is the most complicated transaction, so we'll break it down. The final call other than the `log` is what actually schedules the callback:

`_10

let receipt = FlowCallbackScheduler.schedule(

_10

callback: handlerCap,

_10

data: callbackData,

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

It calls the `schedule` function from the `FlowCallbackScheduler` contract. This function has parameters for:

* `callback`: The handler [capability] for the code that should be executed.

This is created above as a part of the transaction with:

`_10

let handlerCap = signer.capabilities.storage

_10

.issue<auth(FlowCallbackScheduler.Execute) &{FlowCallbackScheduler.CallbackHandler}>(/storage/CounterCallbackHandler)`

That line is creating a capability that allows something with the `FlowCallbackScheduler.Execute` entitlement to call the function (`executeCallback()`) from the `Handler` resource in `CounterCallbackHandler.cdc` that you created and stored an instance of in the `InitCounterCallbackHandler` transaction.

* `data`: The arguments required by the callback function.

In this example, `callBackData` is passed in as a prop on the transaction and is `null`.

* `timestamp`: The timestamp for the time in the `future` that this callback should be run.

The transaction call has an argument for `delaySeconds`, which is then converted to a `future` timestamp:

`_10

let future = getCurrentBlock().timestamp + delaySeconds`

* `priority`: The priority this transaction will be given in the event of network congestion. A higher priority means a higher fee for higher precedence.

The `priority` argument is supplied in the transaction as a `UInt8` for convenience, then converted into the appropriate [enum](https://cadence-lang.org/docs/language/enumerations) type:

`_10

let pr = priority == 0

_10

? FlowCallbackScheduler.Priority.High

_10

: priority == 1

_10

? FlowCallbackScheduler.Priority.Medium

_10

: FlowCallbackScheduler.Priority.Low`

The `executionEffort` is also supplied as an argument in the transaction. It's used to prepare the estimate for the gas fees that must be paid for the callback, and directly in the call to `schedule()` the callback.

* `fees`: A [vault](https://developers.flow.com/build/cadence/guides/fungible-token#vaults-on-flow) containing the appropriate amount of gas fees needed to pay for the execution of the scheduled callback.

To create the vault, the `estimate()` function is first used to calculate the amount needed:

`_10

let est = FlowCallbackScheduler.estimate(

_10

data: callbackData,

_10

timestamp: future,

_10

priority: pr,

_10

executionEffort: executionEffort

_10

)`

Then, an [authorized reference](https://cadence-lang.org/docs/language/references#authorized-references) to the signer's vault is created and used to `withdraw()` the needed funds and [move](https://cadence-lang.org/docs/language/operators/assign-move-force-swap#move-operator--) them into the `fees` variable which is then sent in the `schedule()` function call.

Finally, we also `assert` that some minimums are met to ensure the callback will be called:

`_10

assert(

_10

est.timestamp != nil || pr == FlowCallbackScheduler.Priority.Low,

_10

message: est.error ?? "estimation failed"

_10

)`

## Writing a New Scheduled Callback[​](#writing-a-new-scheduled-callback "Direct link to Writing a New Scheduled Callback")

With this knowledge, we can create our own scheduled callback. For this demo, we'll simply display a hello from an old friend in the emulator's console logs.

### Creating the Contracts[​](#creating-the-contracts "Direct link to Creating the Contracts")

Start by using the [Flow CLI](https://developers.flow.com/tools/flow-cli) to create a new contract called `RickRoll.cdc` and one called `RickRollCallbackHandler.cdc`:

`_10

flow generate contract RickRoll

_10

flow generate contract RickRollCallbackHandler`

Open the `RickRoll` contract, and add functions to log a fun message to the emulator console, and a variable to track which message to call:

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

Next, open `RickRollCallbackHandler.cdc`. Start by importing the `RickRoll` contract, `FlowToken`, `FungibleToken`, and `FlowCallbackScheduler`, and stubbing out the `Handler` and factory:

`_17

import "FlowCallbackScheduler"

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

contract RickRollCallbackHandler {

_17

/// Handler resource that implements the Scheduled Callback interface

_17

access(all) resource Handler: FlowCallbackScheduler.CallbackHandler {

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

Next, add a switch to call the appropriate function based on what the current `messageNumber` is:

`_14

access(FlowCallbackScheduler.Execute) fun executeCallback(id: UInt64, data: AnyStruct?) {

_14

switch (RickRoll.messageNumber) {

_14

case 0:

_14

RickRoll.message1()

_14

case 1:

_14

RickRoll.message2()

_14

case 2:

_14

RickRoll.message3()

_14

case 3:

_14

return

_14

default:

_14

panic("Invalid message number")

_14

}

_14

}`

We could move forward with this, but it would be more fun to have each callback schedule the follow callback to share the next message. You can do this by moving most of the code found in the callback transaction to the handler. Start with configuring the `delay`, `future`, `priority`, and `executionEffort`. We'll hardcode these for simplicity:

`_10

var delay: UFix64 = 5.0

_10

let future = getCurrentBlock().timestamp + delay

_10

let priority = FlowCallbackScheduler.Priority.Medium

_10

let executionEffort: UInt64 = 1000`

Next, create the `estimate` and `assert` to validate minimums are met, and that the `Handler` exists:

`_17

let estimate = FlowCallbackScheduler.estimate(

_17

data: data,

_17

timestamp: future,

_17

priority: priority,

_17

executionEffort: executionEffort

_17

)

_17

_17

assert(

_17

estimate.timestamp != nil || priority == FlowCallbackScheduler.Priority.Low,

_17

message: estimate.error ?? "estimation failed"

_17

)

_17

_17

// Ensure a handler resource exists in the contract account storage

_17

if RickRollCallbackHandler.account.storage.borrow<&AnyResource>(from: /storage/RickRollCallbackHandler) == nil {

_17

let handler <- RickRollCallbackHandler.createHandler()

_17

RickRollCallbackHandler.account.storage.save(<-handler, to: /storage/RickRollCallbackHandler)

_17

}`

Then withdraw the necessary funds:

`_10

let vaultRef = CounterLoopCallbackHandler.account.storage

_10

.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)

_10

?? panic("missing FlowToken vault on contract account")

_10

let fees <- vaultRef.withdraw(amount: estimate.flowFee ?? 0.0) as! @FlowToken.Vault`

Finally, issue a capability, and schedule the callback:

`_12

// Issue a capability to the handler stored in this contract account

_12

let handlerCap = RickRollCallbackHandler.account.capabilities.storage

_12

.issue<auth(FlowCallbackScheduler.Execute) &{FlowCallbackScheduler.CallbackHandler}>(/storage/RickRollCallbackHandler)

_12

_12

let receipt = FlowCallbackScheduler.schedule(

_12

callback: handlerCap,

_12

data: data,

_12

timestamp: future,

_12

priority: priority,

_12

executionEffort: executionEffort,

_12

fees: <-fees

_12

)`

### Setting Up the Transactions[​](#setting-up-the-transactions "Direct link to Setting Up the Transactions")

Next, you need to add transactions to initialize the new callback, and another to fire off the sequence.

Start by adding `InitRickRollHandler.cdc`:

`_10

flow generate transaction InitRickRollHandler`

The contract itself is nearly identical to the one we reviewed:

`_16

import "RickRollCallbackHandler"

_16

import "FlowCallbackScheduler"

_16

_16

transaction() {

_16

prepare(signer: auth(Storage, Capabilities) &Account) {

_16

// Save a handler resource to storage if not already present

_16

if signer.storage.borrow<&AnyResource>(from: /storage/RickRollCallbackHandler) == nil {

_16

let handler <- RickRollCallbackHandler.createHandler()

_16

signer.storage.save(<-handler, to: /storage/RickRollCallbackHandler)

_16

}

_16

_16

// Validation/example that we can create an issue a handler capability with correct entitlement for FlowCallbackScheduler

_16

let _ = signer.capabilities.storage

_16

.issue<auth(FlowCallbackScheduler.Execute) &{FlowCallbackScheduler.CallbackHandler}>(/storage/CounterCallbackHandler)

_16

}

_16

}`

Next, add `ScheduleRickRoll`:

`_10

flow generate transaction ScheduleRickRoll`

This transaction is essentially identical as well, it just uses the `handlerCap` stored in `RickRollCallback`:

`_52

import "FlowCallbackScheduler"

_52

import "FlowToken"

_52

import "FungibleToken"

_52

_52

/// Schedule an increment of the Counter with a relative delay in seconds

_52

transaction(

_52

delaySeconds: UFix64,

_52

priority: UInt8,

_52

executionEffort: UInt64,

_52

callbackData: AnyStruct?

_52

) {

_52

prepare(signer: auth(Storage, Capabilities) &Account) {

_52

let future = getCurrentBlock().timestamp + delaySeconds

_52

_52

let pr = priority == 0

_52

? FlowCallbackScheduler.Priority.High

_52

: priority == 1

_52

? FlowCallbackScheduler.Priority.Medium

_52

: FlowCallbackScheduler.Priority.Low

_52

_52

let est = FlowCallbackScheduler.estimate(

_52

data: callbackData,

_52

timestamp: future,

_52

priority: pr,

_52

executionEffort: executionEffort

_52

)

_52

_52

assert(

_52

est.timestamp != nil || pr == FlowCallbackScheduler.Priority.Low,

_52

message: est.error ?? "estimation failed"

_52

)

_52

_52

let vaultRef = signer.storage

_52

.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)

_52

?? panic("missing FlowToken vault")

_52

let fees <- vaultRef.withdraw(amount: est.flowFee ?? 0.0) as! @FlowToken.Vault

_52

_52

let handlerCap = signer.capabilities.storage

_52

.issue<auth(FlowCallbackScheduler.Execute) &{FlowCallbackScheduler.CallbackHandler}>(/storage/RickRollCallbackHandler)

_52

_52

let receipt = FlowCallbackScheduler.schedule(

_52

callback: handlerCap,

_52

data: callbackData,

_52

timestamp: future,

_52

priority: pr,

_52

executionEffort: executionEffort,

_52

fees: <-fees

_52

)

_52

_52

log("Scheduled callback id: ".concat(receipt.id.toString()).concat(" at ").concat(receipt.timestamp.toString()))

_52

}

_52

}`

### Deployment and Testing[​](#deployment-and-testing "Direct link to Deployment and Testing")

It's now time to deploy and test the new scheduled callback!: First, add the new contracts to the emulator account in `flow.json` (other contracts may be present):

`_10

"deployments": {

_10

"emulator": {

_10

"emulator-account": [

_10

"RickRoll",

_10

"RickRollCallbackHandler"

_10

]

_10

}

_10

}`

Then, deploy the contracts to the emulator:

`_10

flow project deploy --network emulator`

And execute the transaction to initialize the new scheduled callback:

`_10

flow transactions send cadence/transactions/InitRickRollHandler.cdc \

_10

--network emulator --signer emulator-account`

Finally, **get ready to quickly switch to the emulator console** and call the transaction to schedule the callback!:

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

In the logs, you'll see similar to:

`_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "Scheduled callback id: 4 at 1755099632.00000000"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.execute_callback] executing callback 4"

_26

11:40AM INF LOG: "Never gonna give you up"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.execute_callback] executing callback 5"

_26

11:40AM INF LOG: "Never gonna let you down"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.execute_callback] executing callback 6"

_26

11:40AM INF LOG: "Never gonna run around and desert you"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"

_26

11:40AM INF LOG: "[system.process_callbacks] processing callbacks"`

The last case `return`s the function, so it doesn't set a new scheduled callback.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned about scheduled callbacks, a powerful feature that enables smart contracts to execute code at future times without external transactions. You explored how scheduled callbacks solve the fundamental limitation of blockchain computers being unable to run unbounded loops or execute time-delayed operations.

Now that you have completed this tutorial, you should be able to:

* Understand the concept of scheduled callbacks and how they solve blockchain limitations
* Explain the key components of the FlowCallbackScheduler system
* Implement a basic scheduled callback using the provided scaffold
* Analyze the structure and flow of scheduled callback transactions
* Create custom scheduled callback contracts and handlers
* Evaluate the benefits and use cases of scheduled callbacks in DeFi applications

Scheduled callbacks open up new possibilities for DeFi applications, enabling recurring jobs, deferred actions, and autonomous workflows that were previously impossible on blockchain. This feature represents a significant step forward in making blockchain more practical for real-world applications that require time-based execution.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/flow-actions/scheduled-callbacks-introduction.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Basic Combinations](/blockchain-development-tutorials/flow-actions/basic-combinations)[Next

Token Development and Registration](/blockchain-development-tutorials/tokens)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)
* [Cadence Programming Language](#cadence-programming-language)
* [Getting Started](#getting-started)
  + [Review of the Existing Contract and Transactions](#review-of-the-existing-contract-and-transactions)
  + [Callback Handler](#callback-handler)
  + [Initializing the Callback Handler](#initializing-the-callback-handler)
  + [Scheduling the Callback](#scheduling-the-callback)
* [Writing a New Scheduled Callback](#writing-a-new-scheduled-callback)
  + [Creating the Contracts](#creating-the-contracts)
  + [Setting Up the Transactions](#setting-up-the-transactions)
  + [Deployment and Testing](#deployment-and-testing)
* [Conclusion](#conclusion)

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
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.