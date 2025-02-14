# Source: https://developers.flow.com/networks/node-ops/node-operation/node-migration




Node Migration | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* Node Migration
On this page
# Node Migration

There are a few different methods to migrate a running Flow node from one machine to the other.

Choose the method depending upon what part of the staking data of the node is changing.

### Method 1 - No change to the node staking data[​](#method-1---no-change-to-the-node-staking-data "Direct link to Method 1 - No change to the node staking data")

If there is no change to the network address or the staking and networking keys and only the hardware the node is running needs to be changed then do the following:

1. Stop the Flow node.
2. Copy over the bootstrap data (typically under `/var/flow/bootstrap`) which contains the node private key to the new machine.
3. Copy over the data folder (typically under `/var/flow/data`) which contains the state data.
4. Start the new node on the same network address as the old one.

warning

Please ensure that there is minimal downtime during this migration.


warning

The network address is currently part of the staking data that was submitted for the node. It is how other nodes in the network discover this node.
Hence, the network address of the node must stay the same between epochs otherwise the node will become unreachable for the other nodes and stop functioning.

### Method 2 - Network address change[​](#method-2---network-address-change "Direct link to Method 2 - Network address change")

A change to the node network address (IP or a hostname) can only be done during the spork process.

To change the networking address:

1. A day before the [upcoming mainnet spork](/networks/node-ops/node-operation/upcoming-sporks), change the network address for the nodes in Flow Port (using the update network address feature).
   The change will not take effect till an epoch transition happens.
2. Change the addresses in the `/var/flow/bootstrap/private-root-information/private-node-info_<nodeid>/node-info.priv.json` json file on the node.
3. A spork also causes an epoch transition, and the new addresses will take effect after the spork immediately.

### Method 3 - Staking or networking key change[​](#method-3---staking-or-networking-key-change "Direct link to Method 3 - Staking or networking key change")

If the node after migration will be using new staking or networking keys then it needs to be unstaked and then re-staked with the new keys.

1. Unstake the node via Flow Port.
2. Register the new node via Flow Port with the new staking information.
3. Run the new node with the new keys and network address. It should be able to join the network at the next epoch (see [timing](/networks/node-ops/node-operation/node-bootstrap#timing))

warning

Unstaking a node will result in the node [not earning rewards](/networks/staking/technical-overview#staking-operations-available-to-all-stakers) for the next epoch.
Delegators to the old node will have their tokens unstaked automatically. They will also stop earning rewards unless they withdraw their unstaked tokens and delegate them to a different node.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/node-migration.md)Last updated on **Jan 28, 2025** by **Giovanni Sanchez**[PreviousNode Economics](/networks/node-ops/node-operation/node-economics)[NextNode Provisioning](/networks/node-ops/node-operation/node-provisioning)
###### Rate this page

😞😐😊

* [Method 1 - No change to the node staking data](#method-1---no-change-to-the-node-staking-data)
* [Method 2 - Network address change](#method-2---network-address-change)
* [Method 3 - Staking or networking key change](#method-3---staking-or-networking-key-change)
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

