# Source: https://developers.flow.com/networks/node-ops/node-operation/slashing

Slashing Conditions | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)

  + [Access Nodes](/networks/node-ops/access-nodes/access-node-setup)
  + [EVM Gateway Setup](/networks/node-ops/evm-gateway/evm-gateway-setup)
  + [Light Nodes](/networks/node-ops/light-nodes/observer-node)
  + [Participating in the Network](/networks/node-ops/node-operation/faq)

    - [Operator FAQ](/networks/node-ops/node-operation/faq)
    - [Byzantine Attack Response](/networks/node-ops/node-operation/byzantine-node-attack-response)
    - [Database Encryption for Existing Node Operators](/networks/node-ops/node-operation/db-encryption-existing-operator)
    - [Node Operations Guide](/networks/node-ops/node-operation/guides/genesis-bootstrap)
    - [Machine Accounts for Existing Node Operators](/networks/node-ops/node-operation/machine-existing-operator)
    - [Node Monitoring](/networks/node-ops/node-operation/monitoring-nodes)
    - [Node Bootstrapping](/networks/node-ops/node-operation/node-bootstrap)
    - [Node Economics](/networks/node-ops/node-operation/node-economics)
    - [Node Migration](/networks/node-ops/node-operation/node-migration)
    - [Node Provisioning](/networks/node-ops/node-operation/node-provisioning)
    - [Node Roles](/networks/node-ops/node-operation/node-roles)
    - [Node Setup](/networks/node-ops/node-operation/node-setup)
    - [Past Network Upgrades](/networks/node-ops/node-operation/past-upgrades)
    - [Network Upgrade (Spork) Process](/networks/node-ops/node-operation/spork)
    - [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
    - [Slashing Conditions](/networks/node-ops/node-operation/slashing)
    - [Node Providers](/networks/node-ops/node-operation/node-providers)
    - [Height coordinated upgrade](/networks/node-ops/node-operation/hcu)
    - [Protocol State Bootstrapping](/networks/node-ops/node-operation/protocol-state-bootstrap)
    - [Managing disk space](/networks/node-ops/node-operation/reclaim-disk)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Node Ops](/networks/node-ops)
* Participating in the Network
* Slashing Conditions

On this page

# Slashing Conditions

## Introduction[​](#introduction "Direct link to Introduction")

Flow is a proof-of-stake system, which means holders of FLOW can earn inflationary rewards
by staking their FLOW tokens to secure and operate the network.
A node can participate in the Flow network by depositing a specific amount of stake
(based on role types) thereby making a bonded pledge to participate
in the Flow protocol during the upcoming epoch.
(An epoch is a finite amount of time defined by the protocol, approximately one week,
during which the nodes participate to run the protocol and are responsible for their operations.)

See the [Staking and Epochs section of the documentation](/networks/staking) to learn more
about the design and functionality of this part of the protocol.

Flow nodes follow the procedures defined in the protocol (based on their role)
in order to receive rewards. Any deviation (see Slashing Challenges below)
from the protocol can result in decreased reward payments or punishments.
Severe infractions, which undermine the safety of the network,
can lead to “slashing”, where some or all of the staked tokens are confiscated from the offending node(s).

This reward and punishment structure is designed to guarantee the security
of the protocol and optimize performance over time.
This document outlines the most severe infractions against the protocol
which result in some portion of a node’s stake being taken from them (“slashing conditions”).
Enforcing these slashing conditions is critical to ensure the cryptoeconomic security of the protocol.
Future documents will describe an incentive structure that encourages system-wide efficiency and speed,
by providing bonuses to the most performant nodes and withholding payments to nodes that are unresponsive.

This document assumes a working understanding of the high-level architecture of the Flow blockchain.
Readers who are new to Flow or those looking for a refresher are encouraged
to read the Protocol Summary [here](/networks/node-ops/node-operation/node-roles) and the staking documentation.

## Slashing Conditions[​](#slashing-conditions "Direct link to Slashing Conditions")

Any violation of the Flow protocol that could result in staked tokens being seized
from the offending nodes is called **Slashable Behaviour.**
In order for the tokens to be seized, the data necessary to prove the occurrence of Slashable Behaviour
must be combined with the data necessary to attribute the behaviour
to the node(s) responsible into a **Slashing Witness**.
(A reduction of rewards, e.g. due to lack of active participation,
is not formally included in our definition of slashing.)
The Flow protocol considers only server threats to safety and liveness
to be slashable conditions and as such, there are no performance related slashing penalties.
The one exception is in the case of missing Collections (see the section on MCC below),
where a widespread failure to respond by a large number of nodes is presumed
to be coordinated and therefore punishable with slashing.

Most Slashable Behaviour in Flow can be detected and attributed to the offender
by a single honest node observing that behaviour.
(In other words, one node can generate a Slashing Witness without coordinating with other nodes.)
However, some Slashable Behaviour can only be detected and attributed
by combining information from multiple nodes. In those situations,
the node that first detects the potential infraction raises a **Slashing Challenge**.
When a challenge is raised, other nodes are expected to provide additional information
which can be combined with the original challenge into a definitive Slashing Witness
that is used to adjudicate the challenge. Each type of Slashing Challenge depends
on different information provided from a different subset of nodes,
the details of which are provided below.

Flow adheres to a number of principles in the design of its slashing rules:

* Only Consensus Nodes can perform slashing, and only by following the BFT consensus mechanism
  defined in the protocol. As such, a super-majority of Consensus Nodes must inspect
  and confirm a Slashing Witness before any punishment is levied.
* All Slashing Witnesses are objectively decidable.
  Given the current protocol state (maintained by the Consensus Nodes)
  and a well-formed Slashing Witness, all non-Byzantine Consensus Nodes will deterministically come
  to the same conclusion as to which node or nodes should be slashed (if any)
  and the amount of stake to be seized.
* All Slashing Behaviour in Flow requires active malfeasance on the part of the offending node.
  In other words, a node will only be slashed if it takes an action against the rules of the protocol,
  and it will not be slashed if it fails to take an action prescribed by the protocol.
  (“If your machine is crashed, you won’t get slashed.”) The one exception
  is in the case of missing Collections (see the section on MCC below),
  where a widespread failure to respond by a large number of nodes is presumed
  to be coordinated and therefore punishable with slashing.
* Flow makes no attempt to detect and punish liveness failures within the protocol.
  A liveness failure across the network functionally slashes the stake of any participants
  excluded from participating in the reboot (since their stake is locked in a non-functional network).
  Community analysis can determine which nodes were responsible for the failure
  and exclude those Byzantine actors from the new instance.
* Any staked node of Flow can submit a Slashing Witness for any Slashable Behaviour,
  regardless of its role. (For example, a Collection Node could submit a Slashing Witness
  for an invalid execution receipt, even though the protocol doesn’t require Collection Nodes
  to verify execution receipts.)
* Submitting an invalid Slashing Witness is Slashable Behaviour.
  We treat the invalid Slashing Witness itself as the Slashing Witness for that case.

## Stages of Slashing[​](#stages-of-slashing "Direct link to Stages of Slashing")

Transitioning to a rigorous staking protocol in which all slashable conditions are checked,
enforced, and punished will take place over three phases.
The Slashing Challenges section below outlines the various challenges
which may be submitted against an offending node but these challenges
will not be fully enforced until Phase 3 of the network.

### Phase 1: Beta[​](#phase-1-beta "Direct link to Phase 1: Beta")

* In the beta phase of the network, the expectation is that nodes are running error detection
  and logging but not submitting formal challenges. Any errors found may be submitted
  to the Flow team for additional testing and security improvements.

### Phase 2: Testing Slashing Mechanics[​](#phase-2-testing-slashing-mechanics "Direct link to Phase 2: Testing Slashing Mechanics")

* At this time the slashing mechanisms will be implemented and require testing.
  Formal challenges should be raised and the protocol will follow the complete,
  formal mechanics for arbitrating challenges and slashing perpetrators,
  but no real slashing will take place.

### Phase 3: BFT[​](#phase-3-bft "Direct link to Phase 3: BFT")

* By now, the network has been security-hardened and tested and valid challenges
  result in real slashing of the offending node.

## Slashing Challenges[​](#slashing-challenges "Direct link to Slashing Challenges")

### 0. All Nodes[​](#0-all-nodes "Direct link to 0. All Nodes")

\*\*Invalid Report Witness (IRW): \*\*if any nodes report an invalid/inaccurate witness,
an invalid report witness will be reported by the Consensus Nodes,
and the node(s) reporting the witness get slashed.

### 1. Collection Nodes[​](#1-collection-nodes "Direct link to 1. Collection Nodes")

\*\*1.1 Missing Collection Challenge (MCC): \*\* Collection nodes are responsible
for storing collection content (all transactions) for any collection which they guarantee
during the current epoch and the first 1000 blocks of the next epoch.
During this time they have to respond to any collection request from staked execution,
verification and Consensus Nodes and should respond in a timely manner (specific timeout).
If an Execution Node or a Verification Node doesn't receive the response from any
of the collection guarantors (Collection Nodes who signed a collection),
they can raise a Missing Collection Challenge and broadcast it to the Consensus Nodes to evaluate.

\*\*Adjudication: \*\*Consensus nodes randomly contact some of the guarantors.
If Collection Nodes don't respond, a portion of their stakes will be seized.
If the amount of their stake goes to less than half, they will be fully slashed.
Then the Consensus Nodes notify all the Execution Nodes to skip that collection.
If any of the Collection Nodes respond, Consensus Nodes redirect the collection content
to the Execution Nodes but will also set small penalties both
for all the guarantors and that Execution Node (according to their revenue ratio).

**1.2 Invalid Collection Witness (ICW):** Collection nodes are responsible for responding
to collection content queries by collection hash from any staked nodes.
The collection hash is the hash of an ordered list of transaction hashes.
If a collection content sent by the Collection Node turns out to be invalid,
any staked node can report an Invalid Collection Witness. This includes cases where:

* the content is malformed or incomplete,
* there exists an invalid transaction inside the collection, or
* the collection hash doesn't match (inside collection guarantee).

**Adjudication:** Consensus nodes evaluate the content of the collection,
if the collection is found invalid, the Collection Node who signed the content is slashed.

**1.3 Double Collection Proposal Witness (DCPW):** Collection nodes of a cluster run a mini consensus
inside the cluster to decide on a collection, which requires Collection nodes to propose
the collection and aggregate votes from others. During the collection consensus,
if a Collection Node proposes more than one proposal, any other Collection Node
inside the cluster can report a Double Collection Proposal Witness (including both proposals).

\*\*Adjudication: \*\*Consensus nodes evaluate the content and signatures of these two proposals,
and if the witness turns out to be valid, the Collection Node who proposed two collections will get slashed.

**1.4 Double Collection Voting Witness (DCVW):** Collection nodes of a cluster
run a mini consensus inside the cluster to decide on a collection,
which requires Collection nodes to propose the collection and aggregate votes from others.
During the collection consensus, if a Collection Node votes for more than one collection proposal
with identical collection number and size, any other Collection Node inside the cluster
can report a Double Collection Voting Witness (including both votes).

\*\*Adjudication: \*\*Consensus nodes evaluate the signatures of these two votes and evaluate them,
and if the witness turns out to be valid, the Collection Node who voted two times will get slashed.

### 2. Consensus Nodes[​](#2-consensus-nodes "Direct link to 2. Consensus Nodes")

**2.1 Double Block Proposal Witness (DBPW):** Consensus nodes run the consensus (HotStuff algorithm) over blocks.
During these consensus steps, if a Consensus Node proposes more than one variation of a block proposal,
any other Consensus Node can report a Double Block Proposal Witness (including both proposals).
This report will be broadcasted to all other Consensus Nodes.

\*\*Adjudication: \*\*Consensus nodes evaluate content and signatures of both proposals.
If the witness turns out to be valid, the Consensus Node who submitted both proposals will get slashed.

\*\*2.2 Double Block Voting Witness (DBVW): \*\* Consensus nodes run the consensus (HotStuff algorithm)
over blocks. During the consensus steps, if a Consensus Node votes for
more than one block proposal with the same height, any other Consensus Node can report
a Double Block Voting Witness (including both votes).
This report will be broadcasted to all other Consensus Nodes.

\*\*Adjudication: \*\*Consensus nodes evaluate content and signatures of both votes
and If the witness turns out to be valid, the Consensus Node who submitted both votes will get slashed.

**2.3 Invalid Block Vote Witness (IBVW):** If a Consensus Node votes for an invalid block
or the content of the vote itself is invalid (e.g. vote for non-existing block),
any other Consensus Nodes can report an Invalid Block Vote Witness.

\*\*Adjudication: \*\*Consensus nodes evaluate the vote content and signature.
If the witness turns out to be valid, the Consensus Node who submitted the faulty vote will get slashed.

**2.4 Invalid Block Proposal Witness (IBPW):** If a Consensus Node proposes
an invalid block proposal (e.g. quorum certificate without 2/3 vote),
any other Consensus Nodes can raise an Invalid Block Proposal Witness.

\*\*Adjudication: \*\*Consensus nodes evaluate the proposal content and signature,
If the witness turns out to be valid, the Consensus Node who submitted the invalid proposal
will get slashed.

**2.5 Invalid Block Witness (IBW):** If the block contents returned by any Consensus Node is invalid,
any node can raise the Invalid Block Witness:

* It is malformed or incomplete
* It doesn't match the payload hash provided by the block header

\*\*Adjudication: \*\*Consensus nodes evaluate the block content and signatures.
If the witness turns out to be valid, the Consensus Node who signed the block content will get slashed.

**2.6 Invalid Random Beacon Signature Witness (IRBSW):**
If any participant of the random beacon returns an invalid signature,
an Invalid Random Beacon Signature Witness can be reported by other Consensus Nodes.

**Adjudication:** Consensus nodes evaluate the random beacon signature.
If the witness turns out to be valid, the Consensus Node who signed the invalid random beacon part
will get slashed.

### 3. Execution Nodes[​](#3-execution-nodes "Direct link to 3. Execution Nodes")

\*\*3.1 Faulty Computation Challenge (FCC): \*\* If any of the Verification Nodes
find a fault in the execution of transactions by an Execution Node it can raise an FCC challenge.
An FCC challenge includes a faulty chunk and all the evidence.

\*\*Adjudication: \*\*Consensus nodes evaluate the challenge, by sending requests
for collection contents and chunk data needed to run the faulty chunk and comparing
the results against the expected state commitment. If Consensus Nodes detect any fault
in the execution of that chunk, the Execution Node(s) who signed the faulty execution receipts
will get slashed. If no fault is found, the Verification Node who raised the challenge will get slashed.

\*\*3.2 Conflicting Execution Results Challenge (CERC): \*\*
If two or more variations of execution results are reported by Execution Nodes for a given block.
Since only one can be valid, Consensus Nodes raise a conflicting execution results challenge.

\*\*Adjudication: \*\*As soon as this challenge is raised, all the Verification Nodes
go into full check mode (checks all the chunks). The first execution result
that receives result approval from at least 2/3 of Verification Nodes is the accurate one,
and the other execution results will be considered faulty and Execution Nodes generating those
will get slashed. If none of the execution results receive majority approval
from Verification Nodes after a very long timeout,
all the Consensus Nodes start executing chunks to determine the correct output.

**3.3 Invalid Chunk Data Package Witness (ICDPW):** If the contents of a chunk data package
doesn't match the hash provided inside the execution result, or the contents is invalid,
the Verification Nodes can report an Invalid Chunk Data Package Witness.

\*\*Adjudication: \*\*Consensus nodes evaluate the content of the chunk data package.
If the witness turns out to be valid, the Execution Node(s)
who signed the faulty chunk data package will get slashed.

**3.4 Missing Chunk Data Package Challenge (MCDPC):**
If an Execution Node doesn't respond to the chunk data package request by any staked Verification Node,
a Missing Chunk Data Package Challenge can be raised by the Verification Node.

\*\*Adjudication: \*\*When this challenge is received by the Consensus Nodes,
they contact Execution Nodes and ask for the chunk data package.
If none of the Execution Nodes respond after a long timeout, all of them get slashed.
If any of the Execution Nodes responds with a valid chunk data package,
Consensus Nodes redirect the chunk data package to the Verification Nodes
but will also set small penalties both for all the Execution Nodes and the challenge raiser
(Verification Node) according to their revenue ratio.

**3.5 Execution Results Timeout Challenge (ERTC):**
If no execution receipt received in X number of blocks after the submission of each block,
the liveness of the system is compromised and Consensus Nodes can raise
an Execution Results Timeout Challenge for all the Execution Nodes.

\*\*Adjudication: \*\*When this challenge is received by the Consensus Nodes,
they contact Execution Nodes and ask for an update. If none of the Execution Nodes respond
after a long timeout, all of them get slashed.
If any of the Execution Nodes return the execution receipt, the case is dismissed.

**3.6 Invalid Execution Receipt Witness (IERW):**
If an Execution Node provides an execution receipt that is not valid,
the Consensus Nodes can report an Invalid Execution Receipt Witness.

\*\*Adjudication: \*\*Consensus nodes evaluate the content of the execution receipt.
If the witness turns out to be valid, the Execution Node(s)
who signed the invalid execution receipt will get slashed.

\*\*3.7 Non-Matching SPoCKs Challenge (NMSC): \*\*
If the SPoCKs provided by the Execution Node don't match the ones provided by the Verification Node,
the Consensus Nodes can raise a Non-Matching SPoCKs challenge.

\*\*Adjudication: \*\*Consensus nodes have to re-execute the chunk
to be able to compute the accurate SPoCKs secret to be able to adjudicate the challenge.
This requires requesting the collection and all other data needed for execution from other nodes.
Any node which provided invalid SPoCKs will be slashed.

### 4. Verification Nodes[​](#4-verification-nodes "Direct link to 4. Verification Nodes")

**4.1 Non-Matching SPoCKs Challenge (NMSC):**
If the SPoCKs provided by the Execution Node don't match the ones provided by the Verification Node,
the Consensus Nodes can raise a Non-Matching SPoCKs challenge.

\*\*Adjudication: \*\*Consensus nodes have to re-execute the chunk to determine the accurate SPoCKs secret
which is needed to adjudicate the challenge. This requires requesting the collection
and all other data needed for execution from the other nodes.
Any node which provided invalid SPoCKs will be slashed.

**4.2 Invalid Result Approval Witness (IRAW):**
If a Verification Node provides an invalid result approval,
the Consensus Nodes can report this witness.
This includes cases that a Verification Node sends a result approval
for a chunk that was not assigned to the Verification Node (excluding full check mode)
or if the SPoCK’s signature doesn't match the public key of the Verification Node.

\*\*Adjudication: \*\*Consensus nodes evaluate the content and signatures of the result approval.
If the witness turns out to be valid, the Verification Node who signed that result approval be slashed.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/slashing.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)[Next

Node Providers](/networks/node-ops/node-operation/node-providers)

###### Rate this page

😞😐😊

* [Introduction](#introduction)
* [Slashing Conditions](#slashing-conditions)
* [Stages of Slashing](#stages-of-slashing)
  + [Phase 1: Beta](#phase-1-beta)
  + [Phase 2: Testing Slashing Mechanics](#phase-2-testing-slashing-mechanics)
  + [Phase 3: BFT](#phase-3-bft)
* [Slashing Challenges](#slashing-challenges)
  + [0. All Nodes](#0-all-nodes)
  + [1. Collection Nodes](#1-collection-nodes)
  + [2. Consensus Nodes](#2-consensus-nodes)
  + [3. Execution Nodes](#3-execution-nodes)
  + [4. Verification Nodes](#4-verification-nodes)

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