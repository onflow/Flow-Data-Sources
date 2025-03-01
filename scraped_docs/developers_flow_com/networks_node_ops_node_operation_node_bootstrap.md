# Source: https://developers.flow.com/networks/node-ops/node-operation/node-bootstrap

Node Bootstrap | Flow Developer Portal



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
* Node Bootstrapping

On this page

# Node Bootstrap

This guide is for getting a new node staked and running on Flow other than a permissionless Access node. For running a permissionless Access node see [Access node setup](/networks/node-ops/access-nodes/access-node-setup). For sporking documentation for existing node operators, see [Spork Process](/networks/node-ops/node-operation/spork).

## Timing[​](#timing "Direct link to Timing")

New nodes are able to join the network each time a new epoch begins.
In order to join the network at epoch N+1, the node must be registered with sufficient stake and
authorized by the service account prior to the end of epoch N's Staking Auction Phase.
Confirmation of a new node's inclusion in epoch N+1 is included in the [`EpochSetup` event](/networks/staking/epoch-scripts-events#flowepochepochsetup).

Nodes registered for epoch N+1 are able to participate in network communication on a limited basis starting in the `Epoch Setup Phase` of epoch N.

![Flow Epoch Schedule](https://storage.googleapis.com/flow-resources/documentation-assets/epoch-startup-order.png)

Once registered and confirmed to join the network at epoch N+1, the node must start up **before** epoch N+1 begins.

* Verification & Access nodes may start up any time during the `Epoch Setup Phase`.
* Consensus & Collection nodes must start up within the first **1000 views (~30mins)**
  of the `Epoch Setup Phase` to participate in the [Epoch Preparation Protocol](/networks/staking/epoch-preparation#phase-1-epoch-setup).

## Step 1 - Run Genesis Bootstrap[​](#step-1---run-genesis-bootstrap "Direct link to Step 1 - Run Genesis Bootstrap")

info

You will need to run this process for each node that you are operating

### Download the Bootstrapping Kit[​](#download-the-bootstrapping-kit "Direct link to Download the Bootstrapping Kit")

warning

If you have downloaded the bootstrapping kit previously, ensure you check the hash below still matches. If not, re-download to ensure you are using the most up-to-date version.

`_10

curl -sL -O storage.googleapis.com/flow-genesis-bootstrap/boot-tools.tar

_10

tar -xvf boot-tools.tar

_10

chmod +x ./boot-tools/bootstrap

_10

chmod +x ./boot-tools/transit`

CheckSHA256

`_10

sha256sum ./boot-tools/bootstrapcmd

_10

460cfcfeb52b40d8b8b0c4641bc4e423bcc90f82068e95f4267803ed32c26d60 ./boot-tools/bootstrap

_10

_10

sha256sum ./boot-tools/transit

_10

f146bdc82ce0cce73c0fb9de284b2e2639e851120f8b89a1dd9368e8442123b4 ./boot-tools/transit`

### Generate Your Node Keys[​](#generate-your-node-keys "Direct link to Generate Your Node Keys")

#### Network Address[​](#network-address "Direct link to Network Address")

info

Use a fully qualified domain name for the network address. Please also include the port number in the network address e.g. `example.com:3569`

warning

Do not include in `http://` format.

info

If you are running multiple nodes, please
ensure you have different addresses for each node.

warning

All your current keys and Flow genesis files should be in the `bootstrap`
folder created earlier. Please take a back up of the entire folder.

`_10

## Skip this section if this is your first time ##

_10

# If you joined our network previously, make sure to take a backup of your previously generated keys!

_10

cp -r /path/to/bootstrap /path/to/bootstrap.bak

_10

#########################################################

_10

# Generate Keys

_10

$ mkdir ./bootstrap

_10

# YOUR_NODE_ADDRESS: FQDN associated to your instance (do NOT use an IP address, use a hostname)

_10

# YOUR_NODE_ROLE: The Flow nodes that you wish to run, it should be ONE of the following - [ access, collection, consensus, execution, verification ]

_10

$ ./boot-tools/bootstrap key --address \"YOUR_NODE_ADDRESS_GOES_HERE:3569\" --role YOUR_NODE_ROLE_GOES_HERE -o ./bootstrap`

Example

`_31

$./boot-tools/bootstrap key --address "consensus-001.nodes.flow.com:3569" --role consensus -o ./bootstrap

_31

<nil> DBG will generate networking key

_31

<nil> INF generated networking key

_31

<nil> DBG will generate staking key

_31

<nil> INF generated staking key

_31

<nil> DBG will generate db encryption key

_31

<nil> INF generated db encryption key

_31

<nil> DBG assembling node information address=consensus-001.nodes.flow.com:3569

_31

<nil> DBG encoded public staking and network keys networkPubKey=7f31ae79017a2a58a5e59af9184f440d08885a16614b2c4e361019fa72a9a1a42bf85b4e3f9674782f12ca06afd9782e9ccf19496baed069139385b82f8f40f6 stakingPubKey=829d086b292d84de8e7938fd2fafa8f51a6e025f429291835c20e59d9e25665febf24fa59de12a4df08be7e82c5413180cc7b1c73e01f26e05344506aaca4fa9cc009dc1c33f8ba3d7c7509e86d3d3e7341b43b9bf80bb9fba56ae0b3135dd72

_31

<nil> INF wrote file bootstrap/public-root-information/node-id

_31

<nil> INF wrote file bootstrap/private-root-information/private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9/node-info.priv.json

_31

<nil> INF wrote file bootstrap/private-root-information/private-node-info_5e44ad5598bb0acb44784f629e84000ffea34d5552427247d9008ccf147fb87f/secretsdb-key

_31

<nil> INF wrote file bootstrap/public-root-information/node-info.pub.ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9.json

_31

<nil> DBG will generate machine account key

_31

<nil> INF generated machine account key

_31

<nil> DBG assembling machine account information address=consensus-001.nodes.flow.com:3569

_31

<nil> INF encoded machine account public key for entry to Flow Port machineAccountPubKey=f847b8406e8969b869014cd1684770a8db02d01621dd1846cdf42fc2bca3444d2d55fe7abf740c548639cc8451bcae0cd6a489e6ff59bb6b38c2cfb83e095e81035e507b02038203e8

_31

<nil> INF wrote file bootstrap/private-root-information/private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9/node-machine-account-key.priv.json

_31

_31

$tree ./bootstrap/

_31

./bootstrap

_31

├── private-root-information

_31

│ └── private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9

_31

│ ├── node-info.priv.json

_31

│ ├─  ─ node-machine-account-key.priv.json

_31

│ └── secretsdb-key

_31

└── public-root-information

_31

├── node-id

_31

└── node-info.pub.ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9.json

_31

_31

3 directories, 4 files`

info

For `consensus` and `collection` node types an additional key will be created for the Machine Account.
For all other node types this will not be needed.

#### Machine Account Creation[​](#machine-account-creation "Direct link to Machine Account Creation")

If you are running a collection and consensus node, you will have an additional private key file (`node-machine-account-key.priv.json`)
which contains the private key for your node's machine account. You can learn more about machine
accounts [here](/networks/staking/machine-account).

In Step 2 of this guide, when you submit a transaction to stake your node, you will need to provide the
machine account public key, which can be found in the output of the previous `bootstrap key` command.

MachineAccountPublicKey

`_10

$./boot-tools/bootstrap key --address YOUR_NODE_ADDRESS_GOES_HERE --role YOUR_NODE_ROLE_GOES_HERE -o ./bootstrap

_10

...

_10

<nil> DBG encoded public machine account key machineAccountPubKey=1b9c00e6f0930792c5738d3397169f8a592416f334cf11e84e6327b98691f2b72158b40886a4c3663696f96cd15bfb5a08730e529f62a00c78e2405013a6016d

_10

<nil> INF wrote file bootstrap/private-root-information/private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9/node-machine-account-key.priv.json`

warning

Copy the machine account public key somewhere safe. You will need it in a later step.

## Step 2 - Stake Your Node[​](#step-2---stake-your-node "Direct link to Step 2 - Stake Your Node")

Stake your node via [Flow Port](https://port.onflow.org/)

The `node details` (`Node ID`, `Network Address`, `Networking Key` and `Staking Key`) that need to be submitted when staking the node on Flow Port, can be found in the file: `./bootstrap/public-root-information/node-info.pub.<node-id>.json`.

Example

`_10

$cat ./bootstrap/public-root-information/node-info.pub.39fa54984b8eaa463e129919464f61c8cec3a4389478df79c44eb9bfbf30799a.json

_10

{

_10

"Role": "consensus",

_10

"Address": "consensus-001.nodes.flow.com:3569",

_10

"NodeID": "39fa54984b8eaa463e129919464f61c8cec3a4389478df79c44eb9bfbf30799a",

_10

"Weight": 0,

_10

"NetworkPubKey": "d92e3d5880abe233cf9fe9104db34bbb31251468a541454722b3870c04156a1b0504aef443bcaad124b997384b8fe7052847ce1e6189af1392d865e6be69835b",

_10

"StakingPubKey": "917826e018f056a00b778a58ae83054906957ffd4b6f1b7da083551f7a9f35e02b76ace50424ed7d2c9fc69207a59f0f08a031048f5641db94e77d0648b24d150dedd54bab7cd44b4aa60cfd54be418647b0b3965f8ae54c0bcb48ae9d705162"

_10

}`

If you are running a collection or consensus node, you will need to provide an additional field `Machine Account Public Key`.
This value is found in the output of the `bootstrap key` command from Step 1.

Staking a collection or consensus node will also create a machine account for the node. The machine account will be mentioned in the output of the staking transaction displayed by Flow Port. Please save the machine account for the next step.

info

Please let us know your node id via discord or email.

### Finalize Machine Account Setup[​](#finalize-machine-account-setup "Direct link to Finalize Machine Account Setup")

warning

If you are not running a collection or consensus node, you can skip this step.

You will now need to use the `bootstrap` utility to run `machine-account` with the created address to finalize the set up of your Machine account.

`_10

$ ./boot-tools/bootstrap machine-account --address YOUR_MACHINE_ACCOUNT_ADDRESS_GOES_HERE -o ./bootstrap`

Example

`_18

$ ./boot-tools/bootstrap machine-account --address 0x1de23de44985c7e7 -o ./bootstrap

_18

<nil> INF read machine account private key json

_18

<nil> DBG encoded public machine account key machineAccountPubKey=2743786d1ff1bf7d7026d693a774210eaa54728343859baab62e2df7f71a370651f4c7fd239d07af170e484eedd4f3c2df47103f6c39baf2eb2a50f67bbcba6a

_18

<nil> INF wrote file bootstrap/private-root-information/private-node-info_6f6e98c983dbd9aa69320452949b81abeab2ac591a247f55f19f4dbf0b477d26/node-machine-account-info.priv.json

_18

_18

$tree ./bootstrap/

_18

./bootstrap

_18

├── private-root-information

_18

│ └── private-node-info_d60bd55ee616c5c297cae1d5cfb7f65e7e04014d9c4abe595af2fd83f3cfe160

_18

│ ├── node-info.priv.json

_18

│ ├── node-machine-account-info.priv.json

_18

│ ├── node-machine-account-key.priv.json

_18

│ └── secretsdb-key

_18

└── public-root-information

_18

├── node-id

_18

└── node-info.pub.d60bd55ee616c5c297cae1d5cfb7f65e7e04014d9c4abe595af2fd83f3cfe160.json

_18

_18

3 directories, 5 files`

After running this step, you should see the `node-machine-account-info.priv.json` file in your `bootstrap` directory as shown above.

### Verify Machine Account Setup[​](#verify-machine-account-setup "Direct link to Verify Machine Account Setup")

After finalizing your machine account setup, you should verify its correctness with the `check-machine-account` command:

CheckMachineAccount

`_10

$ ./boot-tools/bootstrap check-machine-account --access-address access.mainnet.nodes.onflow.org:9000 -o ./bootstrap

_10

<nil> DBG read machine account info from disk hash_algo=SHA3_256 key_index=0 machine_account_address=0x284463aa6e25877c machine_account_pub_key=f847b84051bad4512101640772bf5e05e8a49868d92eaf9ebed41030881d95485769afd28653c5c53216cdcda4554384bb3ff6396a2ac04842422d55f0562496ad8d952802038203e8 signing_algo=ECDSA_P256

_10

<nil> DBG checking machine account configuration... machine_account_address=0x284463aa6e25877c role=consensus

_10

<nil> DBG machine account balance: 0.10000000

_10

<nil> INF 🤖 machine account is configured correctly`

This command will detect and provide information about common misconfigurations, or confirm that the machine account is configured correctly.

### Push transit keys (consensus node only)[​](#push-transit-keys-consensus-node-only "Direct link to Push transit keys (consensus node only)")

If you are running a consensus node, run the following command to generate the transit keys.

transit

`_10

$ ./boot-tools/transit prepare -b ./bootstrap -r consensus

_10

<nil> INF running prepare

_10

<nil> INF generating key pair

_10

<nil> INF completed preparation role=consensus`

This will generate the public and private transit keys under the bootstrap folder.
The transit keys are used to transfer the DKG keys after a network upgrade.

Please share the **public** transit key with the Flow Foundation via [discord](https://discord.gg/flow) or [email](mailto::governance@flow.com).

## Step 3 - Start Your Flow Node[​](#step-3---start-your-flow-node "Direct link to Step 3 - Start Your Flow Node")

Ensure you have configured your node using the [Node Setup guide](/networks/node-ops/node-operation/node-setup).

### Confirming authorization[​](#confirming-authorization "Direct link to Confirming authorization")

You can confirm your node's successful registration and authorization by executing a Cadence script to query the [Staking Contract](/build/core-contracts/staking-contract-reference#contract).
At the end of the `Staking Auction Phase`, the members of the Proposed Identity Table are confirmed as authorized participants in the next epoch.
Therefore, if your node ID appears in the Proposed Identity Table during the `Staking Auction Phase`, your node will be a participant in the next epoch.

You can read the current Proposed Identity Table using the [getProposedTable script](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_proposed_table.cdc).

You can read the current epoch phase using the [getEpochPhase script](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_phase.cdc). (A return value of `0` indicates the `Staking Auction Phase`.)

### Trusted Root Snapshot[​](#trusted-root-snapshot "Direct link to Trusted Root Snapshot")

Once your node has been registered and authorized by the service account, it will be able to participate in the next epoch.

![Flow Epoch Schedule](https://storage.googleapis.com/flow-resources/documentation-assets/epoch-startup-order.png)

A new node must bootstrap with a trusted root snapshot of the protocol state, where the node is a confirmed participant.
Since new nodes are confirmed at the end of the `Staking Auction Phase`, this means that, if the node is registered to join at epoch `N+1`, it must use a root snapshot from within the `Epoch Setup Phase` of epoch `N`.

### Dynamic Startup[​](#dynamic-startup "Direct link to Dynamic Startup")

Flow provides a mechanism called Dynamic Startup to simplify the process of obtaining the root snapshot.
When using Dynamic Startup, the node can be started **at any time during the `Staking Auction Phase`**.
The node will wait for the `Epoch Setup Phase` to begin, retrieve a valid root snapshot from a trusted Access Node, then bootstrap its state and join the network.
This is the recommended way to start your node for the first time.

1. Remove any `root-protocol-state-snapshot.json` file from your `bootstrap` folder. (If this file is present the node will attempt to bootstrap with it rather than Dynamic Startup.)
2. Select a trusted Access Node to provide the root snapshot. You will need this node's **secure GRPC server address** and **Networking Public Key**.
3. Configure Dynamic Startup by adding flags:

ExampleDynamicStartupFlags

`_10

... \

_10

--dynamic-startup-access-address=secure.mainnet.nodes.onflow.org:9001 \

_10

--dynamic-startup-access-publickey=28a0d9edd0de3f15866dfe4aea1560c4504fe313fc6ca3f63a63e4f98d0e295144692a58ebe7f7894349198613f65b2d960abf99ec2625e247b1c78ba5bf2eae`

4. Start your node (see [guide](/networks/node-ops/node-operation/node-setup#start-the-node))

info

Once the node has bootstrapped, these flags will be ignored and may be removed.

### Manually Provisioned Root Snapshot[​](#manually-provisioned-root-snapshot "Direct link to Manually Provisioned Root Snapshot")

You can also provision the root snapshot file manually, then start the node without configuring Dynamic Startup.
See [here](/networks/node-ops/node-operation/protocol-state-bootstrap) for the available options to provision a Root Snapshot.

warning

The snapshot must be within the `Epoch Setup Phase`.

warning

Since Collection and Consensus Nodes must start up in the first ~30mins of the `Epoch Setup Phase` (see [Timing](/networks/node-ops/node-operation/node-bootstrap#timing)),
the snapshot must be provisioned within this time window.

Once a valid root snapshot file is downloaded to the node's bootstrap folder, it can be started (see [guide](/networks/node-ops/node-operation/node-setup#start-the-node))

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/node-bootstrap.md)

Last updated on **Feb 22, 2025** by **bz**

[Previous

Node Monitoring](/networks/node-ops/node-operation/monitoring-nodes)[Next

Node Economics](/networks/node-ops/node-operation/node-economics)

###### Rate this page

😞😐😊

* [Timing](#timing)
* [Step 1 - Run Genesis Bootstrap](#step-1---run-genesis-bootstrap)
  + [Download the Bootstrapping Kit](#download-the-bootstrapping-kit)
  + [Generate Your Node Keys](#generate-your-node-keys)
* [Step 2 - Stake Your Node](#step-2---stake-your-node)
  + [Finalize Machine Account Setup](#finalize-machine-account-setup)
  + [Verify Machine Account Setup](#verify-machine-account-setup)
  + [Push transit keys (consensus node only)](#push-transit-keys-consensus-node-only)
* [Step 3 - Start Your Flow Node](#step-3---start-your-flow-node)
  + [Confirming authorization](#confirming-authorization)
  + [Trusted Root Snapshot](#trusted-root-snapshot)
  + [Dynamic Startup](#dynamic-startup)
  + [Manually Provisioned Root Snapshot](#manually-provisioned-root-snapshot)

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