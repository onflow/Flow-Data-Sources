# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/mobile

Mobile Development on Flow | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  - [IOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)- [React Native Development](/blockchain-development-tutorials/cadence/mobile/react-native-quickstart)- [Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)+ [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* Mobile Development on Flow

On this page

# Mobile Development on Flow

Building mobile native applications that interact with the blockchain allows a much richer end user experience and provides access to OS capabilities. With Flow Mobile, developers can build native applications for iOS and Android with SDKs and mobile wallets.

## Why Flow[​](#why-flow "Direct link to Why Flow")

Millions of users with Flow accounts explore the ecosystem and look for applications. Most of these users purchased Flow NFTs and are comfortable with web3 principles.

In addition to the existing user base, developers can tap into smart contracts deployed on the Flow blockchain. These contracts, including their onchain state, provide unique possibilities to build experiences that enrich currently-used applications.

The following key capabilities make Flow a standout choice for mobile applications:

* On-device key encryption via Secure Enclave & Keychain.
* Mobile wallet compatibility and support for WalletConnect 2.0.
* Simple, progressive onboarding experience with postponed account linking.
* Seamless in-app experience with onchain interactions without constant signing requests.
* Account flexibility enabling secure account recovery and sharing.

## Why Flow Mobile[​](#why-flow-mobile "Direct link to Why Flow Mobile")

### Proven[​](#proven "Direct link to Proven")

Flow is built with mainstream adoption in mind. Mobile applications can leverage the best-in-class user experiences millions of users have enjoyed on the web, through applications like NBA TopShot or NFL AllDay.

### Best-in-class UX[​](#best-in-class-ux "Direct link to Best-in-class UX")

Flow's Client Library makes it very intuitive to sign up and sign in with their wallet of choice. For transaction signing, Flow offers human readable security, so users get a clear understanding of what they are approving. An increased sense of trust for Flow applications is the outcome.

Furthermore, Flow's powerful account model allows for seamless user flows of onchain operations. Apps can perform transactions on behalf of the users (with their approval) in the background, without the need to switch between apps. The account model also allows apps to pay for transactions to postpone fiat on-ramps to get them to experience the value of an application before they commit to buy tokens.

Last, but not least, developers can leverage progressive web3 onboarding, in which you can use any identity provider authenticate users, but don't have to deal with keys. Developers can create Flow accounts for the users and link them to a wallet at a later point in time.

### Security first[​](#security-first "Direct link to Security first")

Flow's mobile SDKs use on-device key encryption via Apple's Secure Enclave and Android's Keystore. The flexible account model makes it possible for an account to have multiple keys with different weights, which enables secure social recovery, account sharing, and much more.

## Smart contract language inspired by mobile languages[​](#smart-contract-language-inspired-by-mobile-languages "Direct link to Smart contract language inspired by mobile languages")

Cadence, Flow's smart contract language, will look and feel very familiar to mobile languages developers are already familiar with. Cadence was inspired by Move, Swift, and Kotlin. This reduces the ramp-up period to develop mobile applications leveraging onchain logic.

## What is available[​](#what-is-available "Direct link to What is available")

Developers can leverage the following features to get productive quickly:

* Swift & Kotlin FCL SDKs to authenticate and interact with the Flow blockchain (query + execute scripts).
* FCL-compatible mobile wallets.
* User authentication with WalletConnect 2.0.
* Basic mobile sample application (MonsterMaker).

## Guides[​](#guides "Direct link to Guides")

**[iOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)** - Learn native iOS development on Flow through the Monster Maker sample project, which demonstrates wallet integration, transaction signing, and NFT management. The tutorial covers FCL Swift SDK integration, WalletConnect 2.0 for wallet connectivity, and essential blockchain interactions like querying and mutating data.

**[React Native Development](/blockchain-development-tutorials/cadence/mobile/react-native-quickstart)** - Build cross-platform mobile dApps using React Native and Flow Client Library (FCL). This guide walks through how to set up authentication, query the blockchain, and execute transactions while interacting with the Profile Contract on Flow's testnet to create and edit user profiles.

**[Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)** - Create an accessible Progressive Web App with seamless onboarding with Magic integration for walletless authentication. The tutorial covers how to build a balloon inflation game that demonstrates Magic SDK integration, hybrid custody features, and account linking to transition from custodial to non-custodial ownership.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Flow Mobile empowers developers to create native blockchain applications that deliver best-in-class user experiences while maintaining the security and flexibility that mainstream adoption demands. Whether building with native SDKs or creating Progressive Web Apps, Flow's mobile development capabilities provide the tools needed to bring web3 to millions of users through intuitive, secure, and feature-rich mobile experiences.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/mobile/index.md)

Last updated on **Nov 4, 2025** by **cshannon1218**

[Previous

Account Linking With NBA Top Shot](/blockchain-development-tutorials/cadence/account-management/account-linking-with-dapper)[Next

IOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)

###### Rate this page

😞😐😊

Copy as Markdown

* [Why Flow](#why-flow)* [Why Flow Mobile](#why-flow-mobile)
    + [Proven](#proven)+ [Best-in-class UX](#best-in-class-ux)+ [Security first](#security-first)* [Smart contract language inspired by mobile languages](#smart-contract-language-inspired-by-mobile-languages)* [What is available](#what-is-available)* [Guides](#guides)* [Conclusion](#conclusion)

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