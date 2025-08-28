# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm

Cross VM Packages | Flow Developer Portal



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
* Cross VM Packages

On this page

# FCL Cross-VM Packages

These packages enable you to leverage Flow’s Cadence-Owned Account (COA) within Ethereum tooling (e.g., Wagmi, RainbowKit). They provide a unified approach for cross-VM apps on Flow and EVM, letting you perform EVM-like operations using Cadence accounts.

For background and motivation, see the [FCL Ethereum Provider for Cross-VM Apps FLIP #316](https://github.com/onflow/flips/blob/c0fe9b71a9afb85fe70a69cf7c0870b5d327e679/application/20241223-fcl-ethereum-provider.md).

| Package | Purpose |
| --- | --- |
| [@onflow/fcl-ethereum-provider](#onflowfcl-ethereum-provider) | Provides an EIP-1193-compliant Ethereum provider backed by an FCL-authenticated COA. |
| [@onflow/fcl-wagmi-adapter](#onflowfcl-wagmi-adapter) | Integrates Flow-based COAs with Wagmi, exposing them as Ethereum accounts in your dApp. |
| [@onflow/fcl-rainbowkit-adapter](#onflowfcl-rainbowkit-adapter) | Enables a Flow-based wallet option in your RainbowKit wallet selection modal. |

## `@onflow/fcl-ethereum-provider`[​](#onflowfcl-ethereum-provider "Direct link to onflowfcl-ethereum-provider")

* **Description**: A drop-in EIP-1193 provider that authenticates users via [FCL](https://developers.flow.com/) and lets them sign transactions/messages with their COA.
* **Use Cases**:
  + Integrate Flow EVM with any generic EVM library or framework.
  + Direct control over JSON-RPC calls (e.g., `provider.request({ method: 'eth_sendTransaction' })`).
* **Link to Docs**: [Read the @onflow/fcl-ethereum-provider Reference »](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)

## `@onflow/fcl-wagmi-adapter`[​](#onflowfcl-wagmi-adapter "Direct link to onflowfcl-wagmi-adapter")

* **Description**: A Wagmi connector that uses `@onflow/fcl-ethereum-provider` under the hood so you can sign in with your COA through standard Wagmi flows.
* **Use Cases**:
  + Add Flow-based COAs to an existing Wagmi-powered dApp as if they were Ethereum wallets.
* **Link to Docs**: [Read the @onflow/fcl-wagmi-adapter Reference »](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)

## `@onflow/fcl-rainbowkit-adapter`[​](#onflowfcl-rainbowkit-adapter "Direct link to onflowfcl-rainbowkit-adapter")

* **Description**: A RainbowKit adapter that surfaces a Flow-based wallet in the wallet selection modal, making it easy to sign transactions via COAs in a RainbowKit environment.
* **Use Cases**:
  + Offer Flow-based wallets (e.g., Flow Wallet) alongside popular Ethereum wallets in RainbowKit.
* **Link to Docs**: [Read the @onflow/fcl-rainbowkit-adapter Reference »](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/cross-vm/index.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)[Next

FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)

###### Rate this page

😞😐😊

Copy as Markdown

* [`@onflow/fcl-ethereum-provider`](#onflowfcl-ethereum-provider)
* [`@onflow/fcl-wagmi-adapter`](#onflowfcl-wagmi-adapter)
* [`@onflow/fcl-rainbowkit-adapter`](#onflowfcl-rainbowkit-adapter)

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