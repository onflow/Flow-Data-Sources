# Source: https://cadence-lang.org/docs/cadence-migration-guide/ft-guide




Fungible Token Cadence 1.0 Migration Guide | Cadence




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
* FT Cadence 1.0 Guide
On this page
# Fungible Tokens in Cadence 1.0

On September 4th, 2024 the Flow Mainnet upgraded to Cadence 1.0.
In addition to many changes to the Cadence programming language,
the Cadence token standards also got streamlined and improved.
All applications need to migrate their existing Cadence scripts and transactions for the update.
If you do not update your code, your application will not function.

This document describes the changes to the Cadence Fungible Token (FT) standard.
We'll be using the
[`ExampleToken` contract](https://github.com/onflow/flow-ft/blob/master/contracts/ExampleToken.cdc)
as an example. Many projects have used `ExampleToken` as a starting point for their projects,
so it is widely applicable to most NFT developers on Flow.
The upgrades required for `ExampleToken` will cover 90%+ of what you'll
need to do to update your contract. Each project most likely has
additional logic or features that aren't included in `ExampleToken`,
but hopefully after reading this guide, you'll understand Cadence 1.0
well enough that you can easily make any other changes that are necessary.

As always, there are plenty of people on the Flow team and in the community
who are happy to help answer any questions you may have, so please reach out
in Discord if you need any help.

# Important Info

Please read [the FLIP](https://github.com/onflow/flips/pull/55)
that describes the changes to the `FungibleToken` standard first.

The updated code for the V2 Fungible Token standard is located in the
[`master` branch of the flow-ft repo](https://github.com/onflow/flow-ft).
Please look at the [PR that made the changes](https://github.com/onflow/flow-ft/pull/131)
to understand how the standard and examples have changed.
Note the changes to the `FungibleTokenMetadataViews`,
`Burner`, `FungibleTokenSwitchboard`, and `TokenForwarding` contracts.

Additionally, here are the import addresses
for all of the important contracts related to fungible tokens.
The second column is the import address if you are testing with a basic version of the emulator.
The third column contains the import addresses if you are using the Cadence testing framework.

| Contract | Emulator Import Address | Testing Framework |
| --- | --- | --- |
| `FungibleToken` | `0xee82856bf20e2aa6` | `0x0000000000000002` |
| `ViewResolver` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `Burner` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `MetadataViews` | `0xf8d6e0586b0a20c7` | `0x0000000000000001` |
| `FungibleTokenMetadataViews` | `0xee82856bf20e2aa6` | `0x0000000000000002` |
| `FungibleTokenSwitchboard` | `0xee82856bf20e2aa6` | `0x0000000000000002` |

See the other guides in this section of the docs for the import
addresses of other important contracts in the emulator.

As for contracts that are important for NFT developers but aren't "core contracts",
here is information about where to find the Cadence 1.0 versions of each:

**USDC:** USDC was migrated to standard bridged USDC on Flow. See the [repo](https://github.com/onflow/bridged-usdc) for the latest version of the USDC contract.

**Account Linking and Hybrid Custody:**
See [this PR in the hybrid custody repo](https://github.com/onflow/hybrid-custody/pull/164)
for updated hybrid custody contracts.

[This Discord announcement](https://discord.com/channels/613813861610684416/811693600403357706/1225909248429527140)
also contains versions of a lot of important contracts.

Use the [Flow Contract Browser](https://contractbrowser.com/) to find the 1.0 code of other contracts.

# Migration Guide

Please see the [NFT Cadence 1.0 migration guide](/docs/cadence-migration-guide/nft-guide).
While the contracts aren't exactly the same, they share a huge amount of functionality,
and the changes described in that guide will cover 90% of the changes
that are needed for fungible tokens, so if you just follow those instructions
for your fungible token contract, you'll be most of the way there.

Here, we will only describe the changes that are specific to the fungible token standard.

## `Vault` implements `FungibleToken.Vault`[​](#vault-implements-fungibletokenvault "Direct link to vault-implements-fungibletokenvault")

`FungibleToken.Vault` is no longer a resource type specification.
It is now an interface that inherits from `Provider`, `Receiver`, `Balance`,
`ViewResolver.Resolver`, and `Burner.Burnable`.

Since `Vault` is an interface, you will need to update every instance in your code
that refers to `@FungibleToken.Vault` or `&FungibleToken.Vault` to
`@{FungibleToken.Vault}` or `&{FungibleToken.Vault}` respectively to show
that it is now an interface specification instead of a concrete type specification.
Example in `deposit()`:

 `_10/// deposit now accepts a resource that implements the `FungibleToken.Vault` interface type_10access(all) fun deposit(from: @{FungibleToken.Vault})`

If you have any more questions, please ask in discord and the Flow team will be happy to assist!

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/cadence-migration-guide/ft-guide.mdx)[PreviousNFT Cadence 1.0 Guide](/docs/cadence-migration-guide/nft-guide)[NextCore Contracts Guide](/docs/cadence-migration-guide/core-contracts-guide)
###### Rate this page

😞😐😊

* [`Vault` implements `FungibleToken.Vault`](#vault-implements-fungibletokenvault)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

