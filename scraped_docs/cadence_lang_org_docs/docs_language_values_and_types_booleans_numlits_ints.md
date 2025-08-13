# Source: https://cadence-lang.org/docs/language/values-and-types/booleans-numlits-ints

Booleans, Numeric Literals, and Integers | Cadence



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
* Booleans, Numeric Literals, and Integers

On this page

# Booleans, Numeric Literals, and Integers

## Booleans[​](#booleans "Direct link to Booleans")

The two boolean values `true` and `false` have the type `Bool`.

## Numeric literals[​](#numeric-literals "Direct link to Numeric literals")

Numbers can be written in various bases. Numbers are assumed to be decimal by default. Non-decimal literals have a specific prefix:

| Numeral system | Prefix | Characters |
| --- | --- | --- |
| **Decimal** | *None* | one or more numbers (`0` to `9`) |
| **Binary** | `0b` | one or more zeros or ones (`0` or `1`) |
| **Octal** | `0o` | one or more numbers in the range `0` to `7` |
| **Hexadecimal** | `0x` | one or more numbers, or characters `a` to `f`, lowercase or uppercase |

`` _25

// A decimal number

_25

//

_25

1234567890 // is `1234567890`

_25

_25

// A binary number

_25

//

_25

0b101010 // is `42`

_25

_25

// An octal number

_25

//

_25

0o12345670 // is `2739128`

_25

_25

// A hexadecimal number

_25

//

_25

0x1234567890ABCabc // is `1311768467294898876`

_25

_25

// Invalid: unsupported prefix 0z

_25

//

_25

0z0

_25

_25

// A decimal number with leading zeros. Not an octal number!

_25

00123 // is `123`

_25

_25

// A binary number with several trailing zeros.

_25

0b001000 // is `8` ``

Decimal numbers may contain underscores (`_`) to logically separate components:

`_10

let largeNumber = 1_000_000

_10

_10

// Invalid: Value is not a number literal, but a variable.

_10

let notNumber = _123`

Underscores are allowed for all numeral systems:

`_10

let binaryNumber = 0b10_11_01`

## Integers[​](#integers "Direct link to Integers")

Integers are numbers without a fractional part. They are either *signed* (positive, zero, or negative) or *unsigned* (positive or zero).

Signed integer types that check for overflow and underflow have an `Int` prefix and can represent values in the following ranges:

* **`Int8`**: -2^7 through 2^7 − 1 (-128 through 127)
* **`Int16`**: -2^15 through 2^15 − 1 (-32768 through 32767)
* **`Int32`**: -2^31 through 2^31 − 1 (-2147483648 through 2147483647)
* **`Int64`**: -2^63 through 2^63 − 1 (-9223372036854775808 through 9223372036854775807)
* **`Int128`**: -2^127 through 2^127 − 1
* **`Int256`**: -2^255 through 2^255 − 1
* **`Int`**: unbounded

Unsigned integer types that check for overflow and underflow have a `UInt` prefix and can represent values in the following ranges:

* **`UInt8`**: 0 through 2^8 − 1 (255)
* **`UInt16`**: 0 through 2^16 − 1 (65535)
* **`UInt32`**: 0 through 2^32 − 1 (4294967295)
* **`UInt64`**: 0 through 2^64 − 1 (18446744073709551615)
* **`UInt128`**: 0 through 2^128 − 1
* **`UInt256`**: 0 through 2^256 − 1
* **`UInt`**: unbounded >= 0

Unsigned integer types that do **not** check for overflow and underflow (i.e., wrap around) include the `Word` prefix and can represent values in the following ranges:

* **`Word8`**: 0 through 2^8 − 1 (255)
* **`Word16`**: 0 through 2^16 − 1 (65535)
* **`Word32`**: 0 through 2^32 − 1 (4294967295)
* **`Word64`**: 0 through 2^64 − 1 (18446744073709551615)
* **`Word128`**: 0 through 2^128 − 1 (340282366920938463463374607431768211455)
* **`Word256`**: 0 through 2^256 − 1 (115792089237316195423570985008687907853269984665640564039457584007913129639935)

The types are independent types (i.e., they are not subtypes of each other).

See the section about [arithmetic operators](/docs/language/operators/arithmetic-logical-operators#arithmetic-operators) for further information about the behavior of the different integer types.

`` _10

// Declare a constant that has type `UInt8` and the value 10.

_10

let smallNumber: UInt8 = 10 ``

`_10

// Invalid: negative literal cannot be used as an unsigned integer

_10

//

_10

let invalidNumber: UInt8 = -10`

As shown above, there are two arbitrary precision integer types, `Int` and `UInt`:

`_10

let veryLargeNumber: Int = -10000000000000000000000000000000

_10

let veryLargeNonNegativeNumber: UInt = 10000000000000000000000000000000`

Integer literals are [inferred](/docs/language/types-and-type-system/type-inference) to have type `Int`, or if the literal occurs in a position that expects an explicit type (e.g., in a variable declaration with an explicit type annotation):

`` _10

let someNumber = 123

_10

_10

// `someNumber` has type `Int` ``

Negative integers are encoded in two's complement representation.

Integer types are not converted automatically. Types must be explicitly converted, which can be done by calling the constructor of the type with the integer type:

`` _15

let x: Int8 = 1

_15

let y: Int16 = 2

_15

_15

// Invalid: the types of the operands, `Int8` and `Int16` are incompatible.

_15

let z = x + y

_15

_15

// Explicitly convert `x` from `Int8` to `Int16`.

_15

let a = Int16(x) + y

_15

_15

// `a` has type `Int16`

_15

_15

// Invalid: The integer literal is expected to be of type `Int8`,

_15

// but the large integer literal does not fit in the range of `Int8`.

_15

//

_15

let b = x + 1000000000000000000000000 ``

### Integer functions[​](#integer-functions "Direct link to Integer functions")

Integers have multiple built-in functions you can use.

* `_10

  view fun toString(): String`

  Returns the string representation of the integer.

  `_10

  let answer = 42

  _10

  _10

  answer.toString() // is "42"`
* `_10

  view fun toBigEndianBytes(): [UInt8]`

  Returns the byte array representation (`[UInt8]`) in big-endian order of the integer.

  `` _10

  let largeNumber = 1234567890

  _10

  _10

  largeNumber.toBigEndianBytes() // is `[73, 150, 2, 210]` ``

All integer types support the following functions:

* `_10

  view fun T.fromString(_ input: String): T?`

  Attempts to parse an integer value from a base-10 encoded string, returning `nil` if the string is invalid.

  For a given integer `n` of type `T`, `T.fromString(n.toString())` is equivalent to wrapping `n` up in an [optional](/docs/language/values-and-types/anystruct-anyresource-opts-never#optionals).

  Strings are invalid if:

  + they contain non-digit characters.
  + they don't fit in the target type.

  For signed integer types like `Int64` and `Int`, the string may optionally begin with a `+` or `-` sign prefix.

  For unsigned integer types like `Word64`, `UInt64`, and `UInt`, sign prefices are not allowed.

  Examples:

  `_10

  let fortyTwo: Int64? = Int64.fromString("42") // ok

  _10

  _10

  let twenty: UInt? = UInt.fromString("20") // ok

  _10

  _10

  let nilWord: Word8? = Word8.fromString("1024") // nil, out of bounds

  _10

  _10

  let negTwenty: Int? = Int.fromString("-20") // ok`
* `_10

  view fun T.fromBigEndianBytes(_ bytes: [UInt8]): T?`

  Attempts to parse an integer value from a byte array representation (`[UInt8]`) in big-endian order, returning `nil` if the input bytes are invalid.

  For a given integer `n` of type `T`, `T.fromBigEndianBytes(n.toBigEndianBytes())` is equivalent to wrapping `n` up in an [optional](/docs/language/values-and-types/anystruct-anyresource-opts-never#optionals).

  The bytes are invalid if:

  + the length of the bytes array exceeds the number of bytes needed for the target type.
  + they don't fit in the target type.

  Examples:

  `_10

  let fortyTwo: UInt32? = UInt32.fromBigEndianBytes([42]) // ok

  _10

  _10

  let twenty: UInt? = UInt.fromBigEndianBytes([0, 0, 20]) // ok

  _10

  _10

  let nilWord: Word8? = Word8.fromBigEndianBytes("[0, 22, 0, 0, 0, 0, 0, 0, 0]") // nil, out of bounds

  _10

  _10

  let nilWord2: Word8? = Word8.fromBigEndianBytes("[0, 0]") // nil, size (2) exceeds number of bytes needed for Word8 (1)

  _10

  _10

  let negativeNumber: Int64? = Int64.fromBigEndianBytes([128, 0, 0, 0, 0, 0, 0, 1]) // ok -9223372036854775807`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/booleans-numlits-ints.md)

[Previous

Values and Types](/docs/language/values-and-types/)[Next

Fixed-Point Numbers and Functions](/docs/language/values-and-types/fixed-point-nums-ints)

###### Rate this page

😞😐😊

* [Booleans](#booleans)
* [Numeric literals](#numeric-literals)
* [Integers](#integers)
  + [Integer functions](#integer-functions)