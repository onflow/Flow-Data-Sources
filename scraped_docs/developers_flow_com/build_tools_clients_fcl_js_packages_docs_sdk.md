# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/sdk

@onflow/sdk | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                        + [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)

                          + [@onflow/sdk](/build/tools/clients/fcl-js/packages-docs/sdk)

                            - [account](/build/tools/clients/fcl-js/packages-docs/sdk/account)- [arg](/build/tools/clients/fcl-js/packages-docs/sdk/arg)- [args](/build/tools/clients/fcl-js/packages-docs/sdk/args)- [atBlockHeight](/build/tools/clients/fcl-js/packages-docs/sdk/atBlockHeight)- [atBlockId](/build/tools/clients/fcl-js/packages-docs/sdk/atBlockId)- [atLatestBlock](/build/tools/clients/fcl-js/packages-docs/sdk/atLatestBlock)- [authorization](/build/tools/clients/fcl-js/packages-docs/sdk/authorization)- [authorizations](/build/tools/clients/fcl-js/packages-docs/sdk/authorizations)- [block](/build/tools/clients/fcl-js/packages-docs/sdk/block)- [build](/build/tools/clients/fcl-js/packages-docs/sdk/build)- [cadence](/build/tools/clients/fcl-js/packages-docs/sdk/cadence)- [cdc](/build/tools/clients/fcl-js/packages-docs/sdk/cdc)- [config](/build/tools/clients/fcl-js/packages-docs/sdk/config)- [createSdkClient](/build/tools/clients/fcl-js/packages-docs/sdk/createSdkClient)- [createSignableVoucher](/build/tools/clients/fcl-js/packages-docs/sdk/createSignableVoucher)- [decode](/build/tools/clients/fcl-js/packages-docs/sdk/decode)- [destroy](/build/tools/clients/fcl-js/packages-docs/sdk/destroy)- [encodeMessageFromSignable](/build/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable)- [encodeTransactionEnvelope](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionEnvelope)- [encodeTransactionPayload](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionPayload)- [encodeTxIdFromVoucher](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTxIdFromVoucher)- [get](/build/tools/clients/fcl-js/packages-docs/sdk/get)- [getAccount](/build/tools/clients/fcl-js/packages-docs/sdk/getAccount)- [getBlock](/build/tools/clients/fcl-js/packages-docs/sdk/getBlock)- [getBlockHeader](/build/tools/clients/fcl-js/packages-docs/sdk/getBlockHeader)- [getCollection](/build/tools/clients/fcl-js/packages-docs/sdk/getCollection)- [getEvents](/build/tools/clients/fcl-js/packages-docs/sdk/getEvents)- [getEventsAtBlockHeightRange](/build/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockHeightRange)- [getEventsAtBlockIds](/build/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockIds)- [getNetworkParameters](/build/tools/clients/fcl-js/packages-docs/sdk/getNetworkParameters)- [getNodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/sdk/getNodeVersionInfo)- [getTransaction](/build/tools/clients/fcl-js/packages-docs/sdk/getTransaction)- [getTransactionStatus](/build/tools/clients/fcl-js/packages-docs/sdk/getTransactionStatus)- [initInteraction](/build/tools/clients/fcl-js/packages-docs/sdk/initInteraction)- [interaction](/build/tools/clients/fcl-js/packages-docs/sdk/interaction)- [isBad](/build/tools/clients/fcl-js/packages-docs/sdk/isBad)- [isOk](/build/tools/clients/fcl-js/packages-docs/sdk/isOk)- [limit](/build/tools/clients/fcl-js/packages-docs/sdk/limit)- [nodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/sdk/nodeVersionInfo)- [param](/build/tools/clients/fcl-js/packages-docs/sdk/param)- [params](/build/tools/clients/fcl-js/packages-docs/sdk/params)- [payer](/build/tools/clients/fcl-js/packages-docs/sdk/payer)- [ping](/build/tools/clients/fcl-js/packages-docs/sdk/ping)- [pipe](/build/tools/clients/fcl-js/packages-docs/sdk/pipe)- [proposer](/build/tools/clients/fcl-js/packages-docs/sdk/proposer)- [put](/build/tools/clients/fcl-js/packages-docs/sdk/put)- [ref](/build/tools/clients/fcl-js/packages-docs/sdk/ref)- [resolve](/build/tools/clients/fcl-js/packages-docs/sdk/resolve)- [resolveAccounts](/build/tools/clients/fcl-js/packages-docs/sdk/resolveAccounts)- [resolveArguments](/build/tools/clients/fcl-js/packages-docs/sdk/resolveArguments)- [resolveCadence](/build/tools/clients/fcl-js/packages-docs/sdk/resolveCadence)- [resolveFinalNormalization](/build/tools/clients/fcl-js/packages-docs/sdk/resolveFinalNormalization)- [resolveProposerSequenceNumber](/build/tools/clients/fcl-js/packages-docs/sdk/resolveProposerSequenceNumber)- [resolveRefBlockId](/build/tools/clients/fcl-js/packages-docs/sdk/resolveRefBlockId)- [resolveSignatures](/build/tools/clients/fcl-js/packages-docs/sdk/resolveSignatures)- [resolveValidators](/build/tools/clients/fcl-js/packages-docs/sdk/resolveValidators)- [resolveVoucherIntercept](/build/tools/clients/fcl-js/packages-docs/sdk/resolveVoucherIntercept)- [response](/build/tools/clients/fcl-js/packages-docs/sdk/response)- [script](/build/tools/clients/fcl-js/packages-docs/sdk/script)- [send](/build/tools/clients/fcl-js/packages-docs/sdk/send)- [subscribe](/build/tools/clients/fcl-js/packages-docs/sdk/subscribe)- [subscribeEvents](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeEvents)- [subscribeRaw](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeRaw)- [TestUtils](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils)- [transaction](/build/tools/clients/fcl-js/packages-docs/sdk/transaction)- [update](/build/tools/clients/fcl-js/packages-docs/sdk/update)- [validator](/build/tools/clients/fcl-js/packages-docs/sdk/validator)- [voucherIntercept](/build/tools/clients/fcl-js/packages-docs/sdk/voucherIntercept)- [voucherToTxId](/build/tools/clients/fcl-js/packages-docs/sdk/voucherToTxId)- [why](/build/tools/clients/fcl-js/packages-docs/sdk/why)+ [Type Definitions](/build/tools/clients/fcl-js/packages-docs/types)* [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Packages Docs](/build/tools/clients/fcl-js/packages-docs)* @onflow/sdk

On this page

# @onflow/sdk

## Overview[​](#overview "Direct link to Overview")

The Flow sdk library provides a set of tools for developers to build applications on the Flow blockchain.

## Installation[​](#installation "Direct link to Installation")

You can install the @onflow/sdk package using npm or yarn:

`_10

npm install @onflow/sdk`

Or using yarn:

`_10

yarn add @onflow/sdk`

### Requirements[​](#requirements "Direct link to Requirements")

* Node.js 14.x or later

### Importing[​](#importing "Direct link to Importing")

You can import the entire package:

`_10

import * as sdk from '@onflow/sdk';`

Or import specific functions:

`_10

import { functionName } from '@onflow/sdk';`

## Connect[​](#connect "Direct link to Connect")

By default, the library uses HTTP to communicate with the access nodes and it must be configured with the correct access node API URL. An error will be returned if the host is unreachable.

Example:

`_10

import { config } from '@onflow/fcl';

_10

_10

config({

_10

'accessNode.api': 'https://rest-testnet.onflow.org',

_10

});`

## Querying the Flow Network[​](#querying-the-flow-network "Direct link to Querying the Flow Network")

After you have established a connection with an access node, you can query the Flow network to retrieve data about blocks, accounts, events and transactions. We will explore how to retrieve each of these entities in the sections below.

## Mutate Flow Network[​](#mutate-flow-network "Direct link to Mutate Flow Network")

Flow, like most blockchains, allows anybody to submit a transaction that mutates the shared global chain state. A transaction is an object that holds a payload, which describes the state mutation, and one or more authorizations that permit the transaction to mutate the state owned by specific accounts.

Transaction data is composed and signed with help of the SDK. The signed payload of transaction then gets submitted to the access node API. If a transaction is invalid or the correct number of authorizing signatures are not provided, it gets rejected.

## Transactions[​](#transactions "Direct link to Transactions")

A transaction is nothing more than a signed set of data that includes script code which are instructions on how to mutate the network state and properties that define and limit it's execution. All these properties are explained below.

**Script** field is the portion of the transaction that describes the state mutation logic. On Flow, transaction logic is written in [Cadence](https://cadence-lang.org/docs). Here is an example transaction script:

`_10

transaction(greeting: string) {

_10

execute {

_10

log(greeting.concat(", World!"))

_10

}

_10

}`

**Arguments**. A transaction can accept zero or more arguments that are passed into the Cadence script. The arguments on the transaction must match the number and order declared in the Cadence script. Sample script from above accepts a single `String` argument.

**Proposal key** must be provided to act as a sequence number and prevent replay and other potential attacks.

Each account key maintains a separate transaction sequence counter; the key that lends its sequence number to a transaction is called the proposal key.

A proposal key contains three fields:

* Account address
* Key index
* Sequence number

A transaction is only valid if its declared sequence number matches the current on-chain sequence number for that key. The sequence number increments by one after the transaction is executed.

**Payer** is the account that pays the fees for the transaction. A transaction must specify exactly one payer. The payer is only responsible for paying the network and compute unit (gas) fees; the transaction is not authorized to access resources or code stored in the payer account.

**Authorizers** are accounts that authorize a transaction to read and mutate their resources. A transaction can specify zero or more authorizers, depending on how many accounts the transaction needs to access.

The number of authorizers on the transaction must match the number of `&Account` parameters declared in the prepare statement of the Cadence script.

Example transaction with multiple authorizers:

`_10

transaction {

_10

prepare(authorizer1: &Account, authorizer2: &Account) { }

_10

}`

**Compute Limit** is the limit on the amount of computation a transaction requires, and it will abort if it exceeds its compute unit limit. Cadence uses metering to measure the number of operations per transaction. You can read more about it in the [Cadence documentation](https://cadence-lang.org/docs).

The compute limit depends on the complexity of the transaction script. Until dedicated estimation tooling exists, it's best to use the emulator to test complex transactions and determine a safe limit.

Keep in mind that Flow is **very** efficient, so transaction fees are generally low. A limit resulting in max charges of `.001` Flow is sufficient to cover even complex transactions.

* Flow token transfer: 19 CU.
  + Single NFT Transfer: 26 CU.
  + EVM Token transfer 28 CU.

**Reference block** specifies an expiration window (measured in blocks) during which a transaction is considered valid by the network. A transaction will be rejected if it is submitted past its expiry block. Flow calculates transaction expiry using the *reference block* field on a transaction. A transaction expires after `600` blocks are committed on top of the reference block, which takes about 8 minutes at average Mainnet block rates.

## API Reference[​](#api-reference "Direct link to API Reference")

This section contains documentation for all of the functions and namespaces in the sdk package.

* [account](/build/tools/clients/fcl-js/packages-docs/sdk/account) - Retrieve any account from Flow network's latest block or from a specified block...
* [arg](/build/tools/clients/fcl-js/packages-docs/sdk/arg) - A utility builder to be used with fcl.args[...] to create FCL supported...
* [args](/build/tools/clients/fcl-js/packages-docs/sdk/args) - A utility builder to be used with other builders to pass in arguments with a...
* [atBlockHeight](/build/tools/clients/fcl-js/packages-docs/sdk/atBlockHeight) - A builder function that returns a partial interaction to a block at a specific...
* [atBlockId](/build/tools/clients/fcl-js/packages-docs/sdk/atBlockId) - A builder function that returns a partial interaction to a block at a specific...
* [atLatestBlock](/build/tools/clients/fcl-js/packages-docs/sdk/atLatestBlock) - A builder function that returns a partial interaction to query the latest block...
* [authorization](/build/tools/clients/fcl-js/packages-docs/sdk/authorization) - Creates an authorization function for use in transactions. An authorization...
* [authorizations](/build/tools/clients/fcl-js/packages-docs/sdk/authorizations) - A utility builder to set the authorizations on a transaction. Authorizations...
* [block](/build/tools/clients/fcl-js/packages-docs/sdk/block) - Query the network for block by id, height or get the latest block. Block ID is...
* [build](/build/tools/clients/fcl-js/packages-docs/sdk/build) - A builder function that creates an interaction from an array of builder...
* [cadence](/build/tools/clients/fcl-js/packages-docs/sdk/cadence) - Creates a template function
* [cdc](/build/tools/clients/fcl-js/packages-docs/sdk/cdc) - Creates a template function
* [config](/build/tools/clients/fcl-js/packages-docs/sdk/config) - Sets the config
* [createSdkClient](/build/tools/clients/fcl-js/packages-docs/sdk/createSdkClient) - Creates an SDK client with the provided options.
* [createSignableVoucher](/build/tools/clients/fcl-js/packages-docs/sdk/createSignableVoucher) - Creates a signable voucher object from an interaction for signing purposes. A...
* [decode](/build/tools/clients/fcl-js/packages-docs/sdk/decode) - Decodes the response from 'fcl.send()' into the appropriate JSON representation...
* [destroy](/build/tools/clients/fcl-js/packages-docs/sdk/destroy) - Removes a property from an interaction object using a dot-notation key path.
* [encodeMessageFromSignable](/build/tools/clients/fcl-js/packages-docs/sdk/encodeMessageFromSignable) - Encodes a message from a signable object for a specific signer address. This...
* [encodeTransactionEnvelope](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionEnvelope) - Encodes a complete transaction envelope including payload and signatures. This...
* [encodeTransactionPayload](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTransactionPayload) - Encodes a transaction payload for signing. This function takes a transaction...
* [encodeTxIdFromVoucher](/build/tools/clients/fcl-js/packages-docs/sdk/encodeTxIdFromVoucher) - Encodes a transaction ID from a voucher by computing its hash. A voucher is an...
* [get](/build/tools/clients/fcl-js/packages-docs/sdk/get) - Gets a value from an interaction object using a dot-notation key path.
* [getAccount](/build/tools/clients/fcl-js/packages-docs/sdk/getAccount) - A builder function that returns the interaction to get an account by address....
* [getBlock](/build/tools/clients/fcl-js/packages-docs/sdk/getBlock) - A builder function that returns the interaction to get the latest block. Use...
* [getBlockHeader](/build/tools/clients/fcl-js/packages-docs/sdk/getBlockHeader) - A builder function that returns the interaction to get a block header. A block...
* [getCollection](/build/tools/clients/fcl-js/packages-docs/sdk/getCollection) - A builder function that returns a collection containing a list of transaction...
* [getEvents](/build/tools/clients/fcl-js/packages-docs/sdk/getEvents) - A builder function that returns the interaction to get events. Events are...
* [getEventsAtBlockHeightRange](/build/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockHeightRange) - A builder function that returns all instances of a particular event (by name)...
* [getEventsAtBlockIds](/build/tools/clients/fcl-js/packages-docs/sdk/getEventsAtBlockIds) - A builder function that returns all instances of a particular event (by name)...
* [getNetworkParameters](/build/tools/clients/fcl-js/packages-docs/sdk/getNetworkParameters) - A builder function that returns the interaction to get network parameters....
* [getNodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/sdk/getNodeVersionInfo) - A builder function for the Get Node Version Info interaction. Creates an...
* [getTransaction](/build/tools/clients/fcl-js/packages-docs/sdk/getTransaction) - A builder function that returns the interaction to get a transaction by id....
* [getTransactionStatus](/build/tools/clients/fcl-js/packages-docs/sdk/getTransactionStatus) - A builder function that returns the status of transaction. The transaction id...
* [initInteraction](/build/tools/clients/fcl-js/packages-docs/sdk/initInteraction) - Creates a new interaction object with default values.
* [interaction](/build/tools/clients/fcl-js/packages-docs/sdk/interaction) - Creates a new interaction object with default values.
* [isBad](/build/tools/clients/fcl-js/packages-docs/sdk/isBad) - Checks if an interaction has a failed status.
* [isOk](/build/tools/clients/fcl-js/packages-docs/sdk/isOk) - Checks if an interaction has a successful status.
* [limit](/build/tools/clients/fcl-js/packages-docs/sdk/limit) - A utility builder to set the compute limit on a transaction. The compute limit...
* [nodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/sdk/nodeVersionInfo) - Retrieve version information from the connected Flow Access Node. This function...
* [param](/build/tools/clients/fcl-js/packages-docs/sdk/param) - Legacy function for setting a single parameter on an interaction.
* [params](/build/tools/clients/fcl-js/packages-docs/sdk/params) - Legacy function for setting parameters on an interaction.
* [payer](/build/tools/clients/fcl-js/packages-docs/sdk/payer) - A builder function that adds payer account(s) to a transaction. Every...
* [ping](/build/tools/clients/fcl-js/packages-docs/sdk/ping) - A builder function that creates a ping interaction to test connectivity to the...
* [pipe](/build/tools/clients/fcl-js/packages-docs/sdk/pipe) - Async pipe function to compose interactions. The pipe function is the foundation...
* [proposer](/build/tools/clients/fcl-js/packages-docs/sdk/proposer) - A builder function that adds the proposer to a transaction. The proposer is...
* [put](/build/tools/clients/fcl-js/packages-docs/sdk/put) - Sets a value in an interaction object using a dot-notation key path.
* [ref](/build/tools/clients/fcl-js/packages-docs/sdk/ref) - A builder function that sets the reference block for a transaction. The...
* [resolve](/build/tools/clients/fcl-js/packages-docs/sdk/resolve) - Resolves an interaction by applying a series of resolvers in sequence. This is...
* [resolveAccounts](/build/tools/clients/fcl-js/packages-docs/sdk/resolveAccounts) - Resolves account authorization functions and validates account configurations...
* [resolveArguments](/build/tools/clients/fcl-js/packages-docs/sdk/resolveArguments) - Resolves transaction arguments by evaluating argument functions and converting...
* [resolveCadence](/build/tools/clients/fcl-js/packages-docs/sdk/resolveCadence)
* [resolveFinalNormalization](/build/tools/clients/fcl-js/packages-docs/sdk/resolveFinalNormalization) - Normalizes account addresses by removing the "0x" prefix from all account...
* [resolveProposerSequenceNumber](/build/tools/clients/fcl-js/packages-docs/sdk/resolveProposerSequenceNumber) - Resolves the sequence number for the proposer account by querying the...
* [resolveRefBlockId](/build/tools/clients/fcl-js/packages-docs/sdk/resolveRefBlockId) - Resolves the reference block ID for a transaction by querying the latest block...
* [resolveSignatures](/build/tools/clients/fcl-js/packages-docs/sdk/resolveSignatures) - Resolves signatures for a transaction by coordinating the signing process for...
* [resolveValidators](/build/tools/clients/fcl-js/packages-docs/sdk/resolveValidators) - Executes validator functions that have been attached to an interaction to...
* [resolveVoucherIntercept](/build/tools/clients/fcl-js/packages-docs/sdk/resolveVoucherIntercept) - Resolves voucher intercept functions by calling them with the current voucher.
* [response](/build/tools/clients/fcl-js/packages-docs/sdk/response) - Creates a default response object
* [script](/build/tools/clients/fcl-js/packages-docs/sdk/script) - A builder function that creates a script interaction. Scripts allow you to write...
* [send](/build/tools/clients/fcl-js/packages-docs/sdk/send) - Sends arbitrary scripts, transactions, and requests to Flow. This method...
* [subscribe](/build/tools/clients/fcl-js/packages-docs/sdk/subscribe) - Subscribe to real-time data from the Flow blockchain and automatically decode...
* [subscribeEvents](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeEvents) - Subscribe to events with the given filter and parameters. Creates a subscription...
* [subscribeRaw](/build/tools/clients/fcl-js/packages-docs/sdk/subscribeRaw) - Subscribe to a topic without decoding the data. This function creates a raw...
* [TestUtils](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils) (namespace) - Namespace containing TestUtils utilities
* [TestUtils.authzDeepResolveMany](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#authzDeepResolveMany) - Creates a deep test authorization resolver with nested resolution for complex...
* [TestUtils.authzFn](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#authzFn) - Creates a test authorization function for testing transactions.
* [TestUtils.authzResolve](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#authzResolve) - Creates a test authorization resolver that can be used for testing account...
* [TestUtils.authzResolveMany](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#authzResolveMany) - Creates a test authorization resolver that handles multiple accounts with...
* [TestUtils.idof](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#idof) - Generates a unique identifier for an account based on its address and key ID.
* [TestUtils.run](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#run) - Runs a set of functions on an interaction This is a utility function for testing...
* [TestUtils.sig](/build/tools/clients/fcl-js/packages-docs/sdk/testUtils#sig) - Generates a test signature string for an account.
* [transaction](/build/tools/clients/fcl-js/packages-docs/sdk/transaction) - A template builder to use a Cadence transaction for an interaction. FCL "mutate"...
* [update](/build/tools/clients/fcl-js/packages-docs/sdk/update) - Updates a value in an interaction object using a transformation function.
* [validator](/build/tools/clients/fcl-js/packages-docs/sdk/validator) - A builder function that adds a validator to a transaction. Validators are...
* [voucherIntercept](/build/tools/clients/fcl-js/packages-docs/sdk/voucherIntercept) - A builder function that intercepts and modifies a voucher. This function is...
* [voucherToTxId](/build/tools/clients/fcl-js/packages-docs/sdk/voucherToTxId) - Converts a voucher object to a transaction ID. This function computes the...
* [why](/build/tools/clients/fcl-js/packages-docs/sdk/why) - Returns the reason for an interaction failure.

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/sdk/index.md)

Last updated on **Nov 18, 2025** by **Brian Doyle**

[Previous

withPrefix](/build/tools/clients/fcl-js/packages-docs/fcl/withPrefix)[Next

account](/build/tools/clients/fcl-js/packages-docs/sdk/account)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Installation](#installation)
    + [Requirements](#requirements)+ [Importing](#importing)* [Connect](#connect)* [Querying the Flow Network](#querying-the-flow-network)* [Mutate Flow Network](#mutate-flow-network)* [Transactions](#transactions)* [API Reference](#api-reference)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.