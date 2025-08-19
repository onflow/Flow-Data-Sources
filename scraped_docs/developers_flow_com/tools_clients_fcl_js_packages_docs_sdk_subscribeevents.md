# Source: https://developers.flow.com/tools/clients/fcl-js/packages-docs/sdk/subscribeEvents

subscribeEvents | Flow Developer Portal



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
      * [@onflow/sdk](/tools/clients/fcl-js/packages-docs/sdk)

        + [account](/tools/clients/fcl-js/packages-docs/sdk/account)
        + [arg](/tools/clients/fcl-js/packages-docs/sdk/arg)
        + [args](/tools/clients/fcl-js/packages-docs/sdk/args)
        + [atBlockHeight](/tools/clients/fcl-js/packages-docs/sdk/atBlockHeight)
        + [atBlockId](/tools/clients/fcl-js/packages-docs/sdk/atBlockId)
        + [atLatestBlock](/tools/clients/fcl-js/packages-docs/sdk/atLatestBlock)
        + [authorization](/tools/clients/fcl-js/packages-docs/sdk/authorization)
        + [authorizations](/tools/clients/fcl-js/packages-docs/sdk/authorizations)
        + [block](/tools/clients/fcl-js/packages-docs/sdk/block)
        + [build](/tools/clients/fcl-js/packages-docs/sdk/build)
        + [cadence](/tools/clients/fcl-js/packages-docs/sdk/cadence)
        + [cdc](/tools/clients/fcl-js/packages-docs/sdk/cdc)
        + [config](/tools/clients/fcl-js/packages-docs/sdk/config)
        + [createSdkClient](/tools/clients/fcl-js/packages-docs/sdk/createSdkClient)
        + [createSignableVoucher](/tools/clients/fcl-js/packages-docs/sdk/createSignableVoucher)
        + [decode](/tools/clients/fcl-js/packages-docs/sdk/decode)
        + [destroy](/tools/clients/fcl-js/packages-docs/sdk/destroy)
        + [encodeMessageFromSignable](/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable)
        + [encodeTransactionEnvelope](/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionEnvelope)
        + [encodeTransactionPayload](/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionPayload)
        + [encodeTxIdFromVoucher](/tools/clients/fcl-js/packages-docs/sdk/encodeTxIdFromVoucher)
        + [get](/tools/clients/fcl-js/packages-docs/sdk/get)
        + [getAccount](/tools/clients/fcl-js/packages-docs/sdk/getAccount)
        + [getBlock](/tools/clients/fcl-js/packages-docs/sdk/getBlock)
        + [getBlockHeader](/tools/clients/fcl-js/packages-docs/sdk/getBlockHeader)
        + [getCollection](/tools/clients/fcl-js/packages-docs/sdk/getCollection)
        + [getEvents](/tools/clients/fcl-js/packages-docs/sdk/getEvents)
        + [getEventsAtBlockHeightRange](/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockHeightRange)
        + [getEventsAtBlockIds](/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockIds)
        + [getNetworkParameters](/tools/clients/fcl-js/packages-docs/sdk/getNetworkParameters)
        + [getNodeVersionInfo](/tools/clients/fcl-js/packages-docs/sdk/getNodeVersionInfo)
        + [getTransaction](/tools/clients/fcl-js/packages-docs/sdk/getTransaction)
        + [getTransactionStatus](/tools/clients/fcl-js/packages-docs/sdk/getTransactionStatus)
        + [initInteraction](/tools/clients/fcl-js/packages-docs/sdk/initInteraction)
        + [interaction](/tools/clients/fcl-js/packages-docs/sdk/interaction)
        + [isBad](/tools/clients/fcl-js/packages-docs/sdk/isBad)
        + [isOk](/tools/clients/fcl-js/packages-docs/sdk/isOk)
        + [limit](/tools/clients/fcl-js/packages-docs/sdk/limit)
        + [nodeVersionInfo](/tools/clients/fcl-js/packages-docs/sdk/nodeVersionInfo)
        + [param](/tools/clients/fcl-js/packages-docs/sdk/param)
        + [params](/tools/clients/fcl-js/packages-docs/sdk/params)
        + [payer](/tools/clients/fcl-js/packages-docs/sdk/payer)
        + [ping](/tools/clients/fcl-js/packages-docs/sdk/ping)
        + [pipe](/tools/clients/fcl-js/packages-docs/sdk/pipe)
        + [proposer](/tools/clients/fcl-js/packages-docs/sdk/proposer)
        + [put](/tools/clients/fcl-js/packages-docs/sdk/put)
        + [ref](/tools/clients/fcl-js/packages-docs/sdk/ref)
        + [resolve](/tools/clients/fcl-js/packages-docs/sdk/resolve)
        + [resolveAccounts](/tools/clients/fcl-js/packages-docs/sdk/resolveAccounts)
        + [resolveArguments](/tools/clients/fcl-js/packages-docs/sdk/resolveArguments)
        + [resolveCadence](/tools/clients/fcl-js/packages-docs/sdk/resolveCadence)
        + [resolveFinalNormalization](/tools/clients/fcl-js/packages-docs/sdk/resolveFinalNormalization)
        + [resolveProposerSequenceNumber](/tools/clients/fcl-js/packages-docs/sdk/resolveProposerSequenceNumber)
        + [resolveRefBlockId](/tools/clients/fcl-js/packages-docs/sdk/resolveRefBlockId)
        + [resolveSignatures](/tools/clients/fcl-js/packages-docs/sdk/resolveSignatures)
        + [resolveValidators](/tools/clients/fcl-js/packages-docs/sdk/resolveValidators)
        + [resolveVoucherIntercept](/tools/clients/fcl-js/packages-docs/sdk/resolveVoucherIntercept)
        + [response](/tools/clients/fcl-js/packages-docs/sdk/response)
        + [script](/tools/clients/fcl-js/packages-docs/sdk/script)
        + [send](/tools/clients/fcl-js/packages-docs/sdk/send)
        + [subscribe](/tools/clients/fcl-js/packages-docs/sdk/subscribe)
        + [subscribeEvents](/tools/clients/fcl-js/packages-docs/sdk/subscribeEvents)
        + [subscribeRaw](/tools/clients/fcl-js/packages-docs/sdk/subscribeRaw)
        + [TestUtils](/tools/clients/fcl-js/packages-docs/sdk/testUtils)
        + [transaction](/tools/clients/fcl-js/packages-docs/sdk/transaction)
        + [update](/tools/clients/fcl-js/packages-docs/sdk/update)
        + [validator](/tools/clients/fcl-js/packages-docs/sdk/validator)
        + [voucherIntercept](/tools/clients/fcl-js/packages-docs/sdk/voucherIntercept)
        + [voucherToTxId](/tools/clients/fcl-js/packages-docs/sdk/voucherToTxId)
        + [why](/tools/clients/fcl-js/packages-docs/sdk/why)
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
* [@onflow/sdk](/tools/clients/fcl-js/packages-docs/sdk)
* subscribeEvents

On this page

# subscribeEvents

Subscribe to events with the given filter and parameters.

Creates a subscription to listen for real-time events from the Flow blockchain. This function configures
the subscription parameters for filtering specific events based on type, addresses, contracts, and other criteria.

Events are emitted by Cadence code during transaction execution and provide insights into what happened.
Subscriptions allow you to listen for these events in real-time without polling.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.subscribeEvents(eventFilter)`

Or import directly the specific function:

`_10

import { subscribeEvents } from "@onflow/sdk"

_10

_10

subscribeEvents(eventFilter)`

## Usage[​](#usage "Direct link to Usage")

`_23

import * as fcl from "@onflow/fcl";

_23

_23

// Subscribe to FlowToken transfer events

_23

const subscription = await fcl.send([

_23

fcl.subscribeEvents({

_23

eventTypes: [

_23

"A.1654653399040a61.FlowToken.TokensWithdrawn",

_23

"A.1654653399040a61.FlowToken.TokensDeposited"

_23

],

_23

startHeight: 1000000, // Start from specific block height

_23

heartbeatInterval: 3000 // 3 second heartbeat

_23

})

_23

]);

_23

_23

// Subscribe to events from specific contracts

_23

const contractSubscription = await fcl.send([

_23

fcl.subscribeEvents({

_23

contracts: ["FlowToken", "FungibleToken"],

_23

addresses: ["0x1654653399040a61"]

_23

})

_23

]);

_23

_23

// Handle the subscription data elsewhere using fcl.subscribe()`

## Parameters[​](#parameters "Direct link to Parameters")

### `eventFilter`[​](#eventfilter "Direct link to eventfilter")

* Type: [`EventFilter`](/tools/clients/fcl-js/packages-docs/types#eventfilter)

## Returns[​](#returns "Direct link to Returns")

`_10

export type InteractionBuilderFn = (

_10

ix: Interaction

_10

) => Interaction | Promise<Interaction>`

A function that processes an interaction object

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/packages-docs/sdk/subscribeEvents.md)

Last updated on **Jul 25, 2025** by **Jordan Ribbink**

[Previous

subscribe](/tools/clients/fcl-js/packages-docs/sdk/subscribe)[Next

subscribeRaw](/tools/clients/fcl-js/packages-docs/sdk/subscribeRaw)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)
* [Usage](#usage)
* [Parameters](#parameters)
  + [`eventFilter`](#eventfilter)
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