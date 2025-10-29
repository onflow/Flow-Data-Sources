# Source: https://developers.flow.com/build/tools/clients/fcl-js/packages-docs/fcl/createFlowClient

createFlowClient | Flow Developer Portal



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

                              * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)* [WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Packages Docs](/build/tools/clients/fcl-js/packages-docs)* [@onflow/fcl](/build/tools/clients/fcl-js/packages-docs/fcl)* createFlowClient

On this page

# createFlowClient

Creates a Flow client instance with authentication, transaction, and query capabilities.

## Import[​](#import "Direct link to Import")

You can import the entire package and access the function:

`_10

import * as fcl from "@onflow/fcl"

_10

_10

fcl.createFlowClient(params)`

Or import directly the specific function:

`_10

import { createFlowClient } from "@onflow/fcl"

_10

_10

createFlowClient(params)`

## Parameters[​](#parameters "Direct link to Parameters")

### `params`[​](#params "Direct link to params")

* Type:

`_21

export interface FlowClientConfig {

_21

accessNodeUrl: string

_21

flowNetwork?: string

_21

flowJson?: any

_21

discoveryWallet?: string

_21

discoveryWalletMethod?: string

_21

discoveryAuthnEndpoint?: string

_21

discoveryAuthnInclude?: string[]

_21

walletconnectProjectId?: string

_21

walletconnectDisableNotifications?: boolean

_21

storage?: StorageProvider

_21

appDetailTitle?: string

_21

appDetailIcon?: string

_21

appDetailDescription?: string

_21

appDetailUrl?: string

_21

serviceOpenIdScopes?: string[]

_21

transport?: SdkTransport

_21

computeLimit?: number

_21

customResolver?: any

_21

customDecoders?: any

_21

}`

* Description: Configuration object for the Flow client

## Returns[​](#returns "Direct link to Returns")

`_56

{

_56

send: (args?: false | InteractionBuilderFn | (false | InteractionBuilderFn)[], opts?: any) => Promise<any>;

_56

subscribe: <T extends SubscriptionTopic>({

_56

topic, args, onData, onError

_56

}: SubscribeParams<T>, opts?: {

_56

node?: string;

_56

transport?: SdkTransport;

_56

}) => Subscription;

_56

subscribeRaw: <T extends SubscriptionTopic>({

_56

topic, args, onData, onError

_56

}: SubscribeRawParams<T>, opts?: {

_56

node?: string;

_56

transport?: SdkTransport;

_56

}) => {

_56

unsubscribe: () => void;

_56

};

_56

account: (address: string, {

_56

height, id, isSealed

_56

}?: AccountQueryOptions, opts?: object) => Promise<Account>;

_56

block: ({

_56

sealed, id, height

_56

}?: BlockQueryOptions, opts?: object) => Promise<Block>;

_56

resolve: (ix: Interaction) => Promise<Interaction>;

_56

decode: (response: any) => Promise<any>;

_56

currentUser: CurrentUserServiceApi;

_56

mutate: (opts?: MutateOptions) => Promise<string>;

_56

query: (opts?: QueryOptions) => Promise<any>;

_56

queryRaw: (opts?: QueryOptions) => Promise<any>;

_56

verifyUserSignatures: (message: string, compSigs: CompositeSignature[], opts?: VerifySignaturesScriptOptions) => Promise<boolean>;

_56

getChainId: (opts?: GetChainIdOptions) => Promise<string>;

_56

tx: {

_56

(transactionId: string, opts?: {

_56

pollRate?: number;

_56

txNotFoundTimeout?: number;

_56

}): {

_56

snapshot: () => Promise<TransactionStatus>;

_56

subscribe: (onData: (txStatus: TransactionStatus) => void, onError?: (err: Error) => void) => () => void;

_56

onceFinalized: () => Promise<TransactionStatus>;

_56

onceExecuted: () => Promise<TransactionStatus>;

_56

onceSealed: () => Promise<TransactionStatus>;

_56

};

_56

isUnknown: (ix: Interaction) => boolean;

_56

isPending: (tx: TransactionStatus) => boolean;

_56

isFinalized: (tx: TransactionStatus) => boolean;

_56

isExecuted: (tx: TransactionStatus) => boolean;

_56

isSealed: (tx: TransactionStatus) => boolean;

_56

isExpired: (tx: TransactionStatus) => boolean;

_56

};

_56

events: (filterOrType?: string | EventFilter) => {

_56

subscribe: (onData: (event: Event) => void, onError?: (error: Error) => void) => () => void;

_56

};

_56

authenticate: (opts?: AuthenticationOptions) => Promise<CurrentUser>;

_56

unauthenticate: () => void;

_56

signUserMessage: (msg: string) => Promise<CompositeSignature[]>;

_56

serialize: (args: (false | InteractionBuilderFn)[] | Interaction, opts?: SerializeOptions) => Promise<string>;

_56

}`

A Flow client object with many methods for interacting with the Flow blockchain

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/packages-docs/fcl/createFlowClient.md)

Last updated on **Oct 22, 2025** by **Michael Fabozzi**

[Previous

config](/build/tools/clients/fcl-js/packages-docs/fcl/config)[Next

createSignableVoucher](/build/tools/clients/fcl-js/packages-docs/fcl/createSignableVoucher)

###### Rate this page

😞😐😊

Copy as Markdown

* [Import](#import)* [Parameters](#parameters)
    + [`params`](#params)* [Returns](#returns)

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