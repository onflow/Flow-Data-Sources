# Source: https://developers.flow.com/build/tools/clients/fcl-js/cross-vm

Cross VM Packages | Flow Developer Portal



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

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                        * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              + [FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)+ [FCL Rainbowkit Adapter](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)+ [FCL Wagmi Adapter](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)* [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* Cross VM Packages

On this page

# FCL Cross-VM Packages

These packages allow you to leverage Flow’s Cadence-Owned Account (COA) within Ethereum tooling (for example, Wagmi, RainbowKit). They provide a unified approach for cross-VM apps on Flow and EVM, which lets you perform EVM-like operations will Cadence accounts.

For background and motivation, see the [FCL Ethereum Provider for Cross-VM Apps FLIP #316](https://github.com/onflow/flips/blob/c0fe9b71a9afb85fe70a69cf7c0870b5d327e679/application/20241223-fcl-ethereum-provider.md).

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Package Purpose|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [@onflow/fcl-ethereum-provider](#onflowfcl-ethereum-provider) Provides an EIP-1193-compliant Ethereum provider backed by an FCL-authenticated COA.|  |  |  |  | | --- | --- | --- | --- | | [@onflow/fcl-wagmi-adapter](#onflowfcl-wagmi-adapter) Integrates Flow-based COAs with Wagmi, and exposes them as Ethereum accounts in your dApp.|  |  | | --- | --- | | [@onflow/fcl-rainbowkit-adapter](#onflowfcl-rainbowkit-adapter) Allows a Flow-based wallet option in your RainbowKit wallet selection modal. | | | | | | | |

## `@onflow/fcl-ethereum-provider`[​](#onflowfcl-ethereum-provider "Direct link to onflowfcl-ethereum-provider")

* **Description**: A drop-in EIP-1193 provider that authenticates users via [Flow Client Library (FCL)](https://developers.flow.com/) and lets them sign transactions and messages with their COA.
* **Use Cases**:
  + Integrate Flow EVM with any generic EVM library or framework.
  + Direct control over JSON-RPC calls (for example, `provider.request({ method: 'eth_sendTransaction' })`).
* **Link to Docs**: [Read the @onflow/fcl-ethereum-provider Reference »](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)

## `@onflow/fcl-wagmi-adapter`[​](#onflowfcl-wagmi-adapter "Direct link to onflowfcl-wagmi-adapter")

* **Description**: A Wagmi connector that uses `@onflow/fcl-ethereum-provider` under the hood so you can sign in with your COA through standard Wagmi flows.
* **Use Cases**:
  + Add Flow-based COAs to a current Wagmi-powered dApp as if they were Ethereum wallets.
* **Link to Docs**: [Read the @onflow/fcl-wagmi-adapter Reference »](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)

## `@onflow/fcl-rainbowkit-adapter`[​](#onflowfcl-rainbowkit-adapter "Direct link to onflowfcl-rainbowkit-adapter")

* **Description**: A RainbowKit adapter that surfaces a Flow-based wallet in the wallet selection modal, wheich makes it easy to sign transactions via COAs in a RainbowKit environment.
* **Use Cases**:
  + Offer Flow-based wallets (such as Flow Wallet) alongside popular Ethereum wallets in RainbowKit.
* **Link to Docs**: [Read the @onflow/fcl-rainbowkit-adapter Reference »](/build/tools/clients/fcl-js/cross-vm/rainbowkit-adapter)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/cross-vm/index.md)

Last updated on **Dec 10, 2025** by **cshannon1218**

[Previous

How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)[Next

FCL Ethereum Provider](/build/tools/clients/fcl-js/cross-vm/ethereum-provider)

###### Rate this page

😞😐😊

Copy as Markdown

* [`@onflow/fcl-ethereum-provider`](#onflowfcl-ethereum-provider)* [`@onflow/fcl-wagmi-adapter`](#onflowfcl-wagmi-adapter)* [`@onflow/fcl-rainbowkit-adapter`](#onflowfcl-rainbowkit-adapter)

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