# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm/wagmi-adapter

FCL Wagmi Adapter | Flow Developer Portal



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

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                          * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                                + [FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)+ [FCL Rainbowkit Adapter](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)+ [FCL Wagmi Adapter](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)* [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)* FCL Wagmi Adapter

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

* [Installation](#installation)* [Usage](#usage)* [API](#api)
      + [`fclWagmiConnector(options?: FclWagmiConnectorOptions): Connector`](#fclwagmiconnectoroptions-fclwagmiconnectoroptions-connector)

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