# Source: https://developers.flow.com/build/cadence/smart-contracts/best-practices/contract-upgrades

Contract Upgrades with Incompatible Changes | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            - [Learn Cadence ↗️](/build/cadence/learn-cadence)- [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)- [Deploying Contracts](/build/cadence/smart-contracts/deploying)- [Testing Smart Contracts](/build/cadence/smart-contracts/testing-strategy)- [Cadence Testing Framework](/build/cadence/smart-contracts/testing)- [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)

                        * [Security Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)* [Contract Upgrades with Incompatible Changes](/build/cadence/smart-contracts/best-practices/contract-upgrades)* [Development Standards](/build/cadence/smart-contracts/best-practices/project-development-tips)+ [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Writing and Deploying Smart Contracts* Best Practices* Contract Upgrades with Incompatible Changes

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

* [Problem](#problem)* [Solution](#solution)

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