# Source: https://developers.flow.com/networks/node-ops/node-operation/guides/starting-nodes

Starting Your Nodes | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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

      * [Genesis Bootstrapping](/networks/node-ops/node-operation/guides/genesis-bootstrap)
      * [Spork Practice](/networks/node-ops/node-operation/guides/spork-practice)
      * [Starting Your Nodes](/networks/node-ops/node-operation/guides/starting-nodes)
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
* Node Operations Guide
* Starting Your Nodes

On this page

# Starting Your Nodes

Prior to starting up your nodes make sure you have the following items completed:

1. Bootstrap process completed with the bootstrap directory handy (default: `/var/flow/bootstrap`)
2. Flow `data` directory created (default: `/var/flow/data`)
3. [node config](/networks/node-ops/node-operation/node-bootstrap) ready
4. Firewall exposes TCP/3569, and if you are running `access` node also the GRPC port (default: TCP/9000)

For more details head back to [Setting up your node](/networks/node-ops/node-operation/node-setup#prepare-your-node-to-start)

When you have all the above completed, you can start your Flow node via `systemd` or `docker`.

## systemd[​](#systemd "Direct link to systemd")

Ensure that you downloaded the systemd unit file. If you haven't, follow the [Set your node to start](/networks/node-ops/node-operation/node-setup#prepare-your-node-to-start) guide to get your unit file and enabled.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/guides/starting-nodes.md)

Last updated on **Feb 25, 2025** by **Chase Fleming**

[Previous

Spork Practice](/networks/node-ops/node-operation/guides/spork-practice)[Next

Machine Accounts for Existing Node Operators](/networks/node-ops/node-operation/machine-existing-operator)

###### Rate this page

😞😐😊

* [systemd](#systemd)
* [Docker](#docker)
  + [Access](#access)
  + [Collection](#collection)
  + [Consensus](#consensus)
  + [Execution](#execution)
  + [Verification](#verification)
  + [Additional Flags](#additional-flags)

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