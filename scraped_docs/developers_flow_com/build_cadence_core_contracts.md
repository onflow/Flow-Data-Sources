# Source: https://developers.flow.com/build/cadence/core-contracts

Flow Core Contracts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)

                - [Fungible Token](/build/cadence/core-contracts/fungible-token)- [Flow Token](/build/cadence/core-contracts/flow-token)- [Service Account](/build/cadence/core-contracts/service-account)- [Flow Fees](/build/cadence/core-contracts/flow-fees)- [Staking Table](/build/cadence/core-contracts/staking-contract-reference)- [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)- [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)- [NFT Metadata](/build/cadence/core-contracts/nft-metadata)- [NFT Storefront](/build/cadence/core-contracts/nft-storefront)- [Staking Collection](/build/cadence/core-contracts/staking-collection)- [Account Linking](/build/cadence/core-contracts/hybrid-custody)- [EVM](/build/cadence/core-contracts/evm)- [Burner](/build/cadence/core-contracts/burner)- [VM Bridge](/build/cadence/core-contracts/bridge)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Core Smart Contracts

# Flow Core Contracts

Flow relies on a set of core contracts that define key portions of the
Flow protocol.

These contracts control the following:

* Standard fungible token behavior. ([FungibleToken, FungibleTokenMetadataViews, FungibleTokenSwitchboard, Burner](/build/cadence/core-contracts/fungible-token))
* Flow Protocol Token. ([FlowToken](/build/cadence/core-contracts/flow-token))
* Flow Service Account. ([ServiceAccount, NodeVersionBeacon, RandomBeaconHistory](/build/cadence/core-contracts/service-account))
* Account, transaction and storage fee payments. ([FlowFees and FlowStorageFees](/build/cadence/core-contracts/flow-fees))
* Staking and delegation ([FlowIDTableStaking](/build/cadence/core-contracts/staking-contract-reference))
* Epochs ([FlowEpoch, FlowClusterQC, FlowDKG](/build/cadence/core-contracts/epoch-contract-reference))

There are other important contracts that aren't part of the core protocol
but are nevertheless important to developers on Flow:

* Standard Non-Fungible Token Behavior. ([NonFungibleToken](/build/cadence/core-contracts/non-fungible-token))
* NFT Metadata Standard. ([MetadataViews, ViewResolver](/build/cadence/core-contracts/nft-metadata))
* Staking Collection. ([StakingCollection](/build/cadence/core-contracts/staking-collection))
* NFT Storefronts. ([NFTStorefront](/build/cadence/core-contracts/nft-storefront))
* Account linking and Hybrid Custody. ([AccountLinking](/build/cadence/core-contracts/hybrid-custody))
* EVM interfacing contract. ([EVM](/build/cadence/core-contracts/evm))

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/index.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)[Next

Fungible Token](/build/cadence/core-contracts/fungible-token)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.