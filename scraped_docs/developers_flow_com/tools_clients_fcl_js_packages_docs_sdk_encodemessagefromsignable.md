# Source: https://developers.flow.com/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable

encodeMessageFromSignable | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/blockchain-development-tutorials)

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
* encodeMessageFromSignable

On this page

# encodeMessageFromSignable

Encodes a message from a signable object for a specific signer address.

This function determines whether the signer should sign the transaction payload or envelope
based on their role in the transaction (authorizer, proposer, or payer), then encodes the
appropriate message for signing.

Payload signers include authorizers and proposers (but not payers)
Envelope signers include only payers

The encoded message is what gets signed by the account's private key to create the transaction signature.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.encodeMessageFromSignable(signable, signerAddress)`

Or import directly the specific function:

`_10

import { encodeMessageFromSignable } from "@onflow/sdk"

_10

_10

encodeMessageFromSignable(signable, signerAddress)`

## Usage[​](#usage "Direct link to Usage")

`_25

import * as fcl from "@onflow/fcl";

_25

_25

// This function is typically used internally by authorization functions

_25

// when implementing custom wallet connectors or signing flows

_25

_25

const signable = {

_25

voucher: {

_25

cadence: "transaction { prepare(acct: AuthAccount) {} }",

_25

authorizers: ["0x01"],

_25

proposalKey: { address: "0x01", keyId: 0, sequenceNum: 42 },

_25

payer: "0x02",

_25

refBlock: "a1b2c3",

_25

computeLimit: 100,

_25

arguments: [],

_25

payloadSigs: []

_25

}

_25

};

_25

_25

// For an authorizer (payload signer)

_25

const authorizerMessage = fcl.encodeMessageFromSignable(signable, "0x01");

_25

console.log("Authorizer signs:", authorizerMessage);

_25

_25

// For a payer (envelope signer)

_25

const payerMessage = fcl.encodeMessageFromSignable(signable, "0x02");

_25

console.log("Payer signs:", payerMessage);`

## Parameters[​](#parameters "Direct link to Parameters")

### `signable`[​](#signable "Direct link to signable")

* Type:

`_10

export interface Signable {

_10

message: string

_10

addr?: string

_10

keyId?: number

_10

signature?: string

_10

roles: Record<string, boolean>

_10

voucher: Voucher

_10

[key: string]: any

_10

}`

* Description: The signable object containing transaction data and voucher

### `signerAddress`[​](#signeraddress "Direct link to signeraddress")

* Type: `string`
* Description: The address of the signer to encode the message for

## Returns[​](#returns "Direct link to Returns")

`string`

An encoded message string suitable for signing with the account's private key

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable.md)

Last updated on **Jul 25, 2025** by **Jordan Ribbink**

[Previous

destroy](/tools/clients/fcl-js/packages-docs/sdk/destroy)[Next

encodeTransactionEnvelope](/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionEnvelope)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)
* [Usage](#usage)
* [Parameters](#parameters)
  + [`signable`](#signable)
  + [`signerAddress`](#signeraddress)
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