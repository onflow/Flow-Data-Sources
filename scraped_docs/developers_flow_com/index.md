# Source: https://developers.flow.com/

Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

# Better apps deserve better blockchains

**Cadence** for whats next. **Solidity** for what you've got. On Flow, both run natively with no tricks and no rewrites. **Build the next killer app**.

[Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)Start with Cadence

### Cadence

Building something new? Start with Cadence — built for apps, automation, and secure upgrades from day one.

[![why-flow](/images/icons/why-flow.svg)

Automate DeFi with actions and scheduled transactions](/blockchain-development-tutorials/forte)[![flow-cadence](/images/icons/flow-cadence.svg)

Create apps that evolve without a proxy contract](/blockchain-development-tutorials/cadence/cadence-advantages)[![flow-cadence](/images/icons/flow-cadence.svg)

Build faster with React components and hooks](/build/tools/react-sdk)

### Solidity

Already writing Solidity? Bring it over unchanged — then level it up with Flow's MEV-resistance, VRF, and cross-VM composability.

[![evm-on-flow](/images/icons/evm-on-flow.svg)

Deploy Solidity apps on Flow without code changes](/build/evm/quickstart)[![random](/images/icons/random.svg)

Add secure randomness with native VRF in 3 lines](../blockchain-development-tutorials/native-vrf/vrf-in-solidity)[![batched-evm-transactions](/images/icons/batched-evm-transactions.svg)

Simplify user experience with batched transactions](../blockchain-development-tutorials/cross-vm-apps)

[## Why Flow?

Flow supports both **Cadence** and **Solidity**, scales to millions of users without sharding, and provides MEV resistance with ultra-low fees. Built for consumer apps.

Learn more](/build/flow)

## Try Cadence Live

Flow token account balanceAccount storage limit and usageOnchain counter current countBalance of custom tokenNBA Top Shot and NFL All Day

![Flow](/images/logos/flow-runner-flow-icon.svg)

**Open**

**Run

**Share

**Download

**Settings

**

Flow token account balance

1

2

3

4

5

6

7

8

9

10

11

12

13

import FungibleToken from 0xf233dcee88fe0abe

// Returns the balance of the stored Vault at

// the given address if exists, otherwise nil

// Run this with this address: 0xfeb88a0fcc175a3d

access(all) fun main(address: Address): UFix64? {

let path = StoragePath(identifier: "flowTokenVault")

return getAuthAccount<auth(BorrowValue) &Account>(address).storage.borrow<{FungibleToken.Vault}>(

from: path!

)?.balance ?? nil

}

Hover to load interactive examples

**0 Errors

**Environment: Flow Mainnet****

![tools](/images/icons/flow-tools.svg)

## Tools

[![faucet](/images/icons/Faucet.svg)

### Get 100k testnet $FLOW

Other chains drip testnet tokens, Flow gives you 100k $FLOW to play with.](https://faucet.flow.com/fund-account)[![tools](/images/icons/flow-tools.svg)

### Build and ship with Flow CLI

Stop wrestling with setup and boilerplate. Flow CLI lets you initialize projects, manage accounts and contracts, send transactions, and query chain state from one simple tool. Test locally, deploy to testnet or mainnet, and keep dependencies in sync.](/build/tools/flow-cli)[![flow-client-library](/images/icons/flow-client-library.svg)

### Use your favorite platform and tools

Connect with Thirdweb, Crossmint, Dynamic, Privy, and other popular blockchain infrastructure platforms to enhance user experience and reduce development complexity.](/blockchain-development-tutorials/integrations)

![grow](/images/icons/flow-grow.svg)

## Builder toolkit to start, grow, and win

[![vcs-&-funds](/images/icons/vcs-&-funds.svg)

### Developer Support Hub

Access builder perks, grants, and VCs and funds. Get comprehensive support including technical guidance, marketing resources, and ecosystem connections.](/ecosystem/developer-support-hub)[![dev-office-hours](/images/icons/dev-office-hours.svg)

### Dev Office Hours

Join our weekly developer office hours to get direct support from the Flow team and connect with other builders.](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)[![access-incredible-ip](/images/icons/access-incredible-ip.svg)

### Hackathons and Events

Start building at a hackathon or meet us at an event. Join Flow community events and competitions.](/ecosystem/Hackathons%20and%20Events)

## Browse by Category

### Cadence

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/cadence/differences-vs-evm)
* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
* [Basics](/build/cadence/basics/blocks)
* [Writing and Deploying Smart Contracts](/build/cadence/smart-contracts/overview)
* [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
* [Guides](/build/cadence/advanced-concepts/account-abstraction)
* [Core Smart Contracts](/build/cadence/core-contracts)
* [Explore More](/build/cadence/explore-more)

### EVM

* [EVM Quickstart](/evm/quickstart)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Network Information](/evm/networks)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges](/ecosystem/bridges)
* [Faucets](/ecosystem/faucets)
* [Block Explorers](/ecosystem/block-explorers)
* [Guides](/evm/guides)

### Tools

* [@onflow/react-sdk](/tools/react-sdk)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

### Networks

* [Flow Networks](/protocol/flow-networks)
* [Mainnet](/protocol/flow-networks/accessing-mainnet)
* [Testnet](/protocol/flow-networks/accessing-testnet)
* [Network Architecture](/protocol/network-architecture)
* [Staking and Epochs](/protocol/staking)
* [Node Ops](/protocol/node-ops)
* [Accessing Data](/protocol/access-onchain-data)
* [Governance](/protocol/governance)
* [Flow Port](/protocol/flow-port)

### Ecosystem

* [Ecosystem](/ecosystem)
* [Wallets](/ecosystem/wallets)
* [Flow Block Explorers](/ecosystem/block-explorers)
* [Data Indexers](/ecosystem/data-indexers)
* [Developer Profile](/ecosystem/developer-profile)
* [DeFi & Liquidity](/ecosystem/defi-liquidity)
* [Bridges](/ecosystem/bridges)
* [Community Projects](/ecosystem/projects)
* [Builder Perks](/ecosystem/builder-perks)
* [VCs & Funds](/ecosystem/vcs-and-funds)
* [Faucets](/ecosystem/faucets)
* [Grants](/ecosystem/grants)
* [Hackathons and Events](/ecosystem/Hackathons%20and%20Events)
* [Auditors](/ecosystem/auditors)

### Tutorials

* [Tutorials](/tutorials)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Token Launch](/blockchain-development-tutorials/token-launch)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [FlowtoBooth](/blockchain-development-tutorials/flowtobooth)
* [Native VRF](/blockchain-development-tutorials/native-vrf)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
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