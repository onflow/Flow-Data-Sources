# Source: https://developers.flow.com/tools/clients/fcl-js/sdk-guidelines




SDK Reference | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
  + [Flow Client Library (FCL)](/tools/clients/fcl-js)
    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* [Clients](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* SDK Reference
On this page
# SDK Reference

## Overview[​](#overview "Direct link to Overview")

This reference documents methods available in the SDK that can be accessed via FCL, and explains in detail how these methods work.
FCL/SDKs are open source, and you can use them according to the licence.

The library client specifications can be found here:

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api)

## Getting Started[​](#getting-started "Direct link to Getting Started")

### Installing[​](#installing "Direct link to Installing")

NPM:

 `_10npm install --save @onflow/fcl @onflow/types`

Yarn:

 `_10yarn add @onflow/fcl @onflow/types`
### Importing the Library[​](#importing-the-library "Direct link to Importing the Library")

 `_10import * as fcl from "@onflow/fcl"_10import * as types from "@onflow/types"`
## Connect[​](#connect "Direct link to Connect")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/configure-fcl)

By default, the library uses HTTP to communicate with the access nodes and it must be configured with the correct access node API URL. An error will be returned if the host is unreachable.

📖**The HTTP/REST API information** can be found [here](/http-api). The public Flow HTTP/REST access nodes are accessible at:

* Testnet `https://rest-testnet.onflow.org`
* Mainnet `https://rest-mainnet.onflow.org`
* Local Emulator `127.0.0.1:8888`

Example:

 `_10import { config } from "@onflow/fcl"_10_10config({_10 "accessNode.api": "https://rest-testnet.onflow.org"_10})`
## Querying the Flow Network[​](#querying-the-flow-network "Direct link to Querying the Flow Network")

After you have established a connection with an access node, you can query the Flow network to retrieve data about blocks, accounts, events and transactions. We will explore how to retrieve each of these entities in the sections below.

### Get Blocks[​](#get-blocks "Direct link to Get Blocks")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#getblock)

Query the network for block by id, height or get the latest block.

📖 **Block ID** is SHA3-256 hash of the entire block payload. This hash is stored as an ID field on any block response object (ie. response from `GetLatestBlock`).

📖 **Block height** expresses the height of the block on the chain. The latest block height increases by one for every valid block produced.

#### Examples[​](#examples "Direct link to Examples")

This example depicts ways to get the latest block as well as any other block by height or ID:

 `_10import * as fcl from "@onflow/fcl";_10_10// Get latest block_10const latestBlock = await fcl.latestBlock(true); // If true, get the latest sealed block_10_10// Get block by ID (uses builder function)_10await fcl.send([fcl.getBlock(), fcl.atBlockId("23232323232")]).then(fcl.decode);_10_10// Get block at height (uses builder function)_10await fcl.send([fcl.getBlock(), fcl.atBlockHeight(123)]).then(fcl.decode)`

Result output: [BlockObject](/tools/clients/fcl-js/api#blockobject)

### Get Account[​](#get-account "Direct link to Get Account")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#account)

Retrieve any account from Flow network's latest block or from a specified block height.

📖 **Account address** is a unique account identifier. Be mindful about the `0x` prefix, you should use the prefix as a default representation but be careful and safely handle user inputs without the prefix.

An account includes the following data:

* Address: the account address.
* Balance: balance of the account.
* Contracts: list of contracts deployed to the account.
* Keys: list of keys associated with the account.

#### Examples[​](#examples-1 "Direct link to Examples")

Example depicts ways to get an account at the latest block and at a specific block height:

 `_10import * as fcl from "@onflow/fcl";_10_10// Get account from latest block height_10const account = await fcl.account("0x1d007d755706c469");_10_10// Get account at a specific block height_10fcl.send([_10 fcl.getAccount("0x1d007d755706c469"),_10 fcl.atBlockHeight(123)_10]);`

Result output: [AccountObject](/tools/clients/fcl-js/api#accountobject)

### Get Transactions[​](#get-transactions "Direct link to Get Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#gettransaction)

Retrieve transactions from the network by providing a transaction ID. After a transaction has been submitted, you can also get the transaction result to check the status.

📖 **Transaction ID** is a hash of the encoded transaction payload and can be calculated before submitting the transaction to the network.

⚠️ The transaction ID provided must be from the current spork.

📖 **Transaction status** represents the state of a transaction in the blockchain. Status can change until it is finalized.

| Status | Final | Description |
| --- | --- | --- |
| UNKNOWN | ❌ | The transaction has not yet been seen by the network |
| PENDING | ❌ | The transaction has not yet been included in a block |
| FINALIZED | ❌ | The transaction has been included in a block |
| EXECUTED | ❌ | The transaction has been executed but the result has not yet been sealed |
| SEALED | ✅ | The transaction has been executed and the result is sealed in a block |
| EXPIRED | ✅ | The transaction reference block is outdated before being executed |

 `_16import * as fcl from "@onflow/fcl";_16_16// Snapshot the transaction at a point in time_16fcl.tx(transactionId).snapshot();_16_16// Subscribe to a transaction's updates_16fcl.tx(transactionId).subscribe(callback);_16_16// Provides the transaction once the status is finalized_16fcl.tx(transactionId).onceFinalized();_16_16// Provides the transaction once the status is executed_16fcl.tx(transactionId).onceExecuted();_16_16// Provides the transaction once the status is sealed_16fcl.tx(transactionId).onceSealed();`

Result output: [TransactionStatusObject](/tools/clients/fcl-js/api#gettransactionstatus)

### Get Events[​](#get-events "Direct link to Get Events")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#geteventsatblockheightrange)

Retrieve events by a given type in a specified block height range or through a list of block IDs.

📖 **Event type** is a string that follow a standard format:

 `_10A.{contract address}.{contract name}.{event name}`

Please read more about [events in the documentation](https://cadence-lang.org/docs/language/core-events). The exception to this standard are
core events, and you should read more about them in [this document](https://cadence-lang.org/docs/language/core-events).

📖 **Block height range** expresses the height of the start and end block in the chain.

#### Examples[​](#examples-2 "Direct link to Examples")

Example depicts ways to get events within block range or by block IDs:

 `_22import * as fcl from "@onflow/fcl";_22_22// Get events at block height range_22await fcl_22 .send([_22 fcl.getEventsAtBlockHeightRange(_22 "A.7e60df042a9c0868.FlowToken.TokensWithdrawn", // event name_22 35580624, // block to start looking for events at_22 35580624 // block to stop looking for events at_22 ),_22 ])_22 .then(fcl.decode);_22_22// Get events from list of block ids_22await fcl_22 .send([_22 fcl.getEventsAtBlockIds("A.7e60df042a9c0868.FlowToken.TokensWithdrawn", [_22 "c4f239d49e96d1e5fbcf1f31027a6e582e8c03fcd9954177b7723fdb03d938c7",_22 "5dbaa85922eb194a3dc463c946cc01c866f2ff2b88f3e59e21c0d8d00113273f",_22 ]),_22 ])_22 .then(fcl.decode);`

Result output: [EventObject](/tools/clients/fcl-js/api#event-object)

### Get Collections[​](#get-collections "Direct link to Get Collections")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#getcollection)

Retrieve a batch of transactions that have been included in the same block, known as ***collections***.
Collections are used to improve consensus throughput by increasing the number of transactions per block and they act as a link between a block and a transaction.

📖 **Collection ID** is SHA3-256 hash of the collection payload.

Example retrieving a collection:

 `_10import * as fcl from "@onflow/fcl";_10_10const collection = await fcl_10 .send([_10 fcl.getCollection(_10 "cccdb0c67d015dc7f6444e8f62a3244ed650215ed66b90603006c70c5ef1f6e5"_10 ),_10 ])_10 .then(fcl.decode);`

Result output: [CollectionObject](/tools/clients/fcl-js/api#collectionobject)

### Execute Scripts[​](#execute-scripts "Direct link to Execute Scripts")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#query)

Scripts allow you to write arbitrary non-mutating Cadence code on the Flow blockchain and return data. You can learn more about [Cadence here](https://cadence-lang.org/docs/language) and [scripts here](/tools/clients/fcl-js/scripts), but we are now only interested in executing the script code and getting back the data.

We can execute a script using the latest state of the Flow blockchain or we can choose to execute the script at a specific time in history defined by a block height or block ID.

📖 **Block ID** is SHA3-256 hash of the entire block payload, but you can get that value from the block response properties.

📖 **Block height** expresses the height of the block in the chain.

 `_15import * as fcl from "@onflow/fcl";_15_15const result = await fcl.query({_15 cadence: `_15 access(all) fun main(a: Int, b: Int, addr: Address): Int {_15 log(addr)_15 return a + b_15 }_15 `,_15 args: (arg, t) => [_15 arg(7, t.Int), // a: Int_15 arg(6, t.Int), // b: Int_15 arg("0xba1132bc08f82fe2", t.Address), // addr: Address_15 ],_15});`

Example output:

 `_10console.log(result); // 13`
## Mutate Flow Network[​](#mutate-flow-network "Direct link to Mutate Flow Network")

Flow, like most blockchains, allows anybody to submit a transaction that mutates the shared global chain state. A transaction is an object that holds a payload, which describes the state mutation, and one or more authorizations that permit the transaction to mutate the state owned by specific accounts.

Transaction data is composed and signed with help of the SDK. The signed payload of transaction then gets submitted to the access node API. If a transaction is invalid or the correct number of authorizing signatures are not provided, it gets rejected.

## Transactions[​](#transactions "Direct link to Transactions")

A transaction is nothing more than a signed set of data that includes script code which are instructions on how to mutate the network state and properties that define and limit it's execution. All these properties are explained bellow.

📖 **Script** field is the portion of the transaction that describes the state mutation logic. On Flow, transaction logic is written in [Cadence](https://cadence-lang.org/docs). Here is an example transaction script:

 `_10transaction(greeting: String) {_10 execute {_10 log(greeting.concat(", World!"))_10 }_10}`

📖 **Arguments**. A transaction can accept zero or more arguments that are passed into the Cadence script. The arguments on the transaction must match the number and order declared in the Cadence script. Sample script from above accepts a single `String` argument.

📖 **[Proposal key](/build/basics/transactions#proposal-key)** must be provided to act as a sequence number and prevent replay and other potential attacks.

Each account key maintains a separate transaction sequence counter; the key that lends its sequence number to a transaction is called the proposal key.

A proposal key contains three fields:

* Account address
* Key index
* Sequence number

A transaction is only valid if its declared sequence number matches the current on-chain sequence number for that key. The sequence number increments by one after the transaction is executed.

📖 **[Payer](/build/basics/transactions#signer-roles)** is the account that pays the fees for the transaction. A transaction must specify exactly one payer. The payer is only responsible for paying the network and gas fees; the transaction is not authorized to access resources or code stored in the payer account.

📖 **[Authorizers](/build/basics/transactions#signer-roles)** are accounts that authorize a transaction to read and mutate their resources. A transaction can specify zero or more authorizers, depending on how many accounts the transaction needs to access.

The number of authorizers on the transaction must match the number of `&Account` parameters declared in the prepare statement of the Cadence script.

Example transaction with multiple authorizers:

 `_10transaction {_10 prepare(authorizer1: &Account, authorizer2: &Account) { }_10}`

📖 **Gas limit** is the limit on the amount of computation a transaction requires, and it will abort if it exceeds its gas limit.
Cadence uses metering to measure the number of operations per transaction. You can read more about it in the [Cadence documentation](https://cadence-lang.org/docs).

The gas limit depends on the complexity of the transaction script. Until dedicated gas estimation tooling exists, it's best to use the emulator to test complex transactions and determine a safe limit.

📖 **Reference block** specifies an expiration window (measured in blocks) during which a transaction is considered valid by the network.
A transaction will be rejected if it is submitted past its expiry block. Flow calculates transaction expiry using the *reference block* field on a transaction.
A transaction expires after `600` blocks are committed on top of the reference block, which takes about 10 minutes at average Mainnet block rates.

### Mutate[​](#mutate "Direct link to Mutate")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/tools/clients/fcl-js/api#mutate)

FCL "mutate" does the work of building, signing, and sending a transaction behind the scenes. In order to mutate the blockchain state using FCL, you need to do the following:

 `_16import * as fcl from "@onflow/fcl"_16_16await fcl.mutate({_16 cadence: `_16 transaction(a: Int) {_16 prepare(acct: &Account) {_16 log(acct)_16 log(a)_16 }_16 }_16 `,_16 args: (arg, t) => [_16 arg(6, t.Int)_16 ],_16 limit: 50_16})`

Flow supports great flexibility when it comes to transaction signing, we can define multiple authorizers (multi-sig transactions) and have different payer account than proposer. We will explore advanced signing scenarios bellow.

### [Single party, single signature](/build/basics/transactions#single-party-single-signature)[​](#single-party-single-signature "Direct link to single-party-single-signature")

* Proposer, payer and authorizer are the same account (`0x01`).
* Only the envelope must be signed.
* Proposal key must have full signing weight.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |

 `_56// There are multiple ways to acheive this_56import * as fcl from "@onflow/fcl"_56_56// FCL provides currentUser as an authorization function_56await fcl.mutate({_56 cadence: `_56 transaction {_56 prepare(acct: &Account) {}_56 }_56 `,_56 proposer: currentUser,_56 payer: currentUser,_56 authorizations: [currentUser],_56 limit: 50,_56})_56_56// Or, simplified_56_56mutate({_56 cadence: `_56 transaction {_56 prepare(acct: &Account) {}_56 }_56 `,_56 authz: currentUser, // Optional. Will default to currentUser if not provided._56 limit: 50,_56})_56_56_56// Or, create a custom authorization function_56const authzFn = async (txAccount) => {_56 return {_56 ...txAccount,_56 addr: "0x01",_56 keyId: 0,_56 signingFunction: async(signable) => {_56 return {_56 addr: "0x01",_56 keyId: 0,_56 signature_56 }_56 }_56 }_56}_56_56mutate({_56 cadence: `_56 transaction {_56 prepare(acct: &Account) {}_56 }_56 `,_56 proposer: authzFn,_56 payer: authzFn,_56 authorizations: [authzFn],_56 limit: 50,_56})`
### [Single party, multiple signatures](/build/basics/transactions#single-party-multiple-signatures)[​](#single-party-multiple-signatures "Direct link to single-party-multiple-signatures")

* Proposer, payer and authorizer are the same account (`0x01`).
* Only the envelope must be signed.
* Each key has weight 500, so two signatures are required.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 500 |
| `0x01` | 2 | 500 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#single-party-multiple-signatures)**

 `_42import * as fcl from "@onflow/fcl"_42_42const authzFn = async (txAccount) => {_42 return [_42 {_42 ...txAccount,_42 addr: "0x01",_42 keyId: 0,_42 signingFunction: async(signable) => {_42 return {_42 addr: "0x01",_42 keyId: 0,_42 signature_42 }_42 }_42 },_42 {_42 ...txAccount,_42 addr: "0x01",_42 keyId: 1,_42 signingFunction: async(signable) => {_42 return {_42 addr: "0x01",_42 keyId: 1,_42 signature_42 }_42 }_42 }_42 ]_42}_42_42mutate({_42 cadence: `_42 transaction {_42 prepare(acct: &Account) {}_42 }_42 `,_42 proposer: authzFn,_42 payer: authzFn,_42 authorizations: [authzFn],_42 limit: 50,_42})`
### [Multiple parties](/build/basics/transactions#multiple-parties)[​](#multiple-parties "Direct link to multiple-parties")

* Proposer and authorizer are the same account (`0x01`).
* Payer is a separate account (`0x02`).
* Account `0x01` signs the payload.
* Account `0x02` signs the envelope.
  + Account `0x02` must sign last since it is the payer.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |
| `0x02` | 3 | 1000 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#multiple-parties)**

 `_43import * as fcl from "@onflow/fcl"_43_43const authzFn = async (txAccount) => {_43 return {_43 ...txAccount,_43 addr: "0x01",_43 keyId: 0,_43 signingFunction: async(signable) => {_43 return {_43 addr: "0x01",_43 keyId: 0,_43 signature_43 }_43 }_43 }_43}_43_43const authzTwoFn = async (txAccount) => {_43 return {_43 ...txAccount,_43 addr: "0x02",_43 keyId: 0,_43 signingFunction: async(signable) => {_43 return {_43 addr: "0x02",_43 keyId: 0,_43 signature_43 }_43 }_43 }_43}_43_43mutate({_43 cadence: `_43 transaction {_43 prepare(acct: &Account) {}_43 }_43 `,_43 proposer: authzFn,_43 payer: authzTwoFn,_43 authorizations: [authzFn],_43 limit: 50,_43})`
### [Multiple parties, two authorizers](/build/basics/transactions#multiple-parties)[​](#multiple-parties-two-authorizers "Direct link to multiple-parties-two-authorizers")

* Proposer and authorizer are the same account (`0x01`).
* Payer is a separate account (`0x02`).
* Account `0x01` signs the payload.
* Account `0x02` signs the envelope.
  + Account `0x02` must sign last since it is the payer.
* Account `0x02` is also an authorizer to show how to include two `&Account` objects into an transaction

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |
| `0x02` | 3 | 1000 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#multiple-parties-two-authorizers)**

 `_43import * as fcl from "@onflow/fcl"_43_43const authzFn = async (txAccount) => {_43 return {_43 ...txAccount,_43 addr: "0x01",_43 keyId: 0,_43 signingFunction: async(signable) => {_43 return {_43 addr: "0x01",_43 keyId: 0,_43 signature_43 }_43 }_43 }_43}_43_43const authzTwoFn = async (txAccount) => {_43 return {_43 ...txAccount,_43 addr: "0x02",_43 keyId: 0,_43 signingFunction: async(signable) => {_43 return {_43 addr: "0x02",_43 keyId: 0,_43 signature_43 }_43 }_43 }_43}_43_43mutate({_43 cadence: `_43 transaction {_43 prepare(acct: &Account, acct2: &Account) {}_43 }_43 `,_43 proposer: authzFn,_43 payer: authzTwoFn,_43 authorizations: [authzFn, authzTwoFn],_43 limit: 50,_43})`
### [Multiple parties, multiple signatures](/build/basics/transactions#multiple-parties)[​](#multiple-parties-multiple-signatures "Direct link to multiple-parties-multiple-signatures")

* Proposer and authorizer are the same account (`0x01`).
* Payer is a separate account (`0x02`).
* Account `0x01` signs the payload.
* Account `0x02` signs the envelope.
  + Account `0x02` must sign last since it is the payer.
* Both accounts must sign twice (once with each of their keys).

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 500 |
| `0x01` | 2 | 500 |
| `0x02` | 3 | 500 |
| `0x02` | 4 | 500 |

 `_71import * as fcl from "@onflow/fcl"_71_71const authzFn = async (txAccount) => {_71 return [_71 {_71 ...txAccount,_71 addr: "0x01",_71 keyId: 0,_71 signingFunction: async(signable) => {_71 return {_71 addr: "0x01",_71 keyId: 0,_71 signature_71 }_71 }_71 },_71 {_71 ...txAccount,_71 addr: "0x01",_71 keyId: 1,_71 signingFunction: async(signable) => {_71 return {_71 addr: "0x01",_71 keyId: 1,_71 signature_71 }_71 }_71 }_71 ]_71}_71_71const authzTwoFn = async (txAccount) => {_71 return [_71 {_71 ...txAccount,_71 addr: "0x02",_71 keyId: 0,_71 signingFunction: async(signable) => {_71 return {_71 addr: "0x02",_71 keyId: 0,_71 signature_71 }_71 }_71 },_71 {_71 ...txAccount,_71 addr: "0x02",_71 keyId: 1,_71 signingFunction: async(signable) => {_71 return {_71 addr: "0x02",_71 keyId: 1,_71 signature_71 }_71 }_71 }_71 ]_71}_71_71mutate({_71 cadence: `_71 transaction {_71 prepare(acct: &Account) {}_71 }_71 `,_71 proposer: authzFn,_71 payer: authzTwoFn,_71 authorizations: [authzFn],_71 limit: 50,_71})`

After a transaction has been **built** and **signed**, it can be sent to the Flow blockchain where it will be executed. If sending was successful you can then [retrieve the transaction result](#get-transactions).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/sdk-guidelines.md)Last updated on **Jan 3, 2025** by **Brian Doyle**[PreviousFCL Reference](/tools/clients/fcl-js/api)[NextAuthentication](/tools/clients/fcl-js/authentication)
###### Rate this page

😞😐😊

* [Overview](#overview)
* [Getting Started](#getting-started)
  + [Installing](#installing)
  + [Importing the Library](#importing-the-library)
* [Connect](#connect)
* [Querying the Flow Network](#querying-the-flow-network)
  + [Get Blocks](#get-blocks)
  + [Get Account](#get-account)
  + [Get Transactions](#get-transactions)
  + [Get Events](#get-events)
  + [Get Collections](#get-collections)
  + [Execute Scripts](#execute-scripts)
* [Mutate Flow Network](#mutate-flow-network)
* [Transactions](#transactions)
  + [Mutate](#mutate)
  + [Single party, single signature](#single-party-single-signature)
  + [Single party, multiple signatures](#single-party-multiple-signatures)
  + [Multiple parties](#multiple-parties)
  + [Multiple parties, two authorizers](#multiple-parties-two-authorizers)
  + [Multiple parties, multiple signatures](#multiple-parties-multiple-signatures)
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
* [Flowscan Mainnet](https://flowdscan.io/)
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

