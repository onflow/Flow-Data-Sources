# Source: https://developers.flow.com/networks/staking

Epochs, Staking & Delegating on Flow | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)

  + [Epoch and Staking Terminology](/networks/staking/epoch-terminology)
  + [Epoch and Reward Schedule](/networks/staking/schedule)
  + [Epoch Preparation Protocol](/networks/staking/epoch-preparation)
  + [Stake Slashing](/networks/staking/stake-slashing)
  + [Epoch Scripts and Events](/networks/staking/epoch-scripts-events)
  + [Staking Technical Overview](/networks/staking/technical-overview)
  + [Staking Scripts and Events](/networks/staking/staking-scripts-events)
  + [How to Query Staking rewards](/networks/staking/staking-rewards)
  + [QC and DKG](/networks/staking/qc-dkg)
  + [QC/DKG Scripts and Events](/networks/staking/qc-dkg-scripts-events)
  + [Machine Account](/networks/staking/machine-account)
  + [FAQs](/networks/staking/faq)
  + [Technical Staking Options](/networks/staking/staking-options)
  + [Staking Collection Guide](/networks/staking/staking-collection)
  + [Basic Staking Guide (Deprecated)](/networks/staking/staking-guide)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* Staking and Epochs

On this page

# Epochs, Staking & Delegating on Flow

This document provides an introduction to staking FLOW tokens on the Flow network
for token holders and node operators.
Staking is an important part of the security protocol of a proof-of-stake (PoS) blockchain.
Running nodes and staking tokens contributes to the blockchain's
security and is rewarded accordingly.

## What is Staking?[​](#what-is-staking "Direct link to What is Staking?")

Flow is a global network of computers working together
to maintain the security and integrity of its users' data.

This global network is made up of many individual nodes: software applications run by people.
Every node in the network shares a small part of the responsibility
to keep the network running smoothly and to ensure that other nodes are doing the same.
This shared responsibility is a core premise of decentralization, because no single central
node is solely responsible for the security and integrity of the network and the data it contains.

Node operators are what we call the people who run nodes.
In order to connect their software applications as nodes on the network,
a node operator must first purchase tokens. Every node operator has to temporarily give (or ‘stake’)
a large number of their tokens to the network as a promise that they will not modify their node
to do something that is against the rules of the network, like steal funds from users' accounts.
This process of temporarily giving up tokens is called staking.

If a node ever breaks the rules defined by the network,
a number of the node operator's staked tokens will be taken from them as a punishment.
This process is automatic. Every node knows the rules defined by the network
and automatically watches other nodes and reports them if they misbehave.
Meanwhile, the network pays the node operator a reward from a mixture of
transaction fees and newly minted tokens
on a regular basis provided their node does not break the rules.

If a node operator breaks the rules, they lose the tokens they've staked.
If they operate their node with integrity, they get rewarded with more tokens!
This is the basic incentive that enables a decentralized proof-of-stake network, like Flow.

## How Does Staking Work on Flow?[​](#how-does-staking-work-on-flow "Direct link to How Does Staking Work on Flow?")

The Flow protocol maintains a list of node operators.
The list contains important information about each node, like their public keys, node address,
and what kind of node they are running.
(Collection, Consensus, Execution, Verification, or Access)

A node operator registers a node by submitting a transaction containing
their node information, a cryptographic proof that they control their node info,
and the FLOW they wish to stake.
If they meet the requirements to run a node, then will be accepted to join the network!

Once a node is staking and operating properly, it will receive periodic reward payments,
assuming it stays online and actively participates in the protocol
without committing any actions that would harm the network, which we call slashable offenses.
Once nodes have registered, they are required to operate for a protocol-specified timeframe.
This timeframe is otherwise known as an **Epoch.**

## Epochs[​](#epochs "Direct link to Epochs")

An **Epoch** is a roughly week-long period that the network uses
to manage list of nodes and pay rewards.

* Only a pre-determined set of nodes is authorized to participate in the protocol.
  The set of authorized nodes is known to all network participants.
  This set is referred to as the **Identity Table**.
* An **Epoch** is defined as a period of time, where the set of authorized nodes is constant
  (or can only shrink due to ejection of malicious nodes).

Every epoch, a list of committed nodes are chosen to be the staked nodes of the network.
This list is called the **Identity Table (ID Table)**.
The node's staked tokens are locked in and cannot change for the duration of the epoch.
At the end of the epoch, rewards are paid to each staked node based on how many tokens they had staked for that epoch
and how well they performed during the epoch. Nodes can choose to join or leave, but changes to the Identity Table
can only happen at end of an epoch, which is also the beginning of a new epoch.
This process repeats itself indefinitely, as long as the network remains functioning.

To determine the list of nodes that are included as officially staked nodes in the next epoch,
the protocol looks at the records of all the nodes that have committed tokens.
It checks to make sure each node's information is correct and that the node is running properly.
Each node also has to have committed tokens above the minimum stake required for their node role
and be authorized by the service account.
If any of these checks are insufficient, the node is not included in the next epoch.

Every epoch, some nodes also have to perform certain processes to initialize the state and communication
with other nodes for the next epoch. These processes are called **Cluster Quorum Certificate Generation (QC)**,
and **Distributed Key Generation (DKG)**. If any node does not perform this initialization properly,
it is not included in the next epoch's Identity Table.

If a node passes all the checks and initializations, it is approved and included as an official node for the next epoch.

Nodes (and users who delegate to them) do not have to continue to submit
staking registration transactions every epoch in order to remain staked.
As long as they continue to run their node properly, their tokens will remain staked.
A node operator only needs to take action if they want to stake more tokens
or if they want to unstake their staked tokens.

If a node operator or delegator decides to stake or unstake tokens,
their requests are not carried out until the end of the current epoch.
In the case of unstaking requests, they also must wait an additional
epoch before their unstaked tokens are available to withdraw.
This allows the protocol to deal with any slashable offenses that may have happened in the previous epoch.

See the [Epochs](/networks/staking/epoch-preparation) section of the documentation for in-depth explanations
of the identity table, epoch schedule, QC, and DKG.

## Rewards[​](#rewards "Direct link to Rewards")

Please see the [schedule](/networks/staking/schedule) section of the documentation
for information about reward calculations and schedule and
what you can do with the rewards you earn by staking a node!

## Delegation[​](#delegation "Direct link to Delegation")

Any account in the network may also participate in staking by delegating their tokens to a node operator.
Every node operator in the network is eligible to receive delegations, there is no opting out.

To delegate to a node, a user simply specifies the ID of the node they want to delegate to
and the amount of tokens they want to delegate.
The tokens are committed and managed in the exact same way that normal staked tokens are managed.

Rewards for delegators are also calculated in the exact same way that rewards for node operators are calculated,
with one difference in that 8% of the calculated amount is given to the delegatee (the node being delegated to).
The remaining 92% is awarded to the delegator.

## How Do I Stake?[​](#how-do-i-stake "Direct link to How Do I Stake?")

So you have decided you want to be a part of the Flow network? Welcome!
You are joining a group of people from all around the world that are a part of a movement that is bringing decentralization and transparency into the world.

### Staking using Flow Port[​](#staking-using-flow-port "Direct link to Staking using Flow Port")

[Flow Port](https://port.onflow.org/) is a simple browser-based app for the Flow blockchain
that provides functionality for sending, receiving, and staking tokens.
Any wallet that uses the [Flow Client Library](/tools/clients/fcl-js)
is compatible with Flow Port.

If you created your account using [Flow Port](https://port.onflow.org/),
you can also stake and earn rewards using the Flow Port.
Follow this [step-by-step guide](/networks/flow-port/staking-guide) to stake using Flow Port.
Flow Port currently supports staking as a node, delegating,
and reward withdrawal using **Flow Reference Wallet**, **Ledger**, **Shadow**, **NuFi**, and any other FCL compatible accounts / wallets.

### Staking via a Custody Provider[​](#staking-via-a-custody-provider "Direct link to Staking via a Custody Provider")

If you are using a custody provider who controls your account and private keys for you,
such as Kraken, Finoa, or Coinlist, they all have different policies and processes
for what you need to do to stake your tokens, the rewards you receive,
and the fees that they take from your staking rewards.

### Manual Staking or Building your own Staking Integration[​](#manual-staking-or-building-your-own-staking-integration "Direct link to Manual Staking or Building your own Staking Integration")

If you are self-custodying your Flow account and keys, or you want to build a staking service for customers,
you will need to learn more about how staking works,
the various methods for staking, and how you can participate safely and reliably.
See the [staking technical overview](/networks/staking/technical-overview) first
for information about technical integration.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/index.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

User safety](/networks/network-architecture/user-safety)[Next

Epoch and Staking Terminology](/networks/staking/epoch-terminology)

###### Rate this page

😞😐😊

* [What is Staking?](#what-is-staking)
* [How Does Staking Work on Flow?](#how-does-staking-work-on-flow)
* [Epochs](#epochs)
* [Rewards](#rewards)
* [Delegation](#delegation)
* [How Do I Stake?](#how-do-i-stake)
  + [Staking using Flow Port](#staking-using-flow-port)
  + [Staking via a Custody Provider](#staking-via-a-custody-provider)
  + [Manual Staking or Building your own Staking Integration](#manual-staking-or-building-your-own-staking-integration)

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