# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/cadence-advantages/upgrading-cadence-contracts

Upgrading Cadence Contracts | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              - [Compose with Cadence Transactions](/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions)- [Native Data Availability With Cadence Scripts](/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts)- [Upgrading Cadence Contracts](/blockchain-development-tutorials/cadence/cadence-advantages/upgrading-cadence-contracts)+ [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)+ [Emulator Fork Testing](/blockchain-development-tutorials/cadence/emulator-fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* Upgrading Cadence Contracts

On this page

# Upgrading Cadence Contracts

In Cadence, to upgrade deployed contracts, you can add new functionality while preserving the current state and maintain the same contract address. Unlike other blockchain platforms that require complex proxy patterns or complete redeployment, Cadence allows you to seamlessly extend your contracts with new functions and events through multiple incremental upgrades.

This tutorial demonstrates how to upgrade a deployed contract through two scenarios:

* Add an event to notify users when the counter reaches an even number.
* Extend the contract with additional functionality, like incrementing by two and checking if numbers are even.

## Objectives[​](#objectives "Direct link to Objectives")

After you complete this guide, you will be able to:

* **Deploy a contract** to Flow testnet using Flow command line interface (CLI).
* **Perform incremental contract upgrades** by adding new events and functions.
* **Update deployed contracts multiple times** using the `flow accounts update-contract` command
* **Test upgraded functionality** with Cadence transactions and scripts.
* **Understand what can and cannot be changed** during contract upgrades.
* **Apply realistic upgrade scenarios** based on user feedback and requirements.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Flow CLI installed](/build/tools/flow-cli/install) and configured.
* Basic familiarity with [Cadence](https://cadence-lang.org/docs/tutorial/first-steps) and [Flow accounts](/build/cadence/basics/accounts).
* A **funded testnet account** to deploy and update contracts.
  + See [Create accounts](/build/tools/flow-cli/commands#create-accounts) and [Fund accounts](/build/tools/flow-cli/commands#fund-accounts) in the Flow CLI commands.

## Contract upgrade overview[​](#contract-upgrade-overview "Direct link to Contract upgrade overview")

Cadence provides a sophisticated contract upgrade system that allows you to modify deployed contracts while ensuring data consistency and preventing runtime crashes. It's crucial for successful upgrades that you understand what you can and can't change.

### What you CAN upgrade[​](#what-you-can-upgrade "Direct link to What you CAN upgrade")

* **Add new functions** - Extend contract functionality with new methods.
* **Add new events** - Emit additional events for monitoring and indexing.
* **Modify function implementations** - Change how existing functions work.
* **Change function signatures** - Update parameters and return types.
* **Remove functions** - Delete functions that are no longer needed.
* **Change access modifiers** - Update visibility of functions and fields.
* **Reorder existing fields** - Field order doesn't affect storage.

### What you CANNOT upgrade[​](#what-you-cannot-upgrade "Direct link to What you CANNOT upgrade")

* **Add new fields** - Would cause runtime crashes when loading existing data.
* **Change field types** - Would cause deserialization errors.
* **Remove existing fields** - Fields become inaccessible, but data remains.
* **Change enum structures** - Raw values must remain consistent.
* **Change contract name** - Contract address must remain the same.

### Why these restrictions exist[​](#why-these-restrictions-exist "Direct link to Why these restrictions exist")

The [Cadence Contract Updatability documentation](https://cadence-lang.org/docs/language/contract-updatability) explains that these restrictions prevent:

* **Runtime crashes** from missing or garbage field values.
* **Data corruption** from type mismatches.
* **Storage inconsistencies** from structural changes.
* **Type confusion** from enum value changes.

The validation system ensures that current stored data remains valid and accessible after upgrades.

## Get started[​](#get-started "Direct link to Get started")

Create a new Flow project for this tutorial:

`_10

# Create a new Flow project

_10

flow init upgrading-contracts-tutorial`

Follow the prompts and create a `Basic Cadence project (no dependencies)` then open the new project in your editor.

### Create and fund testnet account[​](#create-and-fund-testnet-account "Direct link to Create and fund testnet account")

You'll need a funded testnet account to deploy and update contracts. In a terminal in the root of your project folder:

`_10

# Create a testnet account

_10

flow accounts create --network testnet`

When prompted:

1. **Account name**: Enter `testnet-account`
2. Select `testnet` as the network when prompted

Fund your account with testnet FLOW tokens:

`_10

# Fund the account

_10

flow accounts fund testnet-account`

This will open the faucet in your browser where you can request 100,000 testnet FLOW tokens.

info

The faucet provides free testnet tokens for development and testing purposes. These tokens have no real value and are only used on the testnet network.

---

## Deploy the initial counter contract[​](#deploy-the-initial-counter-contract "Direct link to Deploy the initial counter contract")

To start, let's deploy a simple Counter contract to testnet.

Open and review `cadence/contracts/Counter.cdc`. This is a simple contract created with all projects:

`_36

access(all) contract Counter {

_36

_36

access(all) var count: Int

_36

_36

// Event to be emitted when the counter is incremented

_36

access(all) event CounterIncremented(newCount: Int)

_36

_36

// Event to be emitted when the counter is decremented

_36

access(all) event CounterDecremented(newCount: Int)

_36

_36

init() {

_36

self.count = 0

_36

}

_36

_36

// Public function to increment the counter

_36

access(all) fun increment() {

_36

self.count = self.count + 1

_36

emit CounterIncremented(newCount: self.count)

_36

_36

// NEW: Also emit event if the result is even

_36

if self.count % 2 == 0 {

_36

emit CounterIncrementedToEven(newCount: self.count)

_36

}

_36

}

_36

_36

// Public function to decrement the counter

_36

access(all) fun decrement() {

_36

self.count = self.count - 1

_36

emit CounterDecremented(newCount: self.count)

_36

}

_36

_36

// Public function to get the current count

_36

view access(all) fun getCount(): Int {

_36

return self.count

_36

}

_36

}`

### Configure deployment[​](#configure-deployment "Direct link to Configure deployment")

Add testnet deployment configuration to your `flow.json`:

`_10

flow config add deployment`

Follow the prompts:

1. **Network**: `testnet`
2. **Account**: `testnet-account`
3. **Contract**: `Counter`
4. **Deploy more contracts**: `no`

Your `flow.json` will now include a testnet deployment section:

`_10

{

_10

"deployments": {

_10

"testnet": {

_10

"testnet-account": ["Counter"]

_10

}

_10

}

_10

}`

### Deploy to Testnet[​](#deploy-to-testnet "Direct link to Deploy to Testnet")

Deploy your Counter contract to testnet:

`_10

flow project deploy --network testnet`

You will see output similar to:

`_10

Deploying 1 contracts for accounts: testnet-account

_10

_10

Counter -> 0x9942a81bc6c3c5b7 (contract deployed successfully)

_10

_10

🎉 All contracts deployed successfully`

### Test the initial contract[​](#test-the-initial-contract "Direct link to Test the initial contract")

Use the provided transaction to test initial functionality:

Review `cadence/transactions/TestCounter.cdc`. This transaction simply increments the counter:

`_17

import "Counter"

_17

_17

transaction {

_17

_17

prepare(acct: &Account) {

_17

// Authorizes the transaction

_17

}

_17

_17

execute {

_17

// Increment the counter

_17

Counter.increment()

_17

_17

// Retrieve the new count and log it

_17

let newCount = Counter.getCount()

_17

log("New count after incrementing: ".concat(newCount.toString()))

_17

}

_17

}`

info

Cadence transactions are written in Cadence and can call one or more functions on one or more contracts, all with a single user signature. Check out our tutorial to learn how to [Compose with Cadence Transactions](/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions) to learn more!

Run the test transaction:

`_10

flow transactions send cadence/transactions/IncrementCounter.cdc --signer testnet-account --network testnet`

You will see logs that show the counter incrementing and decrementing as expected.

`_25

Transaction ID: 251ee40a050b8c7298d33f1b73ed94996a9d99deae8559526d9dddae182f7752

_25

_25

Block ID 25cdb14fcbaf47b3fb13e6ec43bdef0ede85a6a580caea758220c53d48493e17

_25

Block Height 284173579

_25

Status ✅ SEALED

_25

ID 251ee40a050b8c7298d33f1b73ed94996a9d99deae8559526d9dddae182f7752

_25

Payer adb1efc5826d3768

_25

Authorizers [adb1efc5826d3768]

_25

_25

Proposal Key:

_25

Address adb1efc5826d3768

_25

Index 0

_25

Sequence 1

_25

_25

No Payload Signatures

_25

_25

Envelope Signature 0: adb1efc5826d3768

_25

Signatures (minimized, use --include signatures)

_25

_25

Events:

_25

Index 0

_25

Type A.adb1efc5826d3768.Counter.CounterIncremented

_25

Tx ID 251ee40a050b8c7298d33f1b73ed94996a9d99deae8559526d9dddae182f7752

_25

Values

_25

- newCount (Int): 1`

---

## Upgrade the contract - Part 1: add event for even numbers[​](#upgrade-the-contract---part-1-add-event-for-even-numbers "Direct link to Upgrade the contract - Part 1: add event for even numbers")

Let's start with a realistic scenario: What if we've realized it's very important to our users that they know when the counter reaches an even number, but we forgot to add an event for that case? Let's add that functionality first.

### Modify the Counter contract - first upgrade[​](#modify-the-counter-contract---first-upgrade "Direct link to Modify the Counter contract - first upgrade")

Update `cadence/contracts/Counter.cdc` to add the new event and enhance the current `increment()` function:

`_39

access(all) contract Counter {

_39

_39

access(all) var count: Int

_39

_39

// Event to be emitted when the counter is incremented

_39

access(all) event CounterIncremented(newCount: Int)

_39

_39

// Event to be emitted when the counter is decremented

_39

access(all) event CounterDecremented(newCount: Int)

_39

_39

// NEW: Event to be emitted when the counter is incremented and the result is even

_39

access(all) event CounterIncrementedToEven(newCount: Int)

_39

_39

init() {

_39

self.count = 0

_39

}

_39

_39

// Public function to increment the counter

_39

access(all) fun increment() {

_39

self.count = self.count + 1

_39

emit CounterIncremented(newCount: self.count)

_39

_39

// NEW: Also emit event if the result is even

_39

if self.count % 2 == 0 {

_39

emit CounterIncrementedToEven(newCount: self.count)

_39

}

_39

}

_39

_39

// Public function to decrement the counter

_39

access(all) fun decrement() {

_39

self.count = self.count - 1

_39

emit CounterDecremented(newCount: self.count)

_39

}

_39

_39

// Public function to get the current count

_39

view access(all) fun getCount(): Int {

_39

return self.count

_39

}

_39

}`

### Key changes made - part 1[​](#key-changes-made---part-1 "Direct link to Key changes made - part 1")

This first upgrade adds:

1. **New event**: `CounterIncrementedToEven` to notify when incrementing results in an even number.
2. **Enhanced existing function**: The `increment()` function now also emits the new event when appropriate.
3. **No new fields**: We only use the current `count` field to avoid validation errors.

info

This demonstrates how you can add new behavior and modify current function behavior, which enhances current functionality. The original `CounterIncremented` event still works as before, which ensures backward compatibility.

---

## Update the deployed contract - part 1[​](#update-the-deployed-contract---part-1 "Direct link to Update the deployed contract - part 1")

Now let's update the deployed contract on testnet with the Flow CLI update command with our first upgrade.

### Update the contract[​](#update-the-contract "Direct link to Update the contract")

Use the [Flow CLI update contract command](/build/tools/flow-cli/accounts/account-update-contract) to upgrade your deployed contract:

`_10

flow accounts update-contract ./cadence/contracts/Counter.cdc --signer testnet-account --network testnet`

You will see output similar to:

`_16

Contract 'Counter' updated on account '0x9942a81bc6c3c5b7'

_16

_16

Address 0x9942a81bc6c3c5b7

_16

Balance 99999999999.70000000

_16

Keys 1

_16

_16

Key 0 Public Key [your public key]

_16

Weight 1000

_16

Signature Algorithm ECDSA_P256

_16

Hash Algorithm SHA3_256

_16

Revoked false

_16

Sequence Number 2

_16

Index 0

_16

_16

Contracts Deployed: 1

_16

Contract: 'Counter'`

tip

The contract successfully updated! Notice that:

* The contract address remains the same (`0x9942a81bc6c3c5b7`).
* The current state (`count`) is preserved.
* New functionality is available.

### Test the first upgrade[​](#test-the-first-upgrade "Direct link to Test the first upgrade")

Let's test the new event functionality. Create a simple transaction to test the enhanced `increment()` function:

`_10

flow generate transaction TestEvenEvent`

Replace the contents of `cadence/scripts/CheckCounter.cdc` with:

`_10

import "Counter"

_10

_10

access(all) fun main(): {String: AnyStruct} {

_10

return {

_10

"count": Counter.getCount(),

_10

"isEven": Counter.isEven()

_10

}

_10

}`

Run the script to check the current state:

`_10

flow scripts execute cadence/scripts/CheckCounter.cdc --network testnet`

You will see output that shows the counter state:

`_10

Result: {"count": 1, "isEven": false}`

Notice that:

* The original `count` value is preserved (showing the increment from our earlier test).
* The new `isEven()` function works correctly (1 is odd, so it returns false).

---

## Upgrade the contract - part 2: add more functionality[​](#upgrade-the-contract---part-2-add-more-functionality "Direct link to Upgrade the contract - part 2: add more functionality")

Now that we've successfully added the even number event, let's add more functionality to our contract. This demonstrates how you can make multiple incremental upgrades to extend your contract's capabilities.

### Modify the Counter contract - second upgrade[​](#modify-the-counter-contract---second-upgrade "Direct link to Modify the Counter contract - second upgrade")

Update `cadence/contracts/Counter.cdc` to add the additional functionality:

`_62

access(all) contract Counter {

_62

_62

access(all) var count: Int

_62

_62

// Event to be emitted when the counter is incremented

_62

access(all) event CounterIncremented(newCount: Int)

_62

_62

// Event to be emitted when the counter is decremented

_62

access(all) event CounterDecremented(newCount: Int)

_62

_62

// Event to be emitted when the counter is incremented and the result is even

_62

access(all) event CounterIncrementedToEven(newCount: Int)

_62

_62

// NEW: Event to be emitted when the counter is incremented by 2

_62

access(all) event CounterIncrementedByTwo(newCount: Int)

_62

_62

// NEW: Event to be emitted when the counter is decremented by 2

_62

access(all) event CounterDecrementedByTwo(newCount: Int)

_62

_62

init() {

_62

self.count = 0

_62

}

_62

_62

// Public function to increment the counter

_62

access(all) fun increment() {

_62

self.count = self.count + 1

_62

emit CounterIncremented(newCount: self.count)

_62

_62

// Also emit event if the result is even

_62

if self.count % 2 == 0 {

_62

emit CounterIncrementedToEven(newCount: self.count)

_62

}

_62

}

_62

_62

// Public function to decrement the counter

_62

access(all) fun decrement() {

_62

self.count = self.count - 1

_62

emit CounterDecremented(newCount: self.count)

_62

}

_62

_62

// Public function to get the current count

_62

view access(all) fun getCount(): Int {

_62

return self.count

_62

}

_62

_62

// NEW: Public function to increment the counter by 2

_62

access(all) fun incrementByTwo() {

_62

self.count = self.count + 2

_62

emit CounterIncrementedByTwo(newCount: self.count)

_62

}

_62

_62

// NEW: Public function to decrement the counter by 2

_62

access(all) fun decrementByTwo() {

_62

self.count = self.count - 2

_62

emit CounterDecrementedByTwo(newCount: self.count)

_62

}

_62

_62

// NEW: Public function to check if the current count is even

_62

view access(all) fun isEven(): Bool {

_62

return self.count % 2 == 0

_62

}

_62

}`

### Key changes made - part 2[​](#key-changes-made---part-2 "Direct link to Key changes made - part 2")

This second upgrade adds:

1. **New functions**: `incrementByTwo()` and `decrementByTwo()` that modify the current counter by two.
2. **New events**: `CounterIncrementedByTwo` and `CounterDecrementedByTwo` for the new functionality.
3. **New view function**: `isEven()` to check if the current count is even.
4. **Preserved existing functionality**: All previous functionality remains intact.

---

## Update the deployed contract - part 2[​](#update-the-deployed-contract---part-2 "Direct link to Update the deployed contract - part 2")

Now let's update the deployed contract with our second upgrade.

### Update the contract again[​](#update-the-contract-again "Direct link to Update the contract again")

Use the [Flow CLI update contract command](/build/tools/flow-cli/accounts/account-update-contract) to upgrade your deployed contract with the additional functionality:

`_10

flow accounts update-contract ./cadence/contracts/Counter.cdc --signer testnet-account --network testnet`

You will see output similar to:

`_16

Contract 'Counter' updated on account '0x9942a81bc6c3c5b7'

_16

_16

Address 0x9942a81bc6c3c5b7

_16

Balance 99999999999.70000000

_16

Keys 1

_16

_16

Key 0 Public Key [your public key]

_16

Weight 1000

_16

Signature Algorithm ECDSA_P256

_16

Hash Algorithm SHA3_256

_16

Revoked false

_16

Sequence Number 3

_16

Index 0

_16

_16

Contracts Deployed: 1

_16

Contract: 'Counter'`

tip

The contract successfully updated again! Notice that:

* The contract address remains the same (`0x9942a81bc6c3c5b7`).
* The current state (`count`) is preserved.
* All previous functionality is still available.
* New functionality is now available.

### Verify the update[​](#verify-the-update "Direct link to Verify the update")

Let's verify that the existing functionality still works and the new functionality is available.

Create a script to check the current state:

`_10

flow generate script CheckCounter`

Replace the contents of `cadence/scripts/CheckCounter.cdc` with:

`_10

import "Counter"

_10

_10

access(all) fun main(): {String: AnyStruct} {

_10

return {

_10

"count": Counter.getCount(),

_10

"isEven": Counter.isEven()

_10

}

_10

}`

Run the script to check the current state:

`_10

flow scripts execute cadence/scripts/CheckCounter.cdc --network testnet`

You will see output showing the counter state:

`_10

Result: {"count": 2, "isEven": true}`

Notice that:

* The original `count` value is preserved (showing the increments from our earlier tests).
* The new `isEven()` function works correctly (two is even, so it returns true).

---

## Test the new functionality[​](#test-the-new-functionality "Direct link to Test the new functionality")

Now let's create a transaction to test the new even counter functionality.

### Create test transaction[​](#create-test-transaction "Direct link to Create test transaction")

Create a new transaction to test the upgraded functionality:

`_10

flow generate transaction TestNewCounter`

Replace the contents of `cadence/transactions/TestNewCounter.cdc` with:

`_35

import "Counter"

_35

_35

transaction {

_35

prepare(acct: &Account) {

_35

// Authorizes the transaction

_35

}

_35

_35

execute {

_35

// Test the new functionality

_35

log("Current count: ".concat(Counter.getCount().toString()))

_35

log("Is even: ".concat(Counter.isEven().toString()))

_35

_35

// Test the new incrementByTwo function

_35

Counter.incrementByTwo()

_35

log("After incrementByTwo: ".concat(Counter.getCount().toString()))

_35

log("Is even now: ".concat(Counter.isEven().toString()))

_35

_35

Counter.incrementByTwo()

_35

log("After second incrementByTwo: ".concat(Counter.getCount().toString()))

_35

_35

// Test the new decrementByTwo function

_35

Counter.decrementByTwo()

_35

log("After decrementByTwo: ".concat(Counter.getCount().toString()))

_35

_35

// Verify original functionality still works and test the new event

_35

Counter.increment()

_35

log("After regular increment: ".concat(Counter.getCount().toString()))

_35

log("Is even now: ".concat(Counter.isEven().toString()))

_35

_35

// Increment again to trigger the CounterIncrementedToEven event

_35

Counter.increment()

_35

log("After second increment: ".concat(Counter.getCount().toString()))

_35

log("Is even now: ".concat(Counter.isEven().toString()))

_35

}

_35

}`

### Run the test transaction[​](#run-the-test-transaction "Direct link to Run the test transaction")

Execute the transaction to test the new functionality:

`_10

flow transactions send cadence/transactions/TestNewCounter.cdc --signer testnet-account --network testnet`

You will see logs that show:

* The counter incrementing by two each time with `incrementByTwo()`
* The counter decrementing by two with `decrementByTwo()`
* The `isEven()` function working correctly
* The original `increment()` function still working normally
* The new `CounterIncrementedToEven` event being emitted when incrementing results in an even number

### Verify final state[​](#verify-final-state "Direct link to Verify final state")

Run the check script again to see the final state:

`_10

flow scripts execute cadence/scripts/CheckCounter.cdc --network testnet`

You will see output similar to:

`_10

Result: {"count": 6, "isEven": true}`

This confirms that:

* The new functions work correctly with the existing counter.
* The original state was preserved during the upgrade.
* The new functionality is fully operational.

---

## Understand contract upgrades in Cadence[​](#understand-contract-upgrades-in-cadence "Direct link to Understand contract upgrades in Cadence")

Cadence provides a sophisticated contract upgrade system that ensures data consistency and allows controlled modifications. The [Cadence Contract Updatability documentation](https://cadence-lang.org/docs/language/contract-updatability) provides comprehensive details about the validation rules and restrictions.

### What you can upgrade[​](#what-you-can-upgrade-1 "Direct link to What you can upgrade")

When you upgrade Cadence contracts, you can:

* **Add new state variables** (like `countEven`)
* **Add new functions** (like `incrementEven()` and `decrementEven()`)
* **Add new events** (like `EvenCounterIncremented`)
* **Add new interfaces** and resource types
* **Modify function implementations** (with careful consideration)
* **Remove existing functions** (they are not stored as data)
* **Change function signatures** (parameters, return types)
* **Change access modifiers** of fields and functions
* **Reorder existing fields** (order doesn't affect storage)

### What You cannot change[​](#what-you-cannot-change "Direct link to What You cannot change")

There are important limitations to contract upgrades:

* **Cannot add new fields** to current structs, resources, or contracts.
  + This would cause runtime crashes when you load current data.
  + The initializer only runs once during deployment, not on updates.
* **Cannot change the type** of current state variables.
  + Would cause deserialization errors with stored data.
* **Cannot remove existing state variables** (though they become inaccessible).
* **Cannot change enum structures** (raw values must remain consistent).
* **Cannot change the contract name** or address.

### Validation goals[​](#validation-goals "Direct link to Validation goals")

The contract update validation ensures that:

* **Stored data doesn't change its meaning** when a contract updates.
* **Decoding and using stored data** does not lead to runtime crashes.
* **Type safety is maintained** across all stored values.

warning

The validation system focuses on how to prevent runtime inconsistencies with stored data. It does not ensure that programs which import the updated contract remain valid - you may need to update dependent code if you change function signatures or remove functions.

### Advanced upgrade patterns[​](#advanced-upgrade-patterns "Direct link to Advanced upgrade patterns")

#### The `#removedType` pragma[​](#the-removedtype-pragma "Direct link to the-removedtype-pragma")

For cases where you need to remove a type declaration (which is normally invalid), Cadence provides the `#removedType` pragma. This allows you to "tombstone" a type, which prevents it from being re-added with the same name:

`_10

access(all) contract Foo {

_10

// Remove the resource R permanently

_10

#removedType(R)

_10

_10

// Other contract code...

_10

}`

This pragma:

* **Prevents security issues** from type confusion.
* **Cannot be removed** after you add it (prevents circumventing restrictions).
* **Only works with composite types**, not interfaces.

#### Enum upgrade restrictions[​](#enum-upgrade-restrictions "Direct link to Enum upgrade restrictions")

Enums have special restrictions due to their raw value representation:

* **Can only add enum cases at the end** of current cases.
* **Cannot reorder, rename, or remove** current enum cases.
* **Cannot change the raw type** of an enum.
* **Cannot change enum case names** (would change stored values' meaning).

### Best practices[​](#best-practices "Direct link to Best practices")

When you upgrade contracts:

1. **Plan upgrades carefully** - Consider future extensibility and avoid breaking changes.
2. **Test thoroughly** - Verify both old and new functionality work correctly.
3. **Use events** - Emit events for new functionality to allow monitoring and indexing.
4. **Document changes** - Keep track of what was added, removed, or modified in each upgrade.
5. **Consider dependent code** - Update any programs that import your contract if you change function signatures.
6. **Use the `#removedType` pragma** - When you need to permanently remove types.
7. **Validate enum changes** - Ensure enum modifications follow the strict rules.
8. **Test with existing data** - Verify upgrades work with real stored state, not just empty contracts.

---

## Why this matters[​](#why-this-matters "Direct link to Why this matters")

Cadence's contract upgrade model provides several advantages:

* **No proxy patterns needed** - Unlike Ethereum, you don't need complex proxy contracts.
* **State preservation** - Current data and functionality remain intact.
* **Address stability** - Contract addresses don't change during upgrades.
* **Gas efficiency** - Upgrades are more efficient than redeployment.
* **User experience** - Applications continue working without interruption.

This approach allows you to evolve your contracts over time, You can add new features and capabilities and maintain backward compatibility and preserve user data.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to upgrade deployed Cadence contracts through multiple incremental upgrades by:

* **Deploying an initial contract** to Flow testnet.
* **Performing a first upgrade** to add an event for even numbers based on user feedback.
* **Testing the first upgrade** to verify the new event functionality works correctly.
* **Performing a second upgrade** to add additional functions and events.
* **Testing the complete upgraded functionality** with comprehensive transactions.
* **Verifying state preservation** and backward compatibility across multiple upgrades.

Now that you have completed the tutorial, you should be able to:

* Deploy contracts to Flow testnet with Flow CLI.
* Perform incremental contract upgrades by adding new functions and events.
* Update deployed contracts multiple times and preserve the current state.
* Test upgraded functionality with Cadence transactions and scripts.
* Understand what can and cannot be changed during contract upgrades.
* Apply realistic upgrade scenarios based on user feedback and requirements.
* Plan and execute multiple contract upgrades over time.

This incremental upgrade model makes Cadence contracts more flexible and maintainable than traditional smart contract platforms, which allows you to evolve your applications over time based on real user needs without complex migration patterns or breaking changes. The ability to make multiple upgrades while you maintain state and the same contract address provides a powerful foundation for long-term application development.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/cadence-advantages/upgrading-cadence-contracts.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Native Data Availability With Cadence Scripts](/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts)[Next

Account Linking](/blockchain-development-tutorials/cadence/account-management)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)* [Prerequisites](#prerequisites)* [Contract upgrade overview](#contract-upgrade-overview)
      + [What you CAN upgrade](#what-you-can-upgrade)+ [What you CANNOT upgrade](#what-you-cannot-upgrade)+ [Why these restrictions exist](#why-these-restrictions-exist)* [Get started](#get-started)
        + [Create and fund testnet account](#create-and-fund-testnet-account)* [Deploy the initial counter contract](#deploy-the-initial-counter-contract)
          + [Configure deployment](#configure-deployment)+ [Deploy to Testnet](#deploy-to-testnet)+ [Test the initial contract](#test-the-initial-contract)* [Upgrade the contract - Part 1: add event for even numbers](#upgrade-the-contract---part-1-add-event-for-even-numbers)
            + [Modify the Counter contract - first upgrade](#modify-the-counter-contract---first-upgrade)+ [Key changes made - part 1](#key-changes-made---part-1)* [Update the deployed contract - part 1](#update-the-deployed-contract---part-1)
              + [Update the contract](#update-the-contract)+ [Test the first upgrade](#test-the-first-upgrade)* [Upgrade the contract - part 2: add more functionality](#upgrade-the-contract---part-2-add-more-functionality)
                + [Modify the Counter contract - second upgrade](#modify-the-counter-contract---second-upgrade)+ [Key changes made - part 2](#key-changes-made---part-2)* [Update the deployed contract - part 2](#update-the-deployed-contract---part-2)
                  + [Update the contract again](#update-the-contract-again)+ [Verify the update](#verify-the-update)* [Test the new functionality](#test-the-new-functionality)
                    + [Create test transaction](#create-test-transaction)+ [Run the test transaction](#run-the-test-transaction)+ [Verify final state](#verify-final-state)* [Understand contract upgrades in Cadence](#understand-contract-upgrades-in-cadence)
                      + [What you can upgrade](#what-you-can-upgrade-1)+ [What You cannot change](#what-you-cannot-change)+ [Validation goals](#validation-goals)+ [Advanced upgrade patterns](#advanced-upgrade-patterns)+ [Best practices](#best-practices)* [Why this matters](#why-this-matters)* [Conclusion](#conclusion)

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