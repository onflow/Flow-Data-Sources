# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/crossmint/minting-platform

Minting Platform Integration | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Actions](/blockchain-development-tutorials/defi)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Token Launch](/blockchain-development-tutorials/token-launch)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [FlowtoBooth](/blockchain-development-tutorials/flowtobooth)
* [Integrations](/blockchain-development-tutorials/integrations/crossmint)

  + [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)

    - [Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)
    - [Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)
    - [Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)
  + [Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)

* Integrations
* [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)
* Minting Platform Integration

On this page

# Minting Platform Integration Guide

Deploy secure smart contracts and mint tokens at scale on Flow using Crossmint's comprehensive minting platform.

## Overview[​](#overview "Direct link to Overview")

Crossmint's minting platform provides no-code tools and powerful APIs to create, mint, update, burn, and airdrop tokens on Flow.

> **Key Benefits:**
>
> * Deploy secure smart contracts without coding
> * Mint, update, burn, and airdrop tokens at scale
> * Manage metadata and collections
> * Flow EVM and Cadence support

---

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Crossmint account with minting enabled
* Flow development environment
* Basic understanding of NFT standards

## Step 1: Deploy Smart Contract[​](#step-1-deploy-smart-contract "Direct link to Step 1: Deploy Smart Contract")

### No-Code Contract Deployment[​](#no-code-contract-deployment "Direct link to No-Code Contract Deployment")

1. Go to Crossmint Console > **Collections**
2. Click **Create Collection**
3. Choose **Flow** blockchain and configure:
   * Contract type: ERC-721 or Cadence NFT
   * Collection metadata
   * Royalty settings
   * Access controls

### API Contract Deployment[​](#api-contract-deployment "Direct link to API Contract Deployment")

`_15

// Deploy contract via API

_15

const contract = await crossmint.contracts.deploy({

_15

blockchain: "flow",

_15

type: "erc-721",

_15

name: "My Flow Collection",

_15

symbol: "MFC",

_15

metadata: {

_15

description: "Amazing NFTs on Flow",

_15

image: "https://example.com/collection.png"

_15

},

_15

royalty: {

_15

recipient: "0x...",

_15

percentage: 250 // 2.5%

_15

}

_15

});`

## Step 2: Mint NFTs[​](#step-2-mint-nfts "Direct link to Step 2: Mint NFTs")

### Single NFT Minting[​](#single-nft-minting "Direct link to Single NFT Minting")

`_13

const nft = await crossmint.nfts.mint({

_13

collectionId: "your-collection-id",

_13

recipient: "user-wallet-address",

_13

metadata: {

_13

name: "Amazing Flow NFT",

_13

description: "Unique digital art",

_13

image: "https://example.com/nft.png",

_13

attributes: [

_13

{ trait_type: "Rarity", value: "Legendary" },

_13

{ trait_type: "Network", value: "Flow" }

_13

]

_13

}

_13

});`

### Batch Minting[​](#batch-minting "Direct link to Batch Minting")

`_10

const batchMint = await crossmint.nfts.batchMint({

_10

collectionId: "your-collection-id",

_10

recipients: [

_10

{ address: "0x...", metadata: { name: "NFT #1" } },

_10

{ address: "0x...", metadata: { name: "NFT #2" } }

_10

]

_10

});`

## Step 3: Airdrops[​](#step-3-airdrops "Direct link to Step 3: Airdrops")

`_10

const airdrop = await crossmint.airdrops.create({

_10

collectionId: "your-collection-id",

_10

recipients: ["0x...", "0x...", "0x..."],

_10

metadata: {

_10

name: "Flow Airdrop NFT",

_10

description: "Special airdrop for community"

_10

}

_10

});`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/integrations/crossmint/minting-platform.md)

Last updated on **Aug 17, 2025** by **0xLisanAlGaib**

[Previous

Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)[Next

Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Step 1: Deploy Smart Contract](#step-1-deploy-smart-contract)
  + [No-Code Contract Deployment](#no-code-contract-deployment)
  + [API Contract Deployment](#api-contract-deployment)
* [Step 2: Mint NFTs](#step-2-mint-nfts)
  + [Single NFT Minting](#single-nft-minting)
  + [Batch Minting](#batch-minting)
* [Step 3: Airdrops](#step-3-airdrops)

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