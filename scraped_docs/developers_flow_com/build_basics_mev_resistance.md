# Source: https://developers.flow.com/build/basics/mev-resistance

MEV Resistance | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)

  + [Network Architecture ↗️](/build/basics/network-architecture)
  + [Blocks](/build/basics/blocks)
  + [Collections](/build/basics/collections)
  + [Accounts](/build/basics/accounts)
  + [Transactions](/build/basics/transactions)
  + [Scripts](/build/basics/scripts)
  + [Fees](/build/basics/fees)
  + [MEV Resistance](/build/basics/mev-resistance)
  + [Events](/build/basics/events)
  + [FLOW Coin](/build/basics/flow-token)
  + [Smart Contracts ↙](/build/basics/smart-contracts)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Flow Protocol
* MEV Resistance

On this page

# How Flow Suppresses MEV to Ensure Equitable Access

## The Hidden Cost of MEV in Decentralized Systems[​](#the-hidden-cost-of-mev-in-decentralized-systems "Direct link to The Hidden Cost of MEV in Decentralized Systems")

One of the most under-discussed benefits of decentralization is **equitable access**. Ideally, the value and quality-of-service you receive from a decentralized platform should not depend on your identity, computing power, or personal connections. However, **Maximal Extractable Value (MEV)** poses a significant threat to this principle.

MEV allows block producers to manipulate transaction ordering for profit—often at the direct expense of users. The ability to front-run, back-run, or sandwich transactions can extract value from ordinary users, reinforcing inequalities rather than eliminating them. In most blockchain networks, MEV is not just an unfortunate side effect; it is structurally embedded in how transactions are processed.

## Why MEV Persists on Most Blockchains[​](#why-mev-persists-on-most-blockchains "Direct link to Why MEV Persists on Most Blockchains")

MEV is difficult to prevent on most blockchains because **each block has a single builder**. This builder must have:

* A full copy of the blockchain state
* The ability to simulate transactions before they are finalized
* Absolute control over transaction selection and ordering

In practice, this means that **the entity responsible for adding your transaction to the blockchain can first simulate it to identify profit opportunities**. They can test hundreds or thousands of ways to rearrange transactions, inserting their own to extract MEV—often at **your** expense.

For example, if a block builder can earn $10 by sandwiching your transaction, it means **you** likely lose $10 in value. This is functionally theft, and the worst part? If your transaction is airtight and offers no MEV opportunities, the block builder has no obligation to include it at all. Pay the toll, or get locked out.

## How Flow Accomplishes MEV Resilience[​](#how-flow-accomplishes-mev-resilience "Direct link to How Flow Accomplishes MEV Resilience")

Unlike many blockchains, **Flow was designed from the ground up to minimize MEV** through a unique multi-role architecture. Flow introduces key design choices that break the typical MEV-enabling structure:

### 1. **Separating Transaction Selection from Execution**[​](#1-separating-transaction-selection-from-execution "Direct link to 1-separating-transaction-selection-from-execution")

On Flow, **Collection Nodes** select transactions, but they do not have access to the execution state or computing power to simulate them. Meanwhile, **Execution Nodes** run transactions but cannot choose or reorder them.

This separation significantly reduces the ability of block builders to test transactions before execution. Even if an attacker controls both a Collection Node and an Execution Node, they cannot easily extract MEV.

### 2. **Separating Transaction Ordering from Execution**[​](#2-separating-transaction-ordering-from-execution "Direct link to 2-separating-transaction-ordering-from-execution")

Flow further decentralizes control by introducing **Consensus Nodes** that determine transaction order. These nodes are separate from both Collection Nodes and Execution Nodes.

For an attacker to perform MEV, they would need to:

* Control a **Collection Node** to insert a transaction
* Control a **Consensus Node** to place it in the desired order
* Have execution state access to predict its effects

This makes it vastly more difficult to extract MEV compared to traditional blockchains, where a single entity often controls all three functions.

### 3. **Strict Transaction Execution Rules**[​](#3-strict-transaction-execution-rules "Direct link to 3-strict-transaction-execution-rules")

Execution Nodes on Flow have a **simple, enforceable rule**:  
They **must** execute transactions exactly as ordered by Consensus Nodes—or they get slashed.

Unlike traditional blockchains, where the same party both orders and executes transactions, Flow ensures that Execution Nodes cannot manipulate transaction order for profit.

### 4. **Parallel Processing for Extra MEV Resistance**[​](#4-parallel-processing-for-extra-mev-resistance "Direct link to 4-parallel-processing-for-extra-mev-resistance")

Flow’s unique **pipelined execution model** adds another layer of complexity for potential attackers.

While one block is being executed, the next block is undergoing consensus, and a third block is still collecting transactions. This means that **to front-run or sandwich attack on Flow, an attacker must successfully predict the outcome of at least two unexecuted blocks—one of which hasn’t even been built yet**.

Even with significant resources, this makes profitable MEV attacks incredibly difficult.

## The End Result: A Fairer Blockchain[​](#the-end-result-a-fairer-blockchain "Direct link to The End Result: A Fairer Blockchain")

Flow’s architecture ensures that:

* The nodes selecting transactions **don’t know** their order
* The nodes ordering transactions **don’t know** the blockchain state
* The nodes executing transactions **can’t** modify the order

By **intentionally separating powers**, Flow eliminates MEV at its root rather than merely mitigating its effects.

This level of protection against MEV is not an afterthought—it has been a fundamental design goal of Flow since day one. If equitable access matters, **why settle for anything less?**

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/basics/mev-resistance.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Fees](/build/basics/fees)[Next

Events](/build/basics/events)

###### Rate this page

😞😐😊

* [The Hidden Cost of MEV in Decentralized Systems](#the-hidden-cost-of-mev-in-decentralized-systems)
* [Why MEV Persists on Most Blockchains](#why-mev-persists-on-most-blockchains)
* [How Flow Accomplishes MEV Resilience](#how-flow-accomplishes-mev-resilience)
  + [1. **Separating Transaction Selection from Execution**](#1-separating-transaction-selection-from-execution)
  + [2. **Separating Transaction Ordering from Execution**](#2-separating-transaction-ordering-from-execution)
  + [3. **Strict Transaction Execution Rules**](#3-strict-transaction-execution-rules)
  + [4. **Parallel Processing for Extra MEV Resistance**](#4-parallel-processing-for-extra-mev-resistance)
* [The End Result: A Fairer Blockchain](#the-end-result-a-fairer-blockchain)

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
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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