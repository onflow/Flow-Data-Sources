# Source: https://developers.flow.com/networks/staking/qc-dkg

Quorum Certificate and Distributed Key Generation | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* QC and DKG

On this page

# Quorum Certificate and Distributed Key Generation

warning

If you haven't read the Intro to Flow Staking document and the Epoch protocol document,
please read that first. Those documents provide an overview of epochs on Flow for
all users and are necessary prerequisites to this document.

warning

This document assumes you have some technical knowledge about the Flow
blockchain and programming environment.

## Epoch Setup Phase[​](#epoch-setup-phase "Direct link to Epoch Setup Phase")

**Purpose:** During the epoch setup phase, all nodes participating in the upcoming epoch
must perform setup tasks in preparation for the upcoming epoch, including
the Collector Cluster Quorum Certificate Generation and Consensus Committe Distributed Key Generation.

**Duration:** The epoch setup phase begins right after the `EpochSetup` service event is emitted.
It ends with the block where `EpochCommit` service emitted.

## Machine Accounts[​](#machine-accounts "Direct link to Machine Accounts")

The processes described in this document are fully automated.

They are expected to be performed entirely by the node software with no manual
interaction required by the node operator after the node has been set up and registered.

To facilitate this, we recommend that node operators use a secondary "machine account"
that only stores the `FlowClusterQC.Voter` or `FlowDKG.Participant` resource objects
in addition to FLOW to pay for transaction fees. You can connect your node to this account
to participate in the Epoch Setup Phase without having to do the actions manually.

If you are using the [Staking Collection](/networks/staking/staking-collection) for your node,
this functionality is built-in. When you register a node with the staking collection,
you also have to provide a public key or keys for your machine account for the node.

If you have a node without a machine account (if you were operating a node from the time
before epochs and staking collection were enabled, for example) the staking collection
also provides a method to create a machine account for an existing node.

See the [Staking Collection Docs](/networks/staking/staking-collection#machine-account-support)
for more information.

## Collector Cluster Quorum Certificate Generation Protocol[​](#collector-cluster-quorum-certificate-generation-protocol "Direct link to Collector Cluster Quorum Certificate Generation Protocol")

The collector nodes are organized into clusters and must bootstrap
the Hotstuff consensus algorithm for each cluster. To do this,
they generate the root block for their respective clusters
and submit a vote for the root block to a specialized smart contract, `FlowClusterQC`.
If 2/3 of the collectors in a cluster have voted with the same unique vote,
then the cluster is considered complete.
Once all clusters are complete, the QC is complete.

### `FlowClusterQC` Transactions[​](#flowclusterqc-transactions "Direct link to flowclusterqc-transactions")

#### Create QC Voter Object[​](#create-qc-voter-object "Direct link to Create QC Voter Object")

A node uses the [`getClusterQCVoter()`](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowEpoch.cdc#L905)
function in the `FlowEpoch` contract to create their Voter object and needs to provide
a reference to their `FlowIDTableStaking.NodeStaker` object to prove they are the node owner.

When registering a node with the staking collection, this process is handled by
[the transaction to register.](/networks/staking/staking-collection#register-a-new-staked-node)
It also creates a machine account for the QC object.

If a user already has a registered node with the staking collection, but hasn't created their QC Voter object yet,
they can use the [`create_machine_account.cdc` transaction.](/networks/staking/staking-collection#create-a-machine-account-for-an-existing-node)

If a user is not using the staking collection, they can use the **Create QC Voter** ([QC.01](/build/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts))
transaction. This will only store the QC Voter object in the account that stores the `NodeStaker` object.
It does not create a machine account or store it elsewhere, so it is not recommended to use. We encourage to use the staking collection instead.

#### Submit Vote[​](#submit-vote "Direct link to Submit Vote")

During the Epoch Setup Phase, the node software should submit the votes for the QC generation
automatically using the **Submit QC Vote** ([QC.02](/build/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts))
transaction with the following arguments.

| Argument | Type | Description |
| --- | --- | --- |
| **voteSignature** | `String` | The signed message (signed with the node's staking key) |
| **voteMessage** | `String` | The raw message itself. |

## Consensus Committee Distributed Key Generation Protocol (DKG)[​](#consensus-committee-distributed-key-generation-protocol-dkg "Direct link to Consensus Committee Distributed Key Generation Protocol (DKG)")

The Random Beacon Committee for the next Epoch (currently all consensus nodes)
will run the DKG through a specialized smart contract, `FlowDKG`.
To do this, they post a series of messages to a public "whiteboard" to
collectively generate a shared key array. When each node has enough information
to generate their array of keys, they send the generated array to the smart contract
as their final submission.
If `(# of consensus nodes-1)/2` consensus nodes submit the same key array,
the DKG is considered to be complete.

### `FlowDKG` Transactions[​](#flowdkg-transactions "Direct link to flowdkg-transactions")

#### Create DKG Participant Object[​](#create-dkg-participant-object "Direct link to Create DKG Participant Object")

A node uses the [`getDKGParticipant()`](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowEpoch.cdc#L919)
function in the `FlowEpoch` contract to create their Voter object and needs to provide
a reference to their `FlowIDTableStaking.NodeStaker` object to prove they are the node owner.

When registering a node with the staking collection, this process is handled by
[the transaction to register.](/networks/staking/staking-collection#register-a-new-staked-node)
It also creates a machine account for the DKG Object.

If a user already has a registered node with the staking collection, but hasn't created their DKG Participant object yet,
they can use the [`create_machine_account.cdc` transaction.](/networks/staking/staking-collection#create-a-machine-account-for-an-existing-node)

If a user is not using the staking collection, they can use the **Create DKG Participant** ([DKG.01](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts))
transaction. This will only store the DKG Participant object in the account that stores the `NodeStaker` object.
It does not create a machine account or store it elsewhere, so it is not recommended to use.
The staking collection is the recommended method.

#### Post Whiteboard Message[​](#post-whiteboard-message "Direct link to Post Whiteboard Message")

During the Epoch Setup Phase, the node software should post whiteboard messages to the DKG
automatically using the **Post Whiteboard Message** ([DKG.02](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts))
transaction with the following arguments.

| Argument | Type | Description |
| --- | --- | --- |
| **content** | `String` | The content of the whiteboard message |

#### Send Final Submission[​](#send-final-submission "Direct link to Send Final Submission")

During the Epoch Setup Phase, the node software should send its final submission for the DKG
automatically using the **Send Final Submission** ([DKG.03](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts))
transaction with the following arguments.

| Argument | Type | Description |
| --- | --- | --- |
| **submission** | `[String?]` | The final key vector submission for the DKG. |

## Monitor Events and Query State from the QC and DKG Contracts[​](#monitor-events-and-query-state-from-the-qc-and-dkg-contracts "Direct link to Monitor Events and Query State from the QC and DKG Contracts")

See the [QC and DKG events and scripts document](/networks/staking/qc-dkg-scripts-events) for information
about the events that can be emitted by these contracts and scripts you can use to query information.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/09-qc-dkg.md)

Last updated on **Mar 6, 2025** by **Giovanni Sanchez**

[Previous

How to Query Staking rewards](/networks/staking/staking-rewards)[Next

QC/DKG Scripts and Events](/networks/staking/qc-dkg-scripts-events)

###### Rate this page

😞😐😊

* [Epoch Setup Phase](#epoch-setup-phase)
* [Machine Accounts](#machine-accounts)
* [Collector Cluster Quorum Certificate Generation Protocol](#collector-cluster-quorum-certificate-generation-protocol)
  + [`FlowClusterQC` Transactions](#flowclusterqc-transactions)
    - [Create QC Voter Object](#create-qc-voter-object)
    - [Submit Vote](#submit-vote)
* [Consensus Committee Distributed Key Generation Protocol (DKG)](#consensus-committee-distributed-key-generation-protocol-dkg)
  + [`FlowDKG` Transactions](#flowdkg-transactions)
    - [Create DKG Participant Object](#create-dkg-participant-object)
    - [Post Whiteboard Message](#post-whiteboard-message)
    - [Send Final Submission](#send-final-submission)
* [Monitor Events and Query State from the QC and DKG Contracts](#monitor-events-and-query-state-from-the-qc-and-dkg-contracts)

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