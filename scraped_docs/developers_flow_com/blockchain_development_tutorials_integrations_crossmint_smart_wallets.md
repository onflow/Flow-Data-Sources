# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/crossmint/smart-wallets

Crossmint Smart Wallets | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

                      + [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)

                        - [Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)- [Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)- [Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)- [Crossmint Smart Wallets](/blockchain-development-tutorials/integrations/crossmint/smart-wallets)

* * [Third-Party Integrations](/blockchain-development-tutorials/integrations)* [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)* Crossmint Smart Wallets

On this page

# Crossmint Smart Wallets Integration Guide

Traditional blockchain wallets create significant friction for mainstream users. Managing seed phrases, understanding gas fees, and connecting multiple wallets are barriers that prevent widespread Web3 adoption. Crossmint Smart Wallets solves these problems by providing **enterprise-grade wallet infrastructure** that enables Web2-like user experiences without compromising on security or decentralization.

With Crossmint Smart Wallets, you can:

* **Eliminate wallet complexity** with email and social login authentication.
* **Remove onboarding friction** with automatic user wallet creation.
* **Support multiple authentication methods** such as email, Google, passkeys, and external wallets.
* **Enable gasless transactions** to improve user experience.
* **Build on Flow** with full support for both mainnet and testnet environments.
* **Scale with confidence** using infrastructure trusted by Fortune 500 companies.

This tutorial will guide you through how to integrate Crossmint Smart Wallets into your Flow application. You'll learn how to set up authentication, automatically create wallets, check balances, transfer tokens, and display transaction historyall with a familiar Web2-style developer experience.

info

Crossmint provides flexible wallet solutions across more than 50 blockchains, such as Flow. This tutorial focuses on the **React implementation** for web applications, but Crossmint also supports Node.js, React Native, Swift (iOS), and Kotlin (Android) platforms.

## Objectives[​](#objectives "Direct link to Objectives")

After you complete this guide, you'll be able to:

* Configure a Crossmint account with proper API keys and permissions.
* Implement email and social authentication for automatic wallet creation.
* Display wallet information including address, balance, and ownership details.
* Execute token transfers on Flow using Crossmint's SDK.
* Build an activity feed showing transaction history.
* Handle authentication states and error scenarios properly.
* Deploy your Crossmint-powered application to production.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you start this tutorial, you should have:

* **Development Environment**: Node.js and npm/yarn/pnpm installed.
* **React Knowledge**: Familiarity with React hooks and component patterns.
* **Next.js or Create-React-App**: A React application ready for integration.
* **Basic Blockchain Concepts**: Knowledge of wallet addresses and token transfers (helpful but not required).

## Set up your crossmint account[​](#set-up-your-crossmint-account "Direct link to Set up your crossmint account")

You need to create a Crossmint account and configure API access before you implement wallet functionality.

### Step 1. Create your Crossmint account[​](#step-1-create-your-crossmint-account "Direct link to Step 1. Create your Crossmint account")

Sign up on the [Crossmint Console](https://www.crossmint.com/console) to establish an account. For development and testing, use the [Staging Console](https://staging.crossmint.com/console) instead.

tip

Always use the staging environment during development. Staging supports testnet blockchains only, while production supports mainnet deployments.

### Step 2. Create a new project[​](#step-2-create-a-new-project "Direct link to Step 2. Create a new project")

After you log in to the console:

1. Click **Create New Project**.
2. Enter a project name (such as "Flow DApp").
3. Select your project type (Web Application recommended).
4. Save your project settings.

### Step 3. Generate API keys[​](#step-3-generate-api-keys "Direct link to Step 3. Generate API keys")

Navigate to your project dashboard to create a client-side API key:

1. Go to the **API Keys** section
2. Click **Create New API Key**
3. Select **Client API Key** (not server key)
4. Activate the following scopes:

   * `users.create` - Create new users
   * `users.read` - Read user information
   * `wallets.read` - Read wallet data
   * `wallets.create` - Create new wallets
   * `wallets:transactions.create` - Create transactions
   * `wallets:transactions.sign` - Sign transactions
   * `wallets:balance.read` - Read balance information
   * `wallets.fund` - Fund wallets (staging and development only)
5. Copy the generated API key to your clipboard

warning

Keep your API keys secure! Never commit them to version control. Use environment variables to store sensitive credentials.

### Step 4. Configure environment variables[​](#step-4-configure-environment-variables "Direct link to Step 4. Configure environment variables")

Create a `.env` or `.env.local` file in your project root:

`_10

NEXT_PUBLIC_CROSSMINT_API_KEY=your_api_key_here

_10

NEXT_PUBLIC_CHAIN=flow-testnet`

For production deployments, update to:

`_10

NEXT_PUBLIC_CROSSMINT_API_KEY=your_production_api_key

_10

NEXT_PUBLIC_CHAIN=flow`

## Implement Crossmint Smart Wallets[​](#implement-crossmint-smart-wallets "Direct link to Implement Crossmint Smart Wallets")

With your Crossmint account configured, you can now integrate wallet functionality into your React application.

### Step 1. Install dependencies[​](#step-1-install-dependencies "Direct link to Step 1. Install dependencies")

Install the Crossmint React SDK:

* pnpm* bun* yarn* npm

`_10

pnpm add @crossmint/client-sdk-react-ui`

`_10

bun add @crossmint/client-sdk-react-ui`

`_10

yarn add @crossmint/client-sdk-react-ui`

`_10

npm install @crossmint/client-sdk-react-ui`

### Step 2. Configure Crossmint providers[​](#step-2-configure-crossmint-providers "Direct link to Step 2. Configure Crossmint providers")

Crossmint requires three providers to be set up in a specific hierarchy. These providers handle API configuration, authentication, and wallet management.

* Next.js App Router* Create-React-App

Create a new file `app/providers.tsx`:

`_40

"use client";

_40

_40

import {

_40

CrossmintProvider,

_40

CrossmintAuthProvider,

_40

CrossmintWalletProvider,

_40

} from "@crossmint/client-sdk-react-ui";

_40

_40

if (!process.env.NEXT_PUBLIC_CROSSMINT_API_KEY) {

_40

throw new Error("NEXT_PUBLIC_CROSSMINT_API_KEY is not set");

_40

}

_40

_40

const chain = (process.env.NEXT_PUBLIC_CHAIN ?? "flow-testnet") as any;

_40

_40

export function Providers({ children }: { children: React.ReactNode }) {

_40

return (

_40

<CrossmintProvider apiKey={process.env.NEXT_PUBLIC_CROSSMINT_API_KEY}>

_40

<CrossmintAuthProvider

_40

authModalTitle="Welcome to Flow"

_40

loginMethods={["google", "email"]}

_40

appearance={{

_40

colors: {

_40

accent: "#00EF8B", // Flow brand color

_40

},

_40

}}

_40

>

_40

<CrossmintWalletProvider

_40

createOnLogin={{

_40

chain: chain,

_40

signer: {

_40

type: "email",

_40

},

_40

}}

_40

>

_40

{children}

_40

</CrossmintWalletProvider>

_40

</CrossmintAuthProvider>

_40

</CrossmintProvider>

_40

);

_40

}`

Then wrap your app in `app/layout.tsx`:

`_15

import { Providers } from "./providers";

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

<Providers>{children}</Providers>

_15

</body>

_15

</html>

_15

);

_15

}`

Update your `src/index.tsx` or `src/index.jsx`:

`_41

import React from 'react';

_41

import ReactDOM from 'react-dom/client';

_41

import App from './App';

_41

import {

_41

CrossmintProvider,

_41

CrossmintAuthProvider,

_41

CrossmintWalletProvider,

_41

} from "@crossmint/client-sdk-react-ui";

_41

_41

const chain = process.env.REACT_APP_CHAIN ?? "flow-testnet";

_41

const apiKey = process.env.REACT_APP_CROSSMINT_API_KEY;

_41

_41

if (!apiKey) {

_41

throw new Error("REACT_APP_CROSSMINT_API_KEY is not set");

_41

}

_41

_41

const root = ReactDOM.createRoot(document.getElementById('root'));

_41

root.render(

_41

<React.StrictMode>

_41

<CrossmintProvider apiKey={apiKey}>

_41

<CrossmintAuthProvider

_41

authModalTitle="Welcome to Flow"

_41

loginMethods={["google", "email"]}

_41

appearance={{

_41

colors: {

_41

accent: "#00EF8B",

_41

},

_41

}}

_41

>

_41

<CrossmintWalletProvider

_41

createOnLogin={{

_41

chain: chain,

_41

signer: { type: "email" },

_41

}}

_41

>

_41

<App />

_41

</CrossmintWalletProvider>

_41

</CrossmintAuthProvider>

_41

</CrossmintProvider>

_41

</React.StrictMode>

_41

);`

**Provider configuration cptions:**

* **CrossmintProvider**: Top-level provider that requires only your API key.
* **CrossmintAuthProvider**: Manages authentication with configurable options:
  + `authModalTitle`: Title displayed in the authentication modal.
  + `loginMethods`: Array of active authentication methods (`"email"`, `"google"`, `"apple"`, `"twitter"`, `"farcaster"`).
  + `appearance`: Customize UI colors and style.
* **CrossmintWalletProvider**: Handles wallet creation and management:
  + `createOnLogin.chain`: Target blockchain (such as `"flow"`, `"flow-testnet"`)
  + `createOnLogin.signer.type`: Authentication method for wallet signing (`"email"`, `"passkey"`).

info

The `createOnLogin` configuration enables **automatic wallet creation**. When a user logs in for the first time, Crossmint automatically provisions a wallet on the specified chain. No additional setup required!

### Step 3. Implement authentication[​](#step-3-implement-authentication "Direct link to Step 3. Implement authentication")

Create login and logout components with Crossmint's `useAuth` hook.

**LoginButton.tsx:**

`_16

"use client";

_16

_16

import { useAuth } from "@crossmint/client-sdk-react-ui";

_16

_16

export function LoginButton() {

_16

const { login } = useAuth();

_16

_16

return (

_16

<button

_16

className="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors"

_16

onClick={login}

_16

>

_16

Sign In

_16

</button>

_16

);

_16

}`

**LogoutButton.tsx:**

`_16

"use client";

_16

_16

import { useAuth } from "@crossmint/client-sdk-react-ui";

_16

_16

export function LogoutButton() {

_16

const { logout } = useAuth();

_16

_16

return (

_16

<button

_16

className="px-4 py-2 bg-white text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"

_16

onClick={logout}

_16

>

_16

Sign Out

_16

</button>

_16

);

_16

}`

**Header.tsx (Conditional rendering):**

`_21

"use client";

_21

_21

import { useAuth, useWallet } from "@crossmint/client-sdk-react-ui";

_21

import { LoginButton } from "./LoginButton";

_21

import { LogoutButton } from "./LogoutButton";

_21

_21

export function Header() {

_21

const { status: authStatus } = useAuth();

_21

const { wallet } = useWallet();

_21

_21

const isLoggedIn = wallet != null && authStatus === "logged-in";

_21

_21

return (

_21

<header className="border-b">

_21

<div className="container mx-auto px-4 py-4 flex justify-between items-center">

_21

<h1 className="text-2xl font-bold">Flow DApp</h1>

_21

{isLoggedIn ? <LogoutButton /> : <LoginButton />}

_21

</div>

_21

</header>

_21

);

_21

}`

### Step 4. Display wallet information[​](#step-4-display-wallet-information "Direct link to Step 4. Display wallet information")

Create a component to show wallet details with the `useWallet` hook.

**WalletInfo.tsx:**

`` _65

"use client";

_65

_65

import { useState } from "react";

_65

import { useAuth, useWallet } from "@crossmint/client-sdk-react-ui";

_65

_65

export function WalletInfo() {

_65

const { wallet, status } = useWallet();

_65

const { user } = useAuth();

_65

const [copied, setCopied] = useState(false);

_65

_65

if (status === "in-progress") {

_65

return (

_65

<div className="bg-white rounded-lg p-6 border">

_65

<div className="animate-pulse">Loading wallet...</div>

_65

</div>

_65

);

_65

}

_65

_65

if (!wallet) {

_65

return null;

_65

}

_65

_65

const formatAddress = (address: string) => {

_65

return `${address.slice(0, 6)}...${address.slice(-6)}`;

_65

};

_65

_65

const handleCopy = async () => {

_65

await navigator.clipboard.writeText(wallet.address);

_65

setCopied(true);

_65

setTimeout(() => setCopied(false), 2000);

_65

};

_65

_65

return (

_65

<div className="bg-white rounded-lg p-6 border">

_65

<h2 className="text-xl font-semibold mb-4">Wallet Details</h2>

_65

_65

<div className="space-y-3">

_65

<div>

_65

<div className="text-sm text-gray-500 mb-1">Address</div>

_65

<div className="flex items-center gap-2">

_65

<code className="text-sm bg-gray-100 px-3 py-2 rounded">

_65

{formatAddress(wallet.address)}

_65

</code>

_65

<button

_65

onClick={handleCopy}

_65

className="text-sm px-3 py-2 bg-gray-100 rounded hover:bg-gray-200"

_65

>

_65

{copied ? "Copied!" : "Copy"}

_65

</button>

_65

</div>

_65

</div>

_65

_65

<div>

_65

<div className="text-sm text-gray-500 mb-1">Chain</div>

_65

<div className="font-medium">{wallet.chain}</div>

_65

</div>

_65

_65

<div>

_65

<div className="text-sm text-gray-500 mb-1">Owner</div>

_65

<div className="font-medium">{user?.email || wallet.owner}</div>

_65

</div>

_65

</div>

_65

</div>

_65

);

_65

} ``

### Step 5. Display wallet balance[​](#step-5-display-wallet-balance "Direct link to Step 5. Display wallet balance")

Fetch and display the wallet's token balance with the `wallet.balances()` method.

**WalletBalance.tsx:**

`_69

"use client";

_69

_69

import { useEffect, useState } from "react";

_69

import { Balances, useWallet } from "@crossmint/client-sdk-react-ui";

_69

_69

export function WalletBalance() {

_69

const { wallet } = useWallet();

_69

const [balances, setBalances] = useState<Balances | null>(null);

_69

const [isLoading, setIsLoading] = useState(true);

_69

_69

useEffect(() => {

_69

async function fetchBalances() {

_69

if (!wallet) return;

_69

_69

try {

_69

setIsLoading(true);

_69

const balances = await wallet.balances();

_69

setBalances(balances);

_69

} catch (error) {

_69

console.error("Error fetching wallet balances:", error);

_69

} finally {

_69

setIsLoading(false);

_69

}

_69

}

_69

_69

fetchBalances();

_69

}, [wallet]);

_69

_69

if (isLoading) {

_69

return (

_69

<div className="bg-white rounded-lg p-6 border">

_69

<div className="animate-pulse">Loading balance...</div>

_69

</div>

_69

);

_69

}

_69

_69

const nativeBalance = balances?.nativeToken?.amount

_69

? Number(balances.nativeToken.amount).toFixed(4)

_69

: "0.0000";

_69

_69

return (

_69

<div className="bg-white rounded-lg p-6 border">

_69

<h2 className="text-xl font-semibold mb-4">Balance</h2>

_69

_69

<div className="space-y-4">

_69

<div>

_69

<div className="text-sm text-gray-500 mb-1">

_69

{balances?.nativeToken?.symbol || "FLOW"}

_69

</div>

_69

<div className="text-3xl font-bold">{nativeBalance}</div>

_69

</div>

_69

_69

{balances?.tokens && balances.tokens.length > 0 && (

_69

<div className="pt-4 border-t">

_69

<div className="text-sm font-medium text-gray-700 mb-2">Tokens</div>

_69

{balances.tokens.map((token, index) => (

_69

<div key={index} className="flex justify-between py-2">

_69

<span className="text-gray-600">{token.symbol}</span>

_69

<span className="font-medium">

_69

{Number(token.amount).toFixed(2)}

_69

</span>

_69

</div>

_69

))}

_69

</div>

_69

)}

_69

</div>

_69

</div>

_69

);

_69

}`

### Step 6. Implement token transfers[​](#step-6-implement-token-transfers "Direct link to Step 6. Implement token transfers")

Create a component to transfer tokens with the `wallet.send()` method.

**TransferTokens.tsx:**

`_117

"use client";

_117

_117

import { useState } from "react";

_117

import { useWallet } from "@crossmint/client-sdk-react-ui";

_117

_117

export function TransferTokens() {

_117

const { wallet } = useWallet();

_117

const [recipient, setRecipient] = useState("");

_117

const [amount, setAmount] = useState("");

_117

const [isLoading, setIsLoading] = useState(false);

_117

const [explorerLink, setExplorerLink] = useState<string | null>(null);

_117

const [error, setError] = useState<string | null>(null);

_117

_117

async function handleTransfer() {

_117

if (!wallet || !recipient || !amount) {

_117

setError("Please fill in all fields");

_117

return;

_117

}

_117

_117

try {

_117

setIsLoading(true);

_117

setError(null);

_117

setExplorerLink(null);

_117

_117

const txn = await wallet.send(

_117

recipient,

_117

"flow", // Token symbol - use native FLOW token

_117

amount

_117

);

_117

_117

setExplorerLink(txn.explorerLink);

_117

_117

// Reset form

_117

setRecipient("");

_117

setAmount("");

_117

} catch (err) {

_117

console.error("Transfer error:", err);

_117

_117

if (err instanceof Error && err.name === "AuthRejectedError") {

_117

// User cancelled the transaction - don't show error

_117

return;

_117

}

_117

_117

setError(err instanceof Error ? err.message : "Transfer failed");

_117

} finally {

_117

setIsLoading(false);

_117

}

_117

}

_117

_117

return (

_117

<div className="bg-white rounded-lg p-6 border">

_117

<h2 className="text-xl font-semibold mb-4">Transfer Tokens</h2>

_117

_117

<div className="space-y-4">

_117

<div>

_117

<label className="block text-sm font-medium text-gray-700 mb-2">

_117

Amount

_117

</label>

_117

<input

_117

type="number"

_117

inputMode="decimal"

_117

step="0.01"

_117

value={amount}

_117

onChange={(e) => setAmount(e.target.value)}

_117

placeholder="0.00"

_117

className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"

_117

disabled={isLoading}

_117

/>

_117

</div>

_117

_117

<div>

_117

<label className="block text-sm font-medium text-gray-700 mb-2">

_117

Recipient Address

_117

</label>

_117

<input

_117

type="text"

_117

value={recipient}

_117

onChange={(e) => setRecipient(e.target.value)}

_117

placeholder="0x..."

_117

className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent font-mono text-sm"

_117

disabled={isLoading}

_117

/>

_117

</div>

_117

_117

{error && (

_117

<div className="p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">

_117

{error}

_117

</div>

_117

)}

_117

_117

{explorerLink && (

_117

<div className="p-3 bg-green-50 border border-green-200 rounded-lg">

_117

<div className="text-green-700 text-sm mb-2">

_117

Transaction successful!

_117

</div>

_117

<a

_117

href={explorerLink}

_117

target="_blank"

_117

rel="noopener noreferrer"

_117

className="text-blue-600 hover:text-blue-800 text-sm underline"

_117

>

_117

View on Explorer �

_117

</a>

_117

</div>

_117

)}

_117

_117

<button

_117

onClick={handleTransfer}

_117

disabled={isLoading || !recipient || !amount}

_117

className="w-full py-3 px-4 bg-black text-white rounded-lg font-medium hover:bg-gray-800 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"

_117

>

_117

{isLoading ? "Transferring..." : "Transfer"}

_117

</button>

_117

</div>

_117

</div>

_117

);

_117

}`

tip

The `wallet.send()` method throws an `AuthRejectedError` when users cancel the transaction. Handle this separately to avoid a display of unnecessary error messages.

### Step 7. Build activity feed[​](#step-7-build-activity-feed "Direct link to Step 7. Build activity feed")

Display transaction history with the `wallet.experimental_activity()` method with polling for real-time updates.

**ActivityFeed.tsx:**

`` _117

"use client";

_117

_117

import { useEffect, useState } from "react";

_117

import { type Activity, useWallet } from "@crossmint/client-sdk-react-ui";

_117

_117

export function ActivityFeed() {

_117

const { wallet } = useWallet();

_117

const [activity, setActivity] = useState<Activity | null>(null);

_117

const [isLoading, setIsLoading] = useState(true);

_117

_117

useEffect(() => {

_117

if (!wallet) return;

_117

_117

const fetchActivity = async () => {

_117

try {

_117

const activity = await wallet.experimental_activity();

_117

setActivity(activity);

_117

setIsLoading(false);

_117

} catch (error) {

_117

console.error("Failed to fetch activity:", error);

_117

setIsLoading(false);

_117

}

_117

};

_117

_117

// Initial fetch

_117

fetchActivity();

_117

_117

// Poll every 8 seconds for updates

_117

const interval = setInterval(fetchActivity, 8000);

_117

_117

return () => clearInterval(interval);

_117

}, [wallet]);

_117

_117

const formatAddress = (address: string) => {

_117

return `${address.slice(0, 6)}...${address.slice(-6)}`;

_117

};

_117

_117

const formatTimestamp = (timestamp: number) => {

_117

// Handle both seconds and milliseconds

_117

const date = new Date(

_117

timestamp < 10000000000 ? timestamp * 1000 : timestamp

_117

);

_117

const now = new Date();

_117

const diffInMs = now.getTime() - date.getTime();

_117

_117

if (diffInMs < 0) return "just now";

_117

_117

const diffInMinutes = Math.floor(diffInMs / (1000 * 60));

_117

const diffInHours = Math.floor(diffInMs / (1000 * 60 * 60));

_117

const diffInDays = Math.floor(diffInMs / (1000 * 60 * 60 * 24));

_117

_117

if (diffInMinutes < 1) return "just now";

_117

else if (diffInMinutes < 60) return `${diffInMinutes}m ago`;

_117

else if (diffInHours < 24) return `${diffInHours}h ago`;

_117

else return `${diffInDays}d ago`;

_117

};

_117

_117

if (isLoading) {

_117

return (

_117

<div className="bg-white rounded-lg p-6 border">

_117

<div className="animate-pulse">Loading activity...</div>

_117

</div>

_117

);

_117

}

_117

_117

return (

_117

<div className="bg-white rounded-lg p-6 border">

_117

<h2 className="text-xl font-semibold mb-4">Recent Activity</h2>

_117

_117

{activity?.events && activity.events.length > 0 ? (

_117

<div className="space-y-3">

_117

{activity.events.map((event, index) => {

_117

const isIncoming =

_117

event.to_address?.toLowerCase() === wallet?.address.toLowerCase();

_117

_117

return (

_117

<div

_117

key={event.transaction_hash || index}

_117

className="flex items-center justify-between p-4 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors"

_117

>

_117

<div className="flex-1">

_117

<div className="flex items-center gap-2 mb-1">

_117

<span className={`font-medium ${isIncoming ? "text-green-600" : "text-blue-600"}`}>

_117

{isIncoming ? "Received" : "Sent"}

_117

</span>

_117

<span className="text-xs text-gray-500">

_117

{formatTimestamp(event.timestamp)}

_117

</span>

_117

</div>

_117

<div className="text-sm text-gray-600">

_117

{isIncoming

_117

? `From ${formatAddress(event.from_address)}`

_117

: `To ${formatAddress(event.to_address)}`

_117

}

_117

</div>

_117

</div>

_117

<div className={`text-right ${isIncoming ? "text-green-600" : "text-blue-600"}`}>

_117

<div className="font-semibold">

_117

{isIncoming ? "+" : "-"}{event.amount}

_117

</div>

_117

<div className="text-xs text-gray-500">

_117

{event.token_symbol || "FLOW"}

_117

</div>

_117

</div>

_117

</div>

_117

);

_117

})}

_117

</div>

_117

) : (

_117

<div className="text-center py-8 text-gray-500">

_117

<p>No transactions yet</p>

_117

<p className="text-sm mt-2">Your activity will appear here</p>

_117

</div>

_117

)}

_117

</div>

_117

);

_117

} ``

warning

The `experimental_activity()` method is experimental and may change in future SDK versions. Always handle errors gracefully and provide fallback UI.

### Step 8. Create main dashboard[​](#step-8-create-main-dashboard "Direct link to Step 8. Create main dashboard")

Combine all components into a cohesive dashboard with proper state management.

**Dashboard.tsx:**

`_24

"use client";

_24

_24

import { WalletInfo } from "./WalletInfo";

_24

import { WalletBalance } from "./WalletBalance";

_24

import { TransferTokens } from "./TransferTokens";

_24

import { ActivityFeed } from "./ActivityFeed";

_24

_24

export function Dashboard() {

_24

return (

_24

<div className="container mx-auto px-4 py-8">

_24

<div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

_24

<div className="space-y-6">

_24

<WalletInfo />

_24

<WalletBalance />

_24

</div>

_24

_24

<div className="space-y-6">

_24

<TransferTokens />

_24

<ActivityFeed />

_24

</div>

_24

</div>

_24

</div>

_24

);

_24

}`

**page.tsx (Main application):**

`_43

"use client";

_43

_43

import { useAuth, useWallet } from "@crossmint/client-sdk-react-ui";

_43

import { Header } from "@/components/Header";

_43

import { Dashboard } from "@/components/Dashboard";

_43

import { LoginButton } from "@/components/LoginButton";

_43

_43

export default function Home() {

_43

const { wallet, status: walletStatus } = useWallet();

_43

const { status: authStatus } = useAuth();

_43

_43

const isLoggedIn = wallet != null && authStatus === "logged-in";

_43

const isLoading = walletStatus === "in-progress" || authStatus === "initializing";

_43

_43

return (

_43

<div className="min-h-screen bg-gray-50">

_43

<Header />

_43

_43

<main className="flex-1">

_43

{isLoading ? (

_43

<div className="flex items-center justify-center min-h-[60vh]">

_43

<div className="text-center">

_43

<div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto mb-4"></div>

_43

<p className="text-gray-600">Initializing wallet...</p>

_43

</div>

_43

</div>

_43

) : isLoggedIn ? (

_43

<Dashboard />

_43

) : (

_43

<div className="flex items-center justify-center min-h-[60vh]">

_43

<div className="text-center max-w-md">

_43

<h1 className="text-4xl font-bold mb-4">Welcome to Flow</h1>

_43

<p className="text-gray-600 mb-8">

_43

Sign in to access your wallet and start transacting on Flow blockchain

_43

</p>

_43

<LoginButton />

_43

</div>

_43

</div>

_43

)}

_43

</main>

_43

</div>

_43

);

_43

}`

---

## Additional Platform Support[​](#additional-platform-support "Direct link to Additional Platform Support")

While this tutorial focuses on React for web applications, Crossmint provides SDKs for multiple platforms:

### Node.js (Backend)[​](#nodejs-backend "Direct link to Node.js (Backend)")

For server-side wallet creation and management, use the Node.js SDK:

* [Node.js Quickstart Documentation](https://docs.crossmint.com/wallets/quickstarts/nodejs)

### React Native (Mobile)[​](#react-native-mobile "Direct link to React Native (Mobile)")

For iOS and Android mobile applications:

* [React Native Quickstart Documentation](https://docs.crossmint.com/wallets/quickstarts/react-native)

### Swift (iOS Native)[​](#swift-ios-native "Direct link to Swift (iOS Native)")

For native iOS development:

* Contact [Crossmint Sales](https://www.crossmint.com/contact/sales) for access

### Kotlin (Android Native)[​](#kotlin-android-native "Direct link to Kotlin (Android Native)")

For native Android development:

* Contact [Crossmint Sales](https://www.crossmint.com/contact/sales) for access

---

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you successfully integrated Crossmint Smart Wallets to enable seamless blockchain experiences on Flow. You learned how to implement email-based authentication, automatically create wallets for users, display balances, execute token transfers, and show transaction history, all without a requirement that users understand complex blockchain concepts like seed phrases or gas fees.

Now that you have completed the tutorial, you should be able to:

* Configure Crossmint accounts with proper API keys and permissions
* Implement multiple authentication methods including email and social login
* Automatically create and manage wallets for users
* Display wallet information, balances, and transaction history
* Execute token transfers with proper error handling
* Build production-ready applications with enterprise-grade wallet infrastructure

Crossmint's wallet infrastructure, combined with Flow's high-performance blockchain, provides a powerful foundation for building user-friendly Web3 applications. By eliminating wallet complexity and onboarding friction, you can create experiences that attract mainstream users while maintaining the security and transparency benefits of blockchain technology.

## Next Steps[​](#next-steps "Direct link to Next Steps")

* Explore [Crossmint's NFT Minting Platform](https://docs.crossmint.com/nft-minting/overview)to add NFT functionality
* Learn about [Payment Checkout](https://docs.crossmint.com/payments/overview) for credit card and crypto payments
* Implement [Passkey Authentication](https://docs.crossmint.com/wallets/signers/passkey) for enhanced security
* Review [Flow Smart Contract Development](/blockchain-development-tutorials/cadence) to build custom on-chain logic
* Join the [Flow Discord](https://discord.gg/flow) to connect with other developers

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/integrations/crossmint/smart-wallets.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)* [Prerequisites](#prerequisites)* [Set up your crossmint account](#set-up-your-crossmint-account)
      + [Step 1. Create your Crossmint account](#step-1-create-your-crossmint-account)+ [Step 2. Create a new project](#step-2-create-a-new-project)+ [Step 3. Generate API keys](#step-3-generate-api-keys)+ [Step 4. Configure environment variables](#step-4-configure-environment-variables)* [Implement Crossmint Smart Wallets](#implement-crossmint-smart-wallets)
        + [Step 1. Install dependencies](#step-1-install-dependencies)+ [Step 2. Configure Crossmint providers](#step-2-configure-crossmint-providers)+ [Step 3. Implement authentication](#step-3-implement-authentication)+ [Step 4. Display wallet information](#step-4-display-wallet-information)+ [Step 5. Display wallet balance](#step-5-display-wallet-balance)+ [Step 6. Implement token transfers](#step-6-implement-token-transfers)+ [Step 7. Build activity feed](#step-7-build-activity-feed)+ [Step 8. Create main dashboard](#step-8-create-main-dashboard)* [Additional Platform Support](#additional-platform-support)
          + [Node.js (Backend)](#nodejs-backend)+ [React Native (Mobile)](#react-native-mobile)+ [Swift (iOS Native)](#swift-ios-native)+ [Kotlin (Android Native)](#kotlin-android-native)* [Conclusion](#conclusion)* [Next Steps](#next-steps)

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