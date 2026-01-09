# Source: https://developers.flow.com/build/flow

Why Flow - The Consumer DeFi Layer-One Network | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Why Flow

On this page

# Why Flow: The Consumer DeFi Layer-One Network

Flow is powering the future of Consumer DeFi. Flow is the home of Consumer DeFi.

Flow is a purpose-built L1 blockchain designed for large-scale consumer finance applications. It is the leading consumer layer-one network, boasting over 1 million monthly active users across ecosystem applications built in collaboration with top global brands like NBA, Disney, PayPal, NFL, and Ticketmaster.

## The Consumer DeFi Movement[​](#the-consumer-defi-movement "Direct link to The Consumer DeFi Movement")

Today's fintech is a digital facade on analog rails, subject to the same outdated limitations of your brick-and-mortar bank. These platforms gave us the appearance of digital money without the benefits of digital-native assets. Your accounts there are mere pointers to the underlying legacy system. But that is about to change with the Consumer DeFi movement: turning decentralized finance into personal finance.

The new chapter for Flow in leading Consumer DeFi is not a sudden shift, but rather the culmination of many years of focused dedication in providing the best consumer experience. Within the past 12 months, Flow network achieved remarkable feats: nearly 10x throughput increase for consumer-scale ambitions, 600% year-over-year increase in total value locked (TVL) to over $100M, and the pivotal Forte upgrade that drastically reduced the development time for consumer finance applications from months to mere days.

The next generation of consumer finance is not just facilitated by the internet; assets themselves are of the internet. Fintech apps serve as opinionated frontends to a new financial layer that is:

* **Global**: Accessible everywhere, by everyone.
* **Always-On**: Operating 24/7/365, unbound by business hours.
* **Real-Time**: Settling transactions in seconds, not days.
* **Open**: Programmable and composable across apps.

The foundation for the future of consumer finance is already being laid. After years of development, DeFi technology is ready to transition from a niche market to the mainstream. However, a significant hurdle remains: current DeFi platforms are designed for crypto-savvy users, demanding steep learning curves and willingness to take on unlimited risk. We must move beyond this crypto native phase to the new consumer DeFi era with better-than-fintech user experiences, safer and sustainable yields, and most importantly delivering a tangible impact on users' daily lives.

**What is Consumer DeFi?** Consumer DeFi is any app or experience that provides the benefits powered by DeFi rails to audiences with zero crypto knowledge. Apps powered by Flow win consumer mindshare because they offer features and benefits that are extremely hard to replicate with just web2 rails while ensuring users do not require crypto-specific knowledge to understand and use them.

Flow has demonstrated its capability to attract global brands and institutions, offering an innovative and safe platform for their millions of users. With the DeFi sector now ready to transition from a niche market to the mainstream, Flow is uniquely positioned to lead the Consumer DeFi charge.

Dieter Shirley, Chief Architect of Flow and co-author of the [ERC-721 NFT standard](https://github.com/ethereum/eips/issues/721), calls Flow:

> ***A computer that anyone can use, everyone can trust, and no one can shut down***

## Flow: Automated DeFi and Consumer Applications[​](#flow-automated-defi-and-consumer-applications "Direct link to Flow: Automated DeFi and Consumer Applications")

Flow is a high-performance layer-one blockchain designed for automated DeFi and large-scale consumer applications. Its multi-role architecture isolates heavy computation to Execution Nodes while keeping validation lightweight, so developers gain incredible performance and users benefit from low-cost transactions, even at scale.

The Forte upgrade expands the core protocol with Flow Actions for atomic multi-step DeFi operations and Scheduled Transactions for fully onchain automation. Developers can compose swaps, staking, or yield workflows that self-execute without off-chain keepers, scripts, or relayers required.

Flow delivers a unified environment for automation-heavy, composable applications that demand reliability and precision at scale. It's where DeFi, fintech, and consumer-grade performance converge in a single L1.

## Forte Network Upgrade: Autonomous DeFi Execution[​](#forte-network-upgrade-autonomous-defi-execution "Direct link to Forte Network Upgrade: Autonomous DeFi Execution")

The Forte network upgrade marks a turning point for builders creating DeFi systems on Flow. Until now, blockchains have largely been reactive, responding only when a user or off-chain keeper sends a transaction. Forte changes that model by giving developers a native framework for composable, autonomous execution.

> ***ERC-20 and ERC-721 unlocked nouns. Actions and scheduled transactions unlock verbs.***

Forte transforms Flow from a reactive blockchain into an autonomous, intelligent network capable of executing complex workflows without external dependencies. The upgrade introduces native time scheduling, protocol-level composability, and AI-optimized development tools that enable entirely new categories of applications.

Together, these systems turn Flow into a self-governing financial runtime that is precise with 128-bit fixed-point math for lossless calculations, secure through resource-based execution, and fully composable across protocols. In this environment, DeFi logic can schedule itself, chain together across protocols, and operate autonomously—a blockchain that finally does more than react.

### Flow Actions: Protocol-native composability[​](#flow-actions-protocol-native-composability "Direct link to Flow Actions: Protocol-native composability")

[**Flow Actions**](/blockchain-development-tutorials/forte/flow-actions) are protocol-native, composable operations that enable developers to create multi-step workflows across protocols in a single atomic transaction. With Flow Actions, builders can link together standardized DeFi primitives such as sources, sinks, swappers, price oracles, and flashers into atomic, protocol-agnostic workflows.

A single transaction can claim rewards, swap assets, add liquidity, and restake LP tokens without any off-chain orchestration. These building blocks eliminate custom integrations and ensure every operation either fully succeeds or safely reverts, unlocking complex strategies like automated yield farming, arbitrage, and rebalancing through simple, auditable Cadence code.

This means developers can:

* **Compose complex operations**: Build sophisticated DeFi strategies by combining multiple Actions in one transaction
* **Eliminate integration complexity**: Use standardized interfaces instead of custom contract integrations
* **Ensure atomicity**: All operations succeed together or fail together, eliminating partial execution risks
* **Reduce gas costs**: Execute multiple protocol interactions more efficiently than separate transactions

### Scheduled Transactions: Autonomous onchain execution[​](#scheduled-transactions-autonomous-onchain-execution "Direct link to Scheduled Transactions: Autonomous onchain execution")

[**Scheduled Transactions**](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction) introduce the first truly onchain time scheduler. Developers can schedule or trigger transactions directly within Flow accounts, enabling recurring actions, deferred settlements, and autonomous portfolio management without external cron jobs or trusted servers.

Scheduled Transactions are onchain resources that run entirely within a Flow account, enabling fully autonomous, secure transaction execution. They can self-trigger based on conditions and operate without external keepers.

Key capabilities:

* **Autonomous operation**: Execute transactions automatically based on programmed logic
* **Self-contained**: Run entirely onchain without external dependencies
* **Trigger-based**: React to onchain events, time schedules, or custom conditions

Combined, Actions and Scheduling allow DeFi protocols to become self-maintaining: positions can compound automatically, vaults can adjust exposure based on time or events, and protocols can enforce predictable behavior entirely onchain.

Scheduled Transactions are the first native time scheduler that lets onchain apps run tasks automatically, like cron jobs for blockchains. Applications are no longer restricted to being reactive only to user transactions. They can be used for:

* **DeFi protocols** that automatically rebalance portfolios on schedule
* **AI-driven agents** that proactively settle, sweep, or optimize positions
* **Subscription services** with automatic recurring payments
* **Gaming mechanics** with time-based events and rewards

Scheduled Transactions run natively on the network, simplifying operations, reducing off-chain dependencies, and making behavior auditable and predictable in code. This implements [FLIP 330: Scheduled Transaction](https://github.com/onflow/flips/blob/main/protocol/20250609-scheduled-callbacks.md).

### High-precision DeFi with 128-bit fixed-point types[​](#high-precision-defi-with-128-bit-fixed-point-types "Direct link to High-precision DeFi with 128-bit fixed-point types")

Cadence now supports **Fix128** and **UFix128** - 128-bit fixed-point types enabling precision up to **24 decimal places** for advanced DeFi, risk engines, and interest accrual workloads.

The native precision in Forte with built-in 128-bit fixed-point support eliminates the need for bespoke arithmetic scaffolding while minimizing rounding-related errors common in integer-based math. This ensures lossless conversion where all existing Fix64 and UFix64 values convert seamlessly, providing financial-grade accuracy that supports sophisticated financial calculations requiring extreme precision.

This implements [FLIP 341: Add 128-bit Fixed-point Types to Cadence](https://github.com/onflow/flips/blob/main/cadence/20250815-128-bit-fixed-point-types.md).

### WebAuthn and passkey support[​](#webauthn-and-passkey-support "Direct link to WebAuthn and passkey support")

Forte adds **native WebAuthn support** including passkeys, enabling wallets to use device-backed credentials on iOS, Android, and popular password managers to sign transactions.

Native WebAuthn support on Flow eliminates seed phrases by enabling biometric authentication while preserving self-custody, with cross-device portability that securely syncs credentials across devices. The native integration requires no additional smart contract layers like ERC-4337, providing a seamless UX where users can sign transactions with Touch ID, Face ID, or hardware keys.

Combined with native account abstraction on Flow, developers can build [smart wallets without relying on complex contract architectures](https://flow.com/post/transforming-smartphones-into-hardware-wallets-how-secure-enclave-support-on-flow-is-ushering-in-the-next-wave-of-web3-applications). This implements [FLIP 264: WebAuthn Credential Support](https://github.com/onflow/flips/blob/cfaaf5f6b7c752e8db770e61ec9c180dc0eb6543/protocol/20250203-webauthn-credential-support.md).

### AI-friendly Cadence errors[​](#ai-friendly-cadence-errors "Direct link to AI-friendly Cadence errors")

Cadence compiler and linter errors are now **designed for AI assistance**, making it easier for agents and IDE copilots to fix issues automatically. Error messages:

* **Explain the cause** with context-aware descriptions
* **Suggest concrete fixes** with actionable recommendations
* **Link directly** to reference docs and migration notes
* **Surface through language server** for AI-powered editors like Cursor

This enables faster feedback, fewer documentation round trips, and smoother AI agent workflows for code refactoring and migration.

### Boosting Efficiency and Scalability[​](#boosting-efficiency-and-scalability "Direct link to Boosting Efficiency and Scalability")

#### Enhanced node performance with PebbleDB[​](#enhanced-node-performance-with-pebbledb "Direct link to Enhanced node performance with PebbleDB")

Forte upgrades node storage from BadgerDB to **PebbleDB**, delivering up to 80% memory usage reduction depending on node type and up to 60% CPU usage improvement for typical operations. The upgrade provides up to 30% annual disk usage reduction through effective pruning, higher stability under load by eliminating memory spikes, and improved ROI for operators through better resource efficiency.

#### Optimized state storage with account key de-duplication[​](#optimized-state-storage-with-account-key-de-duplication "Direct link to Optimized state storage with account key de-duplication")

Public key de-duplication eliminates redundancy while preserving multi-key account flexibility, consolidating 53% of all keys that were duplicates. This optimization delivers a 6% reduction in the Flow execution state (saving 21 GB from 349 GB), removes 0.29 billion entries from the storage trie, and provides a 6-18% reduction in Execution Node memory usage, resulting in faster state access through leaner data structures.

#### Adaptive collection rate limiting for overload resilience[​](#adaptive-collection-rate-limiting-for-overload-resilience "Direct link to Adaptive collection rate limiting for overload resilience")

The [assembly line architecture](https://flow.com/multi-node) on Flow gains intelligent rate limiting to prevent pipeline bottlenecks through automatic throttling when execution or sealing lags behind collection. The system maintains steady pipeline flow even at several hundred TPS while providing priority handling for governance and protocol transactions, creating a self-regulating system that disengages once the backlog clears.

#### Near real-time transaction results[​](#near-real-time-transaction-results "Direct link to Near real-time transaction results")

Building on the [data availability vision](https://flow.com/protocol-autonomy-roadmap) for Flow, Access Nodes ingest account data and transaction results **before finalization**, enabling soft finality access for high-frequency DeFi applications with early state reads that include graceful rollback handling. This approach provides reduced latency for real-time applications and direct data serving without third-party dependencies.

### Protocol Autonomy[​](#protocol-autonomy "Direct link to Protocol Autonomy")

#### Hardened data integrity across the network[​](#hardened-data-integrity-across-the-network "Direct link to Hardened data integrity across the network")

A major milestone on the [protocol autonomy roadmap](https://flow.com/protocol-autonomy-roadmap) ensures every data structure has a **canonical, verifiable identity** through collision-resistant hashing for all inter-node communications and immediate tampering detection by message recipients. The system provides protected data structures with custom linter validation and immutable message semantics for simplified development.

This provides developers and AI agents with a simpler mental model where network messages are treated as immutable objects with stable identities.

## What makes Flow unique[​](#what-makes-flow-unique "Direct link to What makes Flow unique")

Flow is a fast, decentralized, and developer-friendly blockchain designed to be the foundation for a new generation of games, apps, and the [digital assets](https://www.flow.com/post/flow-blockchain-cadence-programming-language-resources-assets) that power them. It is based on a unique [multi-role architecture](https://flow.com/post/flow-blockchain-multi-node-architecture-advantages) and designed to [scale without sharding](https://www.flow.com/post/flow-blockchain-multi-node-architecture-advantages), allowing for massive improvements in speed and throughput while preserving a developer-friendly, ACID-compliant environment.

Much of the protocol design is based on lessons learned from building Web3 applications while working at [Dapper Labs](https://www.dapperlabs.com/), particularly [CryptoKitties](https://www.cryptokitties.co/) — the first onchain game to reach [widespread popularity](https://www.cnn.com/style/article/cryptokitty-blockchain/index.html). The game went viral, then [struggled under its own success](https://spectrum.ieee.org/cryptokitties) when it caused so much traffic that the Ethereum network itself was overwhelmed by the load.

The design of Flow was guided by the need to alleviate this burden while creating the best experience possible for both developers and users. Flow Foundation (the core team) and Dapper Labs (the leading ecosystem builder) work together as two integral parts of a unified effort, combining their strengths to position Flow as the leader in Consumer DeFi. This synergy brings together deep protocol and infrastructure expertise hardened by over 10 years of production experience with the highest security standards, alongside deep consumer audience expertise honed by operating multiple production apps that generated over $1 billion in revenue combined.

The blockchain network of the future must be able to handle millions of users while upholding the key pillars of decentralization:

1. Verifiability
2. Predictability/Reliability
3. Equitable Access for All
4. Permissionless Composability
5. Interoperability
6. Security

Flow solves the [blockchain trilemma](https://coinmarketcap.com/academy/glossary/blockchain-trilemma) and represents the next generation of blockchain technology. It's built to enable seamless consumer-scale apps without compromising decentralization or user experience, and is the chosen blockchain network for [NBA Top Shot](https://nbatopshot.com/), [NFL All Day](https://nflallday.com/), [Mattel Creations](https://creations.mattel.com/pages/virtual), and [Disney Pinnacle](https://disneypinnacle.com/).

### Dual language architecture[​](#dual-language-architecture "Direct link to Dual language architecture")

Flow is unique in supporting two powerful programming languages for smart contract development:

* **Cadence**: A modern programming language developed by smart contract application builders.
* **Solidity**: The industry-standard language for EVM development, fully supported on Flow with full EVM equivalence.

EVM and Cadence environments both use FLOW as gas for transactions and are connected by a native bridge that allows seamless and cheap communication between them. Fungible and non-fungible tokens can also be seamlessly transferred between environments using the native VM token bridge, taking place instantly in a single atomic transaction.

This means developers can choose the language that best fits their needs while maintaining full interoperability between both environments.

### Cadence development on Flow[​](#cadence-development-on-flow "Direct link to Cadence development on Flow")

Flow supports two smart contract languages:

[Cadence](https://cadence-lang.org/) provides native resource safety, 128-bit fixed-point arithmetic for financial precision, built-in WebAuthn authentication for secure, seedless user onboarding, and vastly increased contract size, storage, and computation limits. It also grants native data availability, and Cadence transactions are written in the language itself, which allows for multiple calls to multiple functions on multiple smart contracts all with a single user signature.

Key Cadence features:

* **Advanced Transactions**: [Transactions](https://cadence-lang.org/docs/language/transactions) in Cadence smart contracts are not simply calls to existing functions on already deploy contracts. Instead, transactions are code written in Cadence that can **call any function (with appropriate access) on any smart contract by any author**, all in a single, atomic transaction with a single user signature.
* **AI Ready**: Cadence transactions have [pre- and post-conditions](https://cadence-lang.org/docs/language/pre-and-post-conditions) that clearly define the inputs to a transactions, such as the tokens that may be withdrawn, and outcomes, such as collectibles that must be purchased. With these definitions, Cadence transactions of immense complexity can be written safely. Regardless of code in the actual execution, the user can be sure that they get what they expected and only pay the price they authorized.
* **Data Availability**: Similarly, any author can construct a **view** function to access any public data on any smart contract without needing the author of that smart contract to have anticipated the need to view that data or reliance a provider to cache it and make it available.
* **Native account abstraction**: Cadence transactions have protocol-native [account abstraction](https://flow.com/account-abstraction). All accounts are smart accounts, supporting scripting, multiple keys, multi-signature transactions, and walletless onboarding with social logins.
* **Gasless transactions**: Cadence transactions have multiple [signing roles](/build/cadence/basics/transactions#signer-roles) for each transaction. Most notably, the payer can be set independently of the authorizer. In other words, having one account sign a transaction and another pay for that transaction is a built-in feature.
* **Security**: Smart contracts on Flow are natively written in Cadence, an easier, safer, and more secure programming language for crypto assets and apps. It's the first high-level, [resource-oriented](https://flow.com/post/resources-programming-ownership) programming language.
* **Developer ergonomics**: The Flow network is designed to maximize developer productivity. Examples range from upgradeable smart contracts to built-in logging support to the Flow Emulator.

### Solidity development on Flow EVM[​](#solidity-development-on-flow-evm "Direct link to Solidity development on Flow EVM")

[Solidity](https://soliditylang.org/) allows developers to deploy existing contracts on a fast and efficient, fully EVM-equivalent network while benefitting from access to native VRF, batched transactions, and all the benefits of the Flow protocol. A native bridge allows seamless transfers of assets between these two networks.

Flow EVM provides the best EVM experience available anywhere:

* **Speed, cost, and compatibility**: Flow EVM can already run all of your audited Solidity contracts at an average of less than 1 cent per transaction ([usually way less!](https://evm.flowscan.io/stats)). Unlike L2 solutions, Flow EVM reaches true finality in seconds — not in [a week](https://docs.optimism.io/stack/rollup/overview#fault-proofs).
* **Bridge from Other EVM networks**: You can [bridge](/ecosystem/bridges) hundreds of assets from dozens of chains to Flow.
* **VM token bridge**: Assets can be bridged between Flow Cadence and Flow EVM easily and atomically with the VM token bridge. Assets can even be bridged **and used** in a **single** transaction, allowing full composability between the EVM and Cadence environments.
* **Access to Cadence features**: Access Cadence features and contracts from Flow EVM to take advantage of native [VRF](/blockchain-development-tutorials/native-vrf/vrf-in-solidity), higher computation for lower cost, and any asset on Cadence Flow. You can also build [cross-vm apps](/blockchain-development-tutorials/cross-vm-apps) on top of the *wagmi/viem/RainbowKit* stack, enabling batched transactions and more.
* **EVM equivalence:** Flow EVM is truly *EVM Equivalent*, not just *EVM Compatible*. It runs exactly the same as EVM mainnet, which means builders do not run into *minor* variances or endless 'quirks' when they try to integrate. If it works on Ethereum Mainnet, it works with Flow EVM.

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

### Flow track record in Consumer DeFi[​](#flow-track-record-in-consumer-defi "Direct link to Flow track record in Consumer DeFi")

Flow leadership in Consumer DeFi is built on a foundation of proven expertise and real-world validation:

**Consumer expertise:**

* The leading consumer chain that onboarded millions of net new users onchain and still boasts over 1 million monthly active users
* Deep consumer audience expertise honed by operating multiple production apps that generated over $1 billion in revenue combined
* Vast network of global consumer brands and platforms like NBA, Disney, PayPal, Ticketmaster

**DeFi and fintech expertise:**

* Deep protocol and infrastructure expertise hardened by over 10 years of production experience with the highest security standards (since CryptoKitties days)
* Built the first smart contract wallet (Dapper Wallet plugin) on Ethereum back in 2018, ahead of the account abstraction movement
* Managed the end-to-end infrastructure for on/off-ramp, KYC, and risk monitoring platform that handles hundreds of millions of dollars in volume (Dapper Wallet)
* Flow ALP provides the best risk-adjusted yield opportunities in DeFi for consumers and institutional capital
* The best infrastructure layer that offers the fastest time to market for consumer DeFi apps

Flow is where consumers deposit their funds and access the best risk-adjusted yields, making it the ideal platform for Consumer DeFi applications that prioritize safety and sustainable returns.

### Scalability, performance, and low gas fees[​](#scalability-performance-and-low-gas-fees "Direct link to Scalability, performance, and low gas fees")

For sustainable user adoption, apps require the network they build on to be secure, efficient, affordable, and fast. Gas fees are ultra-low cost on the network, but Flow goes a step further allowing for gasless experiences through sponsored transactions.

The state space on Flow is extensible to the petabyte scale, making it easy to store application data onchain. This means contracts can maintain a full working dataset — including metadata — together with contract logic.

Transaction throughput on the Flow network has reached as many as 2 million daily transactions, a similar average transaction volume as Ethereum. Unlike Ethereum, Flow has always operated well under its maximum throughput ceiling, and that ceiling is scalable to even greater performance when it becomes necessary.

## Getting started[​](#getting-started "Direct link to Getting started")

Whether you're ready to dive into the advantages of building with [Cadence](https://cadence-lang.org/), or are starting with Flow [EVM](https://flow.com/upgrade/crescendo/evm.md), we've got paths to get you up and running as quickly as possible.

### Getting started with Cadence app development[​](#getting-started-with-cadence-app-development "Direct link to Getting started with Cadence app development")

The [Getting Started](/blockchain-development-tutorials/cadence/getting-started) tutorial covers everything you need to know to build a Flow Cadence application:

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

Whether you're building with Cadence or Solidity, porting an existing Solidity dApp or building from scratch, Flow offers a **fast, scalable blockchain with low fees** and the tooling you already know. As a **purpose-built L1 for consumer finance applications**, Flow combines familiar development workflows with performance and UX enhancements you can't get elsewhere. Build the next generation of Consumer DeFi applications that deliver better-than-fintech user experiences, safer and sustainable yields, and tangible impact on users' daily lives.

## Join the community[​](#join-the-community "Direct link to Join the community")

Are you interested in launching a project on Flow or partnering with us? Visit our weekly Flow [office hours](https://calendar.google.com/calendar/ical/c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0%40group.calendar.google.com/public/basic.ics) for discussions on project development and other opportunities for collaboration. You can also connect with us in our developers-chat in the Flow [Discord](https://discord.gg/flow).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/flow.md)

Last updated on **Dec 1, 2025** by **Brian Doyle**

[Next

Quickstart ↙](/build/cadence/quickstart)

###### Rate this page

😞😐😊

Copy as Markdown

* [The Consumer DeFi Movement](#the-consumer-defi-movement)* [Flow: Automated DeFi and Consumer Applications](#flow-automated-defi-and-consumer-applications)* [Forte Network Upgrade: Autonomous DeFi Execution](#forte-network-upgrade-autonomous-defi-execution)
      + [Flow Actions: Protocol-native composability](#flow-actions-protocol-native-composability)+ [Scheduled Transactions: Autonomous onchain execution](#scheduled-transactions-autonomous-onchain-execution)+ [High-precision DeFi with 128-bit fixed-point types](#high-precision-defi-with-128-bit-fixed-point-types)+ [WebAuthn and passkey support](#webauthn-and-passkey-support)+ [AI-friendly Cadence errors](#ai-friendly-cadence-errors)+ [Boosting Efficiency and Scalability](#boosting-efficiency-and-scalability)+ [Protocol Autonomy](#protocol-autonomy)* [What makes Flow unique](#what-makes-flow-unique)
        + [Dual language architecture](#dual-language-architecture)+ [Cadence development on Flow](#cadence-development-on-flow)+ [Solidity development on Flow EVM](#solidity-development-on-flow-evm)+ [Seamless integration for Ethereum developers](#seamless-integration-for-ethereum-developers)+ [Flow blockchain core features](#flow-blockchain-core-features)+ [MEV resilience](#mev-resilience)+ [Flow track record in Consumer DeFi](#flow-track-record-in-consumer-defi)+ [Scalability, performance, and low gas fees](#scalability-performance-and-low-gas-fees)* [Getting started](#getting-started)
          + [Getting started with Cadence app development](#getting-started-with-cadence-app-development)+ [Learn Cadence](#learn-cadence)+ [Build with Solidity on Flow EVM](#build-with-solidity-on-flow-evm)* [FLOW token](#flow-token)* [Technical background](#technical-background)* [Flow Improvement Proposals (FLIPs)](#flow-improvement-proposals-flips)* [Build with Flow](#build-with-flow)* [Join the community](#join-the-community)

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