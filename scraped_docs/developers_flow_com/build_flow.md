# Source: https://developers.flow.com/build/flow

Why Flow - The Best Blockchain for Consumer Apps and Web3 Development | Flow Developer Portal



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
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

* Why Flow

On this page

# Why Flow is the best for consumer apps and Web3 development

Flow is the blockchain designed to be the [best platform for consumer apps](https://flow.com/) and Web3 as a whole. Built by consumer-facing, onchain app developers to solve the problem of building consumer-facing, onchain apps, Flow supports two powerful programming languages: **Cadence** and **Solidity**.

Dieter Shirley, Chief Architect of Flow and co-author of the [ERC-721 NFT standard](https://github.com/ethereum/eips/issues/721), calls Flow:

> ***A computer that anyone can use, everyone can trust, and no one can shut down***

Much of the protocol design is based on lessons learned from building Web3 applications while working at [Dapper Labs](https://www.dapperlabs.com/), particularly [CryptoKitties](https://www.cryptokitties.co/) — the first onchain game to reach [widespread popularity](https://www.cnn.com/style/article/cryptokitty-blockchain/index.html). The game went viral, then [struggled under its own success](https://spectrum.ieee.org/cryptokitties) when it caused so much traffic that the Ethereum network itself was overwhelmed by the load.

The design of Flow was guided by the need to alleviate this burden while creating the best experience possible for both developers and users. The blockchain network of the future must be able to handle millions of users while upholding the key pillars of decentralization:

1. Verifiability
2. Predictability/Reliability
3. Equitable Access for All
4. Permissionless Composability
5. Interoperability
6. Security

Flow solves the [blockchain trilemma](https://coinmarketcap.com/academy/glossary/blockchain-trilemma) and represents the next generation of blockchain technology. It's built to enable seamless consumer-scale apps without compromising decentralization or user experience, and is the chosen blockchain network for [NBA Top Shot](https://nbatopshot.com/), [NFL All Day](https://nflallday.com/), [Mattel Creations](https://creations.mattel.com/pages/virtual), and [Disney Pinnacle](https://disneypinnacle.com/).

## What makes Flow unique[​](#what-makes-flow-unique "Direct link to What makes Flow unique")

Flow is a fast, decentralized, and developer-friendly blockchain designed to be the foundation for a new generation of games, apps, and the [digital assets](https://www.flow.com/post/flow-blockchain-cadence-programming-language-resources-assets) that power them. It is based on a unique [multi-role architecture](https://flow.com/post/flow-blockchain-multi-node-architecture-advantages) and designed to [scale without sharding](https://www.flow.com/post/flow-blockchain-multi-node-architecture-advantages), allowing for massive improvements in speed and throughput while preserving a developer-friendly, ACID-compliant environment.

### Dual language architecture[​](#dual-language-architecture "Direct link to Dual language architecture")

Flow is unique in supporting two powerful programming languages for smart contract development:

* **Cadence**: A modern programming language developed by smart contract application builders.
* **Solidity**: The industry-standard language for EVM development, fully supported on Flow with full EVM equivalence.

EVM and Cadence environments both use FLOW as gas for transactions and are connected by a native bridge that allows seamless and cheap communication between them. Fungible and non-fungible tokens can also be seamlessly transferred between environments using the native VM token bridge, taking place instantly in a single atomic transaction.

This means developers can choose the language that best fits their needs while maintaining full interoperability between both environments.

### Cadence development on Flow[​](#cadence-development-on-flow "Direct link to Cadence development on Flow")

[Cadence](https://cadence-lang.org/) is a modern programming language developed by smart contract application builders for smart contract developers:

* **Advanced Transactions**: [Transactions](https://cadence-lang.org/docs/language/transactions) in Cadence smart contracts are not simply calls to existing functions on already deploy contracts. Instead, transactions are code written in Cadence that can **call any function (with appropriate access) on any smart contract by any author**, all in a single, atomic transaction with a single user signature.
* **AI Ready**: Cadence transactions have [pre- and post-conditions](https://cadence-lang.org/docs/language/pre-and-post-conditions) that clearly define the inputs to a transactions, such as the tokens that may be withdrawn, and outcomes, such as collectibles that must be purchased. With these definitions, Cadence transactions of immense complexity can be written safely. Regardless of code in the actual execution, the user can be sure that they will get what they expected and only pay the price they authorized.
* **Data Availability**: Similarly, any author can construct a **view** function to access any public data on any smart contract without needing the author of that smart contract to have anticipated the need to view that data or reliance a provider to cache it and make it available.
* **Native account abstraction**: Cadence transactions have protocol-native [account abstraction](https://flow.com/account-abstraction). All accounts are smart accounts, supporting scripting, multiple keys, multi-signature transactions, and walletless onboarding with social logins.
* **Gasless transactions**: Cadence transactions have multiple [signing roles](/build/cadence/basics/transactions#signer-roles) for each transaction. Most notably, the payer can be set independently of the authorizer. In other words, having one account sign a transaction and another pay for that transaction is a built-in feature.
* **Security**: Smart contracts on Flow are natively written in , an easier, safer, and more secure programming language for crypto assets and apps. It's the first high-level, [resource-oriented](https://flow.com/post/resources-programming-ownership) programming language.
* **Developer ergonomics**: The Flow network is designed to maximize developer productivity. Examples range from upgradeable smart contracts to built-in logging support to the Flow Emulator.

### Solidity development on Flow EVM[​](#solidity-development-on-flow-evm "Direct link to Solidity development on Flow EVM")

Flow EVM provides the best EVM experience available anywhere:

* **Speed, cost, and compatibility**: Flow EVM can already run all of your audited Solidity contracts at an average of less than 1 cent per transaction ([usually way less!](https://evm.flowscan.io/stats)). Unlike L2 solutions, Flow EVM reaches true finality in seconds — not in [a week](https://docs.optimism.io/stack/rollup/overview#fault-proofs).
* **Bridge from Other EVM networks**: You can [bridge](/ecosystem/bridges) hundreds of assets from dozens of chains to Flow.
* **VM token bridge**: Assets can be bridged between Flow Cadence and Flow EVM easily and atomically with the VM token bridge. Assets can even be bridged **and used** in a **single** transaction, allowing full composability between the EVM and Cadence environments.
* **Access to Cadence features**: Access Cadence features and contracts from Flow EVM to take advantage of native [VRF](/blockchain-development-tutorials/native-vrf/vrf-in-solidity), higher computation for lower cost, and any asset on Cadence Flow. You can also build [cross-vm apps](/blockchain-development-tutorials/cross-vm-apps) on top of the *wagmi/viem/RainbowKit* stack, enabling batched transactions and more.
* **EVM equivalence:** Flow EVM is truly *EVM Equivalent*, not just *EVM Compatible*. It runs exactly the same as EVM mainnet, which means builders won't run into *minor* variances or endless 'quirks' when they try to integrate. If it works on Ethereum Mainnet, it will work with Flow EVM.

### Seamless integration for Ethereum developers[​](#seamless-integration-for-ethereum-developers "Direct link to Seamless integration for Ethereum developers")

Flow EVM is designed to work out-of-the-box with the Ethereum toolchain or other clients. Native EVM transactions continue to be supported when using Metamask and other EVM-compatible clients.

EVM-equivalency on Flow works behind-the-scenes by implementing a minimal transaction script in Cadence to integrate Flow features with EVM. This is made possible because EVM transactions are composed and executed within Cadence transactions, enabling novel use-cases and patterns for integration.

### Flow blockchain core features[​](#flow-blockchain-core-features "Direct link to Flow blockchain core features")

* **MEV resistance**: Flow is designed to [ensure equitable access](/build/cadence/basics/mev-resistance) by resisting MEV. Maximum Extractable Value, also know as Miner-Extractable Value (MEV), is a practice common in other blockchains in which the builder of a block can profit at your expense by manipulating where and how your transaction is included.
* **Native VRF**: Flow provides [onchain randomness](/build/cadence/advanced-concepts/randomness) at the protocol level. Instead of implementing a complex setup and [paying $10+ USD per number](https://docs.chain.link/vrf/v2-5/billing), simply call the built-in function.
* **Scalable and Secure Architecture**: The [multi-role architecture](https://flow.com/post/flow-blockchain-multi-node-architecture-advantages) of Flow allows the network to [scale without sharding](https://www.flow.com/post/flow-blockchain-multi-node-architecture-advantages) to serve billions of users without reducing the decentralization of consensus and verification.
* **True, fast finality**: For most other networks, it takes minutes, [a day](https://docs.zksync.io/zk-stack/concepts/finality#finality-on-zksync-era), or even [a week](https://docs.optimism.io/stack/rollup/overview#fault-proofs) to reach hard finality — the point at which a transaction cannot be reversed. On Flow, the median time for finality is [under 10 seconds](/build/cadence/basics/transactions#flow), without compromising security.
* **Consumer onboarding**: Flow was designed for mainstream consumers, with payment onramps catalyzing a safe and low-friction path from fiat to crypto.
* **Efficient gas costs**: The Flow blockchain is extremely efficient, allowing apps to do more computation at lower costs.

### MEV resilience[​](#mev-resilience "Direct link to MEV resilience")

The [MEV Resilient](/build/cadence/basics/mev-resistance) design on Flow offers DeFi builders improved market efficiency, fairness, trust, and long-term viability for their apps. Since Flow EVM transactions are composed and executed within a Cadence transaction, block production is handled by the [multi-role architecture](https://flow.com/post/flow-blockchain-multi-node-architecture-advantages) on Flow.

This robust MEV resilience is a significant difference from other EVM-compatible networks and results in reasonably priced and predictable gas fees. The impracticality of frontrunning or other attacks improves the user experience by eliminating failed transactions and invisible fees.

### Scalability, performance, and low gas fees[​](#scalability-performance-and-low-gas-fees "Direct link to Scalability, performance, and low gas fees")

For sustainable user adoption, apps require the network they build on to be secure, efficient, affordable, and fast. Gas fees are ultra-low cost on the network, but Flow goes a step further allowing for gasless experiences through sponsored transactions.

The state space on Flow is extensible to the petabyte scale, making it easy to store application data onchain. This means contracts can maintain a full working dataset — including metadata — together with contract logic.

Transaction throughput on the Flow network has reaches as many as 2 million daily transactions, a similar average transaction volume as Ethereum. Unlike Ethereum, Flow has always operated well under its maximum throughput ceiling, and that ceiling is scalable to even greater performance when it becomes necessary.

## Getting started[​](#getting-started "Direct link to Getting started")

Whether you're ready to dive into the advantages of building with [Cadence](https://cadence-lang.org/), or are starting with Flow [EVM](https://flow.com/upgrade/crescendo/evm.md), we've got paths to get you up and running as quickly as possible.

### Getting started with Cadence app development[​](#getting-started-with-cadence-app-development "Direct link to Getting started with Cadence app development")

The [Getting Started](/build/cadence/getting-started/contract-interaction) tutorial covers everything you need to know to build a Flow Cadence application:

* Setting up your local development environment (it's fast and easy!).
* Deploying and interacting with Flow Cadence contracts.
* Building a frontend that can interact with smart contracts written by you or other developers.

### Learn Cadence[​](#learn-cadence "Direct link to Learn Cadence")

[Cadence](https://cadence-lang.org/) is a modern smart contract programming language designed to work with Flow. Learning a new language is an investment, but you'll find that Cadence is safer, more explicit, and less dangerous than other blockchain languages. Plus, it unlocks the full power of the Flow protocol!

tip

If you're already comfortable with Solidity, be sure to check out how [Cadence](https://cadence-lang.org/) works in our [Guide for Solidity Developers](https://cadence-lang.org/docs/solidity-to-cadence)!

### Build with Solidity on Flow EVM[​](#build-with-solidity-on-flow-evm "Direct link to Build with Solidity on Flow EVM")

Not ready to take the plunge and learn [Cadence](https://cadence-lang.org/)? Try out **EVM++** by deploying existing [EVM](https://flow.com/upgrade/crescendo/evm.md) contracts to see that Flow EVM is faster and cheaper than nearly every other EVM solution without compromising on security.

Deploying on Flow EVM also gives your Solidity contracts access to many Flow Cadence features, such as native [VRF](/blockchain-development-tutorials/native-vrf/vrf-in-solidity).

## FLOW token[​](#flow-token "Direct link to FLOW token")

The [FLOW](/build/cadence/core-contracts/flow-token) (or $FLOW) token is the native currency for the Flow network. Developers and users can use FLOW to transact on the network. Developers can integrate FLOW directly into their apps for peer-to-peer payments, service charges, or consumer rewards. FLOW can be held, transferred, or transacted peer-to-peer.

* To understand more about Flow Token Economics and the FLOW token, read the [Flow Token Economics](https://www.flow.com/flow-token-economics) guide.
* FLOW tokens are the native Fungible Token on Flow. To learn more about how to work with them in your applications, review the [FLOW](/build/cadence/core-contracts/flow-token) article.

## Technical background[​](#technical-background "Direct link to Technical background")

* The [Flow Technical Primer](https://www.flow.com/primer) is a great place to start to understand how Flow works.
* The [Three technical whitepapers](https://www.flow.com/technical-paper) cover the unique innovation behind the Flow blockchain network in-depth.

## Flow Improvement Proposals (FLIPs)[​](#flow-improvement-proposals-flips "Direct link to Flow Improvement Proposals (FLIPs)")

Those wishing to understand the technical specifics of how Flow EVM works, we recommend reviewing the following improvement proposals:

* Understanding [EVM Support on Flow](https://github.com/onflow/flips/pull/225)
* Exploring the [Flow VM Bridge](https://github.com/onflow/flips/pull/233/files/d5bc46c4b13f0b9b168a94f994c77a5a689f6b24..122e938b7acae7e774246b1b66aaf5979ca21444)
* Insights into the [Flow EVM Gateway](https://github.com/onflow/flips/pull/235/files)
* Integration of the [Cadence Interface](https://github.com/onflow/flips/blob/f646491ec895442dcccdb24d80080bab1c56188e/protocol/20231116-evm-support.md)

## Build with Flow[​](#build-with-flow "Direct link to Build with Flow")

Whether you're building with Cadence or Solidity, porting an existing Solidity dApp or building from scratch, Flow offers a **fast, scalable blockchain with low fees** and the tooling you already know. As a **scalable platform for apps**, Flow combines familiar development workflows with performance and UX enhancements you can't get elsewhere.

## Join the community[​](#join-the-community "Direct link to Join the community")

Are you interested in launching a project on Flow or partnering with us? Visit our weekly Flow [office hours](https://calendar.google.com/calendar/ical/c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0%40group.calendar.google.com/public/basic.ics) for discussions on project development and other opportunities for collaboration. You can also connect with us in our developers-chat in the Flow [Discord](https://discord.gg/flow).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/flow.md)

Last updated on **Sep 3, 2025** by **Brian Doyle**

[Next

Getting Started](/build/cadence/getting-started)

###### Rate this page

😞😐😊

Copy as Markdown

* [What makes Flow unique](#what-makes-flow-unique)
  + [Dual language architecture](#dual-language-architecture)
  + [Cadence development on Flow](#cadence-development-on-flow)
  + [Solidity development on Flow EVM](#solidity-development-on-flow-evm)
  + [Seamless integration for Ethereum developers](#seamless-integration-for-ethereum-developers)
  + [Flow blockchain core features](#flow-blockchain-core-features)
  + [MEV resilience](#mev-resilience)
  + [Scalability, performance, and low gas fees](#scalability-performance-and-low-gas-fees)
* [Getting started](#getting-started)
  + [Getting started with Cadence app development](#getting-started-with-cadence-app-development)
  + [Learn Cadence](#learn-cadence)
  + [Build with Solidity on Flow EVM](#build-with-solidity-on-flow-evm)
* [FLOW token](#flow-token)
* [Technical background](#technical-background)
* [Flow Improvement Proposals (FLIPs)](#flow-improvement-proposals-flips)
* [Build with Flow](#build-with-flow)
* [Join the community](#join-the-community)

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