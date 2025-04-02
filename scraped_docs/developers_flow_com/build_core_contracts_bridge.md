# Source: https://developers.flow.com/build/core-contracts/bridge

VM Bridge Contracts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
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
* VM Bridge

The Flow VM bridge is the account and series of smart contracts that manage how
assets are safely bridged between the Cadence and EVM Flow Environments.

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0xdfc20aee650fcbdf` |
| Mainnet | `0x1e4aa0b87d10b141` |

# Contracts

There are many important contracts deployed to the bridge account.
You should refer to [the bridge repo](https://github.com/onflow/flow-evm-bridge)
and [the bridge guides](/tutorials/cross-vm-apps/vm-bridge)
for more detailed information about the bridge and tutorials for how to use the bridge properly.

Here is a list of each Cadence contract used for the bridge:

| Contract | Purpose |
| --- | --- |
| `CrossVMNFT` | Contract defining cross-VM NFT-related interfaces |
| `CrossVMToken` | Contract defining cross-VM Fungible Token Vault interface |
| `FlowEVMBridgeHandlerInterfaces` | Defines interface for custom bridged token handlers |
| `IBridgePermissions` | Defines an interface to prevent bridging for a specific token |
| `ICrossVM` | Defines an interface to get EVM contract addresses |
| `ICrossVMAsset` | Defines an interface to represent a Cadence bridged version of an EVM asset |
| `IEVMBridgeNFTMinter` | Defines an interface that allows the bridge to mint NFTs |
| `IEVMBridgeTokenMinter` | Defines an interface that allows the bridge to mint FTs |
| `IFlowEVMNFTBridge` | Defines core methods for bridging NFTs |
| `IFlowEVMTokenBridge` | Defines core methods for bridging FTs |
| `FlowEVMBridge` | The main entrypoint for briding tokens across Flow VMs |
| `FlowEVMBridgeAccessor` | Defines methods to route bridge requests from the EVM contract to the Flow-EVM bridge contract |
| `FlowEVMBridgeConfig` | Used to store configuration options for the VM Bridge |
| `FlowEVMBridgeCustomAssociations` | Stores configuration information about custom bridged asset configurations |
| `FlowEVMBridgeCustomAssociationTypes` | Defines interfaces used to specify custom bridged asset associations |
| `FlowEVMBridgeHandlers` | Defines mechanisms for handling assets with custom associations (Deprecated) |
| `FlowEVMBridgeNFTEscrow` | Handles locking of NFTs that are bridged from Flow to EVM and back |
| `FlowEVMBridgeResolver` | Defines methods to resolve Metadata Views for bridged assets |
| `FlowEVMBridgeTemplates` | Serves Cadence code from chunked templates for bridge-deployed assets |
| `FlowEVMBridgeTokenEscrow` | Handles locking of FTs that are bridged from Flow to EVM and back |
| `FlowEVMBridgeUtils` | Defines many different utility methods that are used by bridge contracts |
| `ArrayUtils` | Provides useful utility functions for manipulating arrays |
| `ScopedFTProviders` | Provides utilities for creating provider capabilities for tokens that are restricted to a specific amount |
| `Serialize` | Provides utilities for serializing common types to json-compatible strings |
| `SerializeMetadata` | Provides methods for serializing NFT metadata as a JSON compatible string |
| `StringUtils` | Provides useful utility functions for manipulating strings |

# EVM Bridge Solidity Contracts

There are also Solidity contracts that are deployed in Flow EVM that are needed for the bridge.
Here are their addresses:

| Contracts | Testnet | Mainnet |
| --- | --- | --- |
| `FlowEVMBridgeFactory.sol` | [`0xf8146b4aef631853f0eb98dbe28706d029e52c52`](https://evm-testnet.flowscan.io/address/0xF8146B4aEF631853F0eB98DBE28706d029e52c52) | [`0x1c6dea788ee774cf15bcd3d7a07ede892ef0be40`](https://evm.flowscan.io/address/0x1C6dEa788Ee774CF15bCd3d7A07ede892ef0bE40) |
| `FlowEVMBridgeDeploymentRegistry.sol` | [`0x8781d15904d7e161f421400571dea24cc0db6938`](https://evm-testnet.flowscan.io/address/0x8781d15904d7e161f421400571dea24cc0db6938) | [`0x8fdec2058535a2cb25c2f8cec65e8e0d0691f7b0`](https://evm.flowscan.io/address/0x8FDEc2058535A2Cb25C2f8ceC65e8e0D0691f7B0) |
| `FlowEVMBridgedERC20Deployer.sol` | [`0x4d45CaD104A71D19991DE3489ddC5C7B284cf263`](https://evm-testnet.flowscan.io/address/0x4d45CaD104A71D19991DE3489ddC5C7B284cf263) | [`0x49631Eac7e67c417D036a4d114AD9359c93491e7`](https://evm.flowscan.io/address/0x49631Eac7e67c417D036a4d114AD9359c93491e7) |
| `FlowEVMBridgedERC721Deployer.sol` | [`0x1B852d242F9c4C4E9Bb91115276f659D1D1f7c56`](https://evm-testnet.flowscan.io/address/0x1B852d242F9c4C4E9Bb91115276f659D1D1f7c56) | [`0xe7c2B80a9de81340AE375B3a53940E9aeEAd79Df`](https://evm.flowscan.io/address/0xe7c2B80a9de81340AE375B3a53940E9aeEAd79Df) |

And below are the bridge escrow's EVM addresses. These addresses are [`CadenceOwnedAccount`s (COA)](https://developers.flow.com/tutorials/cross-vm-apps/interacting-with-coa#coa-interface) and they are stored stored in the same Flow account as you'll find the Cadence contracts (see above).

| Network | Address |
| --- | --- |
| Testnet | [`0x0000000000000000000000023f946ffbc8829bfd`](https://evm-testnet.flowscan.io/address/0x0000000000000000000000023f946FFbc8829BFD) |
| Mainnet | [`0x00000000000000000000000249250a5c27ecab3b`](https://evm.flowscan.io/address/0x00000000000000000000000249250a5C27Ecab3B) |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/15-bridge.md)

Last updated on **Apr 1, 2025** by **Brian Doyle**

[Previous

Burner](/build/core-contracts/burner)[Next

Explore More](/build/explore-more)

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
* [Flowscan Mainnet](https://flowdscan.io/)
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