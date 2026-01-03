# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/crossmint

Crossmint Integration Guide | Flow Developer Portal



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

* * [Third-Party Integrations](/blockchain-development-tutorials/integrations)* Crossmint Integration Guide

On this page

# Crossmint Integration Guide

Crossmint is an all-in-one platform that brings enterprise-grade blockchain infrastructure to Flow developers. Build complete Web3 applications without a need for your users to understand crypto - from embedded wallets and gasless payments to AI agent commerce and stablecoin integration.

**Why this matters:**

* **Eliminate barriers**: No gas fees, seed phrases, or complex wallet setup for your users.
* **Enterprise ready**: Bank-grade security trusted by Fortune 500 companies.

With Crossmint on Flow, you can create comprehensive blockchain applications that feel like traditional Web2 apps and leverage Flow's unique capabilities.

**Core features:** Gasless transactions, fiat payments, token minting

## 🎯 Available Features[​](#-available-features "Direct link to 🎯 Available Features")

### 1. Minting platform[​](#1-minting-platform "Direct link to 1. Minting platform")

Create and distribute tokens at scale via API and no-code tools. You'll be able to:

* Deploy secure smart contracts on Flow.
* Mint, update, burn, and airdrop tokens at scale.
* Manage metadata and collections.
* API and no-code collection creation.

### 2. Authentication[​](#2-authentication "Direct link to 2. Authentication")

Create wallets for users with seamless authentication. This unlocks:

* Authentication with email, social logins, wallets, and passkeys.
* Smart wallets with custodial and non-custodial options.
* Gasless transactions and improved user experience.
* Data APIs to fetch balances and activity.

### 3. Fiat and cross-chain payment checkout[​](#3-fiat-and-cross-chain-payment-checkout "Direct link to 3. Fiat and cross-chain payment checkout")

Digital Asset Checkout supports fiat and cross-chain payments. Allow your users to buy onchain assets with any of the following payment methods:

* Credit card, Apple Pay, Google Pay support.
* Cross-chain crypto payments (40+ tokens).
* No KYC required for most transactions.

### 4. World store[​](#4-world-store "Direct link to 4. World store")

Access to real-world goods and services via crypto payments such as:

* Over one billion products from Amazon, Shopify, flights, and more.
* Pay with FLOW, USDF, and other supported tokens.
* Perfect for expanding crypto utility to real-world commerce.
* API access to global commerce platforms.

## 🛠 Prerequisites[​](#-prerequisites "Direct link to 🛠 Prerequisites")

Make sure you have:

* **Crossmint account:**

  + [Crossmint Console](https://staging.crossmint.com) account.
  + API keys configured for your project.
* **Flow development environment:**

  + Flow CLI installed and configured.
* **Technical knowledge:**

  + Basic JavaScript/TypeScript, React hooks.
  + Understanding of Flow (Cadence or EVM).
* **Setup:**

  1. Clone or create your Flow project.
  2. Install Crossmint SDK: `npm i @crossmint/client-sdk-react-ui`
  3. Configure environment variables for API keys.
  4. Onboard thousands of users seamlessly.

## Guides[​](#guides "Direct link to Guides")

Get started with Crossmint on Flow in under 15 minutes:

1. **[Set up authentication](/blockchain-development-tutorials/integrations/crossmint/authentication)** to seamlessly onboard users.
2. **[Enable fiat payments](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)** for your Flow assets.
3. **[Minting Platform](/blockchain-development-tutorials/integrations/crossmint/minting-platform)** to create and distribute tokens at scale.

If you have trouble during the integrations process, refer to these documentation sites:

* **[Crossmint Documentation](https://docs.crossmint.com/)** - Complete platform docs.
* **[Flow Developer Portal](https://developers.flow.com/)** - Flow-specific resources.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/integrations/crossmint/index.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)[Next

Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)

###### Rate this page

😞😐😊

Copy as Markdown

* [🎯 Available Features](#-available-features)
  + [1. Minting platform](#1-minting-platform)+ [2. Authentication](#2-authentication)+ [3. Fiat and cross-chain payment checkout](#3-fiat-and-cross-chain-payment-checkout)+ [4. World store](#4-world-store)* [🛠 Prerequisites](#-prerequisites)* [Guides](#guides)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.