# Source: https://developers.flow.com/build/getting-started/fcl-quickstart

Building a Simple Frontend with FCL | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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

# Simple Frontend

Building upon the `Counter` contract you interacted with in [Step 1: Contract Interaction](/build/getting-started/contract-interaction) and deployed locally in [Step 2: Local Development](/build/getting-started/flow-cli), this tutorial will guide you through creating a simple frontend application using [Next.js](https://nextjs.org/docs/getting-started) to interact with the `Counter` smart contract on the local Flow emulator. Using the [Flow Client Library](https://github.com/onflow/fcl-js) (FCL), you'll learn how to read and modify the contract's state from a React web application, set up wallet authentication using FCL's Discovery UI connected to the local emulator, and query the chain to read data from smart contracts.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Display data from a [Cadence](https://developers.flow.com/cadence) smart contract (`Counter`) on a Next.js frontend using the [Flow Client Library](https://github.com/onflow/fcl-js).
* Query the chain to read data from smart contracts on the local emulator.
* Mutate the state of a smart contract by sending transactions using FCL and a wallet connected to the local emulator.
* Set up the Discovery UI to use a wallet for authentication with the local emulator.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Completion of [Step 1: Contract Interaction](/build/getting-started/contract-interaction) and [Step 2: Local Development](/build/getting-started/flow-cli).
* Flow CLI installed.
* Node.js and npm installed.

## Setting Up the Next.js App[​](#setting-up-the-nextjs-app "Direct link to Setting Up the Next.js App")

Assuming you're in your project directory from Steps 1 and 2, we'll create a Next.js frontend application to interact with your smart contract deployed on the local Flow emulator.

### Step 1: Create a New Next.js App[​](#step-1-create-a-new-nextjs-app "Direct link to Step 1: Create a New Next.js App")

First, we'll create a new Next.js application using `npx create-next-app`. We'll create it inside your existing project directory and then move it up to the root directory.

**Assumption**: You are already in your project directory.

Run the following command:

`_10

npx create-next-app@latest fcl-app-quickstart`

During the setup process, you'll be prompted with several options. Choose the following:

* **TypeScript**: **No**
* **Use src directory**: **Yes**
* **Use App Router**: **Yes**

This command will create a new Next.js project named `fcl-app-quickstart` inside your current directory.

### Step 2: Move the Next.js App Up a Directory[​](#step-2-move-the-nextjs-app-up-a-directory "Direct link to Step 2: Move the Next.js App Up a Directory")

Now, we'll move the contents of the `fcl-app-quickstart` directory up to your project root directory.

**Note**: Moving the Next.js app into your existing project may overwrite existing files such as `package.json`, `package-lock.json`, `.gitignore`, etc. **Make sure to back up any important files before proceeding.** You may need to merge configurations manually.

#### Remove the README File[​](#remove-the-readme-file "Direct link to Remove the README File")

Before moving the files, let's remove the `README.md` file from the `fcl-app-quickstart` directory to avoid conflicts:

`_10

rm fcl-app-quickstart/README.md`

#### Merge `.gitignore` Files and Move Contents[​](#merge-gitignore-files-and-move-contents "Direct link to merge-gitignore-files-and-move-contents")

To merge the `.gitignore` files, you can use the `cat` command to concatenate them and then remove duplicates:

`_10

cat .gitignore fcl-app-quickstart/.gitignore | sort | uniq > temp_gitignore

_10

mv temp_gitignore .gitignore`

Now, move the contents of the `fcl-app-quickstart` directory to your project root:

On macOS/Linux:

`_10

mv fcl-app-quickstart/* .

_10

mv fcl-app-quickstart/.* . # This moves hidden files like .env.local if any

_10

rm -r fcl-app-quickstart`

On Windows (PowerShell):

`_10

Move-Item -Path .\fcl-app-quickstart\* -Destination . -Force

_10

Move-Item -Path .\fcl-app-quickstart\.* -Destination . -Force

_10

Remove-Item -Recurse -Force .\fcl-app-quickstart`

**Note**: When moving hidden files (those starting with a dot, like `.gitignore`), ensure you don't overwrite important files in your root directory.

### Step 3: Install FCL[​](#step-3-install-fcl "Direct link to Step 3: Install FCL")

Now, install the Flow Client Library (FCL) in your project. FCL is a JavaScript library that simplifies interaction with the Flow blockchain:

`_10

npm install @onflow/fcl`

## Setting Up the Local Flow Emulator and Dev Wallet[​](#setting-up-the-local-flow-emulator-and-dev-wallet "Direct link to Setting Up the Local Flow Emulator and Dev Wallet")

Before proceeding, ensure that both the Flow emulator and the Dev Wallet are running.

### Step 1: Start the Flow Emulator[​](#step-1-start-the-flow-emulator "Direct link to Step 1: Start the Flow Emulator")

In a new terminal window, navigate to your project directory and run:

`_10

flow emulator start`

This starts the Flow emulator on `http://localhost:8888`.

### Step 2: Start the FCL Dev Wallet[​](#step-2-start-the-fcl-dev-wallet "Direct link to Step 2: Start the FCL Dev Wallet")

In another terminal window, run:

`_10

flow dev-wallet`

This starts the Dev Wallet, which listens on `http://localhost:8701`. The Dev Wallet is a local wallet that allows you to authenticate with the Flow blockchain and sign transactions on the local emulator. This is the wallet we'll select in Discovery UI when authenticating.

## Querying the Chain[​](#querying-the-chain "Direct link to Querying the Chain")

Now, let's read data from the `Counter` smart contract deployed on the local Flow emulator.

Since you've already deployed the `Counter` contract in [Step 2: Local Development](/build/getting-started/flow-cli), we can proceed to query it.

### Step 1: Update the Home Page[​](#step-1-update-the-home-page "Direct link to Step 1: Update the Home Page")

Open `src/app/page.js` in your editor.

#### Adding the FCL Configuration Before the Rest[​](#adding-the-fcl-configuration-before-the-rest "Direct link to Adding the FCL Configuration Before the Rest")

At the top of your `page.js` file, before the rest of the code, we'll add the FCL configuration. This ensures that FCL is properly configured before we use it.

Add the following code:

`_10

import * as fcl from "@onflow/fcl";

_10

_10

// FCL Configuration

_10

fcl.config({

_10

"flow.network": "local",

_10

"accessNode.api": "http://localhost:8888", // Flow Emulator

_10

"discovery.wallet": "http://localhost:8701/fcl/authn", // Local Wallet Discovery

_10

});`

This configuration code sets up FCL to work with the local Flow emulator and Dev Wallet. The `flow.network` and `accessNode.api` properties point to the local emulator, while `discovery.wallet` points to the local Dev Wallet for authentication.

For more information on Discovery configurations, refer to the [Wallet Discovery Guide](/tools/clients/fcl-js/discovery).

#### Implementing the Component[​](#implementing-the-component "Direct link to Implementing the Component")

Now, we'll implement the component to query the count from the `Counter` contract.

Update your `page.js` file to the following:

`_54

// src/app/page.js

_54

_54

"use client"; // This directive is necessary when using useState and useEffect in Next.js App Router

_54

_54

import { useState, useEffect } from "react";

_54

import * as fcl from "@onflow/fcl";

_54

_54

// FCL Configuration

_54

fcl.config({

_54

"flow.network": "local",

_54

"accessNode.api": "http://localhost:8888",

_54

"discovery.wallet": "http://localhost:8701/fcl/authn", // Local Dev Wallet

_54

});

_54

_54

export default function Home() {

_54

const [count, setCount] = useState(0);

_54

_54

const queryCount = async () => {

_54

try {

_54

const res = await fcl.query({

_54

cadence: `

_54

import Counter from 0xf8d6e0586b0a20c7

_54

import NumberFormatter from 0xf8d6e0586b0a20c7

_54

_54

access(all)

_54

fun main(): String {

_54

// Retrieve the count from the Counter contract

_54

let count: Int = Counter.getCount()

_54

_54

// Format the count using NumberFormatter

_54

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_54

_54

// Return the formatted count

_54

return formattedCount

_54

}

_54

`,

_54

});

_54

setCount(res);

_54

} catch (error) {

_54

console.error("Error querying count:", error);

_54

}

_54

};

_54

_54

useEffect(() => {

_54

queryCount();

_54

}, []);

_54

_54

return (

_54

<div>

_54

<h1>FCL App Quickstart</h1>

_54

<div>Count: {count}</div>

_54

</div>

_54

);

_54

}`

In the above code:

* We import the necessary React hooks (`useState` and `useEffect`) and the FCL library.
* We define the `Home` component, which is the main page of our app.
* We set up a state variable `count` using the `useState` hook to store the count value.
* We define an `async` function `queryCount` to query the count from the `Counter` contract.
* We use the `useEffect` hook to call `queryCount` when the component mounts.
* We return a simple JSX structure that displays the count value on the page.
* If an error occurs during the query, we log it to the console.
* We use the script from Step 2 to query the count from the `Counter` contract and format it using the `NumberFormatter` contract.

info

In this tutorial, we've shown you hardcoding addresses directly for simplicity and brevity. However, it's **recommended** to use the `import "ContractName"` syntax, as demonstrated in [Step 2: Local Development](/build/getting-started/flow-cli). This approach is supported by the Flow Client Library (FCL) and allows you to use aliases for contract addresses in your `flow.json` file. It makes your code more flexible, maintainable, and easier to adapt across different environments (e.g., `testnet`, `mainnet`).

Learn more about this best practice in the [FCL Documentation](/tools/clients/fcl-js/api#using-flowjson-for-contract-imports).

### Step 2: Run the App[​](#step-2-run-the-app "Direct link to Step 2: Run the App")

Start your development server:

`_10

npm run dev`

Visit `http://localhost:3000` in your browser. You should see the current count displayed on the page, formatted according to the `NumberFormatter` contract.

## Mutating the Chain State[​](#mutating-the-chain-state "Direct link to Mutating the Chain State")

Now that we've successfully read data from the Flow blockchain emulator, let's modify the state by incrementing the `count` in the `Counter` contract. We'll set up wallet authentication and send a transaction to the blockchain emulator.

### Adding Authentication and Transaction Functionality[​](#adding-authentication-and-transaction-functionality "Direct link to Adding Authentication and Transaction Functionality")

#### Step 1: Manage Authentication State[​](#step-1-manage-authentication-state "Direct link to Step 1: Manage Authentication State")

In `src/app/page.js`, add new state variables to manage the user's authentication state:

`_10

const [user, setUser] = useState({ loggedIn: false });`

#### Step 2: Subscribe to Authentication Changes[​](#step-2-subscribe-to-authentication-changes "Direct link to Step 2: Subscribe to Authentication Changes")

Update the `useEffect` hook to subscribe to the current user's authentication state:

`_10

useEffect(() => {

_10

fcl.currentUser.subscribe(setUser);

_10

queryCount();

_10

}, []);`

The `currentUser.subscribe` method listens for changes to the current user's authentication state and updates the `user` state accordingly.

#### Step 3: Define Log In and Log Out Functions[​](#step-3-define-log-in-and-log-out-functions "Direct link to Step 3: Define Log In and Log Out Functions")

Define the `logIn` and `logOut` functions:

`_10

const logIn = () => {

_10

fcl.authenticate();

_10

};

_10

_10

const logOut = () => {

_10

fcl.unauthenticate();

_10

};`

The `authenticate` method opens the Discovery UI for the user to log in, while `unauthenticate` logs the user out.

#### Step 4: Define the `incrementCount` Function[​](#step-4-define-the-incrementcount-function "Direct link to step-4-define-the-incrementcount-function")

Add the `incrementCount` function:

`_38

const incrementCount = async () => {

_38

try {

_38

const transactionId = await fcl.mutate({

_38

cadence: `

_38

import Counter from 0xf8d6e0586b0a20c7

_38

_38

transaction {

_38

_38

prepare(acct: &Account) {

_38

// Authorizes the transaction

_38

}

_38

_38

execute {

_38

// Increment the counter

_38

Counter.increment()

_38

_38

// Retrieve the new count and log it

_38

let newCount = Counter.getCount()

_38

log("New count after incrementing: ".concat(newCount.toString()))

_38

}

_38

}

_38

`,

_38

proposer: fcl.currentUser,

_38

payer: fcl.currentUser,

_38

authorizations: [fcl.currentUser.authorization],

_38

limit: 50,

_38

});

_38

_38

console.log("Transaction Id", transactionId);

_38

_38

await fcl.tx(transactionId).onceExecuted();

_38

console.log("Transaction Executed");

_38

_38

queryCount();

_38

} catch (error) {

_38

console.error("Transaction Failed", error);

_38

}

_38

};`

In the above code:

* We define an `async` function `incrementCount` to send a transaction to increment the count in the `Counter` contract.
* We use the `mutate` method to send a transaction to the blockchain emulator.
* The transaction increments the count in the `Counter` contract and logs the new count.
* We use the `proposer`, `payer`, and `authorizations` properties to set the transaction's proposer, payer, and authorizations to the current user.
* The `limit` property sets the gas limit for the transaction.
* We log the transaction ID and wait for the transaction to be sealed before querying the updated count.
* If an error occurs during the transaction, we log it to the console.
* After the transaction is sealed, we call `queryCount` to fetch and display the updated count.
* We use the transaction from Step 2 to increment the count in the `Counter` contract.

#### Step 5: Update the Return Statement[​](#step-5-update-the-return-statement "Direct link to Step 5: Update the Return Statement")

Update the `return` statement to include authentication buttons and display the user's address when they're logged in:

`_17

return (

_17

<div>

_17

<h1>FCL App Quickstart</h1>

_17

<div>Count: {count}</div>

_17

{user.loggedIn ? (

_17

<div>

_17

<p>Address: {user.addr}</p>

_17

<button onClick={logOut}>Log Out</button>

_17

<div>

_17

<button onClick={incrementCount}>Increment Count</button>

_17

</div>

_17

</div>

_17

) : (

_17

<button onClick={logIn}>Log In</button>

_17

)}

_17

</div>

_17

);`

#### Full `page.js` Code[​](#full-pagejs-code "Direct link to full-pagejs-code")

Your `src/app/page.js` should now look like this:

`_114

// src/app/page.js

_114

_114

"use client";

_114

_114

import { useState, useEffect } from "react";

_114

import * as fcl from "@onflow/fcl";

_114

_114

// FCL Configuration

_114

fcl.config({

_114

"flow.network": "local",

_114

"accessNode.api": "http://localhost:8888",

_114

"discovery.wallet": "http://localhost:8701/fcl/authn", // Local Dev Wallet

_114

});

_114

_114

export default function Home() {

_114

const [count, setCount] = useState(0);

_114

const [user, setUser] = useState({ loggedIn: false });

_114

_114

const queryCount = async () => {

_114

try {

_114

const res = await fcl.query({

_114

cadence: `

_114

import Counter from 0xf8d6e0586b0a20c7

_114

import NumberFormatter from 0xf8d6e0586b0a20c7

_114

_114

access(all)

_114

fun main(): String {

_114

// Retrieve the count from the Counter contract

_114

let count: Int = Counter.getCount()

_114

_114

// Format the count using NumberFormatter

_114

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_114

_114

// Return the formatted count

_114

return formattedCount

_114

}

_114

`,

_114

});

_114

setCount(res);

_114

} catch (error) {

_114

console.error("Error querying count:", error);

_114

}

_114

};

_114

_114

useEffect(() => {

_114

fcl.currentUser.subscribe(setUser);

_114

queryCount();

_114

}, []);

_114

_114

const logIn = () => {

_114

fcl.authenticate();

_114

};

_114

_114

const logOut = () => {

_114

fcl.unauthenticate();

_114

};

_114

_114

const incrementCount = async () => {

_114

try {

_114

const transactionId = await fcl.mutate({

_114

cadence: `

_114

import Counter from 0xf8d6e0586b0a20c7

_114

_114

transaction {

_114

_114

prepare(acct: &Account) {

_114

// Authorizes the transaction

_114

}

_114

_114

execute {

_114

// Increment the counter

_114

Counter.increment()

_114

_114

// Retrieve the new count and log it

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

proposer: fcl.currentUser,

_114

payer: fcl.currentUser,

_114

authorizations: [fcl.currentUser.authorization],

_114

limit: 50,

_114

});

_114

_114

console.log("Transaction Id", transactionId);

_114

_114

await fcl.tx(transactionId).onceExecuted();

_114

console.log("Transaction Executed");

_114

_114

queryCount();

_114

} catch (error) {

_114

console.error("Transaction Failed", error);

_114

}

_114

};

_114

_114

return (

_114

<div>

_114

<h1>FCL App Quickstart</h1>

_114

<div>Count: {count}</div>

_114

{user.loggedIn ? (

_114

<div>

_114

<p>Address: {user.addr}</p>

_114

<button onClick={logOut}>Log Out</button>

_114

<div>

_114

<button onClick={incrementCount}>Increment Count</button>

_114

</div>

_114

</div>

_114

) : (

_114

<button onClick={logIn}>Log In</button>

_114

)}

_114

</div>

_114

);

_114

}`

Visit `http://localhost:3000` in your browser.

* **Log In**:

  + Click the "Log In" button.
  + The Discovery UI will appear, showing the available wallets. Select the "Dev Wallet" option.
  + Select the account to log in with.
  + If prompted, create a new account or use an existing one.
* **Increment Count**:

  + After logging in, you'll see your account address displayed.
  + Click the "Increment Count" button.
  + Your wallet will prompt you to approve the transaction.
  + Approve the transaction to send it to the Flow emulator.
* **View Updated Count**:

  + Once the transaction is sealed, the app will automatically fetch and display the updated count.
  + You should see the count incremented on the page, formatted using the `NumberFormatter` contract.

## Conclusion[​](#conclusion "Direct link to Conclusion")

By following these steps, you've successfully created a simple frontend application using Next.js that interacts with the `Counter` smart contract on the Flow blockchain emulator. You've learned how to:

* Add the FCL configuration before the rest of your code within the `page.js` file.
* Configure FCL to work with the local Flow emulator and Dev Wallet.
* Start the Dev Wallet using `flow dev-wallet` to enable local authentication.
* Read data from the local blockchain emulator, utilizing multiple contracts (`Counter` and `NumberFormatter`).
* Authenticate users using the local Dev Wallet.
* Send transactions to mutate the state of a smart contract on the local emulator.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/getting-started/fcl-quickstart.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

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
  + [Step 3: Install FCL](#step-3-install-fcl)
* [Setting Up the Local Flow Emulator and Dev Wallet](#setting-up-the-local-flow-emulator-and-dev-wallet)
  + [Step 1: Start the Flow Emulator](#step-1-start-the-flow-emulator)
  + [Step 2: Start the FCL Dev Wallet](#step-2-start-the-fcl-dev-wallet)
* [Querying the Chain](#querying-the-chain)
  + [Step 1: Update the Home Page](#step-1-update-the-home-page)
  + [Step 2: Run the App](#step-2-run-the-app)
* [Mutating the Chain State](#mutating-the-chain-state)
  + [Adding Authentication and Transaction Functionality](#adding-authentication-and-transaction-functionality)
* [Conclusion](#conclusion)
* [Additional Resources](#additional-resources)

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