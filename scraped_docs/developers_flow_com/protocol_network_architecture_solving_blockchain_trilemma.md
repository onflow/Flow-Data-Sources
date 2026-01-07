# Source: https://developers.flow.com/protocol/network-architecture/solving-blockchain-trilemma

Solving the blockchain trilemma | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      + [Solving the blockchain trilemma](/protocol/network-architecture/solving-blockchain-trilemma)+ [Sustainability](/protocol/network-architecture/sustainability)+ [User safety](/protocol/network-architecture/user-safety)* [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Flow Network Architecture](/protocol/network-architecture)* Solving the blockchain trilemma

On this page

# Solving the blockchain trilemma

In a monolithic architecture, all nodes perform every task. As network usage grows, the transaction processing capacity of the individual nodes becomes a limiting factor, restricting the network’s throughput and latency. The amount of data that can be stored onchain is limited since nodes have a finite storage capacity. The only way to scale monolithic blockchains is by increasing the capacity of each node by adding more CPU, memory, and storage (i.e. vertical scaling, an approach taken by Solana). However, this solution comes at the cost of decentralization. As nodes scale vertically, they become more expensive to run, and eventually, only a few operators can afford to run such high-performance, high-capacity nodes. Worse, energy consumption for every node in the network increases over time, making the chain environmentally unsustainable.

Through its multi-role architecture, Flow implements a modular pipeline for processing transactions. This design allows the network to scale by tuning the level of decentralization at each specific step without sharding the state and fragmenting the network into smaller security zones.

The modular pipeline is composed of Collection, Consensus, Execution and Verification Nodes.

![pipeline](/assets/images/pipeline-42512db6ead17a2b6aaf1787c1960f57.png)

## Separating Consensus from Compute[​](#separating-consensus-from-compute "Direct link to Separating Consensus from Compute")

At a high level, the pipeline essentially separates consensus from transaction computation. Non-deterministic (or “subjective”) processes such as determining the inclusion and order of transactions are decided by the broadly decentralized consensus committee. The deterministic (or “objective”) task of computing the result of those ordered transactions is done independently by a small number of specialized execution nodes.

Collection and consensus are highly decentralized and achieve high levels of redundancy through a large number of lightweight, cost-effective nodes, numbering in the thousands, operated by several hundred different operators. These steps guarantee resilient transaction ordering (assuming that a malicious actor can only compromise a limited number of nodes).

In comparison, transaction execution has low decentralization and redundancy (10 or less) with more powerful and expensive nodes. To accommodate for the anticipated growth of onchain state without sharding, only the execution nodes have to be scaled vertically. All other node types can continue to run low-cost hardware. The execution nodes may eventually be scaled up to small data centers.

![scaling_flow](/assets/images/scaling_flow-2190d3c5db523859d376bfa600532445.png)

Low decentralization for transaction execution might appear to compromise decentralization of the whole network, as it is conceivable that a malicious actor might compromise a dominant fraction of nodes participating in execution. However, correctness of the transaction results is still guaranteed by the verification step, which also requires reasonably high redundancy, again with a large number of lighter and less expensive verification nodes to withstand compromisation attempts.

Every node in Flow makes the protocol stronger, and the network can grow as needed to achieve different objectives:

* More censorship resistance? Add more collection nodes
* More decentralized block production? Add more consensus nodes
* Need to accommodate higher transaction throughput and state storage? Scale up execution nodes
* Do node operators want to reinforce network security with modest node hardware and low stake? Add more verification nodes.
* Need access to chain data locally? Add access nodes.

In contrast, when traditional Layer 1 blockchains add more nodes to increase decentralization, they do so without providing any additional benefits.

![verying_redundancy](/assets/images/varying_redudancy-5d4e1110d859c415d773d24a8e6b1ff3.png)

> Flow’s architectural goals are to provide a throughput of at least 1M TPS, ingest at least ½ GB of transaction data per second and store and serve a very large state of one Patebyte and beyond.

Thus, Flow’s multi-role architecture solves the blockchain trilemma:

1. **Scalability**: Scale to thousands of times higher throughput and onchain storage capacity.
2. **Decentralization**: Except for the execution nodes, all nodes are light weight and low cost, lowering the barrier to entry and ensuring participation from a diverse set of node operators—big and small
3. **Security**: Maintain a shared non-sharded execution environment for all operations on the network and use a secure in-built platform to build on.

![trilemma_solved](/assets/images/flow_trillema_solved-1ba96289ea436ee41ca530f58ec8b558.png)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/network-architecture/solving-blockchain-trilemma.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Flow Network Architecture](/protocol/network-architecture)[Next

Sustainability](/protocol/network-architecture/sustainability)

###### Rate this page

😞😐😊

Copy as Markdown

* [Separating Consensus from Compute](#separating-consensus-from-compute)

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