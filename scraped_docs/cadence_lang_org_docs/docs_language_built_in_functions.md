# Source: https://cadence-lang.org/docs/language/built-in-functions

Built-in Functions | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax and Glossary](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Values and Types](/docs/language/values-and-types/)
  + [Types and Type System](/docs/language/types-and-type-system/)
  + [Operators](/docs/language/operators/)
  + [Accounts](/docs/language/accounts/)
  + [Functions](/docs/language/functions)
  + [Pre- and Post-Conditions](/docs/language/pre-and-post-conditions)
  + [Built-in Functions](/docs/language/built-in-functions)
  + [Control Flow](/docs/language/control-flow)
  + [Scope](/docs/language/scope)
  + [Resources](/docs/language/resources)
  + [Access Control](/docs/language/access-control)
  + [Capabilities](/docs/language/capabilities)
  + [Interfaces](/docs/language/interfaces)
  + [Enumerations](/docs/language/enumerations)
  + [References](/docs/language/references)
  + [Imports](/docs/language/imports)
  + [Attachments](/docs/language/attachments)
  + [Contracts](/docs/language/contracts)
  + [Contract Updatability](/docs/language/contract-updatability)
  + [Transactions](/docs/language/transactions)
  + [Events](/docs/language/events)
  + [Core Events](/docs/language/core-events)
  + [Environment Information](/docs/language/environment-information)
  + [Crypto](/docs/language/crypto)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Language Reference](/docs/language/)
* Built-in Functions

On this page

# Built-in Functions

The following describes Cadence's built in functions. Examples are also provided.

## `panic`[​](#panic "Direct link to panic")

`_10

view fun panic(_ message: String): Never`

Terminates the program unconditionally and reports a message, which explains why the unrecoverable error occurred.

`_10

panic("something went wrong: ...")`

## `assert`[​](#assert "Direct link to assert")

`_10

view fun assert(_ condition: Bool, message: String)`

Terminates the program if the given condition is false, and reports a message that explains how the condition is false. Use this function for internal sanity checks.

The message argument is optional.

## `revertibleRandom`[​](#revertiblerandom "Direct link to revertiblerandom")

`_10

view fun revertibleRandom<T: FixedSizeUnsignedInteger>(modulo: T): T`

Returns a pseudo-random integer.

`T` can be any fixed-size unsigned integer type (`FixedSizeUnsignedInteger`, i.e., `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `Word8`, `Word16`, `Word32`, `Word64`, `Word128`, or `Word256`).

The modulo argument is optional. If provided, the returned integer is between `0` and `modulo -1`. If not provided, the returned integer is between `0` and the maximum value of `T`. The function errors if `modulo` is equal to 0.

The sequence of returned random numbers is independent for every transaction in each block. Under the hood, Cadence instantiates a cryptographically-secure pseudo-random number generator (CSPRG) for each transaction independently, where the seeds of any two transactions are different with near certainty.

The random numbers returned are unpredictable (unpredictable for miners at block construction time, and unpredictable for cadence logic at time of call), verifiable, as well as *unbiasable* by miners and previously-running Cadence code. See [Secure random number generator for Flow’s smart contracts](https://forum.flow.com/t/secure-random-number-generator-for-flow-s-smart-contracts/5110) and [FLIP120](https://github.com/onflow/flips/pull/120) for more details.

Nevertheless, developers need to be mindful to use `revertibleRandom()` correctly.

danger

A transaction can atomically revert all of its action. This means that if you're letting users submit transactions, as opposed to you submitting them on your backend with a wallet you control, those users can submit the transaction in such a way that it reverts if the user doesn't like the outcome.

The function usage remains safe when called by a trusted party that does not perform post-selection on the returned random numbers.

This limitation is inherent to any smart contract platform that allows transactions to roll back atomically and cannot be solved through safe randomness alone. In cases where a non-trusted party can interact through their own transactions with smart contracts generating random numbers, it is recommended to use [commit-reveal schemes](https://developers.flow.com/tutorials/native-vrf/commit-reveal-cadence).

## `RLP`[​](#rlp "Direct link to rlp")

Recursive Length Prefix (RLP) serialization allows the encoding of arbitrarily nested arrays of binary data.

Cadence provides RLP decoding functions in the built-in `RLP` contract, which does not need to be imported.

### `decodeString`[​](#decodestring "Direct link to decodestring")

`_10

view fun decodeString(_ input: [UInt8]): [UInt8]`

Decodes an RLP-encoded byte array. RLP calls this a *string*. The byte array should only contain a single encoded value for a string.

* If the encoded value type does not match or if it has trailing unnecessary bytes, the program aborts.
* If the function encounters any error while decoding, the program aborts.

### `decodeList`[​](#decodelist "Direct link to decodelist")

`` _10

view fun decodeList(_ input: [UInt8]): [[UInt8]]` ``

Decodes an RLP-encoded list into an array of RLP-encoded items.

Note that this function does not recursively decode, so each element of the resulting array is RLP-encoded data. The byte array should only contain a single encoded value for a list.

* If the encoded value type does not match or if it has trailing unnecessary bytes, the program aborts.
* If the function encounters any error while decoding, the program aborts.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/built-in-functions.mdx)

[Previous

Pre- and Post-Conditions](/docs/language/pre-and-post-conditions)[Next

Control Flow](/docs/language/control-flow)

###### Rate this page

😞😐😊

* [`panic`](#panic)
* [`assert`](#assert)
* [`revertibleRandom`](#revertiblerandom)
* [`RLP`](#rlp)
  + [`decodeString`](#decodestring)
  + [`decodeList`](#decodelist)