# Source: https://developers.flow.com/build/basics/fees

Fees | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)

  + [Network Architecture ↗️](/build/basics/network-architecture)
  + [Blocks](/build/basics/blocks)
  + [Collections](/build/basics/collections)
  + [Accounts](/build/basics/accounts)
  + [Transactions](/build/basics/transactions)
  + [Scripts](/build/basics/scripts)
  + [Fees](/build/basics/fees)
  + [MEV Resistance](/build/basics/mev-resistance)
  + [Events](/build/basics/events)
  + [FLOW Coin](/build/basics/flow-token)
  + [Smart Contracts ↙](/build/basics/smart-contracts)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Flow Protocol
* Fees

On this page

info

Are you an EVM developer looking for information about EVM Accounts on Flow? If so, check out the EVM specific documentation [here](/evm/fees)

# Fees

## Transaction Fees[​](#transaction-fees "Direct link to Transaction Fees")

A transaction fee is a cost paid in Flow by the payer account and is required for a transaction to be included in the Flow blockchain. Fees are necessary for protecting the network against spam/infinite running transactions and to provide monetary incentives for participants that make up the Flow network.

A transaction fee is paid regardless of whether a transaction succeeds or fails. If the payer account doesn't have sufficient Flow balance to pay for the transaction fee, the transaction will fail. We can limit the transaction fee to some extent by providing the gas limit value when submitting the transaction.

### Understanding the need for transaction fees[​](#understanding-the-need-for-transaction-fees "Direct link to Understanding the need for transaction fees")

Segmented transaction fees are essential to ensure fair pricing based on the impact on the network. For instance, more heavy operations will require more resources to process and propagate transactions. Common operations, however, will stay reasonably priced.

Fees will improve the overall security of the network by making malicious actions (eg spam) on the network less viable.

The unique Flow architecture is targeted at high throughput. It makes it easier to have slack in the system, so short spikes can be handled more gracefully.

### **Fee Structure**[​](#fee-structure "Direct link to fee-structure")

Each transaction fee consists of three components: execution fee, inclusion fee, and network surge factor.

![Screenshot 2023-08-17 at 17.16.32.png](/assets/images/Screenshot_2023-08-17_at_17.16.32-8678c30133be0ae0b2503d108f75c357.png)

**Execution Fee**

The execution effort for a transaction is determined by the code path the transaction takes and the actions it does. The actions that have an associated execution effort cost can be separated into four broad buckets:

* Normal lines of cadence, loops, or function calls
* Reading data from storage, charged per byte read
* Writing data to storage, charged per byte written
* Account creation

| Transaction Type | Estimated cost (FLOW) |
| --- | --- |
| FT transfer | 0.00000185 |
| Mint a small NFT (heavily depends on the NFT size) | 0.0000019 |
| Empty Transaction | 0.000001 |
| Add key to an account | 0.000001 |
| Create 1 Account | 0.00000315 |
| Create 10 accounts | 0.00002261 |
| Deploying a contract that is ~50kb | 0.00002965 |

**Inclusion Fee**

The inclusion effort of a transaction represents the work needed for:

* Including the transaction in a block
* Transporting the transaction information from node to node
* Verifying transaction signatures

Right now, the inclusion effort is always 1.0 and the inclusion effort cost is fixed to `0.000001`.

**Surge Factor**

In the future, a network surge will be applied when the network is busy due to an increased influx of transactions required to be processed or a decrease in the ability to process transactions. Right now, the network surge is fixed to `1.0`.

Currently, both the inclusion fee and surge factor don't represent any significant Flow fees. Keep in mind this can change in the future.

**Estimating transaction costs**

Cost estimation is a two-step process. First, you need to gather the execution effort with either the emulator, on testnet, or on mainnet. Second, you use the execution effort for a transaction to calculate the final fees using one of the JavaScript or Go FCL SDKs.

## Storage[​](#storage "Direct link to Storage")

Flow's approach to storage capacity is a bit similar to some banks' pricing models, where maintaining a minimum balance prevents monthly account fees. Here, the amount of data in your account determines your minimum balance. If you fall below the minimum balance, you cannot transact with your account, except for deposits or deleting data. The essence of storage fee model is that it ensures data availability without continuously charging fees for storage, while also preventing abuses that could burden the network's storage resources. This distinction between current state and blockchain history is crucial for understanding storage requirements and limitations.

Each Flow account has associated storage used. The account's storage used is the byte size of all the data stored in the account's storage. Accounts also have a storage capacity, which is directly tied to the amount of Flow tokens an account has. The account can, without any additional cost, use any amount of storage up to its storage capacity.

warning

If a transaction puts an account over storage capacity, that transaction fails and is reverted. Likewise, if a transaction would drop an account's balance below 0.001 Flow tokens, which is the minimum an account can have, the transaction would also fail.

**Storage Capacity**

The storage capacity of an account is dictated by the amount of FLOW it has.

danger

The **minimum amount of FLOW an account can have is 0.001**. This minimum is provided by the account creator at account creation.

The minimum account reservation ensures that most accounts won't run out of storage capacity if anyone deposits anything (like an NFT) to the account.

Currently, the amount required to store 100 MB in account storage is 1 Flow.

![Screenshot 2023-08-17 at 17.27.50.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAccAAABrCAYAAAACVUmTAAABSGlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGASSSwoyGFhYGDIzSspCnJ3UoiIjFJgf8rAzSDOwMMgysCSmFxc4BgQ4ANUwgCjUcG3awyMIPqyLsis/spH557MYbKQcs3in79R6hWmehTAlZJanAyk/wBxenJBUQkDA2MKkK1cXlIAYncA2SJFQEcB2XNA7HQIewOInQRhHwGrCQlyBrJvANkCyRmJQDMYXwDZOklI4ulIbKi9IMDr4urjoxBqbGFo4RJOwL0kg5LUihIQ7ZxfUFmUmZ5RouAIDKVUBc+8ZD0dBSMDI0MGBlCYQ1R/DgSHJaPYGYRY/iIGBouvDAzMExBiSTMZGLa3MjBI3EKIqSxgYOBvYWDYdr4gsSgR7gDGbyzFacZGEDaPEwMD673//z+rMTCwT2Zg+Dvh///fi/7//7sYaP4dBoYDeQB8EGCs2A3Z9wAAAFZlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA5KGAAcAAAASAAAARKACAAQAAAABAAABx6ADAAQAAAABAAAAawAAAABBU0NJSQAAAFNjcmVlbnNob3RoEnuNAAAB1mlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xMDc8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+NDU1PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6VXNlckNvbW1lbnQ+U2NyZWVuc2hvdDwvZXhpZjpVc2VyQ29tbWVudD4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CpGZiREAABddSURBVHgB7Z0FrBxVF8dvsYe2aNHiwYpLoLhLcAqkQJFgISEBgjvFUixoCBBcA4VSXBKCQ3Ar7i5Fixf99nfp2e/uvNmd2ffu7NvZ9z/JvvEz9/5m3j33nCsz4N+KOIkIiIAIiIAIiECVwBTVNa2IgAiIgAiIgAh4AjKOehFEQAREQAREIEFAxjEBRJsiIAIiIAIiIOOod0AEREAEREAEEgRkHBNAtCkCIiACIiACMo56B0RABERABEQgQUDGMQFEmyIgAiIgAiIwVVkRTHr5ZZ/0ruWWy5UFO5+TJ40f3+2armWWcVm6frzuum7XhTt+f+01N2jEiFx6OLeRTDt0qBs4cmSjUxzpaZWe3uaL/CAxOKMniw3nIOFz/29P7d+sZ157trZEQAT6C4EBRUwCEBqReoV3VuFPoTbxxhvdpDffbPgsBg0f3rCgRM+EUaMa6rCDQ8aNs9XU5Sfbbpu6P7mzkZ5Y6elUPbBsJeeuJZZwg0ePTj7C6jacqUxNHDu2uo8Vrgslb+UhvCZtPU/lgetIFyLj7jHojwhEJ1CI55gsSNJSjdHLqv1nGUb0YnwHpt2gyX0Y2SyhQKyXJisszUOqp4vCjHvVqzTYdWXUYwwsD+HSuPWWs+nMo8fObbS0dDU6J+19Tl5HRW5wgygGxixNT7f7VoxwjMoVfLL+v5KRh7R3Lq+x7pYP7RCBkhOI6jmm1bLrFZhZniNcTV89xs3841pNG12qbdcj2nn7w+eelrs870Lae5is3OR5nyccdVTdypWlLcuokZY8kRD+77I84jx6SBdpIr+N9Fn6tRSBTiEQ1TjaP3/WP3inwFM+RKAvCIQGP639nDRleY2cw/+rSdITtv0YWTvWyKO187UUgU4hUEhYNVaos1MgKx8iEJNA6O2G683eI48nSOjVjGOz+nW+CJSZgIZylPnpKe0iUDCBZPi44NtJvQi0DQEZx7Z5FEqICLQvgXp9B9o3xUqZCPSOgIxj7/jpahEQAREQgQ4kIOPYgQ9VWRKBWASsvTFtmEese0iPCLQjgajGUf9A7fiIlSYREAEREIFmCUQ1jn7cYaXrt4xks49B54tA+xEIh4zwvy0Rgf5EIOo4x/4ETnkVgf5AwKby0xjH/vC0lceQgIxjSEPrIiACIiACIlAhEDWsKqIiIAIiIAIi0AkEZBw74SkqDyIgAiIgAlEJyDhGxSllIiACIiACnUBAxrETnqLyIAIiIAIiEJWAjGNUnFImAiIgAiLQCQSiG0c/i//kr5R3AiDlQQREQAREoP8RiPrJKvueYxcfRm3wVfT+h1k5FgEREAERKBOBqJ6jzYxj8zGWCYTSKgIiUEuAKFD4QeTao9oSgc4mENU4djYq5U4E+g8Bpo6bOHas/9BxOI1c/yGgnPZ3AjKO/f0NUP5FQAREQAS6EZBx7IYk344///zTffTRR/lO1lkiIAIiIAKlIiDj2MPHddttt7k999zTjRkzpocadJkIiIAIiEC7EpBx7OGT+emnn/yV48eP76EGXSYC5SDQpZ7n5XhQSmVUAjKOPcT577//+it/+eWXHmrQZWkEfv/9d/fHH3+kHcq9L4aO3DeLcOI777zjPvnkE0eovl1kkip97fIolI4+IhB1nKPloavyweNOFzOOv/32W6dntWX5e+CBB9w555zjhg0b5o499lgHY35TTJG/DhdDR8syXLnRy5VeoQcffLC/5bTTTuuGDh3q5plnHjfvvPO6BRdc0P/mmGOOViZJ9xIBEagQiGoc+Vo4EwDYeMeyEqZApjZPwfXhhx+6b7/91k2cONH9+uuvbv7553e77rqr++eff3z2pp566rJms63S/dZbb7nRo0f7NL3wwgvukEMOcW+++abDC1ym8l5tueWWboMNNmiY5hg6Gt6g4IPk9fnnn/e/8FYYTRiss846/jf99NOHh7UuAiJQAIHSfuz49ttvd4899pjbd9993WKLLdYrNBg6jCHth/bDGNYTavdLVLzjsZVxYKussoo77bTT6p2q/ZMJECq9/PLL3QcffOBOOeUUN80009SwOf74490TTzxRsy+5gXE45phj3JRTTpk85Ldj6EhVnGMnho2w6EwzzZTj7NpTHn30UffGG2+4r7/+2j300EO1BxNbGMq99trLbbvttm7AgAGJo/E2mQCAcY5EgQZPrrTE0y5NItD+BKJ6jq3K7g033OALWu43YcKEHhlHDOL999/vnnzySYenQuFWT+aaay4399xz+xDfSy+95AtBaxfr6uqqd5n2TyYA6xNOOME988wzfs+kSZNqjCNDYpKGcckll3QLL7yw+/zzz92LL77o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)

Please note that storing data in an account on Flow doesn't charge tokens from the account, it just makes sure you will keep the tokens as a reserve. Once the storage is freed up you can transfer the Flow tokens.

### Storage Capacity of the Payer[​](#storage-capacity-of-the-payer "Direct link to Storage Capacity of the Payer")

The storage capacity of the Payer of a transaction is generally computed the same way as the capacity of any other account, however, the system needs to account for the transaction fees the payer will incur at the end of the transaction. The final transaction fee amount is not fully known at this step, only when accounts are checked for storage compliance. If their storage used is more than their storage capacity, the transaction will fail.

Because of this, the payer's balance is conservatively considered to be lower by the maximum possible transaction fees, when checking for storage compliance. The maximum transaction fee of a specific transaction is the transaction fee as if the transaction would have used up all of its execution effort limit.

### Storage Used[​](#storage-used "Direct link to Storage Used")

All data that is in an account's storage counts towards storage used. Even when an account is newly created it is not empty. There are already some items in its storage:

* Metadata that marks that the account exists.
* An empty FLOW vault, and stored receiver capability.
* Public keys to the account if the account was created with keys.
* Smart contracts deployed on the account if the account was created with contracts.
* The value of the account's storage used as an unsigned integer.

Adding additional keys, smart contracts, capabilities, resources, etc. to the account counts towards storage used.

Data stored on the Flow blockchain is stored in a key-value ledger. Each item's key contains the address that owns the item and the path to the item. An account can have many keys, therefore flow considers the account key items are stored with. This means that the storage used by each item is the byte length of the item plus the byte length of the item's key.

### Maximum available balance[​](#maximum-available-balance "Direct link to Maximum available balance")

Due to the storage restrictions, there is a maximum available balance that user can withdraw from the wallet. The core contract [`FlowStorageFees`](/build/core-contracts/flow-fees#flowstoragefees) provides a function to retrieve that value:

`_10

import "FlowStorageFees"

_10

_10

access(all) fun main(accountAddress: Address): UFix64 {

_10

return FlowStorageFees.defaultTokenAvailableBalance(accountAddress)

_10

}`

Alternatively developers can use `availableBalance` property of the `Account`

`_10

access(all) fun main(address: Address): UFix64 {

_10

let acc = getAccount(address)

_10

let balance = acc.availableBalance

_10

_10

return balance

_10

}`

## Practical Understanding of Fees[​](#practical-understanding-of-fees "Direct link to Practical Understanding of Fees")

**Using Flow Emulator**

You can start the [emulator using the Flow CLI](/tools/emulator#running-the-emulator-with-the-flow-cli). Run your transaction and take a look at the events emitted:

`_10

0|emulator | time="2022-04-06T17:13:22-07:00" level=info msg="⭐ Transaction executed" computationUsed=3 txID=a782c2210c0c1f2a6637b20604d37353346bd5389005e4bff6ec7bcf507fac06`

You should see the `computationUsed` field. Take a note of the value, you will use it in the next step.

**On testnet or mainnet**

Once a transaction is completed, you can use an explorer like [Flowscan](https://flowscan.io/) to review the transaction details and events emitted. For Flowscan, you can open the transaction in question and look for the event `FeesDeducted` from the [`FlowFees`](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowFees.cdc) contract:

![flowscan-fees](/assets/images/flowscan-fees-cb6b2a52450fcbbef7f20f30c4130453.png)

In the event data on the right side, you will see a set of fields representing [the fees for a specific transaction.](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowFees.cdc#L14):

* Total Fees Paid
* Inclusion Effort
* Execution Effort

Take a note of the last value in the list - the `executionEffort` value. You will use it in the next step.

### Calculating final costs[​](#calculating-final-costs "Direct link to Calculating final costs")

The cost for transactions can be calculated using the following FCL scripts on mainnet/testnet respectively.

**On mainnet**

`_10

import FlowFees from 0xf919ee77447b7497

_10

access(all) fun main(

_10

inclusionEffort: UFix64,

_10

executionEffort: UFix64

_10

): UFix64 {

_10

return FlowFees.computeFees(inclusionEffort: inclusionEffort, executionEffort: executionEffort)

_10

}`

**On testnet**

`_10

import FlowFees from 0x912d5440f7e3769e

_10

access(all) fun main(

_10

inclusionEffort: UFix64,

_10

executionEffort: UFix64

_10

): UFix64 {

_10

return FlowFees.computeFees(inclusionEffort: inclusionEffort, executionEffort: executionEffort)

_10

}`

## Configuring execution limits[​](#configuring-execution-limits "Direct link to Configuring execution limits")

FCL SDKs allow you to set the execution effort limit for each transaction. Based on the execution effort limit determined in the previous step, you should set a reasonable maximum to avoid unexpected behavior and protect your users. The final transaction fee is computed from the actual execution effort used up to this maximum.

> **Note**: Keep in mind that the limits are not for the final fees that the user will have to pay. The limits are for the execution efforts specifically.

It is important to set a limit that isn't too high or too low. If it is set too high, the payer needs to have more funds in their account before sending the transaction. If it is too low, the execution could fail and all state changes are dropped.

**Using FCL JS SDK**

You need to set the `limit` parameter for the `mutate` function, for example:

`_17

import * as fcl from "@onflow/fcl"

_17

_17

const transactionId = await fcl.mutate({

_17

cadence: `

_17

transaction {

_17

execute {

_17

log("Hello from execute")

_17

}

_17

}

_17

`,

_17

proposer: fcl.currentUser,

_17

payer: fcl.currentUser,

_17

limit: 100

_17

})

_17

_17

const transaction = await fcl.tx(transactionId).onceExecuted();

_17

console.log(transaction;)`

**Using FCL Go SDK**

You need to call the `SetComputeLimit` method to set the fee limit, for example:

`_16

import (

_16

"github.com/onflow/flow-go-sdk"

_16

"github.com/onflow/flow-go-sdk/crypto"

_16

)

_16

_16

var (

_16

myAddress flow.Address

_16

myAccountKey flow.AccountKey

_16

myPrivateKey crypto.PrivateKey

_16

)

_16

_16

tx := flow.NewTransaction().

_16

SetScript([]byte("transaction { execute { log(\"Hello, World!\") } }")).

_16

SetComputeLimit(100).

_16

SetProposalKey(myAddress, myAccountKey.Index, myAccountKey.SequenceNumber).

_16

SetPayer(myAddress)`

### Maximum transaction fees of a transaction[​](#maximum-transaction-fees-of-a-transaction "Direct link to Maximum transaction fees of a transaction")

The maximum possible fee imposed on the payer for a transaction can be calculated as the **inclusion cost plus the execution cost**. The execution cost is the fee calculated for running the transaction based on the [execution effort limit maximum specified](#configuring-execution-limits).

The payer will never pay more than this amount for the transaction.

## Optimizing Cadence code to reduce effort[​](#optimizing-cadence-code-to-reduce-effort "Direct link to Optimizing Cadence code to reduce effort")

Several optimizations can lead to reduced execution time of transactions. Below is a list of some practices. This list is not exhaustive but rather exemplary.

**Limit functions calls**

Whenever you make function calls, make sure these are absolutely required. In some cases, you might be able to check prerequisites and avoid additional calls:

`_10

for obj in sampleList {

_10

/// check if call is required

_10

if obj.id != nil {

_10

functionCall(obj)

_10

}

_10

}`

**Limit loops and iterations**

Whenever you want to iterate over a list, make sure it is necessary to iterate through all elements as opposed to a subset. Avoid loops to grow in size too much over time. Limit loops when possible.

`_20

// Iterating over long lists can be costly

_20

access(all) fun sum(list: [Int]): Int {

_20

var total = 0

_20

var i = 0

_20

// if list grows too large, this might not be possible anymore

_20

while i < list.length {

_20

total = total + list[i]

_20

}

_20

return total

_20

}

_20

_20

// Consider designing transactions (and scripts) in a way where work can be "chunked" into smaller pieces

_20

access(all) fun partialSum(list: [Int], start: Int, end: Int): Int {

_20

var partialTotal = 0

_20

var i = start

_20

while i < end {

_20

partialTotal = partialTotal + list[i]

_20

}

_20

return partialTotal

_20

}`

**Understand the impact of function calls**

Some functions will require more execution efforts than others. You should carefully review what function calls are made and what execution they involve.

`_15

// be aware functions that call a lot of other functions

_15

// (or call themselves) might cost a lot

_15

access(all) fun fib(_ x: Int): Int {

_15

if x == 1 || x== 0 {

_15

return x

_15

}

_15

// + 2 function calls each recursion

_15

return fib(x-1) + fib(x-2)

_15

}

_15

_15

// consider inlining functions with single statements, to reduce costs

_15

access(all) fun add(_ a: Int, _ b: Int): Int {

_15

// single statement; worth inlining

_15

return a + b

_15

}`

**Avoid excessive load and save operations**

Avoid costly loading and storage operations and [borrow references](https://cadence-lang.org/docs/design-patterns#avoid-excessive-load-and-save-storage-operations-prefer-in-place-mutations) where possible, for example:

`_14

transaction {

_14

_14

prepare(acct: auth(BorrowValue) &Account) {

_14

_14

// Borrows a reference to the stored vault, much less costly operation that removing the vault from storage

_14

let vault <- acct.storage.borrow<&ExampleToken.Vault>(from: /storage/exampleToken)

_14

_14

let burnVault <- vault.withdraw(amount: 10)

_14

_14

destroy burnVault

_14

_14

// No `save` required because we only used a reference

_14

}

_14

}`

> **Note**: If the requested resource does not exist, no reading costs are charged.

**Limit accounts created per transaction**

Creating accounts and adding keys are associated with costs. Try to only create accounts and keys when necessary.

**Check user's balance before executing transactions**

You should ensure that the user's balance has enough balance to cover the highest possible fees. For FT transfers, you need to cover the amount to transfer in addition to the highest possible fees.

## Educating users[​](#educating-users "Direct link to Educating users")

Wallets will handle the presentation of the final transaction costs but you can still facilitate the user experience by educating them within your application.

If your user is using self-custody wallets, they may have to pay the transaction and want to understand the fees. Here are some suggestions.

**Explain that costs can vary depending on the network usage**

Suggested message: "Fees improve the security of the network. They are flexible to ensure fair pricing based on the impact on the network."

**Explain that waiting for the network surge to pass is an option**

Inevitably, network surges will cause higher fees. Users who might want to submit a transaction while the network usage is surging should consider sending the transaction at a later time to reduce costs.

**Explain that the wallet might not allow the transaction due to a lack of funds**

If dynamic fees increase to the highest possible level, the user's fund might not be enough to execute the transaction. Let the users know that they should either add funds or try when the network is less busy.

## How to learn more[​](#how-to-learn-more "Direct link to How to learn more")

There are several places to learn more about transaction fees:

* [FLIP-660](https://github.com/onflow/flow/pull/660)
* [FLIP-753](https://github.com/onflow/flow/pull/753)
* [Flow Fees Contract](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowFees.cdc)

> **Note**: If you have thoughts on the implementation of transaction fees on Flow, you can [leave feedback on this forum post](https://forum.onflow.org/t/variable-transaction-fees-are-coming-to-flow/2941).

## FAQs[​](#faqs "Direct link to FAQs")

**When will the fee update go into effect?**

The updates were rolled out with the [Spork on April 6, 2022](/networks/node-ops/node-operation/past-sporks#mainnet-17), and were enabled on [June 1st](https://forum.onflow.org/t/permissionless-contract-deployment-progress/2981) during the [weekly epoch transition](https://github.com/onflow/service-account/tree/main/transactions/set-execution-effort-weights/2022/jun-1).

**Why are fees collected even when transactions fail?**

Broadcasting and verifying a transaction requires execution, so costs are deducted appropriately.

**What execution costs are considered above average?**

There is no average for execution costs. Every function will vary significantly based on the logic implemented. You should review the optimization best practices to determine if you could reduce your costs.

**Do hardware wallets like Ledger support segmented fees?**

Yes.

**What is the lowest execution cost?**

The lowest execution cost is 1. This means your transaction included one function call or loop that didn't read or write any date.

**Can I determine how much a transaction will cost on mainnet without actually paying?**

You can estimate the costs in a two-way process: 1) determine execution costs for transactions (emulator or testnet) and 2) use an FCL SDK method to calculate the final transaction fees.

**How accurate will testnet fees be to mainnet fees?**

Final fees are determined by the surge factor on the network. The surge factor for the testnet will be different from the factor for the mainnet, so you need to expect a variation between mainnet and testnet estimates.

**I use Blocto and I haven't paid any fees yet. Why is that?**

That is because Blocto is acting as the payer for transactions. Self-custody wallets may have the user pay the transaction. Additionally, apps can sponsor the transaction if they choose.

**Why would the same transaction have different fees when executed for different accounts?**

Execution costs, among other things, include the cost to read data from account storage and since the data stored varies from account to account, so does the execution costs, and subsequently the transaction fees.

Additional Details:

* The most expensive operations in Cadence are reading and writing to storage. This isn't punitive! Every read needs to be sent to all Verification nodes for verification (with Merkel proofs), and every write requires a path of Merkel hashes to be updated. Reading and writing to storage is inherently expensive on any blockchain.
* The way data is stored in accounts is as a tree (the hint is in the name "atree" 😉). So, the more elements in the account, the more levels of the tree, and therefore the more nodes of that tree that need to be read and updated. So, looking at the byte size of an account is a decent proxy for figuring out how much it's going to cost.
* Because it's a tree, the cost of reads and writes grows with log(n), but does scale.
* atree has an update queued up for [Crescendo](https://flow.com/upgrade/crescendo) that will improve this. The previous version erred on the side of adding new levels to the tree (to keep the code simple), while the new version tries to pack more data at each level. This should result in fewer levels for the same byte size. Additionally, it includes a more compact encoding leading to a reduction in the byte size of most accounts.
* Even with these improvements, this relationship is likely to remain indefinitely. The bigger the account, the more bookkeeping the nodes have to do, which will result in somewhat larger tx fees.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/basics/fees.md)

Last updated on **Apr 1, 2025** by **Brian Doyle**

[Previous

Scripts](/build/basics/scripts)[Next

MEV Resistance](/build/basics/mev-resistance)

###### Rate this page

😞😐😊

* [Transaction Fees](#transaction-fees)
  + [Understanding the need for transaction fees](#understanding-the-need-for-transaction-fees)
  + [**Fee Structure**](#fee-structure)
* [Storage](#storage)
  + [Storage Capacity of the Payer](#storage-capacity-of-the-payer)
  + [Storage Used](#storage-used)
  + [Maximum available balance](#maximum-available-balance)
* [Practical Understanding of Fees](#practical-understanding-of-fees)
  + [Calculating final costs](#calculating-final-costs)
* [Configuring execution limits](#configuring-execution-limits)
  + [Maximum transaction fees of a transaction](#maximum-transaction-fees-of-a-transaction)
* [Optimizing Cadence code to reduce effort](#optimizing-cadence-code-to-reduce-effort)
* [Educating users](#educating-users)
* [How to learn more](#how-to-learn-more)
* [FAQs](#faqs)

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