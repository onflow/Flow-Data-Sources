# Source: https://developers.flow.com/protocol/node-ops/node-operation/hcu

Height coordinated upgrade (HCU) | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          + [Access Nodes](/protocol/node-ops/access-nodes/access-node-setup)

            + [EVM Gateway Setup](/protocol/node-ops/evm-gateway/evm-gateway-setup)

              + [Light Nodes](/protocol/node-ops/light-nodes/observer-node)

                + [Participating in the Network](/protocol/node-ops/node-operation/faq)

                  - [Operator FAQ](/protocol/node-ops/node-operation/faq)- [Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)- [Database Encryption for Existing Node Operators](/protocol/node-ops/node-operation/db-encryption-existing-operator)- [Node Operations Guide](/protocol/node-ops/node-operation/guides/genesis-bootstrap)

                          - [Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)- [Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)- [Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)- [Node Economics](/protocol/node-ops/node-operation/node-economics)- [Node Migration](/protocol/node-ops/node-operation/node-migration)- [Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)- [Node Roles](/protocol/node-ops/node-operation/node-roles)- [Node Setup](/protocol/node-ops/node-operation/node-setup)- [Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)- [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade)- [Slashing Conditions](/protocol/node-ops/node-operation/slashing)- [Node Providers](/protocol/node-ops/node-operation/node-providers)- [Height coordinated upgrade](/protocol/node-ops/node-operation/hcu)- [Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)- [Managing disk space](/protocol/node-ops/node-operation/reclaim-disk)* [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Node Ops](/protocol/node-ops)* Participating in the Network* Height coordinated upgrade

On this page

# Height coordinated upgrade (HCU)

## Overview[​](#overview "Direct link to Overview")

To enables rapid development of the Flow Protocol, the height coordinated upgrade method is used to roll out non-breaking changes such as bug fixes,
feature implementations and security fixes.

## HCU versus Network Upgrade[​](#hcu-versus-network-upgrade "Direct link to HCU versus Network Upgrade")

A [Network Upgrade (spork)](/protocol/node-ops/node-operation/network-upgrade) requires a coordinated network upgrade process where node operators upgrade their node software and
re-initialize with a consolidated representation of the previous network upgrade's state.
It is used to roll out changes which may be non-backward compatible with respect to the protocol and the execution state.
Network upgrade entails a network downtime as all nodes in the system are upgraded and brought back online.
Network upgrades are only executed once every year.

A height coordinated upgrade (HCU) on the other hand allows the execution and the verification nodes to be upgraded without stopping the network.
There is no network downtime during an HCU but the transaction execution will stop for few minutes while the execution nodes restart.
Currently, an HCU is only used to update the execution and the verification nodes.
For other node types, a simple rolling upgrade is used where operators are asked to upgrade their nodes async.

## HCU process[​](#hcu-process "Direct link to HCU process")

The HCU is executed in two parts.

The first part is executed by the service committee. In this, the version boundary at which the execution nodes and verification nodes should stop is set on chain by submitting the [set\_version\_boundary](https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/admin/set_version_boundary.cdc) transaction.
The version boundary includes the block height at which the two node types should stop and the new node software version that the nodes should compare after a restart.

The second part is executed by the node operator. In this the node operator, monitors the execution and verification node that they are running. When the nodes reach the height set on chain, they stop if their version is lower then the version specified in the version boundary.
At this point, the operator should update the node version to the new node software version and start the node again. The node will continue from where it left off.

The block height and the node version will be announced by the Flow team on Discord as well as the [forum page](https://forum.onflow.org/c/mainnet-sporks/36).
It can also be directly queried from the chain using the following script.

`_10

TODO: insert flow cli command here to query the block version details.`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/hcu.md)

Last updated on **Sep 22, 2025** by **vishal**

[Previous

Node Providers](/protocol/node-ops/node-operation/node-providers)[Next

Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [HCU versus Network Upgrade](#hcu-versus-network-upgrade)* [HCU process](#hcu-process)

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