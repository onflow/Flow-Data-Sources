# Source: https://developers.flow.com/tools/clients/fcl-js/cross-vm

Cross VM Packages | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
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
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
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
* **Link to Docs**: [Read the @onflow/fcl-ethereum-provider Reference »](/tools/clients/fcl-js/cross-vm/ethereum-provider)

## `@onflow/fcl-wagmi-adapter`[​](#onflowfcl-wagmi-adapter "Direct link to onflowfcl-wagmi-adapter")

* **Description**: A Wagmi connector that uses `@onflow/fcl-ethereum-provider` under the hood so you can sign in with your COA through standard Wagmi flows.
* **Use Cases**:
  + Add Flow-based COAs to an existing Wagmi-powered dApp as if they were Ethereum wallets.
* **Link to Docs**: [Read the @onflow/fcl-wagmi-adapter Reference »](/tools/clients/fcl-js/cross-vm/wagmi-adapter)

## `@onflow/fcl-rainbowkit-adapter`[​](#onflowfcl-rainbowkit-adapter "Direct link to onflowfcl-rainbowkit-adapter")

* **Description**: A RainbowKit adapter that surfaces a Flow-based wallet in the wallet selection modal, making it easy to sign transactions via COAs in a RainbowKit environment.
* **Use Cases**:
  + Offer Flow-based wallets (e.g., Flow Wallet) alongside popular Ethereum wallets in RainbowKit.
* **Link to Docs**: [Read the @onflow/fcl-rainbowkit-adapter Reference »](/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/cross-vm/index.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

How to Configure FCL](/tools/clients/fcl-js/configure-fcl)[Next

FCL Ethereum Provider](/tools/clients/fcl-js/cross-vm/ethereum-provider)

###### Rate this page

😞😐😊

* [`@onflow/fcl-ethereum-provider`](#onflowfcl-ethereum-provider)
* [`@onflow/fcl-wagmi-adapter`](#onflowfcl-wagmi-adapter)
* [`@onflow/fcl-rainbowkit-adapter`](#onflowfcl-rainbowkit-adapter)

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
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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