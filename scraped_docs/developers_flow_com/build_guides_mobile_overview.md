# Source: https://developers.flow.com/build/guides/mobile/overview




Overview | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
  + [Create a Fungible Token](/build/guides/fungible-token)
  + [Create an NFT Project](/build/guides/nft)
  + [Account Linking (FLIP 72)](/build/guides/account-linking)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Building on Mobile](/build/guides/mobile/overview)
    - [Overview](/build/guides/mobile/overview)
    - [Build a Walletless Mobile App (PWA)](/build/guides/mobile/walletless-pwa)
    - [IOS Development](/build/guides/mobile/ios-quickstart)
    - [React Native Development](/build/guides/mobile/react-native-quickstart)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Guides
* Building on Mobile
* Overview
On this page
# Overview

Building mobile native applications that interact with the blockchain enables a much richer end user experiences and provides access to OS capabilities. With Flow Mobile, developers can build native applications for iOS and Android leveraging SDKs and mobile wallets.

## Why Flow[​](#why-flow "Direct link to Why Flow")

Millions of users with Flow accounts are exploring the ecosystem and looking for applications. Most of these users purchased Flow NFTs and are comfortable with web3 principles.

In addition to the existing userbase, developers can tap into smart contracts deployed on the Flow blockchain. These contracts, including their on-chain state, provide unique possibilities to build experiences that enrich applications users are already using.

The following key capabilities make Flow a standout choice for mobile applications:

* On-device key encryption via Secure Enclave & Keychain
* Mobile wallet compabilitity and support for WalletConnect 2.0
* Simple, progressive onboarding experience with postponed account linking
* Seamless in-app experience with on-chain interactions without constant signing requests
* Account flexibility enabling secure account recovery and sharing

## Why Flow Mobile[​](#why-flow-mobile "Direct link to Why Flow Mobile")

### Proven[​](#proven "Direct link to Proven")

Flow is built with mainstream adoption in mind. Mobile applications can leverage the best-in-class user experiences millions of users have enjoyed on the web, through applications like NBA TopShot or NFL AllDay.

### Best-in-class UX[​](#best-in-class-ux "Direct link to Best-in-class UX")

Flow's Client Library makes it very intuitive to sign up and sign in with their wallet of choice. For transaction signing, Flow offers human readable security, so users get a clear understanding of what they are approving. An increased sense of trust for Flow applications is the outcome.

Furthermore, Flow's powerful account model allows for seamless user flows of on-chain operations. Apps can perform transactions on behalf of the users (with their approval) in the background, without the need to switch between apps. The account model also allows apps to pay for transactions to postpone fiat on-ramps to get them to experience the value of an application before committing to buying tokens.

Last but not least, developers can leverage progressive web3 onboarding, in which any identity provider can be used to authenticate users, without having to deal with keys. Developers can create Flow accounts for the users and link them to a wallet at a later point in time.

### Security first[​](#security-first "Direct link to Security first")

Flow's mobile SDKs use on-device key encryption via Apple's Secure Enclave and Android's Keystore. The flexible account model makes it possible for an account to have multiple keys with different weights, which enables secure social recovery, account sharing, and much more.

## Smart contract language inspired by mobile languages[​](#smart-contract-language-inspired-by-mobile-languages "Direct link to Smart contract language inspired by mobile languages")

Cadence, Flow's smart contract language, will look and feel very familiar to mobile languages developers are already familiar with. Cadence was inspired by Move, Swift, and Kotlin. This reduces the ramp-up period to develop mobile applications leveraging on-chain logic.

## What is available[​](#what-is-available "Direct link to What is available")

Developers can leverage the following features to get productive quickly:

* Swift & Kotlin FCL SDKs to auth and interact with the Flow blockchain (query + execute scripts)
* FCL-compatible mobile wallets
* User auth using WalletConnect 2.0
* Basic mobile sample application (MonsterMaker)

Coming soon:

* Samples for key in-app functionality, like in-app purchasing
* Progressive user onboarding
[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/mobile/overview.md)Last updated on **Dec 24, 2024** by **Navid TehraniFar**[PreviousMore Guides](/build/guides/more-guides)[NextBuild a Walletless Mobile App (PWA)](/build/guides/mobile/walletless-pwa)
###### Rate this page

😞😐😊

* [Why Flow](#why-flow)
* [Why Flow Mobile](#why-flow-mobile)
  + [Proven](#proven)
  + [Best-in-class UX](#best-in-class-ux)
  + [Security first](#security-first)
* [Smart contract language inspired by mobile languages](#smart-contract-language-inspired-by-mobile-languages)
* [What is available](#what-is-available)
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

