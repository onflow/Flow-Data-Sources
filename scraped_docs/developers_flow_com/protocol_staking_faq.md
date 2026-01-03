# Source: https://developers.flow.com/protocol/staking/faq

Staking FAQ | Flow Developer Portal



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

* * [Staking and Epochs](/protocol/staking)* FAQs

On this page

# Staking FAQ

### Where will users receive their staking reward for each staking option?[​](#where-will-users-receive-their-staking-reward-for-each-staking-option "Direct link to Where will users receive their staking reward for each staking option?")

Staking rewards are not deposited directly into a user's account.
They are deposited to the user's rewards pool in their connected staking object and can be withdrawn or restaked at any time.

If you staked using [Flow Port](https://port.flow.com), then you can see your staking rewards there. You can also withdraw the rewards or manually re-stake them through Flow Port.

If you staked using a staking provider such as Kraken, Blocto or Finoa,
please ask them how they manage staking rewards.

### Will staking rewards be automatically re-staked?[​](#will-staking-rewards-be-automatically-re-staked "Direct link to Will staking rewards be automatically re-staked?")

There will be *no* automatic re-staking of staking rewards with Flow Port (i.e. using Ledger or Blocto). If you want to re-stake your rewards, you must manually do so yourself.

If you staked using a staking provider such as Kraken, Blocto or Finoa,
please ask them what their policies are.

DeFi liquid staking strategies such as offered by [incrementFi](https://app.increment.fi/staking) are not managed by the protocol or nodes, but are more sophisticated ways to manage your staking.

### Does it make a difference as to what TYPE of node we delegate to in terms of rewards?[​](#does-it-make-a-difference-as-to-what-type-of-node-we-delegate-to-in-terms-of-rewards "Direct link to Does it make a difference as to what TYPE of node we delegate to in terms of rewards?")

No, rewards are calculated the same for every node type.

### Can a validator change its fees?[​](#can-a-validator-change-its-fees "Direct link to Can a validator change its fees?")

The network enforces a delegation fee of 8% which cannot be directly changed. Any different fees that nodes claim they have are rebates that they
offer using their own methods and are not enforced by the protocol.

### Can a token holder stake to multiple nodes? If yes, how is the stake split between them?[​](#can-a-token-holder-stake-to-multiple-nodes-if-yes-how-is-the-stake-split-between-them "Direct link to Can a token holder stake to multiple nodes? If yes, how is the stake split between them?")

A token holder can delegate to multiple nodes from a single account if they use the [Staking Collection](/protocol/staking/staking-collection).

The staking collection is enabled by default on Flow port, and many custody providers also support it.

### Is the wallet key transferred to the staked node?[​](#is-the-wallet-key-transferred-to-the-staked-node "Direct link to Is the wallet key transferred to the staked node?")

No - The keys on the node are different from the wallet keys. The wallet keys always stay in the wallet. A node operator generates the staking and networking keys separately which will be used on the node.

### Can I stake through multiple accounts to meet the minimum FLOW required for staking a node?[​](#can-i-stake-through-multiple-accounts-to-meet-the-minimum-flow-required-for-staking-a-node "Direct link to Can I stake through multiple accounts to meet the minimum FLOW required for staking a node?")

No, the minimum stake must come from a single account for all node types.

### Is rewards payout another spork?[​](#is-rewards-payout-another-spork "Direct link to Is rewards payout another spork?")

No, rewards payout is not a spork but is an automatic transaction that happens at the beginning of every new epoch.

### Can I query an account address of a node ID or delegator ID?[​](#can-i-query-an-account-address-of-a-node-id-or-delegator-id "Direct link to Can I query an account address of a node ID or delegator ID?")

The staking smart contract does not directly associate a node or delegator with an account address. It associates it with the assigned resource object that corresponds to that entry in the contract. There can be any number of these objects stored in the same account, and they can be moved to different accounts if the owner chooses.

It is possible to query the information about a node that an address runs though, by using the `get_node_info_from_address.cdc` script.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/12-faq.md)

Last updated on **Oct 7, 2025** by **Brian Doyle**

[Previous

Machine Account](/protocol/staking/machine-account)[Next

Technical Staking Options](/protocol/staking/staking-options)

###### Rate this page

😞😐😊

Copy as Markdown

* [Where will users receive their staking reward for each staking option?](#where-will-users-receive-their-staking-reward-for-each-staking-option)* [Will staking rewards be automatically re-staked?](#will-staking-rewards-be-automatically-re-staked)* [Does it make a difference as to what TYPE of node we delegate to in terms of rewards?](#does-it-make-a-difference-as-to-what-type-of-node-we-delegate-to-in-terms-of-rewards)* [Can a validator change its fees?](#can-a-validator-change-its-fees)* [Can a token holder stake to multiple nodes? If yes, how is the stake split between them?](#can-a-token-holder-stake-to-multiple-nodes-if-yes-how-is-the-stake-split-between-them)* [Is the wallet key transferred to the staked node?](#is-the-wallet-key-transferred-to-the-staked-node)* [Can I stake through multiple accounts to meet the minimum FLOW required for staking a node?](#can-i-stake-through-multiple-accounts-to-meet-the-minimum-flow-required-for-staking-a-node)* [Is rewards payout another spork?](#is-rewards-payout-another-spork)* [Can I query an account address of a node ID or delegator ID?](#can-i-query-an-account-address-of-a-node-id-or-delegator-id)

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