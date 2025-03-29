# Source: https://developers.flow.com/networks/node-ops/node-operation/faq

Operator FAQ | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* Operator FAQ

On this page

# Operator FAQ

### Can anybody run a node? What is the approval process?[​](#can-anybody-run-a-node-what-is-the-approval-process "Direct link to Can anybody run a node? What is the approval process?")

Anyone can run an [observer node](/networks/node-ops/light-nodes/observer-node).

Anyone can run an Access Node after registering and staking. See [Access Node Setup](/networks/node-ops/access-nodes/access-node-setup) for detailed instructions.

For the other node roles, individuals can go through an application process that involves asking about their background and experience contributing to decentralized projects. To pursue an application, please visit [the Flow website here to apply](https://www.onflow.org/node-validators).

Pending approval, new node operators will be onboarded and invited to join a webinar to meet the team and share more about how they’ll grow the community. Node Operators are invited to join and participate in Flow's Node Validator Discord channel for setup questions and network announcements.

In the long-term, anyone can run a node validator on Flow.

### How do I generate keys?[​](#how-do-i-generate-keys "Direct link to How do I generate keys?")

Please follow the instructions provided here: [Generate Your Node Keys](/networks/node-ops/node-operation/node-bootstrap#generate-your-node-keys)

### How do I check on the status of my node?[​](#how-do-i-check-on-the-status-of-my-node "Direct link to How do I check on the status of my node?")

Please follow the instructions provided here: [Monitoring nodes](/networks/node-ops/node-operation/monitoring-nodes)

### Can I bootstrap and run a node at any time?[​](#can-i-bootstrap-and-run-a-node-at-any-time "Direct link to Can I bootstrap and run a node at any time?")

Flow allows nodes to join/leave the network each time a new epoch begins (roughly once per week).
See [Staking & Epochs](/networks/staking#epochs) for general information and [Node Setup](/networks/node-ops/node-operation/node-bootstrap#timing) for a guide to running a new node.

### Would it hurt the network to have a node that constantly spins up and down?[​](#would-it-hurt-the-network-to-have-a-node-that-constantly-spins-up-and-down "Direct link to Would it hurt the network to have a node that constantly spins up and down?")

All staked nodes except access nodes, have to be online at all time. A staked node, other than an access node, which is not online can cause severe degradation of network performance and will be subjected to slashing of rewards.
A way to prevent this is to check your equipment meets Flow's [recommended requirements](/networks/node-ops/node-operation/node-provisioning#hardware-requirements), periodically checking for updates and announcements in Discord but also using a node monitoring system for when your node does go offline.

### Does Flow has a regular schedule for Sporks?[​](#does-flow-has-a-regular-schedule-for-sporks "Direct link to Does Flow has a regular schedule for Sporks?")

Yes, see [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks) for the latest schedule. Currently, Flow has a Mainnet Spork and a Testnet Spork roughly every two months.

### How do I update the Node Software?[​](#how-do-i-update-the-node-software "Direct link to How do I update the Node Software?")

One of the reasons for a [spork](/networks/node-ops/node-operation/spork) is to make sure all nodes update to the latest software version. Hence, you should have the latest software update as long as you are participating in each spork.
However, if we do release any software update in between a Spork (e.g. an emergency patch) we will announce it on Discord.

### Is there any way to know if a node is currently online?[​](#is-there-any-way-to-know-if-a-node-is-currently-online "Direct link to Is there any way to know if a node is currently online?")

To verify if a node is online, please [setup metrics](/networks/node-ops/node-operation/faq#how-do-i-check-on-the-status-of-my-node) for the node.

### Can I migrate a node to a new machine?[​](#can-i-migrate-a-node-to-a-new-machine "Direct link to Can I migrate a node to a new machine?")

Yes, as long as you retain the `boostrap` information which includes the node staking key, networking key, IP address and port from the old node to the new.
More on this [here](/networks/node-ops/node-operation/node-migration)

### Where can I find how many nodes are currently running Flow?[​](#where-can-i-find-how-many-nodes-are-currently-running-flow "Direct link to Where can I find how many nodes are currently running Flow?")

If you are running a node, then you most definitely have this information on your node in the file `<your bootstrap dir>/public-root-information/node-infos.pub.json`. If you are not running a node, you can find this information by using a Cadence script to query the [Staking Smart Contract](/build/core-contracts/staking-contract-reference) (or check [Flowdiver](https://flowdiver.io/staking/overview))

### Why do I need to update my node's ulimit?[​](#why-do-i-need-to-update-my-nodes-ulimit "Direct link to Why do I need to update my node's ulimit?")

Flow nodes create network connections to other nodes on the network to participate in the protocol. The node's operating system represents
these connections as file descriptors, and uses soft and hard limits to control the number of open files. The node software uses these limits
to manage how many connections it will open and accept from other nodes. If the limit is too low, the node will not be able to communicate
with its peers, preventing it from functioning properly.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/faq.md)

Last updated on **Mar 14, 2025** by **j pimmel**

[Previous

Light Node Setup](/networks/node-ops/light-nodes/observer-node)[Next

Byzantine Attack Response](/networks/node-ops/node-operation/byzantine-node-attack-response)

###### Rate this page

😞😐😊

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