# Source: https://developers.flow.com/networks/staking/epoch-preparation

Epoch Preparation Protocol | Flow Developer Portal



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

* [Staking and Epochs](/networks/staking)
* Epoch Preparation Protocol

On this page

warning

If you haven't read the staking introduction, please read that
first. That document provides a non-technical overview of staking on Flow for
all users and is a necessary prerequisite to this document.

warning

This document assumes you have some technical knowledge about the Flow
blockchain and programming environment.

# Epochs

The epoch preparation protocol defines how information about the next epoch
is determined and propagated to the protocol state.

There are two primary actors in this protocol, the Epoch Smart Contracts, and the Consensus Committee:

* [`Epoch Smart Contracts`](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs) - the smart contracts that manage epochs:
  + `FlowClusterQC` : Manages the quorum certificate generation for bootstrapping
    the hotstuff consensus algorithm for each collector cluster.
  + `FlowDKG` : Manages the Distributed Key Generation that consensus nodes participate
    in to initialize the random beacon for each epoch.
  + `FlowIDTableStaking` : Manages the source of truth for the identity table,
    and enforces rules related to staking FLOW, delegating, paying rewards, and allocating token movements between epochs.
  + `FlowEpoch` : Ties all of the previously mentioned contracts together to manage
    the high level epoch lifecycle. `FlowEpoch` acts as a state machine that transitions
    between different epoch phases when specific conditions from the other contracts are met and triggers important operations in the other smart contracts when phase changes happen.
* `Consensus Committee` - the committee of consensus nodes for the current epoch

This document describes the communication protocol between these two actors and the impact on the protocol state.

It gives an overview of the process of epochs, the staking auction, and the epoch setup and commit phases.
It is an important prerequisite to understand before proceeding with any other technical integration or interaction with the Flow Protocol,
but does not provide step-by-step instructions for how to perform specific actions.

The transactions described in this document are contained in the [`flow-core-contracts/transactions/epoch/`](https://github.com/onflow/flow-core-contracts/tree/master/transactions/epoch)
directory. You can see the text of all the transactions used to interact with the smart contracts there.

## Epochs Overview[​](#epochs-overview "Direct link to Epochs Overview")

Only a pre-determined set of nodes is authorized to participate in the protocol at any given time.
The set of authorized nodes is a-priori known to all network participants.
This set is referred to as the **Identity Table**. An **Epoch** is defined as a period of time
where the set of authorized nodes is constant (or can only shrink due to ejection of malicious nodes).

At an Epoch switchover, which is the time when the network transitions from one epoch to the next,
the set of authorized nodes can change. For each of Flow's node roles, the Flow protocol admits a protocol-determined number of nodes.

For each Epoch, there is a [Staking Auction](/networks/staking/technical-overview) in which new potential node operators may submit Staking Commitments.
All this is completely smart-contract based and handled through conventional transactions.

After the Staking Auction is over, the protocol determines which commitments to accept and which to reject.
The node operators whose staking commitments were accepted are added to the Identity Table for the next epoch,
and become authorized participants at the next epoch switchover.
Staked Nodes also can submit other operations to modify their existing stake, which are all carried out at the end of the current epoch.

The smart contract that determines the nodes for the next Epoch has special privileges.
Specifically, it is allowed to emit [Service Events](/networks/staking/epoch-scripts-events#monitor-epoch-service-events),
which are how the execution state updates the consensus node-based protocol state.

At the end of the staking auction, the epoch smart contracts conclude that they have now determined
the set of nodes which will be running the network for the next Epoch, and the amount of FLOW that all the nodes have staked.
The smart contract then emits a service event with this information.

When processing the block with seat assignment, all network nodes (including future ones which are supposed to monitor the chain in anticipation)
are thereby informed about the upcoming change.

warning

Note: At this point in the epoch (end of the staking auction),
there is no change in participating nodes.
The change in participating nodes happens at the end of the epoch.

After the staking auction, there is an interim period of time until the new Epoch starts for the following tasks to be completed:

* The epoch smart contract runs the cluster assignment algorithm for all the collector nodes
  and each collector node will vote for the root block of their respective clusters
* The Random Beacon Committee for the next Epoch (currently all consensus nodes)
  will run the Distributed Key Generation (DKG),
* When completing the QC generation and DKG, the smart contracts will emit a service event.
  After consensus nodes have collected all relevant information (public keys for the random beacon and cluster quorum certificates),
  they can update the identity table to include the information for the next Epoch.

If preparation for the next Epoch is not completed before the current Epoch ends,
the network goes into epoch fallback mode (EFM) and a special transaction, sometimes including
a spork, is required to transition to the next Epoch.

## Epoch Length[​](#epoch-length "Direct link to Epoch Length")

The length of an Epoch is measured in terms of consensus views.
The number of views in an epoch and in the various epoch phases are determined before
the Epoch begins and stored as a field in the main epoch smart contract (`FlowEpoch`).

Generally, there is not a block for every view, so the view number will not change at the same rate as the block height.

Because the length of a consensus view can vary depending on many different factors,
the wall-clock time of an epoch is expected to vary from week to week.
Under typical network conditions we expect the variance in epoch length to be less than 2 hours for a 1-week epoch (~1%).
Under adverse network conditions the variance in epoch length will increase (typically this will result in longer epochs).

As the average view rate changes over time, the Service Account can change the epoch length to
target a 1 week wall-clock epoch length.

# Phases

The preparation for the next epoch is separated into distinct phases.
Each phase occurs completely within the current epoch.

![Flow Epoch Schedule](https://storage.googleapis.com/flow-resources/documentation-assets/epoch-phase-diagram.png)

The Epoch Smart Contract acts as a state machine. The smart contract keeps a record of the current phase,
the number of views in the current phase, and the conditions that need to be met in order to advance to the next phase, or next epoch.
A special `Heartbeat` resource is used to call the `advanceBlock()` method during every single new block in Flow.
During these regular method calls, if all of the conditions are met to advance to the next phase,
the smart contract performs any relevant retrieval and storage of information, emits a Service Event,
and transitions to the next phase, which often involves setting certain metadata
or enabling one of the connected smart contracts to begin its work.

From the perspective of the consensus committee, the phase transitions within epochs
occur as a result of including a service event in a block,
thus the phase transition only applies to the fork containing the block with the service event.

At the end of Phase 0 and beginning of Phase 1, the `EpochSetup` service event is emitted
that contains the identity table and other initial metadata for the upcoming epoch.

At the end of Phase 1 and beginning of Phase 2, the `EpochCommit` service event
is emitted that contains the results of the Epoch Setup phase.

The start of a new epoch is the first block with its view > the last view of the previous epoch,
and its parent view ≤ the last view of the last epoch.

## Phase Transitions[​](#phase-transitions "Direct link to Phase Transitions")

The **Consensus Committee** triggers the **phase transition coinciding with the Epoch switchover**
by publishing the block of the next Epoch.
This block's execution state will also detect the the end view of an epoch has arrived
and trigger the start of the new epoch.
The transition to a new epoch is also marked by the emission of [an event](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowEpoch.cdc#L62) (`EpochStart`)
from the epoch smart contract.



The state of the smart contracts reflect the latest epoch's new identity table and metadata.

For the **Epoch-*internal* Phase transitions**, meaning the phase transitions within an epoch,
the **Epoch Smart Contract** provides the trigger by emitting a respective service event:

* The `EpochSetup` service event triggers the phase transition
  `Staking Auction Phase` → `Epoch Setup Phase`
* The `EpochCommit` service event triggers the phase transition
  `Epoch Setup Phase` → `Epoch Committed Phase`

Only one of each service event may be emitted each epoch, for a given fork.
`EpochCommit` may only be emitted after `EpochSetup` has been generated in the respective given fork.

The `FlowEpoch` contract manages all of these phases, the `FlowIDTableStaking` contract
manages the identity table and staking auction, the `FlowClusterQC` contract manages
the Quorum Certificate generation for collector clusters, and the `FlowDKG` contract manages
the Distributed Key Generation protocol for the consensus nodes.

Initially, control of these phases and contracts will be managed manually by the Flow Token Admin,
but control will eventually be completely decentralized and managed by the node software, smart contracts,
and democratically by all the stakers in the network.

## Phase 0: Staking Auction[​](#phase-0-staking-auction "Direct link to Phase 0: Staking Auction")

**Purpose:** During the staking auction phase, operators can put up stake
in exchange for being a part of the upcoming epoch.
All voluntary commitments to register a new node, increase, or decrease stake for the next epoch
must occur before the end of this phase.

**Duration:** The staking auction phase begins with the first block of the current Epoch
Its last block is the block in which the `EpochSetup` service event is emitted.

### **Protocol Directives:**[​](#protocol-directives "Direct link to protocol-directives")

Epoch Smart Contract

* The `FlowEpoch` Smart Contract is responsible for ensuring that staking, un-staking,
  and stake-modification transactions for the next epoch are
  are only executed during the staking auction and fail otherwise.
  The contract enforces this by setting a `stakingEnabled` field in the staking contract.
  Every staking method checks to see if this is set before executing.
* The `FlowEpoch` Smart Contract must ensure that the subsequent phases
  are sufficiently long to perform all required tasks before the epoch ends.
* As part of the execution result for the last block of the staking auction,
  the `Epoch Smart Contract` computes the seat assignment information for the next epoch,
  and emits a specialized service event, the `EpochSetup` event,
  with the timing and identity table information about the next epoch.
  See the [Epoch Setup Event Documentation](/networks/staking/epoch-scripts-events#flowepochepochsetup)
  for a detailed breakdown of the epoch setup event.

## Phase 1: Epoch Setup[​](#phase-1-epoch-setup "Direct link to Phase 1: Epoch Setup")

**Purpose:** During the epoch setup phase, all nodes participating in the upcoming epoch
must perform setup tasks in preparation for the upcoming epoch.

**Duration:** The epoch setup phase begins right after the `EpochSetup` service event is emitted.
It ends with the block where `EpochCommit` service event is emitted.

### **Protocol Directives:**[​](#protocol-directives-1 "Direct link to protocol-directives-1")

Consensus:

* When a primary constructs a block that seals the `EpochSetup` service event,
  the primary includes an update to the protocol state in the block.
  Specifically, it adds the nodes for the `PendingEpoch` to the list of authorized nodes.
  When this block is propagated, all staked nodes will know about the participants
  in the next epoch and can communicate with them.
* Based on the `RandSeed` field in the `EpochSetup` event, all nodes compute:

  + The seed to initialize the consensus node's primary selection algorithm for the next epoch
  + The seeds to initialize the collector clusters' primary selection algorithm for the next epoch
* The collector nodes generate the root block for their respective clusters
  in the next Epoch and submit a vote for the root block to a specialized smart contract, `FlowClusterQC`.
* The Random Beacon Committee for the next Epoch (currently all consensus nodes)
  will run the DKG through a specialized smart contract, `FlowDKG`.

Epoch Smart Contract:

* The `FlowEpoch` Smart Contract is responsible for ensuring that Epoch Setup transactions
  are only executed during the Epoch Setup phase and fail otherwise.
  The contract enforces this by setting an `enabled` field in the `FlowClusterQC` and `FlowDKG` contracts.
  Every state-changing method from these contracts checks to see if this is set before executing.
* The `FlowEpoch` Smart Contract must ensure that the subsequent phase
  is sufficiently long to perform all required tasks before the epoch ends.
* As part of the execution of the last block of the Epoch Setup phase,
  the `FlowEpoch` Smart Contract computes the public key shares generated by the DKG
  and the `QC`s for the collector clusters and publishes these as `EpochCommit` service event.
  The `FlowEpoch` Smart Contract should emit this event as soon as the artifacts are determined.

See the [Epoch Commit Event Documentation](/networks/staking/epoch-scripts-events#flowepochepochcommit)
for a detailed breakdown of the epoch commit event.

## Phase 2: Epoch Committed[​](#phase-2-epoch-committed "Direct link to Phase 2: Epoch Committed")

**Purpose:** When the epoch committed phase starts, the precise role of each node is fully specified.
From a protocol-perspective, all information is available for each node
to start its operation for the next Epoch.
This phase provides some time for nodes to establish the communication channels
and synchronize with the network to seamlessly switch over to the next epoch.

**Duration:** The epoch committed phase begins right *after* the `EpochCommit` service event
has been emitted. It ends when the epoch ends.

### **Protocol Directives:**[​](#protocol-directives-2 "Direct link to protocol-directives-2")

Consensus

* When a primary constructs a block that seals the `EpochCommit` service event,
  the primary includes an update to the protocol state in the block. Specifically, it:
* adds the information generated in the setup phase to the Protocol State and
* marks the updated Protocol State as `committed` in this respective fork.

# Query Information from the Epoch Contract

See the [epoch scripts and events document](/networks/staking/epoch-scripts-events#introduction) for detailed documentation about
you can use scripts events to learn information about the state of the epoch contracts.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/04-epoch-preparation.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Epoch and Reward Schedule](/networks/staking/schedule)[Next

Stake Slashing](/networks/staking/stake-slashing)

###### Rate this page

😞😐😊

* [Epochs Overview](#epochs-overview)
* [Epoch Length](#epoch-length)
* [Phase Transitions](#phase-transitions)
* [Phase 0: Staking Auction](#phase-0-staking-auction)
  + [**Protocol Directives:**](#protocol-directives)
* [Phase 1: Epoch Setup](#phase-1-epoch-setup)
  + [**Protocol Directives:**](#protocol-directives-1)
* [Phase 2: Epoch Committed](#phase-2-epoch-committed)
  + [**Protocol Directives:**](#protocol-directives-2)

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