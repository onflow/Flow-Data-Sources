# Source: https://developers.flow.com/networks/node-ops/access-nodes/access-node-setup

Setting Up a Flow Access Node | Flow Developer Portal



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

    - [Access Node Setup](/networks/node-ops/access-nodes/access-node-setup)
    - [Execution Data](/networks/node-ops/access-nodes/access-node-configuration-options)
  + [EVM Gateway Setup](/networks/node-ops/evm-gateway/evm-gateway-setup)
  + [Light Nodes](/networks/node-ops/light-nodes/observer-node)
  + [Participating in the Network](/networks/node-ops/node-operation/faq)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Node Ops](/networks/node-ops)
* Access Nodes
* Access Node Setup

On this page

# Setting Up a Flow Access Node



This guide is for running a permissonless Access node on Flow. If you are planning to run a different type of staked node then see [node bootstrap](/networks/node-ops/node-operation/node-bootstrap).

Permissionless Access nodes allow any operator to run a Flow Access node.
Unlike the other staked nodes, a permissionless access node does not have to be approved by the service account before it can join the network, hence the term "permissionless". The goal is to make all node types permissionless and this is the first step towards achieving that goal.

## Who Should Run a Permissionless Access Node?[​](#who-should-run-a-permissionless-access-node "Direct link to Who Should Run a Permissionless Access Node?")

dApp developers can choose to run their own private permissionless access node and move away from using the community access nodes. This will also allow them to not be subjected to the API rate limits of the public access nodes.

Node operators can also run their own permissionless access node and provide access to that node as a service.

Chain analytics, audit and exploration applications can run such an access node and do not have to rely on third parties for the state of the network.

## Timing[​](#timing "Direct link to Timing")

New nodes are able to join the network each time a new epoch begins.
An epoch is a period of time (approximately one week) when the node operators in the network are constant.
At epoch boundaries, newly staked node operators are able to join the network and existing node operators which have unstaked may exit the network.
You can read more about epochs [here](/networks/staking/schedule).

In order to join the network at epoch N+1, the access node **must** be registered with at least 100 FLOW staked prior to the end of epoch N's Staking Auction Phase.

Currently on mainnet, the staking auction starts every Wednesday at around 20:00 UTC and ends on the next Wednesday at around 12:00 UTC.
Since this deadline may shift slightly from epoch to epoch, we recommend the node be staked by *Wednesday, 8:00 UTC* to be able to join the network in the next epoch.

Confirmation of a new node's inclusion in epoch N+1 is included in the [`EpochSetup` event](/networks/staking/epoch-scripts-events#flowepochepochsetup).

![Flow Epoch Schedule](/assets/images/epoch-startup-order-a681148257381a50bda69320c930fc1a.png)

## Limitations[​](#limitations "Direct link to Limitations")

There are five open slots for access nodes every epoch.
You can view the exact epoch phase transition time [here](https://dashboard.flow.com/) under `Epoch Phase`.

To summarize,

| **Epoch** | **Epoch Phase** |  |
| --- | --- | --- |
| N | Staking auction starts | Three new access node slots are opened. Anyone can register their access nodes |
| N | Staking auction ends | Three of the nodes registered during this epoch are randomly selected to be a part of the network in the next epoch. No more nodes can register until the next epoch starts. |
| N+1 | Epoch N+1 starts | The newly selected nodes can now participate in the network. Three new slots are opened. |

## How To Run a Permissionless Access Node?[​](#how-to-run-a-permissionless-access-node "Direct link to How To Run a Permissionless Access Node?")

note

To run an access node you will need to provision a machine or virtual machine to run your node software. Please follow the [node-provisioning](/networks/node-ops/node-operation/node-provisioning) guide for it.
You can provision the machine before or after your node has been chosen.

At a high level, to run a permissionless Access node, you will have to do the following steps:

1. Generate the node identity (private and public keys, node ID etc.).
2. Stake the node with 100 FLOW by the end of the staking phase of the current epoch (see [timing](#timing)) by providing the node information generated in step 1.
3. You can verify if your node ID was selected by the on-chain random selection process on Wednesday at around 20:00 UTC when the next epoch starts.
4. If your node ID was selected, you can provision and start running the node. If your node wasn't selected, your tokens will have been refunded to your unstaked bucket in the staking smart contract. When the next epoch begins, you can try committing tokens again in a future epoch to get a new spot.

Following is a detail explanation of these four steps.
If you want to run multiple access nodes, you will have to run through these steps for each node.

## Step 1 - Generate Node Information[​](#step--1---generate-node-information "Direct link to Step 1 - Generate Node Information")

### Download the Bootstrapping Kit[​](#download-the-bootstrapping-kit "Direct link to Download the Bootstrapping Kit")

`_10

curl -sL -O storage.googleapis.com/flow-genesis-bootstrap/boot-tools.tar

_10

tar -xvf boot-tools.tar`

CheckSHA256

`_10

sha256sum ./boot-tools/bootstrap

_10

460cfcfeb52b40d8b8b0c4641bc4e423bcc90f82068e95f4267803ed32c26d60 ./boot-tools/bootstrap`

> If you have downloaded the bootstrapping kit previously, ensure the SHA256 hash for it still matches. If not, re-download to ensure you are using the most up-to-date version.

### Generate Your Node Identity[​](#generate-your-node-identity "Direct link to Generate Your Node Identity")

`_10

#########################################################

_10

# Generate Keys

_10

$ mkdir ./bootstrap

_10

# YOUR_NODE_ADDRESS: FQDN associated to your instance

_10

$ ./boot-tools/bootstrap key --address "<YOUR_NODE_ADDRESS_GOES_HERE>:3569" --role access -o ./bootstrap`

Example

`_25

$./boot-tools/bootstrap key --address "flowaccess.mycompany.com:3569" --role access -o ./bootstrap

_25

<nil> DBG will generate networking key

_25

<nil> INF generated networking key

_25

<nil> DBG will generate staking key

_25

<nil> INF generated staking key

_25

<nil> DBG will generate db encryption key

_25

<nil> INF generated db encryption key

_25

<nil> DBG assembling node information address=flowaccess.mycompany.com:3569

_25

<nil> DBG encoded public staking and network keys networkPubKey=f493a74704f6961ae7903e062ecd58d990672858eff99aece7bfbccf3aa02de8f1a624ecbf21a01e8b2f4a5854c231fbe218edd7762a34fea881f3958a215305 stakingPubKey=ae8dcf81f3a70d72036b7ba2c586ed37ed0eb82b9c0a4aab998a8420f98894f94c14f84fa716e93654d3940fc0c8ff4d19b504c90a5b4918b28f421e9d3659dc2b7e246025ebeffea0d83cceefe315d7ed346dbe412fdac51b64997d97d29f7e

_25

<nil> INF wrote file bootstrap/public-root-information/node-id

_25

<nil> INF wrote file bootstrap/private-root-information/private-node-info_e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5/node-info.priv.json

_25

<nil> INF wrote file bootstrap/private-root-information/private-node-info_e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5/secretsdb-key

_25

<nil> INF wrote file bootstrap/public-root-information/node-info.pub.e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5.json

_25

_25

$tree ./bootstrap/

_25

./bootstrap/

_25

├── private-root-information

_25

│ └── private-node-info_e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5

_25

│ ├── node-info.priv.json

_25

│ └── secretsdb-key

_25

└── public-root-information

_25

├── node-id

_25

└── node-info.pub.e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5.json

_25

_25

3 directories, 4 files`

warning

*Use a fully qualified domain name for the network address. Please also include the port number in the network address e.g. `flowaccess.mycompany.com:3569`*

warning

*Do not include the prefix `http://` in the network address.*

tip

If you would like to stake multiple access nodes, please ensure you generate a unique identity for each node.

Your node identity has now been generated. Your **node ID** can be found in the file `./bootstrap/public-root-information/node-id`.

Example

`_10

$cat ./bootstrap/public-root-information/node-id

_10

e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5`

info

All your private keys should be in the `bootstrap` folder created earlier. Please take a back up of the entire folder.

## Step 2 - Stake the Node[​](#step--2---stake-the-node "Direct link to Step 2 - Stake the Node")

You need to now register the node on chain by staking the node via [Flow Port](https://port.onflow.org/).

[Here](/networks/flow-port/staking-guide) is a guide on how to use Flow port if you are not familiar with it.
If you are staking via a custody provider or would like to directly submit a staking transaction instead follow this [guide](/networks/staking#how-do-i-stake).

Fund you Flow account with at least 100.01 FLOW tokens, which covers the required stake plus the storage deposit.

On Flow port, choose `Stake and Delegate` -> `Start Staking` or `Stake Again` and then choose Access node as the option.

![choose_access_flowport](/assets/images/choose_access_flowport-fc34e834ae5adb774cfcfcba4729757b.png)

On the next screen, provide the node details of you node.

Those node details (`Node ID`, `Network Address`, `Networking Key` and `Staking Key`) can be found in the file: `./bootstrap/public-root-information/node-info.pub.<node-id>.json`.

Example

`_10

$cat ./bootstrap/public-root-information/node-info.pub. e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5.json

_10

{

_10

"Role": "access",

_10

"Address": "flowaccess.mycompany.com:3569",

_10

"NodeID": "e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5",

_10

"Weight": 0,

_10

"NetworkPubKey": "f493a74704f6961ae7903e062ecd58d990672858eff99aece7bfbccf3aa02de8f1a624ecbf21a01e8b2f4a5854c231fbe218edd7762a34fea881f3958a215305",

_10

"StakingPubKey": "ae8dcf81f3a70d72036b7ba2c586ed37ed0eb82b9c0a4aab998a8420f98894f94c14f84fa716e93654d3940fc0c8ff4d19b504c90a5b4918b28f421e9d3659dc2b7e246025ebeffea0d83cceefe315d7ed346dbe412fdac51b64997d97d29f7e"

_10

}`

#### Example[​](#example "Direct link to Example")

![node_details_permissionless_an](/assets/images/node_details_permissionless_an-14d8b6ff5e900551986f937cac9bd738.png)

On the next screen, ensure that you stake 100 FLOW token.

#### Example[​](#example-1 "Direct link to Example")

![transaction_register_node_permissionless_an](/assets/images/transaction_register_node_permissionless_an-9eb44629ec2075547aee2ad35e42744c.png)

Submit the Transaction.

## Step 3 - Verify That Your Node ID Was Selected[​](#step-3---verify-that-your-node-id-was-selected "Direct link to Step 3 - Verify That Your Node ID Was Selected")

On Wednesday at around 12:00 UTC, the staking auction for the current epoch will end and five nodes from candidate list of nodes will be chosen at random by the staking contract to be part of the next epoch.

note

If all 5 slots have been taken from the previous epoch, then no new access nodes will be chosen (see #limitations)

There are several ways to verify whether your node was chosen as explained below.

When you stake the node, the tokens will show up under the `tokensCommitted` bucket. After the staking auction ends, if the node is selected, the tokens remain in the `tokensCommitted` bucket and are moved to the `tokensStaked` bucket at the end of the epoch.
If the node is not selected, the tokens are moved to the `tokensUnstaked` bucket.

### Check Using Flow Port[​](#check-using-flow-port "Direct link to Check Using Flow Port")

You can check these balances on Flow Port before and after the epoch transition that will occur on Wednesday (see [timing](#timing)).

When you stake the node, you should see the following on Flow Port under `Stake & Delegate`

![Staked_node](/assets/images/Staked_FlowPort-4f1b3c618f615d99208fb8d0fe0b9023.png)

After the epoch transition, if you see you token balance under the Staked Amount then your node got chosen.

![Staked_node](/assets/images/Selected_FlowPort-908de4520a64c15c6dfd74dc32f8e247.png)

Instead, if you see that your token balance is under the Unstaked Amount, then your node did not get chosen.

![Unstaked_node](/assets/images/Unstaked_FlowPort-74ca70b601e5baf4c3a214de6d8c05ad.png)

### Check Using Flow CLI[​](#check-using-flow-cli "Direct link to Check Using Flow CLI")

You can also check these balance using [Flow Cli](https://github.com/onflow/flow-cli). Once you have downloaded and installed Flow Cli, you can query the account balance using the command,

`_10

flow accounts staking-info <your account address> -n mainnet`

For Example, the following node was chosen as Tokens staked is 100.

Example

`_16

$ flow accounts staking-info 0xefdfb20806315bfa -n testnet

_16

_16

Account staking info:

_16

ID: "e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5"

_16

Initial Weight: 100

_16

Networking Address: "flowaccess.mycompany.com:3569"

_16

Networking Key: "f493a74704f6961ae7903e062ecd58d990672858eff99aece7bfbccf3aa02de8f1a624ecbf21a01e8b2f4a5854c231fbe218edd7762a34fea881f3958a215305"

_16

Role: 5

_16

Staking Key: "ae8dcf81f3a70d72036b7ba2c586ed37ed0eb82b9c0a4aab998a8420f98894f94c14f84fa716e93654d3940fc0c8ff4d19b504c90a5b4918b28f421e9d3659dc2b7e246025ebeffea0d83cceefe315d7ed346dbe412fdac51b64997d97d29f7e"

_16

Tokens Committed: 0.00000000

_16

Tokens To Unstake: 100.00000000

_16

Tokens Rewarded: 0.00000000

_16

Tokens Staked: 100.00000000

_16

Tokens Unstaked: 0.00000000

_16

Tokens Unstaking: 0.00000000

_16

Node Total Stake (including delegators): 0.00000000`

### Epoch Setup Event[​](#epoch-setup-event "Direct link to Epoch Setup Event")

Alternatively, if you can monitor events, look for [the epoch setup event](/networks/staking/epoch-scripts-events#flowepochepochsetup) that gets emitted by the epoch contract. That event is emitted at the end of epoch N's staking auction and contains a list of node IDs that are confirmed for the next epoch.

## Step 4 - Start Your Node[​](#step-4---start-your-node "Direct link to Step 4 - Start Your Node")

If your node was selected as part of Step 3, you can now start your node.

First you'll need to provision a machine or virtual machine to run your node software. Please see follow the [node-provisioning](/networks/node-ops/node-operation/node-provisioning) guide for it.

The access node can be run as a Docker container with the following command.

Be sure to set `$VERSION` below to the version tag (e.g. `v1.2.3`) corresponding to the latest **released** version [here](https://github.com/onflow/flow-go/releases) for version releases). Set `$NODEID` to your node's ID (see [Generate Your Node Identity](#generate-your-node-identity) section above).

* Mainnet
* Testnet

`_19

docker run --rm \

_19

-v $PWD/bootstrap:/bootstrap:ro \

_19

-v $PWD/data:/data:rw \

_19

--name flow-go \

_19

--network host \

_19

gcr.io/flow-container-registry/access:$VERSION \

_19

--nodeid=$NODEID \

_19

--bootstrapdir=/bootstrap \

_19

--datadir=/data/protocol \

_19

--secretsdir=/data/secrets \

_19

--rpc-addr=0.0.0.0:9000 \

_19

--http-addr=0.0.0.0:8000 \

_19

--rest-addr=0.0.0.0:80 \

_19

--rpc-metrics-enabled=true \

_19

--bind 0.0.0.0:3569 \

_19

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_19

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae \

_19

--dynamic-startup-epoch-phase=EpochPhaseStaking \

_19

--loglevel=error`

`_19

docker run --rm \

_19

-v $PWD/bootstrap:/bootstrap:ro \

_19

-v $PWD/data:/data:rw \

_19

--name flow-go \

_19

--network host \

_19

gcr.io/flow-container-registry/access:$VERSION \

_19

--nodeid=$NODEID \

_19

--bootstrapdir=/bootstrap \

_19

--datadir=/data/protocol \

_19

--secretsdir=/data/secrets \

_19

--rpc-addr=0.0.0.0:9000 \

_19

--http-addr=0.0.0.0:8000 \

_19

--rest-addr=0.0.0.0:80 \

_19

--rpc-metrics-enabled=true \

_19

--bind 0.0.0.0:3569 \

_19

--dynamic-startup-access-address=secure.testnet.nodes.onflow.org:9001 \

_19

--dynamic-startup-access-publickey=ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d \

_19

--dynamic-startup-epoch-phase=EpochPhaseStaking \

_19

--loglevel=error`

For example, if your Node ID is `e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5` and the software version is `v1.2.3`, the Docker command would be the following:

Example

`_19

docker run --rm \

_19

-v $PWD/bootstrap:/bootstrap:ro \

_19

-v $PWD/data:/data:rw \

_19

--name flow-go \

_19

--network host \

_19

gcr.io/flow-container-registry/access:v1.2.3 \

_19

--nodeid=e737ec6efbd26ef43bf676911cdc5a11ba15fc6562d05413e6589fccdd6c06d5 \

_19

--bootstrapdir=/bootstrap \

_19

--datadir=/data/protocol \

_19

--secretsdir=/data/secrets \

_19

--rpc-addr=0.0.0.0:9000 \

_19

--http-addr=0.0.0.0:8000 \

_19

--rest-addr=0.0.0.0:80 \

_19

--rpc-metrics-enabled=true \

_19

--bind 0.0.0.0:3569 \

_19

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_19

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae \

_19

--dynamic-startup-epoch-phase=EpochPhaseStaking \

_19

--loglevel=error`

> If you would like your node to sync from the start of the last network upgrade, then please see the instructions [here](https://developers.flow.com/networks/node-ops/node-operation/spork)

Alternatively, you can build a binary for the access node to run it without using Docker.
To build the access node binary, see the instructions [here](https://github.com/onflow/flow-go?tab=readme-ov-file#building-a-binary-for-the-access-node).
Please make sure to git checkout the latest release tag before building the binary.

* Mainnet
* Testnet

`_18

$PWD/flow-go/flow_access_node \

_18

--nodeid=e1a8b231156ab6f2a5c6f862c933baf5e5c2e7cf019b509c7c91f4ddb0a13398 \

_18

--bootstrapdir=$PWD/bootstrap \

_18

--datadir=$PWD/data/protocol \

_18

--secretsdir=$PWD/data/secrets \

_18

--execution-data-dir=$PWD/data/execution_data \

_18

--rpc-addr=0.0.0.0:9000 \

_18

--secure-rpc-addr=0.0.0.0:9001 \

_18

--http-addr=0.0.0.0:8000 \

_18

--rest-addr=0.0.0.0:8070 \

_18

--admin-addr=localhost:9002 \

_18

--bind=0.0.0.0:3569 \

_18

--dht-enabled=false \

_18

--grpc-compressor=gzip \

_18

--profiler-dir=$PWD/data/profiler \

_18

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_18

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae \

_18

--dynamic-startup-epoch-phase=EpochPhaseStaking`

`_18

$PWD/flow-go/flow_access_node \

_18

--nodeid=e1a8b231156ab6f2a5c6f862c933baf5e5c2e7cf019b509c7c91f4ddb0a13398 \

_18

--bootstrapdir=$PWD/bootstrap \

_18

--datadir=$PWD/data/protocol \

_18

--secretsdir=$PWD/data/secrets \

_18

--execution-data-dir=$PWD/data/execution_data \

_18

--rpc-addr=0.0.0.0:9000 \

_18

--secure-rpc-addr=0.0.0.0:9001 \

_18

--http-addr=0.0.0.0:8000 \

_18

--rest-addr=0.0.0.0:8070 \

_18

--admin-addr=localhost:9002 \

_18

--bind=0.0.0.0:3569 \

_18

--dht-enabled=false \

_18

--grpc-compressor=gzip \

_18

--profiler-dir=$PWD/data/profiler \

_18

--dynamic-startup-access-address=secure.testnet.nodes.onflow.org:9001 \

_18

--dynamic-startup-access-publickey=ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d \

_18

--dynamic-startup-epoch-phase=EpochPhaseStaking`

For a more mature setup, it is recommended that you run the container using systemd as described [here](/networks/node-ops/node-operation/node-setup#systemd)

> 🚀 The access node should now be up and running, and you should be able to query the node using Flow CLI or curl,

Example

`_10

flow blocks get latest --host localhost:9000`

Example

`_10

curl http://localhost/v1/blocks?height=sealed`

## Monitoring and Metrics[​](#monitoring-and-metrics "Direct link to Monitoring and Metrics")

The node publishes several Prometheus metrics. See [Monitoring Node Health](/networks/node-ops/node-operation/monitoring-nodes) to setup node monitoring.

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

## FAQs[​](#faqs "Direct link to FAQs")

### Will the access node receive rewards?[​](#will-the-access-node-receive-rewards "Direct link to Will the access node receive rewards?")

No, the access nodes do not receive any rewards.

### Why is there a 100 FLOW token minimum?[​](#why-is-there-a-100-flow-token-minimum "Direct link to Why is there a 100 FLOW token minimum?")

As mentioned in the [FLIP](https://github.com/onflow/flips/blob/main/protocol/20220719-automated-slot-assignment.md), the minimum is required to prevent certain vulnerabilities
in the smart contract that are a result of having a zero minimum stake requirement.

### Can the Access node be unstaked?[​](#can-the-access-node-be-unstaked "Direct link to Can the Access node be unstaked?")

Yes, like any other staked node, the Access node can be unstaked. The staked tokens will be moved to the unstaked bucket in the subsequent epoch.

### How to see all the access nodes that have staked?[​](#how-to-see-all-the-access-nodes-that-have-staked "Direct link to How to see all the access nodes that have staked?")

When the nodes are initially staked, they are all added to the candidate list of nodes before the end of the epoch staking phase.
The list can be retrieved from the chain by executing the [get\_candidate\_nodes](https://github.com/onflow/flow-core-contracts/blob/48ba17d3386023d70817197a20effbc5d16339b3/transactions/idTableStaking/scripts/get_candidate_nodes.cdc) script which returns the candidate list for the current epoch.

`_10

$ flow scripts execute ./transactions/idTableStaking/scripts/get_candidate_nodes.cdc -n mainnet`

### How to check the availability of open access nodes slots for the next epoch?[​](#how-to-check-the-availability-of-open-access-nodes-slots-for-the-next-epoch "Direct link to How to check the availability of open access nodes slots for the next epoch?")

The limits for the open slots are defined in the staking contract and can be queried from the chain by executing the [get\_slot\_limits](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_slot_limits.cdc) script.

Node types are defined [here](https://github.com/onflow/flow-core-contracts/blob/5696ec5e3e6aa5fc10762cbfeb42b9c5c0b8ddbe/contracts/FlowIDTableStaking.cdc#L114-L119)

`_10

_10

$ flow scripts execute ./transactions/idTableStaking/scripts/get_slot_limits.cdc --args-json '[{ "type":"UInt8", "value":"5"}]' -n mainnet

_10

Result: 118`

Example: there are 115 access nodes already part of the network. Hence, the total number of new nodes that can join are 118 - 115 = 3.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/access-nodes/access-node-setup.md)

Last updated on **Mar 6, 2025** by **Giovanni Sanchez**

[Previous

Node Operations](/networks/node-ops)[Next

Execution Data](/networks/node-ops/access-nodes/access-node-configuration-options)

###### Rate this page

😞😐😊

* [Who Should Run a Permissionless Access Node?](#who-should-run-a-permissionless-access-node)
* [Timing](#timing)
* [Limitations](#limitations)
* [How To Run a Permissionless Access Node?](#how-to-run-a-permissionless-access-node)
* [Step 1 - Generate Node Information](#step--1---generate-node-information)
  + [Download the Bootstrapping Kit](#download-the-bootstrapping-kit)
  + [Generate Your Node Identity](#generate-your-node-identity)
* [Step 2 - Stake the Node](#step--2---stake-the-node)
* [Step 3 - Verify That Your Node ID Was Selected](#step-3---verify-that-your-node-id-was-selected)
  + [Check Using Flow Port](#check-using-flow-port)
  + [Check Using Flow CLI](#check-using-flow-cli)
  + [Epoch Setup Event](#epoch-setup-event)
* [Step 4 - Start Your Node](#step-4---start-your-node)
* [Monitoring and Metrics](#monitoring-and-metrics)
  + [Node Status](#node-status)
* [FAQs](#faqs)
  + [Will the access node receive rewards?](#will-the-access-node-receive-rewards)
  + [Why is there a 100 FLOW token minimum?](#why-is-there-a-100-flow-token-minimum)
  + [Can the Access node be unstaked?](#can-the-access-node-be-unstaked)
  + [How to see all the access nodes that have staked?](#how-to-see-all-the-access-nodes-that-have-staked)
  + [How to check the availability of open access nodes slots for the next epoch?](#how-to-check-the-availability-of-open-access-nodes-slots-for-the-next-epoch)

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