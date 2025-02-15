# Source: https://developers.flow.com/networks/staking/faq




Staking FAQ | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* FAQs
On this page
# Staking FAQ

### Where will users receive their staking reward for each staking option?[​](#where-will-users-receive-their-staking-reward-for-each-staking-option "Direct link to Where will users receive their staking reward for each staking option?")

Staking rewards are not deposited directly into a user's account.
They are deposited to the user's rewards pool in their connected staking object
and can be withdrawn or restaked at any time.

If you staked using Flow Port, then you should be able to see your staking rewards there.
You can also withdraw the rewards or manually re-stake them through Flow Port.

If you staked using a staking provider such as Kraken, Blocto or Finoa,
please ask them how they manage staking rewards.

### Will staking rewards be automatically re-staked?[​](#will-staking-rewards-be-automatically-re-staked "Direct link to Will staking rewards be automatically re-staked?")

There will be *no* automatic re-staking of staking rewards with Flow Port (i.e. using Ledger or Blocto).
If you want to re-stake your rewards, you must manually do so yourself.

If you staked using a staking provider such as Kraken, Blocto or Finoa,
please ask them what their policies are.

DeFi liquid staking strategies such as offered by [incrementFi](https://app.increment.fi/staking)
are not managed by the protocol or nodes, but are more sophisticated ways
to manage your staking.

### Does it make a difference as to what TYPE of node we delegate to in terms of rewards?[​](#does-it-make-a-difference-as-to-what-type-of-node-we-delegate-to-in-terms-of-rewards "Direct link to Does it make a difference as to what TYPE of node we delegate to in terms of rewards?")

No, rewards are calculated the same for every node type.

### Can a validator change its fees?[​](#can-a-validator-change-its-fees "Direct link to Can a validator change its fees?")

The network enforces a delegation fee of 8% which cannot be directly changed.
Any different fees that nodes claim they have are rebates that they
offer using their own methods and are not enforced by the protocol.

### Can a token holder stake to multiple nodes? If yes, how is the stake split between them?[​](#can-a-token-holder-stake-to-multiple-nodes-if-yes-how-is-the-stake-split-between-them "Direct link to Can a token holder stake to multiple nodes? If yes, how is the stake split between them?")

A token holder can delegate to multiple nodes from a single account if they use the
[Staking Collection](/networks/staking/staking-collection).

The staking collection is enabled by default on Flow port, and many custody providers also support it.

### Is the wallet key transferred to the staked node?[​](#is-the-wallet-key-transferred-to-the-staked-node "Direct link to Is the wallet key transferred to the staked node?")

No - The keys on the node are different from the wallet keys. The wallet keys always stay in the wallet.
A node operator generates the staking and networking keys separately which will be used on the node.

### Can I stake through multiple accounts to meet the minimum FLOW required for staking a node?[​](#can-i-stake-through-multiple-accounts-to-meet-the-minimum-flow-required-for-staking-a-node "Direct link to Can I stake through multiple accounts to meet the minimum FLOW required for staking a node?")

No, the minimum stake must come from a single account for all node types.
Temporarily, the minimum for consensus nodes can come from a combination
of staking actions from two accounts controlled by the same party.

### How can I reach the Consensus node minimum stake of 500K FLOW[​](#how-can-i-reach-the-consensus-node-minimum-stake-of-500k-flow "Direct link to How can I reach the Consensus node minimum stake of 500K FLOW")

The consensus node minimum of 500K FLOW can be met with a minimum
250,000 FLOW staking action and additional delegation
adding a minimum of 250,000 more FLOW from the same entity.

### Is rewards payout another spork?[​](#is-rewards-payout-another-spork "Direct link to Is rewards payout another spork?")

No, rewards payout is not a spork but is an automatic transaction that happens
at the beginning of every new epoch.

### Can I query an account address of a node ID or delegator ID?[​](#can-i-query-an-account-address-of-a-node-id-or-delegator-id "Direct link to Can I query an account address of a node ID or delegator ID?")

The staking smart contract does not directly associate a node or delegator with an account address.
It associates it with the assigned resource object that corresponds to that entry in the contract.
There can be any number of these objects stored in the same account,
and they can be moved to different accounts if the owner chooses.
It is possible to query the information about a node that an address runs though, by using the
`get_node_info_from_address.cdc` script.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/12-faq.md)Last updated on **Feb 5, 2025** by **Brian Doyle**[PreviousMachine Account](/networks/staking/machine-account)[NextTechnical Staking Options](/networks/staking/staking-options)
###### Rate this page

😞😐😊

* [Where will users receive their staking reward for each staking option?](#where-will-users-receive-their-staking-reward-for-each-staking-option)
* [Will staking rewards be automatically re-staked?](#will-staking-rewards-be-automatically-re-staked)
* [Does it make a difference as to what TYPE of node we delegate to in terms of rewards?](#does-it-make-a-difference-as-to-what-type-of-node-we-delegate-to-in-terms-of-rewards)
* [Can a validator change its fees?](#can-a-validator-change-its-fees)
* [Can a token holder stake to multiple nodes? If yes, how is the stake split between them?](#can-a-token-holder-stake-to-multiple-nodes-if-yes-how-is-the-stake-split-between-them)
* [Is the wallet key transferred to the staked node?](#is-the-wallet-key-transferred-to-the-staked-node)
* [Can I stake through multiple accounts to meet the minimum FLOW required for staking a node?](#can-i-stake-through-multiple-accounts-to-meet-the-minimum-flow-required-for-staking-a-node)
* [How can I reach the Consensus node minimum stake of 500K FLOW](#how-can-i-reach-the-consensus-node-minimum-stake-of-500k-flow)
* [Is rewards payout another spork?](#is-rewards-payout-another-spork)
* [Can I query an account address of a node ID or delegator ID?](#can-i-query-an-account-address-of-a-node-id-or-delegator-id)
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

