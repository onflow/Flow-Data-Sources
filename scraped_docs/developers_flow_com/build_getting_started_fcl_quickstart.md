# Source: https://developers.flow.com/build/getting-started/fcl-quickstart

Building a Simple Frontend with "@onflow/kit" | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)

  + [Contract Interaction](/build/getting-started/contract-interaction)
  + [Local Development](/build/getting-started/flow-cli)
  + [Simple Frontend](/build/getting-started/fcl-quickstart)
* [Flow Protocol](/build/basics/network-architecture)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Getting Started
* Simple Frontend

On this page

# Simple Frontend with `@onflow/kit`

Building on the `Counter` contract you deployed in [Step 1: Contract Interaction](/build/getting-started/contract-interaction) and [Step 2: Local Development](/build/getting-started/flow-cli), this tutorial shows you how to create a simple Next.js frontend that interacts with the `Counter` smart contract deployed on your local Flow emulator. Instead of using FCL directly, you'll leverage [**@onflow/kit**](/tools/kit) to simplify authentication, querying, transactions, and to display real-time transaction status updates using convenient React hooks.

## Objectives[​](#objectives "Direct link to Objectives")

After finishing this guide, you will be able to:

* Wrap your Next.js app with a Flow provider using [**@onflow/kit**](/tools/kit).
* Read data from a Cadence smart contract (`Counter`) using kit's query hook.
* Send a transaction to update the smart contract's state using kit's mutation hook.
* Monitor a transaction's status in real time using kit's transaction hook.
* Authenticate with the Flow blockchain using kit's built-in hooks and the local [Dev Wallet](/tools/flow-dev-wallet).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Completion of [Step 1: Contract Interaction](/build/getting-started/contract-interaction) and [Step 2: Local Development](/build/getting-started/flow-cli).
* [Flow CLI](/tools/flow-cli/install) installed.
* Node.js and npm installed.

## Setting Up the Next.js App[​](#setting-up-the-nextjs-app "Direct link to Setting Up the Next.js App")

Follow these steps to set up your Next.js project and integrate [**@onflow/kit**](/tools/kit).

### Step 1: Create a New Next.js App[​](#step-1-create-a-new-nextjs-app "Direct link to Step 1: Create a New Next.js App")

Run the following command in your project directory:

`_10

npx create-next-app@latest kit-app-quickstart`

During setup, choose the following options:

* **Use TypeScript**: **Yes**
* **Use src directory**: **Yes**
* **Use App Router**: **Yes**

This command creates a new Next.js project named `kit-app-quickstart` inside your current directory. We're generating the frontend in a subdirectory so we can next move it into our existing project structure from the previous steps (you can't create an app in a non-empty directory).

### Step 2: Move the Next.js App Up a Directory[​](#step-2-move-the-nextjs-app-up-a-directory "Direct link to Step 2: Move the Next.js App Up a Directory")

Move the contents of the `kit-app-quickstart` directory into your project root. You can use the gui in your editor, or the console.

warning

You'll want to consolidate both `.gitignore` files, keeping the contents of both in the file that ends up in the root.

On macOS/Linux:

`_10

mv kit-app-quickstart/* .

_10

mv kit-app-quickstart/.* . # To move hidden files (e.g. .env.local)

_10

rm -r kit-app-quickstart`

On Windows (PowerShell):

`_10

Move-Item -Path .\kit-app-quickstart\* -Destination . -Force

_10

Move-Item -Path .\kit-app-quickstart\.* -Destination . -Force

_10

Remove-Item -Recurse -Force .\kit-app-quickstart`

**Note:** When moving hidden files (those beginning with a dot) like `.gitignore`, be cautious not to overwrite any important files.

### Step 3: Install @onflow/kit[​](#step-3-install-onflowkit "Direct link to Step 3: Install @onflow/kit")

Install the kit library in your project:

`_10

npm install @onflow/kit`

This library wraps FCL internally and exposes a set of hooks for authentication, querying, sending transactions, and tracking transaction status.

## Configuring the Local Flow Emulator and Dev Wallet[​](#configuring-the-local-flow-emulator-and-dev-wallet "Direct link to Configuring the Local Flow Emulator and Dev Wallet")

warning

You should already have the Flow emulator running from the local development step. If it's not running, you can start it again — but note that restarting the emulator will clear all blockchain state, including any contracts deployed in [Step 2: Local Development](/build/getting-started/flow-cli).

### Start the Flow Emulator (if not already running)[​](#start-the-flow-emulator-if-not-already-running "Direct link to Start the Flow Emulator (if not already running)")

Open a new terminal window in your project directory and run:

`_10

flow emulator start`

This will start the Flow emulator on `http://localhost:8888`. Make sure to keep it running in a separate terminal.

### Start the Dev Wallet[​](#start-the-dev-wallet "Direct link to Start the Dev Wallet")

In another terminal window, run:

`_10

flow dev-wallet`

This will start the [Dev Wallet](/tools/flow-dev-wallet) on `http://localhost:8701`, which you'll use for authentication during development.

## Wrapping Your App with FlowProvider[​](#wrapping-your-app-with-flowprovider "Direct link to Wrapping Your App with FlowProvider")

[**@onflow/kit**](/tools/kit) provides a `FlowProvider` component that sets up the Flow Client Library configuration. In Next.js using the App Router, add or update your `src/app/layout.tsx` as follows:

`_28

// src/app/layout.tsx

_28

'use client';

_28

_28

import { FlowProvider } from '@onflow/kit';

_28

import flowJSON from '../../flow.json';

_28

_28

export default function RootLayout({

_28

children,

_28

}: {

_28

children: React.ReactNode;

_28

}) {

_28

return (

_28

<html>

_28

<body>

_28

<FlowProvider

_28

config={{

_28

accessNodeUrl: 'http://localhost:8888',

_28

flowNetwork: 'emulator',

_28

discoveryWallet: 'https://fcl-discovery.onflow.org/emulator/authn',

_28

}}

_28

flowJson={flowJSON}

_28

>

_28

{children}

_28

</FlowProvider>

_28

</body>

_28

</html>

_28

);

_28

}`

This configuration initializes the kit with your local emulator settings and maps contract addresses based on your `flow.json` file.

For more information on Discovery configurations, refer to the [Wallet Discovery Guide](/tools/clients/fcl-js/discovery).

## Interacting With the Chain[​](#interacting-with-the-chain "Direct link to Interacting With the Chain")

Now that we've set our provider, lets start interacting with the chain.

### Querying the Chain[​](#querying-the-chain "Direct link to Querying the Chain")

First, use the kit's [`useFlowQuery`](/tools/kit#useflowquery) hook to read the current counter value from the blockchain.

`_18

import { useFlowQuery } from '@onflow/kit';

_18

_18

const { data, isLoading, error, refetch } = useFlowQuery({

_18

cadence: `

_18

import "Counter"

_18

import "NumberFormatter"

_18

_18

access(all)

_18

fun main(): String {

_18

let count: Int = Counter.getCount()

_18

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_18

return formattedCount

_18

}

_18

`,

_18

enabled: true,

_18

});

_18

_18

// Use the count data in your component as needed.`

This script fetches the counter value, formats it via the `NumberFormatter`, and returns the formatted string.

info

* **Import Syntax:** The imports (`import "Counter"` and `import "NumberFormatter"`) don't include addresses because those are automatically resolved using the `flow.json` file configured in your `FlowProvider`. This keeps your Cadence scripts portable and environment-independent.
* **`enabled` Flag:** This controls whether the query should run automatically. Set it to `true` to run on mount, or pass a condition (e.g. `!!user?.addr`) to delay execution until the user is available. This is useful for queries that depend on authentication or other asynchronous data.

### Sending a Transaction[​](#sending-a-transaction "Direct link to Sending a Transaction")

Next, use the kit's [`useFlowMutate`](/tools/kit#useflowmutate) hook to send a transaction that increments the counter.

`_27

import { useFlowMutate } from '@onflow/kit';

_27

_27

const {

_27

mutate: increment,

_27

isPending: txPending,

_27

data: txId,

_27

error: txError,

_27

} = useFlowMutate();

_27

_27

const handleIncrement = () => {

_27

increment({

_27

cadence: `

_27

import "Counter"

_27

_27

transaction {

_27

prepare(acct: &Account) {

_27

// Authorization handled via wallet

_27

}

_27

execute {

_27

Counter.increment()

_27

let newCount = Counter.getCount()

_27

log("New count after incrementing: ".concat(newCount.toString()))

_27

}

_27

}

_27

`,

_27

});

_27

};`

#### Explanation[​](#explanation "Direct link to Explanation")

This sends a Cadence transaction to the blockchain using the `mutate` function. The transaction imports the `Counter` contract and calls its `increment` function. Authorization is handled automatically by the connected wallet during the `prepare` phase. Once submitted, the returned `txId` can be used to track the transaction's status in real time.

### Subscribing to Transaction Status[​](#subscribing-to-transaction-status "Direct link to Subscribing to Transaction Status")

Use the kit's [`useFlowTransaction`] hook to monitor and display the transaction status in real time.

`_11

const { transactionStatus, error: txStatusError } = useFlowTransaction(

_11

txId || '',

_11

);

_11

_11

useEffect(() => {

_11

if (txId && transactionStatus?.status === 3) {

_11

refetch();

_11

}

_11

}, [transactionStatus?.status, txId, refetch]);

_11

_11

// You can then use transactionStatus (for example, its statusString) to show updates.`

#### Explanation:[​](#explanation-1 "Direct link to Explanation:")

* `useFlowTransaction(txId)` subscribes to real-time updates about a transaction's lifecycle using the transaction ID.
* `transactionStatus.status` is a numeric code representing the state of the transaction:
  + `0`: **Unknown** – The transaction status is not yet known.
  + `1`: **Pending** – The transaction has been submitted and is waiting to be included in a block.
  + `2`: **Finalized** – The transaction has been included in a block, but not yet executed.
  + `3`: **Executed** – The transaction code has run successfully, but the result has not yet been sealed.
  + `4`: **Sealed** – The transaction is fully complete, included in a block, and now immutable on-chain.
* We recommend calling `refetch()` when the status reaches **3 (Executed)** to update your UI more quickly after the transaction runs, rather than waiting for sealing.
* The `statusString` property gives a human-readable version of the current status you can display in the UI.

#### Why `Executed` is Recommended for UI Updates:[​](#why-executed-is-recommended-for-ui-updates "Direct link to why-executed-is-recommended-for-ui-updates")

Waiting for `Sealed` provides full on-chain confirmation but can introduce a delay — especially in local or test environments. Since most transactions (like incrementing a counter) don't require strong finality guarantees, you can typically refetch data once the transaction reaches `Executed` for a faster, more responsive user experience.

However:

* If you're dealing with critical state changes (e.g., token transfers or contract deployments), prefer waiting for `Sealed`.
* For non-critical UI updates, `Executed` is usually safe and significantly improves perceived performance.

### Integrating Authentication and Building the Complete UI[​](#integrating-authentication-and-building-the-complete-ui "Direct link to Integrating Authentication and Building the Complete UI")

Finally, integrate the query, mutation, and transaction status hooks with authentication using `useCurrentFlowUser`. Combine all parts to build the complete page.

`_114

// src/app/page.js

_114

_114

"use client";

_114

_114

import { useState, useEffect } from "react";

_114

import {

_114

useFlowQuery,

_114

useFlowMutate,

_114

useFlowTransaction,

_114

useCurrentFlowUser,

_114

} from "@onflow/kit";

_114

_114

export default function Home() {

_114

const { user, authenticate, unauthenticate } = useCurrentFlowUser();

_114

const [lastTxId, setLastTxId] = useState<string>();

_114

_114

const { data, isLoading, error, refetch } = useFlowQuery({

_114

cadence: `

_114

import "Counter"

_114

import "NumberFormatter"

_114

_114

access(all)

_114

fun main(): String {

_114

let count: Int = Counter.getCount()

_114

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_114

return formattedCount

_114

}

_114

`,

_114

enabled: true,

_114

});

_114

_114

const {

_114

mutate: increment,

_114

isPending: txPending,

_114

data: txId,

_114

error: txError,

_114

} = useFlowMutate();

_114

_114

const { transactionStatus, error: txStatusError } = useFlowTransaction(

_114

txId || "",

_114

);

_114

_114

useEffect(() => {

_114

if (txId && transactionStatus?.status === 4) {

_114

refetch();

_114

}

_114

}, [transactionStatus?.status, txId, refetch]);

_114

_114

const handleIncrement = () => {

_114

increment({

_114

cadence: `

_114

import "Counter"

_114

_114

transaction {

_114

prepare(acct: &Account) {

_114

// Authorization handled via wallet

_114

}

_114

execute {

_114

Counter.increment()

_114

let newCount = Counter.getCount()

_114

log("New count after incrementing: ".concat(newCount.toString()))

_114

}

_114

}

_114

`,

_114

});

_114

};

_114

_114

return (

_114

<div>

_114

<h1>@onflow/kit App Quickstart</h1>

_114

_114

{isLoading ? (

_114

<p>Loading count...</p>

_114

) : error ? (

_114

<p>Error fetching count: {error.message}</p>

_114

) : (

_114

<div>

_114

<h2>Count: {data as string}</h2>

_114

</div>

_114

)}

_114

_114

{user.loggedIn ? (

_114

<div>

_114

<p>Address: {user.addr}</p>

_114

<button onClick={unauthenticate}>Log Out</button>

_114

<button onClick={handleIncrement} disabled={txPending}>

_114

{txPending ? "Processing..." : "Increment Count"}

_114

</button>

_114

_114

<div>

_114

Latest Transaction Status:{" "}

_114

{transactionStatus?.statusString || "No transaction yet"}

_114

</div>

_114

_114

{txError && <p>Error sending transaction: {txError.message}</p>}

_114

_114

{lastTxId && (

_114

<div>

_114

<h3>Transaction Status</h3>

_114

{transactionStatus ? (

_114

<p>Status: {transactionStatus.statusString}</p>

_114

) : (

_114

<p>Waiting for status update...</p>

_114

)}

_114

{txStatusError && <p>Error: {txStatusError.message}</p>}

_114

</div>

_114

)}

_114

</div>

_114

) : (

_114

<button onClick={authenticate}>Log In</button>

_114

)}

_114

</div>

_114

);

_114

}`

In this complete page:

* **Step 1** queries the counter value.
* **Step 2** sends a transaction to increment the counter and stores the transaction ID.
* **Step 3** subscribes to transaction status updates using the stored transaction ID and uses a `useEffect` hook to automatically refetch the updated count when the transaction is sealed (status code 4).
* **Step 4** integrates authentication via `useCurrentFlowUser` and combines all the pieces into a single user interface.

tip

In this tutorial, we inlined Cadence code for simplicity. For real projects, we recommend storing Cadence in separate `.cdc` files, using the [Cadence VSCode extension](/tools/vscode-extension), and importing them with the [`flow-cadence-plugin`](https://github.com/chasefleming/flow-cadence-plugin) for Next.js or Webpack projects.

## Running the App[​](#running-the-app "Direct link to Running the App")

Start your development server:

`_10

npm run dev`

warning

If you have the Flow wallet browser extension installed, you might automatically log into the app. Normally this is desirable for your users, but you don't want to use it here.

Log out, and log back in selecting the Dev Wallet instead of the Flow Wallet.

Then visit <http://localhost:3000> in your browser. You should see:

* The current counter value displayed (formatted with commas using `NumberFormatter`).
* A **Log In** button that launches the kit Discovery UI with your local [Dev Wallet](/tools/flow-dev-wallet).
* Once logged in, your account address appears with options to **Log Out** and **Increment Count**.
* When you click **Increment Count**, the transaction is sent; its status updates are displayed in real time below the action buttons, and once the transaction is sealed, the updated count is automatically fetched.

## Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up")

By following these steps, you've built a simple Next.js dApp that interacts with a Flow smart contract using [**@onflow/kit**](/tools/kit). In this guide you learned how to:

* Wrap your application in a `FlowProvider` to configure blockchain connectivity.
* Use kit hooks such as `useFlowQuery`, `useFlowMutate`, `useFlowTransaction`, and `useCurrentFlowUser` to manage authentication, query on-chain data, submit transactions, and monitor their status.
* Integrate with the local Flow emulator and Dev Wallet for a fully functional development setup.

For additional details and advanced usage, refer to the [@onflow/kit documentation](/tools/kit) and other Flow developer resources.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/getting-started/fcl-quickstart.md)

Last updated on **Apr 18, 2025** by **Brian Doyle**

[Previous

Local Development](/build/getting-started/flow-cli)[Next

Network Architecture ↗️](/build/basics/network-architecture)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
* [Setting Up the Next.js App](#setting-up-the-nextjs-app)
  + [Step 1: Create a New Next.js App](#step-1-create-a-new-nextjs-app)
  + [Step 2: Move the Next.js App Up a Directory](#step-2-move-the-nextjs-app-up-a-directory)
  + [Step 3: Install @onflow/kit](#step-3-install-onflowkit)
* [Configuring the Local Flow Emulator and Dev Wallet](#configuring-the-local-flow-emulator-and-dev-wallet)
  + [Start the Flow Emulator (if not already running)](#start-the-flow-emulator-if-not-already-running)
  + [Start the Dev Wallet](#start-the-dev-wallet)
* [Wrapping Your App with FlowProvider](#wrapping-your-app-with-flowprovider)
* [Interacting With the Chain](#interacting-with-the-chain)
  + [Querying the Chain](#querying-the-chain)
  + [Sending a Transaction](#sending-a-transaction)
  + [Subscribing to Transaction Status](#subscribing-to-transaction-status)
  + [Integrating Authentication and Building the Complete UI](#integrating-authentication-and-building-the-complete-ui)
* [Running the App](#running-the-app)
* [Wrapping Up](#wrapping-up)

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