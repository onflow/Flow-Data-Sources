# Source: https://developers.flow.com/networks/node-ops/node-operation/spork

Network Upgrade (Spork) Process | Flow Developer Portal



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
* Network Upgrade (Spork) Process

On this page

# Network Upgrade (Spork) Process

## Overview[​](#overview "Direct link to Overview")

A spork is a coordinated network upgrade process where node operators upgrade their node software and
re-initialize with a consolidated representation of the previous spork's state. This enables rapid development
on the Flow Protocol and minimizes the impact of breaking changes.

The Flow network sporks approximately once every year. Upcoming sporks
are announced in advance on the `#flow-validators-announcements` **Discord** channel
and in [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks). The `#flow-validators-announcements` channel is
also used to coordinate during the spork process.

This guide is for existing operators participating in a spork. See [Node Bootstrap](/networks/node-ops/node-operation/node-bootstrap)
for a guide to joining the network for the first time.

## Step 1 - Cleaning Up Previous Spork State[​](#step-1---cleaning-up-previous-spork-state "Direct link to Step 1 - Cleaning Up Previous Spork State")

Once the spork start has been announced on, stop your node and clear your database. The node should stay stopped for the duration of the spork.

warning

You can skip this step if it is your first time running a node on Flow.

1. Stop your Flow node
2. Clear the contents of your `data` directory that you have previously created. The default location is `/var/flow/data`. The `data` directory contains the Flow chain state.

## Step 2 - Start Your Node[​](#step-2---start-your-node "Direct link to Step 2 - Start Your Node")

Once you receive an announcement that the spork process is complete (via Discord), you will need to fetch the genesis info, update your runtime configuration and then boot your Flow node up!

warning

If you had set the [dynamic bootstrap arguments](https://developers.flow.com/networks/node-ops/node-operation/protocol-state-bootstrap) command line arguments (`--dynamic-startup-access-address`, `--dynamic-startup-access-publickey`, `--dynamic-startup-epoch-phase`) please remove them.

1. Run the transit script to fetch the new genesis info:
   `./boot-tools/transit pull -b ./bootstrap -t ${PULL_TOKEN} -r ${YOUR_NODE_TYPE} --concurrency 10 --timeout 15m`

* `PULL_TOKEN` will be provided by the Flow team.

  + For `collection`, `consensus`, `verification` node type it will generally be `testnet-x` or `mainnet-x` where x is the latest number of respective network upgrade. e.g. `testnet-52`, `mainnet-26`.
  + For `execution` node type it will generally be `testnet-x-execution` or `mainnet-x-execution`.
  + For `access` node:
    - It will generally be `testnet-x` or `mainnet-x` if execution data indexing is not enabled.
    - It will generally be `testnet-x-execution` or `mainnet-x-execution` if execution data indexing is enabled.
* `YOUR_NODE_TYPE` should be one of `collection`, `consensus`, `execution`, `verification`, `access` based on the node(s) that you are running.

Example

`_19

$ ./boot-tools/transit pull -b ./bootstrap -t mainnet-16 -r consensus

_19

Transit script Commit: a9f6522855e119ad832a97f8b7bce555a163e490

_19

2020/11/25 01:02:53 Running pull

_19

2020/11/25 01:02:53 Downloading bootstrap/public-root-information/node-infos.pub.json

_19

2020/11/25 01:02:54 Downloading bootstrap/public-root-information/root-protocol-snapshot.json

_19

2020/11/25 01:02:54 Downloading bootstrap/random-beacon.priv.json.39fa54984b8eaa463e129919464f61c8cec3a4389478df79c44eb9bfbf30799a.enc

_19

2020/11/25 01:02:54 SHA256 of the root block is: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

_19

_19

$ tree ./bootstrap/

_19

./bootstrap/

_19

├── private-root-information

_19

│ └── private-node-info_39fa54984b8eaa463e129919464f61c8cec3a4389478df79c44eb9bfbf30799a

_19

│ └── node-info.priv.json

_19

├── public-root-information

_19

│ ├── node-id

_19

│ ├── node-info.pub.39fa54984b8eaa463e129919464f61c8cec3a4389478df79c44eb9bfbf30799a.json

_19

│ ├── node-infos.pub.json

_19

│ └── root-protocol-snapshot.json

_19

└── random-beacon.priv.json.39fa54984b8eaa463e129919464f61c8cec3a4389478df79c44eb9bfbf30799a`

2. Pull the latest changes from [flow-go repository](https://github.com/onflow/flow-go)
3. Get your `node-id`, you can find it at `/path/to/bootstrap/public-genesis-information/node-id`
4. Update the `FLOW_GO_NODE_ID` inside [runtime-conf.env](https://github.com/onflow/flow-go/blob/master/deploy/systemd-docker/runtime-conf.env) to the `node-id` that you got from the previous step
5. Start your Flow node via `docker` or `systemd`

See [Node Bootstrap](/networks/node-ops/node-operation/node-bootstrap) for detailed information on Docker/Systemd configuration.

## Common Issues[​](#common-issues "Direct link to Common Issues")

### Error: cannot create connection[​](#error-cannot-create-connection "Direct link to Error: cannot create connection")

`_10

20T18:34:21Z","message":"could not create connection"}

_10

{"level":"error","node_role":"consensus","node_id":"6d3fac8675a1df96f4bb7a27305ae531b6f4d0d2bc13a233e37bb07ab6b852dc","target":"QmVcSQaCdhmk1CMeMN7HTgGiUY1i2KqgVE2vvEmQXK4gAA","error":"failed to dial : all dials failed

_10

* [/ip4/155.138.151.101/tcp/3569] dial tcp4 155.138.151.101:3569: connect: connection refused","retry_attempt":2,"time":"2020-05-20T18:34:21Z","message":"could not create connection"}`

This error is OK. Your fellow node operators have not turned on/joined the network yet. So no need to worry about it!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/spork.md)

Last updated on **Mar 27, 2025** by **Brian Doyle**

[Previous

Past Spork Info](/networks/node-ops/node-operation/past-sporks)[Next

Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)

###### Rate this page

😞😐😊

* [Overview](#overview)
* [Step 1 - Cleaning Up Previous Spork State](#step-1---cleaning-up-previous-spork-state)
* [Step 2 - Start Your Node](#step-2---start-your-node)
* [Common Issues](#common-issues)
  + [Error: cannot create connection](#error-cannot-create-connection)

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