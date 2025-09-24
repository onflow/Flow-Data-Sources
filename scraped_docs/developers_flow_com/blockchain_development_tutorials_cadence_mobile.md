# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/mobile

Mobile Development on Flow | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Flow Actions](/blockchain-development-tutorials/flow-actions)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

  + [Account Linking (FLIP 72)](/blockchain-development-tutorials/cadence/account-management)
  + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

    - [IOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)
    - [React Native Development](/blockchain-development-tutorials/cadence/mobile/react-native-quickstart)
    - [Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* Mobile Development on Flow

On this page

# Mobile Development on Flow

Building mobile native applications that interact with the blockchain enables a much richer end user experiences and provides access to OS capabilities. With Flow Mobile, developers can build native applications for iOS and Android leveraging SDKs and mobile wallets.

## Why Flow[​](#why-flow "Direct link to Why Flow")

Millions of users with Flow accounts are exploring the ecosystem and looking for applications. Most of these users purchased Flow NFTs and are comfortable with web3 principles.

In addition to the existing user base, developers can tap into smart contracts deployed on the Flow blockchain. These contracts, including their onchain state, provide unique possibilities to build experiences that enrich applications users are already using.

The following key capabilities make Flow a standout choice for mobile applications:

* On-device key encryption via Secure Enclave & Keychain
* Mobile wallet compatibility and support for WalletConnect 2.0
* Simple, progressive onboarding experience with postponed account linking
* Seamless in-app experience with onchain interactions without constant signing requests
* Account flexibility enabling secure account recovery and sharing

## Why Flow Mobile[​](#why-flow-mobile "Direct link to Why Flow Mobile")

### Proven[​](#proven "Direct link to Proven")

Flow is built with mainstream adoption in mind. Mobile applications can leverage the best-in-class user experiences millions of users have enjoyed on the web, through applications like NBA TopShot or NFL AllDay.

### Best-in-class UX[​](#best-in-class-ux "Direct link to Best-in-class UX")

Flow's Client Library makes it very intuitive to sign up and sign in with their wallet of choice. For transaction signing, Flow offers human readable security, so users get a clear understanding of what they are approving. An increased sense of trust for Flow applications is the outcome.

Furthermore, Flow's powerful account model allows for seamless user flows of onchain operations. Apps can perform transactions on behalf of the users (with their approval) in the background, without the need to switch between apps. The account model also allows apps to pay for transactions to postpone fiat on-ramps to get them to experience the value of an application before committing to buying tokens.

Last but not least, developers can leverage progressive web3 onboarding, in which any identity provider can be used to authenticate users, without having to deal with keys. Developers can create Flow accounts for the users and link them to a wallet at a later point in time.

### Security first[​](#security-first "Direct link to Security first")

Flow's mobile SDKs use on-device key encryption via Apple's Secure Enclave and Android's Keystore. The flexible account model makes it possible for an account to have multiple keys with different weights, which enables secure social recovery, account sharing, and much more.

## Smart contract language inspired by mobile languages[​](#smart-contract-language-inspired-by-mobile-languages "Direct link to Smart contract language inspired by mobile languages")

Cadence, Flow's smart contract language, will look and feel very familiar to mobile languages developers are already familiar with. Cadence was inspired by Move, Swift, and Kotlin. This reduces the ramp-up period to develop mobile applications leveraging onchain logic.

## What is available[​](#what-is-available "Direct link to What is available")

Developers can leverage the following features to get productive quickly:

* Swift & Kotlin FCL SDKs to auth and interact with the Flow blockchain (query + execute scripts)
* FCL-compatible mobile wallets
* User auth using WalletConnect 2.0
* Basic mobile sample application (MonsterMaker)

## Guides[​](#guides "Direct link to Guides")

**[iOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)** - Learn native iOS development on Flow through the Monster Maker sample project, which demonstrates wallet integration, transaction signing, and NFT management. The tutorial covers FCL Swift SDK integration, WalletConnect 2.0 for wallet connectivity, and essential blockchain interactions like querying and mutating data.

**[React Native Development](/blockchain-development-tutorials/cadence/mobile/react-native-quickstart)** - Build cross-platform mobile dApps using React Native and Flow Client Library (FCL). This guide walks through setting up authentication, querying the blockchain, and executing transactions while interacting with the Profile Contract on Flow's testnet to create and edit user profiles.

**[Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)** - Create an accessible Progressive Web App with seamless onboarding using Magic integration for walletless authentication. The tutorial covers building a balloon inflation game that demonstrates Magic SDK integration, hybrid custody features, and account linking to transition from custodial to non-custodial ownership.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Flow Mobile empowers developers to create native blockchain applications that deliver best-in-class user experiences while maintaining the security and flexibility that mainstream adoption demands. Whether building with native SDKs or creating Progressive Web Apps, Flow's mobile development capabilities provide the tools needed to bring web3 to millions of users through intuitive, secure, and feature-rich mobile experiences.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/mobile/index.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

More Guides](/blockchain-development-tutorials/cadence/account-management/more-guides)[Next

IOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)

###### Rate this page

😞😐😊

Copy as Markdown

* [Why Flow](#why-flow)
* [Why Flow Mobile](#why-flow-mobile)
  + [Proven](#proven)
  + [Best-in-class UX](#best-in-class-ux)
  + [Security first](#security-first)
* [Smart contract language inspired by mobile languages](#smart-contract-language-inspired-by-mobile-languages)
* [What is available](#what-is-available)
* [Guides](#guides)
* [Conclusion](#conclusion)

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
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.