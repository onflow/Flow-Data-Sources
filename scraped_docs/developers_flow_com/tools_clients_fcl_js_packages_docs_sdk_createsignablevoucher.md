# Source: https://developers.flow.com/tools/clients/fcl-js/packages-docs/sdk/createSignableVoucher

createSignableVoucher | Flow Developer Portal



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
* createSignableVoucher

On this page

# createSignableVoucher

Creates a signable voucher object from an interaction for signing purposes.

A voucher is a standardized representation of a transaction that contains all the necessary
information for signing and submitting to the Flow network. This function transforms an
interaction object into a voucher format.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.createSignableVoucher(ix)`

Or import directly the specific function:

`_10

import { createSignableVoucher } from "@onflow/sdk"

_10

_10

createSignableVoucher(ix)`

## Usage[​](#usage "Direct link to Usage")

`` _27

import * as fcl from "@onflow/fcl";

_27

import { createSignableVoucher } from "@onflow/sdk"

_27

_27

// Build a transaction interaction

_27

const interaction = await fcl.build([

_27

fcl.transaction`

_27

transaction(amount: UFix64) {

_27

prepare(account: AuthAccount) {

_27

log(amount)

_27

}

_27

}

_27

`,

_27

fcl.args([fcl.arg("10.0", fcl.t.UFix64)]),

_27

fcl.proposer(proposerAuthz),

_27

fcl.payer(payerAuthz),

_27

fcl.authorizations([authorizerAuthz]),

_27

fcl.limit(100)

_27

]);

_27

_27

// Create a voucher for signing

_27

const voucher = createSignableVoucher(interaction);

_27

console.log(voucher.cadence); // The Cadence script

_27

console.log(voucher.arguments); // The transaction arguments

_27

console.log(voucher.proposalKey); // Proposer account details

_27

console.log(voucher.authorizers); // List of authorizer addresses

_27

_27

// The voucher can now be signed and submitted ``

## Parameters[​](#parameters "Direct link to Parameters")

### `ix`[​](#ix "Direct link to ix")

* Type: [`Interaction`](/tools/clients/fcl-js/packages-docs/types#interaction)
* Description: The interaction object containing transaction details

## Returns[​](#returns "Direct link to Returns")

`_10

{ cadence: string; refBlock: string; computeLimit: number; arguments: any[]; proposalKey: { address: string; keyId: string | number; sequenceNum: number; } | { address?: undefined; keyId?: undefined; sequenceNum?: undefined; }; payer: string; authorizers: string[]; payloadSigs: { address: string; keyId: string | number; sig: string; }[]; envelopeSigs: { address: string; keyId: string | number; sig: string; }[]; }`

A voucher object containing all transaction data and signatures

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/packages-docs/sdk/createSignableVoucher.md)

Last updated on **Jul 25, 2025** by **Jordan Ribbink**

[Previous

createSdkClient](/tools/clients/fcl-js/packages-docs/sdk/createSdkClient)[Next

decode](/tools/clients/fcl-js/packages-docs/sdk/decode)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)
* [Usage](#usage)
* [Parameters](#parameters)
  + [`ix`](#ix)
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