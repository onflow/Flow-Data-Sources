# Source: https://cadence-lang.org/docs/language/environment-information

Environment Information | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Type Annotations](/docs/language/type-annotations)
  + [Values and Types](/docs/language/values-and-types)
  + [Operators](/docs/language/operators)
  + [Functions](/docs/language/functions)
  + [Control Flow](/docs/language/control-flow)
  + [Scope](/docs/language/scope)
  + [Type Safety](/docs/language/type-safety)
  + [Type Inference](/docs/language/type-inference)
  + [Composite Types](/docs/language/composite-types)
  + [Resources](/docs/language/resources)
  + [Access control](/docs/language/access-control)
  + [Capabilities](/docs/language/capabilities)
  + [Interfaces](/docs/language/interfaces)
  + [Enumerations](/docs/language/enumerations)
  + [Intersection Types](/docs/language/intersection-types)
  + [References](/docs/language/references)
  + [Imports](/docs/language/imports)
  + [Accounts](/docs/language/accounts/)
  + [Attachments](/docs/language/attachments)
  + [Contracts](/docs/language/contracts)
  + [Contract Updatability](/docs/language/contract-updatability)
  + [Transactions](/docs/language/transactions)
  + [Events](/docs/language/events)
  + [Core Events](/docs/language/core-events)
  + [Run-time Types](/docs/language/run-time-types)
  + [Built-in Functions](/docs/language/built-in-functions)
  + [Environment Information](/docs/language/environment-information)
  + [Crypto](/docs/language/crypto)
  + [Type Hierarchy](/docs/language/type-hierarchy)
  + [Glossary](/docs/language/glossary)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Language Reference](/docs/language/)
* Environment Information

On this page

# Environment Information

## Transaction Information[​](#transaction-information "Direct link to Transaction Information")

To get the addresses of the signers of a transaction,
use the `address` field of each signing `Account`
that is passed to the transaction's `prepare` phase.

There is currently no API that allows getting other transaction information.
Please let us know if your use-case demands it by request this feature in an issue.

## Block Information[​](#block-information "Direct link to Block Information")

To get information about a block, the functions `getCurrentBlock` and `getBlock` can be used:

* `_10

  view fun getCurrentBlock(): Block`

  Returns the current block, i.e. the block which contains the currently executed transaction.
* `_10

  view fun getBlock(at: UInt64): Block?`

  Returns the block at the given height.
  If the block exists within the accessible range defined by `flow.DefaultTransactionExpiry - 10` (`590` blocks), it is returned successfully.
  If the block at the given height does not exist or is outside the default transaction expiration range of `590` blocks below the current sealed block, the function returns `nil`.

The `Block` type contains the identifier, height, and timestamp:

`_35

access(all)

_35

struct Block {

_35

/// The ID of the block.

_35

///

_35

/// It is essentially the hash of the block.

_35

///

_35

access(all)

_35

let id: [UInt8; 32]

_35

_35

/// The height of the block.

_35

///

_35

/// If the blockchain is viewed as a tree with the genesis block at the root,

_35

// the height of a node is the number of edges between the node and the genesis block

_35

///

_35

access(all)

_35

let height: UInt64

_35

_35

/// The view of the block.

_35

///

_35

/// It is a detail of the consensus algorithm. It is a monotonically increasing integer

_35

/// and counts rounds in the consensus algorithm. It is reset to zero at each spork.

_35

///

_35

access(all)

_35

let view: UInt64

_35

_35

/// The timestamp of the block.

_35

///

_35

/// Unix timestamp of when the proposer claims it constructed the block.

_35

///

_35

/// NOTE: It is included by the proposer, there are no guarantees on how much the time stamp can deviate from the true time the block was published.

_35

/// Consider observing blocks’ status changes off-chain yourself to get a more reliable value.

_35

///

_35

access(all)

_35

let timestamp: UFix64

_35

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/environment-information.md)

[Previous

Built-in Functions](/docs/language/built-in-functions)[Next

Crypto](/docs/language/crypto)

###### Rate this page

😞😐😊

* [Transaction Information](#transaction-information)
* [Block Information](#block-information)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.