# Source: https://developers.flow.com/networks/node-ops/node-operation/machine-existing-operator




Machine Accounts for Existing Node Operators | Flow Developer Portal





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
* Machine Accounts for Existing Node Operators
On this page
# Machine Accounts for Existing Node Operators

The [Flow Epoch Preparation Protocol](/networks/staking/epoch-preparation) requires that
`collection` and `consensus` nodes use an automated [machine account](/networks/staking/qc-dkg#machine-accounts)
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

Follow the instructions [here](/networks/node-ops/node-operation/node-bootstrap#download-the-bootstrapping-kit)
to download the latest version of the bootstrapping kit, then return to this page.

## Generate Machine Account key[​](#generate-machine-account-key "Direct link to Generate Machine Account key")

You will need to generate a Machine account private key using the `bootstrap` utility.

warning

Ensure you run the following commands on the machine you use to run your node software.
The bootstrap directory passed to the `-o` flag must be the same bootstrap directory used by your node.
The default location is `/var/flow/bootstrap`, but double-check your setup before continuing.


GenerateMachineAccountKey `_17$./boot-tools/bootstrap machine-account-key -o ./bootstrap_17<nil> INF generated machine account private key_17<nil> INF encoded machine account public key for entry to Flow Port machineAccountPubKey=f847b84031d9f47b88435e4ea828310529d2c60e806395da50d3dd0dd2f32e2de336fb44eb06488645673850897d7cc017701d7e6272a1ab7f2f125aede46363e973444a02038203e8_17<nil> INF wrote file bootstrap/private-root-information/private-node-info_6f6e98c983dbd9aa69320452949b81abeab2ac591a247f55f19f4dbf0b477d26/node-machine-account-key.priv.json_17_17$tree ./bootstrap/_17./bootstrap_17├── private-root-information_17│ └── private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9_17│ ├── node-info.priv.json_17│ └── node-machine-account-key.priv.json_17│ └── secretsdb-key_17└── public-root-information_17 ├── node-id_17 └── node-info.pub.ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9.json_17_173 directories, 4 files`
## Create Machine Account[​](#create-machine-account "Direct link to Create Machine Account")

You will now need to copy the Machine account public key displayed in the terminal output and
head over to [Flow Port](/networks/flow-port/staking-guide#stake-a-node) to submit a transaction to create a Machine Account.
For example, from the example above, we would copy `f847...` from this line:

Example `_10<nil> INF encoded machine account public key for entry to Flow Port machineAccountPubKey=f847b84031d9f47b88435e4ea828310529d2c60e806395da50d3dd0dd2f32e2de336fb44eb06488645673850897d7cc017701d7e6272a1ab7f2f125aede46363e973444a02038203e8`

This process will create your machine account for you and show you your machine account's address, which you will need to save for the next step.

## Finalize Machine Account setup[​](#finalize-machine-account-setup "Direct link to Finalize Machine Account setup")

You will now need to use the `bootstrap` utility to run `machine-account` with the created address to finalize the set up of your Machine account.

 `_10$ ./boot-tools/bootstrap machine-account --address ${YOUR_MACHINE_ACCOUNT_ADDRESS} -o ./bootstrap`
Example `_18$./boot-tools/bootstrap machine-account --address 0x1de23de44985c7e7 -o ./bootstrap_18<nil> INF read machine account private key json_18<nil> DBG encoded public machine account key machineAccountPubKey=2743786d1ff1bf7d7026d693a774210eaa54728343859baab62e2df7f71a370651f4c7fd239d07af170e484eedd4f3c2df47103f6c39baf2eb2a50f67bbcba6a_18<nil> INF wrote file bootstrap/private-root-information/private-node-info_6f6e98c983dbd9aa69320452949b81abeab2ac591a247f55f19f4dbf0b477d26/node-machine-account-info.priv.json_18_18$tree ./bootstrap/_18./bootstrap_18├── private-root-information_18│ └── private-node-info_d60bd55ee616c5c297cae1d5cfb7f65e7e04014d9c4abe595af2fd83f3cfe160_18│ ├── node-info.priv.json_18│ ├── node-machine-account-info.priv.json_18│ └── node-machine-account-key.priv.json_18│ └── secretsdb-key_18└── public-root-information_18 ├── node-id_18 └── node-info.pub.d60bd55ee616c5c297cae1d5cfb7f65e7e04014d9c4abe595af2fd83f3cfe160.json_18_183 directories, 5 files`

After running this step, you should see the `node-machine-account-info.priv.json` file in your `bootstrap` directory as shown above.

### Verify Machine Account Setup[​](#verify-machine-account-setup "Direct link to Verify Machine Account Setup")

After finalizing your machine account setup, you should verify its correctness with the `check-machine-account` command:

CheckMachineAccount `_10$ ./boot-tools/bootstrap check-machine-account --access-address access.mainnet.nodes.onflow.org:9000 -o ./bootstrap_10<nil> DBG read machine account info from disk hash_algo=SHA3_256 key_index=0 machine_account_address=0x284463aa6e25877c machine_account_pub_key=f847b84051bad4512101640772bf5e05e8a49868d92eaf9ebed41030881d95485769afd28653c5c53216cdcda4554384bb3ff6396a2ac04842422d55f0562496ad8d952802038203e8 signing_algo=ECDSA_P256_10<nil> DBG checking machine account configuration... machine_account_address=0x284463aa6e25877c role=consensus_10<nil> DBG machine account balance: 0.10000000_10<nil> INF 🤖 machine account is configured correctly`

This command will detect and provide information about common misconfigurations, or confirm that the machine account is configured correctly.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/machine-existing-operator.md)Last updated on **Jan 10, 2025** by **Brian Doyle**[PreviousStarting Your Nodes](/networks/node-ops/node-operation/guides/starting-nodes)[NextNode Monitoring](/networks/node-ops/node-operation/monitoring-nodes)
###### Rate this page

😞😐😊

* [Downloading Bootstrap Utility](#downloading-bootstrap-utility)
* [Generate Machine Account key](#generate-machine-account-key)
* [Create Machine Account](#create-machine-account)
* [Finalize Machine Account setup](#finalize-machine-account-setup)
  + [Verify Machine Account Setup](#verify-machine-account-setup)
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

