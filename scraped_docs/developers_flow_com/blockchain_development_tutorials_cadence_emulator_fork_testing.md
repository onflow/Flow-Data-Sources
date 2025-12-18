# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/emulator-fork-testing

Interactive Testing with Forked Emulator | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)+ [Emulator Fork Testing](/blockchain-development-tutorials/cadence/emulator-fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* Emulator Fork Testing

On this page

# Interactive Testing with Forked Emulator

Fork testing gives you a local copy of mainnet state that you can freely modify and reset instantly. Test your DeFi app against real DEX liquidity pools and lending protocols without risking funds, verify integrations with existing mainnet contracts before deploying, and debug production issues at specific block heights with exact mainnet state.

This tutorial teaches you how to run your app and E2E tests against Flow mainnet using `flow emulator --fork`. You'll connect your frontend to production-like state, impersonate any mainnet account, and test with real balances and assets—all running locally.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

After you complete this tutorial, you'll be able to:

* **Start the emulator in fork mode** with `flow emulator --fork`.
* **Connect your app frontend** to the forked emulator.
* **Test DeFi integrations** against real liquidity pools, DEXs, and protocols.
* **Test against real mainnet contracts** and production data interactively.
* **Run E2E tests** (Cypress, Playwright) against forked state.
* **Use account impersonation** to test as any mainnet account with real balances and assets.
* **Pin to specific block heights** for reproducible testing.
* **Debug and explore** contract interactions manually.

## What You'll Build[​](#what-youll-build "Direct link to What You'll Build")

You'll create a complete forked emulator setup that demonstrates:

* Starting the emulator with forked mainnet state.
* A React app connected to the forked emulator reading real FlowToken data.
* Manual testing flows using account impersonation.
* Automating tests with E2E frameworks against forked state.
* A reusable pattern for interactive testing and debugging.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Flow CLI[​](#flow-cli "Direct link to Flow CLI")

This tutorial requires [Flow CLI](/build/tools/flow-cli) v1.8.0 or later installed. If you haven't installed it yet and have [homebrew](https://brew.sh) installed, run:

`_10

brew install flow-cli`

For other operating systems, refer to the [installation guide](/build/tools/flow-cli/install).

### Node.js and npm[​](#nodejs-and-npm "Direct link to Node.js and npm")

You'll need Node.js (v16+) and npm to run the React frontend examples. Check your installation:

`_10

node --version

_10

npm --version`

### Frontend development knowledge[​](#frontend-development-knowledge "Direct link to Frontend development knowledge")

Basic familiarity with React and JavaScript is helpful but not required. The examples use the [Flow React SDK](/build/tools/react-sdk) for Flow blockchain integration.

tip

This tutorial uses `@onflow/react-sdk` for all React examples. The React SDK provides hooks and components that make Flow development feel native to React. For non-React applications, you can use `@onflow/fcl` directly.

### Network access[​](#network-access "Direct link to Network access")

You'll need network access to Flow's public access nodes:

* Mainnet: `access.mainnet.nodes.onflow.org:9000`
* Testnet: `access.devnet.nodes.onflow.org:9000`

info

This tutorial covers `flow emulator --fork` (interactive testing with a forked emulator), which is different from `flow test --fork` (running Cadence test files against forked state). For an overview of both modes, see [Fork Testing](/build/tools/flow-cli/fork-testing). For testing Cadence contracts with test files, see [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing).

## Understanding Emulator Fork Mode[​](#understanding-emulator-fork-mode "Direct link to Understanding Emulator Fork Mode")

### What is `flow emulator --fork`?[​](#what-is-flow-emulator---fork "Direct link to what-is-flow-emulator---fork")

The emulator's fork mode starts a local Flow blockchain that connects to a real network (mainnet or testnet) and fetches state on-demand. Your app, scripts, and transactions run locally but can read from and interact with real network data.

**Key capabilities:**

* Full gRPC and REST API servers running locally
* On-demand fetching of accounts, contracts, and state from the live network
* Disabled signature validation. You can impersonate any mainnet account to execute transactions
* All mutations stay local—never affect the real network
* Perfect for E2E tests, manual exploration, and debugging

### When to Use This[​](#when-to-use-this "Direct link to When to Use This")

Use `flow emulator --fork` for:

* **DeFi application testing**: Test against real liquidity pools, DEXs, and lending protocols with production state
* **E2E and frontend testing**: Run Cypress/Playwright tests against production-like state
* **Manual exploration**: Interact with your app connected to forked mainnet
* **Debugging user issues**: Reproduce bugs at specific block heights
* **Migration testing**: Test contract upgrades with real account state
* **Wallet integration**: Test wallet connect flows and transactions
* **Bot and indexer testing**: Run automated tools against forked data

**Don't use this for:**

* Cadence unit/integration tests (use `flow test --fork` instead—see [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing))

### Emulator Fork vs Test Framework Fork[​](#emulator-fork-vs-test-framework-fork "Direct link to Emulator Fork vs Test Framework Fork")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Feature `flow emulator --fork` `flow test --fork`|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Use for** App E2E, manual testing, debugging Cadence unit/integration tests|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Connects to** Frontend, wallets, bots, E2E tools Cadence Testing Framework|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Run with** FCL, Cypress, Playwright, manual clicks `flow test` command| **Best for** User flows, UI testing, exploration Contract logic validation|  |  |  | | --- | --- | --- | | **Examples** React app, wallet flows, E2E suites `*_test.cdc` files | | | | | | | | | | | | | | | | | |

Both modes are valuable—use the right tool for the job.

## Quick Start: Run in 60 Seconds[​](#quick-start-run-in-60-seconds "Direct link to Quick Start: Run in 60 Seconds")

Want to see it work immediately? Here's the fastest path:

`_11

# 1. Initialize a Flow project

_11

flow init

_11

_11

# 2. Install FlowToken dependency

_11

flow dependencies install FlowToken FungibleToken

_11

_11

# 3. Start forked emulator (in a separate terminal)

_11

flow emulator --fork mainnet

_11

_11

# 4. Create a script to check the forked state

_11

flow generate script getFlowSupply`

Add the following to `cadence/scripts/getFlowSupply.cdc`:

`_10

import "FlowToken"

_10

_10

access(all) fun main(): UFix64 {

_10

return FlowToken.totalSupply

_10

}`

First, verify the script works against real mainnet:

`_10

flow scripts execute cadence/scripts/getFlowSupply.cdc --network mainnet`

Then, in another terminal, run the script against the fork:

`_10

flow scripts execute cadence/scripts/getFlowSupply.cdc --network mainnet-fork`

You'll see the real mainnet FlowToken supply! Now let's build a complete example with a frontend.

## Create Your Project[​](#create-your-project "Direct link to Create Your Project")

Navigate to your development directory and create a new Flow project:

`_10

mkdir emulator-fork-demo

_10

cd emulator-fork-demo

_10

flow init --yes`

This creates an empty Flow project with default configuration.

## Start the Forked Emulator[​](#start-the-forked-emulator "Direct link to Start the Forked Emulator")

Start the emulator in fork mode, connected to mainnet:

`_10

flow emulator --fork mainnet`

You'll see output like:

`_10

INFO[0000] ⚙️ Using service account 0xf8d6e0586b0a20c7

_10

INFO[0000] 🌱 Starting Flow Emulator in fork mode (mainnet)

_10

INFO[0000] 🛠 GRPC server started on 127.0.0.1:3569

_10

INFO[0000] 📡 REST server started on 127.0.0.1:8888

_10

INFO[0000] 🌐 Forking from access.mainnet.nodes.onflow.org:9000`

**Leave this terminal running.** The emulator is now serving:

* **REST API**: `http://localhost:8888` (for FCL/frontend)
* **gRPC API**: `localhost:3569` (for Flow CLI)

Fork Network Configuration

When you run `flow init`, the CLI automatically configures a `mainnet-fork` network in your `flow.json` that inherits all contract aliases from mainnet. This means you don't need to manually configure fork networks—it just works!

For details on fork network configuration, see the [Fork Testing Overview](/build/tools/flow-cli/fork-testing) and [flow.json Configuration Reference](/build/tools/flow-cli/flow.json/configuration#networks).

tip

Pin to a specific block height for reproducibility:

`_10

flow emulator --fork mainnet --fork-height <BLOCK_HEIGHT>`

This ensures the forked state is consistent across runs—essential for E2E tests in CI.

## Deploy Your Contracts Against Mainnet State[​](#deploy-your-contracts-against-mainnet-state "Direct link to Deploy Your Contracts Against Mainnet State")

The most common use case: deploy your NEW contracts to the forked emulator so they can interact with real mainnet contracts and data. This lets you test your DeFi protocol against live DEXs, lending protocols, liquidity pools, and other production DeFi infrastructure.

### Example: Deploy and Test Your Contract[​](#example-deploy-and-test-your-contract "Direct link to Example: Deploy and Test Your Contract")

**1. Create your contract:**

`_10

flow generate contract MyDeFiProtocol`

Edit `cadence/contracts/MyDeFiProtocol.cdc`:

`_10

import "FlowToken"

_10

_10

access(all) contract MyDeFiProtocol {

_10

// Your DeFi logic that reads real mainnet FlowToken data

_10

access(all) fun getTotalSupply(): UFix64 {

_10

return FlowToken.totalSupply

_10

}

_10

}`

**2. Start the forked emulator:**

`_10

flow emulator --fork mainnet`

When the emulator starts, note the service account address in the logs:

`_10

⚙️ Using service account 0xe467b9dd11fa00df`

**3. Configure the service account:**

Add the forked emulator's service account (use the address from the startup logs and a dummy key).

First, create a dummy key file:

`_10

echo "0000000000000000000000000000000000000000000000000000000000000000" > blank-key.pkey`

Then manually add to your `flow.json`:

`_11

{

_11

"accounts": {

_11

"mainnet-fork-service": {

_11

"address": "0xe467b9dd11fa00df",

_11

"key": {

_11

"type": "file",

_11

"location": "blank-key.pkey"

_11

}

_11

}

_11

}

_11

}`

Since signature validation is disabled in fork mode, the key value doesn't matter.

**4. Configure deployment:**

`_10

flow config add deployment \

_10

--network mainnet-fork \

_10

--account mainnet-fork-service \

_10

--contract MyDeFiProtocol`

**5. Deploy your contract:**

`_10

flow project deploy --network mainnet-fork --update`

tip

Use `--update` if you're working on an existing project that's already deployed to mainnet. The forked emulator mirrors mainnet state, so if your contract already exists at that address on mainnet, it will exist in the fork too. The `--update` flag replaces the mainnet version with your local changes.

**6. Test your contract:**

Your contract can now interact with real mainnet contracts! Create a script to test it:

`_10

flow generate script getTotalSupply`

Add the following to `cadence/scripts/getTotalSupply.cdc`:

`_10

import "MyDeFiProtocol"

_10

_10

access(all) fun main(): UFix64 {

_10

return MyDeFiProtocol.getTotalSupply()

_10

}`

Run the script:

`_10

flow scripts execute cadence/scripts/getTotalSupply.cdc --network mainnet-fork`

You'll see something like `Result: 1628083999.54686045` - the real mainnet FlowToken supply! Your contract runs locally but reads production data. Perfect for testing integrations before mainnet deployment.

## Mock Existing Mainnet Contracts[​](#mock-existing-mainnet-contracts "Direct link to Mock Existing Mainnet Contracts")

You can override existing mainnet contracts with your own versions for testing. This is useful for testing contract upgrades, fixing bugs, or adding test functionality to mainnet contracts.

### Example: Mock a Mainnet Contract[​](#example-mock-a-mainnet-contract "Direct link to Example: Mock a Mainnet Contract")

Let's say you want to test how your DeFi protocol behaves with a modified version of an existing mainnet contract.

**1. Create your mock oracle contract:**

`_10

flow generate contract PriceOracle`

Edit `cadence/contracts/PriceOracle.cdc` to match the interface of the mainnet oracle you want to mock:

`_10

// Mock implementation of mainnet PriceOracle with fixed test prices

_10

access(all) contract PriceOracle {

_10

access(all) fun getPrice(): UFix64 {

_10

return 123.45 // Fixed test price for predictable testing

_10

}

_10

}`

**2. Deploy to the SAME address as the mainnet oracle:**

In your `flow.json`, configure deployment to use the mainnet oracle's address:

`_19

{

_19

"contracts": {

_19

"PriceOracle": "cadence/contracts/PriceOracle.cdc"

_19

},

_19

"deployments": {

_19

"mainnet-fork": {

_19

"mainnet-oracle-account": ["PriceOracle"]

_19

}

_19

},

_19

"accounts": {

_19

"mainnet-oracle-account": {

_19

"address": "0x1654653399040a61",

_19

"key": {

_19

"type": "file",

_19

"location": "blank-key.pkey"

_19

}

_19

}

_19

}

_19

}`

**3. Deploy with `--update` flag:**

`_10

flow project deploy --network mainnet-fork --update`

Now your mock oracle replaces the mainnet oracle at that address. All imports and references to the original oracle will use your mocked version with fixed test prices instead!

tip

This is how you test contract upgrades or modifications against real mainnet state without affecting the live network.

## Install Dependencies[​](#install-dependencies "Direct link to Install Dependencies")

Use the [Dependency Manager](/build/tools/flow-cli/dependency-manager) to install common Flow contracts. This adds them to your `flow.json` with mainnet aliases that will automatically work on the fork:

`_10

flow dependencies install FlowToken FungibleToken`

Your `flow.json` now includes:

`_20

{

_20

"dependencies": {

_20

"FlowToken": {

_20

"source": "mainnet://1654653399040a61.FlowToken",

_20

"aliases": {

_20

"emulator": "0x0ae53cb6e3f42a79",

_20

"mainnet": "0x1654653399040a61",

_20

"testnet": "0x7e60df042a9c0868"

_20

}

_20

},

_20

"FungibleToken": {

_20

"source": "mainnet://f233dcee88fe0abe.FungibleToken",

_20

"aliases": {

_20

"emulator": "0xee82856bf20e2aa6",

_20

"mainnet": "0xf233dcee88fe0abe",

_20

"testnet": "0x9a0766d93b6608b7"

_20

}

_20

}

_20

}

_20

}`

**Key insight:** Notice there's no `mainnet-fork` alias. That's the beauty—`mainnet-fork` automatically inherits the `mainnet` aliases thanks to the fork configuration!

## Test with Flow CLI Scripts[​](#test-with-flow-cli-scripts "Direct link to Test with Flow CLI Scripts")

Before connecting a frontend, verify the fork works with a simple script.

Generate a script file using the Flow CLI:

`_10

flow generate script getFlowSupply`

Add the following to `cadence/scripts/getFlowSupply.cdc`:

`_10

import "FlowToken"

_10

_10

access(all) fun main(): UFix64 {

_10

return FlowToken.totalSupply

_10

}`

Notice we're using the import shorthand `import "FlowToken"` instead of an address. The CLI will automatically resolve this to the mainnet address on the fork.

First, verify the script works against real mainnet:

`_10

flow scripts execute cadence/scripts/getFlowSupply.cdc --network mainnet`

Then, in a **new terminal** (keep the emulator running), execute the script against the fork:

`_10

flow scripts execute cadence/scripts/getFlowSupply.cdc --network mainnet-fork`

You should see the real mainnet FlowToken supply (e.g., `Result: 1523456789.00000000`).

**What happened:**

1. Your script ran on the local emulator
2. The CLI resolved `"FlowToken"` to the mainnet address (`0x1654653399040a61`)
3. The emulator fetched FlowToken contract state from mainnet on-demand
4. The script returned real production data

Now let's connect a frontend.

## Create a React App[​](#create-a-react-app "Direct link to Create a React App")

Create a Next.js app with Flow integration:

`_10

npx create-next-app@latest flow-fork-app`

During setup, choose:

* **Use TypeScript**: Yes
* **Use src directory**: Yes
* **Use App Router**: Yes

Then install the Flow React SDK:

`_10

cd flow-fork-app

_10

npm install @onflow/react-sdk`

Copy your project's `flow.json` into the app's `src` directory:

`_10

# From your flow-fork-app directory

_10

cp ../flow.json src/`

This allows the `FlowProvider` to resolve contract imports.

### Configure for Fork Testing[​](#configure-for-fork-testing "Direct link to Configure for Fork Testing")

Since Next.js uses the App Router with server components, create a client component wrapper. First, create the components directory:

`_10

mkdir -p src/components`

Then create `src/components/FlowProviderWrapper.tsx`:

`_24

'use client';

_24

_24

import { FlowProvider } from '@onflow/react-sdk';

_24

import flowJSON from '../flow.json';

_24

_24

export default function FlowProviderWrapper({

_24

children,

_24

}: {

_24

children: React.ReactNode;

_24

}) {

_24

return (

_24

<FlowProvider

_24

config={{

_24

accessNodeUrl: 'http://localhost:8888', // Point to forked emulator REST endpoint

_24

flowNetwork: 'mainnet-fork', // Use fork network (inherits mainnet aliases)

_24

appDetailTitle: 'Flow Fork Demo',

_24

discoveryWallet: 'http://localhost:8701/fcl/authn', // Dev wallet

_24

}}

_24

flowJson={flowJSON}

_24

>

_24

{children}

_24

</FlowProvider>

_24

);

_24

}`

Then update `src/app/layout.tsx` to use the wrapper:

`_15

import FlowProviderWrapper from '@/components/FlowProviderWrapper';

_15

_15

export default function RootLayout({

_15

children,

_15

}: {

_15

children: React.ReactNode;

_15

}) {

_15

return (

_15

<html lang="en">

_15

<body>

_15

<FlowProviderWrapper>{children}</FlowProviderWrapper>

_15

</body>

_15

</html>

_15

);

_15

}`

### Create a Demo Component[​](#create-a-demo-component "Direct link to Create a Demo Component")

Create a simple demo that queries FlowToken supply from the forked mainnet. Update `src/app/page.tsx`:

`` _60

'use client';

_60

_60

import { useState } from 'react';

_60

import { useFlowCurrentUser, useFlowQuery, Connect } from '@onflow/react-sdk';

_60

_60

export default function Home() {

_60

const { user } = useFlowCurrentUser();

_60

const [shouldFetch, setShouldFetch] = useState(false);

_60

_60

// Query FlowToken supply from forked mainnet

_60

const {

_60

data: flowSupply,

_60

isLoading,

_60

error,

_60

} = useFlowQuery({

_60

cadence: `

_60

import "FlowToken"

_60

_60

access(all) fun main(): UFix64 {

_60

return FlowToken.totalSupply

_60

}

_60

`,

_60

args: (arg, t) => [],

_60

query: {

_60

enabled: shouldFetch, // Only run when button is clicked

_60

},

_60

});

_60

_60

return (

_60

<div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>

_60

<h1>🌊 Flow Emulator Fork Demo</h1>

_60

<p>

_60

Connected to: <strong>Forked Mainnet (localhost:8888)</strong>

_60

</p>

_60

_60

<div style={{ marginTop: '2rem' }}>

_60

<h2>FlowToken Supply (Real Mainnet Data)</h2>

_60

<button onClick={() => setShouldFetch(true)} disabled={isLoading}>

_60

{isLoading ? 'Loading...' : 'Get FlowToken Supply'}

_60

</button>

_60

{error && <p style={{ color: 'red' }}>Error: {(error as Error).message}</p>}

_60

{flowSupply && (

_60

<p style={{ fontSize: '1.5rem', color: 'green' }}>

_60

Total Supply: {Number(flowSupply).toLocaleString()} FLOW

_60

</p>

_60

)}

_60

</div>

_60

_60

<div style={{ marginTop: '2rem' }}>

_60

<h2>Wallet Connection</h2>

_60

<Connect />

_60

{user?.loggedIn && (

_60

<p style={{ marginTop: '1rem' }}>

_60

Connected: <code>{user.addr}</code>

_60

</p>

_60

)}

_60

</div>

_60

</div>

_60

);

_60

} ``

### Start the dev wallet (optional)[​](#start-the-dev-wallet-optional "Direct link to Start the dev wallet (optional)")

For wallet authentication flows, start the FCL dev wallet in another terminal:

`_10

flow dev-wallet`

This starts the dev wallet at `http://localhost:8701`.

### Run your app[​](#run-your-app "Direct link to Run your app")

Start the Next.js dev server:

`_10

npm run dev`

Navigate to `http://localhost:3000`. Click "Get FlowToken Supply" to see real mainnet data!

**What's happening:**

1. `FlowProvider` receives `flow.json` and configures import resolution
2. The string import `import "FlowToken"` resolves to the mainnet address automatically
3. `useFlowQuery` executes the Cadence script via the local emulator
4. The emulator fetches FlowToken state from mainnet on-demand
5. Your app displays real production data—all running locally!

**Key React SDK features used:**

* `FlowProvider` – Wraps your app, configures the Flow connection, and resolves contract imports from `flow.json`
* `useFlowCurrentUser` – Provides wallet authentication state
* `useFlowQuery` – Executes Cadence scripts with automatic caching and loading states
* `Connect` – Pre-built wallet connection UI component

Contract Import Resolution

By passing `flowJson` to the `FlowProvider`, string imports like `import "FlowToken"` automatically resolve to the correct network addresses.

**How it works:**

1. SDK looks up contract aliases for the specified `flowNetwork`
2. For fork networks, it checks if the network has a `fork` property and inherits aliases from the parent network
3. Contract imports in your Cadence code are replaced with the resolved addresses

**Example:** With `flowNetwork: 'mainnet-fork'` (which has `fork: 'mainnet'`), `import "FlowToken"` resolves to `0x1654653399040a61` (the mainnet FlowToken address).

## Account Impersonation[​](#account-impersonation "Direct link to Account Impersonation")

The forked emulator's superpower: you can execute transactions as **any mainnet account** because signature validation is disabled.

### Read Account Balance[​](#read-account-balance "Direct link to Read Account Balance")

Generate a script to read account balances:

`_10

flow generate script getBalance`

Add the following to `cadence/scripts/getBalance.cdc`:

`_11

import "FlowToken"

_11

import "FungibleToken"

_11

_11

access(all) fun main(address: Address): UFix64 {

_11

let account = getAccount(address)

_11

let vaultRef = account.capabilities

_11

.borrow<&{FungibleToken.Balance}>(/public/flowTokenBalance)

_11

?? panic("Could not borrow FlowToken Balance reference")

_11

_11

return vaultRef.balance

_11

}`

Check the Flow service account balance (a real mainnet account):

`_10

flow scripts execute cadence/scripts/getBalance.cdc 0x1654653399040a61 --network mainnet-fork`

You'll see the service account's actual mainnet balance! The imports automatically resolved to mainnet addresses because you're using the `mainnet-fork` network.

### Execute Transaction as Any Account[​](#execute-transaction-as-any-account "Direct link to Execute Transaction as Any Account")

Generate a transaction to transfer tokens:

`_10

flow generate transaction transferTokens`

Add the following to `cadence/transactions/transferTokens.cdc`:

`_23

import "FungibleToken"

_23

import "FlowToken"

_23

_23

transaction(amount: UFix64, to: Address) {

_23

let sentVault: @{FungibleToken.Vault}

_23

_23

prepare(signer: auth(Storage) &Account) {

_23

let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_23

from: /storage/flowTokenVault

_23

) ?? panic("Could not borrow reference to the owner's Vault")

_23

_23

self.sentVault <- vaultRef.withdraw(amount: amount)

_23

}

_23

_23

execute {

_23

let recipient = getAccount(to)

_23

let receiverRef = recipient.capabilities

_23

.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)

_23

?? panic("Could not borrow receiver reference")

_23

_23

receiverRef.deposit(from: <-self.sentVault)

_23

}

_23

}`

The forked emulator disables transaction signature validation, allowing you to send transactions as any address without valid signatures.

Now let's test transferring tokens from a mainnet account using impersonation.

### CLI-Based Impersonation[​](#cli-based-impersonation "Direct link to CLI-Based Impersonation")

To use impersonation with the CLI, you need to add the mainnet account to your `flow.json` (signature validation is disabled, so the key value doesn't matter).

Manually add to your `flow.json` (using the same `blank-key.pkey` file):

`_11

{

_11

"accounts": {

_11

"mainnet-service": {

_11

"address": "0x1654653399040a61",

_11

"key": {

_11

"type": "file",

_11

"location": "blank-key.pkey"

_11

}

_11

}

_11

}

_11

}`

Transfer tokens from the mainnet service account to another mainnet account:

`_10

# Transfer from mainnet service account to any mainnet address (impersonation!)

_10

flow transactions send cadence/transactions/transferTokens.cdc 100.0 0xRECIPIENT_ADDRESS \

_10

--signer mainnet-service \

_10

--network mainnet-fork

_10

_10

# Verify the transfer

_10

flow scripts execute cadence/scripts/getBalance.cdc 0xRECIPIENT_ADDRESS \

_10

--network mainnet-fork`

### Dev Wallet Authentication with Impersonation[​](#dev-wallet-authentication-with-impersonation "Direct link to Dev Wallet Authentication with Impersonation")

The most powerful feature: when connecting your app to the forked emulator with the dev wallet, **you can authenticate as ANY mainnet account** directly in the UI.

Start the dev wallet:

`_10

flow dev-wallet`

In your app (running against the forked emulator), click the wallet connect button. In the dev wallet UI:

1. **Enter any mainnet address** in the address field (e.g., a whale wallet, liquidity provider, or DeFi protocol account)
2. Click "Authenticate"
3. Your app is now authenticated as that mainnet account with all its real balances, liquidity positions, and storage!

**Additional dev wallet features in fork mode:**

* **Fund accounts**: The dev wallet can add FLOW tokens to any account, even real mainnet accounts
* **No configuration needed**: The dev wallet handles impersonation automatically when connected to a forked emulator
* **Full account state**: Access all assets, storage, and capabilities from the real mainnet account

This lets you:

* Test your app as a user with specific assets or permissions
* Debug issues reported by specific mainnet accounts
* Verify flows work for accounts with large balances or complex liquidity positions
* Test edge cases with real account states
* Add test funds to accounts that need more FLOW for testing

How "Impersonation" Works

The forked emulator simply skips signature verification. You can specify any mainnet address as the signer, and the emulator will execute the transaction as that account. Empty or invalid signatures are accepted. This lets you test with real account balances, storage, and capabilities without needing private keys. For frontend flows with the dev wallet, it works the same way—the wallet can "sign" as any address because the emulator doesn't validate signatures.

## Automating with E2E Testing[​](#automating-with-e2e-testing "Direct link to Automating with E2E Testing")

The forked emulator works with any E2E testing framework (Cypress, Playwright, Puppeteer, etc.). This lets you automate your app tests against production-like state.

### Quick Example with Cypress[​](#quick-example-with-cypress "Direct link to Quick Example with Cypress")

`_10

npm install --save-dev cypress`

Create `cypress/e2e/flowFork.cy.js`:

`_10

describe('Flow Fork Test', () => {

_10

it('reads real mainnet data', () => {

_10

cy.visit('http://localhost:3000');

_10

cy.contains('Get FlowToken Supply').click();

_10

cy.contains('Total Supply:', { timeout: 10000 }).should('be.visible');

_10

});

_10

});`

### Running E2E Tests[​](#running-e2e-tests "Direct link to Running E2E Tests")

Run three terminals:

1. **Terminal 1**: `flow emulator --fork mainnet --fork-height <BLOCK_HEIGHT>`
2. **Terminal 2**: `npm start` (your React app)
3. **Terminal 3**: `npx cypress run`

Your tests now run against forked mainnet—**perfect for CI/CD pipelines** with pinned block heights ensuring deterministic results.

tip

Use the same approach with Playwright, Puppeteer, or any browser automation tool. The key is having your app connect to the forked emulator (`http://localhost:8888`) while your E2E framework tests the UI.

## Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

### Testing DeFi Applications[​](#testing-defi-applications "Direct link to Testing DeFi Applications")

Test your DeFi application against real mainnet liquidity and protocols:

1. Fork mainnet at a specific block height
2. Impersonate accounts with large token balances or LP positions
3. Test your swap, lending, or yield farming logic against real DEX state
4. Verify slippage calculations with actual liquidity pool reserves
5. Test edge cases like low liquidity scenarios using real market conditions

**Example: Testing a swap integration**

`_10

# Fork at a known block with specific liquidity conditions

_10

flow emulator --fork mainnet --fork-height <BLOCK_HEIGHT>

_10

_10

# In your test, impersonate a whale account

_10

# Execute swaps against real DEX contracts (IncrementFi, etc.)

_10

# Verify your price calculations match actual execution`

This lets you test against production liquidity without spending real tokens or affecting live markets.

### Testing Contract Upgrades[​](#testing-contract-upgrades "Direct link to Testing Contract Upgrades")

Test a contract upgrade against real mainnet state by mocking the contract with your upgraded version:

1. Configure the mock in `flow.json` (see [Mocking Mainnet Contracts](#mocking-mainnet-contracts))
2. Start the forked emulator
3. Deploy your upgraded contract: `flow project deploy --network mainnet-fork --update`
4. Test your app against the upgraded contract with all real mainnet state intact
5. Verify existing integrations and users aren't broken by the upgrade

### Debugging User-Reported Issues[​](#debugging-user-reported-issues "Direct link to Debugging User-Reported Issues")

Reproduce a bug at the exact block height it occurred:

`_10

flow emulator --fork mainnet --fork-height <BLOCK_HEIGHT>`

Then manually interact with your app or run specific transactions to reproduce the issue.

### Testing Wallet Integrations[​](#testing-wallet-integrations "Direct link to Testing Wallet Integrations")

Test wallet connect flows, transaction signing, and account creation against production-like state:

1. Start forked emulator and dev wallet
2. Use your app to authenticate
3. Sign transactions as real mainnet accounts (via impersonation)
4. Verify balance updates, event emissions, etc.

### Running Bots and Indexers[​](#running-bots-and-indexers "Direct link to Running Bots and Indexers")

Test automated tools against forked data by pointing your SDK to the local emulator:

**Any Flow SDK works:**

* **JavaScript/TypeScript**: `@onflow/fcl`
* **Go**: `flow-go-sdk`
* **Python**: `flow-py-sdk`
* **Other languages**: Configure to connect to `http://localhost:8888`

**Example with JavaScript:**

`_11

// Node.js bot that monitors FlowToken transfers

_11

const fcl = require('@onflow/fcl');

_11

_11

fcl.config({

_11

'accessNode.api': 'http://localhost:8888', // Point to forked emulator

_11

});

_11

_11

async function monitorTransfers() {

_11

// Subscribe to blocks and process FlowToken events

_11

// Bot reads real mainnet data but runs locally

_11

}`

**Example with Go:**

`_10

import "github.com/onflow/flow-go-sdk/client"

_10

_10

// Connect to forked emulator

_10

flowClient, err := client.New("localhost:3569", grpc.WithInsecure())

_10

_10

// Your bot/indexer logic reads from forked mainnet state`

## Best Practices[​](#best-practices "Direct link to Best Practices")

### 1. Pin Block Heights for Reproducibility[​](#1-pin-block-heights-for-reproducibility "Direct link to 1. Pin Block Heights for Reproducibility")

Always pin heights in E2E tests and CI:

`_10

flow emulator --fork mainnet --fork-height 85432100`

**Why:** Ensures tests run against identical state every time.

### 2. Keep Emulator Running During Development[​](#2-keep-emulator-running-during-development "Direct link to 2. Keep Emulator Running During Development")

Start the forked emulator once and leave it running. Restart only when you need to change the fork height or network.

### 3. Use Testnet Before Mainnet[​](#3-use-testnet-before-mainnet "Direct link to 3. Use Testnet Before Mainnet")

Test against testnet first to avoid mainnet access node rate limits:

`_10

flow emulator --fork testnet --fork-height <BLOCK_HEIGHT>`

### 4. Mock External Dependencies[​](#4-mock-external-dependencies "Direct link to 4. Mock External Dependencies")

The forked emulator only mirrors Flow blockchain state. External APIs, oracles, and cross-chain data won't work. Mock them in your E2E tests:

`_10

// In Cypress: Mock external oracle response

_10

cy.intercept('GET', 'https://api.example.com/price', {

_10

statusCode: 200,

_10

body: { price: 123.45 },

_10

});`

In your React app, you can mock API calls during testing while keeping real implementations for production.

### 5. Test Against Real User Accounts[​](#5-test-against-real-user-accounts "Direct link to 5. Test Against Real User Accounts")

The forked emulator disables signature validation, so you can transact as any mainnet account. Just reference the address—empty or invalid signatures are accepted:

`_10

# Execute a transaction as any mainnet account

_10

flow transactions send my_transaction.cdc \

_10

--signer 0x1234567890abcdef \

_10

--network mainnet-fork`

This lets you test with real whale wallets, liquidity provider accounts, or any address that has interesting DeFi state on mainnet.

### 6. Document Your Fork Heights[​](#6-document-your-fork-heights "Direct link to 6. Document Your Fork Heights")

Keep a log of which block heights you use for testing and why:

`_10

# .env.test

_10

FORK_HEIGHT_STABLE=<BLOCK_HEIGHT_1> # Known stable state

_10

FORK_HEIGHT_LATEST=<BLOCK_HEIGHT_2> # Latest tested state`

## Limitations and Considerations[​](#limitations-and-considerations "Direct link to Limitations and Considerations")

### Network State Fetching[​](#network-state-fetching "Direct link to Network State Fetching")

Fork mode fetches state from the access node on-demand. The first access to an account or contract fetches data over the network; subsequent accesses benefit from caching. With pinned block heights, caching is very effective.

### Spork Boundaries[​](#spork-boundaries "Direct link to Spork Boundaries")

Historical data is only available within the current spork. You cannot fork to block heights from previous sporks via public access nodes.

See: [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade).

### Off-Chain Services[​](#off-chain-services "Direct link to Off-Chain Services")

The fork only includes Flow blockchain state. External services don't work:

* **Oracles**: Mock responses
* **IPFS/Arweave**: Mock or run local nodes
* **Cross-chain bridges**: Mock or test separately

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Emulator Won't Start[​](#emulator-wont-start "Direct link to Emulator Won't Start")

**Error:** `network "mainnet" not found in flow.json`

**Solution:** Make sure your `flow.json` includes the mainnet network:

`_10

{

_10

"networks": {

_10

"mainnet": "access.mainnet.nodes.onflow.org:9000"

_10

}

_10

}`

Or use `--fork-host` directly:

`_10

flow emulator --fork-host access.mainnet.nodes.onflow.org:9000`

### Contract Import Fails[​](#contract-import-fails "Direct link to Contract Import Fails")

**Error:** `import "FlowToken" could not be resolved`

**Solution:** Make sure you've installed dependencies with the mainnet alias:

`_10

flow dependencies install FlowToken FungibleToken`

Verify the contract has a mainnet alias that the fork can inherit.

### App Can't Connect[​](#app-cant-connect "Direct link to App Can't Connect")

**Error:** Frontend can't reach the emulator

**Solution:** Verify FlowProvider is configured correctly:

`_10

<FlowProvider

_10

config={{

_10

accessNodeUrl: 'http://localhost:8888', // Must match emulator REST port

_10

flowNetwork: 'mainnet-fork', // Use your fork network from flow.json

_10

}}

_10

flowJson={flowJSON}

_10

>

_10

<App />

_10

</FlowProvider>`

Check the emulator is running and serving on port 8888.

**Common mistakes:**

1. **Wrong network:** Using `flowNetwork: 'emulator'` when forking mainnet will use emulator contract addresses (`0x0ae53cb6...`) instead of mainnet addresses. Use your fork network name (`'mainnet-fork'`).
2. **Missing flowJson prop:** The `flowJson` prop is required for contract import resolution. Make sure you're importing and passing your `flow.json` file.

### Script Returns Stale Data[​](#script-returns-stale-data "Direct link to Script Returns Stale Data")

**Issue:** Script returns unexpected/old values

**Solution:** The fork fetches state at the pinned height or latest. Verify:

`_10

# Check which block the emulator is at

_10

flow blocks get latest --network emulator`

If you need fresher data, restart without `--fork-height`.

### E2E Tests Flaky[​](#e2e-tests-flaky "Direct link to E2E Tests Flaky")

**Issue:** Tests pass sometimes but fail randomly

**Solution:**

1. Pin block height for consistency
2. Add longer timeouts for network calls
3. Check for race conditions in async code

## When to Use Emulator Fork vs Test Framework Fork[​](#when-to-use-emulator-fork-vs-test-framework-fork "Direct link to When to Use Emulator Fork vs Test Framework Fork")

Choose the right tool:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Use Case Tool|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Cadence unit tests `flow test` (no fork)| Cadence integration tests with real contracts `flow test --fork`| Manual testing with app `flow emulator --fork`| E2E testing (Cypress/Playwright) `flow emulator --fork`| Debugging frontend issues `flow emulator --fork`| Testing wallets/bots/indexers `flow emulator --fork` | | | | | | | | | | | | | |

Both modes complement each other. See [Testing Strategy](/build/cadence/smart-contracts/testing-strategy) for the full picture.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to use the forked emulator for interactive testing, E2E test automation, and manual exploration. You created a React app using the Flow React SDK connected to forked mainnet, used account impersonation to test with real account states, and saw how to automate tests with E2E frameworks—all without deploying to a live network.

Now that you have completed this tutorial, you can:

* **Start the emulator in fork mode** with `flow emulator --fork`.
* **Connect your app frontend** to the forked emulator.
* **Test against real mainnet contracts** and production data interactively.
* **Run E2E tests** (Cypress, Playwright) against forked state.
* **Use account impersonation** to test as any mainnet account.
* **Pin to specific block heights** for reproducible testing.
* **Debug and explore** contract interactions manually.

The forked emulator bridges the gap between local development and testnet/mainnet deployments. Use it to catch integration issues early, test against real-world conditions, and validate your app before going live.

### Next Steps[​](#next-steps "Direct link to Next Steps")

* Add E2E tests to your CI/CD pipeline using pinned fork heights
* Test your app's upgrade flows against forked mainnet
* Review the [Fork Testing Overview](/build/tools/flow-cli/fork-testing) for both emulator and test framework fork modes
* For Cadence contract testing, see [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing)
* Explore [Flow React SDK](/build/tools/react-sdk) hooks and components (events, mutations, Cross-VM features)
* Review the [Testing Strategy](/build/cadence/smart-contracts/testing-strategy) for the full testing approach
* Check [Flow Emulator](/build/tools/emulator) docs for advanced emulator flags

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/emulator-fork-testing/index.md)

Last updated on **Dec 16, 2025** by **Jordan Ribbink**

[Previous

Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)[Next

Flow EVM Guides](/blockchain-development-tutorials/evm)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)* [What You'll Build](#what-youll-build)* [Prerequisites](#prerequisites)
      + [Flow CLI](#flow-cli)+ [Node.js and npm](#nodejs-and-npm)+ [Frontend development knowledge](#frontend-development-knowledge)+ [Network access](#network-access)* [Understanding Emulator Fork Mode](#understanding-emulator-fork-mode)
        + [What is `flow emulator --fork`?](#what-is-flow-emulator---fork)+ [When to Use This](#when-to-use-this)+ [Emulator Fork vs Test Framework Fork](#emulator-fork-vs-test-framework-fork)* [Quick Start: Run in 60 Seconds](#quick-start-run-in-60-seconds)* [Create Your Project](#create-your-project)* [Start the Forked Emulator](#start-the-forked-emulator)* [Deploy Your Contracts Against Mainnet State](#deploy-your-contracts-against-mainnet-state)
                + [Example: Deploy and Test Your Contract](#example-deploy-and-test-your-contract)* [Mock Existing Mainnet Contracts](#mock-existing-mainnet-contracts)
                  + [Example: Mock a Mainnet Contract](#example-mock-a-mainnet-contract)* [Install Dependencies](#install-dependencies)* [Test with Flow CLI Scripts](#test-with-flow-cli-scripts)* [Create a React App](#create-a-react-app)
                        + [Configure for Fork Testing](#configure-for-fork-testing)+ [Create a Demo Component](#create-a-demo-component)+ [Start the dev wallet (optional)](#start-the-dev-wallet-optional)+ [Run your app](#run-your-app)* [Account Impersonation](#account-impersonation)
                          + [Read Account Balance](#read-account-balance)+ [Execute Transaction as Any Account](#execute-transaction-as-any-account)+ [CLI-Based Impersonation](#cli-based-impersonation)+ [Dev Wallet Authentication with Impersonation](#dev-wallet-authentication-with-impersonation)* [Automating with E2E Testing](#automating-with-e2e-testing)
                            + [Quick Example with Cypress](#quick-example-with-cypress)+ [Running E2E Tests](#running-e2e-tests)* [Common Use Cases](#common-use-cases)
                              + [Testing DeFi Applications](#testing-defi-applications)+ [Testing Contract Upgrades](#testing-contract-upgrades)+ [Debugging User-Reported Issues](#debugging-user-reported-issues)+ [Testing Wallet Integrations](#testing-wallet-integrations)+ [Running Bots and Indexers](#running-bots-and-indexers)* [Best Practices](#best-practices)
                                + [1. Pin Block Heights for Reproducibility](#1-pin-block-heights-for-reproducibility)+ [2. Keep Emulator Running During Development](#2-keep-emulator-running-during-development)+ [3. Use Testnet Before Mainnet](#3-use-testnet-before-mainnet)+ [4. Mock External Dependencies](#4-mock-external-dependencies)+ [5. Test Against Real User Accounts](#5-test-against-real-user-accounts)+ [6. Document Your Fork Heights](#6-document-your-fork-heights)* [Limitations and Considerations](#limitations-and-considerations)
                                  + [Network State Fetching](#network-state-fetching)+ [Spork Boundaries](#spork-boundaries)+ [Off-Chain Services](#off-chain-services)* [Troubleshooting](#troubleshooting)
                                    + [Emulator Won't Start](#emulator-wont-start)+ [Contract Import Fails](#contract-import-fails)+ [App Can't Connect](#app-cant-connect)+ [Script Returns Stale Data](#script-returns-stale-data)+ [E2E Tests Flaky](#e2e-tests-flaky)* [When to Use Emulator Fork vs Test Framework Fork](#when-to-use-emulator-fork-vs-test-framework-fork)* [Conclusion](#conclusion)
                                        + [Next Steps](#next-steps)

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