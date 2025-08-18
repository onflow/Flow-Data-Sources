# Source: https://developers.flow.com/tutorials

Tutorials | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [Flow Actions](/tutorials/defi)
* [Flow Blockchain 101](/tutorials/flow-101)
* [Use AI To Build On Flow](/tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/tutorials/gasless-transactions)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/tutorials/native-vrf)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Integrations](/tutorials/integrations/crossmint)

* Tutorials

On this page

# Tutorials

Flow Cadence and Flow EVM are two VMs running on the Flow blockchain. A few months after the release of the Crescendo upgrade, we're seeing more apps that aren't Cadence apps -OR- EVM apps, they're both! Cadence unlocks superpowers such as vast computation and storage, native VRF, a much safer and more secure language for handling digital ownership, and more. Flow EVM unlocks the power of the Ethereum ecosystem, allowing you to bring in traditional tools, assets, and liquidity.

For this grand future, we'll need a new suite of tutorials, guides, and resources to help you build with the best of both worlds. This section is dedicated to those tutorials.

## Flow Actions[​](#flow-actions "Direct link to Flow Actions")

Learn how to build composable DeFi applications using the Flow Actions framework. This framework provides a "LEGO" system of reusable components that enable developers to create sophisticated DeFi workflows through atomic composition.

* [Introduction to Flow Actions](/tutorials/defi/intro-to-flow-actions) - Learn about Flow Actions, a suite of standardized Cadence interfaces that enable developers to compose complex DeFi workflows using small, reusable components
* [Connectors](/tutorials/defi/connectors) - Understand how connectors bridge standardized Flow Actions interfaces with different DeFi protocols
* [Basic Combinations](/tutorials/defi/basic-combinations) - Learn how to combine Flow Actions to create new workflows
* [Scheduled Callbacks Introduction](/tutorials/defi/scheduled-callbacks-introduction) - Learn how to implement scheduled callbacks for time-based smart contract execution on Flow

## AI Plus Flow[​](#ai-plus-flow "Direct link to AI Plus Flow")

Learn how to leverage AI tools to enhance your Flow development experience. These tutorials show you how to integrate various AI assistants with Flow development to boost productivity and code quality.

* [Use Flow Knowledge Base in Cursor](/tutorials/use-AI-to-build-on-flow/cursor) - Learn how to set up Cursor with Flow knowledge bases to get intelligent assistance while developing Flow applications
* [Use Flow Knowledge Base in ChatGPT](/tutorials/use-AI-to-build-on-flow/chatgpt) - Create a custom GPT that understands Flow and Cadence to provide accurate answers to your development questions
* [Claude Code for Flow Development](/tutorials/use-AI-to-build-on-flow/claude-code) - Learn how to leverage Claude Code for efficient ways to build on Flow and with Cadence
* [Cadence Rules](/tutorials/use-AI-to-build-on-flow/cadence-rules) - Learn how to use Cursor Rules to enhance AI assistance for Cadence and Flow development with persistent context and automated workflows
* [Flow MCP](/tutorials/use-AI-to-build-on-flow/mcp) - Learn how to use Flow MCP (Model Context Protocol) server to enhance AI tools with on-chain interaction capabilities
* [Flow Data Sources](/tutorials/use-AI-to-build-on-flow/flow-data-sources) - Learn about this comprehensive resource and how to integrate it with various AI platforms
* [Build AI Agents with AgentKit](/tutorials/use-AI-to-build-on-flow/agentkit-flow-guide) - Learn how to create AI agents that can interact with Flow using AgentKit

## Backend Usage[​](#backend-usage "Direct link to Backend Usage")

Learn some tips and tutorials for interacting with the Flow blockchain in a backend application.

* [Gas Free EVM Endpoint](/tutorials/gasless-transactions/gas-free-evm-endpoint) - Learn how to set up a gas free EVM endpoint for your backend, all transactions sent through this endpoint will not be charged for gas fees from the transaction sender's account.

## Token Launch[​](#token-launch "Direct link to Token Launch")

Learn how to launch your own token on Flow using Cadence and EVM. This guide covers the process of registering and deploying tokens that can be used across both virtual machines.

* [Register Your ERC20 Token](/tutorials/token-launch/register-erc20-token) - Learn how to register your ERC20 token on Flow EVM based on Github Pull Request process so it appears in Flow standard Token List which is used by Flow Wallet, MetaMask, and other ecosystem apps.
* [Register Your Assets in Cadence](/tutorials/token-launch/register-cadence-assets) - Learn how to register your Fungible Token or Non-Fungible Token on Flow through Cadence transaction so it appears in Flow Wallet, IncrementFi, and other ecosystem apps.

## Cross-VM Applications[​](#cross-vm-applications "Direct link to Cross-VM Applications")

Learn how to build applications that interact with both Cadence and Flow EVM. These tutorials cover everything from basic integration to advanced features like transaction batching and token bridging.

* [Introduction to Cross-VM Applications](/tutorials/cross-vm-apps/introduction) - Learn how to use FCL with Wagmi and RainbowKit to create a cross-VM app
* [Add Flow Cadence to Your wagmi App](/tutorials/cross-vm-apps/add-to-wagmi) - Learn how to integrate Flow Cadence with your existing wagmi/RainbowKit application to enable batch transactions and other Cadence features.
* [Interacting with COAs](/tutorials/cross-vm-apps/interacting-with-coa) - Learn how to create and interact with Cadence Owned Accounts (COAs) to control EVM accounts from Cadence
* [Batched EVM Transactions](/tutorials/cross-vm-apps/batched-evm-transactions) - Discover how to batch multiple EVM transactions into a single Cadence transaction
* [Cross-VM Bridge](/tutorials/cross-vm-apps/vm-bridge) - Explore how to bridge fungible and non-fungible tokens between Cadence and EVM environments

## Native VRF[​](#native-vrf "Direct link to Native VRF")

Learn how to leverage Flow's native VRF capabilities in both Cadence and Solidity smart contracts. These tutorials demonstrate how to implement secure randomness without relying on external oracles.

* [Secure Randomness with Commit-Reveal in Cadence](/tutorials/native-vrf/commit-reveal-cadence) - Learn how to implement secure randomness in Cadence using Flow's commit-reveal scheme
* [VRF (Randomness) in Solidity](/tutorials/native-vrf/vrf-in-solidity) - Learn how to use Flow's native VRF capabilities in Solidity.
* [Deploy a Solidity Contract Using Cadence](/tutorials/native-vrf/deploy-solidity-contract) - Discover how to deploy and interact with Solidity contracts on Flow EVM using Cadence

## FlowtoBooth[​](#flowtobooth "Direct link to FlowtoBooth")

Explore Flow's unique capabilities through fun benchmark applications that showcase what's possible with Flow's efficient gas pricing. These tutorials demonstrate practical applications of Flow's advanced features.

* [Build a Fully-Onchain Image Gallery](/tutorials/flowtobooth/image-gallery) - Create a fully onchain image gallery that demonstrates Flow's efficient storage capabilities

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/index.md)

Last updated on **Aug 14, 2025** by **Felipe Cevallos**

[Next

Flow Actions](/tutorials/defi)

###### Rate this page

😞😐😊

Copy as Markdown

* [Flow Actions](#flow-actions)
* [AI Plus Flow](#ai-plus-flow)
* [Backend Usage](#backend-usage)
* [Token Launch](#token-launch)
* [Cross-VM Applications](#cross-vm-applications)
* [Native VRF](#native-vrf)
* [FlowtoBooth](#flowtobooth)

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