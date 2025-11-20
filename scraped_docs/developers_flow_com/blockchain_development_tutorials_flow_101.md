# Source: https://developers.flow.com/blockchain-development-tutorials/flow-101

Flow Blockchain 101 | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * Flow Blockchain 101

On this page

# Flow Blockchain 101

[![cadence](/images/icons/cadence-logo-mark-black-1.svg)

### Build with Cadence

Get started with Flow's native resource-oriented smart contract language. Learn how to deploy, interact, and build secure dApps using Cadence.](./cadence/getting-started/smart-contract-interaction)[![solidity](/images/icons/flow-evm.svg)

### Build with Solidity

Deploy Solidity contracts on Flow EVM using familiar Ethereum tools like Hardhat and Foundry. Start building EVM-compatible dApps on Flow.](../build/evm/quickstart)

## What is Flow?[​](#what-is-flow "Direct link to What is Flow?")

Flow is a Layer 1 blockchain built from the ground up to support large-scale applications, especially in the world of consumer crypto. Originally developed by the team behind CryptoKitties, Flow was designed to address the limitations they experienced with other blockchains — particularly around scalability and user experience.

At the heart of Flow's design is a modular architecture that separates the responsibilities of consensus, execution, verification, and collection across different node types. This allows the network to process many transactions in parallel without compromising decentralization or safety.

Other defining features of Flow include:

* **Modular architecture** that enables scalability without sharding.
* **Fast finality**, making applications responsive and user-friendly.
* **Resistance to Miner Extractable Value (MEV)**, protecting users from front-running.
* **EVM equivalence**, allowing developers to deploy Solidity contracts on Flow EVM.
* **Low compute fees (on the Cadence side) and low gas fees (on the EVM side)**, which make applications affordable and accessible to users.

Flow has already powered some of the most successful Web3 products to date, including:

* [NBA Top Shot](https://nbatopshot.com/): One of the most widely adopted NFT applications in history.
* [Disney Pinnacle](https://disneypinnacle.com/): A collectible platform with iconic Disney content.
* [CryptoKitties: AllTheZen](https://allthezen.cryptokitties.co/): A spiritual successor to the original CryptoKitties.

### Flow EVM vs Cadence[​](#flow-evm-vs-cadence "Direct link to Flow EVM vs Cadence")

Flow supports two smart contract environments, giving builders the flexibility to use whichever tool fits best:

* **Flow EVM** is fully compatible with the Ethereum Virtual Machine, allowing you to use Solidity, Hardhat, MetaMask, and other familiar tools with no changes.
* **Cadence** is Flow's native smart contract language, purpose-built to handle digital assets safely and intuitively using a resource-oriented programming model.

Developers can build entirely in one or mix both environments for hybrid applications.

## Flow features[​](#flow-features "Direct link to Flow features")

### Onchain randomness[​](#onchain-randomness "Direct link to Onchain randomness")

Flow natively supports verifiable randomness through its built-in Verifiable Random Function (VRF), which developers can use directly in smart contracts. This removes the need for third-party randomness oracles in many cases.

* [Learn more](https://developers.flow.com/blockchain-development-tutorials/native-vrf)

### Batch transactions[​](#batch-transactions "Direct link to Batch transactions")

Batching allows you to group multiple transactions together for atomic execution across both Flow EVM and Cadence-based contracts. This enables powerful cross-VM apps and composability.

* [Explore the tutorial](https://developers.flow.com/blockchain-development-tutorials/cross-vm-apps/introduction)

### Account linking[​](#account-linking "Direct link to Account linking")

Account linking is a unique feature that lets users connect different accounts — such as linking their Dapper Wallet to another address — without compromising control or security. This is particularly useful in onboarding flows and games.

* [Read the guide](https://developers.flow.com/build/cadence/guides/account-linking-with-dapper)

## What Cadence enables[​](#what-cadence-enables "Direct link to What Cadence enables")

Cadence is a smart contract language built specifically for digital assets. It uses a **resource-oriented programming model**, which ensures that assets like NFTs and tokens are treated as first-class citizens that can't be duplicated or accidentally lost.

Key advantages of Cadence include:

* A powerful **account model** that supports multiple keys and roles.
* **Capability-based access control**, which lets users share or restrict access to resources with fine granularity.
* A **resource-oriented system** that prevents bugs common in other ecosystems, like token duplication or loss due to programming mistakes.

Cadence helps developers write safer code, faster — and is a great choice for apps where assets, ownership, and identity matter.

## Building on Flow[​](#building-on-flow "Direct link to Building on Flow")

### Connecting to the network[​](#connecting-to-the-network "Direct link to Connecting to the network")

Flow provides robust support for both Cadence and EVM development. Here's how to get started:

**For Flow EVM:**

* [Connect to Testnet](https://developers.flow.com/protocol/flow-networks/accessing-testnet)
* [Connect to Mainnet](https://developers.flow.com/protocol/flow-networks/accessing-mainnet)

**For Cadence:**

* [Flow Network Overview and Setup](https://developers.flow.com/protocol/flow-networks)

### Developer tools[​](#developer-tools "Direct link to Developer tools")

**Cadence development:**

* [Flow CLI](https://developers.flow.com/tools/flow-cli): Command-line tool for managing accounts, deploying contracts, and running scripts/transactions.
* [@onflow/react-sdk](https://developers.flow.com/tools/react-sdk): A development toolkit to scaffold, simulate, and deploy Cadence apps quickly.

**Flow EVM development:**

* Fully compatible with Ethereum development tools like Hardhat, Foundry, MetaMask, and Ethers.js. If you know how to build for Ethereum, you'll feel right at home.

### Ecosystem partners and tools[​](#ecosystem-partners-and-tools "Direct link to Ecosystem partners and tools")

The Flow ecosystem includes infrastructure providers, wallet integrations, analytics tools, dev tooling, and much more. Browse the full list of partners and recommended resources:

* [Explore the Ecosystem](https://developers.flow.com/ecosystem)

### Join the community[​](#join-the-community "Direct link to Join the community")

Whether you're looking for support, feedback, or collaboration, Flow's community is active and welcoming:

* **Discord**: [Connect](https://discord.com/invite/flow) with other developers and get real-time help.
* **Twitter/𝕏**: Follow [@flow\_blockchain](https://x.com/flow_blockchain) for updates, announcements, and highlights.

### Flow Cadence Quickstart[​](#flow-cadence-quickstart "Direct link to Flow Cadence Quickstart")

* [Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction): Interact with your first Cadence smart contract on the Flow testnet.
* [Local Development](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup): Set up your dev environment, run tests, add already deployed contracts to your environment with Dependency Manager, and deploy and use your first contract with the emulator.
* [Simple Frontend](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app): Read and write from a smart contract using the hooks from [@onflow/react-sdk](https://developers.flow.com/tools/react-sdk).

### Flow EVM Quickstart[​](#flow-evm-quickstart "Direct link to Flow EVM Quickstart")

* [EVM Quickstart](/build/evm/quickstart): Deploy a contract with Hardhat and interact with it using [Testnet Flowscan](https://evm-testnet.flowscan.io/).
* [Foundry](/blockchain-development-tutorials/evm/development-tools/foundry): Build and deploy an ERC20 on Flow with Foundry.

We also have guides for working with [Rainbowkit](/blockchain-development-tutorials/evm/frameworks/rainbowkit) and [wagmi](/blockchain-development-tutorials/evm/frameworks/wagmi).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/flow-101.md)

Last updated on **Nov 18, 2025** by **Brian Doyle**

[Previous

Blockchain Development Tutorials](/blockchain-development-tutorials)[Next

Forte Network Upgrade](/blockchain-development-tutorials/forte)

###### Rate this page

😞😐😊

Copy as Markdown

* [What is Flow?](#what-is-flow)
  + [Flow EVM vs Cadence](#flow-evm-vs-cadence)* [Flow features](#flow-features)
    + [Onchain randomness](#onchain-randomness)+ [Batch transactions](#batch-transactions)+ [Account linking](#account-linking)* [What Cadence enables](#what-cadence-enables)* [Building on Flow](#building-on-flow)
        + [Connecting to the network](#connecting-to-the-network)+ [Developer tools](#developer-tools)+ [Ecosystem partners and tools](#ecosystem-partners-and-tools)+ [Join the community](#join-the-community)+ [Flow Cadence Quickstart](#flow-cadence-quickstart)+ [Flow EVM Quickstart](#flow-evm-quickstart)

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