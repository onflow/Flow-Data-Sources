# Source: https://developers.flow.com/build/cadence/core-contracts

Flow Core Contracts | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

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

* Standard Non-Fungible Token Behavior. ([NonFungibleToken])
* NFT Metadata Standard. ([MetadataViews, ViewResolver])
* Staking Collection. ([StakingCollection])
* NFT Storefronts. ([NFTStorefront])
* Account linking and Hybrid Custody. ([AccountLinking])
* EVM interfacing contract. ([EVM])

[NonFungibleToken]: ./08-non-fungible-token.md))
[MetadataViews, ViewResolver]: ./09-nft-metadata.md))
[StakingCollection]: ./11-staking-collection.md
[NFTStorefront]: ./10-nft-storefront.md
[AccountLinking]: ./12-hybrid-custody.md
[EVM]: ./13-evm.md)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/index.md)

Last updated on **Dec 3, 2025** by **cshannon1218**

[Previous

Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)[Next

Fungible Token](/build/cadence/core-contracts/fungible-token)

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