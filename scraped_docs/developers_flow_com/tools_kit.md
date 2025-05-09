# Source: https://developers.flow.com/tools/kit

@onflow/kit | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* @onflow/kit

On this page

# @onflow/kit

`@onflow/kit` is a lightweight React utility library that simplifies interacting with the Flow blockchain. It provides a collection of hooks, similar to those in other popular web3 libraries, that make it easier to build frontends that understand blockchain interactions. **In the future**, it will also provide components designed to make authentication, script execution, transactions, event subscriptions, and network configuration seamless in React apps.

## 🔌 Included React Hooks[​](#-included-react-hooks "Direct link to 🔌 Included React Hooks")

* [`useCurrentFlowUser`](#usecurrentflowuser) – Authenticate and manage the current Flow user
* [`useFlowAccount`](#useflowaccount) – Fetch Flow account details by address
* [`useFlowBlock`](#useflowblock) – Query latest or specific Flow blocks
* [`useFlowConfig`](#useflowconfig) – Access the current Flow configuration
* [`useFlowEvents`](#useflowevents) – Subscribe to Flow events in real-time
* [`useFlowQuery`](#useflowquery) – Execute Cadence scripts with optional arguments
* [`useFlowMutate`](#useflowmutate) – Send transactions to the Flow blockchain
* [`useFlowRevertibleRandom`](#useflowrevertiblerandom) – Generate pseudorandom values tied to block height
* [`useFlowTransaction`](#useflowtransaction) – Track transaction status updates

## Installation[​](#installation "Direct link to Installation")

`_10

npm install @onflow/kit`

## Usage[​](#usage "Direct link to Usage")

### Wrapping Your App With `FlowProvider`[​](#wrapping-your-app-with-flowprovider "Direct link to wrapping-your-app-with-flowprovider")

Begin by wrapping your application with the `FlowProvider` to initialize FCL configuration. This sets up FCL and maps its configuration keys to a strictly typed format for your hooks.

`_24

import React from "react"

_24

import App from "./App"

_24

import { FlowProvider } from "@onflow/kit"

_24

import flowJSON from "../flow.json"

_24

_24

function Root() {

_24

return (

_24

<FlowProvider

_24

config={{

_24

accessNodeUrl: "https://access-mainnet.onflow.org",

_24

flowNetwork: "mainnet",

_24

appDetailTitle: "My On Chain App",

_24

appDetailIcon: "https://example.com/icon.png",

_24

appDetailDescription: "A decentralized app on Flow",

_24

appDetailUrl: "https://myonchainapp.com",

_24

}}

_24

flowJson={flowJSON}

_24

>

_24

<App />

_24

</FlowProvider>

_24

)

_24

}

_24

_24

export default Root`

If you're using Next.js, put this in `layout.tsx`. Adapt as appropriate for other frontend frameworks.

👉 Learn more about configuring `flow.json` in the [Configuration Guide](/tools/flow-cli/flow.json/configuration).

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
* `query?: UseQueryOptions<Account | null, Error>` – Optional TanStackQuery options

#### Returns: `UseQueryResult<Account | null, Error>`[​](#returns-usequeryresultaccount--null-error "Direct link to returns-usequeryresultaccount--null-error")

`_19

function AccountDetails() {

_19

const { data: account, isLoading, error, refetch } = useFlowAccount({

_19

address: "0x1cf0e2f2f715450",

_19

query: { staleTime: 5000 },

_19

})

_19

_19

if (isLoading) return <p>Loading account...</p>

_19

if (error) return <p>Error fetching account: {error.message}</p>

_19

if (!account) return <p>No account data</p>

_19

_19

return (

_19

<div>

_19

<h2>Account: {account.address}</h2>

_19

<p>Balance: {account.balance}</p>

_19

<pre>{account.code}</pre>

_19

<button onClick={refetch}>Refetch</button>

_19

</div>

_19

)

_19

}`

---

### `useFlowBlock`[​](#useflowblock "Direct link to useflowblock")

`_10

import { useFlowBlock } from "@onflow/kit"`

#### Parameters:[​](#parameters-1 "Direct link to Parameters:")

* `sealed?: boolean` – If `true`, fetch latest sealed block
* `id?: string` – Block by ID
* `height?: number` – Block by height
* `query?: UseQueryOptions<Block | null, Error>` – Optional TanStackQuery options

Only one of `sealed`, `id`, or `height` should be provided.

#### Returns: `UseQueryResult<Block | null, Error>`[​](#returns-usequeryresultblock--null-error "Direct link to returns-usequeryresultblock--null-error")

`_14

function LatestBlock() {

_14

const { data: block, isLoading, error } = useFlowBlock({ query: { staleTime: 10000 } })

_14

_14

if (isLoading) return <p>Loading...</p>

_14

if (error) return <p>Error: {error.message}</p>

_14

if (!block) return <p>No block data.</p>

_14

_14

return (

_14

<div>

_14

<h2>Block {block.height}</h2>

_14

<p>ID: {block.id}</p>

_14

</div>

_14

)

_14

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

#### Parameters:[​](#parameters-2 "Direct link to Parameters:")

* `startBlockId?: string` – Optional ID of the block to start listening from
* `startHeight?: number` – Optional block height to start listening from
* `eventTypes?: string[]` – Array of event type strings (e.g., `A.0xDeaDBeef.Contract.EventName`)
* `addresses?: string[]` – Filter by Flow addresses
* `contracts?: string[]` – Filter by contract identifiers
* `opts?: { heartbeatInterval?: number }` – Options for subscription heartbeat
* `onEvent: (event: Event) => void` – Callback for each event received
* `onError?: (error: Error) => void` – Optional error handler

#### Example:[​](#example "Direct link to Example:")

`_10

function EventListener() {

_10

useFlowEvents({

_10

eventTypes: ["A.0xDeaDBeef.SomeContract.SomeEvent"],

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

#### Parameters:[​](#parameters-3 "Direct link to Parameters:")

* `cadence: string` – Cadence script to run
* `args?: (arg, t) => unknown[]` – Function returning FCL arguments
* `query?: UseQueryOptions<unknown, Error>` – Optional TanStackQuery options

#### Returns: `UseQueryResult<unknown, Error>`[​](#returns-usequeryresultunknown-error "Direct link to returns-usequeryresultunknown-error")

`_22

function QueryExample() {

_22

const { data, isLoading, error, refetch } = useFlowQuery({

_22

cadence: `

_22

access(all)

_22

fun main(a: Int, b: Int): Int {

_22

return a + b

_22

}

_22

`,

_22

args: (arg, t) => [arg(1, t.Int), arg(2, t.Int)],

_22

query: { staleTime: 10000 },

_22

})

_22

_22

if (isLoading) return <p>Loading query...</p>

_22

if (error) return <p>Error: {error.message}</p>

_22

_22

return (

_22

<div>

_22

<p>Result: {data}</p>

_22

<button onClick={refetch}>Refetch</button>

_22

</div>

_22

)

_22

}`

---

### `useFlowMutate`[​](#useflowmutate "Direct link to useflowmutate")

`_10

import { useFlowMutate } from "@onflow/kit"`

#### Parameters:[​](#parameters-4 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, FCLMutateParams>` – Optional TanStackQuery mutation options

#### Returns: `UseMutationResult<string, Error, FCLMutateParams>`[​](#returns-usemutationresultstring-error-fclmutateparams "Direct link to returns-usemutationresultstring-error-fclmutateparams")

`_33

function CreatePage() {

_33

const { mutate, isPending, error, data: txId } = useFlowMutate({

_33

mutation: {

_33

onSuccess: (txId) => console.log("TX ID:", txId),

_33

},

_33

})

_33

_33

const sendTransaction = () => {

_33

mutate({

_33

cadence: `transaction() {

_33

prepare(acct: &Account) {

_33

log(acct.address)

_33

}

_33

}`,

_33

args: (arg, t) => [],

_33

proposer: fcl.currentUser,

_33

payer: fcl.currentUser,

_33

authorizations: [],

_33

limit: 100,

_33

})

_33

}

_33

_33

return (

_33

<div>

_33

<button onClick={sendTransaction} disabled={isPending}>

_33

Send Transaction

_33

</button>

_33

{isPending && <p>Sending transaction...</p>}

_33

{error && <p>Error: {error.message}</p>}

_33

{txId && <p>Transaction ID: {txId}</p>}

_33

</div>

_33

)

_33

}`

---

### `useFlowRevertibleRandom`[​](#useflowrevertiblerandom "Direct link to useflowrevertiblerandom")

`_10

import { useFlowRevertibleRandom } from "@onflow/kit"`

#### Parameters:[​](#parameters-5 "Direct link to Parameters:")

* `min?: string` – Minimum random value (inclusive), as a UInt256 decimal string. Defaults to `"0"`.
* `max: string` – Maximum random value (inclusive), as a UInt256 decimal string. **Required**.
* `count?: number` – Number of random values to fetch (must be at least 1). Defaults to `1`.
* `query?: Omit<UseQueryOptions<any, Error>, "queryKey" | "queryFn">` – Optional TanStack Query settings like `staleTime`, `enabled`, `retry`, etc.

#### Returns: `UseQueryResult<RevertibleRandomResult[], Error>`[​](#returns-usequeryresultrevertiblerandomresult-error "Direct link to returns-usequeryresultrevertiblerandomresult-error")

Each `RevertibleRandomResult` includes:

* `blockHeight: string` — The block height from which the random value was generated.
* `value: string` — The random UInt256 value, returned as a decimal string.

`_26

function RandomValues() {

_26

const { data: randoms, isLoading, error, refetch } = useFlowRevertibleRandom({

_26

min: "0",

_26

max: "1000000000000000000000000", // Example large max

_26

count: 3,

_26

query: { staleTime: 10000 },

_26

})

_26

_26

if (isLoading) return <p>Loading random numbers...</p>

_26

if (error) return <p>Error fetching random numbers: {error.message}</p>

_26

if (!randoms) return <p>No random values generated.</p>

_26

_26

return (

_26

<div>

_26

<h2>Generated Random Numbers</h2>

_26

<ul>

_26

{randoms.map((rand, idx) => (

_26

<li key={idx}>

_26

Block {rand.blockHeight}: {rand.value}

_26

</li>

_26

))}

_26

</ul>

_26

<button onClick={refetch}>Regenerate</button>

_26

</div>

_26

)

_26

}`

#### Notes:[​](#notes "Direct link to Notes:")

* Randomness is generated using Flow’s **on-chain `revertibleRandom`**, producing pseudorandom values tied to block and transaction execution.
* The value returned for identical calls within the same block will be identical.
* This hook is intended for **non-critical randomness** like randomized UIs, loot crates, and temporary rewards.
* For **critical applications** requiring secure and unpredictable randomness, use a [commit-reveal scheme](/build/advanced-concepts/randomness#commit-reveal-scheme) on Flow instead.
* Values are **deterministic**: if a transaction fails and retries, the same random value will be regenerated.

---

### `useFlowTransaction`[​](#useflowtransaction "Direct link to useflowtransaction")

`_10

import { useFlowTransaction } from "@onflow/kit"`

#### Parameters:[​](#parameters-6 "Direct link to Parameters:")

* `id: string` – Transaction ID to subscribe to

#### Returns:[​](#returns-1 "Direct link to Returns:")

* `transactionStatus: TransactionStatus | null`
* `error: Error | null`

`_12

function TransactionComponent() {

_12

const txId = "your-transaction-id-here"

_12

const { transactionStatus, error } = useFlowTransaction({ id: txId })

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

Last updated on **May 8, 2025** by **Chase Fleming**

[Next

Flow Emulator](/tools/emulator)

###### Rate this page

😞😐😊

Copy as Markdown

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
  + [`useFlowRevertibleRandom`](#useflowrevertiblerandom)
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
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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