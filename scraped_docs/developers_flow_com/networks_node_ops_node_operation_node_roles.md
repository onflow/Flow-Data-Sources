# Source: https://developers.flow.com/networks/node-ops/node-operation/node-roles

Node Roles | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
    - [Past Spork Info](/networks/node-ops/node-operation/past-sporks)
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
* Node Roles

On this page

# Node Roles

Unlike most blockchains, not all Flow nodes are equal. Flow nodes all specialize and fulfill a specific role in the operation of the network.
Collection, consensus, execution, verification and access nodes are all staked nodes while the observer node is not staked.

## Collection[​](#collection "Direct link to Collection")

Collection nodes are bandwidth-optimized nodes divided by the protocol into several cooperating Clusters. Their first task is managing the transaction pool and collecting well-formed transactions to propose to Consensus nodes. Transactions are assigned to a cluster pseudorandomly by transaction hash. A well-formed transaction must include credentials from the guarantor of the transaction. When a Collection Node sees a well-formed transaction, it hashes the text of that transaction and signs the transaction to indicate two things: first, that it is well-formed; and second, that it will commit to storing the transaction text until the Execution nodes have finished processing it. Each cluster collects transactions, assembles them into Collections and submits a Collection Guarantee signed by a super-majority of the cluster to the Consensus nodes.

Collection nodes are required to stake a minimum of 250,000 FLOW to be a confirmed node operator.

## Consensus[​](#consensus "Direct link to Consensus")

Consensus nodes form and propose blocks in a manner similar to traditionally-structured proof-of-stake blockchains, using the HotStuff consensus algorithm to create a globally consistent chain of blocks. Consensus nodes validate that the signed collection hashes submitted to them by Collection nodes were, in fact, signed by the required majority of Collection nodes. Thereafter, the Consensus nodes assemble the transactions into blocks and finalize them through voting.
The more participants there are in this process, the more decentralized the network. However, consensus algorithms typically bottleneck the limit to the number of participants. The Flow protocol chose the HotStuff algorithm because it is flexible enough to add participants and currently supports about 100 operators. Adding more than 100 participants to the protocol by adapting HotStuff will continue to be an area of active development.

Consensus nodes act as checkpoints against other Collection nodes. They are responsible for checking that a critical number of Collection nodes reviewed and signed for the transaction. Collection nodes are held accountable by Consensus nodes. A common concern with proof-of-work- and proof-of-stake based systems is that a small subset of the population of nodes can control important resources such as the mining or stake needed to produce and vote on blocks, which is a degradation of the security of the system. By lowering the requirements to participate, Flow makes it extremely difficult and expensive to coordinate a Byzantine majority of Consensus nodes.

Consensus nodes have minimal bandwidth and computation requirements, allowing even a modest computing device (any consumer-grade hardware) to participate in the voting process and ensure the safety of the network. Many networks claim open participation, yet substantial resources — stake, computation, or otherwise — are needed to partake. Maintaining such barriers to entry undermines the security of the network. Lowering the participation requirements preserves the security of the network by providing a high degree of byzantine fault tolerance since it becomes exceedingly difficult for a subset of bad actors to subvert the network.

Consensus nodes are required to stake a minimum of 500,000 FLOW to be a confirmed node operator.

## Execution[​](#execution "Direct link to Execution")

Execution nodes are the most resource-intensive nodes on the Flow network, responsible for executing transactions and maintaining the Execution State — a cryptographically-verifiable data store for all user accounts and smart contract states — as well as responding to queries related to it. Execution nodes compute the outputs of the blocks they are provided. They then ask the Collection nodes for the collections which contain transactions waiting to be executed. With this data they are able to compute the output, which is later verified by Verification nodes to ensure honesty (allocation of Verification nodes is via a sortition algorithm). The Execution nodes are primarily responsible for Flow's improvements in scale and efficiency because only a very small number of these powerful compute resources are required to compute and store the historical state.

Execution nodes give the Flow network its performance characteristics: highly scalable within a single shared state environment (i.e., no sharding). However, the significant hardware requirements make them the least accessible option for participation as a Validator. Because the revenue pool splits between relatively few nodes, the revenue per-node should more than compensate for the high capital costs of operating this node.

An Execution Node presents a hashed commitment once it has computed the output. The output is only revealed once its co-executors have also submitted their outputs. This is important to ensure nodes aren't spoofing each other's work. Once they've all submitted their answers, the output is revealed and subjected to random queries and checks run by Verification nodes. The Execution nodes have relatively low byzantine fault tolerance. However, this does not compromise the overall security of the system because the process they perform is deterministic -- any bad actor will easily be detected and punished by Verification nodes.

This relatively small group of nodes has the most substantial technical requirements for processor speed and bandwidth because they are tasked with all the computations necessary to determine the output of the network. Allowing for this degree of specialization can reduce computation costs by at least one thousand times, and possibly much more, when compared to Ethereum.

Execution nodes are required to stake a minimum of 1,250,000 FLOW to be a confirmed node operator.

## Verification[​](#verification "Direct link to Verification")

Verification nodes are responsible for confirming the correctness of the work done by Execution nodes. Individual Verification nodes only check a small amount of the total computation, but collectively they check every computation many times in parallel. Verification nodes verify Execution Receipts provided by Execution nodes and issue Result Approvals. A sortition algorithm determines which chunks of the Execution Receipt from the Execution nodes the Verification Node must query to check they were computed correctly. Ultimately, these nodes keep the Execution nodes honest; this balance of power maintains the access, security, and verifiability criteria of decentralization. It is highly byzantine fault tolerant because even if there is a substantial number of byzantine errors in the Verification Node
pool, the Consensus nodes are still required to approve that transactions they signed were reviewed by a critical amount of the network.

Verification nodes are required to stake a minimum of 135,000 FLOW to be a confirmed node operator.

## Access[​](#access "Direct link to Access")

Access nodes act as a proxy to the Flow network. The Access node routes transactions to the correct collection node and routes state queries to execution nodes (while likely caching state to answer queries in a timely manner in the future). Clients submit their transactions to any Access node or run their own if they can't find a service provider they're happy with.

Access nodes are required to stake 100 FLOW to be a confirmed node operator. However, since an access node does not participate in block production, it does not receive any staking rewards.

## Observer[​](#observer "Direct link to Observer")

An observer node provides locally accessible, continuously updated, verified copy of the block data. It serves the Access API but unlike an access node, an observer node does not need to be staked, and **anyone** can run it without being added to the approved list of nodes.

[Get started running an observer node](/networks/node-ops/light-nodes/observer-node)

## 

Here is a comparison of the different node roles,

| Role | Staked | Recives Rewards | Permissioned |
| --- | --- | --- | --- |
| Collection | Yes | Yes | Yes |
| Consensus | Yes | Yes | Yes |
| Execution | Yes | Yes | Yes |
| Verification | Yes | Yes | Yes |
| Access | Yes | No | No 🆕 |
| Observer | No | No | No |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/node-roles.md)

Last updated on **Feb 27, 2025** by **Chase Fleming**

[Previous

Node Provisioning](/networks/node-ops/node-operation/node-provisioning)[Next

Node Setup](/networks/node-ops/node-operation/node-setup)

###### Rate this page

😞😐😊

* [Collection](#collection)
* [Consensus](#consensus)
* [Execution](#execution)
* [Verification](#verification)
* [Access](#access)
* [Observer](#observer)

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