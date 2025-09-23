# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/sdk/testUtils

TestUtils | Flow Developer Portal



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
* TestUtils

On this page

# TestUtils

## Overview[​](#overview "Direct link to Overview")

Namespace containing TestUtils utilities

## Functions[​](#functions "Direct link to Functions")

### authzDeepResolveMany[​](#authzdeepresolvemany "Direct link to authzDeepResolveMany")

Creates a deep test authorization resolver with nested resolution for complex testing scenarios.

#### Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.authzDeepResolveMany(opts, depth)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.authzDeepResolveMany(opts, depth)`

#### Parameters[​](#parameters "Direct link to Parameters")

##### `opts` (optional)[​](#opts-optional "Direct link to opts-optional")

* Type:

`_10

interface IAuthzResolveMany {

_10

tempId?: string

_10

authorizations: any[]

_10

proposer?: any

_10

payer?: any

_10

}`

* Description: Configuration including authorizations array and optional proposer/payer

##### `depth` (optional)[​](#depth-optional "Direct link to depth-optional")

* Type: `number`
* Description: The depth of nesting for the resolver (default: 1)

#### Returns[​](#returns "Direct link to Returns")

[`InteractionAccount`](/build/tools/clients/fcl-js/packages-docs/types#interactionaccount)

### authzFn[​](#authzfn "Direct link to authzFn")

Creates a test authorization function for testing transactions.

#### Import[​](#import-1 "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.authzFn(opts)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.authzFn(opts)`

#### Parameters[​](#parameters-1 "Direct link to Parameters")

##### `opts` (optional)[​](#opts-optional-1 "Direct link to opts-optional-1")

* Type:

`_10

interface IAuthzOpts {

_10

signingFunction?: (signable: any) => any

_10

}`

* Description: Optional configuration including custom signing function

#### Returns[​](#returns-1 "Direct link to Returns")

`Partial<InteractionAccount>`

### authzResolve[​](#authzresolve "Direct link to authzResolve")

Creates a test authorization resolver that can be used for testing account resolution.

#### Import[​](#import-2 "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.authzResolve(opts)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.authzResolve(opts)`

#### Parameters[​](#parameters-2 "Direct link to Parameters")

##### `opts` (optional)[​](#opts-optional-2 "Direct link to opts-optional-2")

* Type:

`_10

interface IAuthzResolveOpts {

_10

tempId?: string

_10

}`

* Description: Optional configuration including temporary ID

#### Returns[​](#returns-2 "Direct link to Returns")

`_10

Partial<InteractionAccount>; kind: InteractionResolverKind.ACCOUNT; addr: string; keyId: string | number; sequenceNum: number; signature: string; signingFunction: any; role: { proposer: boolean; authorizer: boolean; payer: boolean; param?: boolean; }; authorization: any; }`

### authzResolveMany[​](#authzresolvemany "Direct link to authzResolveMany")

Creates a test authorization resolver that handles multiple accounts with different roles.

#### Import[​](#import-3 "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.authzResolveMany(opts)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.authzResolveMany(opts)`

#### Parameters[​](#parameters-3 "Direct link to Parameters")

##### `opts` (optional)[​](#opts-optional-3 "Direct link to opts-optional-3")

* Type:

`_10

interface IAuthzResolveMany {

_10

tempId?: string

_10

authorizations: any[]

_10

proposer?: any

_10

payer?: any

_10

}`

* Description: Configuration including authorizations array and optional proposer/payer

#### Returns[​](#returns-3 "Direct link to Returns")

[`InteractionAccount`](/build/tools/clients/fcl-js/packages-docs/types#interactionaccount)

### idof[​](#idof "Direct link to idof")

Generates a unique identifier for an account based on its address and key ID.

#### Import[​](#import-4 "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.idof(acct)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.idof(acct)`

#### Parameters[​](#parameters-4 "Direct link to Parameters")

##### `acct`[​](#acct "Direct link to acct")

* Type: [`InteractionAccount`](/build/tools/clients/fcl-js/packages-docs/types#interactionaccount)
* Description: The account object

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

### run[​](#run "Direct link to run")

Runs a set of functions on an interaction

This is a utility function for testing that builds and resolves an interaction with the provided builder functions.
It automatically adds a reference block and then resolves the interaction for testing purposes.

#### Import[​](#import-5 "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.run(fns)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.run(fns)`

#### Usage[​](#usage "Direct link to Usage")

`` _28

import { run } from "@onflow/sdk"

_28

import * as fcl from "@onflow/fcl";

_28

_28

// Test a simple script interaction

_28

const result = await run([

_28

fcl.script`

_28

access(all) fun main(): Int {

_28

return 42

_28

}

_28

`

_28

]);

_28

_28

console.log(result.cadence); // The Cadence script

_28

console.log(result.tag); // "SCRIPT"

_28

_28

// Test a transaction with arguments

_28

const txResult = await run([

_28

fcl.transaction`

_28

transaction(amount: UFix64) {

_28

prepare(account: AuthAccount) {

_28

log(amount)

_28

}

_28

}

_28

`,

_28

fcl.args([fcl.arg("10.0", fcl.t.UFix64)])

_28

]);

_28

_28

console.log(txResult.message.arguments); // The resolved arguments ``

#### Parameters[​](#parameters-5 "Direct link to Parameters")

##### `fns` (optional)[​](#fns-optional "Direct link to fns-optional")

* Type:

`_10

((ix: Interaction) => Interaction | Promise<Interaction>)[]`

* Description: An array of functions to run on the interaction

#### Returns[​](#returns-5 "Direct link to Returns")

[`Promise<Interaction>`](/build/tools/clients/fcl-js/packages-docs/types#interaction)

### sig[​](#sig "Direct link to sig")

Generates a test signature string for an account.

#### Import[​](#import-6 "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.TestUtils.sig(opts)`

Or import the namespace directly:

`_10

import { TestUtils } from "@onflow/sdk"

_10

_10

TestUtils.sig(opts)`

#### Parameters[​](#parameters-6 "Direct link to Parameters")

##### `opts`[​](#opts "Direct link to opts")

* Type: `Partial<InteractionAccount>`
* Description: Partial account object containing address and keyId

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/sdk/testUtils.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

subscribeRaw](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeRaw)[Next

transaction](/build/tools/clients/fcl-js/packages-docs/sdk/transaction)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)
* [Functions](#functions)
  + [authzDeepResolveMany](#authzdeepresolvemany)
  + [authzFn](#authzfn)
  + [authzResolve](#authzresolve)
  + [authzResolveMany](#authzresolvemany)
  + [idof](#idof)
  + [run](#run)
  + [sig](#sig)

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
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.