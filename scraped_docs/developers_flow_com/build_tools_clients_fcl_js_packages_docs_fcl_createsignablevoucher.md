# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/fcl/createSignableVoucher

createSignableVoucher | Flow Developer Portal



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

                          - [account](/build/tools/clients/fcl-js/packages-docs/fcl/account)- [arg](/build/tools/clients/fcl-js/packages-docs/fcl/arg)- [args](/build/tools/clients/fcl-js/packages-docs/fcl/args)- [atBlockHeight](/build/tools/clients/fcl-js/packages-docs/fcl/atBlockHeight)- [atBlockId](/build/tools/clients/fcl-js/packages-docs/fcl/atBlockId)- [authenticate](/build/tools/clients/fcl-js/packages-docs/fcl/authenticate)- [authorization](/build/tools/clients/fcl-js/packages-docs/fcl/authorization)- [authorizations](/build/tools/clients/fcl-js/packages-docs/fcl/authorizations)- [authz](/build/tools/clients/fcl-js/packages-docs/fcl/authz)- [block](/build/tools/clients/fcl-js/packages-docs/fcl/block)- [build](/build/tools/clients/fcl-js/packages-docs/fcl/build)- [cadence](/build/tools/clients/fcl-js/packages-docs/fcl/cadence)- [cdc](/build/tools/clients/fcl-js/packages-docs/fcl/cdc)- [config](/build/tools/clients/fcl-js/packages-docs/fcl/config)- [createFlowClient](/build/tools/clients/fcl-js/packages-docs/fcl/createFlowClient)- [createSignableVoucher](/build/tools/clients/fcl-js/packages-docs/fcl/createSignableVoucher)- [currentUser](/build/tools/clients/fcl-js/packages-docs/fcl/currentUser)- [decode](/build/tools/clients/fcl-js/packages-docs/fcl/decode)- [display](/build/tools/clients/fcl-js/packages-docs/fcl/display)- [events](/build/tools/clients/fcl-js/packages-docs/fcl/events)- [getAccount](/build/tools/clients/fcl-js/packages-docs/fcl/getAccount)- [getBlock](/build/tools/clients/fcl-js/packages-docs/fcl/getBlock)- [getBlockHeader](/build/tools/clients/fcl-js/packages-docs/fcl/getBlockHeader)- [getCollection](/build/tools/clients/fcl-js/packages-docs/fcl/getCollection)- [getEvents](/build/tools/clients/fcl-js/packages-docs/fcl/getEvents)- [getEventsAtBlockHeightRange](/build/tools/clients/fcl-js/packages-docs/fcl/getEventsAtBlockHeightRange)- [getEventsAtBlockIds](/build/tools/clients/fcl-js/packages-docs/fcl/getEventsAtBlockIds)- [getNetworkParameters](/build/tools/clients/fcl-js/packages-docs/fcl/getNetworkParameters)- [getNodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/fcl/getNodeVersionInfo)- [getTransaction](/build/tools/clients/fcl-js/packages-docs/fcl/getTransaction)- [getTransactionStatus](/build/tools/clients/fcl-js/packages-docs/fcl/getTransactionStatus)- [invariant](/build/tools/clients/fcl-js/packages-docs/fcl/invariant)- [isBad](/build/tools/clients/fcl-js/packages-docs/fcl/isBad)- [isOk](/build/tools/clients/fcl-js/packages-docs/fcl/isOk)- [limit](/build/tools/clients/fcl-js/packages-docs/fcl/limit)- [logIn](/build/tools/clients/fcl-js/packages-docs/fcl/logIn)- [mutate](/build/tools/clients/fcl-js/packages-docs/fcl/mutate)- [nodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/fcl/nodeVersionInfo)- [param](/build/tools/clients/fcl-js/packages-docs/fcl/param)- [params](/build/tools/clients/fcl-js/packages-docs/fcl/params)- [payer](/build/tools/clients/fcl-js/packages-docs/fcl/payer)- [ping](/build/tools/clients/fcl-js/packages-docs/fcl/ping)- [pipe](/build/tools/clients/fcl-js/packages-docs/fcl/pipe)- [pluginRegistry](/build/tools/clients/fcl-js/packages-docs/fcl/pluginRegistry)- [proposer](/build/tools/clients/fcl-js/packages-docs/fcl/proposer)- [query](/build/tools/clients/fcl-js/packages-docs/fcl/query)- [queryRaw](/build/tools/clients/fcl-js/packages-docs/fcl/queryRaw)- [reauthenticate](/build/tools/clients/fcl-js/packages-docs/fcl/reauthenticate)- [ref](/build/tools/clients/fcl-js/packages-docs/fcl/ref)- [sansPrefix](/build/tools/clients/fcl-js/packages-docs/fcl/sansPrefix)- [script](/build/tools/clients/fcl-js/packages-docs/fcl/script)- [send](/build/tools/clients/fcl-js/packages-docs/fcl/send)- [serialize](/build/tools/clients/fcl-js/packages-docs/fcl/serialize)- [signUp](/build/tools/clients/fcl-js/packages-docs/fcl/signUp)- [subscribe](/build/tools/clients/fcl-js/packages-docs/fcl/subscribe)- [subscribeEvents](/build/tools/clients/fcl-js/packages-docs/fcl/subscribeEvents)- [subscribeRaw](/build/tools/clients/fcl-js/packages-docs/fcl/subscribeRaw)- [transaction](/build/tools/clients/fcl-js/packages-docs/fcl/transaction)- [tx](/build/tools/clients/fcl-js/packages-docs/fcl/tx)- [unauthenticate](/build/tools/clients/fcl-js/packages-docs/fcl/unauthenticate)- [validator](/build/tools/clients/fcl-js/packages-docs/fcl/validator)- [verifyUserSignatures](/build/tools/clients/fcl-js/packages-docs/fcl/verifyUserSignatures)- [voucherIntercept](/build/tools/clients/fcl-js/packages-docs/fcl/voucherIntercept)- [voucherToTxId](/build/tools/clients/fcl-js/packages-docs/fcl/voucherToTxId)- [why](/build/tools/clients/fcl-js/packages-docs/fcl/why)- [withPrefix](/build/tools/clients/fcl-js/packages-docs/fcl/withPrefix)+ [@onflow/sdk](/build/tools/clients/fcl-js/packages-docs/sdk)

                            + [Type Definitions](/build/tools/clients/fcl-js/packages-docs/types)* [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Packages Docs](/build/tools/clients/fcl-js/packages-docs)* [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)* createSignableVoucher

On this page

# createSignableVoucher

Creates a signable voucher object from an interaction for signing purposes.

A voucher is a standardized representation of a transaction that contains all the necessary
information for signing and submitting to the Flow network. This function transforms an
interaction object into a voucher format.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as fcl from "@onflow/fcl"

_10

_10

fcl.createSignableVoucher(ix)`

Or import directly the specific function:

`_10

import { createSignableVoucher } from "@onflow/fcl"

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

* Type: [`Interaction`](/build/tools/clients/fcl-js/packages-docs/types#interaction)
* Description: The interaction object containing transaction details

## Returns[​](#returns "Direct link to Returns")

`_19

{

_19

cadence: string;

_19

refBlock: string;

_19

computeLimit: number;

_19

arguments: any[];

_19

proposalKey: {

_19

address: string;

_19

keyId: string | number;

_19

sequenceNum: number;

_19

} | {

_19

address?: undefined;

_19

keyId?: undefined;

_19

sequenceNum?: undefined;

_19

};

_19

payer: string;

_19

authorizers: string[];

_19

payloadSigs: any[];

_19

envelopeSigs: any[];

_19

}`

A voucher object containing all transaction data and signatures

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/fcl/createSignableVoucher.md)

Last updated on **Oct 22, 2025** by **Michael Fabozzi**

[Previous

createFlowClient](/build/tools/clients/fcl-js/packages-docs/fcl/createFlowClient)[Next

currentUser](/build/tools/clients/fcl-js/packages-docs/fcl/currentUser)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)* [Usage](#usage)* [Parameters](#parameters)
      + [`ix`](#ix)* [Returns](#returns)

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