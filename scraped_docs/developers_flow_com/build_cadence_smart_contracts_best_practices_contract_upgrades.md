# Source: https://developers.flow.com/build/cadence/smart-contracts/best-practices/contract-upgrades

Contract Upgrades with Incompatible Changes | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

    - [Learn Cadence ↗️](/build/cadence/learn-cadence)
    - [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)
    - [Deploying Contracts](/build/cadence/smart-contracts/deploying)
    - [Testing Smart Contracts](/build/cadence/smart-contracts/testing)
    - [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)

      * [Security Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)
      * [Contract Upgrades with Incompatible Changes](/build/cadence/smart-contracts/best-practices/contract-upgrades)
      * [Development Standards](/build/cadence/smart-contracts/best-practices/project-development-tips)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

* Cadence
* Writing and Deploying Smart Contracts
* Best Practices
* Contract Upgrades with Incompatible Changes

On this page

# Contract Upgrades with Incompatible Changes

### Problem[​](#problem "Direct link to Problem")

I have an incompatible upgrade for a contract. How can I deploy this?

### Solution[​](#solution "Direct link to Solution")

Please don't perform incompatible upgrades between contract versions in the same account.
There is too much that can go wrong.

You can make [compatible upgrades](https://cadence-lang.org/docs/language/contract-updatability) and then run a post-upgrade function on the new contract code if needed.

If you must replace your contract rather than update it,
the simplest solution is to add or increase a suffix on any named paths in the contract code
(e.g. `/public/MyProjectVault` becomes `/public/MyProjectVault002`) in addition to making the incompatible changes,
then create a new account and deploy the updated contract there.

⚠️ Flow identifies types relative to addresses, so you will also need to provide *upgrade transactions* to exchange the old contract's resources for the new contract's ones. Make sure to inform users as soon as possible when and how they will need to perform this task.

If you absolutely must keep the old address when making an incompatible upgrade, then you do so at your own risk. Make sure you perform the following actions in this exact order:

1. Delete any resources used in the contract account, e.g. an Admin resource.
2. Delete the contract from the account.
3. Deploy the new contract to the account.

⚠️ Note that if any user accounts contain `structs` or `resources` from the *old* version of the contract that have been replaced with incompatible versions in the new one, **they will not load and will cause transactions that attempt to access them to crash**. For this reason, once any users have received `structs` or `resources` from the contract, this method of making an incompatible upgrade should not be attempted!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/smart-contracts/best-practices/contract-upgrades.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Security Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)[Next

Development Standards](/build/cadence/smart-contracts/best-practices/project-development-tips)

###### Rate this page

😞😐😊

Copy as Markdown

* [Problem](#problem)
* [Solution](#solution)

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