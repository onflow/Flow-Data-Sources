# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter

FCL Rainbowkit Adapter | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

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

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                        * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              + [FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)+ [FCL Rainbowkit Adapter](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)+ [FCL Wagmi Adapter](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)* [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)* FCL Rainbowkit Adapter

On this page

info

This package is currently in alpha and is subject to change.

# FCL RainbowKit Adapter

Offers a **RainbowKit**-compatible wallet definition that uses Flow’s COA via FCL. Once installed, RainbowKit can display a “Flow Wallet” (or other FCL-enabled wallets) in its wallet selection modal.

## Installation[​](#installation "Direct link to Installation")

`_10

npm install @onflow/fcl-rainbowkit-adapter`

## Usage[​](#usage "Direct link to Usage")

Below is a typical usage example that shows how to set up a **RainbowKit** config for the Flow testnet, using this adapter. (From your provided sample.)

`_50

import * as fcl from '@onflow/fcl'

_50

import { createFclConnector, flowWallet, useIsCadenceWalletConnected } from '@onflow/fcl-rainbowkit-adapter'

_50

import { connectorsForWallets } from '@rainbow-me/rainbowkit'

_50

import { flowTestnet } from 'wagmi/chains'

_50

import { createConfig, http } from 'wagmi'

_50

_50

// Configure FCL (Flow testnet in this example)

_50

fcl.config({

_50

"accessNode.api": "https://rest-testnet.onflow.org",

_50

"discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn",

_50

"walletconnect.projectId": "9b70cfa398b2355a5eb9b1cf99f4a981", // example WC projectId

_50

})

_50

_50

// Create a list of connectors from your wallets

_50

const connectors = connectorsForWallets([

_50

{

_50

groupName: "Recommended",

_50

wallets: [

_50

flowWallet(),

_50

],

_50

},

_50

], {

_50

appName: 'RainbowKit demo',

_50

projectId: '9b70cfa398b2355a5eb9b1cf99f4a981',

_50

})

_50

_50

// Wagmi config

_50

export const config = createConfig({

_50

chains: [flowTestnet],

_50

connectors,

_50

ssr: true,

_50

transports: {

_50

[flowTestnet.id]: http(),

_50

}

_50

});

_50

_50

// In your React component

_50

function MyApp() {

_50

const isCadenceConnected = useIsCadenceWalletConnected(config)

_50

_50

return (

_50

<div>

_50

{isCadenceConnected ? (

_50

<p>Cadence wallet is connected!</p>

_50

) : (

_50

<p>Please connect your Cadence wallet</p>

_50

)}

_50

</div>

_50

)

_50

}`

## API[​](#api "Direct link to API")

### `flowWallet(options?: FlowWalletOptions): RainbowKitWallet`[​](#flowwalletoptions-flowwalletoptions-rainbowkitwallet "Direct link to flowwalletoptions-flowwalletoptions-rainbowkitwallet")

* Returns a RainbowKit-compatible wallet definition that integrates **@onflow/fcl-ethereum-provider**.
* **Parameters**
  + `options?: FlowWalletOptions` – optional configuration, such as names/icons or custom gateway endpoints.
* **Returns**: A `RainbowKitWallet` object to be included in `connectorsForWallets`.

### `createFclConnector(config?: CreateFclConnectorOptions): Connector`[​](#createfclconnectorconfig-createfclconnectoroptions-connector "Direct link to createfclconnectorconfig-createfclconnectoroptions-connector")

* A lower-level helper to build your own FCL-based EIP-1193 connectors for RainbowKit if you don't want the preconfigured `flowWallet`.
* **Parameters**
  + `config?: CreateFclConnectorOptions` – typical Wagmi + FCL config object (i.e., chain ID, network URL, FCL services, etc.).
* **Returns**: A valid Wagmi `Connector` for EVM interactions via FCL.

### `useIsCadenceWalletConnected(config: Config): boolean`[​](#useiscadencewalletconnectedconfig-config-boolean "Direct link to useiscadencewalletconnectedconfig-config-boolean")

A React hook that monitors the connection status of both FCL (Cadence) and Wagmi accounts to determine whether a Cadence-aware wallet is connected.

* **Parameters**
  + `config: Config` – The Wagmi configuration object
* **Returns**: `boolean` – `true` when both Cadence-aware wallet is connected, `false` if no wallet, or an EVM-only wallet is connected.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter.mdx)

Last updated on **Sep 4, 2025** by **Jordan Ribbink**

[Previous

FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)[Next

FCL Wagmi Adapter](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)* [Usage](#usage)* [API](#api)
      + [`flowWallet(options?: FlowWalletOptions): RainbowKitWallet`](#flowwalletoptions-flowwalletoptions-rainbowkitwallet)+ [`createFclConnector(config?: CreateFclConnectorOptions): Connector`](#createfclconnectorconfig-createfclconnectoroptions-connector)+ [`useIsCadenceWalletConnected(config: Config): boolean`](#useiscadencewalletconnectedconfig-config-boolean)

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