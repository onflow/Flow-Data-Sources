# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm/ethereum-provider

FCL Ethereum Provider | Flow Developer Portal



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
* FCL Ethereum Provider

On this page

info

This package is currently in alpha and is subject to change.

# FCL Ethereum Provider

Exposes a client-side [EIP-1193](https://eips.ethereum.org/EIPS/eip-1193) compatible Ethereum provider that uses an FCL-authenticated Cadence Owned Account (COA) under the hood.
If a wallet does not natively provide EVM capabilities, this provider emulates Ethereum JSON-RPC by delegating to FCL for signing and COA interactions.

## Installation[​](#installation "Direct link to Installation")

`_10

npm install @onflow/fcl-ethereum-provider`

## Usage[​](#usage "Direct link to Usage")

`_40

import * as fcl from "@onflow/fcl"

_40

import { createEthereumProvider } from "@onflow/fcl-ethereum-provider"

_40

_40

// Configure FCL (pointing to whichever Flow network you require)

_40

fcl.config({

_40

"accessNode.api": "https://rest-testnet.onflow.org",

_40

"discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn",

_40

})

_40

_40

// Create the EIP-1193 provider

_40

const provider = createEthereumProvider({

_40

// Optional configuration:

_40

// service?: Service // Custom FCL service config

_40

// gateway?: Eip1193Provider | string // EVM Gateway provider or URL

_40

})

_40

_40

// Example: request EVM-style accounts (COA addresses)

_40

const accounts = await provider.request({ method: "eth_requestAccounts" })

_40

console.log("EVM Accounts:", accounts)

_40

_40

// Use the same session to sign a message

_40

const signature = await provider.request({

_40

method: "personal_sign",

_40

params: ["0x68656c6c6f20776f726c64", accounts[0]], // hex-encoded "hello world"

_40

})

_40

console.log("Signature:", signature)

_40

_40

// Or send transactions

_40

const txHash = await provider.request({

_40

method: "eth_sendTransaction",

_40

params: [

_40

{

_40

from: accounts[0],

_40

to: "0x1234...",

_40

data: "0xabcd1234...",

_40

value: "0x0",

_40

},

_40

],

_40

})

_40

console.log("Transaction Hash:", txHash)`

## API[​](#api "Direct link to API")

### `createEthereumProvider(config?: CreateEthereumProviderConfig): Eip1193Provider`[​](#createethereumproviderconfig-createethereumproviderconfig-eip1193provider "Direct link to createethereumproviderconfig-createethereumproviderconfig-eip1193provider")

* **Parameters**

  + `config.service?: Service`  
    An [FCL “Service” object][fcl-service-docs] for custom FCL authentication flows. If omitted, the default FCL discovery service is used.
  + `config.gateway?: Eip1193Provider | string`  
    An EIP-1193 provider (or a string URL) pointing to a Flow EVM gateway. Defaults to the public Flow EVM gateway if omitted.
* **Returns**: An [EIP-1193](https://eips.ethereum.org/EIPS/eip-1193) provider instance you can pass into EVM tooling or interact with directly in your app.

## Supported JSON-RPC Methods[​](#supported-json-rpc-methods "Direct link to Supported JSON-RPC Methods")

Below are the main request methods handled within the FCL Ethereum provider:

1. **`eth_requestAccounts` / `eth_accounts`**

   * **Behavior**:
     + Invokes the FCL authentication flow (if not already authenticated)
     + Returns the Cadence-Owned Account (COA) address
     + Stores the COA at `/storage/evm` (creates if missing)
2. **`eth_sendTransaction`**

   * **Behavior**:
     + Wraps the transaction in a Cadence transaction that invokes `coa.call(...)` in the Flow EVM
     + Uses the user’s authenticated COA for signing
     + Returns the resulting EVM transaction hash
3. **`personal_sign`**

   * **Behavior**:
     + Requests a user signature via FCL’s `signUserMessage` or equivalent mechanism
     + Returns an RLP-encoded [COA ownership proof](https://github.com/onflow/flow-go/blob/master/fvm/evm/types/proof.go#L139) in place of a raw secp256k1 signature
4. **`eth_chainId`**

   * **Behavior**:
     + Returns the numeric Flow EVM chain ID (e.g., `0x747` for Flow EVM Mainnet)
5. **`wallet_switchEthereumChain`**

   * **Behavior**:
     + Allows dApps to request switching to a different Flow EVM chain (e.g. testnet to mainnet).
     + Under the hood, this can trigger reconfiguration of FCL for a different Flow access node and Flow EVM gateway if recognized.
     + If the requested chain ID is not recognized, the call will throw an error (matching EIP-1193 standard error codes).
6. **`wallet_addEthereumChain`**

   * **Behavior**:
     + Allows a dApp to request adding a Flow EVM chain config.
     + If the chain is recognized by the provider or is one the provider can handle, it will register it. Otherwise, it may reject with an EIP-1193 error.
     + Since Flow EVM is typically a single chain per environment, usage is limited. However, in principle, custom EVM networks or local dev can be added if your provider/gateway supports them.

### Fallback Behavior[​](#fallback-behavior "Direct link to Fallback Behavior")

Any unknown or unsupported request methods will be proxied to the `gateway` (if you provided a standard JSON-RPC URL or EIP-1193 provider). If the gateway does not handle them, an error will be returned.

## Provider Events[​](#provider-events "Direct link to Provider Events")

* **`connect`**: Emitted once the user successfully authenticates via FCL, indicating that the provider is ready.
* **`disconnect`**: Emitted if the FCL session ends or user explicitly logs out, severing the session.
* **`accountsChanged`**: Emitted when the current user changes (e.g. re-authentication, or switching user in the wallet).
* **`chainChanged`**: Emitted when the user switches to a different Flow EVM chain (e.g. testnet to mainnet).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/cross-vm/ethereum-provider.mdx)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)[Next

FCL Rainbowkit Adapter](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)
* [Usage](#usage)
* [API](#api)
  + [`createEthereumProvider(config?: CreateEthereumProviderConfig): Eip1193Provider`](#createethereumproviderconfig-createethereumproviderconfig-eip1193provider)
* [Supported JSON-RPC Methods](#supported-json-rpc-methods)
  + [Fallback Behavior](#fallback-behavior)
* [Provider Events](#provider-events)

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