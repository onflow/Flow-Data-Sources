# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/crossmint/minting-platform

Minting Platform Integration | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

                      + [Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)+ [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)

                          - [Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)- [Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)- [Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)- [Crossmint Smart Wallets](/blockchain-development-tutorials/integrations/crossmint/smart-wallets)

* * [Third-Party Integrations](/blockchain-development-tutorials/integrations)* [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)* Minting Platform Integration

On this page

# Minting Platform Integration Guide

Deploy secure smart contracts and mint tokens at scale on Flow with Crossmint's comprehensive minting platform.

## Overview[​](#overview "Direct link to Overview")

Crossmint's minting platform provides no-code tools and powerful APIs to create, mint, update, burn, and airdrop tokens on Flow.

> **Key benefits:**

> * Deploy secure smart contracts without coding.
> * Mint, update, burn, and airdrop tokens at scale.
> * Manage metadata and collections.
> * Flow EVM and Cadence support.

---

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Crossmint account with minting activated.
* Flow development environment.
* Basic knowledge of NFT standards.

## Step 1: Deploy smart contract[​](#step-1-deploy-smart-contract "Direct link to Step 1: Deploy smart contract")

### No-code contract deployment[​](#no-code-contract-deployment "Direct link to No-code contract deployment")

1. Go to Crossmint Console > **Collections**
2. Click **Create Collection**
3. Choose **Flow** blockchain and configure:
   * Contract type: ERC-721 or Cadence NFT
   * Collection metadata
   * Royalty settings
   * Access controls

### API contract deployment[​](#api-contract-deployment "Direct link to API contract deployment")

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

## Step 2: mint NFTs[​](#step-2-mint-nfts "Direct link to Step 2: mint NFTs")

### Single NFT minting[​](#single-nft-minting "Direct link to Single NFT minting")

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

### Batch minting[​](#batch-minting "Direct link to Batch minting")

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

## Step 3: airdrops[​](#step-3-airdrops "Direct link to Step 3: airdrops")

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

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)[Next

Crossmint Smart Wallets](/blockchain-development-tutorials/integrations/crossmint/smart-wallets)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Prerequisites](#prerequisites)* [Step 1: Deploy smart contract](#step-1-deploy-smart-contract)
      + [No-code contract deployment](#no-code-contract-deployment)+ [API contract deployment](#api-contract-deployment)* [Step 2: mint NFTs](#step-2-mint-nfts)
        + [Single NFT minting](#single-nft-minting)+ [Batch minting](#batch-minting)* [Step 3: airdrops](#step-3-airdrops)

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