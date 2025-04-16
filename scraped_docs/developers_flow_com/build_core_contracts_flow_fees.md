# Source: https://developers.flow.com/build/core-contracts/flow-fees

Flow Fees Contract | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)

  + [Fungible Token](/build/core-contracts/fungible-token)
  + [Flow Token](/build/core-contracts/flow-token)
  + [Service Account](/build/core-contracts/service-account)
  + [Flow Fees](/build/core-contracts/flow-fees)
  + [Staking Table](/build/core-contracts/staking-contract-reference)
  + [Epoch Contracts](/build/core-contracts/epoch-contract-reference)
  + [Non-Fungible Token](/build/core-contracts/non-fungible-token)
  + [NFT Metadata](/build/core-contracts/nft-metadata)
  + [NFT Storefront](/build/core-contracts/nft-storefront)
  + [Staking Collection](/build/core-contracts/staking-collection)
  + [Account Linking](/build/core-contracts/hybrid-custody)
  + [EVM](/build/core-contracts/evm)
  + [Burner](/build/core-contracts/burner)
  + [VM Bridge](/build/core-contracts/bridge)
* [Explore More](/build/explore-more)

* [Core Smart Contracts](/build/core-contracts)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/05-flow-fees.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

[Previous

Service Account](/build/core-contracts/service-account)[Next

Staking Table](/build/core-contracts/staking-contract-reference)

###### Rate this page

😞😐😊

* [FlowFees](#flowfees)
  + [Events](#events)
* [FlowStorageFees](#flowstoragefees)
  + [Events](#events-1)

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