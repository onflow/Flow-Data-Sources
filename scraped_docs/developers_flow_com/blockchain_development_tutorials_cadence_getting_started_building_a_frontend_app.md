# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app

Building a Frontend App | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Forte Network Upgrade](/blockchain-development-tutorials/forte)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

  + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

    - [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)
    - [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
    - [Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)
    - [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)
  + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)
  + [Account Linking](/blockchain-development-tutorials/cadence/account-management)
  + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)
* Building a Frontend App

On this page

# Building a Frontend App

Building on the `Counter` contract you deployed in [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup) and [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction), this tutorial shows you how to create a simple Next.js frontend that interacts with the `Counter` smart contract deployed on your local Flow emulator. Instead of using FCL directly, you'll leverage [**@onflow/react-sdk**](/build/tools/react-sdk) to simplify authentication, querying, transactions, and to display real-time transaction status updates using convenient React hooks.

## Objectives[​](#objectives "Direct link to Objectives")

After finishing this guide, you will be able to:

* Wrap your Next.js app with a Flow provider using [**@onflow/react-sdk**](/build/tools/react-sdk).
* Read data from a Cadence smart contract (`Counter`) using kit's query hook.
* Send a transaction to update the smart contract's state using kit's mutation hook.
* Monitor a transaction's status in real time using kit's transaction hook.
* Authenticate with the Flow blockchain using kit's built-in hooks and the local [Dev Wallet](/build/tools/flow-dev-wallet).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Completion of [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup) and [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction).
* [Flow CLI](/build/tools/flow-cli/install) installed.
* Node.js and npm installed.

## Setting Up the Next.js App[​](#setting-up-the-nextjs-app "Direct link to Setting Up the Next.js App")

Follow these steps to set up your Next.js project and integrate [**@onflow/react-sdk**](/build/tools/react-sdk).

tip

You can visit this [React-sdk Demo](https://react-sdk-demo-git-master-onflow.vercel.app/) to see how the hooks and components are used.

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

### Step 3: Install @onflow/react-sdk[​](#step-3-install-onflowreact-sdk "Direct link to Step 3: Install @onflow/react-sdk")

Install the kit library in your project:

`_10

npm install @onflow/react-sdk`

This library wraps FCL internally and exposes a set of hooks for authentication, querying, sending transactions, and tracking transaction status.

## Configuring the Local Flow Emulator and Dev Wallet[​](#configuring-the-local-flow-emulator-and-dev-wallet "Direct link to Configuring the Local Flow Emulator and Dev Wallet")

warning

You should already have the Flow emulator running from the local development step. If it's not running, you can start it again — but note that restarting the emulator will clear all blockchain state, including any contracts deployed in [Step 2: Local Development].

### Start the Flow Emulator (if not already running)[​](#start-the-flow-emulator-if-not-already-running "Direct link to Start the Flow Emulator (if not already running)")

Open a new terminal window in your project directory and run:

`_10

flow emulator start`

This will start the Flow emulator on `http://localhost:8888`. Make sure to keep it running in a separate terminal.

### Start the Dev Wallet[​](#start-the-dev-wallet "Direct link to Start the Dev Wallet")

In another terminal window, run:

`_10

flow dev-wallet`

This will start the [Dev Wallet](/build/tools/flow-dev-wallet) on `http://localhost:8701`, which you'll use for authentication during development.

## Wrapping Your App with FlowProvider[​](#wrapping-your-app-with-flowprovider "Direct link to Wrapping Your App with FlowProvider")

[**@onflow/react-sdk**](/build/tools/react-sdk) provides a `FlowProvider` component that sets up the Flow Client Library configuration. In Next.js using the App Router, add or update your `src/app/layout.tsx` as follows:

`_27

'use client';

_27

_27

import { FlowProvider } from '@onflow/react-sdk';

_27

import flowJson from '../flow.json';

_27

_27

export default function RootLayout({

_27

children,

_27

}: {

_27

children: React.ReactNode;

_27

}) {

_27

return (

_27

<html>

_27

<body>

_27

<FlowProvider

_27

config={{

_27

accessNodeUrl: 'http://localhost:8888',

_27

flowNetwork: 'emulator',

_27

discoveryWallet: 'https://fcl-discovery.onflow.org/emulator/authn',

_27

}}

_27

flowJson={flowJson}

_27

>

_27

{children}

_27

</FlowProvider>

_27

</body>

_27

</html>

_27

);

_27

}`

This configuration initializes the kit with your local emulator settings and maps contract addresses based on your `flow.json` file.

For more information on Discovery configurations, refer to the [Wallet Discovery Guide](/build/tools/clients/fcl-js/discovery).

## Interacting With the Chain[​](#interacting-with-the-chain "Direct link to Interacting With the Chain")

Now that we've set our provider, lets start interacting with the chain.

### Querying the Chain[​](#querying-the-chain "Direct link to Querying the Chain")

First, use the kit's [`useFlowQuery`](/build/tools/react-sdk#useflowquery) hook to read the current counter value from the blockchain.

`` _18

import { useFlowQuery } from '@onflow/react-sdk';

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

query: { enabled: true },

_18

});

_18

_18

// Use the count data in your component as needed. ``

This script fetches the counter value, formats it via the `NumberFormatter`, and returns the formatted string.

info

* **Import Syntax:** The imports (`import "Counter"` and `import "NumberFormatter"`) don't include addresses because those are automatically resolved using the `flow.json` file configured in your `FlowProvider`. This keeps your Cadence scripts portable and environment-independent.
* **`enabled` Flag:** This controls whether the query should run automatically. Set it to `true` to run on mount, or pass a condition (e.g. `!!user?.addr`) to delay execution until the user is available. This is useful for queries that depend on authentication or other asynchronous data.

### Sending a Transaction[​](#sending-a-transaction "Direct link to Sending a Transaction")

Next, use the kit's [`useFlowMutate`](/build/tools/react-sdk#useflowmutate) hook to send a transaction that increments the counter.

`` _27

import { useFlowMutate } from '@onflow/react-sdk';

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

}; ``

#### Explanation[​](#explanation "Direct link to Explanation")

This sends a Cadence transaction to the blockchain using the `mutate` function. The transaction imports the `Counter` contract and calls its `increment` function. Authorization is handled automatically by the connected wallet during the `prepare` phase. Once submitted, the returned `txId` can be used to track the transaction's status in real time.

### Subscribing to Transaction Status[​](#subscribing-to-transaction-status "Direct link to Subscribing to Transaction Status")

Use the kit's [`useFlowTransactionStatus`] hook to monitor and display the transaction status in real time.

`_13

import { useFlowTransactionStatus } from '@onflow/react-sdk';

_13

_13

const { transactionStatus, error: txStatusError } = useFlowTransactionStatus({

_13

id: txId || '',

_13

});

_13

_13

useEffect(() => {

_13

if (txId && transactionStatus?.status === 3) {

_13

refetch();

_13

}

_13

}, [transactionStatus?.status, txId, refetch]);

_13

_13

// You can then use transactionStatus (for example, its statusString) to show updates.`

#### Explanation:[​](#explanation-1 "Direct link to Explanation:")

* `useFlowTransactionStatus(txId)` subscribes to real-time updates about a transaction's lifecycle using the transaction ID.
* `transactionStatus.status` is a numeric code representing the state of the transaction:
  + `0`: **Unknown** – The transaction status is not yet known.
  + `1`: **Pending** – The transaction has been submitted and is waiting to be included in a block.
  + `2`: **Finalized** – The transaction has been included in a block, but not yet executed.
  + `3`: **Executed** – The transaction code has run successfully, but the result has not yet been sealed.
  + `4`: **Sealed** – The transaction is fully complete, included in a block, and now immutable onchain.
* We recommend calling `refetch()` when the status reaches **3 (Executed)** to update your UI more quickly after the transaction runs, rather than waiting for sealing.
* The `statusString` property gives a human-readable version of the current status you can display in the UI.

#### Why `Executed` is Recommended for UI Updates:[​](#why-executed-is-recommended-for-ui-updates "Direct link to why-executed-is-recommended-for-ui-updates")

Waiting for `Sealed` provides full onchain confirmation but can introduce a delay — especially in local or test environments. Since most transactions (like incrementing a counter) don't require strong finality guarantees, you can typically refetch data once the transaction reaches `Executed` for a faster, more responsive user experience.

However:

* If you're dealing with critical state changes (e.g., token transfers or contract deployments), prefer waiting for `Sealed`.
* For non-critical UI updates, `Executed` is usually safe and significantly improves perceived performance.

### Integrating Authentication and Building the Complete UI[​](#integrating-authentication-and-building-the-complete-ui "Direct link to Integrating Authentication and Building the Complete UI")

Finally, integrate the query, mutation, and transaction status hooks with authentication using `useFlowCurrentUser`. Combine all parts to build the complete page.

`` _106

'use client';

_106

_106

import { useState, useEffect } from 'react';

_106

import {

_106

useFlowQuery,

_106

useFlowMutate,

_106

useFlowTransactionStatus,

_106

useFlowCurrentUser,

_106

} from '@onflow/react-sdk';

_106

_106

export default function Home() {

_106

const { user, authenticate, unauthenticate } = useFlowCurrentUser();

_106

_106

const { data, isLoading, error, refetch } = useFlowQuery({

_106

cadence: `

_106

import "Counter"

_106

import "NumberFormatter"

_106

_106

access(all)

_106

fun main(): String {

_106

let count: Int = Counter.getCount()

_106

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_106

return formattedCount

_106

}

_106

`,

_106

query: { enabled: true },

_106

});

_106

_106

const {

_106

mutate: increment,

_106

isPending: txPending,

_106

data: txId,

_106

error: txError,

_106

} = useFlowMutate();

_106

_106

const { transactionStatus, error: txStatusError } = useFlowTransactionStatus({

_106

id: txId || '',

_106

});

_106

_106

useEffect(() => {

_106

if (txId && transactionStatus?.status === 3) {

_106

// Transaction is executed

_106

refetch(); // Refresh the counter

_106

}

_106

}, [transactionStatus?.status, txId, refetch]);

_106

_106

const handleIncrement = () => {

_106

increment({

_106

cadence: `

_106

import "Counter"

_106

_106

transaction {

_106

prepare(acct: &Account) {

_106

// Authorization handled via wallet

_106

}

_106

execute {

_106

Counter.increment()

_106

let newCount = Counter.getCount()

_106

log("New count after incrementing: ".concat(newCount.toString()))

_106

}

_106

}

_106

`,

_106

});

_106

};

_106

_106

return (

_106

<div>

_106

<h1>Flow Counter dApp</h1>

_106

_106

{isLoading ? (

_106

<p>Loading count...</p>

_106

) : error ? (

_106

<p>Error: {error.message}</p>

_106

) : (

_106

<div>

_106

<h2>{(data as string) || '0'}</h2>

_106

<p>Current Count</p>

_106

</div>

_106

)}

_106

_106

{user?.loggedIn ? (

_106

<div>

_106

<p>Connected: {user.addr}</p>

_106

_106

<button onClick={handleIncrement} disabled={txPending}>

_106

{txPending ? 'Processing...' : 'Increment Count'}

_106

</button>

_106

_106

<button onClick={unauthenticate}>Disconnect</button>

_106

_106

{transactionStatus?.statusString && transactionStatus?.status && (

_106

<p>

_106

Status: {transactionStatus.status >= 3 ? 'Successful' : 'Pending'}

_106

</p>

_106

)}

_106

_106

{txError && <p>Error: {txError.message}</p>}

_106

_106

{txStatusError && <p>Status Error: {txStatusError.message}</p>}

_106

</div>

_106

) : (

_106

<button onClick={authenticate}>Connect Wallet</button>

_106

)}

_106

</div>

_106

);

_106

} ``

In this complete page:

* **Step 1** queries the counter value.
* **Step 2** sends a transaction to increment the counter and stores the transaction ID.
* **Step 3** subscribes to transaction status updates using the stored transaction ID and uses a `useEffect` hook to automatically refetch the updated count when the transaction is sealed (status code 4).
* **Step 4** integrates authentication via `useFlowCurrentUser` and combines all the pieces into a single user interface.

tip

In this tutorial, we inlined Cadence code for simplicity. For real projects, we recommend storing Cadence in separate `.cdc` files, using the [Cadence VSCode extension](/build/tools/vscode-extension), and importing them with the [`flow-cadence-plugin`](https://github.com/chasefleming/flow-cadence-plugin) for Next.js or Webpack projects.

## Running the App[​](#running-the-app "Direct link to Running the App")

Start your development server:

`_10

npm run dev`

warning

If you have the Flow wallet browser extension installed, you might automatically log into the app. Normally this is desirable for your users, but you don't want to use it here.

Log out, and log back in selecting the Dev Wallet instead of the Flow Wallet.

warning

For your app to connect with contracts deployed on the emulator, you need to have completed [Step 1: Contract Interaction] and [Step 2: Local Development].

Then visit <http://localhost:3000> in your browser. You should see:

* The current counter value displayed (formatted with commas using `NumberFormatter`).
* A **Log In** button that launches the kit Discovery UI with your local [Dev Wallet](/build/tools/flow-dev-wallet).
* Once logged in, your account address appears with options to **Log Out** and **Increment Count**.
* When you click **Increment Count**, the transaction is sent; its status updates are displayed in real time below the action buttons, and once the transaction is sealed, the updated count is automatically fetched.

## Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up")

By following these steps, you've built a simple Next.js dApp that interacts with a Flow smart contract using [**@onflow/react-sdk**](/build/tools/react-sdk). In this guide you learned how to:

* Wrap your application in a `FlowProvider` to configure blockchain connectivity.
* Use kit hooks such as `useFlowQuery`, `useFlowMutate`, `useFlowTransactionStatus`, and `useFlowCurrentUser` to manage authentication, query onchain data, submit transactions, and monitor their status.
* Integrate with the local Flow emulator and Dev Wallet for a fully functional development setup.

For additional details and advanced usage, refer to the [@onflow/react-sdk documentation](/build/tools/react-sdk) and other Flow developer resources.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app.md)

Last updated on **Sep 25, 2025** by **Felipe Cevallos**

[Previous

Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)[Next

Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
* [Setting Up the Next.js App](#setting-up-the-nextjs-app)
  + [Step 1: Create a New Next.js App](#step-1-create-a-new-nextjs-app)
  + [Step 2: Move the Next.js App Up a Directory](#step-2-move-the-nextjs-app-up-a-directory)
  + [Step 3: Install @onflow/react-sdk](#step-3-install-onflowreact-sdk)
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

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.