# Source: https://developers.flow.com/protocol/staking/stake-slashing

Stake Slashing | Flow Developer Portal



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

* * [Staking and Epochs](/protocol/staking)* Stake Slashing

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

Copyright © 2025 Flow Foundation. All Rights Reserved.