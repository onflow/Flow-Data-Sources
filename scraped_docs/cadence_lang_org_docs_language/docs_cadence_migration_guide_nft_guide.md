# Source: https://cadence-lang.org/docs/cadence-migration-guide/nft-guide




Non-Fungible Token Cadence 1.0 Migration Guide | Cadence




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
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* NFT Cadence 1.0 Guide
On this page
# Non-Fungible Tokens in Cadence 1.0

On September 4th, 2024 the Flow Mainnet upgraded to Cadence 1.0.
In addition to many changes to the Cadence programming language,
the Cadence token standards were also streamlined and improved.
All applications' scripts and transactions need to be updated.
If you do not update your code, your applications do not function properly.

This document describes the changes to the Cadence Non-Fungible Token (NFT) standard and
gives a step-by-step guide for how to upgrade your NFT contract from Cadence 0.42
to Cadence 1.0.

We'll be using the
[`ExampleNFT` contract](https://github.com/onflow/flow-nft/blob/master/contracts/ExampleNFT.cdc)
as an example. Many projects have used `ExampleNFT` as a starting point for their projects,
so it is widely applicable to most NFT developers on Flow.
The upgrades required for `ExampleNFT` will cover 90%+ of what you'll
need to do to update your contract. Each project most likely has
additional logic or features that aren't included in `ExampleNFT`,
but hopefully after reading this guide, you'll understand Cadence 1.0
well enough that you can easily make any other changes that are necessary.

Additionally, most of the changes described here also apply to anyone
who is updating a Fungible Token contract or interacting with one,
so keep that in mind while reading if that applies to you.

As always, there are plenty of people on the Flow team and in the community
who are happy to help answer any questions you may have, so please reach out
in Discord if you need any help.

# Important Info

Please read [the FLIP](https://github.com/onflow/flips/pull/56)
that describes the changes to the `NonFungibleToken` standard first.

The updated code for the V2 Non-Fungible Token standard is located in the
[`master` branch of the flow-nft repo](https://github.com/onflow/flow-nft).
Please look at [the PR that made the changes](https://github.com/onflow/flow-nft/pull/126)
to understand how the standard and examples have changed.
Note the changes to the `NonFungibleToken`, `MetadataViews`, `ViewResolver`,
and `NFTForwarding` contracts.

Additionally, here are the import addresses
for all of the important contracts related to non-fungible tokens.
The second column is the import address if you are testing with a basic version of the emulator.
The third column contains the import addresses if you are using the Cadence testing framework.

| Contract | Emulator Import Address | Testing Framework |
| --- | --- | --- |
| `NonFungibleToken` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FungibleToken` | `0xee82856bf20e2aa6` | `0x0000000000000002` |
| `ViewResolver` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `Burner` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `MetadataViews` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |

See the other guides in this section of the docs for the import
addresses of other important contracts in the emulator.

As for contracts that are important for NFT developers but aren't "core contracts",
here is information about where to find the Cadence 1.0 Versions of Each:

**NFT Catalog:** The NFT Catalog has been deprecated for Cadence 1.0. Now that the token standards require implementing metadata views, NFT Catalog is not needed in its current form. The Flow team now maintains [TokenList](https://token-list.fixes.world/?utm_source=Flowverse&utm_medium=Website&utm_campaign=Dapp) which is similar to NFT Catalog, but is decentralized. Projects can register there without needing to be approved.

**NFT Storefront:**
See [the `master` branch in the NFT Storefront Repo](https://github.com/onflow/nft-storefront/tree/master/contracts)
for the updated versions of the `NFTStorefront` and `NFTStorefrontV2` contracts.

**USDC:** USDC was migrated to standard bridged USDC on Flow. See the [repo](https://github.com/onflow/bridged-usdc) for the latest version of the USDC contract.

**Account Linking and Hybrid Custody:**
See [the `main` branch in the hybrid custody repo](https://github.com/onflow/hybrid-custody)
for updated hybrid custody contracts.

[This Discord announcement](https://discord.com/channels/613813861610684416/811693600403357706/1225909248429527140)
also contains versions of a lot of important contracts.

Use the [Flow Contract Browser](https://contractbrowser.com/) to find the 1.0 code of other contracts.

## A note for newcomers[​](#a-note-for-newcomers "Direct link to A note for newcomers")

This guide is primarily for developers who have existing contracts
deployed to Flow mainnet that they need to update for Cadence 1.0.
If you don't have any contracts deployed yet, it is recommended that
you start an NFT contract from scratch by either copying the `ExampleNFT` contract
from the `master` branch of the `flow-nft` repo.

Additionally, the Flow community is working on
the [`BasicNFT` contract](https://github.com/onflow/flow-nft/blob/universal-collection/contracts/BasicNFT.cdc)
in the `universal-collection` branch of the flow-nft GitHub repo.
This is a simplified version of standard NFT contracts, but has not been completed yet.

## BasicNFT and UniversalCollection[​](#basicnft-and-universalcollection "Direct link to BasicNFT and UniversalCollection")

As part of the improvements to the NFT standard, there is now a new NFT contract
example in the `flow-nft` GitHub repo: [`BasicNFT`](https://github.com/onflow/flow-nft/blob/universal-collection/contracts/BasicNFT.cdc).

`BasicNFT` defines a Cadence NFT in as few lines of code as possible, 137 at the moment!
This is possible because the contract basically only defines the NFT resource,
the essential metadata views, and a minter resource.
It doesn't have to define a collection! Most collection resources are 99% boilerplate
code, so it really doesn't make sense for most projects to have to define their own
collection.

Instead, `BasicNFT` uses [`UniversalCollection`](https://github.com/onflow/flow-nft/blob/universal-collection/contracts/UniversalCollection.cdc),
a contract that defines a collection resource
that has all of the standard functionality that a collection needs and nothing else.
From now on, any project that doesn't want to do anything unique with their collection
can just import `UniversalCollection` and call it from their `createEmptyCollection`
function:

 `_10access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {_10 return <- UniversalCollection.createEmptyCollection(identifier: "flowBasicNFTCollection", type: Type<@BasicNFT.NFT>())_10}`

All they have to provide is a type and an identifier for the collection.
`UniversalCollection.Collection` will enforce that only NFTs of the given type
can be accepted by the collection:

 `_10access(all) fun deposit(token: @{NonFungibleToken.NFT}) {_10 if self.supportedType != token.getType() {_10 panic("Cannot deposit an NFT of the given type")_10 }`

It also constructs standard paths based on the identifier provided.

`UniversalCollection` will be deployed to all the networks soon after the Cadence 1.0 upgrade,
so developers will be able to import from it after that point.

We'll be putting out more information and guides for `BasicNFT` and `UniversalCollection`
in the near future, but keep it in mind if you are thinking about deploying
any new NFT contracts in the future!

# Migration Guide

This guide will cover changes that are required because of upgrades to
the Cadence Language as well as the token standard.
The improvements will be described here as they apply to specific changes
that projects need to make in order to be ready for the upgrade,
but it is good to read all sources to fully understand the changes.

Please read the motivation section of [the NFT-V2 FLIP](https://github.com/onflow/flips/pull/56)
to learn about why most of the changes to the standard were needed or desired.

First, we will cover the changes that come from the new token standards and then
we will cover the changes that come from Cadence.

## Token Standard Changes[​](#token-standard-changes "Direct link to Token Standard Changes")

### NonFungibleToken.NFT[​](#nonfungibletokennft "Direct link to NonFungibleToken.NFT")

`NonFungibleToken.NFT` used to be a nested type specification, but now it is an interface!

In your code, any instance that refers
to `@NonFungibleToken.NFT` or `&NonFungibleToken.NFT` need to be updated to
`@{NonFungibleToken.NFT}` or `&{NonFungibleToken.NFT}` respectively.

### NonFungibleToken.Collection[​](#nonfungibletokencollection "Direct link to NonFungibleToken.Collection")

Similar to `NFT`, `NonFungibleToken.Collection` is now an interface.

Since `Collection` is an interface, you will need to update every instance in your code
that refers to `@NonFungibleToken.Collection` or `&NonFungibleToken.Collection` to
`@{NonFungibleToken.Collection}` or `&{NonFungibleToken.Collection}` respectively to show
that it is now an interface specification instead of a concrete type specification.

## Conclusion[​](#conclusion "Direct link to Conclusion")

This guide covered the most important changes that are required for the Cadence 1.0
upgrades to NFT contracts. Please ask any questions about the migrations
in the #developer-questions channel in discord and good luck with your upgrades!

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/cadence-migration-guide/nft-guide.mdx)[PreviousImprovements & New Features](/docs/cadence-migration-guide/improvements)[NextFT Cadence 1.0 Guide](/docs/cadence-migration-guide/ft-guide)
###### Rate this page

😞😐😊

* [A note for newcomers](#a-note-for-newcomers)
* [BasicNFT and UniversalCollection](#basicnft-and-universalcollection)
* [Token Standard Changes](#token-standard-changes)
  + [NonFungibleToken.NFT](#nonfungibletokennft)
  + [NonFungibleToken.Collection](#nonfungibletokencollection)
* [Conclusion](#conclusion)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

