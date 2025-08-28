# Source: https://developers.flow.com/build/cadence/smart-contracts/overview

Smart Contracts on Flow | Flow Developer Portal



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

    - [Learn Cadence ↗️](/build/cadence/learn-cadence)
    - [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)
    - [Deploying Contracts](/build/cadence/smart-contracts/deploying)
    - [Testing Your Contracts](/build/cadence/smart-contracts/testing)
    - [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)
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

* Cadence
* Writing and Deploying Smart Contracts
* Smart Contracts on Flow

On this page

# Smart Contracts on Flow

At its core, a decentralized application is defined by the [smart contracts](https://en.wikipedia.org/wiki/Smart_contract) it uses on the blockchain. Rather than relying on centralized application servers and databases, apps model their core application logic using smart contracts, often referred to as the "onchain" code.

It is therefore helpful to develop a clear model for your app that takes into account the data and logic that will exist in your smart contracts. In particular, it is important to differentiate between the parts of your app that must live on chain and those that should live off chain.

## How to Write Smart Contracts on Flow[​](#how-to-write-smart-contracts-on-flow "Direct link to How to Write Smart Contracts on Flow")

Smart contracts on the Flow blockchain are implemented in [Cadence](https://github.com/onflow/cadence), a resource-oriented programming language specifically designed for smart contract development.

### Onboard to Cadence[​](#onboard-to-cadence "Direct link to Onboard to Cadence")

To get started with Cadence, we recommended covering the introductory tutorials available in the [Flow Playground](https://play.flow.com/), a simple web IDE designed for learning Cadence.

### Configure Your Local Environment[​](#configure-your-local-environment "Direct link to Configure Your Local Environment")

To build confidently, you will want to set up the appropriate local environment and have an adequate test suite to ensure your smart contracts operate as intended. To do this, familiarize yourself with the following tools:

* [Flow CLI](/build/tools/flow-cli): A utility to directly interact with the chain and manage accounts and contracts.
* [Flow Emulator](/build/tools/emulator): A lightweight server that simulates the Flow blockchain (strongly recommended during development).
* [Flow Dev Wallet](https://github.com/onflow/fcl-dev-wallet/): A utility to simulate user wallets in development.
* [Visual Studio Code Extension](/build/tools/vscode-extension): An IDE integration for developing smart contracts.

## Storing Data on Flow[​](#storing-data-on-flow "Direct link to Storing Data on Flow")

All apps will store important data on the blockchain, and some more than others -- especially NFT apps. You'll want to consider the following when storing data on the Flow blockchain.

### What does your data need to represent?[​](#what-does-your-data-need-to-represent "Direct link to What does your data need to represent?")

Permanence is a key property of blockchains; users trust that the data they store will continue to exist for years to come, and this is a defining characteristic of assets like NFTs. Therefore, well-designed digital assets store the information necessary to retain their value without external dependencies.

### Storage Limits & Fees[​](#storage-limits--fees "Direct link to Storage Limits & Fees")

However, there are practical constraints to storing data on a blockchain. Developer and user accounts must retain a small amount of FLOW tokens, known as the storage fee, for bytes of data stored in their accounts. The minimum storage fee will grant each account a minimum storage amount. If an account holds assets that demand more bytes of storage, the account will need to retain more FLOW tokens to increase the storage amount according to Flow's [fee schedule](/build/cadence/basics/fees#storage). A more compact data model can keep storage needs down.   
  
Furthermore, a single Flow transaction has a size limit of 4MB, which limits the rate at which large amounts of data can be transferred to the blockchain.

Lastly, a blockchain is not a content delivery network and therefore cannot serve media assets, such as videos, at the speeds expected by modern applications.

For these reasons, it usually isn't practical to store large media assets such as videos and high-definition images on the Flow blockchain. Instead, consider using an external storage solution.

### External Storage Networks[​](#external-storage-networks "Direct link to External Storage Networks")

Decentralized storage networks such as IPFS allow you to store large digital assets off chain, but without relying on centralized servers. Rather than saving an entire asset to the Flow blockchain, you can save the content hash (known as a CID on IPFS) on the blockchain and then store the source file off-chain. This way, users can verify that the media file matches the digital asset.

IPFS files can be uploaded via a pinning service such as Pinata; see their [NFT tutorial](https://medium.com/pinata/how-to-create-nfts-like-nba-top-shot-with-flow-and-ipfs-701296944bf) for an example of how to use Pinata with Flow.

It's worth noting that IPFS files are served through [gateways](https://docs.ipfs.io/concepts/ipfs-gateway/), many of which leverage caching to provide fast response times. Cloudflare provides a [public IPFS Gateway](https://developers.cloudflare.com/distributed-web/ipfs-gateway), and Pinata also supports [dedicated gateways with custom domains](https://medium.com/pinata/announcing-dedicated-ipfs-gateways-60f599949ce).

## Using Existing Standards[​](#using-existing-standards "Direct link to Using Existing Standards")

The Flow blockchain has existing smart contract standards for both fungible and non-fungible tokens that you should implement when building your contracts.

### Non-Fungible Tokens (NFTs)[​](#non-fungible-tokens-nfts "Direct link to Non-Fungible Tokens (NFTs)")

All NFTs on the Flow blockchain implement the [NonFungibleToken](/build/cadence/core-contracts/non-fungible-token) interface, allowing them to be compatible with wallets, marketplaces and other cross-app experiences.

See the [NFT Guide](/blockchain-development-tutorials/tokens/nft-cadence) for a guide on how to create a basic NFT contract
that conforms to the standard.

* [Non-Fungible Token (NFT) contract interface](/build/cadence/core-contracts/non-fungible-token)

### NFT Sales and Trading[​](#nft-sales-and-trading "Direct link to NFT Sales and Trading")

Flow has a standard contract to facilitate both the direct sales and peer-to-peer trading of NFTs. The NFT storefront contract is useful for apps that want to provide an NFT marketplace experience.

* [NFT Storefront contract](https://github.com/onflow/nft-storefront)

### Fungible Tokens[​](#fungible-tokens "Direct link to Fungible Tokens")

Fungible tokens (i.e. coins, currencies) on the Flow blockchain, including the default cryptocurrency token FLOW, implement the [FungibleToken](/build/cadence/core-contracts/fungible-token) interface.

See the [FT Guide](/blockchain-development-tutorials/tokens/fungible-token-cadence) for a guide on how to create a basic fungible token
contract that conforms to the standard.

* [Fungible Token contract interface](/build/cadence/core-contracts/fungible-token)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/smart-contracts/overview.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Learn Cadence ↗️](/build/cadence/learn-cadence)[Next

Deploying Contracts](/build/cadence/smart-contracts/deploying)

###### Rate this page

😞😐😊

Copy as Markdown

* [How to Write Smart Contracts on Flow](#how-to-write-smart-contracts-on-flow)
  + [Onboard to Cadence](#onboard-to-cadence)
  + [Configure Your Local Environment](#configure-your-local-environment)
* [Storing Data on Flow](#storing-data-on-flow)
  + [What does your data need to represent?](#what-does-your-data-need-to-represent)
  + [Storage Limits & Fees](#storage-limits--fees)
  + [External Storage Networks](#external-storage-networks)
* [Using Existing Standards](#using-existing-standards)
  + [Non-Fungible Tokens (NFTs)](#non-fungible-tokens-nfts)
  + [NFT Sales and Trading](#nft-sales-and-trading)
  + [Fungible Tokens](#fungible-tokens)

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