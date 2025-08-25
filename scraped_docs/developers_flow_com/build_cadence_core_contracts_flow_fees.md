# Source: https://developers.flow.com/build/cadence/core-contracts/flow-fees

Flow Fees Contract | Flow Developer Portal



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
  + [Guides](/build/cadence/guides/account-linking)
  + [Core Smart Contracts](/build/cadence/core-contracts)

    - [Fungible Token](/build/cadence/core-contracts/fungible-token)
    - [Flow Token](/build/cadence/core-contracts/flow-token)
    - [Service Account](/build/cadence/core-contracts/service-account)
    - [Flow Fees](/build/cadence/core-contracts/flow-fees)
    - [Staking Table](/build/cadence/core-contracts/staking-contract-reference)
    - [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)
    - [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)
    - [NFT Metadata](/build/cadence/core-contracts/nft-metadata)
    - [NFT Storefront](/build/cadence/core-contracts/nft-storefront)
    - [Staking Collection](/build/cadence/core-contracts/staking-collection)
    - [Account Linking](/build/cadence/core-contracts/hybrid-custody)
    - [EVM](/build/cadence/core-contracts/evm)
    - [Burner](/build/cadence/core-contracts/burner)
    - [VM Bridge](/build/cadence/core-contracts/bridge)
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
  + [Guides](/build/evm/guides)
* [Tools & SDKs](/build/tools)

* Cadence
* [Core Smart Contracts](/build/cadence/core-contracts)
* Flow Fees

On this page

# Flow Fees Contract

## FlowFees[​](#flowfees "Direct link to FlowFees")

The `FlowFees` contract is where all the collected flow fees are gathered.

Source: [FlowFees.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowFees.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xe5a8b7f23e8b548f` |
| Cadence Testing Framework | `0x0000000000000004` |
| Testnet | `0x912d5440f7e3769e` |
| Mainnet | `0xf919ee77447b7497` |

### Events[​](#events "Direct link to Events")

Important events for `FlowFees` are:

`_11

// Event that is emitted when tokens are deposited to the fee vault

_11

access(all) event TokensDeposited(amount: UFix64)

_11

_11

// Event that is emitted when tokens are withdrawn from the fee vault

_11

access(all) event TokensWithdrawn(amount: UFix64)

_11

_11

// Event that is emitted when fees are deducted

_11

access(all) event FeesDeducted(amount: UFix64, inclusionEffort: UFix64, executionEffort: UFix64)

_11

_11

// Event that is emitted when fee parameters change

_11

access(all) event FeeParametersChanged(surgeFactor: UFix64, inclusionEffortCost: UFix64, executionEffortCost: UFix64)`

## FlowStorageFees[​](#flowstoragefees "Direct link to FlowStorageFees")

The `FlowStorageFees` contract defines the parameters and utility methods for storage fees.

Source: [FlowStorageFees.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowStorageFees.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0x8c5303eaa26202d6` |
| Mainnet | `0xe467b9dd11fa00df` |

### Events[​](#events-1 "Direct link to Events")

Important events for `FlowStorageFees` are:

`_10

// Emitted when the amount of storage capacity an account has per reserved Flow token changes

_10

access(all) event StorageMegaBytesPerReservedFLOWChanged(_ storageMegaBytesPerReservedFLOW: UFix64)

_10

_10

// Emitted when the minimum amount of Flow tokens that an account needs to have reserved for storage capacity changes.

_10

access(all) event MinimumStorageReservationChanged(_ minimumStorageReservation: UFix64)`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/05-flow-fees.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Service Account](/build/cadence/core-contracts/service-account)[Next

Staking Table](/build/cadence/core-contracts/staking-contract-reference)

###### Rate this page

😞😐😊

Copy as Markdown

* [FlowFees](#flowfees)
  + [Events](#events)
* [FlowStorageFees](#flowstoragefees)
  + [Events](#events-1)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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