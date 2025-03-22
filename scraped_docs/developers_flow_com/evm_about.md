# Source: https://developers.flow.com/evm/about

Why EVM on Flow | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Networks](/evm/networks)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Data Indexers](/evm/data-indexers)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)
* [Clients](/evm/clients/ethers)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)

* Why EVM on Flow

On this page

# Why EVM on Flow

Flow is an L1 that now supports EVM-equivalency. This means that all of Flow's protocol benefits, such as fast transactions, low costs, and mainstream scalability, are natively available without any additional code changes to solidity contracts. With EVM, solidity devs and builders can now easily tap into Flow's user base and unique IPs without any implementation risk.

## Seamless Integration for Ethereum Developers[​](#seamless-integration-for-ethereum-developers "Direct link to Seamless Integration for Ethereum Developers")

Flow EVM is designed to work out-of-the-box with the Ethereum toolchain or other clients. Native EVM transactions also continue to be supported when using Metamask and other EVM-compatible clients.
EVM-equivalency on Flow works behind-the-scenes by implementing a minimal transaction script in Cadence, Flow's smart contract language, to integrate Flow features with EVM. This is made possible because EVM transactions are composed and executed within Cadence transactions, enabling novel use-cases and patterns for integration.

## Best-In-Class UX[​](#best-in-class-ux "Direct link to Best-In-Class UX")

Flow allows for the creation of app on-boarding experiences that meet every type of user exactly where they are at, from web3 beginners to ecosystem veterans. This is possible through Account Linking, which utilizes the account abstraction model on Flow and enables users to immediately use an app without wallet authentication. On-chain accounts can be created as needed by the application which custodies their use for an anonymous user. At some later point these users may choose to link the custodied account to their self-custodial wallet taking full ownership of the account. EVM apps on Flow can also leverage Account Linking to handle creation of accounts and achieve a similarly smooth onboarding user experience.

With Flow, builders can choose to expand EVM capabilities and transcend limitations using Cadence, which offers a powerful new account model, programmable resources, and hybrid ownership.

## Instant Cross-VM Token Transfers[​](#instant-cross-vm-token-transfers "Direct link to Instant Cross-VM Token Transfers")

EVM and Cadence environments both use FLOW as gas for transactions, sharing a singular token supply across both environments. Fungible and non-fungible tokens can also be seamlessly transferred between environments using the native VM token bridge, taking place instantly in a single atomic transaction.

## Scalability, Performance and Low Gas Fees[​](#scalability-performance-and-low-gas-fees "Direct link to Scalability, Performance and Low Gas Fees")

For sustainable user adoption, apps require the network they build on to be secure, efficient, affordable and fast. Gas fees are ultra-low cost on the network, but Flow goes a step further allowing for gasless experiences through sponsored transactions. Scalable performance is ensured with an innovative multi-node distributed consensus, flexible transaction model and horizontally scaled transaction linearization which solves proposer-builder separation, separation of compute, and settlement – all without sharding.

Flow’s state space is extensible to the petabyte scale making it easy to store application data on-chain. This means contracts can maintain a full working dataset - including metadata - together with contract logic.

Flow's transaction throughput peaked to 2M daily transactions during 2023 sustaining a similar average transaction volume as Ethereum. Unlike Ethereum, Flow has always operated well under its maximum throughput ceiling which is presently scalable to 5x more transactions with further performance optimizations to come when parallel execution is released. State scalability on Flow sets the foundations for further significant throughput optimization.

## MEV Resilience[​](#mev-resilience "Direct link to MEV Resilience")

The MEV Resilient design on Flow offers DeFi builders improved market efficiency, fairness, trust and long-term viability for their apps. Since Flow EVM transactions are composed and executed within a Cadence transaction, block production is handled by Flow’s [multi-role architecture](https://flow.com/post/flow-blockchain-multi-node-architecture-advantages). This heterogeneity between node roles ensures that visibility into block proposal, assembly, asserting block validity and other correctness checks during the block production cycle exposes limited information to each node type on a need to know basis, observing the Principle of Least Privilege. These differences in node and consensus design results in strong economic disincentives for collusion because no individual node has full visibility into the state of block production for the chain. This robust MEV resilience is a significant difference from other EVM-compatible networks and results in reasonably priced, predictable gas fees. The impracticality of frontrunning or other attacks improves the user experience by eliminating failed transactions and invisible fees.

## Join the Community[​](#join-the-community "Direct link to Join the Community")

Are you interested in launching an EVM project on Flow or partnering with us? Visit our weekly Flow [office hours](https://calendar.google.com/calendar/ical/c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0%40group.calendar.google.com/public/basic.ics) for discussions on project development and other opportunities for collaboration. You can also chat with us developers-chat in the Flow [Discord](https://discord.gg/flow).

## Further Reading and Discussions[​](#further-reading-and-discussions "Direct link to Further Reading and Discussions")

* [Why EVM on Flow: Beyond Solidity](https://forum.flow.com/t/evm-on-flow-beyond-solidity/5260)
* [Path to EVM Equivalence on Flow](https://forum.flow.com/t/evm-equivalence-on-flow-proposal-and-path-forward/5478)

## Flow Improvement Proposals (FLIPs)[​](#flow-improvement-proposals-flips "Direct link to Flow Improvement Proposals (FLIPs)")

Those wishing to understand the technical specifics of how Flow EVM works we recommend reviewing the following improvement proposals.

* Understanding [EVM Support on Flow](https://github.com/onflow/flips/pull/225)
* Exploring the [Flow VM Bridge](https://github.com/onflow/flips/pull/233/files/d5bc46c4b13f0b9b168a94f994c77a5a689f6b24..122e938b7acae7e774246b1b66aaf5979ca21444)
* Insights into the [Flow EVM Gateway](https://github.com/onflow/flips/pull/235/files)
* Integration of the [Cadence Interface](https://github.com/onflow/flips/blob/f646491ec895442dcccdb24d80080bab1c56188e/protocol/20231116-evm-support.md)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/about.md)

Last updated on **Mar 6, 2025** by **Giovanni Sanchez**

[Next

How it Works](/evm/how-it-works)

###### Rate this page

😞😐😊

* [Seamless Integration for Ethereum Developers](#seamless-integration-for-ethereum-developers)
* [Best-In-Class UX](#best-in-class-ux)
* [Instant Cross-VM Token Transfers](#instant-cross-vm-token-transfers)
* [Scalability, Performance and Low Gas Fees](#scalability-performance-and-low-gas-fees)
* [MEV Resilience](#mev-resilience)
* [Join the Community](#join-the-community)
* [Further Reading and Discussions](#further-reading-and-discussions)
* [Flow Improvement Proposals (FLIPs)](#flow-improvement-proposals-flips)

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