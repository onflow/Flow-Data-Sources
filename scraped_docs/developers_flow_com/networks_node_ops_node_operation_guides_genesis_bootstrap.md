# Source: https://developers.flow.com/networks/node-ops/node-operation/guides/genesis-bootstrap




Genesis Bootstrapping | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* Genesis Bootstrapping
On this page
# Genesis Bootstrapping


Genesis Only

All nodes joining the network in May are required to go through this process as part of the Genesis Bootstrapping.

## Overview[​](#overview "Direct link to Overview")

To kickstart the Flow network and build the first block, all the nodes that will participate in the first round of consensus need to be known and have exchanged some metadata in advance.

This guide will take you through setting up your nodes, running the initial metadata and key generation, exchanging data back and forth with the Flow team, and then finally starting your nodes to join the network.

## Before You Begin[​](#before-you-begin "Direct link to Before You Begin")

The Flow consensus algorithm depends on there always being a previous block, which means your nodes cannot start until *after* the Genesis block has been signed. The process of signing that block will be done by the Flow team, and can only be done after every node has completed the first half of the bootstrapping process, which assures that all the identities are included. Since the Flow team needs to wait for metadata from all participants, it will take hours to even days until the Flow network can start.

The bootstrapping process will be in 2 phases, with the Flow team signing the Genesis block between the two.

Understanding Keys

The bootstrapping process deals with a number of different keys. Make sure you understand their usage and terminology by reviewing the [Node Keys Guide](/networks/node-ops/node-operation/node-bootstrap#generate-your-node-keys).

## Download the Bootstrapping Toolkit[​](#download-the-bootstrapping-toolkit "Direct link to Download the Bootstrapping Toolkit")

Both phases of the bootstrapping are automated with scripts. Pull a copy onto each of your nodes and extract it.

Pull-boot-tools `_10~ $ curl -sL -O storage.googleapis.com/flow-genesis-bootstrap/boot-tools.tar_10~ $ tar -xvf boot-tools.tar`
## Generate Your Node Keys[​](#generate-your-node-keys "Direct link to Generate Your Node Keys")

Start the bootstrapping process by generating your Staking Key and Networking Key. Use your Node Address that you generated in [Setting Up a Node](/networks/node-ops/node-operation/node-setup) in the `--address` flag, and the node role.

Node AddressYour Node Address must be a publicly routable IPv4 address or valid DNS name that points to your node. This is how other nodes in the network will communicate with you.
Generate-bootstrap-keys" `_10~ $ mkdir ./bootstrap_10~ $ ./boot-tools/bootstrap key --address \"${YOUR_NODE_ADDRESS}:3569\" --role ${YOUR_NODE_ROLE} -o ./bootstrap`
BYO Entropy

By default, the bootstrap script uses the kernel entropy source, either via a `getrandom` syscall or `/dev/urandom`. If you have a more secure source of entropy, like a hardware device, you can specify `--staking-seed` and `--networking-seed`, to provide your own seeds.

Run the `bootstrap` command with no flags to print usage information."


Protect your keys!

The key pairs generated in the bootstrapping process are extremely sensitive and must be managed securely. This guide does not deal with storing the keys in a secure backup or controlling access, as the right approach to this will vary from user to user, but it is something you must consider.

Private keys are suffixed with `.priv.json`, their public counterparts are not sensitive and can be shared freely.

This command generates two keys, a Staking Key and a Network Key, and stores them both in a `.node-info` file. Both these keys are needed during runtime and must be present as a file to start your flow node.

For more details around all the keys that are needed to run nodes and their usage, see the [Node Keys](/networks/node-ops/node-operation/node-bootstrap#generate-your-node-keys) overview.

The bootstrapping process will create a file structure similar to the following

bootstrap-directory `_10~_10└──bootstrap_10 ├──{id}.node-info.priv.json_10 └──{id}.node-info.pub.json",`
## Upload Public Keys[​](#upload-public-keys "Direct link to Upload Public Keys")

To mint the Genesis Block, the Flow team will need the public Staking and Network keys from all your nodes.

**If you have previously joined our networks, and you are generating your keys again. Ensure that you take a backup of your keys before generating it again**

To facilitate this, the boot-tools directory comes with a script `push-keys` that will bundle your `*.pub.json` files and send it to the flow team. You can inspect this script to make sure no private key material is being bundled or uploaded. The data not encrypted before being sent as the public keys involved are not sensitive.

In phase 2 of the bootstrapping process, the Flow team will need to securely issue each node a Random Beacon key. This key is again sensitive and unique to your node. To enable this, the `push-keys` script also generates another key pair called the Transit Key. The public key of this pair will be uploaded along with the Staking and Network keys, and your Random Beacon key will be encrypted with it before being sent to you. You must keep your Transit Key until you have received and decrypted your Random Beacon key from the Flow team.

Token Needed

The transit script here need a `-t` token parameter flag. This token will have been provided to you by the Flow team out of band. Reach out to your contact if you don't have your token.


Upload-public-keys `_10# If you joined our network previously, make sure to take a backup!_10cp /path/to/bootstrap /path/to/bootstrap.bak_10$ ./boot-tools/transit push -d ./bootstrap -t ${TOKEN} -role ${YOUR_NODE_ROLE}_10Running push_10Generating keypair_10Uploading ..._10Uploaded 400 bytes`
One and Done!

Once you've run the bootstrap and are confident in your setup, run the transit push command only once. If you bootstrap again and transit push again with a new node ID, it will count against your quota of Nodes. Exceeding your quota will result in a long back and forth with the Flow team to see which node is the extra one.

## Update Node Config[​](#update-node-config "Direct link to Update Node Config")

As flow node requires a `--nodeid` flag to start. You will need to pass in the contents of the `node-id` into either your container, `runtime-config.env` file, or hard coded into the `systemd` unit file which the flow team provides.

You can get the `node-id` from the metadata that you pulled. It will be at: `/path/to/bootstrap/public-genesis-information/node-id`

### Wait[​](#wait "Direct link to Wait")

Now the ball is in the Flow team's court. As soon as all nodes have completed the above steps, the Genesis block will be created and distributed to you.

Join the [Flow discord server](https://chat.onflow.org) if you haven't already and stay tuned for updates. Your nodes need not be online during this waiting period if you want to suspend them to reduce cost, but you must not lose your key material.

A Note on Staking

For the Genesis Block, your nodes will start pre-staked, which means no action on your part is needed to get your nodes staked.

For more details on staking check the guide on [Staking and Rewards](/networks/staking/staking-rewards).

## Receive Your Random Beacon Keys[​](#receive-your-random-beacon-keys "Direct link to Receive Your Random Beacon Keys")

When the Flow team gives the go-ahead, your Random Beacon keys will be available for retrieval. Each Node will need to pull their own keys down individually.

Pull-beacon-keys `_10~ $ ./boot-tools/transit pull -d ./bootstrap -t ${TOKEN} -role ${YOUR_NODE_ROLE}_10Fetching keys for node ID FEF5CCFD-DC66-4EF6-8ADB-C93D9B6AE5A4_10Decrypting Keys_10Keys available`

Pulling your keys will also pull a bunch of additional metadata needed for the bootstrapping process.
In the end, your bootstrap directory should look like this:

bootstrap-directory `_19~_19bootstrap/_19├── private-genesis-information_19│ └── private-node-info_{node id}_19│ ├── node-info.priv.json_19│ └── random-beacon.priv.json_19├── public-genesis-information_19│ ├── dkg-data.pub.json_19│ ├── genesis-block.json_19│ ├── genesis-cluster-block.{cid}.json_19│ ├── genesis-cluster-block.{cid}.json_19│ ├── genesis-cluster-qc.{cid}.json_19│ ├── genesis-cluster-qc.{cid}.json_19│ ├── genesis-commit.json_19│ ├── genesis-qc.json_19│ ├── node-id_19│ ├── node-info.pub.{node id}.json_19│ └── node-infos.pub.json_19├── <additional files...>`
Why are we generating the beacon keys for you?

Unlike staking and account keys, the beacon keys are not randomly generated, and depend on inputs from all consensus nodes on the network. In typical Flow network operation, these keys will be dynamically generated on demand by the consensus nodes communicating. However for genesis, as the consensus nodes aren't communicating yet, the Flow team will generate and distribute them to kickstart the process.

## Move Genesis Data[​](#move-genesis-data "Direct link to Move Genesis Data")

This bootstrapping data is needed by your node at each startup, so it must be present on disk.

Where in the filesystem you store this data is up to you, but you may not change the folder structure generated by the bootstrapping process. By default, flow stores this data under `/var/flow/bootstrap`.

## New Images[​](#new-images "Direct link to New Images")

Once the Genesis block has been minted, it will be included into the official container images so that it's available to all nodes. Pull the new images, which should now be version `v1.0.0`.

## Start Your Nodes[​](#start-your-nodes "Direct link to Start Your Nodes")

Once every node has puled its keys and fetched the new images, the network is ready to start.

Make sure you're part of the [Discord Chat](https://chat.onflow.org). Once all nodes are ready, updates will be provided to everyone.

Start your systems, let's make some blocks!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/guides/genesis-bootstrap.md)Last updated on **Jan 28, 2025** by **Giovanni Sanchez**[PreviousDatabase Encryption for Existing Node Operators](/networks/node-ops/node-operation/db-encryption-existing-operator)[NextSpork Practice](/networks/node-ops/node-operation/guides/spork-practice)
###### Rate this page

😞😐😊

* [Overview](#overview)
* [Before You Begin](#before-you-begin)
* [Download the Bootstrapping Toolkit](#download-the-bootstrapping-toolkit)
* [Generate Your Node Keys](#generate-your-node-keys)
* [Upload Public Keys](#upload-public-keys)
* [Update Node Config](#update-node-config)
  + [Wait](#wait)
* [Receive Your Random Beacon Keys](#receive-your-random-beacon-keys)
* [Move Genesis Data](#move-genesis-data)
* [New Images](#new-images)
* [Start Your Nodes](#start-your-nodes)
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

