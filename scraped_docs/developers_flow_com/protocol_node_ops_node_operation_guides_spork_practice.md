# Source: https://developers.flow.com/protocol/node-ops/node-operation/guides/spork-practice

Spork Practice | Flow Developer Portal



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
* Node Operations Guide
* Spork Practice

On this page

# Spork Practice

## Sporking[​](#sporking "Direct link to Sporking")

The actual process of Sporking will mostly be covered by the Node Operators Quick Guide, and will not be covered here.

[Spork](/protocol/node-ops/node-operation/spork)

Instead, we'll aim to give some instructions for those that want to Practice the process themselves, before joining the Mainnet Spork.

This guide assumes you have access to the Flow-Go repo, which you'll need to build up-to-date containers and run code snippets.

## Local Testnet[​](#local-testnet "Direct link to Local Testnet")

One way to get a good feel of the network without too much interaction with infrastructure is to play with the local testnet, which we've named the Flow Local Instrumented Test Environment (FLITE).

<https://github.com/onflow/flow-go/blob/master/integration/localnet/README.md>

FLITE will allow you to start a full flow network locally, which means starting all 5 roles required for a functioning network. Instructions for initializing and starting the local network are provided in the README above.

When Starting FLITE, it will build all the docker images required for the network. This can also be done manually ahead of time, using `make docker-build-flow` from the root directory of `flow-go`

## Remote Testnet[​](#remote-testnet "Direct link to Remote Testnet")

If you would like more control over the nodes, beyond what docker compose can provide, or you wish to deploy the docker images to separate VMs, to more closely imitate Mainnet, you will have to manually run bootstrapping for a specific configuration of nodes that you would like to test.

Example files are available in the `cmd/bootstrap/example_files` folder.

Where the `node-config.json` will usually store all flow's nodes, whereas partner node info usually goes into a separate folder. The last file, which will need to be manually populated, is the partner stakes file, which takes the IDs of all the partner nodes and associates a stake. For now, this can be arbitrary.

Once you have all the information, you can make use of the `finalize` command:

And generate the bootstrapping folder required to start up your nodes.

Once you have the bootstrapping folder, you'll be able to start up all the nodes that were included in the bootstrapping process.

[Node Setup Docker](/protocol/node-ops/node-operation/node-setup#docker)

The startup command will look very similar to what is provided in the quick guide. One such example, assuming we named our bootstrap folder `bootstrap`:

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

gcr.io/flow-container-registry/execution:latest \

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

The two missing pieces of info here are `FLOW_GO_NODE_ID` which will have been generated from the bootstrap process, and will depend on which node you're trying to run, and `FLOW_NETWORK_COLLECTION_CLUSTER_COUNT` which we've been defaulting to `2`

## Practice Testnet[​](#practice-testnet "Direct link to Practice Testnet")

Lastly, if the goal is to practice the entire Sporking procedure, including `transit` of staking and networking keys, and joining a network, we can help spin up a Testnet temporarily for this purpose. This will require quite a bit of coordination, and will basically be the same steps as the Mainnet spork, so please let us know if this is something you'd like to do and we’ll connect to plan accordingly.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/guides/spork-practice.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Genesis Bootstrapping](/protocol/node-ops/node-operation/guides/genesis-bootstrap)[Next

Starting Your Nodes](/protocol/node-ops/node-operation/guides/starting-nodes)

###### Rate this page

😞😐😊

Copy as Markdown

* [Sporking](#sporking)
* [Local Testnet](#local-testnet)
* [Remote Testnet](#remote-testnet)
* [Practice Testnet](#practice-testnet)

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
* [EVM](/build/evm/about)

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