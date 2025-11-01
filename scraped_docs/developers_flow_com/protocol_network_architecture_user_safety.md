# Source: https://developers.flow.com/protocol/network-architecture/user-safety

User safety | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      + [Solving the blockchain trilemma](/protocol/network-architecture/solving-blockchain-trilemma)+ [Sustainability](/protocol/network-architecture/sustainability)+ [User safety](/protocol/network-architecture/user-safety)* [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Flow Network Architecture](/protocol/network-architecture)* User safety

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