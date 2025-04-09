# Source: https://developers.flow.com/tutorials/cross-vm-apps/add-to-wagmi

Update Existing wagmi App | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [AI Plus Flow](/tutorials/ai-plus-flow)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)

  + [Batched Tx From Scaffold](/tutorials/cross-vm-apps/introduction)
  + [Update Existing wagmi App](/tutorials/cross-vm-apps/add-to-wagmi)
  + [Interacting with COAs](/tutorials/cross-vm-apps/interacting-with-coa)
  + [Direct Calls to Flow EVM](/tutorials/cross-vm-apps/direct-calls)
  + [Batched EVM Transactions](/tutorials/cross-vm-apps/batched-evm-transactions)
  + [Cross-VM Bridge](/tutorials/cross-vm-apps/vm-bridge)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)
* [AI Guides](/tutorials/AI Guides/agentkit-flow-guide)

* [Cross-VM Apps](/tutorials/cross-vm-apps)
* Update Existing wagmi App

On this page

# Add Flow Cadence to Your wagmi App

This tutorial demonstrates how to enhance your existing wagmi/RainbowKit application with Flow Cadence capabilities. By integrating the Flow Client Library (FCL) with your EVM stack, you can unlock powerful features like batch transactions with a single signature.

## Video Overview[​](#video-overview "Direct link to Video Overview")

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Add FCL to your existing wagmi/RainbowKit application
* Configure FCL to work alongside your EVM wallet connections
* Implement batch transactions that execute multiple EVM calls in a single Cadence transaction
* Display both Cadence and EVM addresses in your application

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Next.js and Modern Frontend Development[​](#nextjs-and-modern-frontend-development "Direct link to Next.js and Modern Frontend Development")

This tutorial uses [Next.js](https://nextjs.org/docs/app/getting-started/installation). You don't need to be an expert, but it's helpful to be comfortable with development using a current React framework. You'll be on your own to select and use a package manager, manage Node versions, and other frontend environment tasks. If you don't have your own preference, you can just follow along with us and use [npm](https://www.npmjs.com/).

### Solidity and Cadence Smart Contract Development[​](#solidity-and-cadence-smart-contract-development "Direct link to Solidity and Cadence Smart Contract Development")

Apps using the hybrid approach can interact with both [Cadence](https://cadence-lang.org/docs) and [Solidity](https://soliditylang.org/) smart contracts. You don't need to be an expert in either of these, but it's helpful to be familiar with how smart contracts work in at least one of these languages.

### Onchain App Frontends[​](#onchain-app-frontends "Direct link to Onchain App Frontends")

We're assuming you're familiar with [wagmi](https://wagmi.sh/), [viem](https://viem.sh/), and [RainbowKit](https://www.rainbowkit.com/). If you're coming from the Cadence, you might want to take a quick look at the getting started guides for these platforms. They're all excellent and will rapidly get you up to speed on how the EVM world commonly connects their apps to their contracts.

## Create an App[​](#create-an-app "Direct link to Create an App")

Start by creating an app using [RainbowKit](https://www.rainbowkit.com/)'s scaffold:

`_10

npm init @rainbow-me/rainbowkit@latest`

## Install Required Dependencies[​](#install-required-dependencies "Direct link to Install Required Dependencies")

Continue by adding the necessary Flow dependencies to your project:

`_10

npm install @onflow/fcl @onflow/fcl-rainbowkit-adapter`

These packages provide:

* `@onflow/fcl`: The Flow Client Library for interacting with the Cadence VM
* `@onflow/fcl-rainbowkit-adapter`: An adapter that allows RainbowKit to work with FCL-compatible wallets

## Step 2: Configure FCL in Your wagmi Setup[​](#step-2-configure-fcl-in-your-wagmi-setup "Direct link to Step 2: Configure FCL in Your wagmi Setup")

Update your wagmi configuration (`src/wagmi.ts`) to include FCL:

`_38

'use client';

_38

_38

import {

_38

flowWallet,

_38

walletConnectWallet,

_38

} from '@onflow/fcl-rainbowkit-adapter';

_38

import { connectorsForWallets } from '@rainbow-me/rainbowkit';

_38

import { flowTestnet } from 'wagmi/chains';

_38

import * as fcl from '@onflow/fcl';

_38

import { createConfig, http } from 'wagmi';

_38

_38

fcl.config({

_38

'accessNode.api': 'https://rest-testnet.onflow.org',

_38

'discovery.wallet': 'https://fcl-discovery.onflow.org/mainnet/authn',

_38

'walletconnect.projectId': '9b70cfa398b2355a5eb9b1cf99f4a981',

_38

});

_38

_38

const connectors = connectorsForWallets(

_38

[

_38

{

_38

groupName: 'Recommended',

_38

wallets: [flowWallet(), walletConnectWallet],

_38

},

_38

],

_38

{

_38

appName: 'RainbowKit demo',

_38

projectId: '9b70cfa398b2355a5eb9b1cf99f4a981',

_38

},

_38

);

_38

_38

export const config = createConfig({

_38

chains: [flowTestnet],

_38

connectors,

_38

ssr: true,

_38

transports: {

_38

[flowTestnet.id]: http(),

_38

},

_38

});`

## Step 3: Add the Batch Transaction Utility[​](#step-3-add-the-batch-transaction-utility "Direct link to Step 3: Add the Batch Transaction Utility")

Create a custom hook in `src/hooks/useBatchTransactions.ts` to handle batch transactions. This utility allows you to execute multiple EVM transactions in a single Cadence transaction:

`_219

import * as fcl from '@onflow/fcl';

_219

import { Abi, bytesToHex, encodeFunctionData, toBytes } from 'viem';

_219

import { useState } from 'react';

_219

import { useAccount } from 'wagmi';

_219

_219

// Define the interface for each EVM call.

_219

export interface EVMBatchCall {

_219

address: string; // The target EVM contract address (as a string)

_219

abi: Abi; // The contract ABI fragment (as JSON)

_219

functionName: string; // The name of the function to call

_219

args?: readonly unknown[]; // The function arguments

_219

gasLimit?: bigint; // The gas limit for the call

_219

value?: bigint; // The value to send with the call

_219

}

_219

_219

export interface CallOutcome {

_219

status: 'passed' | 'failed' | 'skipped';

_219

hash?: string;

_219

errorMessage?: string;

_219

}

_219

_219

export type EvmTransactionExecutedData = {

_219

hash: string[];

_219

index: string;

_219

type: string;

_219

payload: string[];

_219

errorCode: string;

_219

errorMessage: string;

_219

gasConsumed: string;

_219

contractAddress: string;

_219

logs: string[];

_219

blockHeight: string;

_219

returnedData: string[];

_219

precompiledCalls: string[];

_219

stateUpdateChecksum: string;

_219

};

_219

_219

// Helper to encode our ca lls using viem.

_219

// Returns an array of objects with keys "address" and "data" (hex-encoded string without the "0x" prefix).

_219

export function encodeCalls(

_219

calls: EVMBatchCall[],

_219

): Array<Array<{ key: string; value: string }>> {

_219

return calls.map((call) => {

_219

const encodedData = encodeFunctionData({

_219

abi: call.abi,

_219

functionName: call.functionName,

_219

args: call.args,

_219

});

_219

_219

return [

_219

{ key: 'to', value: call.address },

_219

{ key: 'data', value: fcl.sansPrefix(encodedData) ?? '' },

_219

{ key: 'gasLimit', value: call.gasLimit?.toString() ?? '15000000' },

_219

{ key: 'value', value: call.value?.toString() ?? '0' },

_219

];

_219

}) as any;

_219

}

_219

_219

const EVM_CONTRACT_ADDRESSES = {

_219

testnet: '0x8c5303eaa26202d6',

_219

mainnet: '0xe467b9dd11fa00df',

_219

};

_219

_219

// Takes a chain id and returns the cadence tx with addresses set

_219

const getCadenceBatchTransaction = (chainId: number) => {

_219

const isMainnet = chainId === 0x747;

_219

const evmAddress = isMainnet

_219

? EVM_CONTRACT_ADDRESSES.mainnet

_219

: EVM_CONTRACT_ADDRESSES.testnet;

_219

_219

return `

_219

import EVM from ${evmAddress}

_219

_219

transaction(calls: [{String: AnyStruct}], mustPass: Bool) {

_219

_219

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_219

_219

prepare(signer: auth(BorrowValue) & Account) {

_219

let storagePath = /storage/evm

_219

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: storagePath)

_219

?? panic("No CadenceOwnedAccount (COA) found at ".concat(storagePath.toString()))

_219

}

_219

_219

execute {

_219

for i, call in calls {

_219

let to = call["to"] as! String

_219

let data = call["data"] as! String

_219

let gasLimit = call["gasLimit"] as! UInt64

_219

let value = call["value"] as! UInt

_219

_219

let result = self.coa.call(

_219

to: EVM.addressFromString(to),

_219

data: data.decodeHex(),

_219

gasLimit: gasLimit,

_219

value: EVM.Balance(attoflow: value)

_219

)

_219

_219

if mustPass {

_219

assert(

_219

result.status == EVM.Status.successful,

_219

message: "Call index ".concat(i.toString()).concat(" to ").concat(to)

_219

.concat(" with calldata ").concat(data).concat(" failed: ")

_219

.concat(result.errorMessage)

_219

)

_219

}

_219

}

_219

}

_219

}

_219

`;

_219

};

_219

_219

// Custom hook that returns a function to send a batch transaction

_219

export function useBatchTransaction() {

_219

const { chain } = useAccount();

_219

_219

const cadenceTx = chain?.id ? getCadenceBatchTransaction(chain.id) : null;

_219

_219

const [isPending, setIsPending] = useState<boolean>(false);

_219

const [isError, setIsError] = useState<boolean>(false);

_219

const [txId, setTxId] = useState<string>('');

_219

const [results, setResults] = useState<CallOutcome[]>([]);

_219

_219

async function sendBatchTransaction(

_219

calls: EVMBatchCall[],

_219

mustPass: boolean = true,

_219

) {

_219

// Reset state

_219

setIsPending(true);

_219

setIsError(false);

_219

setTxId('');

_219

setResults([]);

_219

_219

try {

_219

if (!cadenceTx) {

_219

throw new Error('No current chain found');

_219

}

_219

_219

const encodedCalls = encodeCalls(calls);

_219

_219

const txId = await fcl.mutate({

_219

cadence: cadenceTx,

_219

args: (arg, t) => [

_219

// Pass encodedCalls as an array of dictionaries with keys (String, String)

_219

arg(

_219

encodedCalls,

_219

t.Array(

_219

t.Dictionary([

_219

{ key: t.String, value: t.String },

_219

{ key: t.String, value: t.String },

_219

{ key: t.String, value: t.UInt64 },

_219

{ key: t.String, value: t.UInt },

_219

] as any),

_219

),

_219

),

_219

// Pass mustPass=true to revert the entire transaction if any call fails

_219

arg(true, t.Bool),

_219

],

_219

limit: 9999,

_219

});

_219

_219

setTxId(txId);

_219

_219

// The transaction may revert if mustPass=true and one of the calls fails,

_219

// so we catch that error specifically.

_219

let txResult;

_219

try {

_219

txResult = await fcl.tx(txId).onceExecuted();

_219

} catch (txError) {

_219

// If we land here, the transaction likely reverted.

_219

// We can return partial or "failed" outcomes for all calls.

_219

setIsError(true);

_219

setResults(

_219

calls.map(() => ({

_219

status: 'failed' as const,

_219

hash: undefined,

_219

errorMessage: 'Transaction reverted',

_219

})),

_219

);

_219

setIsPending(false);

_219

return;

_219

}

_219

_219

// Filter for TransactionExecuted events

_219

const executedEvents = txResult.events.filter((e: any) =>

_219

e.type.includes('TransactionExecuted'),

_219

);

_219

_219

// Build a full outcomes array for every call.

_219

// For any call index where no event exists, mark it as "skipped".

_219

const outcomes: CallOutcome[] = calls.map((_, index) => {

_219

const eventData = executedEvents[index]

_219

?.data as EvmTransactionExecutedData;

_219

if (eventData) {

_219

return {

_219

hash: bytesToHex(

_219

Uint8Array.from(

_219

eventData.hash.map((x: string) => parseInt(x, 10)),

_219

),

_219

),

_219

status: eventData.errorCode === '0' ? 'passed' : 'failed',

_219

errorMessage: eventData.errorMessage,

_219

};

_219

} else {

_219

return {

_219

status: 'skipped',

_219

};

_219

}

_219

});

_219

_219

setResults(outcomes);

_219

setIsPending(false);

_219

} catch (error: any) {

_219

setIsError(true);

_219

setIsPending(false);

_219

}

_219

}

_219

_219

return { sendBatchTransaction, isPending, isError, txId, results };

_219

}`

## Step 4: Implement the UI[​](#step-4-implement-the-ui "Direct link to Step 4: Implement the UI")

Now, update your application's `page.tsx` to use the batch transaction utility. Update

`_87

'use client';

_87

_87

import { ConnectButton } from '@rainbow-me/rainbowkit';

_87

import CodeEvaluator from './code-evaluator';

_87

import { useAccount } from 'wagmi';

_87

import { useEffect, useState } from 'react';

_87

import * as fcl from '@onflow/fcl';

_87

import { CurrentUser } from '@onflow/typedefs';

_87

import {

_87

EVMBatchCall,

_87

useBatchTransaction,

_87

} from '../hooks/useBatchTransaction';

_87

_87

function Page() {

_87

const coa = useAccount();

_87

const [flowAddress, setFlowAddress] = useState<string | null>(null);

_87

const { sendBatchTransaction, isPending, isError, txId, results } =

_87

useBatchTransaction();

_87

_87

useEffect(() => {

_87

const unsub = fcl.currentUser().subscribe((user: CurrentUser) => {

_87

setFlowAddress(user.addr ?? null);

_87

});

_87

return () => unsub();

_87

}, []);

_87

_87

// Define a "real" calls array to demonstrate a batch transaction.

_87

// In this example, we call two functions on a token contract:

_87

// 1. deposit() to wrap FLOW (e.g., WFLOW)

_87

// 2. approve() to allow a spender to spend tokens.

_87

const calls: EVMBatchCall[] = [

_87

{

_87

// Call deposit() function (wrap FLOW) on the token contract.

_87

address: '0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e', // Replace with your actual token contract address.

_87

abi: [

_87

{

_87

inputs: [],

_87

name: 'deposit',

_87

outputs: [],

_87

stateMutability: 'payable',

_87

type: 'function',

_87

},

_87

],

_87

functionName: 'deposit',

_87

args: [], // deposit takes no arguments; value is passed with the call.

_87

},

_87

{

_87

// Call approve() function (ERC20 style) on the same token contract.

_87

address: '0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e', // Replace with your actual token contract address if needed.

_87

abi: [

_87

{

_87

inputs: [

_87

{ name: 'spender', type: 'address' },

_87

{ name: 'value', type: 'uint256' },

_87

],

_87

name: 'approve',

_87

outputs: [{ name: '', type: 'bool' }],

_87

stateMutability: 'nonpayable',

_87

type: 'function',

_87

},

_87

],

_87

functionName: 'approve',

_87

args: [

_87

'0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2', // Spender address.

_87

BigInt('1000000000000000000'), // Approve 1 token (assuming 18 decimals).

_87

],

_87

},

_87

];

_87

_87

return (

_87

<>

_87

<div style={{ display: 'flex', justifyContent: 'flex-end', padding: 12 }}>

_87

<ConnectButton />

_87

</div>

_87

<h3>Flow Address: {flowAddress}</h3>

_87

<h3>EVM Address: {coa?.address}</h3>

_87

<br />

_87

<button onClick={() => sendBatchTransaction(calls)}>

_87

Send Batch Transaction Example

_87

</button>

_87

{<p>{JSON.stringify({ isPending, isError, txId, results })}</p>}

_87

<CodeEvaluator />

_87

</>

_87

);

_87

}

_87

_87

export default Page;`

## Step 5: Test Your Application[​](#step-5-test-your-application "Direct link to Step 5: Test Your Application")

1. Start your development server:

   `_10

   npm run dev`
2. Connect your wallet using the RainbowKit `ConnectButton`

   * Make sure to use a Cadence-compatible wallet like Flow Wallet
3. Click the "Send Batch Transaction" button

   * You'll be prompted to approve the Cadence transaction
   * This transaction will execute multiple EVM calls in a single atomic operation
4. Observe the results

   * The Cadence transaction ID will be displayed
   * The results of each EVM transaction will be shown

## How It Works[​](#how-it-works "Direct link to How It Works")

When you call `sendBatchTransaction`, the following happens:

1. A Cadence transaction is created that includes all your EVM calls
2. The transaction is executed using FCL's `mutate` function
3. The Cadence transaction calls each EVM transaction in sequence
4. If any transaction fails and `mustPass` is true, the entire batch is rolled back
5. The results of each EVM transaction are returned

This approach gives you several advantages:

* **Atomic Operations**: All transactions succeed or fail together
* **Single Signature**: Users only need to sign one transaction
* **Gas Efficiency**: Reduced gas costs compared to separate transactions
* **Simplified UX**: Users don't need to approve multiple transactions

## Conclusion[​](#conclusion "Direct link to Conclusion")

You've successfully integrated Flow Cadence with your wagmi/rainbowkit application! This integration allows you to leverage the power of Cadence while maintaining the familiar EVM development experience.

## Reference Implementation[​](#reference-implementation "Direct link to Reference Implementation")

For a complete reference implementation, check out the [FCL + RainbowKit + wagmi Integration Demo](https://github.com/jribbink/cross-vm-app) repository.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/cross-vm-apps/add-to-wagmi.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

[Previous

Batched Tx From Scaffold](/tutorials/cross-vm-apps/introduction)[Next

Interacting with COAs](/tutorials/cross-vm-apps/interacting-with-coa)

###### Rate this page

😞😐😊

* [Video Overview](#video-overview)
* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
  + [Next.js and Modern Frontend Development](#nextjs-and-modern-frontend-development)
  + [Solidity and Cadence Smart Contract Development](#solidity-and-cadence-smart-contract-development)
  + [Onchain App Frontends](#onchain-app-frontends)
* [Create an App](#create-an-app)
* [Install Required Dependencies](#install-required-dependencies)
* [Step 2: Configure FCL in Your wagmi Setup](#step-2-configure-fcl-in-your-wagmi-setup)
* [Step 3: Add the Batch Transaction Utility](#step-3-add-the-batch-transaction-utility)
* [Step 4: Implement the UI](#step-4-implement-the-ui)
* [Step 5: Test Your Application](#step-5-test-your-application)
* [How It Works](#how-it-works)
* [Conclusion](#conclusion)
* [Reference Implementation](#reference-implementation)

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