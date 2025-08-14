# Source: https://developers.flow.com/tools/clients/fcl-js/packages-docs/fcl/getCollection

getCollection | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/react-sdk](/tools/react-sdk)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)

    - [Packages Docs](/tools/clients/fcl-js/packages-docs)

      * [@onflow/fcl](/tools/clients/fcl-js/packages-docs/fcl)

        + [account](/tools/clients/fcl-js/packages-docs/fcl/account)
        + [arg](/tools/clients/fcl-js/packages-docs/fcl/arg)
        + [args](/tools/clients/fcl-js/packages-docs/fcl/args)
        + [atBlockHeight](/tools/clients/fcl-js/packages-docs/fcl/atBlockHeight)
        + [atBlockId](/tools/clients/fcl-js/packages-docs/fcl/atBlockId)
        + [authenticate](/tools/clients/fcl-js/packages-docs/fcl/authenticate)
        + [authorization](/tools/clients/fcl-js/packages-docs/fcl/authorization)
        + [authorizations](/tools/clients/fcl-js/packages-docs/fcl/authorizations)
        + [authz](/tools/clients/fcl-js/packages-docs/fcl/authz)
        + [block](/tools/clients/fcl-js/packages-docs/fcl/block)
        + [build](/tools/clients/fcl-js/packages-docs/fcl/build)
        + [cadence](/tools/clients/fcl-js/packages-docs/fcl/cadence)
        + [cdc](/tools/clients/fcl-js/packages-docs/fcl/cdc)
        + [config](/tools/clients/fcl-js/packages-docs/fcl/config)
        + [createFcl](/tools/clients/fcl-js/packages-docs/fcl/createFcl)
        + [createSignableVoucher](/tools/clients/fcl-js/packages-docs/fcl/createSignableVoucher)
        + [currentUser](/tools/clients/fcl-js/packages-docs/fcl/currentUser)
        + [decode](/tools/clients/fcl-js/packages-docs/fcl/decode)
        + [display](/tools/clients/fcl-js/packages-docs/fcl/display)
        + [events](/tools/clients/fcl-js/packages-docs/fcl/events)
        + [getAccount](/tools/clients/fcl-js/packages-docs/fcl/getAccount)
        + [getBlock](/tools/clients/fcl-js/packages-docs/fcl/getBlock)
        + [getBlockHeader](/tools/clients/fcl-js/packages-docs/fcl/getBlockHeader)
        + [getChainId](/tools/clients/fcl-js/packages-docs/fcl/getChainId)
        + [getCollection](/tools/clients/fcl-js/packages-docs/fcl/getCollection)
        + [getEvents](/tools/clients/fcl-js/packages-docs/fcl/getEvents)
        + [getEventsAtBlockHeightRange](/tools/clients/fcl-js/packages-docs/fcl/getEventsAtBlockHeightRange)
        + [getEventsAtBlockIds](/tools/clients/fcl-js/packages-docs/fcl/getEventsAtBlockIds)
        + [getNetworkParameters](/tools/clients/fcl-js/packages-docs/fcl/getNetworkParameters)
        + [getNodeVersionInfo](/tools/clients/fcl-js/packages-docs/fcl/getNodeVersionInfo)
        + [getTransaction](/tools/clients/fcl-js/packages-docs/fcl/getTransaction)
        + [getTransactionStatus](/tools/clients/fcl-js/packages-docs/fcl/getTransactionStatus)
        + [invariant](/tools/clients/fcl-js/packages-docs/fcl/invariant)
        + [isBad](/tools/clients/fcl-js/packages-docs/fcl/isBad)
        + [isOk](/tools/clients/fcl-js/packages-docs/fcl/isOk)
        + [limit](/tools/clients/fcl-js/packages-docs/fcl/limit)
        + [logIn](/tools/clients/fcl-js/packages-docs/fcl/logIn)
        + [mutate](/tools/clients/fcl-js/packages-docs/fcl/mutate)
        + [nodeVersionInfo](/tools/clients/fcl-js/packages-docs/fcl/nodeVersionInfo)
        + [param](/tools/clients/fcl-js/packages-docs/fcl/param)
        + [params](/tools/clients/fcl-js/packages-docs/fcl/params)
        + [payer](/tools/clients/fcl-js/packages-docs/fcl/payer)
        + [ping](/tools/clients/fcl-js/packages-docs/fcl/ping)
        + [pipe](/tools/clients/fcl-js/packages-docs/fcl/pipe)
        + [pluginRegistry](/tools/clients/fcl-js/packages-docs/fcl/pluginRegistry)
        + [proposer](/tools/clients/fcl-js/packages-docs/fcl/proposer)
        + [query](/tools/clients/fcl-js/packages-docs/fcl/query)
        + [queryRaw](/tools/clients/fcl-js/packages-docs/fcl/queryRaw)
        + [reauthenticate](/tools/clients/fcl-js/packages-docs/fcl/reauthenticate)
        + [ref](/tools/clients/fcl-js/packages-docs/fcl/ref)
        + [sansPrefix](/tools/clients/fcl-js/packages-docs/fcl/sansPrefix)
        + [script](/tools/clients/fcl-js/packages-docs/fcl/script)
        + [send](/tools/clients/fcl-js/packages-docs/fcl/send)
        + [serialize](/tools/clients/fcl-js/packages-docs/fcl/serialize)
        + [signUp](/tools/clients/fcl-js/packages-docs/fcl/signUp)
        + [subscribe](/tools/clients/fcl-js/packages-docs/fcl/subscribe)
        + [subscribeEvents](/tools/clients/fcl-js/packages-docs/fcl/subscribeEvents)
        + [subscribeRaw](/tools/clients/fcl-js/packages-docs/fcl/subscribeRaw)
        + [transaction](/tools/clients/fcl-js/packages-docs/fcl/transaction)
        + [tx](/tools/clients/fcl-js/packages-docs/fcl/tx)
        + [unauthenticate](/tools/clients/fcl-js/packages-docs/fcl/unauthenticate)
        + [validator](/tools/clients/fcl-js/packages-docs/fcl/validator)
        + [verifyUserSignatures](/tools/clients/fcl-js/packages-docs/fcl/verifyUserSignatures)
        + [voucherIntercept](/tools/clients/fcl-js/packages-docs/fcl/voucherIntercept)
        + [voucherToTxId](/tools/clients/fcl-js/packages-docs/fcl/voucherToTxId)
        + [why](/tools/clients/fcl-js/packages-docs/fcl/why)
        + [withPrefix](/tools/clients/fcl-js/packages-docs/fcl/withPrefix)
      * [@onflow/sdk](/tools/clients/fcl-js/packages-docs/sdk)
      * [Type Definitions](/tools/clients/fcl-js/packages-docs/types)
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
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* [Packages Docs](/tools/clients/fcl-js/packages-docs)
* [@onflow/fcl](/tools/clients/fcl-js/packages-docs/fcl)
* getCollection

On this page

# getCollection

A builder function that returns a collection containing a list of transaction IDs by its collection ID.

A collection is a batch of transactions that have been included in a block. Each collection has a unique ID
which is the SHA3-256 hash of the collection payload. Collections are used to group related transactions
together for more efficient processing by the network.

The collection ID provided must be from the current spork. Collections from past sporks are currently unavailable.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as fcl from "@onflow/fcl"

_10

_10

fcl.getCollection(id)`

Or import directly the specific function:

`_10

import { getCollection } from "@onflow/fcl"

_10

_10

getCollection(id)`

## Usage[​](#usage "Direct link to Usage")

`_18

import * as fcl from "@onflow/fcl";

_18

_18

// Get a collection and see what transactions it contains

_18

const collection = await fcl.send([

_18

fcl.getCollection("cccdb0c67d015dc7f6444e8f62a3244ed650215ed66b90603006c70c5ef1f6e5")

_18

]).then(fcl.decode);

_18

_18

console.log("Collection ID:", collection.id);

_18

console.log("Transaction IDs:", collection.transactionIds);

_18

console.log("Total transactions:", collection.transactionIds.length);

_18

_18

// Process each transaction in the collection

_18

for (const txId of collection.transactionIds) {

_18

const transaction = await fcl.send([

_18

fcl.getTransaction(txId)

_18

]).then(fcl.decode);

_18

console.log("Transaction:", transaction);

_18

}`

## Parameters[​](#parameters "Direct link to Parameters")

### `id` (optional)[​](#id-optional "Direct link to id-optional")

* Type: `string`

## Returns[​](#returns "Direct link to Returns")

`_10

export type InteractionBuilderFn = (

_10

ix: Interaction

_10

) => Interaction | Promise<Interaction>`

A function that processes an interaction object

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/packages-docs/fcl/getCollection.md)

Last updated on **Jul 25, 2025** by **Jordan Ribbink**

[Previous

getChainId](/tools/clients/fcl-js/packages-docs/fcl/getChainId)[Next

getEvents](/tools/clients/fcl-js/packages-docs/fcl/getEvents)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)
* [Usage](#usage)
* [Parameters](#parameters)
  + [`id` (optional)](#id-optional)
* [Returns](#returns)

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
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.