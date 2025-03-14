# Source: https://developers.flow.com/networks/staking/machine-account

Machine Account | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)

  + [Epoch and Staking Terminology](/networks/staking/epoch-terminology)
  + [Epoch and Reward Schedule](/networks/staking/schedule)
  + [Epoch Preparation Protocol](/networks/staking/epoch-preparation)
  + [Stake Slashing](/networks/staking/stake-slashing)
  + [Epoch Scripts and Events](/networks/staking/epoch-scripts-events)
  + [Staking Technical Overview](/networks/staking/technical-overview)
  + [Staking Scripts and Events](/networks/staking/staking-scripts-events)
  + [How to Query Staking rewards](/networks/staking/staking-rewards)
  + [QC and DKG](/networks/staking/qc-dkg)
  + [QC/DKG Scripts and Events](/networks/staking/qc-dkg-scripts-events)
  + [Machine Account](/networks/staking/machine-account)
  + [FAQs](/networks/staking/faq)
  + [Technical Staking Options](/networks/staking/staking-options)
  + [Staking Collection Guide](/networks/staking/staking-collection)
  + [Basic Staking Guide (Deprecated)](/networks/staking/staking-guide)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Staking and Epochs](/networks/staking)
* Machine Account

On this page

# Machine Account

### What is a Machine Account?[​](#what-is-a-machine-account "Direct link to What is a Machine Account?")

A Machine Account is a Flow account which is used autonomously by a node to interact with
system smart contracts. Machine Accounts contain Cadence resources granted to network
participants which are used to participate in smart-contract-mediated protocols. Currently,
Machine Accounts are used in the [Epoch Preparation Protocol](/networks/staking/epoch-preparation),
which prepares the network for the next epoch.

Your Machine Account is distinct from the account you use for staking your node (your Staking Account).
The Machine Account is intended for use by node software and does not have access to your staked tokens or staking rewards.

info

Currently Machine Accounts are required only for `collection` and `consensus` nodes.

#### Creation[​](#creation "Direct link to Creation")

Machine Accounts are created during the [staking process](/networks/flow-port/staking-guide) in Flow Port.

#### Funding[​](#funding "Direct link to Funding")

Machine Accounts must maintain a balance of liquid FLOW tokens to pay fees on transactions they
submit to system smart contracts. Typically very few transactions will be sent (about 1-5 per week)
however more may be required under certain circumstances and network conditions.

info

Because some transactions sent by the Machine Account are system critical, we recommend maintaining
a balance sufficient to accommodate worst-case transaction submission numbers at all times. **See [here](/networks/node-ops/node-operation/monitoring-nodes#machine-account) for how to monitor.**

When creating a new machine account, we recommend initially funding with 0.005 FLOW for collection nodes and
0.25 FLOW for consensus nodes.

Machine account balances should be monitored and periodically refilled to ensure they have sufficient funds.
We recommend a minimum balance at all times of 0.002 FLOW for collection nodes and 0.1 FLOW for consensus nodes.

A node operator can easily withdraw their FLOW from their machine account if they decide they don't need them there any more.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/11-machine-account.md)

Last updated on **Feb 27, 2025** by **Vishal**

[Previous

QC/DKG Scripts and Events](/networks/staking/qc-dkg-scripts-events)[Next

FAQs](/networks/staking/faq)

###### Rate this page

😞😐😊

* [What is a Machine Account?](#what-is-a-machine-account)

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