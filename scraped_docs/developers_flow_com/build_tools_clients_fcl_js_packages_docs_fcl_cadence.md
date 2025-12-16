# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/fcl/cadence

cadence | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Packages Docs](/build/tools/clients/fcl-js/packages-docs)* [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)* cadence

On this page

# cadence

Creates a template function

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as fcl from "@onflow/fcl"

_10

_10

fcl.cadence(head, rest)`

Or import directly the specific function:

`_10

import { cadence } from "@onflow/fcl"

_10

_10

cadence(head, rest)`

## Usage[​](#usage "Direct link to Usage")

`` _30

import { template } from "@onflow/util-template"

_30

_30

// String template

_30

const simpleTemplate = template("Hello, World!");

_30

console.log(simpleTemplate()); // "Hello, World!"

_30

_30

// Template literal with interpolation

_30

const name = "Alice";

_30

const greeting = template`Hello, ${name}!`;

_30

console.log(greeting()); // "Hello, Alice!"

_30

_30

// Cadence script template

_30

const cadenceScript = template`

_30

access(all) fun main(greeting: String): String {

_30

return greeting.concat(", from Flow!")

_30

}

_30

`;

_30

console.log(cadenceScript()); // The Cadence script as a string

_30

_30

// Used with FCL for dynamic Cadence code

_30

import * as fcl from "@onflow/fcl";

_30

_30

const contractAddress = "0x123456789abcdef0";

_30

const scriptTemplate = fcl.cadence`

_30

import MyContract from ${contractAddress}

_30

_30

access(all) fun main(): String {

_30

return MyContract.getMessage()

_30

}

_30

`; ``

## Parameters[​](#parameters "Direct link to Parameters")

### `head`[​](#head "Direct link to head")

* Type:

`_10

string | TemplateStringsArray | ((x?: unknown) => string)`

* Description: - A string, template string array, or template function

### `rest` (optional)[​](#rest-optional "Direct link to rest-optional")

* Type: `unknown[]`
* Description: - The rest of the arguments

## Returns[​](#returns "Direct link to Returns")

`string`

A template function

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/fcl/cadence.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

build](/build/tools/clients/fcl-js/packages-docs/fcl/build)[Next

cdc](/build/tools/clients/fcl-js/packages-docs/fcl/cdc)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)* [Usage](#usage)* [Parameters](#parameters)
      + [`head`](#head)+ [`rest` (optional)](#rest-optional)* [Returns](#returns)

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