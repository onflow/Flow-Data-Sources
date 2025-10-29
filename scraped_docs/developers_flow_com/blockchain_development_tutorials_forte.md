# Source: https://developers.flow.com/blockchain-development-tutorials/forte

Forte Network Upgrade | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      + [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)

        + [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)

          + [DeFi Math Utils](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * Forte Network Upgrade

On this page

# Forte Network Upgrade Tutorials

This series covers the new features and capabilities introduced in the Forte network upgrade for Flow blockchain. The Forte upgrade brings powerful new tools for building sophisticated decentralized finance (DeFi) applications, including automated DeFi workflows and time-based smart contract execution.

## What's New in Forte[​](#whats-new-in-forte "Direct link to What's New in Forte")

The Forte network upgrade introduces several features that expand Flow's capabilities:

* **Flow Actions**: Standardized interfaces for building composable DeFi workflows.
* **Scheduled Transactions**: Time-based smart contract execution and blockchain automation.
* **Enhanced Composability**: New patterns for building complex, interconnected applications.

## Deployed Contract Addresses[​](#deployed-contract-addresses "Direct link to Deployed Contract Addresses")

info

Forte is **live** on testnet and Mainnet.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Testnet [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager) Mainnet [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | DeFiActions [0x4c2ff9dd03ab442f](https://testnet.flowscan.io/contract/A.4c2ff9dd03ab442f.DeFiActions?tab=deployments) [0x92195d814edf9cb0](https://flowscan.io/contract/A.92195d814edf9cb0.DeFiActions?tab=deployments) | DeFiActionsMathUtils [0x4c2ff9dd03ab442f](https://testnet.flowscan.io/contract/A.4c2ff9dd03ab442f.DeFiActionsMathUtils?tab=deployments) [0x92195d814edf9cb0](https://flowscan.io/contract/A.92195d814edf9cb0.DeFiActionsMathUtils?tab=deployments) | DeFiActionsUtils [0x4c2ff9dd03ab442f](https://testnet.flowscan.io/contract/A.4c2ff9dd03ab442f.DeFiActionsUtils?tab=deployments) [0x92195d814edf9cb0](https://flowscan.io/contract/A.92195d814edf9cb0.DeFiActionsUtils?tab=deployments) | FungibleTokenConnectors [0x5a7b9cee9aaf4e4e](https://testnet.flowscan.io/contract/A.5a7b9cee9aaf4e4e.FungibleTokenConnectors?tab=deployments) [0x1d9a619393e9fb53](https://flowscan.io/contract/A.1d9a619393e9fb53.FungibleTokenConnectors?tab=deployments) | EVMNativeFLOWConnectors [0xb88ba0e976146cd1](https://testnet.flowscan.io/contract/A.b88ba0e976146cd1.EVMNativeFLOWConnectors?tab=deployments) [0xcc15a0c9c656b648](https://flowscan.io/contract/A.cc15a0c9c656b648.EVMNativeFLOWConnectors?tab=deployments) | EVMTokenConnectors [0xb88ba0e976146cd1](https://testnet.flowscan.io/contract/A.b88ba0e976146cd1.EVMTokenConnectors?tab=deployments) [0xcc15a0c9c656b648](https://flowscan.io/contract/A.cc15a0c9c656b648.EVMTokenConnectors?tab=deployments) | SwapConnectors [0xaddd594cf410166a](https://testnet.flowscan.io/contract/A.addd594cf410166a.SwapConnectors?tab=deployments) [0x0bce04a00aedf132](https://flowscan.io/contract/A.0bce04a00aedf132.SwapConnectors?tab=deployments) | IncrementFiSwapConnectors [0x49bae091e5ea16b5](https://testnet.flowscan.io/contract/A.49bae091e5ea16b5.IncrementFiSwapConnectors?tab=deployments) [0xefa9bd7d1b17f1ed](https://flowscan.io/contract/A.efa9bd7d1b17f1ed.IncrementFiSwapConnectors?tab=deployments) | IncrementFiFlashloanConnectors [0x49bae091e5ea16b5](https://testnet.flowscan.io/contract/A.49bae091e5ea16b5.IncrementFiFlashloanConnectors?tab=deployments) [0xefa9bd7d1b17f1ed](https://flowscan.io/contract/A.efa9bd7d1b17f1ed.IncrementFiFlashloanConnectors?tab=deployments) | IncrementFiPoolLiquidityConnectors [0x49bae091e5ea16b5](https://testnet.flowscan.io/contract/A.49bae091e5ea16b5.IncrementFiPoolLiquidityConnectors?tab=deployments) [0xefa9bd7d1b17f1ed](https://flowscan.io/contract/A.efa9bd7d1b17f1ed.IncrementFiPoolLiquidityConnectors?tab=deployments) | IncrementFiStakingConnectors [0x49bae091e5ea16b5](https://testnet.flowscan.io/contract/A.49bae091e5ea16b5.IncrementFiStakingConnectors?tab=deployments) [0xefa9bd7d1b17f1ed](https://flowscan.io/contract/A.efa9bd7d1b17f1ed.IncrementFiStakingConnectors?tab=deployments) | BandOracleConnectors [0x1a9f5d18d096cd7a](https://testnet.flowscan.io/contract/A.1a9f5d18d096cd7a.BandOracleConnectors?tab=deployments) [0xf627b5c89141ed99](https://flowscan.io/contract/A.f627b5c89141ed99.BandOracleConnectors?tab=deployments) | UniswapV2Connectors [0xfef8e4c5c16ccda5](https://testnet.flowscan.io/contract/A.fef8e4c5c16ccda5.UniswapV2Connectors?tab=deployments) [0x0e5b1dececaca3a8](https://flowscan.io/contract/A.0e5b1dececaca3a8.UniswapV2Connectors?tab=deployments)  | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

## Tutorial Series[​](#tutorial-series "Direct link to Tutorial Series")

### [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)[​](#flow-actions "Direct link to flow-actions")

Learn how to build DeFi applications with the Flow Actions framework, which allows developers to create composable DeFi workflows. Flow Actions provide standardized interfaces that make it easy to combine different DeFi protocols and create sophisticated financial applications.

### [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)[​](#scheduled-transactions "Direct link to scheduled-transactions")

Discover how to implement scheduled transactions for time-based smart contract execution on Flow. These tutorials cover how to create automated workflows, cron-like functionality, and time-sensitive blockchain applications that can execute without manual intervention.

### [Passkeys](/build/cadence/advanced-concepts/passkeys)[​](#passkeys "Direct link to passkeys")

Implement device-backed passkeys with the Web Authentication API to register Flow account keys and sign transactions with secure, user-friendly authentication. For more information, see the [advanced concepts documentation](/build/cadence/advanced-concepts/passkeys).

### [High-Precision Fixed-Point Math](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)[​](#high-precision-fixed-point-math "Direct link to high-precision-fixed-point-math")

Learn about Flow's high-precision mathematical utilities for DeFi applications using UInt128-based 24-decimal fixed-point arithmetic. This tutorial covers how to perform accurate financial calculations, handle rounding modes, and avoid precision loss in complex DeFi operations like liquidity pools, yield farming, and token swaps.

## Getting Started[​](#getting-started "Direct link to Getting Started")

To begin with Forte tutorials, we recommend that you start with:

1. **[Introduction to Flow Actions](/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions)** - Understand the core concepts and architecture
2. **[Scheduled Transactions Introduction](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction)** - Learn about time-based execution capabilities

## Key Benefits[​](#key-benefits "Direct link to Key Benefits")

* **Automation**: Build applications that can execute complex workflows automatically
* **Composability**: Combine different protocols and services seamlessly
* **Time-based Logic**: Implement sophisticated scheduling and automation features
* **Developer Experience**: Simplified interfaces for complex blockchain operations

## Conclusion[​](#conclusion "Direct link to Conclusion")

The Forte network upgrade represents a significant evolution of Flow's capabilities, with powerful new tools to build the next generation of decentralized applications. These tutorials provide the foundation for you to leverage these new features to create sophisticated, automated, and composable blockchain applications.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/index.md)

Last updated on **Oct 28, 2025** by **Brian Doyle**

[Previous

Flow Blockchain 101](/blockchain-development-tutorials/flow-101)[Next

Flow Actions](/blockchain-development-tutorials/forte/flow-actions)

###### Rate this page

😞😐😊

Copy as Markdown

* [What's New in Forte](#whats-new-in-forte)* [Deployed Contract Addresses](#deployed-contract-addresses)* [Tutorial Series](#tutorial-series)
      + [Flow Actions](#flow-actions)+ [Scheduled Transactions](#scheduled-transactions)+ [Passkeys](#passkeys)+ [High-Precision Fixed-Point Math](#high-precision-fixed-point-math)* [Getting Started](#getting-started)* [Key Benefits](#key-benefits)* [Conclusion](#conclusion)

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