# Source: https://developers.flow.com/networks/node-ops/node-operation/node-setup

Setting Up a Flow Node | Flow Developer Portal



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
* Node Setup

On this page

# Setting Up a Flow Node

This guide is for running a Collection, Consensus, Verification and Execution node.
If you are planning to run an Access node then refer to [access node setup](/networks/node-ops/access-nodes/access-node-setup).

First you'll need to provision a machine or virtual machine to run your node software. Please see follow the [node-provisioning](/networks/node-ops/node-operation/node-provisioning) guide for it.

## Pull the Flow Images[​](#pull-the-flow-images "Direct link to Pull the Flow Images")

The `flow-go` binaries are distributed as container images, and need to be pulled down to your host with your image management tool of choice.

Replace `$ROLE` with the node type you are planning to run. Valid options are:

* collection
* consensus
* execution
* verification
* access

`_10

# Docker

_10

docker pull gcr.io/flow-container-registry/${ROLE}:alpha-v0.0.1

_10

_10

# Containerd

_10

ctr images pull gcr.io/flow-container-registry/${ROLE}:alpha-v0.0.1",`

## Prepare Your Node to Start[​](#prepare-your-node-to-start "Direct link to Prepare Your Node to Start")

Your nodes will need to boot at startup, and restart if they crash.

If you are running `systemd` you can use the service files provided by `flow-go`.
Find them in the [Flow Go](https://github.com/onflow/flow-go/tree/master/deploy).

If you are using some other system besides Systemd, you need to ensure that the Flow container is started,
the appropriate key directories are mounted into the container, and that the container will
automatically restart following a crash.

The `systemd` files pull runtime settings from `/etc/flow/runtime-config.env` and any `.env`
files under `/etc/flow/conf.d`. Examples of these files are also available in the github repo.
You will need to modify the runtime config file later.

### Systemd[​](#systemd "Direct link to Systemd")

info

If you are not using Systemd, you can skip this step

1. Ensure that you pulled the latest changes from [flow-go repository](https://github.com/onflow/flow-go) via `git`

`_10

## Clone the repo if you haven't already done so

_10

git clone https://github.com/onflow/flow-go

_10

_10

## Get latest changes

_10

cd flow-go

_10

git pull origin master`

2. Copy your respective [systemd unit file](https://github.com/onflow/flow-go/tree/master/deploy/systemd-docker) to: `/etc/systemd/system`
3. Create directory `sudo mkdir /etc/flow`
4. Copy the [runtime-conf.env](https://github.com/onflow/flow-go/blob/master/deploy/systemd-docker/runtime-conf.env) file to: `/etc/flow/`
5. Enable your service `sudo systemctl enable flow-$ROLE.service` (replace `$ROLE` with your node role - eg. `collection`)

### Docker Configuration[​](#docker-configuration "Direct link to Docker Configuration")

If you are not using Systemd, sample commands for running each Docker container are below.
Be sure to replace `/path/to/data` and `/path/to/bootstrap` with the appropriate paths you are using.

warning

Do not run your node using `docker run` command directly without a mechanism for the node
to automatically restart following a crash.

info

The actual Docker image tag can be found [here](/networks/node-ops/node-operation/past-sporks) for appropriate spork.

### System Configuration[​](#system-configuration "Direct link to System Configuration")

Flow nodes create connections to other nodes on the network, which are represented as file descriptors by the OS. Depending on the default
limits for your machine, you may need to increase the soft limit available to the node software.

Make sure the soft limit is at least `8192`.

You can configure the ulimit for the node's docker container. See the [Docker documentation](https://docs.docker.com/engine/networks/commandline/run/#ulimit) for more details.

### Admin Server[​](#admin-server "Direct link to Admin Server")

Each node can be configured with an admin server, which allows you to control some of the node's configuration, as well as view some of its internal state. You can find
a few of the commands in the Admin Server [README](https://github.com/onflow/flow-go/blob/master/admin/README.md). Two commands to highlight are:

* `list-commands`: which returns a list of all of the available commands for your node
* `set-log-level`: which allows you to change the log level of your node at runtime

You can enable the admin server by passing the `--admin-addr` flag with an interface and port.

> ⚠️ *IMPORANT: The admin server can modify your node's configuration. DO NOT allow access to untrusted clients.*

### Access[​](#access "Direct link to Access")

`_19

docker run --rm \

_19

-v /path/to/bootstrap:/bootstrap:ro \

_19

-v /path/to/data:/data:rw \

_19

--name flow-go \

_19

--network host \

_19

--ulimit nofile=8192 \

_19

gcr.io/flow-container-registry/access:<applicable docker tag> \

_19

--nodeid=${FLOW_GO_NODE_ID} \

_19

--bootstrapdir=/bootstrap \

_19

--datadir=/data/protocol \

_19

--secretsdir=/data/secrets \

_19

--execution-data-dir=/data/execution_data \

_19

--rpc-addr=0.0.0.0:9000 \

_19

--http-addr=0.0.0.0:8000 \

_19

--admin-addr=0.0.0.0:9002 \

_19

--collection-ingress-port=9000 \

_19

--script-addr=${FLOW_NETWORK_EXECUTION_NODE} \

_19

--bind 0.0.0.0:3569 \

_19

--loglevel=error`

### Collection[​](#collection "Direct link to Collection")

`_18

docker run --rm \

_18

-v /path/to/bootstrap:/bootstrap:ro \

_18

-v /path/to/data:/data:rw \

_18

--name flow-go \

_18

--network host \

_18

--ulimit nofile=8192 \

_18

gcr.io/flow-container-registry/collection:<applicable docker tag> \

_18

--nodeid=${FLOW_GO_NODE_ID} \

_18

--bootstrapdir=/bootstrap \

_18

--datadir=/data/protocol \

_18

--secretsdir=/data/secrets \

_18

--ingress-addr=0.0.0.0:9000 \

_18

--admin-addr=0.0.0.0:9002 \

_18

--bind 0.0.0.0:3569 \

_18

--access-node-ids=4e17496619df8bb4dcd579c252d9fb026e54995db0dc6825bdcd27bd3288a990,7e3fe64ccc119f578a7795df8b8c512e05409bdc7de4f74259c6f48351fecb26,416c65782048656e74736368656c009530ef3ab4b8bf83b24df54fe5f81853de,416e647265772042757269616e00d219355d62b9adad8ebd3fab223a1cf84c22 \

_18

--gossipsub-peer-scoring-enabled=false \

_18

--gossipsub-peer-gater-enabled=true \

_18

--loglevel=error`

### Consensus[​](#consensus "Direct link to Consensus")

`_17

docker run --rm \

_17

-v /path/to/bootstrap:/bootstrap:ro \

_17

-v /path/to/data:/data:rw \

_17

--name flow-go \

_17

--network host \

_17

--ulimit nofile=8192 \

_17

gcr.io/flow-container-registry/consensus:<applicable docker tag> \

_17

--nodeid=${FLOW_GO_NODE_ID} \

_17

--bootstrapdir=/bootstrap \

_17

--datadir=/data/protocol \

_17

--secretsdir=/data/secrets \

_17

--admin-addr=0.0.0.0:9002 \

_17

--bind 0.0.0.0:3569 \

_17

--access-node-ids=4e17496619df8bb4dcd579c252d9fb026e54995db0dc6825bdcd27bd3288a990,7e3fe64ccc119f578a7795df8b8c512e05409bdc7de4f74259c6f48351fecb26,416c65782048656e74736368656c009530ef3ab4b8bf83b24df54fe5f81853de,416e647265772042757269616e00d219355d62b9adad8ebd3fab223a1cf84c22 \

_17

--gossipsub-peer-scoring-enabled=false \

_17

--gossipsub-peer-gater-enabled=true \

_17

--loglevel=error`

### Execution[​](#execution "Direct link to Execution")

`_17

docker run --rm \

_17

-v /path/to/bootstrap:/bootstrap:ro \

_17

-v /path/to/data:/data:rw \

_17

--name flow-go \

_17

--network host \

_17

--ulimit nofile=500000 \

_17

gcr.io/flow-container-registry/execution:<applicable docker tag> \

_17

--nodeid=${FLOW_GO_NODE_ID} \

_17

--bootstrapdir=/bootstrap \

_17

--datadir=/data/protocol \

_17

--secretsdir=/data/secrets \

_17

--triedir=/data/execution \

_17

--execution-data-dir=/data/execution_data \

_17

--rpc-addr=0.0.0.0:9000 \

_17

--admin-addr=0.0.0.0:9002 \

_17

--bind 0.0.0.0:3569 \

_17

--loglevel=error`

For execution nodes, it is recommend to increase the open files limit in your operating system. To do that, add the following to your `/etc/security/limits.conf` or the equivalent `limits.conf` for your distribution:

`_10

* hard nofile 500000

_10

* soft nofile 500000

_10

root hard nofile 500000

_10

root soft nofile 500000`

Restart your machine to apply these changes. To verify that the new limits have been applied, run:

`_10

ulimit -n`

### Verification[​](#verification "Direct link to Verification")

`_14

docker run --rm \

_14

-v /path/to/bootstrap:/bootstrap:ro \

_14

-v /path/to/data:/data:rw \

_14

--name flow-go \

_14

--network host \

_14

--ulimit nofile=8192 \

_14

gcr.io/flow-container-registry/verification:<applicable docker tag> \

_14

--nodeid=${FLOW_GO_NODE_ID} \

_14

--bootstrapdir=/bootstrap \

_14

--datadir=/data/protocol \

_14

--secretsdir=/data/secrets \

_14

--admin-addr=0.0.0.0:9002 \

_14

--bind 0.0.0.0:3569 \

_14

--loglevel=error`

## Start the Node[​](#start-the-node "Direct link to Start the Node")

Now that your node is provisioned and configured, it can be started.

warning

Before starting your node, ensure it is [registered](/networks/node-ops/node-operation/node-bootstrap#step-2---stake-your-node) and [authorized](/networks/node-ops/node-operation/node-bootstrap#confirming-authorization).

Ensure you start your node at the appropriate time.
See [Spork Process](/networks/node-ops/node-operation/spork) for when to start up a node following a spork.
See [Node Bootstrap](/networks/node-ops/node-operation/node-bootstrap#timing) for when to start up a newly registered node.

### Systemd[​](#systemd-1 "Direct link to Systemd")

1. Check that your `runtime-conf.env` is at `/etc/flow/runtime-conf.env`
2. Update your environment variables: `source /etc/flow/runtime-conf.env`
3. Start your service: `sudo systemctl start flow`

## Verify your Node is Running[​](#verify-your-node-is-running "Direct link to Verify your Node is Running")

Here are a few handy commands that you can use to check if your Flow node is up and running

### Systemd[​](#systemd-2 "Direct link to Systemd")

* To get Flow logs: `sudo journalctl -u flow-YOUR_ROLE`
* To get the status: `sudo systemctl status flow`

`_10

● flow-verification.service - Flow Access Node running with Docker

_10

Loaded: loaded (/etc/systemd/system/flow-verification.service; enabled; vendor preset: enabled)

_10

Active: active (running) since Wed 2020-05-20 18:18:13 UTC; 1 day 6h ago

_10

Process: 3207 ExecStartPre=/usr/bin/docker pull gcr.io/flow-container-registry/verification:${FLOW_GO_NODE_VERSION} (code=exited, status=0/SUCCESS)

_10

Main PID: 3228 (docker)

_10

Tasks: 10 (limit: 4915)

_10

Memory: 33.0M

_10

CGroup: /system.slice/flow-verification.service

_10

└─3228 /usr/bin/docker run --rm -v /var/flow/bootstrap:/bootstrap:ro -v /var/flow/data:/data:rw --rm --name flow-go --network host gcr.io/flow-container-registry/verification:candidate8 --nodeid=489f8a4513d5bd8b8b093108fec00327b683db545b37b4ea9153f61b2c0c49dc --bootstrapdir=/bootstrap --datadir=/data/protocol --alpha=1 --bind 0.0.0.0:3569 --loglevel=error`

### Docker[​](#docker "Direct link to Docker")

* To get Flow logs: `sudo docker logs flow-go`
* To get the status: `sudo docker ps`

`_10

$ sudo docker ps

_10

CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES

_10

1dc5d43385b6 gcr.io/flow-container-registry/verification:candidate8 \"/bin/app --nodeid=4…\" 30 hours ago Up 30 hours flow-go`

## Monitoring and Metrics[​](#monitoring-and-metrics "Direct link to Monitoring and Metrics")

This is intended for operators who would like to see what their Flow nodes are currently doing. Head over to [Monitoring Node Health](/networks/node-ops/node-operation/monitoring-nodes) to get setup.

### Node Status[​](#node-status "Direct link to Node Status")

The metrics for the node should be able to provide a good overview of the status of the node. If we want to get a quick snapshot of the status of the node, and if it's properly participating in the network, you can check the `consensus_compliance_finalized_height` or `consensus_compliance_sealed_height` metric, and ensure that it is not zero and strictly increasing.

`_10

curl localhost:8080/metrics | grep consensus_compliance_sealed_height

_10

_10

# HELP consensus_compliance_sealed_height the last sealed height

_10

# TYPE consensus_compliance_sealed_height gauge

_10

consensus_compliance_sealed_height 1.132054e+06`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/node-setup.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

[Previous

Node Roles](/networks/node-ops/node-operation/node-roles)[Next

Past Spork Info](/networks/node-ops/node-operation/past-sporks)

###### Rate this page

😞😐😊

* [Pull the Flow Images](#pull-the-flow-images)
* [Prepare Your Node to Start](#prepare-your-node-to-start)
  + [Systemd](#systemd)
  + [Docker Configuration](#docker-configuration)
  + [System Configuration](#system-configuration)
  + [Admin Server](#admin-server)
  + [Access](#access)
  + [Collection](#collection)
  + [Consensus](#consensus)
  + [Execution](#execution)
  + [Verification](#verification)
* [Start the Node](#start-the-node)
  + [Systemd](#systemd-1)
* [Verify your Node is Running](#verify-your-node-is-running)
  + [Systemd](#systemd-2)
  + [Docker](#docker)
* [Monitoring and Metrics](#monitoring-and-metrics)
  + [Node Status](#node-status)

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