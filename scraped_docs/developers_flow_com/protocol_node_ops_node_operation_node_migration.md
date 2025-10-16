# Source: https://developers.flow.com/protocol/node-ops/node-operation/node-migration

Node Migration | Flow Developer Portal



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

                + [Participating in the Network](/protocol/node-ops/node-operation/faq)

                  - [Operator FAQ](/protocol/node-ops/node-operation/faq)- [Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)- [Database Encryption for Existing Node Operators](/protocol/node-ops/node-operation/db-encryption-existing-operator)- [Node Operations Guide](/protocol/node-ops/node-operation/guides/genesis-bootstrap)

                          - [Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)- [Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)- [Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)- [Node Economics](/protocol/node-ops/node-operation/node-economics)- [Node Migration](/protocol/node-ops/node-operation/node-migration)- [Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)- [Node Roles](/protocol/node-ops/node-operation/node-roles)- [Node Setup](/protocol/node-ops/node-operation/node-setup)- [Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)- [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade)- [Slashing Conditions](/protocol/node-ops/node-operation/slashing)- [Node Providers](/protocol/node-ops/node-operation/node-providers)- [Height coordinated upgrade](/protocol/node-ops/node-operation/hcu)- [Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)- [Managing disk space](/protocol/node-ops/node-operation/reclaim-disk)* [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Node Ops](/protocol/node-ops)* Participating in the Network* Node Migration

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

1. A day before the upcoming mainnet spork, change the network address for the nodes in Flow Port (using the update network address feature).
   The change will not take effect till an epoch transition happens.
2. Change the addresses in the `/var/flow/bootstrap/private-root-information/private-node-info_<nodeid>/node-info.priv.json` json file on the node.
3. A spork also causes an epoch transition, and the new addresses will take effect after the spork immediately.

### Method 3 - Staking or networking key change[​](#method-3---staking-or-networking-key-change "Direct link to Method 3 - Staking or networking key change")

If the node after migration will be using new staking or networking keys then it needs to be unstaked and then re-staked with the new keys.

1. Unstake the node via Flow Port.
2. Register the new node via Flow Port with the new staking information.
3. Run the new node with the new keys and network address. It should be able to join the network at the next epoch (see [timing](/protocol/node-ops/node-operation/node-bootstrap#timing))

warning

Unstaking a node will result in the node [not earning rewards](/protocol/staking/technical-overview#staking-operations-available-to-all-stakers) for the next epoch.
Delegators to the old node will have their tokens unstaked automatically. They will also stop earning rewards unless they withdraw their unstaked tokens and delegate them to a different node.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/node-migration.md)

Last updated on **Sep 12, 2025** by **Vishal**

[Previous

Node Economics](/protocol/node-ops/node-operation/node-economics)[Next

Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)

###### Rate this page

😞😐😊

Copy as Markdown

* [Method 1 - No change to the node staking data](#method-1---no-change-to-the-node-staking-data)* [Method 2 - Network address change](#method-2---network-address-change)* [Method 3 - Staking or networking key change](#method-3---staking-or-networking-key-change)

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