# Source: https://cadence-lang.org/docs/language/built-in-functions




Built-in Functions | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Built-in Functions
On this page
# Built-in Functions

## `panic`[​](#panic "Direct link to panic")

# 

 `_10view fun panic(_ message: String): Never`

Terminates the program unconditionally
and reports a message which explains why the unrecoverable error occurred.

 `_10panic("something went wrong: ...")`
## `assert`[​](#assert "Direct link to assert")

 `_10view fun assert(_ condition: Bool, message: String)`

Terminates the program if the given condition is false,
and reports a message which explains how the condition is false.
Use this function for internal sanity checks.

The message argument is optional.

## `revertibleRandom`[​](#revertiblerandom "Direct link to revertiblerandom")

 `_10view fun revertibleRandom<T: FixedSizeUnsignedInteger>(modulo: T): T`

Returns a pseudo-random integer.

`T` can be any fixed-size unsigned integer type (`FixedSizeUnsignedInteger`, i.e.
(`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`,
`Word8`, `Word16`, `Word32`, `Word64`, `Word128`, `Word256`).

The modulo argument is optional.
If provided, the returned integer is between `0` and `modulo -1`.
If not provided, the returned integer is between `0` and the maximum value of `T`.
The function errors if `modulo` is equal to 0.

The sequence of returned random numbers is independent for
every transaction in each block.
Under the hood, Cadence instantiates a cryptographically-secure pseudo-random number
generator (CSPRG) for each transaction independently, where the seeds of any two transactions
are different with near certainty.

The random numbers returned are unpredictable
(unpredictable for miners at block construction time,
and unpredictable for cadence logic at time of call),
verifiable, as well as unbiasable by miners and previously-running Cadence code.
See [Secure random number generator for Flow’s smart contracts](https://forum.flow.com/t/secure-random-number-generator-for-flow-s-smart-contracts/5110)
and [FLIP120](https://github.com/onflow/flips/pull/120) for more details.

Nevertheless, developers need to be mindful to use `revertibleRandom()` correctly:

warning

A transaction can atomically revert all its action.
It is possible for a transaction submitted by an untrusted party
to post-select favorable results and revert the transaction for unfavorable results.

The function usage remains safe when called by a trusted party that does not
perform post-selection on the returned random numbers.

This limitation is inherent to any smart contract platform that allows transactions to roll back atomically
and cannot be solved through safe randomness alone.
In cases where a non-trusted party can interact through their own transactions
with smart contracts generating random numbers,
it is recommended to use [commit-reveal schemes](https://github.com/onflow/flips/pull/123)
as outlined in this [tentative example](https://github.com/onflow/flips/blob/main/protocol/20230728-commit-reveal.md#tutorials-and-examples) (full tutorial coming soon).

## `RLP`[​](#rlp "Direct link to rlp")

Recursive Length Prefix (RLP) serialization allows the encoding of arbitrarily nested arrays of binary data.

Cadence provides RLP decoding functions in the built-in `RLP` contract, which does not need to be imported.

### `decodeString`[​](#decodestring "Direct link to decodestring")

 `_10view fun decodeString(_ input: [UInt8]): [UInt8]`

Decodes an RLP-encoded byte array. RLP calls this a "string."
The byte array should only contain of a single encoded value for a string.
If the encoded value type does not match, or it has trailing unnecessary bytes, the program aborts.
If the function encounters any error while decoding, the program aborts.

### `decodeList`[​](#decodelist "Direct link to decodelist")

 `_10view fun decodeList(_ input: [UInt8]): [[UInt8]]``

Decodes an RLP-encoded list into an array of RLP-encoded items.

Note that this function does not recursively decode, so each element of the resulting array is RLP-encoded data.
The byte array should only contain of a single encoded value for a list.
If the encoded value type does not match, or it has trailing unnecessary bytes, the program aborts.
If the function encounters any error while decoding, the program aborts.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/built-in-functions.mdx)[PreviousRun-time Types](/docs/language/run-time-types)[NextEnvironment Information](/docs/language/environment-information)
###### Rate this page

😞😐😊

* [`panic`](#panic)
* [`assert`](#assert)
* [`revertibleRandom`](#revertiblerandom)
* [`RLP`](#rlp)
  + [`decodeString`](#decodestring)
  + [`decodeList`](#decodelist)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

