# Source: https://developers.flow.com/build/tools/react-native-sdk

Flow React Native SDK | Flow Developer Portal



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

* * [Tools & SDKs](/build/tools)* Flow React Native SDK

On this page

# Flow React Native SDK

**The easiest way to build React Native apps on Flow.** A lightweight, TypeScript-first library for seamless Flow blockchain integration in your React Native apps.

note

This SDK shares the same hooks as the [Flow React SDK](/build/tools/react-sdk), so if you're familiar with the web version, you'll feel right at home. The main differences are the React Native-specific components (`Connect`, `Profile`) and mobile wallet integrations.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Install[​](#1-install "Direct link to 1. Install")

`_10

npm install @onflow/react-native-sdk`

### 2. Wrap Your App[​](#2-wrap-your-app "Direct link to 2. Wrap Your App")

Create a provider wrapper component:

`_33

import { FlowProvider } from '@onflow/react-native-sdk';

_33

import flowJSON from '../flow.json';

_33

_33

export function FlowProviderWrapper({

_33

children,

_33

}: {

_33

children: React.ReactNode;

_33

}) {

_33

return (

_33

<FlowProvider

_33

config={{

_33

// Network configuration

_33

accessNodeUrl: 'https://rest-testnet.onflow.org',

_33

discoveryWallet: 'https://fcl-discovery.onflow.org/testnet/authn',

_33

discoveryAuthnEndpoint:

_33

'https://fcl-discovery.onflow.org/api/testnet/authn',

_33

flowNetwork: 'testnet',

_33

_33

// App metadata (displayed in wallet)

_33

appDetailTitle: 'My Flow App',

_33

appDetailUrl: 'https://myapp.com',

_33

appDetailIcon: 'https://myapp.com/icon.png',

_33

appDetailDescription: 'A Flow blockchain app built with Expo',

_33

_33

// WalletConnect project ID (get one at https://cloud.walletconnect.com)

_33

walletconnectProjectId: 'YOUR_PROJECT_ID',

_33

}}

_33

flowJson={flowJSON}

_33

>

_33

{children}

_33

</FlowProvider>

_33

);

_33

}`

Then wrap your app in the root layout:

`_15

import { FlowProviderWrapper } from '@/components/flow-provider-wrapper';

_15

import { Stack } from 'expo-router';

_15

import { StatusBar } from 'expo-status-bar';

_15

import { View } from 'react-native';

_15

_15

export default function RootLayout() {

_15

return (

_15

<FlowProviderWrapper>

_15

<View style={{ flex: 1, backgroundColor: '#fff' }}>

_15

<Stack screenOptions={{ headerShown: false }} />

_15

</View>

_15

<StatusBar style="dark" />

_15

</FlowProviderWrapper>

_15

);

_15

}`

### 3. Start Building[​](#3-start-building "Direct link to 3. Start Building")

`` _50

import { View, Text, Pressable } from 'react-native';

_50

import {

_50

Connect,

_50

useFlowCurrentUser,

_50

useFlowQuery,

_50

} from '@onflow/react-native-sdk';

_50

_50

function MyApp() {

_50

const { user } = useFlowCurrentUser();

_50

_50

const {

_50

data: balance,

_50

isLoading,

_50

refetch,

_50

} = useFlowQuery({

_50

cadence: `

_50

import FlowToken from 0x7e60df042a9c0868

_50

_50

access(all) fun main(address: Address): UFix64 {

_50

let account = getAccount(address)

_50

let vaultRef = account.capabilities

_50

.get<&FlowToken.Vault>(/public/flowTokenBalance)

_50

.borrow()

_50

?? panic("Could not borrow Balance reference")

_50

return vaultRef.balance

_50

}

_50

`,

_50

args: (arg, t) => [arg(user?.addr, t.Address)],

_50

query: { enabled: !!user?.addr },

_50

});

_50

_50

return (

_50

<View>

_50

<Connect />

_50

{user?.loggedIn && (

_50

<View>

_50

<Text>Welcome, {user.addr}!</Text>

_50

{isLoading ? (

_50

<Text>Loading balance...</Text>

_50

) : (

_50

<Text>Balance: {balance ? String(balance) : '0.00'} FLOW</Text>

_50

)}

_50

<Pressable onPress={() => refetch()}>

_50

<Text>Refresh</Text>

_50

</Pressable>

_50

</View>

_50

)}

_50

</View>

_50

);

_50

} ``

Starter Template

Get started quickly with the [flow-react-native-sdk-starter](https://github.com/onflow/flow-react-native-sdk-starter) template which includes a pre-configured Expo project with wallet connection, balance queries, and transaction examples.

---

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

The `FlowProvider` accepts the following configuration:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Property Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `accessNodeUrl` REST endpoint for blockchain access (e.g., `https://rest-testnet.onflow.org`)| `discoveryWallet` URL for wallet discovery/selection UI|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `discoveryAuthnEndpoint` API endpoint for authentication|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `flowNetwork` Network selection: `"testnet"` or `"mainnet"`| `appDetailTitle` App name displayed in wallet|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `appDetailUrl` App URL displayed in wallet|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `appDetailIcon` App icon URL displayed in wallet|  |  |  |  | | --- | --- | --- | --- | | `appDetailDescription` App description displayed in wallet|  |  | | --- | --- | | `walletconnectProjectId` WalletConnect Cloud project ID | | | | | | | | | | | | | | | | | | | |

**Mainnet Configuration:**

`_10

config={{

_10

accessNodeUrl: "https://rest-mainnet.onflow.org",

_10

discoveryWallet: "https://fcl-discovery.onflow.org/authn",

_10

discoveryAuthnEndpoint: "https://fcl-discovery.onflow.org/api/authn",

_10

flowNetwork: "mainnet",

_10

// ... other options

_10

}}`

---

## [Hooks](/build/tools/react-native-sdk/hooks)[​](#hooks "Direct link to hooks")

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

[→ View all hooks](/build/tools/react-native-sdk/hooks)

---

## [Components](/build/tools/react-native-sdk/components)[​](#components "Direct link to components")

Native UI components for React Native:

* `<Connect />` – Wallet authentication with balance display
* `<Profile />` – Standalone wallet information display

[→ View all components](/build/tools/react-native-sdk/components)

---

## Why Choose React Native SDK?[​](#why-choose-react-native-sdk "Direct link to Why Choose React Native SDK?")

**Developer Experience First**

* TypeScript-native with full type safety
* Familiar React Native patterns and conventions
* Comprehensive error handling and loading states

**Production Ready**

* Built on battle-tested libraries (TanStack Query)
* Automatic retries, caching, and background updates
* Cross-VM support for hybrid Cadence/EVM applications

**Mobile Native**

* Native mobile wallet integrations via WalletConnect
* React Native components that feel native
* Expo and bare React Native support

---

## Need Help?[​](#need-help "Direct link to Need Help?")

* **[Hooks Documentation](/build/tools/react-native-sdk/hooks)** – Detailed API reference for all hooks
* **[Components Documentation](/build/tools/react-native-sdk/components)** – UI components guide
* **[Configuration Guide](/build/tools/flow-cli/flow.json/configuration)** – Learn about configuring `flow.json`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-native-sdk/index.mdx)

Last updated on **Dec 17, 2025** by **Michael Fabozzi**

[Previous

Tools](/build/tools)[Next

Hooks](/build/tools/react-native-sdk/hooks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Quick Start](#quick-start)
  + [1. Install](#1-install)+ [2. Wrap Your App](#2-wrap-your-app)+ [3. Start Building](#3-start-building)* [Configuration Options](#configuration-options)* [Hooks](#hooks)* [Components](#components)* [Why Choose React Native SDK?](#why-choose-react-native-sdk)* [Need Help?](#need-help)

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