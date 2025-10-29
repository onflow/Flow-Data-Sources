# Source: https://developers.flow.com/protocol/node-ops

Node Operations | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          + [Access Nodes](/protocol/node-ops/access-nodes/access-node-setup)

            + [EVM Gateway Setup](/protocol/node-ops/evm-gateway/evm-gateway-setup)

              + [Light Nodes](/protocol/node-ops/light-nodes/observer-node)

                + [Participating in the Network](/protocol/node-ops/node-operation/faq)* [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * Node Ops

On this page

# Hello Node Operator!

Flow nodes are vital components of the Flow blockchain. These nodes are responsible for a variety of network operations to maintain the distributed ledger.

## Why Run a Node?[​](#why-run-a-node "Direct link to Why Run a Node?")

---

By running your own node, you have direct access to the evolving state of the network, without having to rely on third parties.
This increases privacy and security, reduces reliance on external servers, and helps balance load distribution.
By running a node, you also directly contribute to the security and decentralization of the whole network.

Flow multirole architecture makes it more scalable and provides several node types that you as a node operator can pick and choose from.

## Which Node Should You Run?[​](#which-node-should-you-run "Direct link to Which Node Should You Run?")

---

The different types of nodes are described [here](/protocol/node-ops/node-operation/node-roles). As node operator, you can choose to run any of the different types of node that best fits your needs.

The nodes are classified as follows,

![Flownodesdiagram.png](/assets/images/Flownodesdiagram-1eefd3617fcc0ba8e4610960b1c8ce35.png)

## Light Node A.K.A. Observer Node[​](#light-node-aka-observer-node "Direct link to Light Node A.K.A. Observer Node")

---

The light node is one of the easiest nodes to spin up and can be run by Dapp developers who need the latest block data available locally, e.g. a wallet application that needs to track the latest block ID and height.
In addition to supporting dapps, an observer node can also be run by access node operators who want to scale their access nodes' endpoints. Access node operators can spin up geographically dispersed observer nodes which can talk to their staked access nodes and to each other.

The observer node is not staked but still provides the same API as the access node.

info

To run a light node, follow this [guide](/protocol/node-ops/light-nodes/observer-node)

## Full Node[​](#full-node "Direct link to Full Node")

---

In a nutshell, Full Nodes are staked network participants that drive network progress, e.g. by creating and executing new blocks. They are the primary contributors to network safety (all of them validate the correctness of the consensus process and secure the network additionally through their role-specific tasks). In comparison, Light Nodes don't contribute to the networks progress. Though, they help to secure the network by also validating the integrity of the consensus process.

* The Access node is a full node that serves as an RPC node and acts as a gateway node for the network.
* The Validator node (Collection, Consensus, Verification and Execution) is a full node that plays a role in block generation.

### Access Node[​](#access-node "Direct link to Access Node")

---

If you want local access to the protocol state data (blocks, collections, transactions) and do not want to use one of the community access nodes you can run an access node.
Dapp developers, chain explorers, chain analytics and others who want exclusive access to chain data and not be subject to the rate-limits on the community access node can choose to run an access node.

An access node is minimally staked for network security.
The central goal for Access Nodes is to provide RPC functionality to its node operator.
In comparison, contributing to protocol progress (e.g. routing transactions to collector clusters, relaying blocks to the unstaked peer-to-peer network, etc.) should only take up a marginal fraction an Access Node's computational resources.
Furthermore, Access Node operators can freely rate-limit the amount of resources their Access Node dedicates to supporting the broader ecosystem. Therefore, Access Nodes do not receive staking rewards.

info

Launch an access node using QuickNode

<https://www.quicknode.com/chains/flow>

info

To run a self-hosted access node, follow this [guide](/protocol/node-ops/access-nodes/access-node-setup)

tip

Alternately, instead of running an access node, you can use the [Flow community](/protocol/access-onchain-data) access nodes or the ones run by any of the other node operators.

### Validator Node[​](#validator-node "Direct link to Validator Node")

---

You can also be a core participant in running the Flow network and contribute to securing it. Depending on your preference, you could run one or any combination of the following node roles:

* Collection Nodes collaboratively create batches of transactions (in Flow terminology collections).
* Consensus Nodes create blocks, schedule them for asynchronous execution, and commit execution results once they are verified (so called sealing). In addition, they orchestrate the Flow protocol and enforce protocol compliance.
* Execution Nodes asynchronously execute blocks. They are the power-houses in the protocol, providing the vast computational resources available to Flow transactions.
* Verification Nodes check the execution results in a distributed manner.

Nodes with these roles are staked and also receive staking rewards.

### Running a Staked Node[​](#running-a-staked-node "Direct link to Running a Staked Node")

---

To run a staked node (node type access, collection, consensus, verification or execution) the node must:

* be registered with sufficient stake
* be authorized by the governance working group

Before proceeding, ensure you have the stake required for your new node and that your node will be authorized by the governance working group (apply [here](https://github.com/onflow/flow-validator)).

To set up a new staked node after it has been authorized by the Flow governance working group, you will need to complete the following steps:

1. [Provision](/protocol/node-ops/node-operation/node-setup) the machine on which your node will run.
2. [Generate and register](/protocol/node-ops/node-operation/node-bootstrap) your node identity.
3. [Start](/protocol/node-ops/node-operation/node-bootstrap#step-3---start-your-flow-node) your node!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/index.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Staking Collection Guide](/protocol/staking/staking-collection)[Next

Access Node Setup](/protocol/node-ops/access-nodes/access-node-setup)

###### Rate this page

😞😐😊

Copy as Markdown

* [Why Run a Node?](#why-run-a-node)* [Which Node Should You Run?](#which-node-should-you-run)* [Light Node A.K.A. Observer Node](#light-node-aka-observer-node)* [Full Node](#full-node)
        + [Access Node](#access-node)+ [Validator Node](#validator-node)+ [Running a Staked Node](#running-a-staked-node)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.