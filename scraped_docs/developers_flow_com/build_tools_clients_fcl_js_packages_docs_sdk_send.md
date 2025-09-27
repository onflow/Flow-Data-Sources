# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/sdk/send

send | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/quickstart)

  + [Quickstart ↙](/build/cadence/quickstart)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Basics](/build/cadence/basics/network-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [EVM Wallet Setup](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
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
* send

On this page

# send

Sends arbitrary scripts, transactions, and requests to Flow.

This method consumes an array of builders that are to be resolved and sent. The builders required to be included in the array depend on the interaction that is being built.

WARNING: Must be used in conjunction with 'fcl.decode(response)' to get back correct keys and all values in JSON.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as sdk from "@onflow/sdk"

_10

_10

sdk.send(args, opts)`

Or import directly the specific function:

`_10

import { send } from "@onflow/sdk"

_10

_10

send(args, opts)`

## Usage[​](#usage "Direct link to Usage")

`` _18

import * as fcl from "@onflow/fcl";

_18

_18

// a script only needs to resolve the arguments to the script

_18

const response = await fcl.send([fcl.script`${script}`, fcl.args(args)]);

_18

// note: response values are encoded, call await fcl.decode(response) to get JSON

_18

_18

// a transaction requires multiple 'builders' that need to be resolved prior to being sent to the chain - such as setting the authorizations.

_18

const response = await fcl.send([

_18

fcl.transaction`

_18

${transaction}

_18

`,

_18

fcl.args(args),

_18

fcl.proposer(proposer),

_18

fcl.authorizations(authorizations),

_18

fcl.payer(payer),

_18

fcl.limit(9999)

_18

]);

_18

// note: response contains several values ``

## Parameters[​](#parameters "Direct link to Parameters")

### `args` (optional)[​](#args-optional "Direct link to args-optional")

* Type:

`_10

false | InteractionBuilderFn | (false | InteractionBuilderFn)[]`

* Description: An array of builders (functions that take an interaction object and return a new interaction object)

### `opts` (optional)[​](#opts-optional "Direct link to opts-optional")

* Type: `any`
* Description: Additional optional options for the request

#### Properties:[​](#properties "Direct link to Properties:")

* **`node`** - Custom node endpoint to use for this request
* **`resolve`** - Custom resolve function to use for processing the interaction

## Returns[​](#returns "Direct link to Returns")

`Promise<any>`

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/sdk/send.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

script](/build/tools/clients/fcl-js/packages-docs/sdk/script)[Next

subscribe](/build/tools/clients/fcl-js/packages-docs/sdk/subscribe)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)
* [Usage](#usage)
* [Parameters](#parameters)
  + [`args` (optional)](#args-optional)
  + [`opts` (optional)](#opts-optional)
* [Returns](#returns)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
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
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.