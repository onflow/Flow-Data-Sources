# Source: https://developers.flow.com/protocol/staking/staking-options

Options for Building Staking Integrations | Flow Developer Portal



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
* Technical Staking Options

This document describes two different methods for staking at a high level.

warning

We highly recommended you use the Staking Collection paradigm,
as this will be the most supported method for staking with any set up.

# Staking Collection

A Staking Collection is a resource that allows its owner to manage multiple staking
objects in a single account via a single storage path, and perform staking actions
using Flow. It also supports machine accounts, a necessary feature for Flow epoch node operation.

The staking collection paradigm is the most flexible of the three choices
and will receive the most support in the future. It is the set-up that Flow Port and many other staking providers use.

The staking collection setup and guide is detailed in the [staking collection guide.](/protocol/staking/staking-collection)

# Staking

The basic method to stake is to stake directly with the `FlowIDTableStaking` smart contract.
This would involve calling the node or delegator registration functions directly in the staking
contract and storing the staking objects directly in account storage.

This is probably the simplest way to implement this, but it is not very flexible
and not recommended.

The basic staking guide is detailed [here](/protocol/staking/staking-guide)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/13-staking-options.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

FAQs](/protocol/staking/faq)[Next

Staking Collection Guide](/protocol/staking/staking-collection)

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
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.