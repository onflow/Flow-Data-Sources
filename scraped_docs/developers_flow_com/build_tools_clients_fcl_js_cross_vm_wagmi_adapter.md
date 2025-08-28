# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm/wagmi-adapter

FCL Wagmi Adapter | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/about)

  + [Why EVM on Flow](/build/evm/about)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [EVM Quickstart](/build/evm/quickstart)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)

    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)
      * [Authentication](/build/tools/clients/fcl-js/authentication)
      * [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)
      * [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

        + [FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)
        + [FCL Rainbowkit Adapter](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)
        + [FCL Wagmi Adapter](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)
      * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)
      * [Installation](/build/tools/clients/fcl-js/installation)
      * [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)
      * [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)
      * [Scripts](/build/tools/clients/fcl-js/scripts)
      * [Transactions](/build/tools/clients/fcl-js/transactions)
      * [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)
      * [WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)
    - [Flow Go SDK](/build/tools/clients/flow-go-sdk)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Client Tools](/build/tools/clients)
* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)
* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)
* FCL Wagmi Adapter

On this page

info

This package is currently in alpha and is subject to change.

# FCL Wagmi Adapter

Provides a **Wagmi** connector that uses **@onflow/fcl-ethereum-provider** under the hood, allowing you to integrate Flow-based Cadence-Owned Accounts (COAs) seamlessly into Wagmi applications.

## Installation[​](#installation "Direct link to Installation")

`_10

npm install @onflow/fcl-wagmi-adapter`

## Usage[​](#usage "Direct link to Usage")

**Basic Example**:

`_31

import { createClient, configureChains } from 'wagmi'

_31

import { fclWagmiConnector } from '@onflow/fcl-wagmi-adapter'

_31

import { flowTestnet } from 'wagmi/chains'

_31

import { publicProvider } from 'wagmi/providers/public'

_31

import * as fcl from '@onflow/fcl'

_31

_31

// Configure FCL for Flow

_31

fcl.config({

_31

"accessNode.api": "https://rest-testnet.onflow.org",

_31

"discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn",

_31

})

_31

_31

// Set up Wagmi for Flow Testnet

_31

const { chains, provider } = configureChains(

_31

[flowTestnet],

_31

[publicProvider()]

_31

)

_31

_31

// Create a connector that uses FCL under the hood

_31

const fclConnector = fclWagmiConnector({

_31

// optional: you can pass any config your provider or FCL needs

_31

})

_31

_31

// Create the Wagmi client

_31

const wagmiClient = createClient({

_31

autoConnect: true,

_31

connectors: [fclConnector],

_31

provider,

_31

})

_31

_31

// The rest of your dApp logic...`

## API[​](#api "Direct link to API")

### `fclWagmiConnector(options?: FclWagmiConnectorOptions): Connector`[​](#fclwagmiconnectoroptions-fclwagmiconnectoroptions-connector "Direct link to fclwagmiconnectoroptions-fclwagmiconnectoroptions-connector")

* **Parameters**
  + `options?: object` – any additional configuration for the underlying FCL provider (gateway URL, custom FCL service, etc.)
* **Returns**: A Wagmi `Connector` object that can be used in `createClient` or `getDefaultConfig`.

**Notes**:

* This connector essentially wraps `@onflow/fcl-ethereum-provider` as an EIP-1193 provider to talk to Flow EVM via Wagmi.
* The user’s authenticated COA is exposed as the “account” in Wagmi context.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/cross-vm/wagmi-adapter.mdx)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

FCL Rainbowkit Adapter](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)[Next

Wallet Discovery](/build/tools/clients/fcl-js/discovery)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)
* [Usage](#usage)
* [API](#api)
  + [`fclWagmiConnector(options?: FclWagmiConnectorOptions): Connector`](#fclwagmiconnectoroptions-fclwagmiconnectoroptions-connector)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
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
* [EVM](/build/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.