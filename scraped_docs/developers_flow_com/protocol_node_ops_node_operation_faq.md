# Source: https://developers.flow.com/protocol/node-ops/node-operation/faq

Operator FAQ | Flow Developer Portal



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
* Operator FAQ

On this page

# Operator FAQ

### Can anybody run a node? What is the approval process?[​](#can-anybody-run-a-node-what-is-the-approval-process "Direct link to Can anybody run a node? What is the approval process?")

Anyone can run an [observer node](/protocol/node-ops/light-nodes/observer-node).

Anyone can run an Access Node after registering and staking. See [Access Node Setup](/protocol/node-ops/access-nodes/access-node-setup) for detailed instructions.

For the other node roles, individuals can go through an application process that involves asking about their background and experience contributing to decentralized projects. To pursue an application, please visit [the Flow website here to apply](https://www.flow.com/node-validators).

Pending approval, new node operators will be onboarded and invited to join a webinar to meet the team and share more about how they’ll grow the community. Node Operators are invited to join and participate in Flow's Node Validator Discord channel for setup questions and network announcements.

In the long-term, anyone can run a node validator on Flow.

### How do I generate keys?[​](#how-do-i-generate-keys "Direct link to How do I generate keys?")

Please follow the instructions provided here: [Generate Your Node Keys](/protocol/node-ops/node-operation/node-bootstrap#generate-your-node-keys)

### How do I check on the status of my node?[​](#how-do-i-check-on-the-status-of-my-node "Direct link to How do I check on the status of my node?")

Please follow the instructions provided here: [Monitoring nodes](/protocol/node-ops/node-operation/monitoring-nodes)

### Can I bootstrap and run a node at any time?[​](#can-i-bootstrap-and-run-a-node-at-any-time "Direct link to Can I bootstrap and run a node at any time?")

Flow allows nodes to join/leave the network each time a new epoch begins (roughly once per week).
See [Staking & Epochs](/protocol/staking#epochs) for general information and [Node Setup](/protocol/node-ops/node-operation/node-bootstrap#timing) for a guide to running a new node.

### Would it hurt the network to have a node that constantly spins up and down?[​](#would-it-hurt-the-network-to-have-a-node-that-constantly-spins-up-and-down "Direct link to Would it hurt the network to have a node that constantly spins up and down?")

All staked nodes except access nodes, have to be online at all time. A staked node, other than an access node, which is not online can cause severe degradation of network performance and will be subjected to slashing of rewards.
A way to prevent this is to check your equipment meets Flow's [recommended requirements](/protocol/node-ops/node-operation/node-provisioning#hardware-requirements), periodically checking for updates and announcements in Discord but also using a node monitoring system for when your node does go offline.

### Does Flow has a regular schedule for Sporks?[​](#does-flow-has-a-regular-schedule-for-sporks "Direct link to Does Flow has a regular schedule for Sporks?")

Yes, see [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks) for the latest schedule. Currently, Flow has a Mainnet Spork and a Testnet Spork roughly every two months.

### How do I update the Node Software?[​](#how-do-i-update-the-node-software "Direct link to How do I update the Node Software?")

One of the reasons for a [spork](/protocol/node-ops/node-operation/spork) is to make sure all nodes update to the latest software version. Hence, you should have the latest software update as long as you are participating in each spork.
However, if we do release any software update in between a Spork (e.g. an emergency patch) we will announce it on Discord.

### Is there any way to know if a node is currently online?[​](#is-there-any-way-to-know-if-a-node-is-currently-online "Direct link to Is there any way to know if a node is currently online?")

To verify if a node is online, please [setup metrics](/protocol/node-ops/node-operation/faq#how-do-i-check-on-the-status-of-my-node) for the node.

### Can I migrate a node to a new machine?[​](#can-i-migrate-a-node-to-a-new-machine "Direct link to Can I migrate a node to a new machine?")

Yes, as long as you retain the `boostrap` information which includes the node staking key, networking key, IP address and port from the old node to the new.
More on this [here](/protocol/node-ops/node-operation/node-migration)

### Where can I find how many nodes are currently running Flow?[​](#where-can-i-find-how-many-nodes-are-currently-running-flow "Direct link to Where can I find how many nodes are currently running Flow?")

If you are running a node, then you most definitely have this information on your node in the file `<your bootstrap dir>/public-root-information/node-infos.pub.json`. If you are not running a node, you can find this information by using a Cadence script to query the [Staking Smart Contract](/build/cadence/core-contracts/staking-contract-reference) (or check [Flowdiver](https://flowdiver.io/staking/overview))

### Why do I need to update my node's ulimit?[​](#why-do-i-need-to-update-my-nodes-ulimit "Direct link to Why do I need to update my node's ulimit?")

Flow nodes create network connections to other nodes on the network to participate in the protocol. The node's operating system represents
these connections as file descriptors, and uses soft and hard limits to control the number of open files. The node software uses these limits
to manage how many connections it will open and accept from other nodes. If the limit is too low, the node will not be able to communicate
with its peers, preventing it from functioning properly.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/faq.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Light Node Setup](/protocol/node-ops/light-nodes/observer-node)[Next

Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)

###### Rate this page

😞😐😊

Copy as Markdown

* [Can anybody run a node? What is the approval process?](#can-anybody-run-a-node-what-is-the-approval-process)
* [How do I generate keys?](#how-do-i-generate-keys)
* [How do I check on the status of my node?](#how-do-i-check-on-the-status-of-my-node)
* [Can I bootstrap and run a node at any time?](#can-i-bootstrap-and-run-a-node-at-any-time)
* [Would it hurt the network to have a node that constantly spins up and down?](#would-it-hurt-the-network-to-have-a-node-that-constantly-spins-up-and-down)
* [Does Flow has a regular schedule for Sporks?](#does-flow-has-a-regular-schedule-for-sporks)
* [How do I update the Node Software?](#how-do-i-update-the-node-software)
* [Is there any way to know if a node is currently online?](#is-there-any-way-to-know-if-a-node-is-currently-online)
* [Can I migrate a node to a new machine?](#can-i-migrate-a-node-to-a-new-machine)
* [Where can I find how many nodes are currently running Flow?](#where-can-i-find-how-many-nodes-are-currently-running-flow)
* [Why do I need to update my node's ulimit?](#why-do-i-need-to-update-my-nodes-ulimit)

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