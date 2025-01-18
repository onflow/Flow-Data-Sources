# Source: https://developers.flow.com/networks/node-ops/node-operation/reclaim-disk




Managing disk space | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
  + [Accessing On-chain Data](/networks/node-ops/access-onchain-data/access-nodes/access-node-setup)
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
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)


* [Node Ops](/networks/node-ops)
* Participating in the Network
* Managing disk space
On this page
# Managing disk space

As the chain advances, nodes receive chain data and store it on disk.
Hence, the disk usage of a node keeps increasing gradually over time.

In addition to this, currently nodes also experience an intermittent 30-35% spike in disk usage caused by the compaction process of the Badger database used by the node software.

> The spikes will be eliminated once the Badger database is replaced by the Pebble database in the future.

Hence, as a node operator, please make sure to do the following:

1. Provision enough disk space as per the node role (see: [node-provisioning](/networks/node-ops/node-operation/node-provisioning))
2. Setup disk usage monitoring and ensure that the node has enough room to grow and to also accommodate those intermittent spikes.
3. If needed, please add more disk space to the node from time to time.

> It highly recommended to setup alerting around disk usage to facilitate timely action and avoid any downtime and subsequent reward slashing for the node.

## Reclaiming disk space[​](#reclaiming-disk-space "Direct link to Reclaiming disk space")

### Access, Collection, Consensus and Verification node[​](#access-collection-consensus-and-verification-node "Direct link to Access, Collection, Consensus and Verification node")

If you are running any node other than an execution node and the node is close to running out of disk space or has already exhausted all of its disk, you can re-bootstrap the node's database. This frees up disk space by discarding historical data past a certain threshold.

1. Stop the node.
2. Back up the data folder to a tmp folder in case it is required to revert this change. The default location of the data folder is `/var/flow/data` unless overridden by the `--datadir` flag.

 `_10mv /var/flow/data /var/flow/data_backup`

3. Configure the node to bootstrap from a new, more recent Root Snapshot. You may use either of the two methods described [here](/networks/node-ops/node-operation/protocol-state-bootstrap) to configure your node.
4. Start the node. The node should now recreate the data folder and start fetching blocks.
5. If the node is up and running OK, delete the `data_backup` folder created in step 2.

 `_10rm -rf /var/flow/data_backup`
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/reclaim-disk.md)Last updated on **Dec 20, 2024** by **Brian Doyle**[PreviousProtocol State Bootstrapping](/networks/node-ops/node-operation/protocol-state-bootstrap)[NextGovernance](/networks/governance)
###### Rate this page

😞😐😊

* [Reclaiming disk space](#reclaiming-disk-space)
  + [Access, Collection, Consensus and Verification node](#access-collection-consensus-and-verification-node)
  + [Execution node](#execution-node)
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
* [Flowdiver Mainnet](https://flowdiver.io/)
* [Flowdiver Testnet](https://testnet.flowdiver.io/)
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

