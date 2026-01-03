# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/getting-started

Getting Started with Cadence | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            - [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)- [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)- [Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)- [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)+ [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)+ [Emulator Fork Testing](/blockchain-development-tutorials/cadence/emulator-fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* Getting Started with Cadence

On this page

# Getting Started With Cadence

The Cadence is designed for the next generation of apps, games, and digital assets. This comprehensive tutorial series will guide you from development environment setup to production-ready application deployment on Flow's mainnet as a complete Counter application that demonstrates all essential Flow development patterns.

## What you'll learn[​](#what-youll-learn "Direct link to What you'll learn")

In this tutorial series, you'll discover how to:

* Set up a complete Flow development environment with CLI tools and local emulator.
* Build and deploy smart contracts with Cadence.
* Integrate external dependencies and work with Flow's composable ecosystem.
* Create transactions and implement comprehensive testing strategies.
* Build interactive frontend applications with @onflow/react-sdk.
* Deploy applications to testnet and mainnet with production best practices.
* Implement monitoring, security, and maintenance for live blockchain applications.

## What you'll build[​](#what-youll-build "Direct link to What you'll build")

Throughout these tutorials, you'll build a complete **Counter Application** that demonstrates the core aspects of Flow development:

* **Smart Contracts**: counter contract with increment/decrement functionality.
* **External Dependencies**: integration with NumberFormatter for enhanced display.
* **Frontend Interface**: react-based web application with wallet authentication.
* **Production Deployment**: live application accessible on Flow's public networks.

By the end, you'll have a fully functional blockchain application and the skills to build your own Flow projects.

## Environment setup[​](#environment-setup "Direct link to Environment setup")

Learn how to set up your Flow development environment and deploy your first smart contract. This foundational tutorial covers CLI installation, project creation, contract deployment, and basic blockchain interaction patterns with the local Flow emulator.

Tutorial: [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)

## Smart contract interaction[​](#smart-contract-interaction "Direct link to Smart contract interaction")

Gain advanced Flow development skills including dependency management, sophisticated transaction patterns, and comprehensive testing strategies. Learn to integrate external contracts, handle complex state changes, and implement test-driven development workflows.

Tutorial: [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)

## Build a frontend app[​](#build-a-frontend-app "Direct link to Build a frontend app")

Create a `Next.js` frontend application that interacts with your Flow smart contracts via `@onflow/react-sdk`. Implement wallet authentication, real-time data queries, transaction submission, and status monitoring for a complete user experience.

Tutorial: [Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)

## Production deployment[​](#production-deployment "Direct link to Production deployment")

To take your application live, deploy to Flow's testnet and mainnet networks. Learn security best practices, production configuration, monitoring strategies, and maintenance practices you can use to manage live blockchain applications.

Tutorial: [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)

## Next steps[​](#next-steps "Direct link to Next steps")

After you complete these tutorials, you'll have the fundamental skills needed for Flow development. You can explore our other tutorial series to expand your blockchain development expertise:

* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps/introduction) - Build applications that integrate Flow EVM and Cadence
* [Native VRF](/blockchain-development-tutorials/native-vrf) - Implement verifiable random functions in your applications
* [Token Launch](/blockchain-development-tutorials/tokens) - Create and launch tokens on Flow

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/getting-started/index.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Cadence Tutorials](/blockchain-development-tutorials/cadence)[Next

Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)

###### Rate this page

😞😐😊

Copy as Markdown

* [What you'll learn](#what-youll-learn)* [What you'll build](#what-youll-build)* [Environment setup](#environment-setup)* [Smart contract interaction](#smart-contract-interaction)* [Build a frontend app](#build-a-frontend-app)* [Production deployment](#production-deployment)* [Next steps](#next-steps)

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