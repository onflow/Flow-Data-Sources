# Source: https://developers.flow.com/protocol/staking/stake-slashing

Stake Slashing | Flow Developer Portal



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
* Stake Slashing

# Stake Slashing

Flow slashes nodes only for acts that directly impact
the security and integrity of the network and its shared execution state.
Nodes are not slashed for liveness infractions.
The protocol reserves slashing for maintaining the security of the protocol rather than its liveness.

You can find more details on the conditions under which a node is slashed
in the [Flow whitepapers](https://www.onflow.org/technical-paper).

Direct stake slashing is not currently enforced by the protocol and staking contract.
It will be handled on a case-by-case basis for the foreseeable future
to ensure network participants have time to participate in the testing and rollout of slashing.

There is a very basic form of slashing that is currently used, where
nodes who have liveness issues during an epoch may have their rewards
and their delegators' rewards reduced by a pre-determinded amount based on
the severity of the liveness infractions. This amount is often 50%
and is only taken from the stakers' rewards for a given epoch.
Their staked FLOW is not touched at all.

When slashing is enforced, slashable protocol violations must be adjudicated by a supermajority
of more than 2/3 of the staked consensus nodes in order to take effect.
If a node is found guilty of committing a slashable protocol violation,
the consensus nodes directly deduct a fine from the node's stake.

It is still TBD where the slashed tokens will be deposited.

The remaining un-slashed stake is deposited back into node's unstaked pool
at the end of the unstaking period.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/04-stake-slashing.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Epoch Preparation Protocol](/protocol/staking/epoch-preparation)[Next

Epoch Scripts and Events](/protocol/staking/epoch-scripts-events)

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