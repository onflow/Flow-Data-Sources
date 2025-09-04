# Source: https://developers.flow.com/protocol/node-ops/node-operation/reclaim-disk

Managing disk space | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)
* [Networks](/protocol)
* [Flow Network Architecture](/protocol/network-architecture)
* [Staking and Epochs](/protocol/staking)
* [Node Ops](/protocol/node-ops)

  + [Access Nodes](/protocol/node-ops/access-nodes/access-node-setup)
  + [EVM Gateway Setup](/protocol/node-ops/evm-gateway/evm-gateway-setup)
  + [Light Nodes](/protocol/node-ops/light-nodes/observer-node)
  + [Participating in the Network](/protocol/node-ops/node-operation/faq)

    - [Operator FAQ](/protocol/node-ops/node-operation/faq)
    - [Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)
    - [Database Encryption for Existing Node Operators](/protocol/node-ops/node-operation/db-encryption-existing-operator)
    - [Node Operations Guide](/protocol/node-ops/node-operation/guides/genesis-bootstrap)
    - [Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)
    - [Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)
    - [Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)
    - [Node Economics](/protocol/node-ops/node-operation/node-economics)
    - [Node Migration](/protocol/node-ops/node-operation/node-migration)
    - [Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)
    - [Node Roles](/protocol/node-ops/node-operation/node-roles)
    - [Node Setup](/protocol/node-ops/node-operation/node-setup)
    - [Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)
    - [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/spork)
    - [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
    - [Slashing Conditions](/protocol/node-ops/node-operation/slashing)
    - [Node Providers](/protocol/node-ops/node-operation/node-providers)
    - [Height coordinated upgrade](/protocol/node-ops/node-operation/hcu)
    - [Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)
    - [Managing disk space](/protocol/node-ops/node-operation/reclaim-disk)
* [Accessing Data](/protocol/access-onchain-data)
* [Governance](/protocol/governance)
* [Flow Port](/protocol/flow-port)

* [Node Ops](/protocol/node-ops)
* Participating in the Network
* Managing disk space

On this page

# Managing disk space

As the chain advances, nodes receive chain data and store it on disk.
Hence, the disk usage of a node keeps increasing gradually over time.

In addition to this, currently nodes also experience an intermittent 30-35% spike in disk usage caused by the compaction process of the Badger database used by the node software.

> The spikes will be eliminated once the Badger database is replaced by the Pebble database in the future.

Hence, as a node operator, please make sure to do the following:

1. Provision enough disk space as per the node role (see: [node-provisioning](/protocol/node-ops/node-operation/node-provisioning))
2. Setup disk usage monitoring and ensure that the node has enough room to grow and to also accommodate those intermittent spikes.
3. If needed, please add more disk space to the node from time to time.

> It highly recommended to setup alerting around disk usage to facilitate timely action and avoid any downtime and subsequent reward slashing for the node.

## Reclaiming disk space[​](#reclaiming-disk-space "Direct link to Reclaiming disk space")

### Access, Collection, Consensus and Verification node[​](#access-collection-consensus-and-verification-node "Direct link to Access, Collection, Consensus and Verification node")

If you are running any node other than an execution node and the node is close to running out of disk space or has already exhausted all of its disk, you can re-bootstrap the node's database. This frees up disk space by discarding historical data past a certain threshold.

1. Stop the node.
2. Back up the data folder to a tmp folder in case it is required to revert this change. The default location of the data folder is `/var/flow/data` unless overridden by the `--datadir` flag.

`_10

mv /var/flow/data /var/flow/data_backup`

3. Configure the node to bootstrap from a new, more recent Root Snapshot. You may use either of the two methods described [here](/protocol/node-ops/node-operation/protocol-state-bootstrap) to configure your node.
4. Start the node. The node should now recreate the data folder and start fetching blocks.
5. If the node is up and running OK, delete the `data_backup` folder created in step 2.

`_10

rm -rf /var/flow/data_backup`

#### Limitation for Access Node[​](#limitation-for-access-node "Direct link to Limitation for Access Node")

Re-bootstrapping allows the node to be restarted at a particular block height by deleting all the previous state.

For an **Access Node**, this results in the node not being able to serve any API request before the height at which the node was re-bootstrapped.

*Hence, if you require the access node to serve data from the start of the last network upgrade (spork), do not use this method of reclaiming disk space. Instead provision more disk for the node.*

### Execution node[​](#execution-node "Direct link to Execution node")

For an execution node, the chunk data directory is the one that takes up most of the space. To reclaim space on an execution, do the following:

1. Stop the Execution Node.
2. Remove the Chunk Data Pack Directory. The default is `/var/flow/data/chunk_data_pack` unless overridden by the `chunk-data-pack-dir` parameter.

   Do **not** delete the bootstrap folder.

   `rm -rf /var/flow/data/chunk_data_pack`
3. Start the Execution Node.

Upon restart, the chunk data pack directory will be automatically recreated.

> Note: Always exercise caution when performing system operations, and make sure you have a backup of important data before making any changes.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/reclaim-disk.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)[Next

Access API](/protocol/access-onchain-data)

###### Rate this page

😞😐😊

Copy as Markdown

* [Reclaiming disk space](#reclaiming-disk-space)
  + [Access, Collection, Consensus and Verification node](#access-collection-consensus-and-verification-node)
  + [Execution node](#execution-node)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.