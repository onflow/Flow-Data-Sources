# Source: https://developers.flow.com/networks/node-ops/node-operation/hcu

Height coordinated upgrade (HCU) | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* Height coordinated upgrade

On this page

# Height coordinated upgrade (HCU)

## Overview[​](#overview "Direct link to Overview")

To enables rapid development of the Flow Protocol, the height coordinated upgrade method is used to roll out non-breaking changes such as bug fixes,
feature implementations and security fixes.

## HCU versus Spork[​](#hcu-versus-spork "Direct link to HCU versus Spork")

A [spork](/networks/node-ops/node-operation/spork) requires a coordinated network upgrade process where node operators upgrade their node software and
re-initialize with a consolidated representation of the previous spork's state.
It is used to roll out changes which may be non-backward compatible with respect to the protocol and the execution state.
Spork entails a network downtime as all nodes in the system are upgraded and brought back online.
Sporks are only executed once every quarter.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/hcu.md)

Last updated on **Mar 28, 2025** by **Jordan Ribbink**

[Previous

Node Providers](/networks/node-ops/node-operation/node-providers)[Next

Protocol State Bootstrapping](/networks/node-ops/node-operation/protocol-state-bootstrap)

###### Rate this page

😞😐😊

* [Overview](#overview)
* [HCU versus Spork](#hcu-versus-spork)
* [HCU process](#hcu-process)

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