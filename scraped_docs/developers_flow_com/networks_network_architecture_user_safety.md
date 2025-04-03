# Source: https://developers.flow.com/networks/network-architecture/user-safety

User safety | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)

  + [Solving the blockchain trilemma](/networks/network-architecture/solving-blockchain-trilemma)
  + [Sustainability](/networks/network-architecture/sustainability)
  + [User safety](/networks/network-architecture/user-safety)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Flow's Network Architecture](/networks/network-architecture)
* User safety

# User Safety with Flow

The monolithic node design of common L1s such as Bitcoin and Ethereum overly privileges operator control over block production.
This makes the chain vulnerable to censorship and MEV attacks. This problem is exacerbated by L2s with centralized sequencers. ERC-4337 is also susceptible to MEV on the user operations via bundlers.

![mev](/assets/images/mev_attack-b4d72fcf8ae40bb4ff46a06d6c4322e1.png)

Flow’s multi-role architecture provides censorship & MEV resistance by design:

* Transactions are randomly assigned to collection nodes for inclusion in collections and eventually in blocks. Each collection node only sees a subset of transactions.
* There is already a distinct separation between the proposers (represented by the collection nodes) and the builders (represented by the consensus nodes). This separation essentially provides an inherent implementation of "proposer-builder separation," a concept currently being explored by Ethereum. With this separation, even if the collection nodes were to reorder the transactions, there is no incentive for the consensus nodes to prefer one collection node’s proposal over another.

![mev_protection](/assets/images/mev_protection_in_flow-cb8116a0c2f0defaf2ec9bed7c552eb6.png)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/network-architecture/user-safety.md)

Last updated on **Mar 28, 2025** by **Brian Doyle**

[Previous

Sustainability](/networks/network-architecture/sustainability)[Next

Staking and Epochs](/networks/staking)

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