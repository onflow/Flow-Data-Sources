# Source: https://developers.flow.com/protocol/staking/machine-account

Machine Account | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)
* [Networks](/protocol)
* [Flow Network Architecture](/protocol/network-architecture)
* [Staking and Epochs](/protocol/staking)

  + [Epoch and Staking Terminology](/protocol/staking/epoch-terminology)
  + [Epoch and Reward Schedule](/protocol/staking/schedule)
  + [Epoch Preparation Protocol](/protocol/staking/epoch-preparation)
  + [Stake Slashing](/protocol/staking/stake-slashing)
  + [Epoch Scripts and Events](/protocol/staking/epoch-scripts-events)
  + [Staking Technical Overview](/protocol/staking/technical-overview)
  + [Staking Scripts and Events](/protocol/staking/staking-scripts-events)
  + [How to Query Staking rewards](/protocol/staking/staking-rewards)
  + [QC and DKG](/protocol/staking/qc-dkg)
  + [QC/DKG Scripts and Events](/protocol/staking/qc-dkg-scripts-events)
  + [Machine Account](/protocol/staking/machine-account)
  + [FAQs](/protocol/staking/faq)
  + [Technical Staking Options](/protocol/staking/staking-options)
  + [Staking Collection Guide](/protocol/staking/staking-collection)
  + [Basic Staking Guide (Deprecated)](/protocol/staking/staking-guide)
* [Node Ops](/protocol/node-ops)
* [Accessing Data](/protocol/access-onchain-data)
* [Governance](/protocol/governance)
* [Flow Port](/protocol/flow-port)

* [Staking and Epochs](/protocol/staking)
* Machine Account

On this page

# Machine Account

### What is a Machine Account?[​](#what-is-a-machine-account "Direct link to What is a Machine Account?")

A Machine Account is a Flow account which is used autonomously by a node to interact with
system smart contracts. Machine Accounts contain Cadence resources granted to network
participants which are used to participate in smart-contract-mediated protocols. Currently,
Machine Accounts are used in the [Epoch Preparation Protocol](/protocol/staking/epoch-preparation),
which prepares the network for the next epoch.

Your Machine Account is distinct from the account you use for staking your node (your Staking Account).
The Machine Account is intended for use by node software and does not have access to your staked tokens or staking rewards.

info

Currently Machine Accounts are required only for `collection` and `consensus` nodes.

#### Creation[​](#creation "Direct link to Creation")

Machine Accounts are created during the [staking process](/protocol/flow-port/staking-guide) in Flow Port.

#### Funding[​](#funding "Direct link to Funding")

Machine Accounts must maintain a balance of liquid FLOW tokens to pay fees on transactions they
submit to system smart contracts. Typically very few transactions will be sent (about 1-5 per week)
however more may be required under certain circumstances and network conditions.

info

Because some transactions sent by the Machine Account are system critical, we recommend maintaining
a balance sufficient to accommodate worst-case transaction submission numbers at all times. **See [here](/protocol/node-ops/node-operation/monitoring-nodes#machine-account) for how to monitor.**

When creating a new machine account, we recommend initially funding with 0.005 FLOW for collection nodes and
0.25 FLOW for consensus nodes.

Machine account balances should be monitored and periodically refilled to ensure they have sufficient funds.
We recommend a minimum balance at all times of 0.002 FLOW for collection nodes and 0.1 FLOW for consensus nodes.

A node operator can easily withdraw their FLOW from their machine account if they decide they don't need them there any more.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/11-machine-account.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

QC/DKG Scripts and Events](/protocol/staking/qc-dkg-scripts-events)[Next

FAQs](/protocol/staking/faq)

###### Rate this page

😞😐😊

Copy as Markdown

* [What is a Machine Account?](#what-is-a-machine-account)

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