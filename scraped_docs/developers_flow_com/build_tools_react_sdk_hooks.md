# Source: https://developers.flow.com/build/tools/react-sdk/hooks

Hooks | Flow Developer Portal



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

          - [Hooks](/build/tools/react-sdk/hooks)- [Components](/build/tools/react-sdk/components)+ [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow React SDK](/build/tools/react-sdk)* Hooks

On this page

# React SDK Hooks

info

Many of these hooks are built using [`@tanstack/react-query`](https://tanstack.com/query/latest), which provides powerful caching, revalidation, and background refetching features. As a result, you'll see return types like `UseQueryResult` and `UseMutationResult` throughout this section. Other types—such as `Account`, `Block`, and `CurrentUser`—are from the [Flow Client Library (FCL) TypeDefs](https://github.com/onflow/fcl-js/blob/master/packages/typedefs/src/index.ts). Refer to their respective documentation for full type definitions and usage patterns.

## Cadence Hooks[​](#cadence-hooks "Direct link to Cadence Hooks")

### `useFlowCurrentUser`[​](#useflowcurrentuser "Direct link to useflowcurrentuser")

[Open in Playground →](https://react.flow.com/#useflowcurrentuser)

`_10

import { useFlowCurrentUser } from "@onflow/react-sdk"`

#### Parameters[​](#parameters "Direct link to Parameters")

* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns:[​](#returns "Direct link to Returns:")

* `user: CurrentUser` – The current user object from FCL
* `authenticate: () => Promise<CurrentUser>` – Triggers wallet authentication
* `unauthenticate: () => void` – Logs the user out

`_16

function AuthComponent() {

_16

const { user, authenticate, unauthenticate } = useFlowCurrentUser()

_16

_16

return (

_16

<div>

_16

{user?.loggedIn ? (

_16

<>

_16

<p>Logged in as {user?.addr}</p>

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

[Open in Playground →](https://react.flow.com/#useflowaccount)

`_10

import { useFlowAccount } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-1 "Direct link to Parameters:")

* `address?: string` – Flow address (with or without `0x` prefix)
* `query?: UseQueryOptions<Account | null, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

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

[Open in Playground →](https://react.flow.com/#useflowblock)

`_10

import { useFlowBlock } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-2 "Direct link to Parameters:")

* `sealed?: boolean` – If `true`, fetch latest sealed block
* `id?: string` – Block by ID
* `height?: number` – Block by height
* `query?: UseQueryOptions<Block | null, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

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

### `useFlowChainId`[​](#useflowchainid "Direct link to useflowchainid")

[Open in Playground →](https://react.flow.com/#useflowchainid)

`_10

import { useFlowChainId } from "@onflow/react-sdk"`

This hook retrieves the Flow chain ID, which is useful for identifying the current network.

#### Parameters:[​](#parameters-3 "Direct link to Parameters:")

* `query?: Omit<UseQueryOptions<string | null>, "queryKey" | "queryFn">` – Optional TanStack Query options like `staleTime`, `enabled`, etc.
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<string | null, Error>`[​](#returns-usequeryresultstring--null-error "Direct link to returns-usequeryresultstring--null-error")

Valid chain IDs include: `testnet` (Flow Testnet), `mainnet` (Flow Mainnet), and `emulator` (Flow Emulator). The `flow-` prefix will be stripped from the chain ID returned by the access node (e.g. `flow-testnet` will return `testnet`).

`_10

function ChainIdExample() {

_10

const { data: chainId, isLoading, error } = useFlowChainId({

_10

query: { staleTime: 10000 },

_10

})

_10

_10

if (isLoading) return <p>Loading chain ID...</p>

_10

if (error) return <p>Error fetching chain ID: {error.message}</p>

_10

_10

return <div>Current Flow Chain ID: {chainId}</div>

_10

}`

---

### `useFlowClient`[​](#useflowclient "Direct link to useflowclient")

[Open in Playground →](https://react.flow.com/#useflowclient)

This hook returns the `FlowClient` for the current `<FlowProvider />` context.

#### Parameters:[​](#parameters-4 "Direct link to Parameters:")

* `flowClient?: FlowClient` - Optional `FlowClient` instance to override the result

---

### `useFlowConfig`[​](#useflowconfig "Direct link to useflowconfig")

[Open in Playground →](https://react.flow.com/#useflowconfig)

`_10

import { useFlowConfig } from "@onflow/react-sdk"`

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

[Open in Playground →](https://react.flow.com/#useflowevents)

`_10

import { useFlowEvents } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-5 "Direct link to Parameters:")

* `startBlockId?: string` – Optional ID of the block to start listening from
* `startHeight?: number` – Optional block height to start listening from
* `eventTypes?: string[]` – Array of event type strings (e.g., `A.0xDeaDBeef.Contract.EventName`)
* `addresses?: string[]` – Filter by Flow addresses
* `contracts?: string[]` – Filter by contract identifiers
* `opts?: { heartbeatInterval?: number }` – Options for subscription heartbeat
* `onEvent: (event: Event) => void` – Callback for each event received
* `onError?: (error: Error) => void` – Optional error handler
* `flowClient?: FlowClient` - Optional `FlowClient` instance

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

[Open in Playground →](https://react.flow.com/#useflowquery)

`_10

import { useFlowQuery } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-6 "Direct link to Parameters:")

* `cadence: string` – Cadence script to run
* `args?: (arg, t) => unknown[]` – Function returning FCL arguments
* `query?: UseQueryOptions<unknown, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<unknown, Error>`[​](#returns-usequeryresultunknown-error "Direct link to returns-usequeryresultunknown-error")

`` _22

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

} ``

---

### `useFlowQueryRaw`[​](#useflowqueryraw "Direct link to useflowqueryraw")

[Open in Playground →](https://react.flow.com/#useflowqueryraw)

`_10

import { useFlowQueryRaw } from "@onflow/react-sdk"`

This hook is identical to `useFlowQuery` but returns the raw, non-decoded response data from the Flow blockchain. This is useful when you need access to the original response structure or want to handle decoding manually.

#### Parameters:[​](#parameters-7 "Direct link to Parameters:")

* `cadence: string` – Cadence script to run
* `args?: (arg, t) => unknown[]` – Function returning FCL arguments
* `query?: UseQueryOptions<unknown, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<unknown, Error>`[​](#returns-usequeryresultunknown-error-1 "Direct link to returns-usequeryresultunknown-error-1")

The returned data will be in its raw, non-decoded format as received from the Flow access node.

`` _22

function QueryRawExample() {

_22

const { data: rawData, isLoading, error, refetch } = useFlowQueryRaw({

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

<p>Raw Result: {JSON.stringify(rawData, null, 2)}</p>

_22

<button onClick={refetch}>Refetch</button>

_22

</div>

_22

)

_22

} ``

---

### `useFlowMutate`[​](#useflowmutate "Direct link to useflowmutate")

[Open in Playground →](https://react.flow.com/#useflowmutate)

`_10

import { useFlowMutate } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-8 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, FCLMutateParams>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseMutationResult<string, Error, FCLMutateParams>`[​](#returns-usemutationresultstring-error-fclmutateparams "Direct link to returns-usemutationresultstring-error-fclmutateparams")

`` _33

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

} ``

---

### `useFlowRevertibleRandom`[​](#useflowrevertiblerandom "Direct link to useflowrevertiblerandom")

[Open in Playground →](https://react.flow.com/#useflowrevertiblerandom)

`_10

import { useFlowRevertibleRandom } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-9 "Direct link to Parameters:")

* `min?: string` – Minimum random value (inclusive), as a UInt256 decimal string. Defaults to `"0"`.
* `max: string` – Maximum random value (inclusive), as a UInt256 decimal string. **Required**.
* `count?: number` – Number of random values to fetch (must be at least 1). Defaults to `1`.
* `query?: Omit<UseQueryOptions<any, Error>, "queryKey" | "queryFn">` – Optional TanStack Query settings like `staleTime`, `enabled`, `retry`, etc.
* `flowClient?: FlowClient` - Optional `FlowClient` instance

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

* Randomness is generated using the **onchain `revertibleRandom`** function on Flow, producing pseudorandom values tied to block and script execution.
* Values are **deterministic**: The values returned for identical calls within the same block will be identical.
* If `count`  is larger than one, the returned values are distinct.
* This hook is designed for simple use cases that don't require unpredictability, such as randomized UIs.
  Since the hook uses script executions on existing blocks, the random source is already public and the randoms are predictable.
* For **more advanced use cases** that **do** require onchain randomness logic via transactions, Flow provides built-in support using Cadence's `revertibleRandom` and [commit-reveal scheme](/build/cadence/advanced-concepts/randomness#commit-reveal-scheme).

---

### `useFlowTransaction`[​](#useflowtransaction "Direct link to useflowtransaction")

[Open in Playground →](https://react.flow.com/#useflowtransaction)

`_10

import { useFlowTransaction } from "@onflow/react-sdk"`

Fetches a Flow transaction by ID and returns the decoded transaction object.

#### Parameters:[​](#parameters-10 "Direct link to Parameters:")

* `txId?: string` – The Flow transaction ID to fetch.
* `query?: Omit<UseQueryOptions<Transaction | null, Error>, "queryKey" | "queryFn">` – Optional TanStack Query options like `staleTime`, `enabled`, etc.
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<Transaction | null, Error>`[​](#returns-usequeryresulttransaction--null-error "Direct link to returns-usequeryresulttransaction--null-error")

`_19

function TransactionDetails({ txId }: { txId: string }) {

_19

const { data: transaction, isLoading, error, refetch } = useFlowTransaction({

_19

txId,

_19

query: { staleTime: 10000 },

_19

})

_19

_19

if (isLoading) return <p>Loading transaction...</p>

_19

if (error) return <p>Error fetching transaction: {error.message}</p>

_19

if (!transaction) return <p>No transaction data.</p>

_19

_19

return (

_19

<div>

_19

<h2>Transaction ID: {transaction.id}</h2>

_19

<p>Gas Limit: {transaction.gasLimit}</p>

_19

<pre>Arguments: {JSON.stringify(transaction.arguments, null, 2)}</pre>

_19

<button onClick={refetch}>Refetch</button>

_19

</div>

_19

)

_19

}`

---

### `useFlowTransactionStatus`[​](#useflowtransactionstatus "Direct link to useflowtransactionstatus")

[Open in Playground →](https://react.flow.com/#useflowtransactionstatus)

`_10

import { useFlowTransactionStatus } from "@onflow/react-sdk"`

#### Parameters:[​](#parameters-11 "Direct link to Parameters:")

* `id: string` – Transaction ID to subscribe to
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns:[​](#returns-1 "Direct link to Returns:")

* `transactionStatus: TransactionStatus | null`
* `error: Error | null`

`_10

function TransactionStatusComponent() {

_10

const txId = "your-transaction-id-here"

_10

const { transactionStatus, error } = useFlowTransactionStatus({ id: txId })

_10

_10

if (error) return <div>Error: {error.message}</div>;

_10

_10

return <div>Status: {transactionStatus?.statusString}</div>;

_10

}`

---

### `useDarkMode`[​](#usedarkmode "Direct link to usedarkmode")

[Open in Playground →](https://react.flow.com/#usedarkmode)

`_10

import { useDarkMode } from "@onflow/react-sdk"`

This hook provides access to the current dark mode state from the `FlowProvider`. It's useful for conditionally rendering content or applying custom styling based on the current theme.

#### Returns:[​](#returns-2 "Direct link to Returns:")

* `isDark: boolean` – Whether dark mode is currently enabled

`_10

function ThemeAwareComponent() {

_10

const { isDark } = useDarkMode()

_10

_10

return (

_10

<div className={isDark ? "bg-gray-900 text-white" : "bg-white text-black"}>

_10

<h2>Current Theme: {isDark ? "Dark" : "Light"}</h2>

_10

<p>This component adapts to the current theme!</p>

_10

</div>

_10

)

_10

}`

---

### `useFlowNftMetadata`[​](#useflownftmetadata "Direct link to useflownftmetadata")

[Open in Playground →](https://react.flow.com/#useflownftmetadata)

`_10

import { useFlowNftMetadata } from "@onflow/react-sdk"`

This hook fetches NFT metadata including display information, traits, rarity, and collection details.

#### Parameters:[​](#parameters-12 "Direct link to Parameters:")

* `accountAddress?: string` – Flow address of the account holding the NFT
* `tokenId?: string | number` – The NFT token ID
* `publicPathIdentifier?: string` – Public path identifier for the collection
* `query?: UseQueryOptions<unknown, Error>` – Optional TanStack Query options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<NftViewResult | null, Error>`[​](#returns-usequeryresultnftviewresult--null-error "Direct link to returns-usequeryresultnftviewresult--null-error")

Where `NftViewResult` is defined as:

`_12

interface NftViewResult {

_12

name: string

_12

description: string

_12

thumbnailUrl: string

_12

externalUrl?: string

_12

collectionName?: string

_12

collectionExternalUrl?: string

_12

tokenID: string

_12

traits?: Record<string, string>

_12

rarity?: string

_12

serialNumber?: string

_12

}`

`_32

function NftMetadataExample() {

_32

const { data: nft, isLoading, error } = useFlowNftMetadata({

_32

accountAddress: "0x1cf0e2f2f715450",

_32

tokenId: "123",

_32

publicPathIdentifier: "exampleNFTCollection",

_32

query: { staleTime: 60000 },

_32

})

_32

_32

if (isLoading) return <p>Loading NFT metadata...</p>

_32

if (error) return <p>Error: {error.message}</p>

_32

if (!nft) return <p>NFT not found</p>

_32

_32

return (

_32

<div>

_32

<h2>{nft.name}</h2>

_32

<img src={nft.thumbnailUrl} alt={nft.name} />

_32

<p>{nft.description}</p>

_32

{nft.collectionName && <p>Collection: {nft.collectionName}</p>}

_32

{nft.rarity && <p>Rarity: {nft.rarity}</p>}

_32

{nft.traits && (

_32

<div>

_32

<h3>Traits:</h3>

_32

<ul>

_32

{Object.entries(nft.traits).map(([key, value]) => (

_32

<li key={key}>{key}: {value}</li>

_32

))}

_32

</ul>

_32

</div>

_32

)}

_32

</div>

_32

)

_32

}`

---

### `useFlowAuthz`[​](#useflowauthz "Direct link to useflowauthz")

`_10

import { useFlowAuthz } from "@onflow/react-sdk"`

A React hook that returns an authorization function for Flow transactions. If no custom authorization is provided, it returns the current user's wallet authorization.

#### Parameters:[​](#parameters-13 "Direct link to Parameters:")

* `authz?: AuthorizationFunction` – Optional custom authorization function
* `flowClient?: FlowClient` - Optional `FlowClient` instance

Where `AuthorizationFunction` is defined as:

`_10

type AuthorizationFunction = (

_10

account: Partial<InteractionAccount>

_10

) => Partial<InteractionAccount> | Promise<Partial<InteractionAccount>>`

#### Returns: `AuthorizationFunction`[​](#returns-authorizationfunction "Direct link to returns-authorizationfunction")

The authorization function is compatible with Flow transactions' authorizations parameter.

`` _21

// Example 1: Using current user authorization

_21

function CurrentUserAuthExample() {

_21

const authorization = useFlowAuthz()

_21

_21

const sendTransaction = async () => {

_21

const txId = await fcl.mutate({

_21

cadence: `

_21

transaction {

_21

prepare(signer: auth(Storage) &Account) {

_21

log(signer.address)

_21

}

_21

}

_21

`,

_21

authorizations: [authorization],

_21

limit: 100,

_21

})

_21

console.log("Transaction ID:", txId)

_21

}

_21

_21

return <button onClick={sendTransaction}>Send Transaction</button>

_21

} ``

`` _30

// Example 2: Using custom authorization function

_30

function CustomAuthExample() {

_30

const customAuthz = (account) => ({

_30

...account,

_30

addr: "0xCUSTOMOADDRESS",

_30

keyId: 0,

_30

signingFunction: async (signable) => ({

_30

signature: "0x...",

_30

}),

_30

})

_30

_30

const authorization = useFlowAuthz({ authz: customAuthz })

_30

_30

const sendTransaction = async () => {

_30

const txId = await fcl.mutate({

_30

cadence: `

_30

transaction {

_30

prepare(signer: auth(Storage) &Account) {

_30

log(signer.address)

_30

}

_30

}

_30

`,

_30

authorizations: [authorization],

_30

limit: 100,

_30

})

_30

console.log("Transaction ID:", txId)

_30

}

_30

_30

return <button onClick={sendTransaction}>Send Custom Auth Transaction</button>

_30

} ``

---

### `useFlowScheduledTransaction`[​](#useflowscheduledtransaction "Direct link to useflowscheduledtransaction")

[Open in Playground →](https://react.flow.com/#useflowscheduledtransaction)

`_10

import { useFlowScheduledTransaction } from "@onflow/react-sdk"`

Fetches a scheduled transaction by ID.

#### Parameters:[​](#parameters-14 "Direct link to Parameters:")

* `txId?: string` – Scheduled transaction ID
* `includeHandlerData?: boolean` – Include handler data (default: false)
* `query?: UseQueryOptions<ScheduledTransaction | null, Error>` – Optional TanStack Query options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<ScheduledTransaction | null, Error>`[​](#returns-usequeryresultscheduledtransaction--null-error "Direct link to returns-usequeryresultscheduledtransaction--null-error")

Where `ScheduledTransaction` is defined as:

`_15

interface ScheduledTransaction {

_15

id: string

_15

priority: ScheduledTransactionPriority // 0 = Low, 1 = Medium, 2 = High

_15

executionEffort: bigint

_15

status: ScheduledTransactionStatus // 0 = Pending, 1 = Processing, 2 = Completed, 3 = Failed, 4 = Cancelled

_15

fees: {

_15

value: bigint

_15

formatted: string

_15

}

_15

scheduledTimestamp: number

_15

handlerTypeIdentifier: string

_15

handlerAddress: string

_15

handlerUUID?: string // Only included if includeHandlerData is true

_15

handlerResolvedViews?: {[viewType: string]: any} // Only included if includeHandlerData is true

_15

}`

`_20

function ScheduledTransactionDetails({ txId }: { txId: string }) {

_20

const { data: transaction, isLoading, error } = useFlowScheduledTransaction({

_20

txId,

_20

query: { staleTime: 10000 },

_20

})

_20

_20

if (isLoading) return <p>Loading scheduled transaction...</p>

_20

if (error) return <p>Error: {error.message}</p>

_20

if (!transaction) return <p>Transaction not found</p>

_20

_20

return (

_20

<div>

_20

<h2>Scheduled Transaction #{transaction.id}</h2>

_20

<p>Status: {transaction.status}</p>

_20

<p>Priority: {transaction.priority}</p>

_20

<p>Fees: {transaction.fees.formatted} FLOW</p>

_20

<p>Handler: {transaction.handlerTypeIdentifier}</p>

_20

</div>

_20

)

_20

}`

---

### `useFlowScheduledTransactionList`[​](#useflowscheduledtransactionlist "Direct link to useflowscheduledtransactionlist")

[Open in Playground →](https://react.flow.com/#useflowscheduledtransaction)

`_10

import { useFlowScheduledTransactionList } from "@onflow/react-sdk"`

Lists all scheduled transactions for an account.

#### Parameters:[​](#parameters-15 "Direct link to Parameters:")

* `account?: string` – Flow address to query
* `includeHandlerData?: boolean` – Include handler data (default: false)
* `query?: UseQueryOptions<ScheduledTransaction[], Error>` – Optional TanStack Query options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<ScheduledTransaction[], Error>`[​](#returns-usequeryresultscheduledtransaction-error "Direct link to returns-usequeryresultscheduledtransaction-error")

`_24

function ScheduledTransactionsList({ account }: { account: string }) {

_24

const { data: transactions, isLoading, error, refetch } = useFlowScheduledTransactionList({

_24

account,

_24

query: { staleTime: 10000 },

_24

})

_24

_24

if (isLoading) return <p>Loading scheduled transactions...</p>

_24

if (error) return <p>Error: {error.message}</p>

_24

if (!transactions || transactions.length === 0) return <p>No scheduled transactions</p>

_24

_24

return (

_24

<div>

_24

<h2>Scheduled Transactions for {account}</h2>

_24

<button onClick={() => refetch()}>Refresh</button>

_24

<ul>

_24

{transactions.map((tx) => (

_24

<li key={tx.id}>

_24

Transaction #{tx.id} - Status: {tx.status} - Fees: {tx.fees.formatted} FLOW

_24

</li>

_24

))}

_24

</ul>

_24

</div>

_24

)

_24

}`

---

### `useFlowScheduledTransactionCancel`[​](#useflowscheduledtransactioncancel "Direct link to useflowscheduledtransactioncancel")

[Open in Playground →](https://react.flow.com/#useflowscheduledtransaction)

`_10

import { useFlowScheduledTransactionCancel } from "@onflow/react-sdk"`

Cancels a scheduled transaction and refunds fees.

#### Parameters:[​](#parameters-16 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, string>` – Optional TanStack Query mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseFlowScheduledTransactionCancelResult`[​](#returns-useflowscheduledtransactioncancelresult "Direct link to returns-useflowscheduledtransactioncancelresult")

Where `UseFlowScheduledTransactionCancelResult` is defined as:

`_10

interface UseFlowScheduledTransactionCancelResult extends Omit<

_10

UseMutationResult<string, Error>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

cancelTransaction: (txId: string) => void

_10

cancelTransactionAsync: (txId: string) => Promise<string>

_10

}`

`_27

function CancelScheduledTransaction() {

_27

const { cancelTransactionAsync, isPending, error, data: txId } = useFlowScheduledTransactionCancel({

_27

mutation: {

_27

onSuccess: (txId) => console.log("Cancel transaction ID:", txId),

_27

},

_27

})

_27

_27

const handleCancel = async (scheduledTxId: string) => {

_27

try {

_27

const resultTxId = await cancelTransactionAsync(scheduledTxId)

_27

console.log("Successfully canceled scheduled transaction:", resultTxId)

_27

} catch (error) {

_27

console.error("Failed to cancel:", error)

_27

}

_27

}

_27

_27

return (

_27

<div>

_27

<button onClick={() => handleCancel("42")} disabled={isPending}>

_27

Cancel Scheduled Transaction #42

_27

</button>

_27

{isPending && <p>Canceling transaction...</p>}

_27

{error && <p>Error: {error.message}</p>}

_27

{txId && <p>Cancel Transaction ID: {txId}</p>}

_27

</div>

_27

)

_27

}`

---

### `useFlowScheduledTransactionSetup`[​](#useflowscheduledtransactionsetup "Direct link to useflowscheduledtransactionsetup")

[Open in Playground →](https://react.flow.com/#useflowscheduledtransaction)

`_10

import { useFlowScheduledTransactionSetup } from "@onflow/react-sdk"`

Sets up the Transaction Scheduler Manager resource.

#### Parameters:[​](#parameters-17 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, void>` – Optional TanStack Query mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseFlowScheduledTransactionSetupResult`[​](#returns-useflowscheduledtransactionsetupresult "Direct link to returns-useflowscheduledtransactionsetupresult")

Where `UseFlowScheduledTransactionSetupResult` is defined as:

`_10

interface UseFlowScheduledTransactionSetupResult extends Omit<

_10

UseMutationResult<string, Error>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

setup: () => void

_10

setupAsync: () => Promise<string>

_10

}`

`_27

function SchedulerSetup() {

_27

const { setupAsync, isPending, error, data: txId } = useFlowScheduledTransactionSetup({

_27

mutation: {

_27

onSuccess: (txId) => console.log("Setup transaction ID:", txId),

_27

},

_27

})

_27

_27

const handleSetup = async () => {

_27

try {

_27

const resultTxId = await setupAsync()

_27

console.log("Scheduler setup successful:", resultTxId)

_27

} catch (error) {

_27

console.error("Setup failed:", error)

_27

}

_27

}

_27

_27

return (

_27

<div>

_27

<button onClick={handleSetup} disabled={isPending}>

_27

Setup Transaction Scheduler

_27

</button>

_27

{isPending && <p>Setting up scheduler...</p>}

_27

{error && <p>Error: {error.message}</p>}

_27

{txId && <p>Setup Transaction ID: {txId}</p>}

_27

</div>

_27

)

_27

}`

---

## Cross-VM Hooks[​](#cross-vm-hooks "Direct link to Cross-VM Hooks")

### `useCrossVmBatchTransaction`[​](#usecrossvmbatchtransaction "Direct link to usecrossvmbatchtransaction")

[Open in Playground →](https://react.flow.com/#usecrossvmbatchtransaction)

`_10

import { useCrossVmBatchTransaction } from "@onflow/react-sdk"`

This hook allows you to execute multiple EVM transactions in a single atomic Cadence transaction. It is useful for batch processing EVM calls while ensuring they are executed together, either all succeeding or allowing for some to fail without affecting the others.

#### Parameters:[​](#parameters-18 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmBatchTransactionMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseCrossVmBatchTransactionResult`[​](#returns-usecrossvmbatchtransactionresult "Direct link to returns-usecrossvmbatchtransactionresult")

Where `UseCrossVmBatchTransactionResult` is defined as:

`_10

interface UseCrossVmBatchTransactionResult extends Omit<

_10

UseMutationResult<string, Error, UseCrossVmBatchTransactionMutateArgs>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

mutate: (calls: UseCrossVmBatchTransactionMutateArgs) => void

_10

mutateAsync: (calls: UseCrossVmBatchTransactionMutateArgs) => Promise<string>

_10

}`

Where `UseCrossVmBatchTransactionMutateArgs` is defined as:

`_10

interface UseCrossVmBatchTransactionMutateArgs {

_10

calls: EvmBatchCall[]

_10

mustPass?: boolean

_10

}`

Where `EvmBatchCall` is defined as:

`_14

interface EvmBatchCall {

_14

// The target EVM contract address (as a string)

_14

address: string

_14

// The contract ABI fragment

_14

abi: Abi

_14

// The name of the function to call

_14

functionName: string

_14

// The function arguments

_14

args?: readonly unknown[]

_14

// The gas limit for the call

_14

gasLimit?: bigint

_14

// The value to send with the call

_14

value?: bigint

_14

}`

`_35

function CrossVmBatchTransactionExample() {

_35

const { sendBatchTransaction, isPending, error, data: txId } = useCrossVmBatchTransaction({

_35

mutation: {

_35

onSuccess: (txId) => console.log("TX ID:", txId),

_35

},

_35

})

_35

_35

const sendTransaction = () => {

_35

const calls = [

_35

{

_35

address: "0x1234567890abcdef",

_35

abi: {

_35

// ABI definition for the contract

_35

},

_35

functionName: "transfer",

_35

args: ["0xabcdef1234567890", 100n], // Example arguments

_35

gasLimit: 21000n, // Example gas limit

_35

},

_35

// Add more calls as needed

_35

]

_35

_35

sendBatchTransaction({calls})

_35

}

_35

_35

return (

_35

<div>

_35

<button onClick={sendTransaction} disabled={isPending}>

_35

Send Cross-VM Transaction

_35

</button>

_35

{isPending && <p>Sending transaction...</p>}

_35

{error && <p>Error: {error.message}</p>}

_35

{txId && <p>Transaction ID: {txId}</p>}

_35

</div>

_35

)

_35

}`

---

### `useCrossVmTokenBalance`[​](#usecrossvmtokenbalance "Direct link to usecrossvmtokenbalance")

[Open in Playground →](https://react.flow.com/#usecrossvmtokenbalance)

`_10

import { useCrossVmTokenBalance } from "@onflow/react-sdk"`

Fetch the balance of a token balance for a given user across both Cadence and EVM environments.

#### Parameters:[​](#parameters-19 "Direct link to Parameters:")

* `owner: string` – Cadence address of the account whose token balances you want.
* `vaultIdentifier?: string` – Optional Cadence resource identifier (e.g. "0x1cf0e2f2f715450.FlowToken.Vault") for onchain balance
* `erc20AddressHexArg?: string` – Optional bridged ERC-20 contract address (hex) for EVM/COA balance
* `query?: Omit<UseQueryOptions<unknown, Error>, "queryKey" | "queryFn">` – Optional TanStack Query config (e.g. staleTime, enabled)
* `flowClient?: FlowClient` - Optional `FlowClient` instance

> **Note:** You must pass `owner`, and one of `vaultIdentifier` or `erc20AddressHexArg`.

#### Returns: `UseQueryResult<UseCrossVmTokenBalanceData | null, Error>`[​](#returns-usequeryresultusecrossvmtokenbalancedata--null-error "Direct link to returns-usequeryresultusecrossvmtokenbalancedata--null-error")

Where `UseCrossVmTokenBalanceData` is defined as:

`_10

interface UseCrossVmTokenBalanceData {

_10

cadence: TokenBalance // Token balance of Cadence vault

_10

evm: TokenBalance // Token balance of EVM (COA stored in /storage/coa)

_10

combined: TokenBalance // Combined balance of both Cadence and EVM

_10

}`

Where `TokenBalance` is defined as:

`_10

interface TokenBalance {

_10

value: bigint // Balance value in smallest unit

_10

formatted: string // Formatted balance string (e.g. "123.45")

_10

precision: number // Number of decimal places for the token

_10

}`

`_20

function UseCrossVmTokenBalanceExample() {

_20

const { data, isLoading, error, refetch } = useCrossVmTokenBalance({

_20

owner: '0x1e4aa0b87d10b141',

_20

vaultIdentifier: 'A.1654653399040a61.FlowToken.Vault',

_20

query: { staleTime: 10000 },

_20

});

_20

_20

if (isLoading) return <p>Loading token balance...</p>;

_20

if (error) return <p>Error fetching token balance: {error.message}</p>;

_20

_20

return (

_20

<div>

_20

<h2>Token Balances</h2>

_20

<p>Cadence Balance: {data.cadence.formatted} (Value: {data.cadence.value})</p>

_20

<p>EVM Balance: {data.evm.formatted} (Value: {data.evm.value})</p>

_20

<p>Combined Balance: {data.combined.formatted} (Value: {data.combined.value})</p>

_20

<button onClick={refetch}>Refetch</button>

_20

</div>

_20

)

_20

}`

---

### `useCrossVmTransactionStatus`[​](#usecrossvmtransactionstatus "Direct link to usecrossvmtransactionstatus")

[Open in Playground →](https://react.flow.com/#usecrossvmtransactionstatus)

`_10

import { useCrossVmTransactionStatus } from "@onflow/react-sdk"`

Subscribes to status updates for a given Cross-VM Flow transaction ID that executes EVM calls. This hook monitors the transaction status and extracts EVM call results if available.

#### Parameters:[​](#parameters-20 "Direct link to Parameters:")

* `id?: string` – Optional Flow transaction ID to monitor
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseCrossVmTransactionStatusResult`[​](#returns-usecrossvmtransactionstatusresult "Direct link to returns-usecrossvmtransactionstatusresult")

Where `UseCrossVmTransactionStatusResult` is defined as:

`_10

interface UseCrossVmTransactionStatusResult {

_10

transactionStatus: TransactionStatus | null // Latest transaction status, or null before any update

_10

evmResults?: CallOutcome[] // EVM transaction results, if available

_10

error: Error | null // Any error encountered during status updates

_10

}`

Where `CallOutcome` is defined as:

`_10

interface CallOutcome {

_10

status: "passed" | "failed" | "skipped" // Status of the EVM call

_10

hash?: string // EVM transaction hash if available

_10

errorMessage?: string // Error message if the call failed

_10

}`

`_26

function CrossVmTransactionStatusComponent() {

_26

const txId = "your-cross-vm-transaction-id-here"

_26

const { transactionStatus, evmResults, error } = useCrossVmTransactionStatus({ id: txId })

_26

_26

if (error) return <div>Error: {error.message}</div>

_26

_26

return (

_26

<div>

_26

<div>Flow Status: {transactionStatus?.statusString}</div>

_26

{evmResults && evmResults.length > 0 && (

_26

<div>

_26

<h3>EVM Call Results:</h3>

_26

<ul>

_26

{evmResults.map((result, idx) => (

_26

<li key={idx}>

_26

Status: {result.status}

_26

{result.hash && <span> | Hash: {result.hash}</span>}

_26

{result.errorMessage && <span> | Error: {result.errorMessage}</span>}

_26

</li>

_26

))}

_26

</ul>

_26

</div>

_26

)}

_26

</div>

_26

)

_26

}`

---

### `useCrossVmBridgeNftFromEvm`[​](#usecrossvmbridgenftfromevm "Direct link to usecrossvmbridgenftfromevm")

[Open in Playground →](https://react.flow.com/#usecrossvmbridgenftfromevm)

`_10

import { useCrossVmBridgeNftFromEvm } from "@onflow/react-sdk"`

This hook bridges NFTs from Flow EVM to Cadence. It withdraws an NFT from the signer's COA (Cadence Owned Account) in EVM and deposits it into their Cadence collection.

#### Parameters:[​](#parameters-21 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmBridgeNftFromEvmTxMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseCrossVmBridgeNftFromEvmTxResult`[​](#returns-usecrossvmbridgenftfromevmtxresult "Direct link to returns-usecrossvmbridgenftfromevmtxresult")

Where `UseCrossVmBridgeNftFromEvmTxResult` is defined as:

`_10

interface UseCrossVmBridgeNftFromEvmTxResult extends Omit<

_10

UseMutationResult<string, Error>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

crossVmBridgeNftFromEvm: (args: UseCrossVmBridgeNftFromEvmTxMutateArgs) => void

_10

crossVmBridgeNftFromEvmAsync: (args: UseCrossVmBridgeNftFromEvmTxMutateArgs) => Promise<string>

_10

}`

Where `UseCrossVmBridgeNftFromEvmTxMutateArgs` is defined as:

`_10

interface UseCrossVmBridgeNftFromEvmTxMutateArgs {

_10

nftIdentifier: string // Cadence type identifier (e.g., "A.0x123.MyNFT.NFT")

_10

nftId: string // EVM NFT ID as string representation of UInt256

_10

}`

`_25

function BridgeNftFromEvmExample() {

_25

const { crossVmBridgeNftFromEvm, isPending, error, data: txId } = useCrossVmBridgeNftFromEvm({

_25

mutation: {

_25

onSuccess: (txId) => console.log("Transaction ID:", txId),

_25

},

_25

})

_25

_25

const handleBridge = () => {

_25

crossVmBridgeNftFromEvm({

_25

nftIdentifier: "A.0x1cf0e2f2f715450.ExampleNFT.NFT",

_25

nftId: "123",

_25

})

_25

}

_25

_25

return (

_25

<div>

_25

<button onClick={handleBridge} disabled={isPending}>

_25

Bridge NFT from EVM

_25

</button>

_25

{isPending && <p>Bridging NFT...</p>}

_25

{error && <p>Error: {error.message}</p>}

_25

{txId && <p>Transaction ID: {txId}</p>}

_25

</div>

_25

)

_25

}`

---

### `useCrossVmBridgeNftToEvm`[​](#usecrossvmbridgenfttoevm "Direct link to usecrossvmbridgenfttoevm")

[Open in Playground →](https://react.flow.com/#usecrossvmbridgenfttoevm)

`_10

import { useCrossVmBridgeNftToEvm } from "@onflow/react-sdk"`

This hook bridges NFTs from Cadence to Flow EVM and executes arbitrary EVM transactions atomically. It withdraws NFTs from the signer's Cadence collection and deposits them into their COA in EVM, then executes the provided EVM calls.

#### Parameters:[​](#parameters-22 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmBridgeNftToEvmTxMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseCrossVmBridgeNftToEvmTxResult`[​](#returns-usecrossvmbridgenfttoevmtxresult "Direct link to returns-usecrossvmbridgenfttoevmtxresult")

Where `UseCrossVmBridgeNftToEvmTxResult` is defined as:

`_10

interface UseCrossVmBridgeNftToEvmTxResult extends Omit<

_10

UseMutationResult<string, Error>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

crossVmBridgeNftToEvm: (args: UseCrossVmBridgeNftToEvmTxMutateArgs) => void

_10

crossVmBridgeNftToEvmAsync: (args: UseCrossVmBridgeNftToEvmTxMutateArgs) => Promise<string>

_10

}`

Where `UseCrossVmBridgeNftToEvmTxMutateArgs` is defined as:

`_10

interface UseCrossVmBridgeNftToEvmTxMutateArgs {

_10

nftIdentifier: string // Cadence NFT type identifier

_10

nftIds: string[] // Array of NFT IDs to bridge

_10

calls: EvmBatchCall[] // Array of EVM calls to execute after bridging

_10

}`

`_34

function BridgeNftToEvmExample() {

_34

const { crossVmBridgeNftToEvm, isPending, error, data: txId } = useCrossVmBridgeNftToEvm({

_34

mutation: {

_34

onSuccess: (txId) => console.log("Transaction ID:", txId),

_34

},

_34

})

_34

_34

const handleBridge = () => {

_34

crossVmBridgeNftToEvm({

_34

nftIdentifier: "A.0x1cf0e2f2f715450.ExampleNFT.NFT",

_34

nftIds: ["1", "2", "3"],

_34

calls: [

_34

{

_34

address: "0x1234567890abcdef1234567890abcdef12345678",

_34

abi: myContractAbi,

_34

functionName: "transferNFT",

_34

args: ["0xRecipient", 1n],

_34

gasLimit: 100000n,

_34

},

_34

],

_34

})

_34

}

_34

_34

return (

_34

<div>

_34

<button onClick={handleBridge} disabled={isPending}>

_34

Bridge NFTs to EVM

_34

</button>

_34

{isPending && <p>Bridging NFTs...</p>}

_34

{error && <p>Error: {error.message}</p>}

_34

{txId && <p>Transaction ID: {txId}</p>}

_34

</div>

_34

)

_34

}`

---

### `useCrossVmBridgeTokenFromEvm`[​](#usecrossvmbridgetokenfromevm "Direct link to usecrossvmbridgetokenfromevm")

[Open in Playground →](https://react.flow.com/#usecrossvmbridgetokenfromevm)

`_10

import { useCrossVmBridgeTokenFromEvm } from "@onflow/react-sdk"`

This hook bridges fungible tokens from Flow EVM to Cadence. It withdraws tokens from the signer's COA in EVM and deposits them into their Cadence vault.

#### Parameters:[​](#parameters-23 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmBridgeTokenFromEvmMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseCrossVmBridgeTokenFromEvmResult`[​](#returns-usecrossvmbridgetokenfromevmresult "Direct link to returns-usecrossvmbridgetokenfromevmresult")

Where `UseCrossVmBridgeTokenFromEvmResult` is defined as:

`_10

interface UseCrossVmBridgeTokenFromEvmResult extends Omit<

_10

UseMutationResult<string, Error>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

crossVmBridgeTokenFromEvm: (args: UseCrossVmBridgeTokenFromEvmMutateArgs) => void

_10

crossVmBridgeTokenFromEvmAsync: (args: UseCrossVmBridgeTokenFromEvmMutateArgs) => Promise<string>

_10

}`

Where `UseCrossVmBridgeTokenFromEvmMutateArgs` is defined as:

`_10

interface UseCrossVmBridgeTokenFromEvmMutateArgs {

_10

vaultIdentifier: string // Cadence vault type identifier (e.g., "A.0x123.FlowToken.Vault")

_10

amount: string // Amount as UInt256 string representation

_10

}`

`_25

function BridgeTokenFromEvmExample() {

_25

const { crossVmBridgeTokenFromEvm, isPending, error, data: txId } = useCrossVmBridgeTokenFromEvm({

_25

mutation: {

_25

onSuccess: (txId) => console.log("Transaction ID:", txId),

_25

},

_25

})

_25

_25

const handleBridge = () => {

_25

crossVmBridgeTokenFromEvm({

_25

vaultIdentifier: "A.0x1654653399040a61.FlowToken.Vault",

_25

amount: "1000000000", // Amount in smallest unit

_25

})

_25

}

_25

_25

return (

_25

<div>

_25

<button onClick={handleBridge} disabled={isPending}>

_25

Bridge Tokens from EVM

_25

</button>

_25

{isPending && <p>Bridging tokens...</p>}

_25

{error && <p>Error: {error.message}</p>}

_25

{txId && <p>Transaction ID: {txId}</p>}

_25

</div>

_25

)

_25

}`

---

### `useCrossVmBridgeTokenToEvm`[​](#usecrossvmbridgetokentoevm "Direct link to usecrossvmbridgetokentoevm")

[Open in Playground →](https://react.flow.com/#usecrossvmbridgetokentoevm)

`_10

import { useCrossVmBridgeTokenToEvm } from "@onflow/react-sdk"`

This hook bridges fungible tokens from Cadence to Flow EVM and executes arbitrary EVM transactions atomically. It withdraws tokens from the signer's Cadence vault and deposits them into their COA in EVM, then executes the provided EVM calls.

#### Parameters:[​](#parameters-24 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmBridgeTokenToEvmMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseCrossVmBridgeTokenToEvmResult`[​](#returns-usecrossvmbridgetokentoevmresult "Direct link to returns-usecrossvmbridgetokentoevmresult")

Where `UseCrossVmBridgeTokenToEvmResult` is defined as:

`_10

interface UseCrossVmBridgeTokenToEvmResult extends Omit<

_10

UseMutationResult<string, Error>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

crossVmBridgeTokenToEvm: (args: UseCrossVmBridgeTokenToEvmMutateArgs) => void

_10

crossVmBridgeTokenToEvmAsync: (args: UseCrossVmBridgeTokenToEvmMutateArgs) => Promise<string>

_10

}`

Where `UseCrossVmBridgeTokenToEvmMutateArgs` is defined as:

`_10

interface UseCrossVmBridgeTokenToEvmMutateArgs {

_10

vaultIdentifier: string // Cadence vault type identifier

_10

amount: string // Amount as decimal string (e.g., "1.5")

_10

calls: EvmBatchCall[] // Array of EVM calls to execute after bridging

_10

}`

`_34

function BridgeTokenToEvmExample() {

_34

const { crossVmBridgeTokenToEvm, isPending, error, data: txId } = useCrossVmBridgeTokenToEvm({

_34

mutation: {

_34

onSuccess: (txId) => console.log("Transaction ID:", txId),

_34

},

_34

})

_34

_34

const handleBridge = () => {

_34

crossVmBridgeTokenToEvm({

_34

vaultIdentifier: "A.0x1654653399040a61.FlowToken.Vault",

_34

amount: "10.5",

_34

calls: [

_34

{

_34

address: "0x1234567890abcdef1234567890abcdef12345678",

_34

abi: erc20Abi,

_34

functionName: "transfer",

_34

args: ["0xRecipient", 1000000n],

_34

gasLimit: 100000n,

_34

},

_34

],

_34

})

_34

}

_34

_34

return (

_34

<div>

_34

<button onClick={handleBridge} disabled={isPending}>

_34

Bridge Tokens to EVM

_34

</button>

_34

{isPending && <p>Bridging tokens...</p>}

_34

{error && <p>Error: {error.message}</p>}

_34

{txId && <p>Transaction ID: {txId}</p>}

_34

</div>

_34

)

_34

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-sdk/hooks.md)

Last updated on **Oct 23, 2025** by **Michael Fabozzi**

[Previous

Flow React SDK](/build/tools/react-sdk)[Next

Components](/build/tools/react-sdk/components)

###### Rate this page

😞😐😊

Copy as Markdown

* [Cadence Hooks](#cadence-hooks)
  + [`useFlowCurrentUser`](#useflowcurrentuser)+ [`useFlowAccount`](#useflowaccount)+ [`useFlowBlock`](#useflowblock)+ [`useFlowChainId`](#useflowchainid)+ [`useFlowClient`](#useflowclient)+ [`useFlowConfig`](#useflowconfig)+ [`useFlowEvents`](#useflowevents)+ [`useFlowQuery`](#useflowquery)+ [`useFlowQueryRaw`](#useflowqueryraw)+ [`useFlowMutate`](#useflowmutate)+ [`useFlowRevertibleRandom`](#useflowrevertiblerandom)+ [`useFlowTransaction`](#useflowtransaction)+ [`useFlowTransactionStatus`](#useflowtransactionstatus)+ [`useDarkMode`](#usedarkmode)+ [`useFlowNftMetadata`](#useflownftmetadata)+ [`useFlowAuthz`](#useflowauthz)+ [`useFlowScheduledTransaction`](#useflowscheduledtransaction)+ [`useFlowScheduledTransactionList`](#useflowscheduledtransactionlist)+ [`useFlowScheduledTransactionCancel`](#useflowscheduledtransactioncancel)+ [`useFlowScheduledTransactionSetup`](#useflowscheduledtransactionsetup)* [Cross-VM Hooks](#cross-vm-hooks)
    + [`useCrossVmBatchTransaction`](#usecrossvmbatchtransaction)+ [`useCrossVmTokenBalance`](#usecrossvmtokenbalance)+ [`useCrossVmTransactionStatus`](#usecrossvmtransactionstatus)+ [`useCrossVmBridgeNftFromEvm`](#usecrossvmbridgenftfromevm)+ [`useCrossVmBridgeNftToEvm`](#usecrossvmbridgenfttoevm)+ [`useCrossVmBridgeTokenFromEvm`](#usecrossvmbridgetokenfromevm)+ [`useCrossVmBridgeTokenToEvm`](#usecrossvmbridgetokentoevm)

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