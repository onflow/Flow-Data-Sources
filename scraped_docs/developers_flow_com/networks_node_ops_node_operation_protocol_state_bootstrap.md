# Source: https://developers.flow.com/networks/node-ops/node-operation/protocol-state-bootstrap

Protocol State Bootstrapping | Flow Developer Portal



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
* Protocol State Bootstrapping

On this page

# Protocol State Bootstrapping

When a node joins the network, it bootstraps its local database using a trusted initialization file, called a Root Snapshot.
Most node operators will use the `Spork Root Snapshot` file distributed during the [spork process](/networks/node-ops/node-operation/spork).
This page will explain how the bootstrapping process works and how to use it in general.

For guides covering specific bootstrapping workflows, see:

* [Node Bootstrap](/networks/node-ops/node-operation/node-bootstrap) for bootstrapping a newly joined node.
* [Reclaim Disk](/networks/node-ops/node-operation/reclaim-disk) for bootstrapping from a recent snapshot to recover disk space.

info

This page covers only Protocol State bootstrapping and applies to Access, Collection, Consensus, & Verification Nodes.
Execution Nodes also need to bootstrap an Execution State database, which is not covered here.

## Node Startup[​](#node-startup "Direct link to Node Startup")

When a node starts up, it will first check its database status.
If its local database is already bootstrapped, it will start up and begin operating.
If its local database is not already bootstrapped, it will attempt to bootstrap using a Root Snapshot.

There are two sources for a non-bootstrapped node to obtain a Root Snapshot:

1. Root Snapshot file in the `bootstrap` folder
2. Dynamic Startup flags, which will cause the node to download a Root Snapshot from a specified Access Node

The node software requires that only one of the above options is provided.

## Using a Root Snapshot File[​](#using-a-root-snapshot-file "Direct link to Using a Root Snapshot File")

info

If your node already has a bootstrapped database, the Root Snapshot file will be ignored. If both a Root Snapshot and Dynamic Startup flags are present, the node will not startup.

Using a Root Snapshot file is more flexible but more involved for operators compared to Dynamic Startup.

A file in `$BOOTDIR/public-root-information` named `root-protocol-state-snapshot.json` will be read and used as the Root Snapshot for bootstrapping the database.

### Instructions[​](#instructions "Direct link to Instructions")

1. Obtain a Root Snapshot file (see below for options)
2. Ensure your node is stopped and does not already have a bootstrapped database.
3. Move the Root Snapshot file to `$BOOTDIR/public-root-information/root-protocol-state-snapshot.json`, where `$BOOTDIR` is the value passed to the `--bootstrapdir` flag.
4. Start your node.

### Obtain Root Snapshot File using Flow CLI[​](#obtain-root-snapshot-file-using-flow-cli "Direct link to Obtain Root Snapshot File using Flow CLI")

[Flow CLI](/tools/flow-cli) supports downloading the most recently sealed Root Snapshot from an Access Node using the [`flow snapshot save`](/tools/flow-cli/utils/snapshot-save) command.

When using this method:

* ensure you connect to an Access Node you operate or trust
* ensure you use the [`--network-key`](/tools/flow-cli/utils/snapshot-save#network-key) flag so the connection is encrypted

### Obtain Root Snapshot File from Protocol database[​](#obtain-root-snapshot-file-from-protocol-database "Direct link to Obtain Root Snapshot File from Protocol database")

If you have an existing node actively participating in the network, you can obtain a Root Snapshot using its database.

1. Obtain a copy of the Flow `util` tool and ensure it is in your `$PATH`. This tool is distributed during sporks, or you can build a copy from [here](https://github.com/onflow/flow-go/tree/master/cmd/util).
2. Stop the existing node.
3. Construct a Root Snapshot using the `util` tool. The tool will print the JSON representation to STDOUT, so you can redirect the output to a file.

Replace `$DATADIR` with the value passed to the `--datadir` flag. You can specify the desired reference block for the snapshot.

Retrieve the snapshot for the latest finalized block:

`_10

util read-protocol-state snapshot -d $DATADIR --final > latest-finalized-snapshot.json`

Retrieve the snapshot for a specific finalized block height:

`_10

util read-protocol-state snapshot -d $DATADIR --height 12345 > specific-height-snapshot.json`

## Using Dynamic Startup[​](#using-dynamic-startup "Direct link to Using Dynamic Startup")

Dynamic Startup is a startup configuration where your node will download a Root Snapshot and use it to bootstrap its local database.
Dynamic Startup is designed for nodes which are newly joining the network and need to [bootstrap from within a specific epoch phase](/networks/node-ops/node-operation/node-bootstrap#timing), but can be used for other use-cases.

info

If your node already has a bootstrapped database, Dynamic Startup flags will be ignored. If both a Root Snapshot and Dynamic Startup flags are present, the node will not startup.

When using Dynamic Startup, we specify:

1. An Access Node to retrieve the snapshot from.
2. A target epoch counter and phase to wait for.

After startup, your node will periodically download a candidate Root Snapshot from the specified Access Node.
If the Root Snapshot's reference block is either **within or after** the specified epoch phase, the node will bootstrap using that snapshot.
Otherwise the node will continue polling until it receives a valid Root Snapshot.

See the [Epochs Schedule](/networks/staking/schedule) for additional context on epoch phases.

### Specifying an Access Node[​](#specifying-an-access-node "Direct link to Specifying an Access Node")

Two flags are used to specify which Access Node to connect to:

* `--dynamic-startup-access-address` - the Access Node's secure GRPC server address
* `--dynamic-startup-access-publickey` - the Access Node's networking public key

Select an Access Node you operate or trust to provide the Root Snapshot, and populate these two flags.

For example, to use the Access Node maintained by the Flow Foundation for Dynamic Startup, specify the following flags:

ExampleDynamicStartupFlags

`_10

... \

_10

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_10

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae`

### Specifying an Epoch Phase[​](#specifying-an-epoch-phase "Direct link to Specifying an Epoch Phase")

Two flags are used to specify when to bootstrap:

* `--dynamic-startup-epoch-phase` - the epoch phase to start up in (default `EpochPhaseSetup`)
* `--dynamic-startup-epoch` - the epoch counter to start up in (default `current`)

> You can check the current epoch phase of the network by running [this](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_phase.cdc) script. Alternatively, you can also check the current epoch phase [here](https://dashboard.flow.com/) under Epoch Phase.

#### Bootstrapping Immediately[​](#bootstrapping-immediately "Direct link to Bootstrapping Immediately")

If you would like to bootstrap immediately, using the first Root Snapshot you receive, then specify a past epoch counter:

ExampleDynamicStartupFlags

`_10

... \

_10

--dynamic-startup-epoch-phase=1`

You may omit the `--dynamic-startup-epoch-phase` flag.

### Instructions[​](#instructions-1 "Direct link to Instructions")

#### Example 1[​](#example-1 "Direct link to Example 1")

Use Dynamic Startup to bootstrap your node at the `Epoch Setup Phase` of the current epoch (desired behaviour for newly joining nodes):

1. Ensure your database is not already bootstrapped, and no Root Snapshot file is present in the `$BOOTSTRAPDIR` folder.
2. Add necessary flags to node startup command.
   For example, using the Flow Foundation Access Node:

`_10

... \

_10

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_10

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae`

3. Start your node.

#### Example 2[​](#example-2 "Direct link to Example 2")

Use Dynamic Startup to bootstrap your node immediately, using the most recent Root Snapshot:

1. Ensure your database is not already bootstrapped, and no Root Snapshot file is present in the `$BOOTSTRAPDIR` folder.
2. Add necessary flags to node startup command.
   For example, using the Flow Foundation Access Node:

`_10

... \

_10

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_10

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae \

_10

--dynamic-startup-epoch=1`

3. Start your node.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/protocol-state-bootstrap.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Height coordinated upgrade](/networks/node-ops/node-operation/hcu)[Next

Managing disk space](/networks/node-ops/node-operation/reclaim-disk)

###### Rate this page

😞😐😊

* [Node Startup](#node-startup)
* [Using a Root Snapshot File](#using-a-root-snapshot-file)
  + [Instructions](#instructions)
  + [Obtain Root Snapshot File using Flow CLI](#obtain-root-snapshot-file-using-flow-cli)
  + [Obtain Root Snapshot File from Protocol database](#obtain-root-snapshot-file-from-protocol-database)
* [Using Dynamic Startup](#using-dynamic-startup)
  + [Specifying an Access Node](#specifying-an-access-node)
  + [Specifying an Epoch Phase](#specifying-an-epoch-phase)
  + [Instructions](#instructions-1)

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