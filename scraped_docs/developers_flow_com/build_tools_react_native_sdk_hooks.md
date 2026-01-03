# Source: https://developers.flow.com/build/tools/react-native-sdk/hooks

Hooks | Flow Developer Portal



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

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          - [Hooks](/build/tools/react-native-sdk/hooks)- [Components](/build/tools/react-native-sdk/components)+ [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow React Native SDK](/build/tools/react-native-sdk)* Hooks

On this page

# Hooks

info

Many of these hooks are built using [`@tanstack/react-query`](https://tanstack.com/query/latest), which provides powerful caching, revalidation, and background refetching features. As a result, you'll see return types like `UseQueryResult` and `UseMutationResult` throughout this section. Other types—such as `Account`, `Block`, and `CurrentUser`—are from the [Flow Client Library (FCL) TypeDefs](https://github.com/onflow/fcl-js/blob/master/packages/typedefs/src/index.ts). Refer to their respective documentation for full type definitions and usage patterns.

## Cadence Hooks[​](#cadence-hooks "Direct link to Cadence Hooks")

### `useFlowCurrentUser`[​](#useflowcurrentuser "Direct link to useflowcurrentuser")

`_10

import { useFlowCurrentUser } from "@onflow/react-native-sdk"`

#### Parameters[​](#parameters "Direct link to Parameters")

* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns:[​](#returns "Direct link to Returns:")

* `user: CurrentUser` – The current user object from FCL
* `authenticate: () => Promise<CurrentUser>` – Triggers wallet authentication
* `unauthenticate: () => void` – Logs the user out

`_22

import { View, Text, TouchableOpacity } from 'react-native';

_22

_22

function AuthComponent() {

_22

const { user, authenticate, unauthenticate } = useFlowCurrentUser()

_22

_22

return (

_22

<View>

_22

{user?.loggedIn ? (

_22

<View>

_22

<Text>Logged in as {user?.addr}</Text>

_22

<TouchableOpacity onPress={unauthenticate}>

_22

<Text>Logout</Text>

_22

</TouchableOpacity>

_22

</View>

_22

) : (

_22

<TouchableOpacity onPress={authenticate}>

_22

<Text>Login</Text>

_22

</TouchableOpacity>

_22

)}

_22

</View>

_22

)

_22

}`

---

### `useFlowAccount`[​](#useflowaccount "Direct link to useflowaccount")

`_10

import { useFlowAccount } from "@onflow/react-native-sdk"`

#### Parameters:[​](#parameters-1 "Direct link to Parameters:")

* `address?: string` – Flow address (with or without `0x` prefix)
* `query?: UseQueryOptions<Account | null, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<Account | null, Error>`[​](#returns-usequeryresultaccount--null-error "Direct link to returns-usequeryresultaccount--null-error")

`_22

import { View, Text, TouchableOpacity } from 'react-native';

_22

_22

function AccountDetails() {

_22

const { data: account, isLoading, error, refetch } = useFlowAccount({

_22

address: "0x1cf0e2f2f715450",

_22

query: { staleTime: 5000 },

_22

})

_22

_22

if (isLoading) return <Text>Loading account...</Text>

_22

if (error) return <Text>Error fetching account: {error.message}</Text>

_22

if (!account) return <Text>No account data</Text>

_22

_22

return (

_22

<View>

_22

<Text>Account: {account.address}</Text>

_22

<Text>Balance: {account.balance}</Text>

_22

<TouchableOpacity onPress={() => refetch()}>

_22

<Text>Refetch</Text>

_22

</TouchableOpacity>

_22

</View>

_22

)

_22

}`

---

### `useFlowBlock`[​](#useflowblock "Direct link to useflowblock")

`_10

import { useFlowBlock } from "@onflow/react-native-sdk"`

#### Parameters:[​](#parameters-2 "Direct link to Parameters:")

* `sealed?: boolean` – If `true`, fetch latest sealed block
* `id?: string` – Block by ID
* `height?: number` – Block by height
* `query?: UseQueryOptions<Block | null, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

Only one of `sealed`, `id`, or `height` should be provided.

#### Returns: `UseQueryResult<Block | null, Error>`[​](#returns-usequeryresultblock--null-error "Direct link to returns-usequeryresultblock--null-error")

`_16

import { View, Text } from 'react-native';

_16

_16

function LatestBlock() {

_16

const { data: block, isLoading, error } = useFlowBlock({ query: { staleTime: 10000 } })

_16

_16

if (isLoading) return <Text>Loading...</Text>

_16

if (error) return <Text>Error: {error.message}</Text>

_16

if (!block) return <Text>No block data.</Text>

_16

_16

return (

_16

<View>

_16

<Text>Block {block.height}</Text>

_16

<Text>ID: {block.id}</Text>

_16

</View>

_16

)

_16

}`

---

### `useFlowChainId`[​](#useflowchainid "Direct link to useflowchainid")

`_10

import { useFlowChainId } from "@onflow/react-native-sdk"`

This hook retrieves the Flow chain ID, which is useful for identifying the current network.

#### Parameters:[​](#parameters-3 "Direct link to Parameters:")

* `query?: Omit<UseQueryOptions<string | null>, "queryKey" | "queryFn">` – Optional TanStack Query options like `staleTime`, `enabled`, etc.
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<string | null, Error>`[​](#returns-usequeryresultstring--null-error "Direct link to returns-usequeryresultstring--null-error")

Valid chain IDs include: `testnet` (Flow Testnet), `mainnet` (Flow Mainnet), and `emulator` (Flow Emulator). The `flow-` prefix will be stripped from the chain ID returned by the access node (e.g. `flow-testnet` will return `testnet`).

`_12

import { View, Text } from 'react-native';

_12

_12

function ChainIdExample() {

_12

const { data: chainId, isLoading, error } = useFlowChainId({

_12

query: { staleTime: 10000 },

_12

})

_12

_12

if (isLoading) return <Text>Loading chain ID...</Text>

_12

if (error) return <Text>Error fetching chain ID: {error.message}</Text>

_12

_12

return <Text>Current Flow Chain ID: {chainId}</Text>

_12

}`

---

### `useFlowClient`[​](#useflowclient "Direct link to useflowclient")

This hook returns the `FlowClient` for the current `<FlowProvider />` context.

#### Parameters:[​](#parameters-4 "Direct link to Parameters:")

* `flowClient?: FlowClient` - Optional `FlowClient` instance to override the result

---

### `useFlowConfig`[​](#useflowconfig "Direct link to useflowconfig")

`_10

import { useFlowConfig } from "@onflow/react-native-sdk"`

#### Returns: `FlowConfig`[​](#returns-flowconfig "Direct link to returns-flowconfig")

`_12

import { View, Text } from 'react-native';

_12

_12

function MyComponent() {

_12

const config = useFlowConfig()

_12

_12

return (

_12

<View>

_12

<Text>Current network: {config.flowNetwork}</Text>

_12

<Text>Current access node: {config.accessNodeUrl}</Text>

_12

</View>

_12

)

_12

}`

---

### `useFlowEvents`[​](#useflowevents "Direct link to useflowevents")

`_10

import { useFlowEvents } from "@onflow/react-native-sdk"`

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

`_11

import { View, Text } from 'react-native';

_11

_11

function EventListener() {

_11

useFlowEvents({

_11

eventTypes: ["A.0xDeaDBeef.SomeContract.SomeEvent"],

_11

onEvent: (event) => console.log("New event:", event),

_11

onError: (error) => console.error("Error:", error),

_11

})

_11

_11

return <Text>Listening for events...</Text>

_11

}`

---

### `useFlowQuery`[​](#useflowquery "Direct link to useflowquery")

`_10

import { useFlowQuery } from "@onflow/react-native-sdk"`

#### Parameters:[​](#parameters-6 "Direct link to Parameters:")

* `cadence: string` – Cadence script to run
* `args?: (arg, t) => unknown[]` – Function returning FCL arguments
* `query?: UseQueryOptions<unknown, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<unknown, Error>`[​](#returns-usequeryresultunknown-error "Direct link to returns-usequeryresultunknown-error")

`` _26

import { View, Text, TouchableOpacity } from 'react-native';

_26

_26

function QueryExample() {

_26

const { data, isLoading, error, refetch } = useFlowQuery({

_26

cadence: `

_26

access(all)

_26

fun main(a: Int, b: Int): Int {

_26

return a + b

_26

}

_26

`,

_26

args: (arg, t) => [arg(1, t.Int), arg(2, t.Int)],

_26

query: { staleTime: 10000 },

_26

})

_26

_26

if (isLoading) return <Text>Loading query...</Text>

_26

if (error) return <Text>Error: {error.message}</Text>

_26

_26

return (

_26

<View>

_26

<Text>Result: {data}</Text>

_26

<TouchableOpacity onPress={() => refetch()}>

_26

<Text>Refetch</Text>

_26

</TouchableOpacity>

_26

</View>

_26

)

_26

} ``

---

### `useFlowQueryRaw`[​](#useflowqueryraw "Direct link to useflowqueryraw")

`_10

import { useFlowQueryRaw } from "@onflow/react-native-sdk"`

This hook is identical to `useFlowQuery` but returns the raw, non-decoded response data from the Flow blockchain. This is useful when you need access to the original response structure or want to handle decoding manually.

#### Parameters:[​](#parameters-7 "Direct link to Parameters:")

* `cadence: string` – Cadence script to run
* `args?: (arg, t) => unknown[]` – Function returning FCL arguments
* `query?: UseQueryOptions<unknown, Error>` – Optional TanStackQuery options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<unknown, Error>`[​](#returns-usequeryresultunknown-error-1 "Direct link to returns-usequeryresultunknown-error-1")

The returned data will be in its raw, non-decoded format as received from the Flow access node.

`` _26

import { View, Text, TouchableOpacity } from 'react-native';

_26

_26

function QueryRawExample() {

_26

const { data: rawData, isLoading, error, refetch } = useFlowQueryRaw({

_26

cadence: `

_26

access(all)

_26

fun main(a: Int, b: Int): Int {

_26

return a + b

_26

}

_26

`,

_26

args: (arg, t) => [arg(1, t.Int), arg(2, t.Int)],

_26

query: { staleTime: 10000 },

_26

})

_26

_26

if (isLoading) return <Text>Loading query...</Text>

_26

if (error) return <Text>Error: {error.message}</Text>

_26

_26

return (

_26

<View>

_26

<Text>Raw Result: {JSON.stringify(rawData, null, 2)}</Text>

_26

<TouchableOpacity onPress={() => refetch()}>

_26

<Text>Refetch</Text>

_26

</TouchableOpacity>

_26

</View>

_26

)

_26

} ``

---

### `useFlowMutate`[​](#useflowmutate "Direct link to useflowmutate")

`_10

import { useFlowMutate } from "@onflow/react-native-sdk"`

#### Parameters:[​](#parameters-8 "Direct link to Parameters:")

* `mutation?: UseMutationOptions<string, Error, FCLMutateParams>` – Optional TanStackQuery mutation options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseMutationResult<string, Error, FCLMutateParams>`[​](#returns-usemutationresultstring-error-fclmutateparams "Direct link to returns-usemutationresultstring-error-fclmutateparams")

`` _36

import { View, Text, TouchableOpacity } from 'react-native';

_36

import * as fcl from '@onflow/fcl';

_36

_36

function CreatePage() {

_36

const { mutate, isPending, error, data: txId } = useFlowMutate({

_36

mutation: {

_36

onSuccess: (txId) => console.log("TX ID:", txId),

_36

},

_36

})

_36

_36

const sendTransaction = () => {

_36

mutate({

_36

cadence: `transaction() {

_36

prepare(acct: &Account) {

_36

log(acct.address)

_36

}

_36

}`,

_36

args: (arg, t) => [],

_36

proposer: fcl.currentUser,

_36

payer: fcl.currentUser,

_36

authorizations: [],

_36

limit: 100,

_36

})

_36

}

_36

_36

return (

_36

<View>

_36

<TouchableOpacity onPress={sendTransaction} disabled={isPending}>

_36

<Text>Send Transaction</Text>

_36

</TouchableOpacity>

_36

{isPending && <Text>Sending transaction...</Text>}

_36

{error && <Text>Error: {error.message}</Text>}

_36

{txId && <Text>Transaction ID: {txId}</Text>}

_36

</View>

_36

)

_36

} ``

---

### `useFlowRevertibleRandom`[​](#useflowrevertiblerandom "Direct link to useflowrevertiblerandom")

`_10

import { useFlowRevertibleRandom } from "@onflow/react-native-sdk"`

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

`_30

import { View, Text, TouchableOpacity, FlatList } from 'react-native';

_30

_30

function RandomValues() {

_30

const { data: randoms, isLoading, error, refetch } = useFlowRevertibleRandom({

_30

min: "0",

_30

max: "1000000000000000000000000",

_30

count: 3,

_30

query: { staleTime: 10000 },

_30

})

_30

_30

if (isLoading) return <Text>Loading random numbers...</Text>

_30

if (error) return <Text>Error fetching random numbers: {error.message}</Text>

_30

if (!randoms) return <Text>No random values generated.</Text>

_30

_30

return (

_30

<View>

_30

<Text>Generated Random Numbers</Text>

_30

<FlatList

_30

data={randoms}

_30

keyExtractor={(_, idx) => idx.toString()}

_30

renderItem={({ item }) => (

_30

<Text>Block {item.blockHeight}: {item.value}</Text>

_30

)}

_30

/>

_30

<TouchableOpacity onPress={() => refetch()}>

_30

<Text>Regenerate</Text>

_30

</TouchableOpacity>

_30

</View>

_30

)

_30

}`

#### Notes:[​](#notes "Direct link to Notes:")

* Randomness is generated using the **onchain `revertibleRandom`** function on Flow, producing pseudorandom values tied to block and script execution.
* Values are **deterministic**: The values returned for identical calls within the same block will be identical.
* If `count` is larger than one, the returned values are distinct.
* This hook is designed for simple use cases that don't require unpredictability, such as randomized UIs.
  Since the hook uses script executions on existing blocks, the random source is already public and the randoms are predictable.
* For **more advanced use cases** that **do** require onchain randomness logic via transactions, Flow provides built-in support using Cadence's `revertibleRandom` and [commit-reveal scheme](/build/cadence/advanced-concepts/randomness#commit-reveal-scheme).

---

### `useFlowTransaction`[​](#useflowtransaction "Direct link to useflowtransaction")

`_10

import { useFlowTransaction } from "@onflow/react-native-sdk"`

Fetches a Flow transaction by ID and returns the decoded transaction object.

#### Parameters:[​](#parameters-10 "Direct link to Parameters:")

* `txId?: string` – The Flow transaction ID or scheduled transaction ID to fetch.
* `query?: Omit<UseQueryOptions<Transaction | null, Error>, "queryKey" | "queryFn">` – Optional TanStack Query options like `staleTime`, `enabled`, etc.
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<Transaction | null, Error>`[​](#returns-usequeryresulttransaction--null-error "Direct link to returns-usequeryresulttransaction--null-error")

`_23

import { View, Text, TouchableOpacity } from 'react-native';

_23

_23

function TransactionDetails({ txId }: { txId: string }) {

_23

const { data: transaction, isLoading, error, refetch } = useFlowTransaction({

_23

txId,

_23

query: { staleTime: 10000 },

_23

})

_23

_23

if (isLoading) return <Text>Loading transaction...</Text>

_23

if (error) return <Text>Error fetching transaction: {error.message}</Text>

_23

if (!transaction) return <Text>No transaction data.</Text>

_23

_23

return (

_23

<View>

_23

<Text>Transaction ID: {transaction.id}</Text>

_23

<Text>Gas Limit: {transaction.gasLimit}</Text>

_23

<Text>Arguments: {JSON.stringify(transaction.arguments, null, 2)}</Text>

_23

<TouchableOpacity onPress={() => refetch()}>

_23

<Text>Refetch</Text>

_23

</TouchableOpacity>

_23

</View>

_23

)

_23

}`

---

### `useFlowTransactionStatus`[​](#useflowtransactionstatus "Direct link to useflowtransactionstatus")

`_10

import { useFlowTransactionStatus } from "@onflow/react-native-sdk"`

#### Parameters:[​](#parameters-11 "Direct link to Parameters:")

* `id: string` – Transaction ID or scheduled transaction ID to subscribe to
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns:[​](#returns-1 "Direct link to Returns:")

* `transactionStatus: TransactionStatus | null`
* `error: Error | null`

`_10

import { View, Text } from 'react-native';

_10

_10

function TransactionStatusComponent() {

_10

const txId = "your-transaction-id-here"

_10

const { transactionStatus, error } = useFlowTransactionStatus({ id: txId })

_10

_10

if (error) return <Text>Error: {error.message}</Text>

_10

_10

return <Text>Status: {transactionStatus?.statusString}</Text>

_10

}`

---

### `useFlowNftMetadata`[​](#useflownftmetadata "Direct link to useflownftmetadata")

`_10

import { useFlowNftMetadata } from "@onflow/react-native-sdk"`

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

import { View, Text, Image, FlatList } from 'react-native';

_32

_32

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

if (isLoading) return <Text>Loading NFT metadata...</Text>

_32

if (error) return <Text>Error: {error.message}</Text>

_32

if (!nft) return <Text>NFT not found</Text>

_32

_32

return (

_32

<View>

_32

<Text>{nft.name}</Text>

_32

<Image source={{ uri: nft.thumbnailUrl }} style={{ width: 200, height: 200 }} />

_32

<Text>{nft.description}</Text>

_32

{nft.collectionName && <Text>Collection: {nft.collectionName}</Text>}

_32

{nft.rarity && <Text>Rarity: {nft.rarity}</Text>}

_32

{nft.traits && (

_32

<View>

_32

<Text>Traits:</Text>

_32

{Object.entries(nft.traits).map(([key, value]) => (

_32

<Text key={key}>{key}: {value}</Text>

_32

))}

_32

</View>

_32

)}

_32

</View>

_32

)

_32

}`

---

### `useFlowAuthz`[​](#useflowauthz "Direct link to useflowauthz")

`_10

import { useFlowAuthz } from "@onflow/react-native-sdk"`

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

`` _28

import { View, Text, TouchableOpacity } from 'react-native';

_28

import * as fcl from '@onflow/fcl';

_28

_28

// Example 1: Using current user authorization

_28

function CurrentUserAuthExample() {

_28

const authorization = useFlowAuthz()

_28

_28

const sendTransaction = async () => {

_28

const txId = await fcl.mutate({

_28

cadence: `

_28

transaction {

_28

prepare(signer: auth(Storage) &Account) {

_28

log(signer.address)

_28

}

_28

}

_28

`,

_28

authorizations: [authorization],

_28

limit: 100,

_28

})

_28

console.log("Transaction ID:", txId)

_28

}

_28

_28

return (

_28

<TouchableOpacity onPress={sendTransaction}>

_28

<Text>Send Transaction</Text>

_28

</TouchableOpacity>

_28

)

_28

} ``

`` _34

// Example 2: Using custom authorization function

_34

function CustomAuthExample() {

_34

const customAuthz = (account) => ({

_34

...account,

_34

addr: "0xCUSTOMOADDRESS",

_34

keyId: 0,

_34

signingFunction: async (signable) => ({

_34

signature: "0x...",

_34

}),

_34

})

_34

_34

const authorization = useFlowAuthz({ authz: customAuthz })

_34

_34

const sendTransaction = async () => {

_34

const txId = await fcl.mutate({

_34

cadence: `

_34

transaction {

_34

prepare(signer: auth(Storage) &Account) {

_34

log(signer.address)

_34

}

_34

}

_34

`,

_34

authorizations: [authorization],

_34

limit: 100,

_34

})

_34

console.log("Transaction ID:", txId)

_34

}

_34

_34

return (

_34

<TouchableOpacity onPress={sendTransaction}>

_34

<Text>Send Custom Auth Transaction</Text>

_34

</TouchableOpacity>

_34

)

_34

} ``

---

### `useFlowScheduledTransaction`[​](#useflowscheduledtransaction "Direct link to useflowscheduledtransaction")

`_10

import { useFlowScheduledTransaction } from "@onflow/react-native-sdk"`

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

`_22

import { View, Text } from 'react-native';

_22

_22

function ScheduledTransactionDetails({ txId }: { txId: string }) {

_22

const { data: transaction, isLoading, error } = useFlowScheduledTransaction({

_22

txId,

_22

query: { staleTime: 10000 },

_22

})

_22

_22

if (isLoading) return <Text>Loading scheduled transaction...</Text>

_22

if (error) return <Text>Error: {error.message}</Text>

_22

if (!transaction) return <Text>Transaction not found</Text>

_22

_22

return (

_22

<View>

_22

<Text>Scheduled Transaction #{transaction.id}</Text>

_22

<Text>Status: {transaction.status}</Text>

_22

<Text>Priority: {transaction.priority}</Text>

_22

<Text>Fees: {transaction.fees.formatted} FLOW</Text>

_22

<Text>Handler: {transaction.handlerTypeIdentifier}</Text>

_22

</View>

_22

)

_22

}`

---

### `useFlowScheduledTransactionList`[​](#useflowscheduledtransactionlist "Direct link to useflowscheduledtransactionlist")

`_10

import { useFlowScheduledTransactionList } from "@onflow/react-native-sdk"`

Lists all scheduled transactions for an account.

#### Parameters:[​](#parameters-15 "Direct link to Parameters:")

* `account?: string` – Flow address to query
* `includeHandlerData?: boolean` – Include handler data (default: false)
* `query?: UseQueryOptions<ScheduledTransaction[], Error>` – Optional TanStack Query options
* `flowClient?: FlowClient` - Optional `FlowClient` instance

#### Returns: `UseQueryResult<ScheduledTransaction[], Error>`[​](#returns-usequeryresultscheduledtransaction-error "Direct link to returns-usequeryresultscheduledtransaction-error")

`_30

import { View, Text, TouchableOpacity, FlatList } from 'react-native';

_30

_30

function ScheduledTransactionsList({ account }: { account: string }) {

_30

const { data: transactions, isLoading, error, refetch } = useFlowScheduledTransactionList({

_30

account,

_30

query: { staleTime: 10000 },

_30

})

_30

_30

if (isLoading) return <Text>Loading scheduled transactions...</Text>

_30

if (error) return <Text>Error: {error.message}</Text>

_30

if (!transactions || transactions.length === 0) return <Text>No scheduled transactions</Text>

_30

_30

return (

_30

<View>

_30

<Text>Scheduled Transactions for {account}</Text>

_30

<TouchableOpacity onPress={() => refetch()}>

_30

<Text>Refresh</Text>

_30

</TouchableOpacity>

_30

<FlatList

_30

data={transactions}

_30

keyExtractor={(tx) => tx.id}

_30

renderItem={({ item: tx }) => (

_30

<Text>

_30

Transaction #{tx.id} - Status: {tx.status} - Fees: {tx.fees.formatted} FLOW

_30

</Text>

_30

)}

_30

/>

_30

</View>

_30

)

_30

}`

---

### `useFlowScheduledTransactionCancel`[​](#useflowscheduledtransactioncancel "Direct link to useflowscheduledtransactioncancel")

`_10

import { useFlowScheduledTransactionCancel } from "@onflow/react-native-sdk"`

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

`_29

import { View, Text, TouchableOpacity } from 'react-native';

_29

_29

function CancelScheduledTransaction() {

_29

const { cancelTransactionAsync, isPending, error, data: txId } = useFlowScheduledTransactionCancel({

_29

mutation: {

_29

onSuccess: (txId) => console.log("Cancel transaction ID:", txId),

_29

},

_29

})

_29

_29

const handleCancel = async (scheduledTxId: string) => {

_29

try {

_29

const resultTxId = await cancelTransactionAsync(scheduledTxId)

_29

console.log("Successfully canceled scheduled transaction:", resultTxId)

_29

} catch (error) {

_29

console.error("Failed to cancel:", error)

_29

}

_29

}

_29

_29

return (

_29

<View>

_29

<TouchableOpacity onPress={() => handleCancel("42")} disabled={isPending}>

_29

<Text>Cancel Scheduled Transaction #42</Text>

_29

</TouchableOpacity>

_29

{isPending && <Text>Canceling transaction...</Text>}

_29

{error && <Text>Error: {error.message}</Text>}

_29

{txId && <Text>Cancel Transaction ID: {txId}</Text>}

_29

</View>

_29

)

_29

}`

---

### `useFlowScheduledTransactionSetup`[​](#useflowscheduledtransactionsetup "Direct link to useflowscheduledtransactionsetup")

`_10

import { useFlowScheduledTransactionSetup } from "@onflow/react-native-sdk"`

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

`_29

import { View, Text, TouchableOpacity } from 'react-native';

_29

_29

function SchedulerSetup() {

_29

const { setupAsync, isPending, error, data: txId } = useFlowScheduledTransactionSetup({

_29

mutation: {

_29

onSuccess: (txId) => console.log("Setup transaction ID:", txId),

_29

},

_29

})

_29

_29

const handleSetup = async () => {

_29

try {

_29

const resultTxId = await setupAsync()

_29

console.log("Scheduler setup successful:", resultTxId)

_29

} catch (error) {

_29

console.error("Setup failed:", error)

_29

}

_29

}

_29

_29

return (

_29

<View>

_29

<TouchableOpacity onPress={handleSetup} disabled={isPending}>

_29

<Text>Setup Transaction Scheduler</Text>

_29

</TouchableOpacity>

_29

{isPending && <Text>Setting up scheduler...</Text>}

_29

{error && <Text>Error: {error.message}</Text>}

_29

{txId && <Text>Setup Transaction ID: {txId}</Text>}

_29

</View>

_29

)

_29

}`

---

## Cross-VM Hooks[​](#cross-vm-hooks "Direct link to Cross-VM Hooks")

### `useCrossVmBatchTransaction`[​](#usecrossvmbatchtransaction "Direct link to usecrossvmbatchtransaction")

`_10

import { useCrossVmBatchTransaction } from "@onflow/react-native-sdk"`

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

`_36

import { View, Text, TouchableOpacity } from 'react-native';

_36

_36

function CrossVmBatchTransactionExample() {

_36

const { sendBatchTransaction, isPending, error, data: txId } = useCrossVmBatchTransaction({

_36

mutation: {

_36

onSuccess: (txId) => console.log("TX ID:", txId),

_36

},

_36

})

_36

_36

const sendTransaction = () => {

_36

const calls = [

_36

{

_36

address: "0x1234567890abcdef",

_36

abi: {

_36

// ABI definition for the contract

_36

},

_36

functionName: "transfer",

_36

args: ["0xabcdef1234567890", 100n],

_36

gasLimit: 21000n,

_36

},

_36

]

_36

_36

sendBatchTransaction({calls})

_36

}

_36

_36

return (

_36

<View>

_36

<TouchableOpacity onPress={sendTransaction} disabled={isPending}>

_36

<Text>Send Cross-VM Transaction</Text>

_36

</TouchableOpacity>

_36

{isPending && <Text>Sending transaction...</Text>}

_36

{error && <Text>Error: {error.message}</Text>}

_36

{txId && <Text>Transaction ID: {txId}</Text>}

_36

</View>

_36

)

_36

}`

---

### `useCrossVmTokenBalance`[​](#usecrossvmtokenbalance "Direct link to usecrossvmtokenbalance")

`_10

import { useCrossVmTokenBalance } from "@onflow/react-native-sdk"`

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

`_24

import { View, Text, TouchableOpacity } from 'react-native';

_24

_24

function UseCrossVmTokenBalanceExample() {

_24

const { data, isLoading, error, refetch } = useCrossVmTokenBalance({

_24

owner: '0x1e4aa0b87d10b141',

_24

vaultIdentifier: 'A.1654653399040a61.FlowToken.Vault',

_24

query: { staleTime: 10000 },

_24

});

_24

_24

if (isLoading) return <Text>Loading token balance...</Text>

_24

if (error) return <Text>Error fetching token balance: {error.message}</Text>

_24

_24

return (

_24

<View>

_24

<Text>Token Balances</Text>

_24

<Text>Cadence Balance: {data.cadence.formatted} (Value: {data.cadence.value.toString()})</Text>

_24

<Text>EVM Balance: {data.evm.formatted} (Value: {data.evm.value.toString()})</Text>

_24

<Text>Combined Balance: {data.combined.formatted} (Value: {data.combined.value.toString()})</Text>

_24

<TouchableOpacity onPress={() => refetch()}>

_24

<Text>Refetch</Text>

_24

</TouchableOpacity>

_24

</View>

_24

)

_24

}`

---

### `useCrossVmTransactionStatus`[​](#usecrossvmtransactionstatus "Direct link to usecrossvmtransactionstatus")

`_10

import { useCrossVmTransactionStatus } from "@onflow/react-native-sdk"`

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

`_30

import { View, Text, FlatList } from 'react-native';

_30

_30

function CrossVmTransactionStatusComponent() {

_30

const txId = "your-cross-vm-transaction-id-here"

_30

const { transactionStatus, evmResults, error } = useCrossVmTransactionStatus({ id: txId })

_30

_30

if (error) return <Text>Error: {error.message}</Text>

_30

_30

return (

_30

<View>

_30

<Text>Flow Status: {transactionStatus?.statusString}</Text>

_30

{evmResults && evmResults.length > 0 && (

_30

<View>

_30

<Text>EVM Call Results:</Text>

_30

<FlatList

_30

data={evmResults}

_30

keyExtractor={(_, idx) => idx.toString()}

_30

renderItem={({ item, index }) => (

_30

<View>

_30

<Text>Call {index}: {item.status}</Text>

_30

{item.hash && <Text>Hash: {item.hash}</Text>}

_30

{item.errorMessage && <Text>Error: {item.errorMessage}</Text>}

_30

</View>

_30

)}

_30

/>

_30

</View>

_30

)}

_30

</View>

_30

)

_30

}`

---

### `useCrossVmBridgeNftFromEvm`[​](#usecrossvmbridgenftfromevm "Direct link to usecrossvmbridgenftfromevm")

`_10

import { useCrossVmBridgeNftFromEvm } from "@onflow/react-native-sdk"`

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

`_27

import { View, Text, TouchableOpacity } from 'react-native';

_27

_27

function BridgeNftFromEvmExample() {

_27

const { crossVmBridgeNftFromEvm, isPending, error, data: txId } = useCrossVmBridgeNftFromEvm({

_27

mutation: {

_27

onSuccess: (txId) => console.log("Transaction ID:", txId),

_27

},

_27

})

_27

_27

const handleBridge = () => {

_27

crossVmBridgeNftFromEvm({

_27

nftIdentifier: "A.0x1cf0e2f2f715450.ExampleNFT.NFT",

_27

nftId: "123",

_27

})

_27

}

_27

_27

return (

_27

<View>

_27

<TouchableOpacity onPress={handleBridge} disabled={isPending}>

_27

<Text>Bridge NFT from EVM</Text>

_27

</TouchableOpacity>

_27

{isPending && <Text>Bridging NFT...</Text>}

_27

{error && <Text>Error: {error.message}</Text>}

_27

{txId && <Text>Transaction ID: {txId}</Text>}

_27

</View>

_27

)

_27

}`

---

### `useCrossVmBridgeNftToEvm`[​](#usecrossvmbridgenfttoevm "Direct link to usecrossvmbridgenfttoevm")

`_10

import { useCrossVmBridgeNftToEvm } from "@onflow/react-native-sdk"`

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

`_36

import { View, Text, TouchableOpacity } from 'react-native';

_36

_36

function BridgeNftToEvmExample() {

_36

const { crossVmBridgeNftToEvm, isPending, error, data: txId } = useCrossVmBridgeNftToEvm({

_36

mutation: {

_36

onSuccess: (txId) => console.log("Transaction ID:", txId),

_36

},

_36

})

_36

_36

const handleBridge = () => {

_36

crossVmBridgeNftToEvm({

_36

nftIdentifier: "A.0x1cf0e2f2f715450.ExampleNFT.NFT",

_36

nftIds: ["1", "2", "3"],

_36

calls: [

_36

{

_36

address: "0x1234567890abcdef1234567890abcdef12345678",

_36

abi: myContractAbi,

_36

functionName: "transferNFT",

_36

args: ["0xRecipient", 1n],

_36

gasLimit: 100000n,

_36

},

_36

],

_36

})

_36

}

_36

_36

return (

_36

<View>

_36

<TouchableOpacity onPress={handleBridge} disabled={isPending}>

_36

<Text>Bridge NFTs to EVM</Text>

_36

</TouchableOpacity>

_36

{isPending && <Text>Bridging NFTs...</Text>}

_36

{error && <Text>Error: {error.message}</Text>}

_36

{txId && <Text>Transaction ID: {txId}</Text>}

_36

</View>

_36

)

_36

}`

---

### `useCrossVmBridgeTokenFromEvm`[​](#usecrossvmbridgetokenfromevm "Direct link to usecrossvmbridgetokenfromevm")

`_10

import { useCrossVmBridgeTokenFromEvm } from "@onflow/react-native-sdk"`

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

`_27

import { View, Text, TouchableOpacity } from 'react-native';

_27

_27

function BridgeTokenFromEvmExample() {

_27

const { crossVmBridgeTokenFromEvm, isPending, error, data: txId } = useCrossVmBridgeTokenFromEvm({

_27

mutation: {

_27

onSuccess: (txId) => console.log("Transaction ID:", txId),

_27

},

_27

})

_27

_27

const handleBridge = () => {

_27

crossVmBridgeTokenFromEvm({

_27

vaultIdentifier: "A.0x1654653399040a61.FlowToken.Vault",

_27

amount: "1000000000", // Amount in smallest unit

_27

})

_27

}

_27

_27

return (

_27

<View>

_27

<TouchableOpacity onPress={handleBridge} disabled={isPending}>

_27

<Text>Bridge Tokens from EVM</Text>

_27

</TouchableOpacity>

_27

{isPending && <Text>Bridging tokens...</Text>}

_27

{error && <Text>Error: {error.message}</Text>}

_27

{txId && <Text>Transaction ID: {txId}</Text>}

_27

</View>

_27

)

_27

}`

---

### `useCrossVmBridgeTokenToEvm`[​](#usecrossvmbridgetokentoevm "Direct link to usecrossvmbridgetokentoevm")

`_10

import { useCrossVmBridgeTokenToEvm } from "@onflow/react-native-sdk"`

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

`_36

import { View, Text, TouchableOpacity } from 'react-native';

_36

_36

function BridgeTokenToEvmExample() {

_36

const { crossVmBridgeTokenToEvm, isPending, error, data: txId } = useCrossVmBridgeTokenToEvm({

_36

mutation: {

_36

onSuccess: (txId) => console.log("Transaction ID:", txId),

_36

},

_36

})

_36

_36

const handleBridge = () => {

_36

crossVmBridgeTokenToEvm({

_36

vaultIdentifier: "A.0x1654653399040a61.FlowToken.Vault",

_36

amount: "10.5",

_36

calls: [

_36

{

_36

address: "0x1234567890abcdef1234567890abcdef12345678",

_36

abi: erc20Abi,

_36

functionName: "transfer",

_36

args: ["0xRecipient", 1000000n],

_36

gasLimit: 100000n,

_36

},

_36

],

_36

})

_36

}

_36

_36

return (

_36

<View>

_36

<TouchableOpacity onPress={handleBridge} disabled={isPending}>

_36

<Text>Bridge Tokens to EVM</Text>

_36

</TouchableOpacity>

_36

{isPending && <Text>Bridging tokens...</Text>}

_36

{error && <Text>Error: {error.message}</Text>}

_36

{txId && <Text>Transaction ID: {txId}</Text>}

_36

</View>

_36

)

_36

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-native-sdk/hooks.md)

Last updated on **Dec 17, 2025** by **Michael Fabozzi**

[Previous

Flow React Native SDK](/build/tools/react-native-sdk)[Next

Components](/build/tools/react-native-sdk/components)

###### Rate this page

😞😐😊

Copy as Markdown

* [Cadence Hooks](#cadence-hooks)
  + [`useFlowCurrentUser`](#useflowcurrentuser)+ [`useFlowAccount`](#useflowaccount)+ [`useFlowBlock`](#useflowblock)+ [`useFlowChainId`](#useflowchainid)+ [`useFlowClient`](#useflowclient)+ [`useFlowConfig`](#useflowconfig)+ [`useFlowEvents`](#useflowevents)+ [`useFlowQuery`](#useflowquery)+ [`useFlowQueryRaw`](#useflowqueryraw)+ [`useFlowMutate`](#useflowmutate)+ [`useFlowRevertibleRandom`](#useflowrevertiblerandom)+ [`useFlowTransaction`](#useflowtransaction)+ [`useFlowTransactionStatus`](#useflowtransactionstatus)+ [`useFlowNftMetadata`](#useflownftmetadata)+ [`useFlowAuthz`](#useflowauthz)+ [`useFlowScheduledTransaction`](#useflowscheduledtransaction)+ [`useFlowScheduledTransactionList`](#useflowscheduledtransactionlist)+ [`useFlowScheduledTransactionCancel`](#useflowscheduledtransactioncancel)+ [`useFlowScheduledTransactionSetup`](#useflowscheduledtransactionsetup)* [Cross-VM Hooks](#cross-vm-hooks)
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

Copyright © 2026 Flow Foundation. All Rights Reserved.