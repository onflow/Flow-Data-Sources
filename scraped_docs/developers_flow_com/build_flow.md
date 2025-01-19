# Source: https://developers.flow.com/build/flow




Why Flow | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Why Flow
On this page
# Why Flow

Flow was built by consumer-facing, onchain app developers to solve the problem of building consumer-facing, onchain apps. Dieter Shirley, Chief Architect of Flow and co-author of the [ERC-721 NFT standard](https://github.com/ethereum/eips/issues/721) calls it:

> **A computer that anyone can use, everyone can trust, and no one can shut down.**

Much of the protocol design is based on lessons learned from building web3 applications while working at [Dapper Labs](https://www.dapperlabs.com/), particularly [CryptoKitties](https://www.cryptokitties.co/) - the first onchain game to reach [widespread popularity](https://www.cnn.com/style/article/cryptokitty-blockchain/index.html). The game went viral, then [struggled under its own success](https://spectrum.ieee.org/cryptokitties) when it caused so much traffic that Ethereum network itself was overwhelmed by the load.

The design of Flow was guided by the need to alleviate this burden while creating the best experience possible for both developers and users. The blockchain network of the future must be able to handle millions of users while upholding the key pillars of decentralization:

1. Verifiability
2. Predictability/Reliability
3. Equitable Access for All
4. Permissionless Composability
5. Interoperability
6. Security

Flow solves the [blockchain trilemma](https://coinmarketcap.com/academy/glossary/blockchain-trilemma) and represents the next generation of blockchain technology. It's built to enable seamless consumer-scale apps without compromising decentralization or user experience and is the chosen blockchain network for [NBA Top Shot](https://nbatopshot.com/), [NFL All Day](https://nflallday.com/), [Mattel Creations](https://creations.mattel.com/pages/virtual), and [Disney Pinnacle](https://disneypinnacle.com/).

## What Makes Flow Unique[​](#what-makes-flow-unique "Direct link to What Makes Flow Unique")

Flow is a fast, decentralized, and developer-friendly blockchain designed to be the foundation for a new generation of games, apps, and the [digital assets](https://www.onflow.org/post/flow-blockchain-cadence-programming-language-resources-assets) that power them. It is based on a unique [multi-role architecture](https://www.onflow.org/primer), and designed to [scale without sharding](https://www.onflow.org/post/flow-blockchain-multi-node-architecture-advantages), allowing for massive improvements in speed and throughput while preserving a developer-friendly, ACID-compliant environment. It natively allows development of smart contracts in the powerful [Cadence](https://cadence-lang.org/) language, and also supports full [Ethereum Virtual Machine (EVM)](https://flow.com/upgrade/crescendo/evm.md) equivalence with contracts written in Solidity.

### Flow Blockchain[​](#flow-blockchain "Direct link to Flow Blockchain")

* **Multi-role architecture:** The [multi-role architecture](https://www.onflow.org/primer) of Flow allows the network to [scale without sharding](https://www.onflow.org/post/flow-blockchain-multi-node-architecture-advantages) to serve billions of users without reducing the decentralization of consensus and verification.
* **True Fast Finality**: For most other networks, it takes minutes, [a day](https://docs.zksync.io/zk-stack/concepts/finality#finality-on-zksync-era), or even [a week](https://docs.optimism.io/stack/rollup/overview#fault-proofs) to reach hard finality - the point in which a transaction cannot be reversed. On Flow, the median time for finality is [under 10 seconds](/build/basics/transactions#flow), without compromising security.
* **Native VRF**: Flow provides [onchain randomness](/build/advanced-concepts/randomness) at the protocol level. Instead of implementing a complex setup and [paying $10+ USD per number](https://docs.chain.link/vrf/v2-5/billing), simply call the built-in function.
* **Consumer Onboarding:** Flow was designed for mainstream consumers, with payment onramps catalyzing a safe and low-friction path from fiat to crypto.
* **EVM Equivalence**: The [Cadence](https://cadence-lang.org/) Virtual Machine (VM) is powerful enough to allow other VMs to run inside of it, almost like a Docker Container. The first one integrated in this way is [EVM](https://flow.com/upgrade/crescendo/evm.md) and the EVM RPC API.
* **Efficient Gas Costs**: The Flow blockchain is extremely efficient, allowing apps to do more computation at lower costs.

### Flow Cadence[​](#flow-cadence "Direct link to Flow Cadence")

* **Native Account Abstraction**: Flow has protocol-native [account abstraction](https://flow.com/account-abstraction). All accounts are smart accounts, supporting scripting, multiple keys, multi-signature transactions, and walletless onboarding with social logins.
* **Gasless Transactions**: Flow has multiple [signing roles](/build/basics/transactions#signer-roles) for each transaction. Most notably, the payer can be set independently of the authorizer. In other words, having one account sign a transaction and another pay for that transaction is a built-in feature.
* **Security:** Smart contracts on Flow are natively written in [Cadence](https://cadence-lang.org/), an easier, safer, and more secure programming language for crypto assets and apps. It's the first high-level, [resource-oriented](https://flow.com/post/resources-programming-ownership) programming language.
* **Developer Ergonomics:** The Flow network is designed to maximize developer productivity. Examples range from upgradeable smart contracts to built-in logging support to the Flow Emulator.

### Flow EVM[​](#flow-evm "Direct link to Flow EVM")

* **Speed, Cost, and Compatibility**: Flow EVM can already run all of your audited Solidity contracts at an average of less than 1 cent per transaction ([usually way less!](https://evm.flowscan.io/stats)). Unlike L2 solutions, Flow EVM reaches true finality in seconds - not in [a week](https://docs.optimism.io/stack/rollup/overview#fault-proofs). 😳
* **Bridge from Other EVM Networks**: You can [bridge](/ecosystem/bridges) hundreds of assets from dozens of chains to Flow.
* **VM Token Bridge**: Assets can be bridged between Flow Cadence and Flow EVM easily and atomically with the VM token bridge. Assets can even be bridged **and used** in a **single** transaction, allowing full composability between the EVM and Cadence environments.
* **Access to Cadence**: Access Cadence features and contracts from Flow EVM to take advantage of native [VRF](/evm/guides/vrf), higher computation for lower cost, and any asset on Cadence Flow.
* **EVM Equivalence:** Flow EVM is truly *EVM Equivalent*, not just *EVM Compatible*. It runs exactly the same as EVM mainnet, which means builders won't run into "minor" variances or endless "quirks" when they try to integrate. If it works on Ethereum Mainnet, it will work with Flow EVM.

## Learning Shortcuts[​](#learning-shortcuts "Direct link to Learning Shortcuts")

To get a complete picture on how to build on Flow, follow the 👈 sidebar top to bottom. This path will give you the most thorough onboarding experience.

If you like to jump right into the deep end of the pool, take a look below for direct links to advanced topics!

### Learn Cadence[​](#learn-cadence "Direct link to Learn Cadence")

[Cadence](https://cadence-lang.org/) is a modern smart contract programming language designed to work with Flow. Learning a new language is an investment, but you'll find that Cadence is safer, more explicit, and less dangerous than other blockchain languages. Plus, it unlocks the full power of the Flow protocol!

tip

If you're already comfortable with Solidity, be sure to check out how [Cadence](https://cadence-lang.org/) works in our [Guide for Solidity Developers](https://cadence-lang.org/docs/solidity-to-cadence)!

### Build with the EVM[​](#build-with-the-evm "Direct link to Build with the EVM")

Not ready to take the plunge and learn [Cadence](https://cadence-lang.org/)? Try out "EVM++" by deploying existing [EVM](https://flow.com/upgrade/crescendo/evm.md) contracts to see that Flow EVM is faster and cheaper than nearly every other EVM solution without compromising on security.

Deploying on Flow EVM also gives your Solidity contracts access to many Flow Cadence features, such as native [VRF](/evm/guides/vrf).

### Getting Started with App Development[​](#getting-started-with-app-development "Direct link to Getting Started with App Development")

The [Getting Started](/build/getting-started/contract-interaction) tutorial covers everything you need to know to build a Flow Cadence application:

* Setting up your local development environment (it's fast and easy!)
* Deploying and interacting with Flow Cadence contracts
* Building a frontend that can interact with smart contracts written by you, or other developers

### Core Contracts[​](#core-contracts "Direct link to Core Contracts")

The Flow blockchain implements core functionality using its own smart contract language, [Cadence](https://cadence-lang.org/). The core functionality is split into a set of contracts, called the [core contracts](/build/core-contracts):

* **Fungible Token:** The FungibleToken contract implements the Fungible Token Standard. It is the second contract ever deployed on Flow.
* **Flow Token:** The FlowToken contract defines the FLOW network token.
* **Flow Fees:** The FlowFees contract is where all the collected Flow fees are gathered.
* **Service Account:** The FlowServiceAccount contract tracks transaction fees and deployment permissions and provides convenient methods for Flow Token operations.
* **Staking Table:** The FlowIDTableStaking contract is the central table that manages staked nodes, delegation, and rewards.
* **Epoch Contract:** The FlowEpoch contract is the state machine that manages Epoch phases and emits service events.

### FLOW Token[​](#flow-token "Direct link to FLOW Token")

The [FLOW](/build/core-contracts/flow-token) (or $FLOW) token is the native currency for the Flow network. Developers and users can use FLOW to transact on the network. Developers can integrate FLOW directly into their apps for peer-to-peer payments, service charges, or consumer rewards. FLOW can be held, transferred, or transacted peer-to-peer.

* To understand more about Flow Token Economics and the FLOW token, read the [Flow Token Economics](https://www.onflow.org/flow-token-economics) guide.
* FLOW tokens are the native Fungible Token on Flow. To learn more about how to work with them in your applications, review the [FLOW](/build/core-contracts/flow-token) article.

### Technical Background[​](#technical-background "Direct link to Technical Background")

* The [Flow Technical Primer](https://www.onflow.org/primer) is a great place to start to understand how Flow works.
* The [Three technical whitepapers](https://www.onflow.org/technical-paper) cover the unique innovation behind the Flow blockchain network in-depth.
[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/flow.md)Last updated on **Dec 24, 2024** by **Navid TehraniFar**[NextDifferences vs. EVM](/build/differences-vs-evm)
###### Rate this page

😞😐😊

* [What Makes Flow Unique](#what-makes-flow-unique)
  + [Flow Blockchain](#flow-blockchain)
  + [Flow Cadence](#flow-cadence)
  + [Flow EVM](#flow-evm)
* [Learning Shortcuts](#learning-shortcuts)
  + [Learn Cadence](#learn-cadence)
  + [Build with the EVM](#build-with-the-evm)
  + [Getting Started with App Development](#getting-started-with-app-development)
  + [Core Contracts](#core-contracts)
  + [FLOW Token](#flow-token)
  + [Technical Background](#technical-background)
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

