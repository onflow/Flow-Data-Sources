# Source: https://cadence-lang.org/docs/language/values-and-types/fixed-point-nums-ints

Fixed-Point Numbers and Functions | Cadence



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
* Fixed-Point Numbers and Functions

On this page

# Fixed-Point Numbers and Functions

## Fixed-point numbers[​](#fixed-point-numbers "Direct link to Fixed-point numbers")

🚧 Status

Currently only the 64-bit wide `Fix64` and `UFix64` types are available. More fixed-point number types will be added in a future release.

Fixed-point numbers are useful for representing fractional values. They have a fixed number of digits after a decimal point.

They are essentially integers which are scaled by a factor. For example, the value 1.23 can be represented as 1230 with a scaling factor of 1/1000. The scaling factor is the same for all values of the same type and stays the same during calculations.

Fixed-point numbers in Cadence have a scaling factor with a power of 10, instead of a power of 2 (i.e., they are decimal, not binary).

Signed fixed-point number types have the prefix `Fix`, have the following factors, and can represent values in the following ranges:

* **`Fix64`**: Factor 1/100,000,000; -92233720368.54775808 through 92233720368.54775807

Unsigned fixed-point number types have the prefix `UFix`, have the following factors, and can represent values in the following ranges:

* **`UFix64`**: Factor 1/100,000,000; 0.0 through 184467440737.09551615

### Fixed-point number functions[​](#fixed-point-number-functions "Direct link to Fixed-point number functions")

Fixed-Point numbers have multiple built-in functions you can use:

* `_10

  view fun toString(): String`

  Returns the string representation of the fixed-point number.

  `_10

  let fix = 1.23

  _10

  _10

  fix.toString() // is "1.23000000"`
* `_10

  view fun toBigEndianBytes(): [UInt8]`

  Returns the byte array representation (`[UInt8]`) in big-endian order of the fixed-point number.

  `` _10

  let fix = 1.23

  _10

  _10

  fix.toBigEndianBytes() // is `[0, 0, 0, 0, 7, 84, 212, 192]` ``

All fixed-point types support the following functions:

* `_10

  view fun T.fromString(_ input: String): T?`

  Attempts to parse a fixed-point value from a base-10 encoded string, returning `nil` if the string is invalid.

  For a given fixed-point numeral `n` of type `T`, `T.fromString(n.toString())` is equivalent to wrapping `n` up in an `optional`.

  Strings are invalid if:

  + they contain non-digit characters.
  + they don't fit in the target type.
  + they're missing a decimal or fractional component. For example, both `0.` and `.1` are invalid strings, but `0.1` is accepted.

  For signed types like `Fix64`, the string may optionally begin with a `+` or `-` sign prefix.

  For unsigned types like `UFix64`, sign prefices are not allowed.

  Examples:

  `_11

  let nil1: UFix64? = UFix64.fromString("0.") // nil, fractional part is required

  _11

  _11

  let nil2: UFix64? = UFix64.fromString(".1") // nil, decimal part is required

  _11

  _11

  let smol: UFix64? = UFix64.fromString("0.1") // ok

  _11

  _11

  let smolString: String = "-0.1"

  _11

  _11

  let nil3: UFix64? = UFix64.fromString(smolString) // nil, unsigned types don't allow a sign prefix

  _11

  _11

  let smolFix64: Fix64? = Fix64.fromString(smolString) // ok`
* `_10

  view fun T.fromBigEndianBytes(_ bytes: [UInt8]): T?`

  Attempts to parse an integer value from a byte array representation (`[UInt8]`) in big-endian order, returning `nil` if the input bytes are invalid.

  For a given integer `n` of type `T`, `T.fromBigEndianBytes(n.toBigEndianBytes())` is equivalent to wrapping `n` up in an [optional](/docs/language/values-and-types/anystruct-anyresource-opts-never#optionals).

  The bytes are invalid if:

  + the length of the bytes array exceeds the number of bytes needed for the target type.
  + they don't fit in the target type.

  Examples:

  `_10

  let fortyTwo: UFix64? = UFix64.fromBigEndianBytes([0, 0, 0, 0, 250, 86, 234, 0]) // ok, 42.0

  _10

  _10

  let nilWord: UFix64? = UFix64.fromBigEndianBytes("[100, 22, 0, 0, 0, 0, 0, 0, 0]") // nil, out of bounds

  _10

  _10

  let nilWord2: Fix64? = Fix64.fromBigEndianBytes("[0, 22, 0, 0, 0, 0, 0, 0, 0]") // // nil, size (9) exceeds number of bytes needed for Fix64 (8)

  _10

  _10

  let negativeNumber: Fix64? = Fix64.fromBigEndianBytes([255, 255, 255, 255, 250, 10, 31, 0]) // ok, -1`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/fixed-point-nums-ints.md)

[Previous

Booleans, Numeric Literals, and Integers](/docs/language/values-and-types/booleans-numlits-ints)[Next

Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers](/docs/language/values-and-types/min-max-saturation-floating-pt-nums)

###### Rate this page

😞😐😊

* [Fixed-point numbers](#fixed-point-numbers)
  + [Fixed-point number functions](#fixed-point-number-functions)