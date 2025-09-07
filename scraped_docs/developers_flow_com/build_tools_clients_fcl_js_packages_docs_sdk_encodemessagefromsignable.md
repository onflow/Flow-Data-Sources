# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable

encodeMessageFromSignable | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)

    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

        + [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)
        + [@onflow/sdk](/build/tools/clients/fcl-js/packages-docs/sdk)

          - [account](/build/tools/clients/fcl-js/packages-docs/sdk/account)
          - [arg](/build/tools/clients/fcl-js/packages-docs/sdk/arg)
          - [args](/build/tools/clients/fcl-js/packages-docs/sdk/args)
          - [atBlockHeight](/build/tools/clients/fcl-js/packages-docs/sdk/atBlockHeight)
          - [atBlockId](/build/tools/clients/fcl-js/packages-docs/sdk/atBlockId)
          - [atLatestBlock](/build/tools/clients/fcl-js/packages-docs/sdk/atLatestBlock)
          - [authorization](/build/tools/clients/fcl-js/packages-docs/sdk/authorization)
          - [authorizations](/build/tools/clients/fcl-js/packages-docs/sdk/authorizations)
          - [block](/build/tools/clients/fcl-js/packages-docs/sdk/block)
          - [build](/build/tools/clients/fcl-js/packages-docs/sdk/build)
          - [cadence](/build/tools/clients/fcl-js/packages-docs/sdk/cadence)
          - [cdc](/build/tools/clients/fcl-js/packages-docs/sdk/cdc)
          - [config](/build/tools/clients/fcl-js/packages-docs/sdk/config)
          - [createSdkClient](/build/tools/clients/fcl-js/packages-docs/sdk/createSdkClient)
          - [createSignableVoucher](/build/tools/clients/fcl-js/packages-docs/sdk/createSignableVoucher)
          - [decode](/build/tools/clients/fcl-js/packages-docs/sdk/decode)
          - [destroy](/build/tools/clients/fcl-js/packages-docs/sdk/destroy)
          - [encodeMessageFromSignable](/build/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable)
          - [encodeTransactionEnvelope](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionEnvelope)
          - [encodeTransactionPayload](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionPayload)
          - [encodeTxIdFromVoucher](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTxIdFromVoucher)
          - [get](/build/tools/clients/fcl-js/packages-docs/sdk/get)
          - [getAccount](/build/tools/clients/fcl-js/packages-docs/sdk/getAccount)
          - [getBlock](/build/tools/clients/fcl-js/packages-docs/sdk/getBlock)
          - [getBlockHeader](/build/tools/clients/fcl-js/packages-docs/sdk/getBlockHeader)
          - [getCollection](/build/tools/clients/fcl-js/packages-docs/sdk/getCollection)
          - [getEvents](/build/tools/clients/fcl-js/packages-docs/sdk/getEvents)
          - [getEventsAtBlockHeightRange](/build/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockHeightRange)
          - [getEventsAtBlockIds](/build/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockIds)
          - [getNetworkParameters](/build/tools/clients/fcl-js/packages-docs/sdk/getNetworkParameters)
          - [getNodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/sdk/getNodeVersionInfo)
          - [getTransaction](/build/tools/clients/fcl-js/packages-docs/sdk/getTransaction)
          - [getTransactionStatus](/build/tools/clients/fcl-js/packages-docs/sdk/getTransactionStatus)
          - [initInteraction](/build/tools/clients/fcl-js/packages-docs/sdk/initInteraction)
          - [interaction](/build/tools/clients/fcl-js/packages-docs/sdk/interaction)
          - [isBad](/build/tools/clients/fcl-js/packages-docs/sdk/isBad)
          - [isOk](/build/tools/clients/fcl-js/packages-docs/sdk/isOk)
          - [limit](/build/tools/clients/fcl-js/packages-docs/sdk/limit)
          - [nodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/sdk/nodeVersionInfo)
          - [param](/build/tools/clients/fcl-js/packages-docs/sdk/param)
          - [params](/build/tools/clients/fcl-js/packages-docs/sdk/params)
          - [payer](/build/tools/clients/fcl-js/packages-docs/sdk/payer)
          - [ping](/build/tools/clients/fcl-js/packages-docs/sdk/ping)
          - [pipe](/build/tools/clients/fcl-js/packages-docs/sdk/pipe)
          - [proposer](/build/tools/clients/fcl-js/packages-docs/sdk/proposer)
          - [put](/build/tools/clients/fcl-js/packages-docs/sdk/put)
          - [ref](/build/tools/clients/fcl-js/packages-docs/sdk/ref)
          - [resolve](/build/tools/clients/fcl-js/packages-docs/sdk/resolve)
          - [resolveAccounts](/build/tools/clients/fcl-js/packages-docs/sdk/resolveAccounts)
          - [resolveArguments](/build/tools/clients/fcl-js/packages-docs/sdk/resolveArguments)
          - [resolveCadence](/build/tools/clients/fcl-js/packages-docs/sdk/resolveCadence)
          - [resolveFinalNormalization](/build/tools/clients/fcl-js/packages-docs/sdk/resolveFinalNormalization)
          - [resolveProposerSequenceNumber](/build/tools/clients/fcl-js/packages-docs/sdk/resolveProposerSequenceNumber)
          - [resolveRefBlockId](/build/tools/clients/fcl-js/packages-docs/sdk/resolveRefBlockId)
          - [resolveSignatures](/build/tools/clients/fcl-js/packages-docs/sdk/resolveSignatures)
          - [resolveValidators](/build/tools/clients/fcl-js/packages-docs/sdk/resolveValidators)
          - [resolveVoucherIntercept](/build/tools/clients/fcl-js/packages-docs/sdk/resolveVoucherIntercept)
          - [response](/build/tools/clients/fcl-js/packages-docs/sdk/response)
          - [script](/build/tools/clients/fcl-js/packages-docs/sdk/script)
          - [send](/build/tools/clients/fcl-js/packages-docs/sdk/send)
          - [subscribe](/build/tools/clients/fcl-js/packages-docs/sdk/subscribe)
          - [subscribeEvents](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeEvents)
          - [subscribeRaw](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeRaw)
          - [TestUtils](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils)
          - [transaction](/build/tools/clients/fcl-js/packages-docs/sdk/transaction)
          - [update](/build/tools/clients/fcl-js/packages-docs/sdk/update)
          - [validator](/build/tools/clients/fcl-js/packages-docs/sdk/validator)
          - [voucherIntercept](/build/tools/clients/fcl-js/packages-docs/sdk/voucherIntercept)
          - [voucherToTxId](/build/tools/clients/fcl-js/packages-docs/sdk/voucherToTxId)
          - [why](/build/tools/clients/fcl-js/packages-docs/sdk/why)
        + [Type Definitions](/build/tools/clients/fcl-js/packages-docs/types)
      * [Authentication](/build/tools/clients/fcl-js/authentication)
      * [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)
      * [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)
      * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)
      * [Installation](/build/tools/clients/fcl-js/installation)
      * [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)
      * [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)
      * [Scripts](/build/tools/clients/fcl-js/scripts)
      * [Transactions](/build/tools/clients/fcl-js/transactions)
      * [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)
      * [WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)
    - [Flow Go SDK](/build/tools/clients/flow-go-sdk)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Client Tools](/build/tools/clients)
* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)
* [Packages Docs](/build/tools/clients/fcl-js/packages-docs)
* [@onflow/sdk](/build/tools/clients/fcl-js/packages-docs/sdk)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

destroy](/build/tools/clients/fcl-js/packages-docs/sdk/destroy)[Next

encodeTransactionEnvelope](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionEnvelope)

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
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.