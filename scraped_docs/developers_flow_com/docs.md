# Source: https://developers.flow.com/docs/

Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

# Better apps deserve better blockchains

**Cadence** for whats next. **Solidity** for what you've got. On Flow, both run natively with no tricks and no rewrites. **Build the next killer app**.

[Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)Start with Cadence

### Cadence

A purpose-build smart contract language for apps that do more than token movement.

[![why-flow](/images/icons/why-flow.svg)

Why Flow?](/build/flow)[![hello-world](/images/icons/hello-world.svg)

Query state and run transactions](https://run.dnz.dev/)[![flow-cadence](/images/icons/flow-cadence.svg)

Build quickly & securely with Cadence](https://cadence-lang.org)

### Solidity

EVM equivalence with seamless composability and interoperability with Cadence.

[![evm-on-flow](/images/icons/evm-on-flow.svg)

Simply run with EVM equivalence](/build/evm/quickstart)[![random](/images/icons/random.svg)

Integrate native VRF in 3 lines](../blockchain-development-tutorials/native-vrf/vrf-in-solidity)[![batched-evm-transactions](/images/icons/batched-evm-transactions.svg)

Native batched transactions](../blockchain-development-tutorials/cross-vm-apps)

### Tools

Best in class tools powering best in class applications builders.

[![flow-client-library](/images/icons/flow-client-library.svg)

Build apps fast](/tools/react-sdk)[![tools](/images/icons/flow-tools.svg)

Import and compose with contracts](/tools/flow-cli/dependency-manager)[![faucet](/images/icons/Faucet.svg)

Get 100k testnet $FLOW](https://faucet.flow.com/fund-account)

## Try it live

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

![grow](/images/icons/flow-grow.svg)

## Builder toolkit to start, grow, and win

[![builder-credits](/images/icons/builder-credits.svg)

### Builder Perks

Access thousands of dollars worth of Builder perks for building on Flow!](/ecosystem/builder-perks)[![dev-office-hours](/images/icons/dev-office-hours.svg)

### Dev Office Hours

Join our weekly developer office hours to get direct support from the Flow team and connect with other builders.](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)[![grants](/images/icons/flow-grants.svg)

### Grants

Discover grant opportunities available to developers and teams building on Flow.](/ecosystem/grants)[![startup-support](/images/icons/startup-support.svg)

### Startup Support

Get comprehensive support including technical guidance, marketing resources, and ecosystem connections.](/growth)[![vcs-&-funds](/images/icons/vcs-&-funds.svg)

### VCs & Funds

Connect with venture capital firms and investment funds actively supporting Flow projects.](/ecosystem/vcs-and-funds)

## Browse by Category

### Cadence

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/cadence/differences-vs-evm)
* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Flow Protocol](/build/cadence/basics/blocks)
* [App Architecture](/build/cadence/app-architecture)
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
* [Ecosystem Overview](/ecosystem/overview)

### Tutorials

* [Tutorials](/tutorials)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Token Launch](/blockchain-development-tutorials/token-launch)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [FlowtoBooth](/blockchain-development-tutorials/flowtobooth)
* [Native VRF](/blockchain-development-tutorials/native-vrf)

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
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.