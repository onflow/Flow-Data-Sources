# Source: https://developers.flow.com/tools/kit

@onflow/kit | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* @onflow/kit

On this page

# @onflow/kit

warning

🚧 This library is currently in alpha and is subject to change.

`@onflow/kit` is a lightweight React utility library that simplifies interacting with the Flow blockchain. It provides a collection of hooks, similar to those in other popular web3 libraries, that make it easier to build frontends that understand blockchain interactions. **In the future**, it will also provided components designed to make authentication, script execution, transactions, event subscriptions, and network configuration seamless in React apps.

## 🔌 Included React Hooks[​](#-included-react-hooks "Direct link to 🔌 Included React Hooks")

* [`useCurrentFlowUser`](#usecurrentflowuser) – Authenticate and manage the current Flow user
* [`useFlowAccount`](#useflowaccount) – Fetch Flow account details by address
* [`useFlowBlock`](#useflowblock) – Query latest or specific Flow blocks
* [`useFlowConfig`](#useflowconfig) – Access the current Flow configuration
* [`useFlowEvents`](#useflowevents) – Subscribe to Flow events in real-time
* [`useFlowQuery`](#useflowquery) – Execute Cadence scripts with optional arguments
* [`useFlowMutate`](#useflowmutate) – Send transactions to the Flow blockchain
* [`useFlowTransaction`](#useflowtransaction) – Track transaction status updates

## Installation[​](#installation "Direct link to Installation")

`_10

npm install @onflow/kit`

## Usage[​](#usage "Direct link to Usage")

### Wrapping Your App With `FlowProvider`[​](#wrapping-your-app-with-flowprovider "Direct link to wrapping-your-app-with-flowprovider")

Begin by wrapping your application with the `FlowProvider` to initialize FCL configuration. This sets up FCL and maps its configuration keys to a strictly typed format for your hooks.

`_25

import React from "react"

_25

import App from "./App"

_25

import { FlowProvider } from "@onflow/kit"

_25

import flowJSON from "../flow.json"

_25

_25

function Root() {

_25

return (

_25

<FlowProvider

_25

config={{

_25

accessNodeUrl: "https://access-mainnet.onflow.org",

_25

flowNetwork: "mainnet",

_25

appDetailTitle: "My On Chain App",

_25

appDetailIcon: "https://example.com/icon.png",

_25

appDetailDescription: "A decentralized app on Flow",

_25

appDetailUrl: "https://myonchainapp.com",

_25

// include other typed configuration keys as needed...

_25

}}

_25

flowJson={flowJSON}

_25

>

_25

<App />

_25

</FlowProvider>

_25

)

_25

}

_25

_25

export default Root`

If you're using [Next.js], put this in `layout.tsx`. Adapt as appropriate for other frontend frameworks.

---

## Hooks[​](#hooks "Direct link to Hooks")

info

Many of these hooks are built using [`@tanstack/react-query`](https://tanstack.com/query/latest), which provides powerful caching, revalidation, and background refetching features. As a result, you’ll see return types like `UseQueryResult` and `UseMutationResult` throughout this section. Other types—such as `Account`, `Block`, and `CurrentUser`—are from the [Flow Client Library (FCL) TypeDefs](https://github.com/onflow/fcl-js/blob/master/packages/typedefs/src/index.ts). Refer to their respective documentation for full type definitions and usage patterns.

### `useCurrentFlowUser`[​](#usecurrentflowuser "Direct link to usecurrentflowuser")

`_10

import { useCurrentFlowUser } from "@onflow/kit"`

#### Returns:[​](#returns "Direct link to Returns:")

* `user: CurrentUser` – The current user object from FCL
* `authenticate: () => Promise<CurrentUser>` – Triggers wallet authentication
* `unauthenticate: () => void` – Logs the user out

`_16

function AuthComponent() {

_16

const { user, authenticate, unauthenticate } = useCurrentFlowUser()

_16

_16

return (

_16

<div>

_16

{user.loggedIn ? (

_16

<>

_16

<p>Logged in as {user.addr}</p>

_16

<button onClick={unauthenticate}>Logout</button>

_16

</>

_16

) : (

_16

<button onClick={authenticate}>Login</button>

_16

)}

_16

</div>

_16

)

_16

}`

---

### `useFlowAccount`[​](#useflowaccount "Direct link to useflowaccount")

`_10

import { useFlowAccount } from "@onflow/kit"`

#### Parameters:[​](#parameters "Direct link to Parameters:")

* `address?: string` – Flow address (with or without `0x` prefix)

#### Returns: `UseQueryResult<Account | null, Error>`[​](#returns-usequeryresultaccount--null-error "Direct link to returns-usequeryresultaccount--null-error")

`_16

function AccountDetails() {

_16

const { data: account, isLoading, error, refetch } = useFlowAccount("0x1cf0e2f2f715450")

_16

_16

if (isLoading) return <p>Loading account...</p>

_16

if (error) return <p>Error fetching account: {error.message}</p>

_16

if (!account) return <p>No account data</p>

_16

_16

return (

_16

<div>

_16

<h2>Account: {account.address}</h2>

_16

<p>Balance: {account.balance}</p>

_16

<pre>{account.code}</pre>

_16

<button onClick={refetch}>Refetch</button>

_16

</div>

_16

)

_16

}`

---

### `useFlowBlock`[​](#useflowblock "Direct link to useflowblock")

`_10

import { useFlowBlock } from "@onflow/kit"`

#### Parameters (mutually exclusive):[​](#parameters-mutually-exclusive "Direct link to Parameters (mutually exclusive):")

* `{}` – Latest block (default)
* `{ sealed: true }` – Latest sealed block
* `{ id: string }` – Block by ID
* `{ height: number }` – Block by height

#### Returns: `UseQueryResult<Block | null, Error>`[​](#returns-usequeryresultblock--null-error "Direct link to returns-usequeryresultblock--null-error")

`_13

function LatestBlock() {

_13

const { data: block, isLoading, error } = useFlowBlock()

_13

if (isLoading) return <p>Loading...</p>

_13

if (error) return <p>Error: {error.message}</p>

_13

if (!block) return <p>No block data.</p>

_13

_13

return (

_13

<div>

_13

<h2>Block {block.height}</h2>

_13

<p>ID: {block.id}</p>

_13

</div>

_13

)

_13

}`

---

### `useFlowConfig`[​](#useflowconfig "Direct link to useflowconfig")

`_10

import { useFlowConfig } from "@onflow/kit"`

#### Returns: `FlowConfig`[​](#returns-flowconfig "Direct link to returns-flowconfig")

`_10

function MyComponent() {

_10

const config = useFlowConfig()

_10

_10

return (

_10

<div>

_10

<p>Current network: {config.flowNetwork}</p>

_10

<p>Current access node: {config.accessNodeUrl}</p>

_10

</div>

_10

)

_10

}`

---

### `useFlowEvents`[​](#useflowevents "Direct link to useflowevents")

`_10

import { useFlowEvents } from "@onflow/kit"`

#### Parameters:[​](#parameters-1 "Direct link to Parameters:")

* `eventNameOrFilter`: string | EventFilter
* `options: { onEvent: (event) => void, onError?: (error) => void }`

#### Example:[​](#example "Direct link to Example:")

`_10

function EventListener() {

_10

useFlowEvents("A.0xDeaDBeef.SomeContract.SomeEvent", {

_10

onEvent: (event) => console.log("New event:", event),

_10

onError: (error) => console.error("Error:", error),

_10

})

_10

_10

return <div>Listening for events...</div>

_10

}`

---

### `useFlowQuery`[​](#useflowquery "Direct link to useflowquery")

`_10

import { useFlowQuery } from "@onflow/kit"`

#### Parameters:[​](#parameters-2 "Direct link to Parameters:")

* `cadence: string` – Cadence script to run
* `args?: (arg, t) => unknown[]` – Function returning FCL arguments
* `enabled?: boolean` – Defaults to `true`

#### Returns: `UseQueryResult<unknown, Error>`[​](#returns-usequeryresultunknown-error "Direct link to returns-usequeryresultunknown-error")

`_20

function QueryExample() {

_20

const { data, isLoading, error, refetch } = useFlowQuery({

_20

cadence: `

_20

pub fun main(a: Int, b: Int): Int {

_20

return a + b

_20

}

_20

`,

_20

args: (arg, t) => [arg(1, t.Int), arg(2, t.Int)],

_20

})

_20

_20

if (isLoading) return <p>Loading query...</p>

_20

if (error) return <p>Error: {error.message}</p>

_20

_20

return (

_20

<div>

_20

<p>Result: {data}</p>

_20

<button onClick={refetch}>Refetch</button>

_20

</div>

_20

)

_20

}`

---

### `useFlowMutate`[​](#useflowmutate "Direct link to useflowmutate")

`_10

import { useFlowMutate } from "@onflow/kit"`

#### Returns: `UseMutationResult<string, Error, FCLMutateParams>`[​](#returns-usemutationresultstring-error-fclmutateparams "Direct link to returns-usemutationresultstring-error-fclmutateparams")

* `mutate`: A function to send the transaction
* `data`: Transaction ID
* `error`: Any error
* `isPending`: Boolean status

`_29

function CreatePage() {

_29

const { mutate, isPending, error, data: txId } = useFlowMutate()

_29

_29

const sendTransaction = () => {

_29

mutate({

_29

cadence: `transaction() {

_29

prepare(acct: &Account) {

_29

log(acct.address)

_29

}

_29

}`,

_29

args: (arg, t) => [],

_29

proposer: fcl.currentUser,

_29

payer: fcl.currentUser,

_29

authorizations: [],

_29

limit: 100,

_29

})

_29

}

_29

_29

return (

_29

<div>

_29

<button onClick={sendTransaction} disabled={isPending}>

_29

Send Transaction

_29

</button>

_29

{isPending && <p>Sending transaction...</p>}

_29

{error && <p>Error: {error.message}</p>}

_29

{txId && <p>Transaction ID: {txId}</p>}

_29

</div>

_29

)

_29

}`

---

### `useFlowTransaction`[​](#useflowtransaction "Direct link to useflowtransaction")

`_10

import { useFlowTransaction } from "@onflow/kit"`

#### Parameters:[​](#parameters-3 "Direct link to Parameters:")

* `txId: string` – Transaction ID to subscribe to

#### Returns:[​](#returns-1 "Direct link to Returns:")

* `transactionStatus: TransactionStatus | null`
* `error: Error | null`

`_12

function TransactionComponent() {

_12

const txId = "your-transaction-id-here"

_12

const { transactionStatus, error } = useFlowTransaction(txId)

_12

_12

if (error) return <div>Error: {error.message}</div>

_12

_12

return (

_12

<div>

_12

Status: {transactionStatus?.statusString}

_12

</div>

_12

)

_12

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/kit/index.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

Data Collection](/tools/flow-cli/data-collection)[Next

Flow Emulator](/tools/emulator)

###### Rate this page

😞😐😊

* [🔌 Included React Hooks](#-included-react-hooks)
* [Installation](#installation)
* [Usage](#usage)
  + [Wrapping Your App With `FlowProvider`](#wrapping-your-app-with-flowprovider)
* [Hooks](#hooks)
  + [`useCurrentFlowUser`](#usecurrentflowuser)
  + [`useFlowAccount`](#useflowaccount)
  + [`useFlowBlock`](#useflowblock)
  + [`useFlowConfig`](#useflowconfig)
  + [`useFlowEvents`](#useflowevents)
  + [`useFlowQuery`](#useflowquery)
  + [`useFlowMutate`](#useflowmutate)
  + [`useFlowTransaction`](#useflowtransaction)

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
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.