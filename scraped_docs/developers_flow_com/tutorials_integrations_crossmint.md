# Source: https://developers.flow.com/tutorials/integrations/crossmint

Crossmint Integration Guide | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [DeFi Actions](/tutorials/defi)
* [Tutorials](/tutorials)
* [Flow Blockchain 101](/tutorials/flow-101)
* [Use AI To Build On Flow](/tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/tutorials/gasless-transactions)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)
* [Integrations](/tutorials/integrations/crossmint)

  + [Crossmint Integration Guide](/tutorials/integrations/crossmint)

    - [Authentication Integration Guide](/tutorials/integrations/crossmint/authentication)
    - [Payment Checkout Integration](/tutorials/integrations/crossmint/payment-checkout)
    - [Minting Platform Integration](/tutorials/integrations/crossmint/minting-platform)
  + [Gelato Smart Wallet](/tutorials/integrations/gelato-sw)

* Integrations
* Crossmint Integration Guide

On this page

# Crossmint Integration Guide

Crossmint is an all-in-one platform that brings enterprise-grade blockchain infrastructure to Flow developers. Build complete Web3 applications without requiring users to understand crypto - from embedded wallets and gasless payments to AI agent commerce and stablecoin integration.

**Why this matters:**

* **Eliminate barriers**: No gas fees, seed phrases, or complex wallet setup for your users
* **Enterprise ready**: Bank-grade security trusted by Fortune 500 companies

With Crossmint on Flow, you can create comprehensive blockchain applications that feel like traditional Web2 apps while leveraging Flow's unique capabilities.

**Core features:** Gasless transactions, fiat payments, token minting

## 🎯 Available Features[​](#-available-features "Direct link to 🎯 Available Features")

### 1. Minting Platform[​](#1-minting-platform "Direct link to 1. Minting Platform")

Create and distribute tokens at scale via API and no-code tools. You'll be able to:

* Deploy secure smart contracts on Flow
* Mint, update, burn, and airdrop tokens at scale
* Manage metadata and collections
* API and no-code collection creation

### 2. Authentication[​](#2-authentication "Direct link to 2. Authentication")

Create wallets for users with seamless authentication. This unlocks:

* Authentication with email, social logins, wallets, and passkeys
* Smart wallets with custodial and non-custodial options
* Gasless transactions and improved user experience
* Data APIs for fetching balances and activity

### 3. Fiat and Cross-chain Payment Checkout[​](#3-fiat-and-cross-chain-payment-checkout "Direct link to 3. Fiat and Cross-chain Payment Checkout")

Digital Asset Checkout supporting fiat and cross-chain payments. Allow your users to buy onchain assets using any of the following payment methods:

* Credit card, Apple Pay, Google Pay support
* Cross-chain crypto payments (40+ tokens)
* No KYC required for most transactions

### 4. World Store[​](#4-world-store "Direct link to 4. World Store")

Access to real-world goods and services via crypto payments such as:

* Over 1 billion products from Amazon, Shopify, flights, and more
* Pay with FLOW, USDF, and other supported tokens
* Perfect for expanding crypto utility to real-world commerce
* API access to global commerce platforms

## 🛠 Prerequisites[​](#-prerequisites "Direct link to 🛠 Prerequisites")

Make sure you have:

* **Crossmint account:**

  + [Crossmint Console](https://staging.crossmint.com) account
  + API keys configured for your project
* **Flow development environment:**

  + Flow CLI installed and configured
* **Technical knowledge:**

  + Basic JavaScript/TypeScript, React hooks
  + Understanding of Flow (Cadence or EVM)
* **Setup:**

  1. Clone or create your Flow project
  2. Install Crossmint SDK: `npm i @crossmint/client-sdk-react-ui`
  3. Configure environment variables for API keys
  4. Onboard thousands of users seamlessly

## Guides[​](#guides "Direct link to Guides")

Get up and running with Crossmint on Flow in under 15 minutes:

1. **[Set up authentication](/tutorials/integrations/crossmint/authentication)** for seamless user onboarding
2. **[Enable fiat payments](/tutorials/integrations/crossmint/payment-checkout)** for your Flow assets
3. **[Minting Platform](/tutorials/integrations/crossmint/minting-platform)** to create and distribute tokens at scale

If you have trouble during the integrations process, please refer to these documentation sites:

* **[Crossmint Documentation](https://docs.crossmint.com/)** - Complete platform docs
* **[Flow Developer Portal](https://developers.flow.com/)** - Flow-specific resources

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/integrations/crossmint/index.md)

Last updated on **Jul 31, 2025** by **0xLisanAlGaib**

[Previous

VRF (Randomness) in Solidity](/tutorials/native-vrf/vrf-in-solidity)[Next

Authentication Integration Guide](/tutorials/integrations/crossmint/authentication)

###### Rate this page

😞😐😊

Copy as Markdown

* [🎯 Available Features](#-available-features)
  + [1. Minting Platform](#1-minting-platform)
  + [2. Authentication](#2-authentication)
  + [3. Fiat and Cross-chain Payment Checkout](#3-fiat-and-cross-chain-payment-checkout)
  + [4. World Store](#4-world-store)
* [🛠 Prerequisites](#-prerequisites)
* [Guides](#guides)

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
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.