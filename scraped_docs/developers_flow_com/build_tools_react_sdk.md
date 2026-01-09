# Source: https://developers.flow.com/build/tools/react-sdk

Flow React SDK | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            - [Hooks](/build/tools/react-sdk/hooks)- [Components](/build/tools/react-sdk/components)+ [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* Flow React SDK

On this page

# Flow React SDK

**The easiest way to build React apps on Flow.** A lightweight, TypeScript-first library that makes Flow blockchain interactions feel native to React development.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Install[​](#1-install "Direct link to 1. Install")

`_10

npm install @onflow/react-sdk`

### 2. Wrap Your App[​](#2-wrap-your-app "Direct link to 2. Wrap Your App")

`_25

import React from 'react';

_25

import App from './App';

_25

import { FlowProvider } from '@onflow/react-sdk';

_25

import flowJSON from '../flow.json';

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

accessNodeUrl: 'https://access-mainnet.onflow.org',

_25

flowNetwork: 'mainnet',

_25

appDetailTitle: 'My On Chain App',

_25

appDetailIcon: 'https://example.com/icon.png',

_25

appDetailDescription: 'A decentralized app on Flow',

_25

appDetailUrl: 'https://myonchainapp.com',

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

);

_25

}

_25

_25

export default Root;`

Next.js Users

Create a client component wrapper for the `FlowProvider`:

`_22

'use client';

_22

_22

import { FlowProvider } from '@onflow/react-sdk';

_22

import flowJSON from '../flow.json';

_22

_22

export default function FlowProviderWrapper({ children }) {

_22

return (

_22

<FlowProvider

_22

config={{

_22

accessNodeUrl: 'https://access-mainnet.onflow.org',

_22

flowNetwork: 'mainnet',

_22

appDetailTitle: 'My On Chain App',

_22

appDetailIcon: 'https://example.com/icon.png',

_22

appDetailDescription: 'A decentralized app on Flow',

_22

appDetailUrl: 'https://myonchainapp.com',

_22

}}

_22

flowJson={flowJSON}

_22

>

_22

{children}

_22

</FlowProvider>

_22

);

_22

}`

Then use it in your `layout.tsx`:

`_11

import FlowProviderWrapper from '@/components/FlowProviderWrapper';

_11

_11

export default function RootLayout({ children }) {

_11

return (

_11

<html>

_11

<body>

_11

<FlowProviderWrapper>{children}</FlowProviderWrapper>

_11

</body>

_11

</html>

_11

);

_11

}`

### 3. Start Building[​](#3-start-building "Direct link to 3. Start Building")

`` _18

import { useFlowCurrentUser, Connect, useFlowQuery } from '@onflow/react-sdk';

_18

_18

function MyApp() {

_18

const { user } = useFlowCurrentUser();

_18

_18

const { data: greeting } = useFlowQuery({

_18

cadence: `access(all) fun main(): String { return "Hello, Flow!" }`,

_18

args: (arg, t) => [],

_18

});

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

);

_18

} ``

---

## 🎣 [Hooks](/build/tools/react-sdk/hooks)[​](#-hooks "Direct link to -hooks")

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

---

## 🎨 [Components](/build/tools/react-sdk/components)[​](#-components "Direct link to -components")

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-sdk/index.mdx)

Last updated on **Nov 7, 2025** by **Michael Fabozzi**

[Previous

Components](/build/tools/react-native-sdk/components)[Next

Hooks](/build/tools/react-sdk/hooks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Quick Start](#quick-start)
  + [1. Install](#1-install)+ [2. Wrap Your App](#2-wrap-your-app)+ [3. Start Building](#3-start-building)* [🎣 Hooks](#-hooks)* [🎨 Components](#-components)* [Why Choose React SDK?](#why-choose-react-sdk)* [Need Help?](#need-help)

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