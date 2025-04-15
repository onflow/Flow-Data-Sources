# Source: https://developers.flow.com/tutorials/cross-vm-apps/introduction

Batched Tx From Scaffold | Flow Developer Portal



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

* [Cross-VM Apps](/tutorials/cross-vm-apps)
* Batched Tx From Scaffold

On this page

# Batched Tx From Scaffold

Ever since the launch of Flow EVM, it's been possible to *supercharge* your EVM apps by using Flow Cadence features and contracts. Some benefits, such as [native VRF](/evm/guides/vrf) and inexpensive gas without compromising security are built in and either easy or automatic to use. Others, such as the ability to use [Cadence](https://cadence-lang.org/docs) to [structure and call EVM transactions](/tutorials/cross-vm-apps/batched-evm-transactions), are powerful but complicated to configure and use. They also require developers to manage concurrent connections to both networks.

[FLIP 316](https://github.com/onflow/flips/pull/317) improves the [Flow Client Library (FCL)](/tools/clients/fcl-js) to support cross-VM functionality between Flow EVM and Flow Cadence.

For EVM developers, this means that you can use the familiar [wagmi](https://wagmi.sh/), [viem](https://viem.sh/), and [RainbowKit](https://www.rainbowkit.com/) stack you're used to, add FCL, and get features like **multi-call write** with one signature for users with a Cadence-compatible [wallet](/ecosystem/wallets).

In this tutorial, you'll learn how to create [Click to Mint](https://clicktomint.vercel.app/), a simple game that allows players to mint an ERC-20 token by clicking a button. With the power of Flow, they can also click a button, and **complete 10 separate transactions with just one approval!**

![Click to Mint](/assets/images/click-to-mint-89f90591b2006954bf4b6b1ff5546e4c.png)

warning

The FCL functionality described in this tutorial is in alpha. Some steps may change. We'll keep the tutorial updated, but please [create an issue](https://github.com/onflow/docs/issues/new/choose) or let us know on [Discord](https://discord.com/channels/613813861610684416/1162086721471647874) if something isn't working for you.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Build an app that seamlessly integrates Flow Cadence and Flow EVM connections
* Add Cadence features to your [Rainbowkit](https://www.rainbowkit.com/)/[wagmi](https://wagmi.sh/)/[viem](https://viem.sh/) app
* Utilize [Flow Client Library (FCL)](/tools/clients/fcl-js) to enable multi-call contract writes to Flow EVM

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Next.js and Modern Frontend Development[​](#nextjs-and-modern-frontend-development "Direct link to Next.js and Modern Frontend Development")

This tutorial uses [Next.js](https://nextjs.org/docs/app/getting-started/installation). You don't need to be an expert, but it's helpful to be comfortable with development using a current React framework. You'll be on your own to select and use a package manager, manage Node versions, and other frontend environment tasks. If you don't have your own preference, you can just follow along with us and use [npm](https://www.npmjs.com/).

### Solidity and Cadence Smart Contract Development[​](#solidity-and-cadence-smart-contract-development "Direct link to Solidity and Cadence Smart Contract Development")

Apps using the hybrid approach can interact with both [Cadence](https://cadence-lang.org/docs) and [Solidity](https://soliditylang.org/) smart contracts. You don't need to be an expert in either of these, but it's helpful to be familiar with how smart contracts work in at least one of these languages.

### Onchain App Frontends[​](#onchain-app-frontends "Direct link to Onchain App Frontends")

We're assuming you're familiar with [wagmi](https://wagmi.sh/), [viem](https://viem.sh/), and [RainbowKit](https://www.rainbowkit.com/). If you're coming from the Cadence, you might want to take a quick look at the getting started guides for these platforms. They're all excellent and will rapidly get you up to speed on how the EVM world commonly connects their apps to their contracts.

## Getting Started[​](#getting-started "Direct link to Getting Started")

For this tutorial, we'll be starting from a fork of the [FCL + RainbowKit + Wagmi Integration Demo](https://github.com/jribbink/cross-vm-app) built by the team.

Fork the repo so you can push your work freely to your own copy, then follow the setup instructions.

## Project Overview[​](#project-overview "Direct link to Project Overview")

Open the cross-vm app scaffold in your editor, run it, and view the site in your browser:

`_10

npm run dev`

You'll see:

![Hybrid App Demo](/assets/images/hybrid-app-demo-1dc8ad463bcb9605323ac4c54302bd01.png)

Connect with a Cadence-compatible [wallet](/ecosystem/wallets).

warning

In a production app, you'll want to manage this process carefully. Non-Cadence EVM wallets may be able to connect, but they will **not** be able to use any Cadence features.

## Send Batch Transactions[​](#send-batch-transactions "Direct link to Send Batch Transactions")

The first demo built into this scaffold is **multi-call contract write**.

On Flow, this isn't an unstable experimental feature - it's a demonstration of the power of EVM + Cadence.

Click `Send Batch Transaction Example` and approve the transaction. You'll see three lines appear on the page, similar to:

`_10

{"isPending":false,"isError":false,"txId":"b3c2b8c86e68177af04324152d45d9de9c2a118ff8f090476b3a07e0c9554912","results":[{"hash":"0x46e923a08d9008632e3782ea512c4c590d4650ba58b3e8b49628f58e6adddaa9","status":"passed","errorMessage":""},{"hash":"0x52c82dc689cd5909519f8a90d0a1ec2e74192d7603fd3b5d33f7f4d54a618a84","status":"passed","errorMessage":""}]}`

tip

Currently, the Flow wallet sponsors all gas for all transactions signed with the wallet on both testnet **and mainnet!**

### Cadence Parent Transaction[​](#cadence-parent-transaction "Direct link to Cadence Parent Transaction")

The first line is the transaction id of the Flow Cadence transaction that calls **both** of the EVM transactions. Search for it in [Testnet Cadence Flowscan](https://testnet.flowscan.io).

Cadence transactions are more complicated than those in Solidity contracts. Rather than being restricted to running functions present on the contract, they can run arbitrary code as long as the caller has access to all of the resources required by the transaction.

You can see the code of the transaction in the `Script` tab, but we've included it here for convenience:

`_38

import EVM from 0x8c5303eaa26202d6

_38

_38

transaction(calls: [{String: AnyStruct}], mustPass: Bool) {

_38

_38

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_38

_38

// Borrow a reference to the EVM account that has the ability to sign transactions

_38

prepare(signer: auth(BorrowValue) & Account) {

_38

let storagePath = /storage/evm

_38

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: storagePath)

_38

?? panic("No CadenceOwnedAccount (COA) found at ".concat(storagePath.toString()))

_38

}

_38

_38

// Iterate through the list of provided EVM transactions

_38

execute {

_38

for i, call in calls {

_38

let to = call["to"] as! String

_38

let data = call["data"] as! String

_38

let gasLimit = call["gasLimit"] as! UInt64

_38

let value = call["value"] as! UInt

_38

_38

let result = self.coa.call(

_38

to: EVM.addressFromString(to),

_38

data: data.decodeHex(),

_38

gasLimit: gasLimit,

_38

value: EVM.Balance(attoflow: value)

_38

)

_38

_38

if mustPass {

_38

assert(

_38

result.status == EVM.Status.successful,

_38

message: "Call index ".concat(i.toString()).concat(" to ").concat(to)

_38

.concat(" with calldata ").concat(data).concat(" failed: ")

_38

.concat(result.errorMessage)

_38

)

_38

}

_38

}

_38

}`

In this case, it's checking that the caller of the Cadence transaction has permission to control to the EVM account, which is built in for [Cadence Owned Accounts](/build/basics/accounts). The `execute` phase then iterates through the EVM transactions and uses the Cadence accounts own permissions to sign the EVM transactions.

The loop also handles a check for the optional flag to cancel all of the transactions if any one of them fails. **In other words, you could set up a 20 transaction arbitrage attempt and unwind everything if it fails at any step!**

### EVM Child Transactions[​](#evm-child-transactions "Direct link to EVM Child Transactions")

The next two lines show the transaction hashes for the EVM transactions. You can view this in [Testnet EVM Flowscan](https://evm-testnet.flowscan.io) by searching for the transaction hashes, the same as any other.

Look up both transactions.

The first is calling the `deposit()` function to wrap FLOW and move it to EVM.

The second is calling the ERC-20 `approve()` function to give another address the authority to spend those tokens.

For the demo, the code for this is hard-coded into `src/app/page.tsx`:

`_38

const calls: EVMBatchCall[] = [

_38

{

_38

// Call deposit() function (wrap FLOW) on the token contract.

_38

address: '0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e', // Replace with your actual token contract address.

_38

abi: [

_38

{

_38

inputs: [],

_38

name: 'deposit',

_38

outputs: [],

_38

stateMutability: 'payable',

_38

type: 'function',

_38

},

_38

],

_38

functionName: 'deposit',

_38

args: [], // deposit takes no arguments; value is passed with the call.

_38

},

_38

{

_38

// Call approve() function (ERC20 style) on the same token contract.

_38

address: '0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e', // Replace with your actual token contract address if needed.

_38

abi: [

_38

{

_38

inputs: [

_38

{ name: 'spender', type: 'address' },

_38

{ name: 'value', type: 'uint256' },

_38

],

_38

name: 'approve',

_38

outputs: [{ name: '', type: 'bool' }],

_38

stateMutability: 'nonpayable',

_38

type: 'function',

_38

},

_38

],

_38

functionName: 'approve',

_38

args: [

_38

'0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2', // Spender address.

_38

BigInt('1000000000000000000'), // Approve 1 token (assuming 18 decimals).

_38

],

_38

},

_38

];`

It's called with the `useBatchTransaction` hook via the `sendBatchTransaction(calls)` function.

## Code Evaluator[​](#code-evaluator "Direct link to Code Evaluator")

The demo also has an embedded code evaluator that you can use to experiment with snippets of code from `fcl` or `wagmi`.

For example:

`_10

const user = await fcl.currentUser().snapshot();

_10

return user.addr;`

Will return your Cadence address. This snippet:

`_10

const block = await fcl.block();

_10

return block.height;`

Returns the current Cadence VM block number.

## Calling Your Own Contract[​](#calling-your-own-contract "Direct link to Calling Your Own Contract")

Next, we'll update the starter to connect to and call functions in our own contract. For this, we'll use a simple [Button Clicker Contract](https://github.com/briandoyle81/button-clicker-contract/blob/main/contracts/ClickToken.sol). You can deploy your own copy, or use the one deployed at [`0xA7Cf2260e501952c71189D04FAd17c704DFB36e6`](https://evm-testnet.flowscan.io/address/0xA7Cf2260e501952c71189D04FAd17c704DFB36e6?tab=contract).

## Set Up Contract Imports[​](#set-up-contract-imports "Direct link to Set Up Contract Imports")

info

The following steps assume deployment with Hardhat Ignition. If you are using a different deployment method, import the contract address and abi as appropriate.

In your fork of the app, add a folder called `contracts` to the `src` folder. In it, copy over ['deployed\_addresses.json`] from` ignition/deployments/chain-545`in the Button Clicker repo, and`ignition/deployments/chain-545/ClickTokenModule#ClickToken.json`.

Next, create a folder called `constants` and add a file called `contracts.ts` to it.

In it, import the contract artifact and addresses file, and create export a constant with this information.

`_10

import ClickToken from '../contracts/ClickTokenModule#ClickToken.json';

_10

import deployedAddresses from '../contracts/deployed_addresses.json';

_10

_10

export const clickToken = {

_10

abi: ClickToken.abi,

_10

address: deployedAddresses['ClickTokenModule#ClickToken'] as `0x${string}`,

_10

};`

## Build Traditional Functionality[​](#build-traditional-functionality "Direct link to Build Traditional Functionality")

This isn't a wagmi tutorial, so we'll give you some components to speed up the process. Add a folder called `components` inside `src` and add the following files.

`TheButton.tsx`

`_48

'use client';

_48

_48

import { useAccount } from 'wagmi';

_48

import { clickToken } from '../constants/contracts';

_48

_48

interface theButtonProps {

_48

// eslint-disable-next-line

_48

writeContract: Function;

_48

awaitingResponse: boolean;

_48

setAwaitingResponse: (value: boolean) => void;

_48

}

_48

_48

export default function TheButton({

_48

writeContract,

_48

awaitingResponse,

_48

setAwaitingResponse,

_48

}: theButtonProps) {

_48

const account = useAccount();

_48

_48

function handleClick() {

_48

setAwaitingResponse(true);

_48

writeContract({

_48

abi: clickToken.abi,

_48

address: clickToken.address,

_48

functionName: 'mintTo',

_48

args: [account.address],

_48

gas: 45000,

_48

});

_48

}

_48

_48

return (

_48

<>

_48

{!awaitingResponse && (

_48

<button

_48

onClick={handleClick}

_48

className="w-full py-4 px-8 text-2xl font-bold text-white bg-green-500 hover:bg-green-600 rounded-lg shadow-lg transition-transform transform active:scale-95"

_48

>

_48

Click Me!!!

_48

</button>

_48

)}

_48

{awaitingResponse && (

_48

<button className="disabled w-full py-4 px-8 text-2xl font-bold text-white bg-gray-500 rounded-lg shadow-lg">

_48

Please Wait...

_48

</button>

_48

)}

_48

</>

_48

);

_48

}`

`TopTenDisplay.tsx`

`_110

import { useAccount, useReadContract } from 'wagmi';

_110

import { clickToken } from '../constants/contracts';

_110

import { useEffect, useState } from 'react';

_110

import { useQueryClient } from '@tanstack/react-query';

_110

import { formatUnits } from 'viem';

_110

_110

type scoreBoardEntry = {

_110

user: string;

_110

value: bigint;

_110

};

_110

_110

interface TopTenDisplayProps {

_110

reloadScores: boolean;

_110

setReloadScores: (value: boolean) => void;

_110

}

_110

_110

export default function TopTenDisplay({

_110

reloadScores,

_110

setReloadScores,

_110

}: TopTenDisplayProps) {

_110

const [scores, setScores] = useState<scoreBoardEntry[]>([]);

_110

_110

const account = useAccount();

_110

const queryClient = useQueryClient();

_110

_110

const { data: scoresData, queryKey: getAllScoresQueryKey } = useReadContract({

_110

abi: clickToken.abi,

_110

address: clickToken.address as `0x${string}`,

_110

functionName: 'getAllScores',

_110

});

_110

_110

useEffect(() => {

_110

if (scoresData) {

_110

const sortedScores = scoresData as scoreBoardEntry[];

_110

// Sort scores in descending order

_110

sortedScores.sort((a, b) => Number(b.value) - Number(a.value));

_110

_110

setScores(sortedScores);

_110

}

_110

}, [scoresData]);

_110

_110

useEffect(() => {

_110

if (reloadScores) {

_110

console.log('Reloading scores...');

_110

queryClient.invalidateQueries({ queryKey: getAllScoresQueryKey });

_110

setReloadScores(false);

_110

}

_110

}, [reloadScores]);

_110

_110

function renderAddress(address: string) {

_110

return address?.slice(0, 5) + '...' + address?.slice(-3);

_110

}

_110

_110

function renderTopTen() {

_110

if (scores.length === 0 || !account) {

_110

return (

_110

<ol>

_110

<li>Loading...</li>

_110

</ol>

_110

);

_110

}

_110

// Only display the top 10 scores. If the user is in the top 10, bold the item with their score. If not, show it at the bottom with their ranking number

_110

const topTen = scores.length > 10 ? scores.slice(0, 10) : scores;

_110

// myRank is my address's position in the array of scores, +1. If it's not present, my rank is the length of the array

_110

const myRank =

_110

scores.findIndex((entry) => entry.user === account?.address) + 1 ||

_110

scores.length + 1;

_110

_110

const topTenList = topTen.map((entry, index) => {

_110

return (

_110

<li key={entry.user + index + 1}>

_110

{entry.user === account.address ? (

_110

<strong>

_110

{index + 1} -- {renderAddress(entry.user)} --{' '}

_110

{formatUnits(entry.value, 18)}

_110

</strong>

_110

) : (

_110

<>

_110

{index + 1} -- {renderAddress(entry.user)} --{' '}

_110

{formatUnits(entry.value, 18)}

_110

</>

_110

)}

_110

</li>

_110

);

_110

});

_110

_110

// Append my score if myRank is > 10

_110

if (account?.address && (myRank > 10 || myRank > scores.length)) {

_110

topTenList.push(

_110

<li key={myRank}>

_110

<strong>

_110

{myRank} -- {renderAddress(account.address.toString())} --{' '}

_110

{myRank > scores.length

_110

? 0

_110

: formatUnits(scores[myRank - 1].value, 18)}

_110

</strong>

_110

</li>,

_110

);

_110

}

_110

_110

return <ol>{topTenList}</ol>;

_110

}

_110

_110

return (

_110

<div>

_110

<h3>Top 10 Scores</h3>

_110

{renderTopTen()}

_110

</div>

_110

);

_110

}`

`Content.tsx`

`_61

'use client';

_61

_61

import { useEffect, useState } from 'react';

_61

import TopTenDisplay from './TopTenDisplay';

_61

import {

_61

useWaitForTransactionReceipt,

_61

useWriteContract,

_61

useAccount,

_61

} from 'wagmi';

_61

import TheButton from './TheButton';

_61

_61

export default function Content() {

_61

const [reload, setReload] = useState(false);

_61

const [awaitingResponse, setAwaitingResponse] = useState(false);

_61

_61

const account = useAccount();

_61

_61

const { data, writeContract, error: writeError } = useWriteContract();

_61

_61

const { data: receipt, error: receiptError } = useWaitForTransactionReceipt({

_61

hash: data,

_61

});

_61

_61

useEffect(() => {

_61

if (receipt) {

_61

console.log('Transaction receipt:', receipt);

_61

setReload(true);

_61

setAwaitingResponse(false);

_61

}

_61

}, [receipt]);

_61

_61

useEffect(() => {

_61

if (writeError) {

_61

console.error(writeError);

_61

setAwaitingResponse(false);

_61

}

_61

}, [writeError]);

_61

_61

useEffect(() => {

_61

if (receiptError) {

_61

console.error(receiptError);

_61

setAwaitingResponse(false);

_61

}

_61

}, [receiptError]);

_61

_61

return (

_61

<div className="card gap-1">

_61

{account.address && (

_61

<div className="mb-4">

_61

<TheButton

_61

writeContract={writeContract}

_61

awaitingResponse={awaitingResponse}

_61

setAwaitingResponse={setAwaitingResponse}

_61

/>

_61

</div>

_61

)}

_61

<br />

_61

{<TopTenDisplay reloadScores={reload} setReloadScores={setReload} />}

_61

</div>

_61

);

_61

}`

Then, import and add `<Content />` to `page.tsx`:

`_15

return (

_15

<>

_15

<div style={{ display: 'flex', justifyContent: 'flex-end', padding: 12 }}>

_15

<ConnectButton />

_15

</div>

_15

<h3>Flow Address: {flowAddress}</h3>

_15

<h3>EVM Address: {coa?.address}</h3>

_15

<br />

_15

<button onClick={() => sendBatchTransaction(calls)}>

_15

Send Batch Transaction Example

_15

</button>

_15

{<p>{JSON.stringify({ isPending, isError, txId, results })}</p>}

_15

<Content />

_15

</>

_15

);`

You'll now see the button and scoreboard from the contract. Test it out and earn a few points!

![scores](data:image/png;base64,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)

## Supercharge your EVM App With Cadence[​](#supercharge-your-evm-app-with-cadence "Direct link to Supercharge your EVM App With Cadence")

Now let's supercharge it. With the power of Cadence, you can use multi-call write and give your users way more tokens with a single click and single signature!

For the first pass, we'll skip some organization best practices.

Import `clickToken` into `page.tsx` and update `calls` to instead call the `mint` function from the Button Clicker contract.

`_10

const calls: EVMBatchCall[] = [

_10

{

_10

address: clickToken.address,

_10

abi: clickToken.abi as Abi,

_10

functionName: 'mintTo',

_10

args: [coa?.address],

_10

},

_10

];`

Try clicking the `Send Batch Transaction Example` button again. You'll have to **manually refresh** the page when the EVM transaction hash appears to see the score update. We haven't wired in the query invalidation yet.

Next, use some JavaScript to put 10 copies of the transaction call into the array:

`_10

const calls: EVMBatchCall[] = Array.from({ length: 10 }, () => ({

_10

address: clickToken.address,

_10

abi: clickToken.abi as Abi,

_10

functionName: 'mintTo',

_10

args: [coa?.address],

_10

}));`

Click the button again and **manually** refresh page once the transaction hashes appear.

**You just minted 10 tokens from 10 transactions with one signature!**

## Improve the UI/UX[​](#improve-the-uiux "Direct link to Improve the UI/UX")

While we've got the batched transactions feature working, we've got a few flaws in the user experience that we'll need to resolve, and we should make this a bit nicer looking.

### Install Tailwind[​](#install-tailwind "Direct link to Install Tailwind")

warning

We initially tried getting an AI friend to install this for us and it got very confused. Next.js and Tailwind have both had a lot of change recently. As a result, the LLMs don't seem to have caught up just yet.

Do this part the old-fashioned way.

The components we borrowed already use [Tailwind](https://tailwindcss.com/), so install it:

`_10

npm install tailwindcss @tailwindcss/postcss postcss`

Then, in the root of the project, add `postcss.config.mjs` and add:

`_10

const config = {

_10

plugins: {

_10

'@tailwindcss/postcss': {},

_10

},

_10

};

_10

export default config;`

Then, add the following to the top of `src/styles/global.css`:

`_10

@import 'tailwindcss';`

Run the app and make sure you see some styling. It won't look nice yet. We'll help you reorganize the components and hook up state monitoring, but it will be up to you to style the app how you'd like. You can check out the [reference repo](https://github.com/briandoyle81/cross-vm-app-1/tree/main) for inspiration, but it's far from perfect or beautiful.

### Update State Display[​](#update-state-display "Direct link to Update State Display")

The first thing we'll need to fix is that the user has to refresh the window manually to see the results of the batched transaction in the scoreboard. Start by moving the functionality in `page.tsx` into a new component, called `SuperButton.tsx`. Note that we're mimicking the pattern in `TheButton.tsx` where the blockchain state is managed in `Content.tsx` and we're passing in the relevant information and functions as props:

`_76

'use client';

_76

_76

import { useAccount } from 'wagmi';

_76

import { clickToken } from '../constants/contracts';

_76

import { CallOutcome, EVMBatchCall } from '../hooks/useBatchTransaction';

_76

import { Abi } from 'viem';

_76

_76

interface SuperButtonProps {

_76

flowAddress: string | null;

_76

awaitingResponse: boolean;

_76

setAwaitingResponse: (value: boolean) => void;

_76

sendBatchTransaction: (calls: EVMBatchCall[]) => void;

_76

isPending: boolean;

_76

isError: boolean;

_76

txId: string;

_76

results: CallOutcome[];

_76

}

_76

_76

export default function SuperButton({

_76

flowAddress,

_76

awaitingResponse,

_76

setAwaitingResponse,

_76

sendBatchTransaction,

_76

isPending,

_76

isError,

_76

txId,

_76

results,

_76

}: SuperButtonProps) {

_76

const account = useAccount();

_76

_76

const calls: EVMBatchCall[] = Array.from({ length: 10 }, () => ({

_76

address: clickToken.address,

_76

abi: clickToken.abi as Abi,

_76

functionName: 'mintTo',

_76

args: [account?.address],

_76

}));

_76

_76

function handleClick() {

_76

setAwaitingResponse(true);

_76

sendBatchTransaction(calls);

_76

}

_76

_76

return (

_76

<div className="bg-blue-500 text-white p-4 m-4 rounded">

_76

<div>

_76

With the{' '}

_76

<a

_76

href="https://wallet.flow.com/"

_76

target="_blank"

_76

rel="noopener noreferrer"

_76

>

_76

Flow Wallet

_76

</a>

_76

, you can sign 10 mint transactions at once!

_76

</div>

_76

{!awaitingResponse && (

_76

<button

_76

disabled={!flowAddress}

_76

onClick={handleClick}

_76

className="w-full py-4 px-8 text-2xl font-bold text-white bg-blue-600 hover:bg-blue-700 rounded-lg shadow-lg transition-transform transform active:scale-95 disabled:bg-gray-400 disabled:cursor-not-allowed"

_76

>

_76

{flowAddress ? 'Mint 10 at Once!' : 'Requires Flow Wallet'}

_76

</button>

_76

)}

_76

{awaitingResponse && (

_76

<button

_76

className="w-full py-4 px-8 text-2xl font-bold text-white bg-gray-500 rounded-lg shadow-lg disabled:cursor-not-allowed"

_76

disabled

_76

>

_76

Please Wait...

_76

</button>

_76

)}

_76

{<p>{JSON.stringify({ isPending, isError, txId, results })}</p>}

_76

</div>

_76

);

_76

}`

You should end up with a vastly simplified `page.tsx`:

`_11

import Content from '../components/Content';

_11

_11

function Page() {

_11

return (

_11

<>

_11

<Content />

_11

</>

_11

);

_11

}

_11

_11

export default Page;`

Next, update `Content.tsx`. First, add the decomposition of the `useBatchTransactions` hook that used to be in `page.tsx`. You'll keep blockchain-state-related code here, in a similar pattern to `useWriteTransaction`.

`_10

import { useBatchTransaction } from '../hooks/useBatchTransaction';`

`_10

const { sendBatchTransaction, isPending, isError, txId, results } =

_10

useBatchTransaction();`

You'll also need to move the `useEffect` that subscribes to the current user on the Cadence side:

`_10

useEffect(() => {

_10

const unsub = fcl.currentUser().subscribe((user: CurrentUser) => {

_10

setFlowAddress(user.addr ?? null);

_10

});

_10

return () => unsub();

_10

}, []);`

Then, update the `useEffect` that waits for a `receipt` to also trigger if `results` is updated with the result of a batched transaction:

`_10

useEffect(() => {

_10

if (receipt || results.length > 0) {

_10

console.log('Transaction receipt:', receipt);

_10

setReload(true);

_10

setAwaitingResponse(false);

_10

}

_10

}, [receipt, results]);`

Finally, reorganize the `return` into two side-by-side cards and put the new component in the right card:

`_35

return (

_35

<div>

_35

<div className="flex justify-end p-3">

_35

<ConnectButton />

_35

</div>

_35

<h3>Flow Address: {flowAddress}</h3>

_35

<h3>EVM Address: {account?.address}</h3>

_35

<br />

_35

<div className="flex flex-row items-center justify-center">

_35

<div className="bg-green-500 text-white p-4 m-4 rounded">

_35

{account.address && (

_35

<div className="mb-4">

_35

<TheButton

_35

writeContract={writeContract}

_35

awaitingResponse={awaitingResponse}

_35

setAwaitingResponse={setAwaitingResponse}

_35

/>

_35

</div>

_35

)}

_35

<br />

_35

</div>

_35

<SuperButton

_35

flowAddress={flowAddress}

_35

awaitingResponse={awaitingResponse}

_35

setAwaitingResponse={setAwaitingResponse}

_35

sendBatchTransaction={sendBatchTransaction}

_35

isPending={isPending}

_35

isError={isError}

_35

txId={txId}

_35

results={results}

_35

/>

_35

</div>

_35

{<TopTenDisplay reloadScores={reload} setReloadScores={setReload} />}

_35

</div>

_35

);`

### Testing[​](#testing "Direct link to Testing")

Run the app and make sure it's working as expected, even if in a rather ugly fashion.

### Add UI Hints[​](#add-ui-hints "Direct link to Add UI Hints")

With this kind of app, you're likely to have two types of users. Those that have upgraded to the [Flow Wallet] can take advantage of advanced features such as batched transactions, and those who haven't cannot.

It's up to you do design a comprehensive strategy for your app, but here, we can at least let users know what's going on. Add some explainer text, and configure the button to show an appropriate message and disable itself if the wallet won't support it.

`_10

<div>

_10

With the <a href="https://flow.com/wallet" target="_blank" rel="noopener noreferrer">Flow Wallet</a>, you can sign 10 mint transactions at once!

_10

</div>

_10

<button disabled={!flowAddress} onClick={() => sendBatchTransaction(calls)}>

_10

{flowAddress ? 'Mint 10 at Once!' : 'Requires Flow Wallet'}

_10

</button>`

### Styling[​](#styling "Direct link to Styling")

It's up to you to make the app pretty. If you need inspiration, you can always check the [reference repo](https://github.com/briandoyle81/cross-vm-app-1/tree/main).

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you reviewed the demo starter for building hybrid applications that utilize a common EVM stack and integrate with Flow Cadence. You then added functionality to interface with another contract that mints ERC-20 tokens. Finally, you supercharged your app by using the power of Cadence for EVM multi-call contract writes.

Now that you have completed the tutorial, you should be able to:

* Build an app that seamlessly integrates Flow Cadence and Flow EVM connections
* Add Cadence features to your [Rainbowkit](https://www.rainbowkit.com/)/[wagmi](https://wagmi.sh/)/[viem](https://viem.sh/) app
* Utilize [Flow Client Library (FCL)](/tools/clients/fcl-js) to enable multi-call contract writes to Flow EVM

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/cross-vm-apps/introduction.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

Cross-VM Apps](/tutorials/cross-vm-apps)[Next

Update Existing wagmi App](/tutorials/cross-vm-apps/add-to-wagmi)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
  + [Next.js and Modern Frontend Development](#nextjs-and-modern-frontend-development)
  + [Solidity and Cadence Smart Contract Development](#solidity-and-cadence-smart-contract-development)
  + [Onchain App Frontends](#onchain-app-frontends)
* [Getting Started](#getting-started)
* [Project Overview](#project-overview)
* [Send Batch Transactions](#send-batch-transactions)
  + [Cadence Parent Transaction](#cadence-parent-transaction)
  + [EVM Child Transactions](#evm-child-transactions)
* [Code Evaluator](#code-evaluator)
* [Calling Your Own Contract](#calling-your-own-contract)
* [Set Up Contract Imports](#set-up-contract-imports)
* [Build Traditional Functionality](#build-traditional-functionality)
* [Supercharge your EVM App With Cadence](#supercharge-your-evm-app-with-cadence)
* [Improve the UI/UX](#improve-the-uiux)
  + [Install Tailwind](#install-tailwind)
  + [Update State Display](#update-state-display)
  + [Testing](#testing)
  + [Add UI Hints](#add-ui-hints)
  + [Styling](#styling)
* [Conclusion](#conclusion)

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