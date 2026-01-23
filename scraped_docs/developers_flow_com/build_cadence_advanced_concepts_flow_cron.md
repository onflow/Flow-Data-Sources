# Source: https://developers.flow.com/build/cadence/advanced-concepts/flow-cron

Cron-Based Recurring Transactions | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              - [Cadence Computation Profiling](/build/cadence/advanced-concepts/computation-profiling)- [Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)- [Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions)- [Cron-Based Recurring Transactions](/build/cadence/advanced-concepts/flow-cron)- [Passkeys](/build/cadence/advanced-concepts/passkeys)- [FLIX (Flow Interaction Templates)](/build/cadence/advanced-concepts/flix)- [NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)- [VRF (Randomness) in Cadence](/build/cadence/advanced-concepts/randomness)- [Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)+ [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Advanced Concepts* Cron-Based Recurring Transactions

On this page

# Cron-Based Recurring Transactions

Sometimes you need blockchain logic to run automatically on a schedule: distributing rewards every day, checking conditions every hour, or processing batches every week. Instead of manually triggering these transactions, you can automate them.

**Cron** is a time-based scheduling system originally from Unix. It lets you define "run this at 9am every Monday" using a simple pattern called a cron expression. The **FlowCron** smart contract brings this same concept onchain, so you can schedule recurring transactions that run automatically without any external triggers.

For example, with the cron expression `0 0 * * *` (daily at midnight), your transaction executes every day at midnight UTC—indefinitely—until you stop it.

info

`FlowCron` builds on Flow's Scheduled Transactions. If you haven't worked with scheduled transactions before, check out the [Scheduled Transactions documentation](/build/cadence/advanced-concepts/scheduled-transactions) first.

## How It Works[​](#how-it-works "Direct link to How It Works")

`FlowCron` provides a `CronHandler` resource that wraps your existing [TransactionHandler](/build/cadence/advanced-concepts/scheduled-transactions#create-a-scheduled-transaction). You give it a cron expression (like `*/5 * * * *` for every 5 minutes) and your handler, and `FlowCron` takes care of the rest. Once started, your schedule runs indefinitely without any further action from you.

### Why Two Transactions?[​](#why-two-transactions "Direct link to Why Two Transactions?")

A key challenge with recurring schedules is fault tolerance: what happens if your code has a bug? You don't want one failed execution to break the entire schedule.

`FlowCron` solves this by running two separate transactions each time your cron triggers:

* **Executor**: Runs your code. If your logic fails, only this transaction reverts.
* **Keeper**: Schedules the next cycle. Runs independently, so even if your code throws an error, the schedule continues.

**The benefit**: Your recurring schedule won't break if your `TransactionHandler` execution fails. The keeper always ensures the next execution is scheduled, regardless of whether the current one succeeded or failed.

`_10

Timeline ─────────────────────────────────────────────────────────>

_10

T1 T2 T3

_10

│ │ │

_10

├── Executor ──────────►├── Executor ──────────►├── Executor

_10

│ (runs user code) │ (runs user code) │ (runs user code)

_10

│ │ │

_10

└── Keeper ────────────►└── Keeper ────────────►└── Keeper

_10

(schedules T2) (schedules T3) (schedules T4)

_10

(+1s offset) (+1s offset) (+1s offset)`

## Cron Expressions[​](#cron-expressions "Direct link to Cron Expressions")

A cron expression is just five numbers (or wildcards) that define when something should run.

`FlowCron` uses the standard 5-field cron format:

`_10

┌───────────── minute (0-59)

_10

│ ┌───────────── hour (0-23)

_10

│ │ ┌───────────── day of month (1-31)

_10

│ │ │ ┌───────────── month (1-12)

_10

│ │ │ │ ┌───────────── day of week (0-6, Sunday=0)

_10

│ │ │ │ │

_10

* * * * *`

**Operators:** `*` (any), `,` (list), `-` (range), `/` (step)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pattern When it runs|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `* * * * *` Every minute|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `*/5 * * * *` Every 5 minutes|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `0 * * * *` Top of every hour|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `0 0 * * *` Daily at midnight|  |  |  |  | | --- | --- | --- | --- | | `0 0 * * 0` Weekly on Sunday|  |  | | --- | --- | | `0 9-17 * * 1-5` Hourly, 9am-5pm weekdays | | | | | | | | | | | | | |

note

When you specify both day-of-month and day-of-week (not `*`), the job runs if **either** matches. So `0 0 15 * 0` fires on the 15th OR on Sundays.

## Setup[​](#setup "Direct link to Setup")

Setting up a cron job involves four steps:

1. **Create a handler**: Write the code you want to run on each tick
2. **Wrap it with FlowCron**: Connect your handler to a cron schedule
3. **Start the schedule**: Kick off the first execution
4. **Monitor**: Check that everything is running

All transactions and scripts referenced below are available in the [FlowCron GitHub repository](https://github.com/onflow/flow-cron).

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you start, make sure you have:

* **[Flow CLI](/build/tools/flow-cli)** installed: This is the command-line tool you'll use to deploy contracts, send transactions, and run scripts. If you don't have it yet, follow the [installation guide](/build/tools/flow-cli/install).
* **FLOW tokens** for transaction fees: Every transaction costs a small amount of FLOW. Get free testnet FLOW from the [Faucet](https://faucet.flow.com/).
* A **Flow account**: The CLI will help you create one if you don't have one yet.

### 1. Create Your Handler[​](#1-create-your-handler "Direct link to 1. Create Your Handler")

First, you need to write the code that will run on each scheduled tick. In Cadence, this is called a `TransactionHandler`. A `TransactionHandler` is a resource that implements the `FlowTransactionScheduler.TransactionHandler` interface.

The key part is the `executeTransaction` function. This is where you put whatever logic you want to run on schedule: updating state, distributing tokens, checking conditions, etc.

For more details on how handlers work, see the [Scheduled Transactions documentation](/build/cadence/advanced-concepts/scheduled-transactions#create-a-scheduled-transaction).

Here's a simple example contract:

`_32

import "FlowTransactionScheduler"

_32

_32

access(all) contract MyRecurringTask {

_32

_32

access(all) resource Handler: FlowTransactionScheduler.TransactionHandler {

_32

_32

access(FlowTransactionScheduler.Execute)

_32

fun executeTransaction(id: UInt64, data: AnyStruct?) {

_32

// Your logic here

_32

log("Cron fired at ".concat(getCurrentBlock().timestamp.toString()))

_32

}

_32

_32

access(all) view fun getViews(): [Type] {

_32

return [Type<StoragePath>(), Type<PublicPath>()]

_32

}

_32

_32

access(all) fun resolveView(_ view: Type): AnyStruct? {

_32

switch view {

_32

case Type<StoragePath>():

_32

return /storage/MyRecurringTaskHandler

_32

case Type<PublicPath>():

_32

return /public/MyRecurringTaskHandler

_32

default:

_32

return nil

_32

}

_32

}

_32

}

_32

_32

access(all) fun createHandler(): @Handler {

_32

return <- create Handler()

_32

}

_32

}`

This example handler simply logs the timestamp when executed. Replace the `log` statement with your own logic.

#### Deploy Your Contract[​](#deploy-your-contract "Direct link to Deploy Your Contract")

Use the Flow CLI to deploy your `TransactionHandler` contract:

`_10

flow project deploy --network=testnet`

This command reads your `flow.json` configuration and deploys all configured contracts. If you're new to deploying, see the [deployment guide](/build/cadence/smart-contracts/deploying) for a complete walkthrough.

#### Create and Store a Handler Instance[​](#create-and-store-a-handler-instance "Direct link to Create and Store a Handler Instance")

After deploying, you need to create an instance of your handler and save it to your account's **storage**. The **storage** is an area in your account where you can save resources (like your handler) that persist between transactions.

See [CounterTransactionHandler.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/tests/mocks/contracts/CounterTransactionHandler.cdc) for a complete working example that includes the storage setup.

### 2. Wrap It with `FlowCron`[​](#2-wrap-it-with-flowcron "Direct link to 2-wrap-it-with-flowcron")

Now you need to wrap your handler with a `CronHandler`. This connects your handler to a cron schedule.

The following transaction creates a new `CronHandler` resource that holds your cron expression and a reference to your handler:

`_21

transaction(

_21

cronExpression: String,

_21

wrappedHandlerStoragePath: StoragePath,

_21

cronHandlerStoragePath: StoragePath

_21

) {

_21

prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, SaveValue) &Account) {

_21

// Issue capability for wrapped handler

_21

let wrappedHandlerCap = acct.capabilities.storage.issue<

_21

auth(FlowTransactionScheduler.Execute) &{FlowTransactionScheduler.TransactionHandler}

_21

>(wrappedHandlerStoragePath)

_21

_21

// Create and save the CronHandler

_21

let cronHandler <- FlowCron.createCronHandler(

_21

cronExpression: cronExpression,

_21

wrappedHandlerCap: wrappedHandlerCap,

_21

feeProviderCap: feeProviderCap,

_21

schedulerManagerCap: schedulerManagerCap

_21

)

_21

acct.storage.save(<-cronHandler, to: cronHandlerStoragePath)

_21

}

_21

}`

See [CreateCronHandler.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/transactions/CreateCronHandler.cdc) for the full transaction.

**Send this transaction using the Flow CLI:**

`_10

flow transactions send CreateCronHandler.cdc \

_10

"*/5 * * * *" \

_10

/storage/MyRecurringTaskHandler \

_10

/storage/MyCronHandler \

_10

--network=testnet`

The arguments are: your cron expression, the storage path where your handler lives, and the path where the new `CronHandler` will be stored.

### 3. Start the Schedule[​](#3-start-the-schedule "Direct link to 3. Start the Schedule")

This transaction schedules the first executor and keeper, which kicks off the self-perpetuating loop. After this, your cron job runs automatically:

`_31

transaction(

_31

cronHandlerStoragePath: StoragePath,

_31

wrappedData: AnyStruct?,

_31

executorPriority: UInt8,

_31

executorExecutionEffort: UInt64,

_31

keeperExecutionEffort: UInt64

_31

) {

_31

prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, SaveValue) &Account) {

_31

// Calculate next cron tick time

_31

let cronHandler = signer.storage.borrow<&FlowCron.CronHandler>(from: cronHandlerStoragePath)

_31

?? panic("CronHandler not found")

_31

let executorTime = FlowCronUtils.nextTick(spec: cronHandler.getCronSpec(), afterUnix: currentTime)

_31

}

_31

_31

execute {

_31

// Schedule executor (runs your code)

_31

self.manager.schedule(

_31

handlerCap: self.cronHandlerCap,

_31

data: self.executorContext,

_31

timestamp: UFix64(self.executorTime),

_31

...

_31

)

_31

// Schedule keeper (schedules next cycle)

_31

self.manager.schedule(

_31

handlerCap: self.cronHandlerCap,

_31

data: self.keeperContext,

_31

timestamp: UFix64(self.keeperTime),

_31

...

_31

)

_31

}

_31

}`

See [ScheduleCronHandler.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/transactions/ScheduleCronHandler.cdc) for the full transaction.

**Send this transaction using the Flow CLI:**

`_10

flow transactions send ScheduleCronHandler.cdc \

_10

/storage/MyCronHandler \

_10

nil \

_10

2 \

_10

500 \

_10

2500 \

_10

--network=testnet`

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Parameter Description|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `cronHandlerStoragePath` Path to your CronHandler|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `wrappedData` Optional data passed to handler (`nil` or your data)| `executorPriority` 0 (High), 1 (Medium), or 2 (Low)|  |  |  |  | | --- | --- | --- | --- | | `executorExecutionEffort` Computation units for your code (start with `500`)| `keeperExecutionEffort` Computation units for keeper (use `2500`) | | | | | | | | | | | |

Fees

Starting a cron job requires prepaying fees for the scheduled transactions. FLOW will be deducted from your account to cover the executor and keeper fees. Make sure you have enough FLOW before running this transaction.

Once this transaction succeeds, **your cron job is live**. The first execution will happen at the next cron tick, and the schedule will continue automatically from there. You don't need to do anything else, unless you want to monitor it or stop it.

### 4. Check Status[​](#4-check-status "Direct link to 4. Check Status")

Use Cadence **scripts** to check your cron job's status. Scripts are read-only queries that inspect blockchain state without submitting a transaction—they're free to run and don't modify anything. Learn more in the [scripts documentation](/build/cadence/basics/scripts).

#### Query Cron Info[​](#query-cron-info "Direct link to Query Cron Info")

The [GetCronInfo.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/scripts/GetCronInfo.cdc) script returns metadata about your cron handler:

`_10

access(all) fun main(handlerAddress: Address, handlerStoragePath: StoragePath): FlowCron.CronInfo? {

_10

let account = getAuthAccount<auth(BorrowValue) &Account>(handlerAddress)

_10

if let handler = account.storage.borrow<&FlowCron.CronHandler>(from: handlerStoragePath) {

_10

return handler.resolveView(Type<FlowCron.CronInfo>()) as? FlowCron.CronInfo

_10

}

_10

return nil

_10

}`

**Run this script using the Flow CLI:**

`_10

flow scripts execute GetCronInfo.cdc 0xYourAddress /storage/MyCronHandler --network=testnet`

If your cron job is running, you'll see output showing the cron expression, next scheduled execution time, and handler status.

#### Calculate Next Execution Time[​](#calculate-next-execution-time "Direct link to Calculate Next Execution Time")

The [GetNextExecutionTime.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/scripts/GetNextExecutionTime.cdc) script calculates when your cron expression will next trigger:

`_10

access(all) fun main(cronExpression: String, afterUnix: UInt64?): UFix64? {

_10

let cronSpec = FlowCronUtils.parse(expression: cronExpression)

_10

if cronSpec == nil { return nil }

_10

let nextTime = FlowCronUtils.nextTick(

_10

spec: cronSpec!,

_10

afterUnix: afterUnix ?? UInt64(getCurrentBlock().timestamp)

_10

)

_10

return nextTime != nil ? UFix64(nextTime!) : nil

_10

}`

**Run this script using the Flow CLI:**

`_10

flow scripts execute GetNextExecutionTime.cdc "*/5 * * * *" nil --network=testnet`

#### Additional Debugging Scripts[​](#additional-debugging-scripts "Direct link to Additional Debugging Scripts")

* [GetCronScheduleStatus.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/scripts/GetCronScheduleStatus.cdc) — Returns executor/keeper transaction IDs, timestamps, and current status
* [GetParsedCronExpression.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/scripts/GetParsedCronExpression.cdc) — Validates and parses a cron expression into a `CronSpec`

## Stopping a Cron Job[​](#stopping-a-cron-job "Direct link to Stopping a Cron Job")

You might want to stop a cron job for several reasons:

* **Debugging**: Something isn't working and you need to investigate
* **Updating**: You want to change the schedule or handler logic
* **Cost**: You no longer need the recurring execution
* **Temporary pause**: You want to stop temporarily and restart later

To stop a running cron job, you need to cancel both the pending executor and keeper transactions. This transaction retrieves the scheduled transaction IDs from your `CronHandler` and cancels them:

`_21

transaction(cronHandlerStoragePath: StoragePath) {

_21

prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, SaveValue) &Account) {

_21

let cronHandler = signer.storage.borrow<&FlowCron.CronHandler>(from: cronHandlerStoragePath)

_21

?? panic("CronHandler not found")

_21

_21

self.executorID = cronHandler.getNextScheduledExecutorID()

_21

self.keeperID = cronHandler.getNextScheduledKeeperID()

_21

}

_21

_21

execute {

_21

// Cancel executor and keeper, receive fee refunds

_21

if let id = self.executorID {

_21

let refund <- self.manager.cancel(id: id)

_21

self.feeReceiver.deposit(from: <-refund)

_21

}

_21

if let id = self.keeperID {

_21

let refund <- self.manager.cancel(id: id)

_21

self.feeReceiver.deposit(from: <-refund)

_21

}

_21

}

_21

}`

See [CancelCronSchedule.cdc](https://github.com/onflow/flow-cron/blob/main/cadence/transactions/CancelCronSchedule.cdc) for the full transaction.

**Send this transaction using the Flow CLI:**

`_10

flow transactions send CancelCronSchedule.cdc /storage/MyCronHandler --network=testnet`

Cancelling refunds 50% of the prepaid fees back to your account.

## Contract Addresses[​](#contract-addresses "Direct link to Contract Addresses")

`FlowCron` is deployed on both Testnet and Mainnet:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Testnet Mainnet|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `FlowCron` `0x5cbfdec870ee216d` `0x6dec6e64a13b881e`| `FlowCronUtils` `0x5cbfdec870ee216d` `0x6dec6e64a13b881e` | | | | | | | | |

## Resources[​](#resources "Direct link to Resources")

* [FlowCron GitHub repository](https://github.com/onflow/flow-cron)
* [Scheduled Transactions Documentation](/build/cadence/advanced-concepts/scheduled-transactions)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/advanced-concepts/flow-cron.md)

Last updated on **Jan 20, 2026** by **Michael Fabozzi**

[Previous

Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions)[Next

Passkeys](/build/cadence/advanced-concepts/passkeys)

###### Rate this page

😞😐😊

Copy as Markdown

* [How It Works](#how-it-works)
  + [Why Two Transactions?](#why-two-transactions)* [Cron Expressions](#cron-expressions)* [Setup](#setup)
      + [Prerequisites](#prerequisites)+ [1. Create Your Handler](#1-create-your-handler)+ [2. Wrap It with `FlowCron`](#2-wrap-it-with-flowcron)+ [3. Start the Schedule](#3-start-the-schedule)+ [4. Check Status](#4-check-status)* [Stopping a Cron Job](#stopping-a-cron-job)* [Contract Addresses](#contract-addresses)* [Resources](#resources)

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