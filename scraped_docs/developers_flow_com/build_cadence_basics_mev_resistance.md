# Source: https://developers.flow.com/build/cadence/basics/mev-resistance

MEV Resistance | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)

    - [Network Architecture ↗️](/build/cadence/basics/network-architecture)
    - [Blocks](/build/cadence/basics/blocks)
    - [Collections](/build/cadence/basics/collections)
    - [Accounts](/build/cadence/basics/accounts)
    - [Transactions](/build/cadence/basics/transactions)
    - [Scripts](/build/cadence/basics/scripts)
    - [Fees](/build/cadence/basics/fees)
    - [MEV Resistance](/build/cadence/basics/mev-resistance)
    - [Events](/build/cadence/basics/events)
    - [FLOW Coin](/build/cadence/basics/flow-token)
    - [Smart Contracts ↙](/build/cadence/basics/smart-contracts)
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

* Cadence
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/basics/mev-resistance.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Fees](/build/cadence/basics/fees)[Next

Events](/build/cadence/basics/events)

###### Rate this page

😞😐😊

Copy as Markdown

* [The Hidden Cost of MEV in Decentralized Systems](#the-hidden-cost-of-mev-in-decentralized-systems)
* [Why MEV Persists on Most Blockchains](#why-mev-persists-on-most-blockchains)
* [How Flow Accomplishes MEV Resilience](#how-flow-accomplishes-mev-resilience)
  + [1. **Separating Transaction Selection from Execution**](#1-separating-transaction-selection-from-execution)
  + [2. **Separating Transaction Ordering from Execution**](#2-separating-transaction-ordering-from-execution)
  + [3. **Strict Transaction Execution Rules**](#3-strict-transaction-execution-rules)
  + [4. **Parallel Processing for Extra MEV Resistance**](#4-parallel-processing-for-extra-mev-resistance)
* [The End Result: A Fairer Blockchain](#the-end-result-a-fairer-blockchain)

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
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.