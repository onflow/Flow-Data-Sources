# Source: https://developers.flow.com/tools/clients/fcl-js/cross-vm/rainbowkit-adapter

FCL Rainbowkit Adapter | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)

    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Cross VM Packages](/tools/clients/fcl-js/cross-vm)

      * [FCL Ethereum Provider](/tools/clients/fcl-js/cross-vm/ethereum-provider)
      * [FCL Rainbowkit Adapter](/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)
      * [FCL Wagmi Adapter](/tools/clients/fcl-js/cross-vm/wagmi-adapter)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Clients](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* [Cross VM Packages](/tools/clients/fcl-js/cross-vm)
* FCL Rainbowkit Adapter

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

`_35

import * as fcl from '@onflow/fcl'

_35

import { createFclConnector, flowWallet } from '@onflow/fcl-rainbowkit-adapter'

_35

import { connectorsForWallets } from '@rainbow-me/rainbowkit'

_35

import { flowTestnet } from 'wagmi/chains'

_35

import { createConfig, http } from 'wagmi'

_35

_35

// Configure FCL (Flow testnet in this example)

_35

fcl.config({

_35

"accessNode.api": "https://rest-testnet.onflow.org",

_35

"discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn",

_35

"walletconnect.projectId": "9b70cfa398b2355a5eb9b1cf99f4a981", // example WC projectId

_35

})

_35

_35

// Create a list of connectors from your wallets

_35

const connectors = connectorsForWallets([

_35

{

_35

groupName: "Recommended",

_35

wallets: [

_35

flowWallet(),

_35

],

_35

},

_35

], {

_35

appName: 'RainbowKit demo',

_35

projectId: '9b70cfa398b2355a5eb9b1cf99f4a981',

_35

})

_35

_35

// Wagmi config

_35

export const config = createConfig({

_35

chains: [flowTestnet],

_35

connectors,

_35

ssr: true,

_35

transports: {

_35

[flowTestnet.id]: http(),

_35

}

_35

});`

## API[​](#api "Direct link to API")

### `flowWallet(options?: FlowWalletOptions): RainbowKitWallet`[​](#flowwalletoptions-flowwalletoptions-rainbowkitwallet "Direct link to flowwalletoptions-flowwalletoptions-rainbowkitwallet")

* Returns a RainbowKit-compatible wallet definition that integrates **@onflow/fcl-ethereum-provider**.
* **Parameters**
  + `options?: FlowWalletOptions` – optional configuration, such as names/icons or custom gateway endpoints.
* **Returns**: A `RainbowKitWallet` object to be included in `connectorsForWallets`.

### `createFclConnector(config?: CreateFclConnectorOptions): Connector`[​](#createfclconnectorconfig-createfclconnectoroptions-connector "Direct link to createfclconnectorconfig-createfclconnectoroptions-connector")

* A lower-level helper to build your own FCL-based EIP-1193 connectors for RainbowKit if you don’t want the preconfigured `flowWallet`.
* **Parameters**
  + `config?: CreateFclConnectorOptions` – typical Wagmi + FCL config object (i.e., chain ID, network URL, FCL services, etc.).
* **Returns**: A valid Wagmi `Connector` for EVM interactions via FCL.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/cross-vm/rainbowkit-adapter.mdx)

Last updated on **Mar 13, 2025** by **j pimmel**

[Previous

FCL Ethereum Provider](/tools/clients/fcl-js/cross-vm/ethereum-provider)[Next

FCL Wagmi Adapter](/tools/clients/fcl-js/cross-vm/wagmi-adapter)

###### Rate this page

😞😐😊

* [Installation](#installation)
* [Usage](#usage)
* [API](#api)
  + [`flowWallet(options?: FlowWalletOptions): RainbowKitWallet`](#flowwalletoptions-flowwalletoptions-rainbowkitwallet)
  + [`createFclConnector(config?: CreateFclConnectorOptions): Connector`](#createfclconnectorconfig-createfclconnectoroptions-connector)

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
* [Flowscan Mainnet](https://flowdscan.io/)
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