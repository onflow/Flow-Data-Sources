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

Currently only the 64-bit wide (`Fix64`, `UFix64`), and 128-bit wide (`Fix128`, `UFix128`) types are available.
More fixed-point number types will be added in a future release.

Fixed-point numbers are useful for representing fractional values.
They have a fixed number of digits after a decimal point.

They are essentially integers which are scaled by a factor.
For example, the value 1.23 can be represented as 1230 with a scaling factor of 1/1000.
The scaling factor is the same for all values of the same type and stays the same during calculations.

Fixed-point numbers in Cadence have a scaling factor with a power of 10, instead of a power of 2 (i.e., they are decimal, not binary).

Signed fixed-point number types have the prefix `Fix`, have the following factors, and can represent values in the following ranges:

* **`Fix64`**: Factor 1e-8; `-92233720368.54775808` through `92233720368.54775807`
* **`Fix128`**: Factor 1e-24; `-170141183460469.231731687303715884105728` through `170141183460469.231731687303715884105727`

Unsigned fixed-point number types have the prefix `UFix`, have the following factors, and can represent values in the following ranges:

* **`UFix64`**: Factor 1e-8; `0.0` through `184467440737.09551615`
* **`UFix128`**: Factor 1e-24; `0.0` through `340282366920938.463463374607431768211455`

### Fixed-point type inference[​](#fixed-point-type-inference "Direct link to Fixed-point type inference")

An untyped positive fixed-point literal is assumed to be of type `UFix64`, whereas an untyped negative fixed-point
literal is assumed to be of type `Fix64`.

`` _10

var v1 = 1.23 // v1 would have the type `UFix64`

_10

_10

var v2 = -1.23 // v2 would have the type `Fix64` ``

Type annotations can be used to construct a fixed-point value belong to a specific type. e.g:

`` _10

var v1: Fix64 = 1.23 // v1 would have the type `Fix64`

_10

_10

var v2: Fix128 = -1.23 // v2 would have the type `Fix128` ``

### Fixed-point number functions[​](#fixed-point-number-functions "Direct link to Fixed-point number functions")

Fixed-Point numbers have multiple built-in functions you can use:

* `_10

  view fun toString(): String`

  Returns the string representation of the fixed-point number.

  `` _10

  // For `Fix64`

  _10

  let fix64: Fix64 = 1.23

  _10

  fix64.toString() // is "1.23000000"

  _10

  _10

  // For `Fix128`

  _10

  let fix128: Fix128 = 1.23

  _10

  fix128.toString() // is "1.230000000000000000000000" ``
* `_10

  view fun toBigEndianBytes(): [UInt8]`

  Returns the byte array representation (`[UInt8]`) in big-endian order of the fixed-point number.

  `` _10

  // For `Fix64`

  _10

  let fix64: Fix64 = 1.23

  _10

  fix64.toBigEndianBytes() // is `[0, 0, 0, 0, 7, 84, 212, 192]`

  _10

  _10

  // For `Fix128`

  _10

  let fix128: Fix128 = 1.23

  _10

  fix128.toBigEndianBytes() // is `[0, 0, 0, 0, 0, 1, 4, 118, 111, 0, 236, 179, 164, 192, 0, 0]` ``

All fixed-point types support the following functions:

* `_10

  view fun T.fromString(_ input: String): T?`

  Attempts to parse a fixed-point value from a base-10 encoded string, returning `nil` if the string is invalid.

  For a given fixed-point numeral `n` of type `T`, `T.fromString(n.toString())` is equivalent to wrapping `n` up in an `optional`.

  Strings are invalid if:

  + they contain non-digit characters.
  + they don't fit in the target type.
  + they're missing a decimal or fractional component. For example, both `0.` and `.1` are invalid strings, but `0.1` is accepted.

  For signed types like `Fix64` and `Fix128`, the string may optionally begin with a `+` or `-` sign prefix.

  For unsigned types like `UFix64` and `UFix128`, sign prefixes are not allowed.

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

  Attempts to parse an integer value from a byte array representation (`[UInt8]`) in big-endian order, returning `nil`
  if the input bytes are invalid.

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

## Number type casting[​](#number-type-casting "Direct link to Number type casting")

Casting between number types (e.g. `Int` to `UInt`, `Fix64` to `Int`) using the [casting operators](/docs/language/operators/casting-operators) (`as`, `as?` and `as!`) is not supported.

To convert between number types, the conversion functions ((e.g. `UInt(_)`)) must be used.
These conversion functions have the same name as the desired type.

`` _10

let value: UInt8 = 1

_10

_10

let intValue: Int? = value as? Int

_10

// intValue is `nil` and has type `Int?`

_10

_10

let validInt: Int = Int(value)

_10

// validInt is `1` and has type `Int` ``

When converting from a larger number type to a smaller one (narrowing), the conversion will succeed if the value can be
represented in the smaller type.
If it cannot an error will be thrown indicating overflow or underflow.
Converting to a larger number type will always succeed.

`` _10

let intValue: Int16 = 256

_10

_10

let uintValue: UInt8 = UInt8(intValue)

_10

// error: overflow, UInt8 has max value of `255`

_10

_10

let validUInt: UInt16 = UInt16(intValue)

_10

// validUInt is `256` and has type `UInt16`

_10

_10

let largerIntValue: Int = Int(intValue)

_10

// largerIntValue is `256` and has type `Int` ``

Converting from integer types to fixed point types and vice versa is supported by calling the conversion functions as well.
The same conditions as narrowing applies, an error will be thrown if the value cannot be represented in the range.

`` _10

let intValue: Int = -1

_10

_10

let fixValue: Fix64 = Fix64(intValue)

_10

// fixValue is `-1.00000000` and has type `Fix64`

_10

_10

let ufixValue: UFix64 = UFix64(intValue)

_10

// error: underflow, UFix64 has min value `0.0` ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/fixed-point-nums-ints.md)

[Previous

Booleans, Numeric Literals, and Integers](/docs/language/values-and-types/booleans-numlits-ints)[Next

Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers](/docs/language/values-and-types/min-max-saturation-floating-pt-nums)

###### Rate this page

😞😐😊

* [Fixed-point numbers](#fixed-point-numbers)
  + [Fixed-point type inference](#fixed-point-type-inference)
  + [Fixed-point number functions](#fixed-point-number-functions)
* [Number type casting](#number-type-casting)