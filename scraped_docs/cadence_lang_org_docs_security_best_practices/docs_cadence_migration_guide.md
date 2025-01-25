# Source: https://cadence-lang.org/docs/cadence-migration-guide/




Cadence 1.0 Migration Guide | Cadence




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


* Cadence 1.0 Migration Guide
On this page
# Cadence 1.0 Migration Guide

On September 4th, 2024 the Flow Mainnet upgraded to Cadence 1.0.

This migration guide offers developers guidance, actionable steps,
around updating projects to be compatible with Cadence 1.0.

The Cadence 1.0 release, introduced in the
[Crescendo](https://flow.com/upgrade/crescendo) network upgrade, is a breaking change.
Developers need to make sure all Cadence code used by their app (transactions and scripts)
to Cadence 1.0, to ensure it continues to work after the network upgrade.

Many of the improvements of Cadence 1.0 fundamentally change how Cadence works and is used.
This means it is necessary to break existing code to release this version,
which will guarantee stability going forward.

### Benefits of Cadence 1.0[​](#benefits-of-cadence-10 "Direct link to Benefits of Cadence 1.0")

Cadence 1.0 is the latest version of the Cadence smart contract programming language.
The stable release of Cadence 1.0 represents a significant milestone in the language’s maturity,
delivering a [comprehensive suite of new features and improvements](/docs/cadence-migration-guide/improvements)
that provide new possibilities, increase speed, security and efficiency.
With Cadence 1.0, developers gain access to over 20 new features and enhancements.
Each change is thoughtfully designed to streamline workflows, reduce duplication
and improve code readability, making writing and understanding smart contracts much easier.

### Upgrading NFT and FT Contracts[​](#upgrading-nft-and-ft-contracts "Direct link to Upgrading NFT and FT Contracts")

In addition to changes to the Cadence programming language,
the Cadence token standards were also streamlined and improved.
Existing Cadence scripts and transactions interacting with NFTs and FTs need to be updated.
If you do not update your code, your applications is non-functional.

* [Guide for NFT Standard v2](/docs/cadence-migration-guide/nft-guide)
* [Guide for FT Standard v2](/docs/cadence-migration-guide/ft-guide)
* [Cadence 1.0 Improvements & New Features](/docs/cadence-migration-guide/improvements)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/cadence-migration-guide/index.md)[PreviousGlossary](/docs/language/glossary)[NextImprovements & New Features](/docs/cadence-migration-guide/improvements)
###### Rate this page

😞😐😊

* [Benefits of Cadence 1.0](#benefits-of-cadence-10)
* [Upgrading NFT and FT Contracts](#upgrading-nft-and-ft-contracts)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

