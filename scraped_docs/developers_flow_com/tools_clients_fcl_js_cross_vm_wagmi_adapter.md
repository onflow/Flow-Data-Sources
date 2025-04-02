# Source: https://developers.flow.com/tools/clients/fcl-js/cross-vm/wagmi-adapter

FCL Wagmi Adapter | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)

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
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Use Cursor AI](/tools/cursor)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* [Cross VM Packages](/tools/clients/fcl-js/cross-vm)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/cross-vm/wagmi-adapter.mdx)

Last updated on **Mar 27, 2025** by **Brian Doyle**

[Previous

FCL Rainbowkit Adapter](/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)[Next

Wallet Discovery](/tools/clients/fcl-js/discovery)

###### Rate this page

😞😐😊

* [Installation](#installation)
* [Usage](#usage)
* [API](#api)
  + [`fclWagmiConnector(options?: FclWagmiConnectorOptions): Connector`](#fclwagmiconnectoroptions-fclwagmiconnectoroptions-connector)

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