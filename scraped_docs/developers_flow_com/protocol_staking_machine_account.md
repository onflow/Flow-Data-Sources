# Source: https://developers.flow.com/protocol/staking/machine-account

Machine Account | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        + [Epoch and Staking Terminology](/protocol/staking/epoch-terminology)+ [Epoch and Reward Schedule](/protocol/staking/schedule)+ [Epoch Preparation Protocol](/protocol/staking/epoch-preparation)+ [Stake Slashing](/protocol/staking/stake-slashing)+ [Epoch Scripts and Events](/protocol/staking/epoch-scripts-events)+ [Staking Technical Overview](/protocol/staking/technical-overview)+ [Staking Scripts and Events](/protocol/staking/staking-scripts-events)+ [How to Query Staking rewards](/protocol/staking/staking-rewards)+ [QC and DKG](/protocol/staking/qc-dkg)+ [QC/DKG Scripts and Events](/protocol/staking/qc-dkg-scripts-events)+ [Machine Account](/protocol/staking/machine-account)+ [FAQs](/protocol/staking/faq)+ [Technical Staking Options](/protocol/staking/staking-options)+ [Staking Collection Guide](/protocol/staking/staking-collection)* [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Staking and Epochs](/protocol/staking)* Machine Account

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

When creating a new machine account, we recommend initially funding with **0.75 FLOW for collection nodes** and
**6 FLOW for consensus nodes**.

Machine account balances must be [monitored](/protocol/node-ops/node-operation/monitoring-nodes#machine-account) and periodically refilled to ensure they have sufficient funds.
We recommend a minimum balance at all times of 0.25 FLOW for collection nodes and 2 FLOW for consensus nodes.

FLOW deposited to a machine account can be withdrawn at any time by the node operator.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/11-machine-account.md)

Last updated on **Dec 8, 2025** by **Jordan Schalm**

[Previous

QC/DKG Scripts and Events](/protocol/staking/qc-dkg-scripts-events)[Next

FAQs](/protocol/staking/faq)

###### Rate this page

😞😐😊

Copy as Markdown

* [What is a Machine Account?](#what-is-a-machine-account)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.