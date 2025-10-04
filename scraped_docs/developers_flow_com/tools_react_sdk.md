# Source: https://developers.flow.com/tools/react-sdk

@onflow/react-sdk | Flow Developer Portal



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

        + [@onflow/react-sdk](/build/tools/react-sdk)

          - [Flow React SDK Hooks](/build/tools/react-sdk/hooks)- [Flow React SDK Components](/build/tools/react-sdk/components)+ [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* @onflow/react-sdk

On this page

# @onflow/react-sdk

**The easiest way to build React apps on Flow.** A lightweight, TypeScript-first library that makes Flow blockchain interactions feel native to React development.

🚀 **Quick to setup** – One provider, minimal configuration  
⚡ **Built for performance** – Powered by TanStack Query for optimal caching  
🎨 **Styled beautifully** – Tailwind-based components that match your design  
🔗 **Cross-VM ready** – Seamlessly bridge between Cadence and Flow EVM

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Install[​](#1-install "Direct link to 1. Install")

`_10

npm install @onflow/react-sdk`

### 2. Wrap Your App[​](#2-wrap-your-app "Direct link to 2. Wrap Your App")

`_25

import React from "react"

_25

import App from "./App"

_25

import { FlowProvider } from "@onflow/react-sdk"

_25

import flowJSON from "../flow.json"

_25

_25

function Root() {

_25

return (

_25

<FlowProvider

_25

config={{

_25

accessNodeUrl: "https://access-mainnet.onflow.org",

_25

flowNetwork: "mainnet",

_25

appDetailTitle: "My On Chain App",

_25

appDetailIcon: "https://example.com/icon.png",

_25

appDetailDescription: "A decentralized app on Flow",

_25

appDetailUrl: "https://myonchainapp.com",

_25

}}

_25

flowJson={flowJSON}

_25

darkMode={false}

_25

>

_25

<App />

_25

</FlowProvider>

_25

)

_25

}

_25

_25

export default Root`

Next.js Users

Place the `FlowProvider` inside your `layout.tsx`. Since React hooks must run on the client, you may need to wrap the provider in a separate file that begins with `'use client'` to avoid issues with server-side rendering.

### 3. Start Building[​](#3-start-building "Direct link to 3. Start Building")

`` _18

import { useFlowCurrentUser, Connect, useFlowQuery } from "@onflow/react-sdk"

_18

_18

function MyApp() {

_18

const { user } = useFlowCurrentUser()

_18

_18

const { data: greeting } = useFlowQuery({

_18

cadence: `access(all) fun main(): String { return "Hello, Flow!" }`,

_18

args: (arg, t) => [],

_18

})

_18

_18

return (

_18

<div>

_18

<Connect />

_18

{user?.loggedIn && <p>Welcome, {user.addr}!</p>}

_18

<p>{greeting}</p>

_18

</div>

_18

)

_18

} ``

### Live Demo[​](#live-demo "Direct link to Live Demo")



---

## What's Included[​](#whats-included "Direct link to What's Included")

### 🎣 [Hooks](/build/tools/react-sdk/hooks)[​](#-hooks "Direct link to -hooks")

**Cadence Hooks** for native Flow interactions:

* Authentication & user management
* Account details & balances
* Block & transaction queries
* Real-time event subscriptions
* Script execution & mutations

**Cross-VM Hooks** for bridging Cadence ↔ Flow EVM:

* Atomic batch transactions
* Token & NFT bridging
* Cross-chain balance queries

[→ View all hooks](/build/tools/react-sdk/hooks)

### 🎨 [Components](/build/tools/react-sdk/components)[​](#-components "Direct link to -components")

Beautiful, accessible UI components:

* `<Connect />` – Wallet authentication with balance display
* `<TransactionButton />` – Smart transaction execution
* `<TransactionDialog />` – Real-time transaction tracking
* `<TransactionLink />` – Network-aware block explorer links

[→ View all components](/build/tools/react-sdk/components)

---

## Why Choose React SDK?[​](#why-choose-react-sdk "Direct link to Why Choose React SDK?")

**Developer Experience First**

* TypeScript-native with full type safety
* Familiar React patterns and conventions
* Comprehensive error handling and loading states

**Production Ready**

* Built on battle-tested libraries (TanStack Query, Tailwind CSS)
* Automatic retries, caching, and background updates
* Cross-VM support for hybrid Cadence/EVM applications

**Customizable**

* Theme system for brand consistency
* Composable hooks for custom UI
* Dark mode support out of the box

---

## Need Help?[​](#need-help "Direct link to Need Help?")

* 📖 **[Hooks Documentation](/build/tools/react-sdk/hooks)** – Detailed API reference for all hooks
* 🎨 **[Components Documentation](/build/tools/react-sdk/components)** – UI components and theming guide
* 🔗 **[Configuration Guide](/build/tools/flow-cli/flow.json/configuration)** – Learn about configuring `flow.json`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-sdk/index.md)

Last updated on **Sep 25, 2025** by **Felipe Cevallos**

[Previous

Tools](/build/tools)[Next

Flow React SDK Hooks](/build/tools/react-sdk/hooks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Quick Start](#quick-start)
  + [1. Install](#1-install)+ [2. Wrap Your App](#2-wrap-your-app)+ [3. Start Building](#3-start-building)+ [Live Demo](#live-demo)* [What's Included](#whats-included)
    + [🎣 Hooks](#-hooks)+ [🎨 Components](#-components)* [Why Choose React SDK?](#why-choose-react-sdk)* [Need Help?](#need-help)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.