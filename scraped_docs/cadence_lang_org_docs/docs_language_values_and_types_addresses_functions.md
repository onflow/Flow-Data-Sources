# Source: https://cadence-lang.org/docs/language/values-and-types/addresses-functions

Addresses and Address Functions | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Values and Types](/docs/language/values-and-types/)

    - [Booleans, Numeric Literals, and Integers](/docs/language/values-and-types/booleans-numlits-ints)
    - [Fixed-Point Numbers and Functions](/docs/language/values-and-types/fixed-point-nums-ints)
    - [Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers](/docs/language/values-and-types/min-max-saturation-floating-pt-nums)
    - [Addresses and Address Functions](/docs/language/values-and-types/addresses-functions)
    - [AnyStruct, AnyResource, Optionals, and Never](/docs/language/values-and-types/anystruct-anyresource-opts-never)
    - [Strings and Characters](/docs/language/values-and-types/strings-and-characters)
    - [Arrays](/docs/language/values-and-types/arrays)
    - [Dictionaries](/docs/language/values-and-types/dictionaries)
    - [InclusiveRange](/docs/language/values-and-types/inclusive-range)
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
  + [Glossary](/docs/language/glossary)
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
* [Values and Types](/docs/language/values-and-types/)
* Addresses and Address Functions

On this page

# Addresses and Address Functions

## Addresses[​](#addresses "Direct link to Addresses")

The type `Address` represents an address. Addresses are unsigned integers with a size of 64 bits (8 bytes). Hexadecimal integer literals can be used to create address values:

`` _13

// Declare a constant that has type `Address`.

_13

//

_13

let someAddress: Address = 0x436164656E636521

_13

_13

// Invalid: Initial value is not compatible with type `Address`,

_13

// it is not a number.

_13

//

_13

let notAnAddress: Address = ""

_13

_13

// Invalid: Initial value is not compatible with type `Address`.

_13

// The integer literal is valid, however, it is larger than 64 bits.

_13

//

_13

let alsoNotAnAddress: Address = 0x436164656E63652146757265766572 ``

Integer literals are not inferred to be an address:

`` _10

// Declare a number. Even though it happens to be a valid address,

_10

// it is not inferred as it.

_10

//

_10

let aNumber = 0x436164656E636521

_10

_10

// `aNumber` has type `Int` ``

An `Address` can also be created using a byte array or string.

`` _17

// Declare an address with hex representation as 0x436164656E636521.

_17

let someAddress: Address = Address.fromBytes([67, 97, 100, 101, 110, 99, 101, 33])

_17

_17

// Invalid: Provided value is not compatible with type `Address`. The function panics.

_17

let invalidAddress: Address = Address.fromBytes([12, 34, 56, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111])

_17

_17

// Declare an address with the string representation as "0x436164656E636521".

_17

let addressFromString: Address? = Address.fromString("0x436164656E636521")

_17

_17

// Invalid: Provided value does not have the "0x" prefix. Returns Nil

_17

let addressFromStringWithoutPrefix: Address? = Address.fromString("436164656E636521")

_17

_17

// Invalid: Provided value is an invalid hex string. Return Nil.

_17

let invalidAddressForInvalidHex: Address? = Address.fromString("0xZZZ")

_17

_17

// Invalid: Provided value is larger than 64 bits. Return Nil.

_17

let invalidAddressForOverflow: Address? = Address.fromString("0x436164656E63652146757265766572") ``

### Address functions[​](#address-functions "Direct link to Address functions")

Addresses have multiple built-in functions you can use.

* `_10

  view fun toString(): String`

  Returns the string representation of the address. The result has a `0x` prefix and is zero-padded.

  `_10

  let someAddress: Address = 0x436164656E636521

  _10

  someAddress.toString() // is "0x436164656E636521"

  _10

  _10

  let shortAddress: Address = 0x1

  _10

  shortAddress.toString() // is "0x0000000000000001"`
* `_10

  view fun toBytes(): [UInt8]`

  Returns the byte array representation (`[UInt8]`) of the address.

  `` _10

  let someAddress: Address = 0x436164656E636521

  _10

  _10

  someAddress.toBytes() // is `[67, 97, 100, 101, 110, 99, 101, 33]` ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/addresses-functions.md)

[Previous

Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers](/docs/language/values-and-types/min-max-saturation-floating-pt-nums)[Next

AnyStruct, AnyResource, Optionals, and Never](/docs/language/values-and-types/anystruct-anyresource-opts-never)

###### Rate this page

😞😐😊

* [Addresses](#addresses)
  + [Address functions](#address-functions)