# Source: https://developers.flow.com/protocol/node-ops/node-operation/guides/starting-nodes

Starting Your Nodes | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

      * [Genesis Bootstrapping](/protocol/node-ops/node-operation/guides/genesis-bootstrap)
      * [Spork Practice](/protocol/node-ops/node-operation/guides/spork-practice)
      * [Starting Your Nodes](/protocol/node-ops/node-operation/guides/starting-nodes)
    - [Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)
    - [Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)
    - [Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)
    - [Node Economics](/protocol/node-ops/node-operation/node-economics)
    - [Node Migration](/protocol/node-ops/node-operation/node-migration)
    - [Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)
    - [Node Roles](/protocol/node-ops/node-operation/node-roles)
    - [Node Setup](/protocol/node-ops/node-operation/node-setup)
    - [Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)
    - [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade)
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
* Node Operations Guide
* Starting Your Nodes

On this page

# Starting Your Nodes

Prior to starting up your nodes make sure you have the following items completed:

1. Bootstrap process completed with the bootstrap directory handy (default: `/var/flow/bootstrap`)
2. Flow `data` directory created (default: `/var/flow/data`)
3. [node config](/protocol/node-ops/node-operation/node-bootstrap) ready
4. Firewall exposes TCP/3569, and if you are running `access` node also the GRPC port (default: TCP/9000)

For more details head back to [Setting up your node](/protocol/node-ops/node-operation/node-setup#prepare-your-node-to-start)

When you have all the above completed, you can start your Flow node via `systemd` or `docker`.

## systemd[​](#systemd "Direct link to systemd")

Ensure that you downloaded the systemd unit file. If you haven't, follow the [Set your node to start](/protocol/node-ops/node-operation/node-setup#prepare-your-node-to-start) guide to get your unit file and enabled.

Once you have your Flow service enabled you can now start your service: `systemctl start flow`

## Docker[​](#docker "Direct link to Docker")

If you don't have have systemd on your system, or prefer not to use systemd, you can run the following `docker` commands for your respective Flow role to start your node!

### Access[​](#access "Direct link to Access")

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

gcr.io/flow-container-registry/access:v0.0.6-alpha \

_14

--nodeid=${FLOW_GO_NODE_ID} \

_14

--bootstrapdir=/bootstrap \

_14

--datadir=/data/protocol \

_14

--rpc-addr=0.0.0.0:9000 \

_14

--ingress-addr=${FLOW_NETWORK_COLLECTION_NODE} \

_14

--script-addr=${FLOW_NETWORK_EXECUTION_NODE} \

_14

--bind 0.0.0.0:3569 \

_14

--loglevel=error`

### Collection[​](#collection "Direct link to Collection")

`_13

docker run --rm \

_13

-v /path/to/bootstrap:/bootstrap:ro \

_13

-v /path/to/data:/data:rw \

_13

--name flow-go \

_13

--network host \

_13

gcr.io/flow-container-registry/collection:v0.0.6-alpha \

_13

--nodeid=${FLOW_GO_NODE_ID} \

_13

--bootstrapdir=/bootstrap \

_13

--datadir=/data/protocol \

_13

--rpc-addr=0.0.0.0:9000 \

_13

--nclusters=${FLOW_NETWORK_COLLECTION_CLUSTER_COUNT} \

_13

--bind 0.0.0.0:3569 \

_13

--loglevel=error`

### Consensus[​](#consensus "Direct link to Consensus")

`_12

docker run --rm \

_12

-v /path/to/bootstrap:/bootstrap:ro \

_12

-v /path/to/data:/data:rw \

_12

--name flow-go \

_12

--network host \

_12

gcr.io/flow-container-registry/consensus:v0.0.6-alpha \

_12

--nodeid=${FLOW_GO_NODE_ID} \

_12

--bootstrapdir=/bootstrap \

_12

--datadir=/data/protocol \

_12

--nclusters=${FLOW_NETWORK_COLLECTION_CLUSTER_COUNT} \

_12

--bind 0.0.0.0:3569 \

_12

--loglevel=error`

### Execution[​](#execution "Direct link to Execution")

`_13

docker run --rm \

_13

-v /path/to/bootstrap:/bootstrap:ro \

_13

-v /path/to/data:/data:rw \

_13

--name flow-go \

_13

--network host \

_13

gcr.io/flow-container-registry/execution:v0.0.6-alpha \

_13

--nodeid=${FLOW_GO_NODE_ID} \

_13

--bootstrapdir=/bootstrap \

_13

--datadir=/data/protocol \

_13

--ingress-addr=0.0.0.0:9000 \

_13

--nclusters=${FLOW_NETWORK_COLLECTION_CLUSTER_COUNT} \

_13

--bind 0.0.0.0:3569 \

_13

--loglevel=error`

### Verification[​](#verification "Direct link to Verification")

`_12

docker run --rm \

_12

-v /path/to/bootstrap:/bootstrap:ro \

_12

-v /path/to/data:/data:rw \

_12

--name flow-go \

_12

--network host \

_12

gcr.io/flow-container-registry/verification:v0.0.6-alpha \

_12

--nodeid=${FLOW_GO_NODE_ID} \

_12

--bootstrapdir=/bootstrap \

_12

--datadir=/data/protocol \

_12

--nclusters=${FLOW_NETWORK_COLLECTION_CLUSTER_COUNT} \

_12

--bind 0.0.0.0:3569 \

_12

--loglevel=error`

### Additional Flags[​](#additional-flags "Direct link to Additional Flags")

#### Networking Layer[​](#networking-layer "Direct link to Networking Layer")

All networking layer settings are initialized to default values from the [config/default-config.yml](https://github.com/onflow/flow-go/blob/master/config/default-config.yml) file when the Flow node starts up. Each attribute in this YAML file matches a flag name, allowing you to override the default setting by specifying the corresponding flag in the `docker run` command. For instance, to change the `networking-connection-pruning` setting, use its matching flag name (`networking-connection-pruning`) and desired value in the `docker run` command.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/guides/starting-nodes.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Spork Practice](/protocol/node-ops/node-operation/guides/spork-practice)[Next

Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)

###### Rate this page

😞😐😊

Copy as Markdown

* [systemd](#systemd)
* [Docker](#docker)
  + [Access](#access)
  + [Collection](#collection)
  + [Consensus](#consensus)
  + [Execution](#execution)
  + [Verification](#verification)
  + [Additional Flags](#additional-flags)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
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
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.