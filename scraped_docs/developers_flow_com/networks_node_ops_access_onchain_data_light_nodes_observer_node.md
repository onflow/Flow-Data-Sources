# Source: https://developers.flow.com/networks/node-ops/access-onchain-data/light-nodes/observer-node




Light Node a.k.a Observer Node | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
  + [Accessing On-chain Data](/networks/node-ops/access-onchain-data/access-nodes/access-node-setup)
    - [Access Nodes](/networks/node-ops/access-onchain-data/access-nodes/access-node-setup)
    - [EVM Gateway](/networks/node-ops/access-onchain-data/evm-gateway/evm-gateway-setup)
    - [Light Nodes](/networks/node-ops/access-onchain-data/light-nodes/observer-node)
      * [Light Node Setup](/networks/node-ops/access-onchain-data/light-nodes/observer-node)
  + [Participating in the Network](/networks/node-ops/node-operation/faq)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)


* [Node Ops](/networks/node-ops)
* Accessing On-chain Data
* Light Nodes
* Light Node Setup
On this page
# Light Node a.k.a Observer Node

A light node also known as the observer node is similar to an access node and provides a locally accessible, continuously updated, verified copy of the block data. It serves the [gRPC Access API](/networks/node-ops/access-onchain-data/access-nodes/accessing-data/access-api) but unlike an access node, an light node does not need to be staked, and **anyone** can run it without being added to the approved list of nodes.

The light node bootstraps by connecting to an access node and becoming part of the public network comprised of access nodes and other light nodes. It then continuously receives blocks, which the consensus nodes are adding to the chain, either directly from access nodes or from other light nodes that are part of the public network. However, it makes no trust assumption of the upstream access node or the light node which is providing the block and locally verifies that the blocks that are received are the correct extension of the chain e.g. after receiving valid blocks A, B and C when it receives block D, it verifies that block D is indeed signed by the consensus nodes and is a valid next block. The received block data is indexed and made available via the Access API. For Collection, Transactions and Account queries, it delegates those requests to the upstream access node. Similarly, transactions and scripts sent to a light node are also forwarded to the upstream access node. Future versions of the light node will be able to serve this data locally as well.

Since the light node is not staked, it does not produce or execute blocks but instead serves as an *unstaked access node* that can be easily run on any consumer-grade computer which has enough disk space.

![Observer nodes](/assets/images/observer-ca7f0bed4fc93098aef7600d3fe7f304.png)

## Who should run a light node?[​](#who-should-run-a-light-node "Direct link to Who should run a light node?")

The light node provides an alternative to running an access node. Hence, it is ideal for Dapps that need access to the latest block data locally on a machine they control. Examples include a wallet application that needs to track the latest block ID and height. Alternatively, access node operators that want to scale their access node endpoints geographically can spin up light nodes in different regions, which can talk to their staked access node and to each other.

## Running an light node[​](#running-an-light-node "Direct link to Running an light node")

### Hardware[​](#hardware "Direct link to Hardware")

In general, any consumer-grade computer with a decent network connection and sufficient disk space should be able to run a light node.

Minimum requirements

* CPU with 2+ cores
* 4 GB RAM minimum
* 300 GB SSD disk
* 10Mbps network connection

### Steps to run a light node[​](#steps-to-run-a-light-node "Direct link to Steps to run a light node")

> [Here](https://www.loom.com/share/990a725531754106b91d8ccec6244219) is video walk-though of these 👇 steps.

#### Step 1 - Generate the node directory structure[​](#step-1---generate-the-node-directory-structure "Direct link to Step 1 - Generate the node directory structure")

The light node requires the following directory structure,

 `_10$ tree flow_observer_10flow_observer/_10├── bootstrap_10│ ├── network.key (file containing the node private network key)_10│ └── public-root-information_10│ └── root-protocol-state-snapshot.json (the genesis data of the current spork)_10└── data (directory used by the light node to store block data)`

Create the parent and the sub-directories
e.g.

 `_10mkdir -p flow_observer/bootstrap/public-root-information_10mkdir flow_observer/data`
#### Step 2 - Generate the network key[​](#step-2---generate-the-network-key "Direct link to Step 2 - Generate the network key")

Like any other Flow node, the light node also needs a networking [ECDSA key](https://github.com/onflow/flow-go/blob/master/cmd/bootstrap/utils/key_generation.go#L52-L54) to talk to the network.
Download the Bootstrapping kit, and generate the networking key.

 `_10curl -sL -O storage.googleapis.com/flow-genesis-bootstrap/boot-tools.tar_10tar -xvf boot-tools.tar_10./boot-tools/bootstrap observer-network-key --output-file ./flow_observer/bootstrap/network.key`

*If you are running on a mac, download the boot-tools for mac to generate the key*

 `_10# For M1_10curl -sL -O storage.googleapis.com/flow-genesis-bootstrap/boot-tools-m1.tar_10# For Intel Mac_10curl -sL -O storage.googleapis.com/flow-genesis-bootstrap/boot-tools-intel-mac.tar`
#### Step 3 - Download the root-protocol-state-snapshot.json file for the current spork[​](#step-3---download-the-root-protocol-state-snapshotjson-file-for-the-current-spork "Direct link to Step 3 - Download the root-protocol-state-snapshot.json file for the current spork")

The `root-protocol-state-snapshot.json` is generated for each [spork](/networks/node-ops/node-operation/spork) and contains the genesis data for that spork.
It is published and made available after each spork. The download location is specified [here](https://github.com/onflow/flow/blob/master/sporks.json) under [rootProtocolStateSnapshot](https://github.com/onflow/flow/blob/master/sporks.json#L16) and can be downloaded as follows,

For mainnet find the latest spork version from [sporks.json](https://github.com/onflow/flow/blob/master/sporks.json) and then download the `root-protocol-state-snapshot.json` and the signature file for it.

 `_10wget -P ./flow_observer/bootstrap/public-root-information https://storage.googleapis.com/flow-genesis-bootstrap/mainnet-<spork version>-execution/public-root-information/root-protocol-state-snapshot.json_10wget -P ./flow_observer/bootstrap/public-root-information https://storage.googleapis.com/flow-genesis-bootstrap/mainnet-<spork version>-execution/public-root-information/root-protocol-state-snapshot.json.asc`

Similarly, for testnet find the latest spork version from [sporks.json](https://github.com/onflow/flow/blob/master/sporks.json) and then download the `root-protocol-state-snapshot.json` and the signature file for it.

 `_10wget -P ./flow_observer/bootstrap/public-root-information https://storage.googleapis.com/flow-genesis-bootstrap/testnet-<spork version>/public-root-information/root-protocol-state-snapshot.json_10wget -P ./flow_observer/bootstrap/public-root-information https://storage.googleapis.com/flow-genesis-bootstrap/testnet-<spork version>/public-root-information/root-protocol-state-snapshot.json.asc`
##### Verify the PGP signature[​](#verify-the-pgp-signature "Direct link to Verify the PGP signature")

Add the `flow-signer@onflow.org` public key

 `_10gpg --keyserver keys.openpgp.org --search-keys flow-signer@onflow.org_10_10gpg: data source: http://keys.openpgp.org:11371_10(1) Flow Team (Flow Full Observer node snapshot verification master key) <_10 256 bit ECDSA key CB5264F7FD4CDD27, created: 2021-09-15_10Keys 1-1 of 1 for "flow-signer@onflow.org". Enter number(s), N)ext, or Q)uit > 1`

Verify the root-snapshot file

 `_10gpg --verify ./flow_observer/bootstrap/public-root-information/root-protocol-state-snapshot.json.asc_10_10gpg: assuming signed data in 'bootstrap/public-root-information/root-protocol-state-snapshot.json'_10gpg: Signature made Wed Sep 15 11:34:33 2021 PDT_10gpg: using ECDSA key 40CD95717AC463E61EE3B285B718CA310EDB542F_10gpg: Good signature from "Flow Team (Flow Full Observer node snapshot verification master key) <flow-signer@onflow.org>" [unknown]_10gpg: WARNING: This key is not certified with a trusted signature!_10gpg: There is no indication that the signature belongs to the owner._10Primary key fingerprint: 7D23 8D1A E6D3 2A71 8ECD 8611 CB52 64F7 FD4C DD27_10 Subkey fingerprint: 40CD 9571 7AC4 63E6 1EE3 B285 B718 CA31 0EDB 542F`

Alternately, if you don't care about the blocks before the current block, you can request the current root-snapshot file via the [Flow CLI](/tools/flow-cli).

For mainnet

 `_10 flow snapshot save ./flow_observer/bootstrap/public-root-information/root-protocol-state-snapshot.json --host secure.mainnet.nodes.onflow.org:9001 --network-key 28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae`

For testnet

 `_10flow snapshot save ./flow_observer/bootstrap/public-root-information/root-protocol-state-snapshot.json --host secure.testnet.nodes.onflow.org:9001 --network-key ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d`
#### Step 4 - Start the node[​](#step-4---start-the-node "Direct link to Step 4 - Start the node")

The light node can be run as a docker container

##### Observer for Flow Mainnet[​](#observer-for-flow-mainnet "Direct link to Observer for Flow Mainnet")

 `_20docker run --rm \_20 -v $PWD/flow_observer/bootstrap:/bootstrap:ro \_20 -v $PWD/flow_observer/data:/data:rw \_20 --name flow_observer \_20 -p 80:80 \_20 -p 3569:3569 \_20 -p 9000:9000 \_20 -p 9001:9001 \_20 gcr.io/flow-container-registry/observer:v0.27.2 \_20 --bootstrapdir=/bootstrap \_20 --datadir=/data/protocol \_20 --bind 0.0.0.0:3569 \_20 --rest-addr=:80 \_20 --loglevel=error \_20 --secretsdir=/data/secrets \_20 --upstream-node-addresses=secure.mainnet.nodes.onflow.org:9001 \_20 --upstream-node-public-keys=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae \_20 --bootstrap-node-addresses=secure.mainnet.nodes.onflow.org:3570 \_20 --bootstrap-node-public-keys=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae \_20 --observer-networking-key-path=/bootstrap/network.key`
##### Observer for Flow Testnet[​](#observer-for-flow-testnet "Direct link to Observer for Flow Testnet")

 `_20docker run --rm \_20 -v $PWD/flow_observer/bootstrap:/bootstrap:ro \_20 -v $PWD/flow_observer/data:/data:rw \_20 --name flow_observer \_20 -p 80:80 \_20 -p 3569:3569 \_20 -p 9000:9000 \_20 -p 9001:9001 \_20 gcr.io/flow-container-registry/observer:v0.27.2 \_20 --bootstrapdir=/bootstrap \_20 --datadir=/data/protocol \_20 --bind 0.0.0.0:3569 \_20 --rest-addr=:80 \_20 --loglevel=error \_20 --secretsdir=/data/secrets \_20 --upstream-node-addresses=secure.devnet.nodes.onflow.org:9001 \_20 --upstream-node-public-keys=ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d \_20 --bootstrap-node-addresses=secure.devnet.nodes.onflow.org:3570 \_20 --bootstrap-node-public-keys=ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d \_20 --observer-networking-key-path=/bootstrap/network.key`

The light node acts as a DHT client and bootstraps from upstream access nodes which run the DHT server.
The upstream bootstrap server is specified using the `bootstrap-node-addresses` which is the comma-separated list of hostnames of the access nodes.
The `bootstrap-node-public-keys` is the list of the corresponding networking public key of those nodes.

The light node delegates many of the API calls to the upstream access nodes.
The `upstream-node-addresses` is the list of access node hostnames to which this light node can delegate to. The list can be different from the bootstrap node list.
The `bootstrap-node-public-key` is the list of the corresponding networking public key of those nodes.

> In the above docker commands, the Flow community access nodes are being used as the upstream access nodes. However, any other Flow access node that supports a light node can be used

*All parameters and their explanation can be found [here](https://github.com/onflow/flow-go/blob/82da35141ff095fbf75ce2c950efec240ad38565/cmd/access/node_builder/access_node_builder.go#L523-L558)*

🚀 **The node should now be up and running**

You can now query the node for blocks, transaction etc. similar to how you would query an access node.

e.g. querying the gRPC API endpoint using Flow CLI

 `_10flow blocks get latest --host localhost:9000`

e.g. querying the REST API endpoint using curl

 `_10curl "http://localhost/v1/blocks?height=sealed"`

The light node, like the other type of Flow nodes, also produces Prometheus metrics that can be used to monitor node health. More on that [here](/networks/node-ops/node-operation/node-setup#monitoring-and-metrics)

## FAQs[​](#faqs "Direct link to FAQs")

### Does the light node need to be staked?[​](#does-the-light-node-need-to-be-staked "Direct link to Does the light node need to be staked?")

No, the light node is not a staked node.

### Can any access node be used to bootstrap a light node?[​](#can-any-access-node-be-used-to-bootstrap-a-light-node "Direct link to Can any access node be used to bootstrap a light node?")

No, only Access nodes which have explicitly turned ON support for light nodes can be used to bootstrap a light node.

The public access nodes that support light nodes are listed below. Apart from these, other public access nodes run by node operators other than the Flow foundation team may choose to support light nodes.

### How can an access node turn ON support for light node?[​](#how-can-an-access-node-turn-on-support-for-light-node "Direct link to How can an access node turn ON support for light node?")

An access node can support a light node by passing in the following two parameters when starting the access node

 `_10 --supports-observer=true --public-network-address=0.0.0.0:3570`

`public-network-address` is the address the light nodes will connect to.

### Are light nodes subject to rate limits?[​](#are-light-nodes-subject-to-rate-limits "Direct link to Are light nodes subject to rate limits?")

The light node serves all the [Block related queries](https://github.com/onflow/flow/blob/master/protobuf/flow/access/access.proto#L24-L42) from is local database. These are not subjected to any rate limits.

However, it proxies all the other requests to the access node and those will be rate limited as per the rate limits defined on that access node.

### Flow community access nodes that support connections from light nodes[​](#flow-community-access-nodes-that-support-connections-from-light-nodes "Direct link to Flow community access nodes that support connections from light nodes")

#### For mainnet[​](#for-mainnet "Direct link to For mainnet")

Access-007:

* Host: `access-007.[current mainnet spork].nodes.onflow.org`
* Public Key: `28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae`

Access-008:

* Host: `access-008.[current mainnet spork].nodes.onflow.org`
* Public Key: `11742552d21ac93da37ccda09661792977e2ca548a3b26d05f22a51ae1d99b9b75c8a9b3b40b38206b38951e98e4d145f0010f8942fd82ddf0fb1d670202264a`

#### For testnet[​](#for-testnet "Direct link to For testnet")

Access-001:

* Host: `access-001.[current devnet spork].nodes.onflow.org`
* Public Key: `ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d`

Access-003:

* Host: `access-003.[current devnet spork].nodes.onflow.org`
* Public Key: `b662102f4184fc1caeb2933cf87bba75cdd37758926584c0ce8a90549bb12ee0f9115111bbbb6acc2b889461208533369a91e8321eaf6bcb871a788ddd6bfbf7`

While the public keys remain the same, the hostnames change each spork to include the spork name. Substitute `[current mainnet spork]` and `[current devnet spork]` with the appropriate spork name (e.g. `mainnet20`).
See [Past Sporks](/networks/node-ops/node-operation/past-sporks) for the current spork for each network.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/access-onchain-data/light-nodes/observer-node.md)Last updated on **Dec 20, 2024** by **Brian Doyle**[PreviousEVM Gateway Setup](/networks/node-ops/access-onchain-data/evm-gateway/evm-gateway-setup)[NextOperator FAQ](/networks/node-ops/node-operation/faq)
###### Rate this page

😞😐😊

* [Who should run a light node?](#who-should-run-a-light-node)
* [Running an light node](#running-an-light-node)
  + [Hardware](#hardware)
  + [Steps to run a light node](#steps-to-run-a-light-node)
* [FAQs](#faqs)
  + [Does the light node need to be staked?](#does-the-light-node-need-to-be-staked)
  + [Can any access node be used to bootstrap a light node?](#can-any-access-node-be-used-to-bootstrap-a-light-node)
  + [How can an access node turn ON support for light node?](#how-can-an-access-node-turn-on-support-for-light-node)
  + [Are light nodes subject to rate limits?](#are-light-nodes-subject-to-rate-limits)
  + [Flow community access nodes that support connections from light nodes](#flow-community-access-nodes-that-support-connections-from-light-nodes)
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

