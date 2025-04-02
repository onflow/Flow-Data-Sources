# Source: https://developers.flow.com/tools/clients/fcl-js/transactions

Transactions | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)

    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Cross VM Packages](/tools/clients/fcl-js/cross-vm)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Use Cursor AI](/tools/cursor)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* Transactions

On this page

# Transactions

Transactions let you send Cadence code to the Flow blockchain that permanently alters its state.

We are assuming you have read the [Scripts Documentation](/tools/clients/fcl-js/scripts) before this, as transactions are sort of scripts with more required things.

While `query` is used for sending scripts to the chain, `mutate` is used for building and sending transactions. Just like [scripts](/tools/clients/fcl-js/scripts), `fcl.mutate` is a [JavaScript Tagged Template Literal](https://styled-components.com/docs/advanced#tagged-template-literals) that we can pass Cadence code into.

Unlike scripts, they require a little more information, things like a proposer, authorizations and a payer, which may be a little confusing and overwhelming.

## Sending Your First Transaction[​](#sending-your-first-transaction "Direct link to Sending Your First Transaction")

There is a lot to unpack in the following code snippet.
It sends a transaction to the Flow blockchain. For the transaction, the current user is authorizing it as both the `proposer` and the `payer`.
Something that is unique to Flow is the one paying for the transaction doesn't always need to be the one performing the transaction.
Proposers and Payers are special kinds of authorizations that are always required for a transaction.
The `proposer` acts similar to the `nonce` in Ethereum transactions, and helps prevent repeat attacks.
The `payer` is who will be paying for the transaction.
If these are not set, FCL defaults to using the current user for all roles.

`fcl.mutate` will return a `transactionId`. We can pass the response directly to `fcl.tx` and then use the `onceExecuted` method which resolves a promise when a transaction result is available.

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

limit: 50

_17

})

_17

_17

const transaction = await fcl.tx(transactionId).onceExecuted()

_17

console.log(transaction) // The transactions status and events after being executed`

## Authorizing a Transaction[​](#authorizing-a-transaction "Direct link to Authorizing a Transaction")

The below code snippet is the same as the above one, except for one extremely important difference.
Our Cadence code this time has a prepare statement, and we are using the `fcl.currentUser` when constructing our transaction.

The `prepare` statement's arguments directly map to the order of the authorizations in the `authorizations` array.
Four authorizations means four `&Account`s as arguments passed to `prepare`. In this case though there is only one, and it is the `currentUser`.

These authorizations are important as you can only access/modify an accounts storage if you have the said accounts authorization.

`_21

import * as fcl from "@onflow/fcl"

_21

_21

const transactionId = await fcl.mutate({

_21

cadence: `

_21

transaction {

_21

prepare(acct: &Account) {

_21

log("Hello from prepare")

_21

}

_21

execute {

_21

log("Hello from execute")

_21

}

_21

}

_21

`,

_21

proposer: fcl.currentUser,

_21

payer: fcl.currentUser,

_21

authorizations: [fcl.currentUser],

_21

limit: 50

_21

})

_21

_21

const transaction = await fcl.tx(transactionId).onceExecuted()

_21

console.log(transaction) // The transactions status and events after being executed`

To learn more about `mutate`, check out the [API documentation](/tools/clients/fcl-js/api#mutate).

## Transaction Finality[​](#transaction-finality "Direct link to Transaction Finality")

As of **FCL v1.15.0**, it is now recommended to use use `onceExecuted` in most cases, leading to a 2.5x reduction in latency when waiting for a transaction result. For example, the following code snippet should be updated from:

`_10

import * as fcl from "@onflow/fcl"

_10

const result = await fcl.tx(txId).onceSealed()`

to:

`_10

import * as fcl from "@onflow/fcl"

_10

const result = await fcl.tx(txId).onceExecuted()`

Developers manually subscribing to transaction statuses should update their listeners to treat "executed" as the final status (see the release notes [here](https://github.com/onflow/fcl-js/releases/tag/%40onflow%2Ffcl%401.15.0)). For example, the following code snippet should be updated from:

`_10

import * as fcl from "@onflow/fcl"

_10

import { TransactionExecutionStatus } from "@onflow/typedefs"

_10

_10

fcl.tx(txId).subscribe((txStatus) => {

_10

if (

_10

txStatus.status === TransactionExecutionStatus.SEALED

_10

) {

_10

console.log("Transaction executed!")

_10

}

_10

})`

`_11

import * as fcl from "@onflow/fcl"

_11

import { TransactionExecutionStatus } from "@onflow/typedefs"

_11

_11

fcl.tx(txId).subscribe((txStatus) => {

_11

if (

_11

// SEALED status is no longer necessary

_11

txStatus.status === TransactionExecutionStatus.EXECUTED

_11

) {

_11

console.log("Transaction executed!")

_11

}

_11

})`

The "executed" status corresponds to soft finality, indicating that the transaction has been included in a block and a transaction status is available, backed by a cryptographic proof. Only in rare cases should a developer need to wait for "sealed" status in their applications and you can learn more about the different transaction statuses on Flow [here](/build/basics/transactions#transaction-status).

See the following video for demonstration of how to update your code to wait for "executed" status:

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/transactions.md)

Last updated on **Apr 1, 2025** by **Jordan Ribbink**

[Previous

Scripts](/tools/clients/fcl-js/scripts)[Next

Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)

###### Rate this page

😞😐😊

* [Sending Your First Transaction](#sending-your-first-transaction)
* [Authorizing a Transaction](#authorizing-a-transaction)
* [Transaction Finality](#transaction-finality)

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