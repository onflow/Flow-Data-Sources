# Source: https://developers.flow.com/build/core-contracts/nft-metadata

NFT Metadata Contract | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* [Explore More](/build/explore-more)

* [Core Smart Contracts](/build/core-contracts)
* NFT Metadata

# NFT Metadata Contract

The `ViewResolver` and `MetadataViews` contracts implement a standard to attach on-chain metadata
to NFTs. This standard was originally proposed in [FLIP-0636](https://github.com/onflow/flips/blob/main/application/20210916-nft-metadata.md).

It is deployed at the same address as the `NonFungibleToken` contract interface.

Source: [ViewResolver.cdc](https://github.com/onflow/flow-nft/blob/master/contracts/ViewResolver.cdc)

Source: [MetadataViews.cdc](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0x631e88ae7f1d7c20` |
| Mainnet | `0x1d7e57aa55817448` |

There exists a tool, [Flow NFT Catalog](https://flow-nft-catalog.com), which enables dapp developers the ability to unlock interoperability of your NFT collection across the Flow ecosystem. This will help make your NFT collection's metadata more discoverable and interoperable.

To optimize your NFT collections for this catalog, you'll need to:

1. Update your NFT contract to support `ViewResolver` and `MetadataViews` with implementation of the [core NFT views](/build/advanced-concepts/metadata-views).
2. Deploy the updated contract to both testnet and mainnet.
3. Afterwards, onboard your NFT to the Flow NFT catalog at <https://flow-nft-catalog.com>.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/09-nft-metadata.md)

Last updated on **Mar 4, 2025** by **Brian Doyle**

[Previous

Non-Fungible Token](/build/core-contracts/non-fungible-token)[Next

NFT Storefront](/build/core-contracts/nft-storefront)

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