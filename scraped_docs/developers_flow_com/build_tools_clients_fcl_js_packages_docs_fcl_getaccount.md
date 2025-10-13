# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/fcl/getAccount

getAccount | Flow Developer Portal



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

        + [@onflow/react-sdk](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                        + [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)

                          - [account](/build/tools/clients/fcl-js/packages-docs/fcl/account)- [arg](/build/tools/clients/fcl-js/packages-docs/fcl/arg)- [args](/build/tools/clients/fcl-js/packages-docs/fcl/args)- [atBlockHeight](/build/tools/clients/fcl-js/packages-docs/fcl/atBlockHeight)- [atBlockId](/build/tools/clients/fcl-js/packages-docs/fcl/atBlockId)- [authenticate](/build/tools/clients/fcl-js/packages-docs/fcl/authenticate)- [authorization](/build/tools/clients/fcl-js/packages-docs/fcl/authorization)- [authorizations](/build/tools/clients/fcl-js/packages-docs/fcl/authorizations)- [authz](/build/tools/clients/fcl-js/packages-docs/fcl/authz)- [block](/build/tools/clients/fcl-js/packages-docs/fcl/block)- [build](/build/tools/clients/fcl-js/packages-docs/fcl/build)- [cadence](/build/tools/clients/fcl-js/packages-docs/fcl/cadence)- [cdc](/build/tools/clients/fcl-js/packages-docs/fcl/cdc)- [config](/build/tools/clients/fcl-js/packages-docs/fcl/config)- [createFcl](/build/tools/clients/fcl-js/packages-docs/fcl/createFcl)- [createSignableVoucher](/build/tools/clients/fcl-js/packages-docs/fcl/createSignableVoucher)- [currentUser](/build/tools/clients/fcl-js/packages-docs/fcl/currentUser)- [decode](/build/tools/clients/fcl-js/packages-docs/fcl/decode)- [display](/build/tools/clients/fcl-js/packages-docs/fcl/display)- [events](/build/tools/clients/fcl-js/packages-docs/fcl/events)- [getAccount](/build/tools/clients/fcl-js/packages-docs/fcl/getAccount)- [getBlock](/build/tools/clients/fcl-js/packages-docs/fcl/getBlock)- [getBlockHeader](/build/tools/clients/fcl-js/packages-docs/fcl/getBlockHeader)- [getChainId](/build/tools/clients/fcl-js/packages-docs/fcl/getChainId)- [getCollection](/build/tools/clients/fcl-js/packages-docs/fcl/getCollection)- [getEvents](/build/tools/clients/fcl-js/packages-docs/fcl/getEvents)- [getEventsAtBlockHeightRange](/build/tools/clients/fcl-js/packages-docs/fcl/getEventsAtBlockHeightRange)- [getEventsAtBlockIds](/build/tools/clients/fcl-js/packages-docs/fcl/getEventsAtBlockIds)- [getNetworkParameters](/build/tools/clients/fcl-js/packages-docs/fcl/getNetworkParameters)- [getNodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/fcl/getNodeVersionInfo)- [getTransaction](/build/tools/clients/fcl-js/packages-docs/fcl/getTransaction)- [getTransactionStatus](/build/tools/clients/fcl-js/packages-docs/fcl/getTransactionStatus)- [invariant](/build/tools/clients/fcl-js/packages-docs/fcl/invariant)- [isBad](/build/tools/clients/fcl-js/packages-docs/fcl/isBad)- [isOk](/build/tools/clients/fcl-js/packages-docs/fcl/isOk)- [limit](/build/tools/clients/fcl-js/packages-docs/fcl/limit)- [logIn](/build/tools/clients/fcl-js/packages-docs/fcl/logIn)- [mutate](/build/tools/clients/fcl-js/packages-docs/fcl/mutate)- [nodeVersionInfo](/build/tools/clients/fcl-js/packages-docs/fcl/nodeVersionInfo)- [param](/build/tools/clients/fcl-js/packages-docs/fcl/param)- [params](/build/tools/clients/fcl-js/packages-docs/fcl/params)- [payer](/build/tools/clients/fcl-js/packages-docs/fcl/payer)- [ping](/build/tools/clients/fcl-js/packages-docs/fcl/ping)- [pipe](/build/tools/clients/fcl-js/packages-docs/fcl/pipe)- [pluginRegistry](/build/tools/clients/fcl-js/packages-docs/fcl/pluginRegistry)- [proposer](/build/tools/clients/fcl-js/packages-docs/fcl/proposer)- [query](/build/tools/clients/fcl-js/packages-docs/fcl/query)- [queryRaw](/build/tools/clients/fcl-js/packages-docs/fcl/queryRaw)- [reauthenticate](/build/tools/clients/fcl-js/packages-docs/fcl/reauthenticate)- [ref](/build/tools/clients/fcl-js/packages-docs/fcl/ref)- [sansPrefix](/build/tools/clients/fcl-js/packages-docs/fcl/sansPrefix)- [script](/build/tools/clients/fcl-js/packages-docs/fcl/script)- [send](/build/tools/clients/fcl-js/packages-docs/fcl/send)- [serialize](/build/tools/clients/fcl-js/packages-docs/fcl/serialize)- [signUp](/build/tools/clients/fcl-js/packages-docs/fcl/signUp)- [subscribe](/build/tools/clients/fcl-js/packages-docs/fcl/subscribe)- [subscribeEvents](/build/tools/clients/fcl-js/packages-docs/fcl/subscribeEvents)- [subscribeRaw](/build/tools/clients/fcl-js/packages-docs/fcl/subscribeRaw)- [transaction](/build/tools/clients/fcl-js/packages-docs/fcl/transaction)- [tx](/build/tools/clients/fcl-js/packages-docs/fcl/tx)- [unauthenticate](/build/tools/clients/fcl-js/packages-docs/fcl/unauthenticate)- [validator](/build/tools/clients/fcl-js/packages-docs/fcl/validator)- [verifyUserSignatures](/build/tools/clients/fcl-js/packages-docs/fcl/verifyUserSignatures)- [voucherIntercept](/build/tools/clients/fcl-js/packages-docs/fcl/voucherIntercept)- [voucherToTxId](/build/tools/clients/fcl-js/packages-docs/fcl/voucherToTxId)- [why](/build/tools/clients/fcl-js/packages-docs/fcl/why)- [withPrefix](/build/tools/clients/fcl-js/packages-docs/fcl/withPrefix)+ [@onflow/sdk](/build/tools/clients/fcl-js/packages-docs/sdk)

                            + [Type Definitions](/build/tools/clients/fcl-js/packages-docs/types)* [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)* [WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Packages Docs](/build/tools/clients/fcl-js/packages-docs)* [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)* getAccount

On this page

# getAccount

A builder function that returns the interaction to get an account by address.

Consider using the pre-built interaction 'fcl.account(address)' if you do not need to pair with any other builders.

Account address is a unique account identifier. Be mindful about the '0x' prefix, you should use the prefix as a default representation but be careful and safely handle user inputs without the prefix.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.getAccount(addr);`

Or import directly the specific function:

`_10

import { getAccount } from '@onflow/fcl';

_10

_10

getAccount(addr);`

## Usage[​](#usage "Direct link to Usage")

`_10

import * as fcl from '@onflow/fcl';

_10

_10

// somewhere in an async function

_10

// fcl.account is the same as this function

_10

const getAccount = async (address) => {

_10

const account = await fcl.send([fcl.getAccount(address)]).then(fcl.decode);

_10

return account;

_10

};`

## Parameters[​](#parameters "Direct link to Parameters")

### `addr`[​](#addr "Direct link to addr")

* Type: `string`

## Returns[​](#returns "Direct link to Returns")

`_10

export type InteractionBuilderFn = (

_10

ix: Interaction,

_10

) => Interaction | Promise<Interaction>;`

A function that processes an interaction object

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/fcl/getAccount.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

events](/build/tools/clients/fcl-js/packages-docs/fcl/events)[Next

getBlock](/build/tools/clients/fcl-js/packages-docs/fcl/getBlock)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)* [Usage](#usage)* [Parameters](#parameters)
      + [`addr`](#addr)* [Returns](#returns)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.