# Source: https://developers.flow.com/protocol/node-ops/node-operation/db-encryption-existing-operator

Database Encryption for Existing Node Operators | Flow Developer Portal



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
* Database Encryption for Existing Node Operators

On this page

# Database Encryption for Existing Node Operators

In Mainnet14, the DKG (distributed key generation) is turned on, requiring storage of
dynamically generated confidential data (random beacon keys). These are stored in a
separate database which is new with the Mainnet14 release.

All node operators joining after Mainnet14 will generate encryption keys for this database
through the node bootstrapping and staking process. We strongly recommend all node operators
(especially consensus node operators) generate an encryption key for this database. This
guide demonstrates how to enable encryption for this database for existing operators.

## Downloading Bootstrap Utility[​](#downloading-bootstrap-utility "Direct link to Downloading Bootstrap Utility")

warning

If you have downloaded the bootstrapping kit previously, ensure that you do
this step again to get the latest copy of the bootstrapping kit since there
have been significant changes to it.

Follow the instructions [here](/protocol/node-ops/node-operation/node-bootstrap#download-the-bootstrapping-kit)
to download the latest version of the bootstrapping kit, then return to this page.

## Generate Database Encryption Key[​](#generate-database-encryption-key "Direct link to Generate Database Encryption Key")

You will need to generate an encryption key for the database using the `bootstrap` utility.

warning

Ensure you run the following commands on the machine you use to run your node software.
The bootstrap directory passed to the `-o` flag must be the same bootstrap directory used by your node.
The default location is `/var/flow/bootstrap`, but double-check your setup before continuing.

GenerateEncryptionKey

`_15

$./boot-tools/bootstrap db-encryption-key -o ./bootstrap

_15

<nil> INF generated db encryption key

_15

<nil> INF wrote file bootstrap/private-root-information/private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9secretsdb-key

_15

_15

$tree ./bootstrap/

_15

./bootstrap

_15

├── private-root-information

_15

│ └── private-node-info_ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9

_15

│ ├── node-info.priv.json

_15

│ └── secretsdb-key

_15

└── public-root-information

_15

├── node-id

_15

└── node-info.pub.ab6e0b15837de7e5261777cb65665b318cf3f94492dde27c1ea13830e989bbf9.json

_15

_15

3 directories, 4 files`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/db-encryption-existing-operator.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)[Next

Genesis Bootstrapping](/protocol/node-ops/node-operation/guides/genesis-bootstrap)

###### Rate this page

😞😐😊

Copy as Markdown

* [Downloading Bootstrap Utility](#downloading-bootstrap-utility)
* [Generate Database Encryption Key](#generate-database-encryption-key)

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
* [EVM](/build/evm/quickstart)

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