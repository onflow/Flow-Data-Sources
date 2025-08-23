# Source: https://developers.flow.com/protocol/node-ops/node-operation/machine-existing-operator

Machine Accounts for Existing Node Operators | Flow Developer Portal



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
* Machine Accounts for Existing Node Operators

On this page

# Machine Accounts for Existing Node Operators

The [Flow Epoch Preparation Protocol](/protocol/staking/epoch-preparation) requires that
`collection` and `consensus` nodes use an automated [machine account](/protocol/staking/qc-dkg#machine-accounts)
to participate in important processes required to start the next epoch. (QC and DKG, respectively)

Starting on Thursday, August 26th 2021, all collector and consensus nodes who register with Flow Port will
automatically create and initialize this machine account as part of their node registration.

If you have an existing `consensus` or `collection` node that you registered with Flow Port before Thursday August 26th,
you will need to create this Machine Account manually in order to participate in epochs.
You will need to create one Machine Account for each `consensus` or `collection` node that you operate.

This guide will walk you through creating a Machine Account and getting it set up.

warning

During this process you will generate a new private key which will have sole control over your machine account.
This private key will be stored on the machine you use to run your node, alongside your staking and networking keys.
Loss of any of these keys (staking, networking, or machine account) will require you to un-stake your tokens, start a completely new node, and register the new node to continue participating in the Flow network, which takes multiple weeks.

## Downloading Bootstrap Utility[​](#downloading-bootstrap-utility "Direct link to Downloading Bootstrap Utility")

warning

If you have downloaded the bootstrapping kit previously, ensure that you do
this step again to get the latest copy of the bootstrapping kit since there
have been significant changes to it.

Follow the instructions [here](/protocol/node-ops/node-operation/node-bootstrap#download-the-bootstrapping-kit)
to download the latest version of the bootstrapping kit, then return to this page.

## Generate Machine Account key[​](#generate-machine-account-key "Direct link to Generate Machine Account key")

You will need to generate a Machine account private key using the `bootstrap` utility.

warning

Ensure you run the following commands on the machine you use to run your node software.
The bootstrap directory passed to the `-o` flag must be the same bootstrap directory used by your node.
The default location is `/var/flow/bootstrap`, but double-check your setup before continuing.

GenerateMachineAccountKey

`_17

$./boot-tools/bootstrap machine-account-key -o ./bootstrap

_17

<nil> INF generated machine account private key

_17

<nil> INF encoded machine account public key for entry to Flow Port machineAccountPubKey=f847b84031d9f47b88435e4ea828310529d2c60e806395da50d3dd0dd2f32e2de336fb44eb06488645673850897d7cc017701d7e6272a1ab7f2f125aede46363e973444a02038203e8

_17

<nil> INF wrote file bootstrap/private-root-information/private-node-info_6f6e98c983dbd9aa69320452949b81abeab2ac591a247f55f19f4dbf0b477d26/node-machine-account-key.priv.json

_17

_17

$tree ./bootstrap/

_17

./bootstrap

_17

├── private-root-information

_17

│ └── private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9

_17

│ ├── node-info.priv.json

_17

│ └── node-machine-account-key.priv.json

_17

│ └── secretsdb-key

_17

└── public-root-information

_17

├── node-id

_17

└── node-info.pub.ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9.json

_17

_17

3 directories, 4 files`

## Create Machine Account[​](#create-machine-account "Direct link to Create Machine Account")

You will now need to copy the Machine account public key displayed in the terminal output and
head over to [Flow Port](/protocol/flow-port/staking-guide#stake-a-node) to submit a transaction to create a Machine Account.
For example, from the example above, we would copy `f847...` from this line:

Example

`_10

<nil> INF encoded machine account public key for entry to Flow Port machineAccountPubKey=f847b84031d9f47b88435e4ea828310529d2c60e806395da50d3dd0dd2f32e2de336fb44eb06488645673850897d7cc017701d7e6272a1ab7f2f125aede46363e973444a02038203e8`

This process will create your machine account for you and show you your machine account's address, which you will need to save for the next step.

## Finalize Machine Account setup[​](#finalize-machine-account-setup "Direct link to Finalize Machine Account setup")

You will now need to use the `bootstrap` utility to run `machine-account` with the created address to finalize the set up of your Machine account.

`_10

$ ./boot-tools/bootstrap machine-account --address ${YOUR_MACHINE_ACCOUNT_ADDRESS} -o ./bootstrap`

Example

`_18

$./boot-tools/bootstrap machine-account --address 0x1de23de44985c7e7 -o ./bootstrap

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

│ └── node-machine-account-key.priv.json

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/machine-existing-operator.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Starting Your Nodes](/protocol/node-ops/node-operation/guides/starting-nodes)[Next

Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)

###### Rate this page

😞😐😊

Copy as Markdown

* [Downloading Bootstrap Utility](#downloading-bootstrap-utility)
* [Generate Machine Account key](#generate-machine-account-key)
* [Create Machine Account](#create-machine-account)
* [Finalize Machine Account setup](#finalize-machine-account-setup)
  + [Verify Machine Account Setup](#verify-machine-account-setup)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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