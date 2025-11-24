# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm/ethereum-provider

FCL Ethereum Provider | Flow Developer Portal



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

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)* FCL Ethereum Provider

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

* [Installation](#installation)* [Usage](#usage)* [API](#api)
      + [`createEthereumProvider(config?: CreateEthereumProviderConfig): Eip1193Provider`](#createethereumproviderconfig-createethereumproviderconfig-eip1193provider)* [Supported JSON-RPC Methods](#supported-json-rpc-methods)
        + [Fallback Behavior](#fallback-behavior)* [Provider Events](#provider-events)

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