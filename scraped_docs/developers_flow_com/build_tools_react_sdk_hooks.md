# Source: https://developers.flow.com/build/tools/react-sdk/hooks

Hooks | Flow Developer Portal



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

### Parameters[​](#parameters "Direct link to Parameters")

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

## Cross-VM Hooks[​](#cross-vm-hooks "Direct link to Cross-VM Hooks")

### `useCrossVmBatchTransaction`[​](#usecrossvmbatchtransaction "Direct link to usecrossvmbatchtransaction")

[Open in Playground →](https://react.flow.com/#usecrossvmbatchtransaction)

`_10

import { useCrossVmBatchTransaction } from "@onflow/react-sdk"`

This hook allows you to execute multiple EVM transactions in a single atomic Cadence transaction. It is useful for batch processing EVM calls while ensuring they are executed together, either all succeeding or allowing for some to fail without affecting the others.

#### Parameters:[​](#parameters-12 "Direct link to Parameters:")

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

#### Parameters:[​](#parameters-13 "Direct link to Parameters:")

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

### `useCrossVmSpendNft`[​](#usecrossvmspendnft "Direct link to usecrossvmspendnft")

[Open in Playground →](https://react.flow.com/#usecrossvmspendnft)

`_10

import { useCrossVmSpendNft } from "@onflow/react-sdk"`

Bridge NFTs from Cadence to Flow EVM and execute arbitrary EVM transactions to atomically spend them.

#### Parameters:[​](#parameters-14 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmSpendFtMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

Where `UseCrossVmSpendFtMutateArgs` is defined as:

`_10

interface UseCrossVmSpendFtMutateArgs {

_10

nftIdentifier: string // Cadence NFT identifier (e.g. "0x1cf0e2f2f715450.FlowNFT")

_10

nftIds: string[] // Array of NFT IDs to bridge

_10

calls: EVMBatchCall[] // Array of EVM calls to execute atomically

_10

}`

#### Returns: `UseCrossVmSpendNftResult`[​](#returns-usecrossvmspendnftresult "Direct link to returns-usecrossvmspendnftresult")

Where `UseCrossVmSpendNftResult` is defined as:

`_10

interface UseCrossVmSpendNftResult extends Omit<

_10

UseMutationResult<string, Error, CrossVmSpendNftParams>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

spendNft: (params: CrossVmSpendNftParams) => Promise<string>

_10

spendNftAsync: (params: CrossVmSpendNftParams) => Promise<string>

_10

}`

`_31

function CrossVmSpendNftExample() {

_31

const { spendNft, isPending, error, data: txId } = useCrossVmSpendNft()

_31

_31

const handleSpendNft = () => {

_31

spendNft({

_31

nftIdentifier: "0x1cf0e2f2f715450.FlowNFT", // Cadence NFT identifier

_31

nftIds: ["1"], // Array of NFT IDs to bridge

_31

calls: [

_31

{

_31

abi: contractAbi, // ABI of the EVM contract

_31

contractAddress: "0x1234567890abcdef1234567890abcdef12345678", // EVM contract address

_31

functionName: "transferNFT",

_31

args: ["123"], // Example args

_31

value: "1000000000000000000", // Amount in wei (if applicable)

_31

gasLimit: "21000", // Gas limit for the EVM call

_31

},

_31

],

_31

})

_31

}

_31

_31

return (

_31

<div>

_31

<button onClick={handleSpendNft} disabled={isPending}>

_31

Bridge and Spend NFT

_31

</button>

_31

{isPending && <p>Sending transaction...</p>}

_31

{error && <p>Error: {error.message}</p>}

_31

{txId && <p>Transaction ID: {txId}</p>}

_31

</div>

_31

)

_31

}`

---

### `useCrossVmSpendToken`[​](#usecrossvmspendtoken "Direct link to usecrossvmspendtoken")

[Open in Playground →](https://react.flow.com/#usecrossvmspendtoken)

`_10

import { useCrossVmSpendToken } from "@onflow/react-sdk"`

Bridge FTs from Cadence to Flow EVM and execute arbitrary EVM transactions to atomically spend them.

#### Parameters:[​](#parameters-15 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, UseCrossVmSpendTokenMutateArgs>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

Where `UseCrossVmSpendTokenMutateArgs` is defined as:

`_10

interface UseCrossVmSpendTokenMutateArgs {

_10

vaultIdentifier: string; // Cadence vault identifier (e.g. "0x1cf0e2f2f715450.ExampleToken.Vault")

_10

amount: string; // Amount of tokens to bridge, as a decimal string (e.g. "1.23")

_10

calls: EVMBatchCall[]; // Array of EVM calls to execute after bridging

_10

}`

#### Returns: `UseCrossVmSpendTokenResult`[​](#returns-usecrossvmspendtokenresult "Direct link to returns-usecrossvmspendtokenresult")

Where `UseCrossVmSpendTokenResult` is defined as:

`_10

interface UseCrossVmSpendTokenResult extends Omit<

_10

UseMutationResult<string, Error, UseCrossVmSpendTokenMutateArgs>,

_10

"mutate" | "mutateAsync"

_10

> {

_10

spendToken: (args: UseCrossVmSpendTokenMutateArgs) => void; // Function to trigger the FT bridging and EVM calls

_10

spendTokenAsync: (args: UseCrossVmSpendTokenMutateArgs) => Promise<string>; // Async version of spendToken

_10

}`

`_31

function CrossVmSpendTokenExample() {

_31

const { spendToken, isPending, error, data: txId } = useCrossVmSpendToken()

_31

_31

const handleSpendToken = () => {

_31

spendToken({

_31

vaultIdentifier: "0x1cf0e2f2f715450.ExampleToken.Vault", // Cadence vault identifier

_31

amount: "1.23", // Amount of tokens to bridge to EVM

_31

calls: [

_31

{

_31

abi: myEvmContractAbi, // EVM contract ABI

_31

address: "0x01234567890abcdef01234567890abcdef", // EVM contract address

_31

function: "transfer", // EVM function to call

_31

args: [

_31

"0xabcdef01234567890abcdef01234567890abcdef", // Recipient address

_31

],

_31

},

_31

],

_31

})

_31

}

_31

_31

return (

_31

<div>

_31

<button onClick={handleSpendToken} disabled={isPending}>

_31

Bridge and Spend FTs

_31

</button>

_31

{isPending && <p>Sending transaction...</p>}

_31

{error && <p>Error: {error.message}</p>}

_31

{txId && <p>Cadence Transaction ID: {txId}</p>}

_31

</div>

_31

)

_31

}`

---

### `useCrossVmTransactionStatus`[​](#usecrossvmtransactionstatus "Direct link to usecrossvmtransactionstatus")

[Open in Playground →](https://react.flow.com/#usecrossvmtransactionstatus)

`_10

import { useCrossVmTransactionStatus } from "@onflow/react-sdk"`

Subscribes to status updates for a given Cross-VM Flow transaction ID that executes EVM calls. This hook monitors the transaction status and extracts EVM call results if available.

#### Parameters:[​](#parameters-16 "Direct link to Parameters:")

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-sdk/hooks.md)

Last updated on **Oct 7, 2025** by **mfbz**

[Previous

Flow React SDK](/build/tools/react-sdk)[Next

Components](/build/tools/react-sdk/components)

###### Rate this page

😞😐😊

Copy as Markdown

* [Cadence Hooks](#cadence-hooks)
  + [`useFlowCurrentUser`](#useflowcurrentuser)+ [Parameters](#parameters)+ [`useFlowAccount`](#useflowaccount)+ [`useFlowBlock`](#useflowblock)+ [`useFlowChainId`](#useflowchainid)+ [`useFlowClient`](#useflowclient)+ [`useFlowConfig`](#useflowconfig)+ [`useFlowEvents`](#useflowevents)+ [`useFlowQuery`](#useflowquery)+ [`useFlowQueryRaw`](#useflowqueryraw)+ [`useFlowMutate`](#useflowmutate)+ [`useFlowRevertibleRandom`](#useflowrevertiblerandom)+ [`useFlowTransaction`](#useflowtransaction)+ [`useFlowTransactionStatus`](#useflowtransactionstatus)+ [`useDarkMode`](#usedarkmode)* [Cross-VM Hooks](#cross-vm-hooks)
    + [`useCrossVmBatchTransaction`](#usecrossvmbatchtransaction)+ [`useCrossVmTokenBalance`](#usecrossvmtokenbalance)+ [`useCrossVmSpendNft`](#usecrossvmspendnft)+ [`useCrossVmSpendToken`](#usecrossvmspendtoken)+ [`useCrossVmTransactionStatus`](#usecrossvmtransactionstatus)

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