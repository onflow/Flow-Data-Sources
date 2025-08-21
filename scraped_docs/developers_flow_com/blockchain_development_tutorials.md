# Source: https://developers.flow.com/blockchain-development-tutorials

Blockchain Development Tutorials | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Actions](/blockchain-development-tutorials/defi)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Token Launch](/blockchain-development-tutorials/token-launch)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [FlowtoBooth](/blockchain-development-tutorials/flowtobooth)
* [Integrations](/blockchain-development-tutorials/integrations/crossmint)

* Blockchain Development Tutorials

On this page

# Blockchain Development Tutorials

Flow Cadence and Flow EVM are two VMs running on the Flow blockchain. A few months after the release of the Crescendo upgrade, we're seeing more apps that aren't Cadence apps -OR- EVM apps, they're both! Cadence unlocks superpowers such as vast computation and storage, native VRF, a much safer and more secure language for handling digital ownership, and more. Flow EVM unlocks the power of the Ethereum ecosystem, allowing you to bring in traditional tools, assets, and liquidity.

For this grand future, we'll need a new suite of blockchain development tutorials, guides, and resources to help you build with the best of both worlds. This section is dedicated to those tutorials.

## [Flow Actions](https://developers.flow.com/tutorials/defi)[​](#flow-actions "Direct link to flow-actions")

Learn how to build composable DeFi applications using the Flow Actions framework. This framework provides a "LEGO" system of reusable components that enable developers to create sophisticated DeFi workflows through atomic composition.

* [Introduction to Flow Actions](/blockchain-development-tutorials/defi/intro-to-flow-actions) - Learn about Flow Actions, a suite of standardized Cadence interfaces that enable developers to compose complex DeFi workflows using small, reusable components
* [Flow Actions Transactions](https://developers.flow.com/tutorials/defi/flow-actions-transaction) - Learn how to create transactions that can chain multiple DeFi operations atomically
* [Connectors](/blockchain-development-tutorials/defi/connectors) - Understand how connectors bridge standardized Flow Actions interfaces with different DeFi protocols
* [Basic Combinations](/blockchain-development-tutorials/defi/basic-combinations) - Learn how to combine Flow Actions to create new workflows
* [Scheduled Callbacks Introduction](/blockchain-development-tutorials/defi/scheduled-callbacks-introduction) - Learn how to implement scheduled callbacks for time-based smart contract execution on Flow

## [Use AI to Build on the Flow Blockchain](https://developers.flow.com/tutorials/use-AI-to-build-on-flow)[​](#use-ai-to-build-on-the-flow-blockchain "Direct link to use-ai-to-build-on-the-flow-blockchain")

Learn how to leverage AI tools to enhance your Flow development experience. These tutorials show you how to integrate various AI assistants with Flow development to boost productivity and code quality.

* [Use Flow Knowledge Base in Cursor](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor) - Learn how to set up Cursor with Flow knowledge bases to get intelligent assistance while developing Flow applications
* [Use Flow Knowledge Base in ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/chatgpt) - Create a custom GPT that understands Flow and Cadence to provide accurate answers to your development questions
* [Claude Code for Flow Development](/blockchain-development-tutorials/use-AI-to-build-on-flow/claude-code) - Learn how to leverage Claude Code for efficient ways to build on Flow and with Cadence
* [Cadence Rules](/blockchain-development-tutorials/use-AI-to-build-on-flow/cadence-rules) - Learn how to use Cursor Rules to enhance AI assistance for Cadence and Flow development with persistent context and automated workflows
* [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp) - Learn how to use Flow MCP (Model Context Protocol) server to enhance AI tools with on-chain interaction capabilities
* [Flow Data Sources](/blockchain-development-tutorials/use-AI-to-build-on-flow/flow-data-sources) - Learn about this comprehensive resource and how to integrate it with various AI platforms
* [Build AI Agents with AgentKit](/blockchain-development-tutorials/use-AI-to-build-on-flow/agentkit-flow-guide) - Learn how to create AI agents that can interact with Flow using AgentKit

## [Token Launch](https://developers.flow.com/tutorials/token-launch)[​](#token-launch "Direct link to token-launch")

Learn how to launch your own token on Flow using Cadence and EVM. This guide covers the process of registering and deploying tokens that can be used across both virtual machines.

* [Register Your ERC20 Token](/blockchain-development-tutorials/token-launch/register-erc20-token) - Learn how to register your ERC20 token on Flow EVM based on Github Pull Request process so it appears in Flow standard Token List which is used by Flow Wallet, MetaMask, and other ecosystem apps.
* [Register Your Assets in Cadence](/blockchain-development-tutorials/token-launch/register-cadence-assets) - Learn how to register your Fungible Token or Non-Fungible Token on Flow through Cadence transaction so it appears in Flow Wallet, IncrementFi, and other ecosystem apps.

## [Cross-VM Applications](https://developers.flow.com/tutorials/cross-vm-apps)[​](#cross-vm-applications "Direct link to cross-vm-applications")

Learn how to build applications that interact with both Cadence and Flow EVM. These tutorials cover everything from basic integration to advanced features like transaction batching and token bridging.

* [Introduction to Cross-VM Applications](/blockchain-development-tutorials/cross-vm-apps/introduction) - Learn how to use FCL with Wagmi and RainbowKit to create a cross-VM app
* [Add Flow Cadence to Your wagmi App](/blockchain-development-tutorials/cross-vm-apps/add-to-wagmi) - Learn how to integrate Flow Cadence with your existing wagmi/RainbowKit application to enable batch transactions and other Cadence features.
* [Interacting with COAs](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa) - Learn how to create and interact with Cadence Owned Accounts (COAs) to control EVM accounts from Cadence
* [Batched EVM Transactions](/blockchain-development-tutorials/cross-vm-apps/batched-evm-transactions) - Discover how to batch multiple EVM transactions into a single Cadence transaction
* [Cross-VM Bridge](/blockchain-development-tutorials/cross-vm-apps/vm-bridge) - Explore how to bridge fungible and non-fungible tokens between Cadence and EVM environments

## [Native VRF (Built-in Randomness) Tutorials](https://developers.flow.com/tutorials/native-vrf)[​](#native-vrf-built-in-randomness-tutorials "Direct link to native-vrf-built-in-randomness-tutorials")

Learn how to leverage Flow's native VRF capabilities in both Cadence and Solidity smart contracts. These tutorials demonstrate how to implement secure randomness without relying on external oracles.

* [Secure Randomness with Commit-Reveal in Cadence](/blockchain-development-tutorials/native-vrf/commit-reveal-cadence) - Learn how to implement secure randomness in Cadence using Flow's commit-reveal scheme
* [VRF (Randomness) in Solidity](/blockchain-development-tutorials/native-vrf/vrf-in-solidity) - Learn how to use Flow's native VRF capabilities in Solidity.
* [Deploy a Solidity Contract Using Cadence](/blockchain-development-tutorials/native-vrf/deploy-solidity-contract) - Discover how to deploy and interact with Solidity contracts on Flow EVM using Cadence

## [Backend Usage](https://developers.flow.com/tutorials/gasless-transactions)[​](#backend-usage "Direct link to backend-usage")

Learn some tips and tutorials for interacting with the Flow blockchain in a backend application.

* [Gas Free EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/gas-free-evm-endpoint) - Learn how to set up a gas free EVM endpoint for your backend, all transactions sent through this endpoint will not be charged for gas fees from the transaction sender's account.

## [FlowtoBooth](https://developers.flow.com/tutorials/flowtobooth)[​](#flowtobooth "Direct link to flowtobooth")

Explore Flow's unique capabilities through fun benchmark applications that showcase what's possible with Flow's efficient gas pricing. These tutorials demonstrate practical applications of Flow's advanced features.

* [Build a Fully-Onchain Image Gallery](/blockchain-development-tutorials/flowtobooth/image-gallery) - Create a fully onchain image gallery that demonstrates Flow's efficient storage capabilities

### Building in Web3 has never been easier[​](#building-in-web3-has-never-been-easier "Direct link to Building in Web3 has never been easier")

Flow will continue to provide quality walkthroughs and tutorials to provide developers all of the tools needed to build the next generation of web3 apps on a fast blockchain, with built in randomness, gasless transactions, and AI integration.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/index.md)

Last updated on **Aug 20, 2025** by **0xLisanAlGaib**

[Next

Flow Actions](/blockchain-development-tutorials/defi)

###### Rate this page

😞😐😊

Copy as Markdown

* [Flow Actions](#flow-actions)
* [Use AI to Build on the Flow Blockchain](#use-ai-to-build-on-the-flow-blockchain)
* [Token Launch](#token-launch)
* [Cross-VM Applications](#cross-vm-applications)
* [Native VRF (Built-in Randomness) Tutorials](#native-vrf-built-in-randomness-tutorials)
* [Backend Usage](#backend-usage)
* [FlowtoBooth](#flowtobooth)
  + [Building in Web3 has never been easier](#building-in-web3-has-never-been-easier)

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
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.