# Source: https://developers.flow.com/protocol/network-architecture/user-safety

User safety | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)
* [Networks](/protocol)
* [Flow Network Architecture](/protocol/network-architecture)

  + [Solving the blockchain trilemma](/protocol/network-architecture/solving-blockchain-trilemma)
  + [Sustainability](/protocol/network-architecture/sustainability)
  + [User safety](/protocol/network-architecture/user-safety)
* [Staking and Epochs](/protocol/staking)
* [Node Ops](/protocol/node-ops)
* [Accessing Data](/protocol/access-onchain-data)
* [Governance](/protocol/governance)
* [Flow Port](/protocol/flow-port)

* [Flow Network Architecture](/protocol/network-architecture)
* User safety

# User Safety with Flow

The monolithic node design of common L1s such as Bitcoin and Ethereum overly privileges operator control over block production.
This makes the chain vulnerable to censorship and MEV attacks. This problem is exacerbated by L2s with centralized sequencers. ERC-4337 is also susceptible to MEV on the user operations via bundlers.

![mev](/assets/images/mev_attack-b4d72fcf8ae40bb4ff46a06d6c4322e1.png)

Flow’s multi-role architecture provides censorship & MEV resistance by design:

* Transactions are randomly assigned to collection nodes for inclusion in collections and eventually in blocks. Each collection node only sees a subset of transactions.
* There is already a distinct separation between the proposers (represented by the collection nodes) and the builders (represented by the consensus nodes). This separation essentially provides an inherent implementation of "proposer-builder separation," a concept currently being explored by Ethereum. With this separation, even if the collection nodes were to reorder the transactions, there is no incentive for the consensus nodes to prefer one collection node’s proposal over another.

![mev_protection](/assets/images/mev_protection_in_flow-cb8116a0c2f0defaf2ec9bed7c552eb6.png)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/network-architecture/user-safety.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Sustainability](/protocol/network-architecture/sustainability)[Next

Staking and Epochs](/protocol/staking)

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
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.