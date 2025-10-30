# Source: https://developers.flow.com/protocol/node-ops/node-operation/network-upgrade

Network Upgrade (Spork) Process | Flow Developer Portal



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

                + [Participating in the Network](/protocol/node-ops/node-operation/faq)

                  - [Operator FAQ](/protocol/node-ops/node-operation/faq)- [Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)- [Database Encryption for Existing Node Operators](/protocol/node-ops/node-operation/db-encryption-existing-operator)- [Node Operations Guide](/protocol/node-ops/node-operation/guides/genesis-bootstrap)

                          - [Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)- [Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)- [Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)- [Node Economics](/protocol/node-ops/node-operation/node-economics)- [Node Migration](/protocol/node-ops/node-operation/node-migration)- [Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)- [Node Roles](/protocol/node-ops/node-operation/node-roles)- [Node Setup](/protocol/node-ops/node-operation/node-setup)- [Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)- [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade)- [Slashing Conditions](/protocol/node-ops/node-operation/slashing)- [Node Providers](/protocol/node-ops/node-operation/node-providers)- [Height coordinated upgrade](/protocol/node-ops/node-operation/hcu)- [Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)- [Managing disk space](/protocol/node-ops/node-operation/reclaim-disk)* [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Node Ops](/protocol/node-ops)* Participating in the Network* Network Upgrade (Spork) Process

On this page

# Network Upgrade (Spork) Process

## Overview[​](#overview "Direct link to Overview")

A Network Upgrade (spork) is a coordinated network upgrade process where node operators upgrade their node software and
re-initialize with a consolidated representation of the previous network upgrade's state. This enables rapid development
on the Flow Protocol and minimizes the impact of breaking changes.

Network upgrade are also referred to as Spork.

Network Upgrades are approximately once every year.
Upcoming network upgrades are announced in advance on the `#flow-validators-announcements` [Discord channel](https://discord.gg/flow) and on the [status](https://status.flow.com/) page.
The `#flow-validators-announcements` channel is also used to coordinate during the upgrade process with all the node operators.

> 📢 [Forte Upgrade](https://status.flow.com/incidents/x91d6t1x1qh4) on Wednesday, Oct 22nd, 2025 at 15:00 UTC

This guide is for existing operators participating in a network upgrade. See [Node Bootstrap](/protocol/node-ops/node-operation/node-bootstrap)
for a guide to joining the network for the first time.

## Step 1 - Cleaning Up Previous Spork State[​](#step-1---cleaning-up-previous-spork-state "Direct link to Step 1 - Cleaning Up Previous Spork State")

Once the spork start has been announced on Discord, stop your node and clear your database. The node should stay stopped for the duration of the spork.

warning

You can skip this step if it is your first time running a node on Flow.

1. Stop your Flow node
2. Clear the contents of your `data` directory that you have previously created. The default location is `/var/flow/data`. The `data` directory contains the Flow chain state.

## Step 2 - Start Your Node[​](#step-2---start-your-node "Direct link to Step 2 - Start Your Node")

Once you receive an announcement that the spork process is complete (via [Discord server](https://discord.gg/flow)), you will need to fetch the genesis info, update your runtime configuration and then boot your Flow node up!

warning

If you had set the [dynamic bootstrap arguments](https://developers.flow.com/protocol/node-ops/node-operation/protocol-state-bootstrap) command line arguments (`--dynamic-startup-access-address`, `--dynamic-startup-access-publickey`, `--dynamic-startup-epoch-phase`) please remove them.

1. Run the transit script to fetch the new genesis info:

Download the latest transit script - see instructions [here](/protocol/node-ops/node-operation/node-bootstrap#download-the-bootstrapping-kit)

`_10

./boot-tools/transit pull -b ./bootstrap -t ${PULL_TOKEN} -r ${YOUR_NODE_TYPE} --concurrency 10 --timeout 50m`

* `PULL_TOKEN` will be provided by the Flow team.

  + For `collection`, `consensus`, `verification` node type it will generally be `testnet-x` or `mainnet-x` where x is the latest number of respective network upgrade. e.g. `testnet-53`, `mainnet-27`.
  + For `execution` node type it will generally be `testnet-x-execution` or `mainnet-x-execution`.
  + For `access` node:
    - It will generally be `testnet-x` or `mainnet-x` if execution data indexing is not enabled.
    - It will generally be `testnet-x-execution` or `mainnet-x-execution` if execution data indexing is enabled. See [here](/protocol/node-ops/access-nodes/access-node-configuration-options) to enable execution date indexing.
* `YOUR_NODE_TYPE` should be one of `collection`, `consensus`, `execution`, `verification` based on the node(s) that you are running.

  + For access nodes however, if you have execution data index enabled use the role `execution` to ensure the execution state files (`root.checkpoint*`) are also downloaded. If you do not have execution data indexing enabled, specify the role as `access`.

Example

`_19

$ ./boot-tools/transit pull -b ./bootstrap -t mainnet-27 -r consensus

_19

Transit script Commit: 98a6ac408fdd86dba0011e698d40ebd71f4276fa

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

2. Update command line arguments

For the Forte upgrade, remove the `pebble-dir` argument as it has been deprecated. This applies to all node types.
The node will continue to use the `datadir` argument which points to the location of the node database.

3. Start your Flow node via `docker` or `systemd`

The FlowFoundation team will share the new docker tag at the completion of the upgrade. Please use that docker tag to bring up the node.

See [Node Bootstrap](/protocol/node-ops/node-operation/node-bootstrap) for detailed information on Docker/Systemd configuration.

## Common Issues[​](#common-issues "Direct link to Common Issues")

### Error: cannot create connection[​](#error-cannot-create-connection "Direct link to Error: cannot create connection")

`_10

20T18:34:21Z","message":"could not create connection"}

_10

{"level":"error","node_role":"consensus","node_id":"6d3fac8675a1df96f4bb7a27305ae531b6f4d0d2bc13a233e37bb07ab6b852dc","target":"QmVcSQaCdhmk1CMeMN7HTgGiUY1i2KqgVE2vvEmQXK4gAA","error":"failed to dial : all dials failed

_10

* [/ip4/155.138.151.101/tcp/3569] dial tcp4 155.138.151.101:3569: connect: connection refused","retry_attempt":2,"time":"2020-05-20T18:34:21Z","message":"could not create connection"}`

This error is OK. Your fellow node operators have not turned on/joined the network yet. So no need to worry about it!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/network-upgrade.md)

Last updated on **Oct 21, 2025** by **Vishal**

[Previous

Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)[Next

Slashing Conditions](/protocol/node-ops/node-operation/slashing)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Step 1 - Cleaning Up Previous Spork State](#step-1---cleaning-up-previous-spork-state)* [Step 2 - Start Your Node](#step-2---start-your-node)* [Common Issues](#common-issues)
        + [Error: cannot create connection](#error-cannot-create-connection)

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