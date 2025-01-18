# Source: https://cadence-lang.org/docs/cadence-migration-guide/core-contracts-guide




Protocol Smart Contracts 1.0 Changes Guide | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
  + [Improvements & New Features](/docs/cadence-migration-guide/improvements)
  + [NFT Cadence 1.0 Guide](/docs/cadence-migration-guide/nft-guide)
  + [FT Cadence 1.0 Guide](/docs/cadence-migration-guide/ft-guide)
  + [Core Contracts Guide](/docs/cadence-migration-guide/core-contracts-guide)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* Core Contracts Guide
On this page
# Protocol Smart Contracts 1.0 Changes Guide

## Protocol Smart Contracts in Cadence 1.0[​](#protocol-smart-contracts-in-cadence-10 "Direct link to Protocol Smart Contracts in Cadence 1.0")

On September 4th, 2024 the Flow Mainnet upgraded to Cadence 1.0.
In addition to many changes to the Cadence programming language and
the Cadence token standards, the Flow Protocol smart contracts
also updated to be compatible with the changes.

All applications that interact with these contracts need to update their transactions and scripts
in order to be compatible with the changes.

## Important Info[​](#important-info "Direct link to Important Info")

This document assumes you have a basic understanding of the
[Cadence 1.0 improvements](/docs/cadence-migration-guide/improvements) and modifications to the Fungible Token Standard.
We encourage you to consult those guides for more details on these changes if you are interested.

The updated code for the Cadence 1.0 versions of the protocol smart contracts is located in the
[`master` branch of the flow-core-contracts repo](https://github.com/onflow/flow-core-contracts).
Please look at the [PR that made the changes](https://github.com/onflow/flow-core-contracts/pull/319)
to understand how the contracts have changed. Every contract in the repo changed.

Additionally, here are the import addresses
for all of the important contracts related to the protocol:

| Contract | Emulator Import Address | Testing Framework |
| --- | --- | --- |
| `FungibleToken` | `0xee82856bf20e2aa6` | `0x0000000000000002` |
| `ViewResolver` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `Burner` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `MetadataViews` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FungibleTokenMetadataViews` | `0xee82856bf20e2aa6` | `0x0000000000000002` |
| `FlowToken` | `0x0ae53cb6e3f42a79` | `0x0000000000000003` |
| `FlowFees` | `0xe5a8b7f23e8b548f` | `0x0000000000000004` |
| `FlowStorageFees` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FlowServiceAccount` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `NodeVersionBeacon` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `RandomBeaconHistory` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `LockedTokens` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `StakingProxy` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FlowIDTableStaking` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FlowClusterQC` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FlowDKG` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FlowEpoch` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FlowStakingCollection` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |

See the other guides in this section of the docs for the import
addresses of other important contracts in the emulator.

## Upgrade Guide[​](#upgrade-guide "Direct link to Upgrade Guide")

The NFT guide covers a lot of common changes that are required for NFT contracts,
but many of these changes will also apply to any contract on Flow, so it is still
useful to read even if you don't have an NFT contract.

The core contracts do not have any meaningful changes outside of what is required
to be compatible with Cadence 1.0 and the token standard changes.
If you have questions about the core contracts changes for Cadence 1.0,
please reach out to the Flow team in Discord and we will be happy to help.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/cadence-migration-guide/core-contracts-guide.mdx)[PreviousFT Cadence 1.0 Guide](/docs/cadence-migration-guide/ft-guide)[NextDesign Patterns](/docs/design-patterns)
###### Rate this page

😞😐😊

* [Protocol Smart Contracts in Cadence 1.0](#protocol-smart-contracts-in-cadence-10)
* [Important Info](#important-info)
* [Upgrade Guide](#upgrade-guide)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

