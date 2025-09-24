# Source: https://developers.flow.com/blockchain-development-tutorials/cross-vm-apps

Cross-VM Apps | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Flow Actions](/blockchain-development-tutorials/flow-actions)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

  + [Batched Tx From Scaffold](/blockchain-development-tutorials/cross-vm-apps/introduction)
  + [Update Existing wagmi App](/blockchain-development-tutorials/cross-vm-apps/add-to-wagmi)
  + [Batched EVM Transactions](/blockchain-development-tutorials/cross-vm-apps/batched-evm-transactions)
  + [Direct Calls to Flow EVM](/blockchain-development-tutorials/cross-vm-apps/direct-calls)
  + [Interacting with COAs](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa)
  + [Cross-VM Bridge](/blockchain-development-tutorials/cross-vm-apps/vm-bridge)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* Cross-VM Apps

On this page

# Cross-VM App Tutorials

This series covers how to build cross-VM applications that integrate Flow EVM with Flow Cadence, unlocking new capabilities by combining both environments. Flow's unique architecture enables seamless interaction between Cadence smart contracts and EVM-compatible contracts, allowing developers to leverage the best features of both virtual machines in a single application.

## Tutorials[​](#tutorials "Direct link to Tutorials")

### [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps/introduction)[​](#batched-transactions "Direct link to batched-transactions")

Learn to create hybrid applications using FCL, wagmi, and RainbowKit that connect simultaneously to Flow EVM and Flow Cadence. This comprehensive tutorial demonstrates building "Click to Mint," a game where users can mint ERC-20 tokens individually or batch 10 transactions with a single signature using Cadence's powerful multi-call functionality. You'll integrate traditional EVM development tools with Flow's advanced features while maintaining familiar wagmi/viem patterns. The tutorial covers project setup, wallet integration, smart contract interaction, and UI/UX improvements for cross-VM applications.

### [Add Flow Cadence to Your wagmi App](/blockchain-development-tutorials/cross-vm-apps/add-to-wagmi)[​](#add-flow-cadence-to-your-wagmi-app "Direct link to add-flow-cadence-to-your-wagmi-app")

Discover how to enhance your existing wagmi/RainbowKit applications by integrating Flow Cadence functionality without rebuilding from scratch. This guide shows you how to add FCL to your current EVM-based dApp to enable advanced features like batched transactions, native randomness, and account abstraction. You'll learn to manage concurrent connections to both Flow EVM and Cadence environments while maintaining your existing user interface and development workflows. The tutorial provides step-by-step integration strategies and best practices for hybrid application architecture.

### [Interacting with COAs](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa)[​](#interacting-with-coas "Direct link to interacting-with-coas")

Master the creation and management of Cadence Owned Accounts (COAs), which enable Cadence smart contracts to control EVM accounts on Flow. This tutorial covers setting up COAs, understanding their permissions model, and implementing secure interactions between Cadence and EVM environments. You'll learn how to deploy and manage EVM contracts from Cadence, handle cross-VM asset transfers, and implement proper access controls for hybrid applications.

### [Batched EVM Transactions](/blockchain-development-tutorials/cross-vm-apps/batched-evm-transactions)[​](#batched-evm-transactions "Direct link to batched-evm-transactions")

Explore advanced techniques for executing multiple EVM transactions atomically within a single Cadence transaction. This guide demonstrates how to batch complex EVM operations like multi-step DeFi protocols, NFT minting sequences, or arbitrage strategies while maintaining transaction atomicity. You'll learn to handle transaction failures gracefully, optimize gas usage across batched calls, and implement error handling for complex multi-transaction workflows.

### [Direct Calls to Flow EVM](/blockchain-development-tutorials/cross-vm-apps/direct-calls)[​](#direct-calls-to-flow-evm "Direct link to direct-calls-to-flow-evm")

Learn how Cadence smart contracts can directly interact with Flow EVM without requiring separate user transactions. This technical guide covers making direct calls from Cadence to query EVM state, execute EVM transactions programmatically, and handle responses and errors appropriately. You'll understand gas calculation models, transaction status handling, and best practices for integrating direct EVM calls into your Cadence contracts.

### [Cross-VM Bridge](/blockchain-development-tutorials/cross-vm-apps/vm-bridge)[​](#cross-vm-bridge "Direct link to cross-vm-bridge")

Explore the automated bridging of fungible and non-fungible tokens between Flow Cadence and Flow EVM environments. This comprehensive guide covers the Cross-VM Bridge protocol, which enables atomic movement of ERC-20, ERC-721, and Flow native tokens between virtual machines. You'll learn to onboard tokens to the bridge, implement custom token associations, handle bridging fees, and design tokens that work seamlessly across both Cadence and EVM environments.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Cross-VM applications represent the future of blockchain development on Flow, combining Cadence's innovative resource-oriented programming with EVM's ecosystem compatibility. These tutorials provide the foundation for building sophisticated applications that leverage both virtual machines, enabling developers to create unique experiences that wouldn't be possible on single-VM blockchains while maintaining compatibility with existing Ethereum tooling and user expectations.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cross-vm-apps/index.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)[Next

Batched Tx From Scaffold](/blockchain-development-tutorials/cross-vm-apps/introduction)

###### Rate this page

😞😐😊

Copy as Markdown

* [Tutorials](#tutorials)
  + [Batched Transactions](#batched-transactions)
  + [Add Flow Cadence to Your wagmi App](#add-flow-cadence-to-your-wagmi-app)
  + [Interacting with COAs](#interacting-with-coas)
  + [Batched EVM Transactions](#batched-evm-transactions)
  + [Direct Calls to Flow EVM](#direct-calls-to-flow-evm)
  + [Cross-VM Bridge](#cross-vm-bridge)
* [Conclusion](#conclusion)

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
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.