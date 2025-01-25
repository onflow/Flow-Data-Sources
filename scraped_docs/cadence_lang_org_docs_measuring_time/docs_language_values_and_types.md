# Source: https://cadence-lang.org/docs/language/values-and-types




Values and Types | Cadence




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
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Values and Types
On this page
# Values and Types

Values are objects, like for example booleans, integers, or arrays.
Values are typed.

## Booleans[​](#booleans "Direct link to Booleans")

The two boolean values `true` and `false` have the type `Bool`.

## Numeric Literals[​](#numeric-literals "Direct link to Numeric Literals")

Numbers can be written in various bases. Numbers are assumed to be decimal by default.
Non-decimal literals have a specific prefix.

| Numeral system | Prefix | Characters |
| --- | --- | --- |
| **Decimal** | *None* | one or more numbers (`0` to `9`) |
| **Binary** | `0b` | one or more zeros or ones (`0` or `1`) |
| **Octal** | `0o` | one or more numbers in the range `0` to `7` |
| **Hexadecimal** | `0x` | one or more numbers, or characters `a` to `f`, lowercase or uppercase |

 `_25// A decimal number_25//_251234567890 // is `1234567890`_25_25// A binary number_25//_250b101010 // is `42`_25_25// An octal number_25//_250o12345670 // is `2739128`_25_25// A hexadecimal number_25//_250x1234567890ABCabc // is `1311768467294898876`_25_25// Invalid: unsupported prefix 0z_25//_250z0_25_25// A decimal number with leading zeros. Not an octal number!_2500123 // is `123`_25_25// A binary number with several trailing zeros._250b001000 // is `8``

Decimal numbers may contain underscores (`_`) to logically separate components.

 `_10let largeNumber = 1_000_000_10_10// Invalid: Value is not a number literal, but a variable._10let notNumber = _123`

Underscores are allowed for all numeral systems.

 `_10let binaryNumber = 0b10_11_01`
## Integers[​](#integers "Direct link to Integers")

Integers are numbers without a fractional part.
They are either *signed* (positive, zero, or negative)
or *unsigned* (positive or zero).

Signed integer types which check for overflow and underflow have an `Int` prefix
and can represent values in the following ranges:

* **`Int8`**: -2^7 through 2^7 − 1 (-128 through 127)
* **`Int16`**: -2^15 through 2^15 − 1 (-32768 through 32767)
* **`Int32`**: -2^31 through 2^31 − 1 (-2147483648 through 2147483647)
* **`Int64`**: -2^63 through 2^63 − 1 (-9223372036854775808 through 9223372036854775807)
* **`Int128`**: -2^127 through 2^127 − 1
* **`Int256`**: -2^255 through 2^255 − 1

Unsigned integer types which check for overflow and underflow have a `UInt` prefix
and can represent values in the following ranges:

* **`UInt8`**: 0 through 2^8 − 1 (255)
* **`UInt16`**: 0 through 2^16 − 1 (65535)
* **`UInt32`**: 0 through 2^32 − 1 (4294967295)
* **`UInt64`**: 0 through 2^64 − 1 (18446744073709551615)
* **`UInt128`**: 0 through 2^128 − 1
* **`UInt256`**: 0 through 2^256 − 1

Unsigned integer types which do **not** check for overflow and underflow,
i.e. wrap around, have the `Word` prefix
and can represent values in the following ranges:

* **`Word8`**: 0 through 2^8 − 1 (255)
* **`Word16`**: 0 through 2^16 − 1 (65535)
* **`Word32`**: 0 through 2^32 − 1 (4294967295)
* **`Word64`**: 0 through 2^64 − 1 (18446744073709551615)
* **`Word128`**: 0 through 2^128 − 1 (340282366920938463463374607431768211455)
* **`Word256`**: 0 through 2^256 − 1 (115792089237316195423570985008687907853269984665640564039457584007913129639935)

The types are independent types, i.e. not subtypes of each other.

See the section about [arithmetic operators](/docs/language/operators#arithmetic-operators) for further
information about the behavior of the different integer types.

 `_10// Declare a constant that has type `UInt8` and the value 10._10let smallNumber: UInt8 = 10`
 `_10// Invalid: negative literal cannot be used as an unsigned integer_10//_10let invalidNumber: UInt8 = -10`

In addition, the arbitrary precision integer type `Int` is provided.

 `_10let veryLargeNumber: Int = 10000000000000000000000000000000`

Integer literals are [inferred](/docs/language/type-inference) to have type `Int`,
or if the literal occurs in a position that expects an explicit type,
e.g. in a variable declaration with an explicit type annotation.

 `_10let someNumber = 123_10_10// `someNumber` has type `Int``

Negative integers are encoded in two's complement representation.

Integer types are not converted automatically. Types must be explicitly converted,
which can be done by calling the constructor of the type with the integer type.

 `_15let x: Int8 = 1_15let y: Int16 = 2_15_15// Invalid: the types of the operands, `Int8` and `Int16` are incompatible._15let z = x + y_15_15// Explicitly convert `x` from `Int8` to `Int16`._15let a = Int16(x) + y_15_15// `a` has type `Int16`_15_15// Invalid: The integer literal is expected to be of type `Int8`,_15// but the large integer literal does not fit in the range of `Int8`._15//_15let b = x + 1000000000000000000000000`
### Integer Functions[​](#integer-functions "Direct link to Integer Functions")

Integers have multiple built-in functions you can use.

* `_10view fun toString(): String`
  
  Returns the string representation of the integer.
  
   `_10let answer = 42_10_10answer.toString() // is "42"`
* `_10view fun toBigEndianBytes(): [UInt8]`
  
  Returns the byte array representation (`[UInt8]`) in big-endian order of the integer.
  
   `_10let largeNumber = 1234567890_10_10largeNumber.toBigEndianBytes() // is `[73, 150, 2, 210]``

All integer types support the following functions:

* `_10view fun T.fromString(_ input: String): T?`
  
  Attempts to parse an integer value from a base-10 encoded string, returning `nil` if the string is invalid.
  
  For a given integer `n` of type `T`, `T.fromString(n.toString())` is equivalent to wrapping `n` up in an [optional](#optionals).
  
  Strings are invalid if:
  
  + they contain non-digit characters
  + they don't fit in the target type
  
  For signed integer types like `Int64`, and `Int`, the string may optionally begin with `+` or `-` sign prefix.
  
  For unsigned integer types like `Word64`, `UInt64`, and `UInt`, sign prefices are not allowed.
  
  Examples:
  
   `_10let fortyTwo: Int64? = Int64.fromString("42") // ok_10_10let twenty: UInt? = UInt.fromString("20") // ok_10_10let nilWord: Word8? = Word8.fromString("1024") // nil, out of bounds_10_10let negTwenty: Int? = Int.fromString("-20") // ok`
* `_10view fun T.fromBigEndianBytes(_ bytes: [UInt8]): T?`
  
  Attempts to parse an integer value from a byte array representation (`[UInt8]`) in big-endian order, returning `nil` if the input bytes are invalid.
  
  For a given integer `n` of type `T`, `T.fromBigEndianBytes(n.toBigEndianBytes())` is equivalent to wrapping `n` up in an [optional](#optionals).
  
  The bytes are invalid if:
  
  + length of the bytes array exceeds the number of bytes needed for the target type
  + they don't fit in the target type
  
  Examples:
  
   `_10let fortyTwo: UInt32? = UInt32.fromBigEndianBytes([42]) // ok_10_10let twenty: UInt? = UInt.fromBigEndianBytes([0, 0, 20]) // ok_10_10let nilWord: Word8? = Word8.fromBigEndianBytes("[0, 22, 0, 0, 0, 0, 0, 0, 0]") // nil, out of bounds_10_10let nilWord2: Word8? = Word8.fromBigEndianBytes("[0, 0]") // nil, size (2) exceeds number of bytes needed for Word8 (1)_10_10let negativeNumber: Int64? = Int64.fromBigEndianBytes([128, 0, 0, 0, 0, 0, 0, 1]) // ok -9223372036854775807`

## Fixed-Point Numbers[​](#fixed-point-numbers "Direct link to Fixed-Point Numbers")

🚧 Status

Currently only the 64-bit wide `Fix64` and `UFix64` types are available.
More fixed-point number types will be added in a future release.

Fixed-point numbers are useful for representing fractional values.
They have a fixed number of digits after decimal point.

They are essentially integers which are scaled by a factor.
For example, the value 1.23 can be represented as 1230 with a scaling factor of 1/1000.
The scaling factor is the same for all values of the same type
and stays the same during calculations.

Fixed-point numbers in Cadence have a scaling factor with a power of 10, instead of a power of 2,
i.e. they are decimal, not binary.

Signed fixed-point number types have the prefix `Fix`,
have the following factors, and can represent values in the following ranges:

* **`Fix64`**: Factor 1/100,000,000; -92233720368.54775808 through 92233720368.54775807

Unsigned fixed-point number types have the prefix `UFix`,
have the following factors, and can represent values in the following ranges:

* **`UFix64`**: Factor 1/100,000,000; 0.0 through 184467440737.09551615

### Fixed-Point Number Functions[​](#fixed-point-number-functions "Direct link to Fixed-Point Number Functions")

Fixed-Point numbers have multiple built-in functions you can use.

* `_10view fun toString(): String`
  
  Returns the string representation of the fixed-point number.
  
   `_10let fix = 1.23_10_10fix.toString() // is "1.23000000"`
* `_10view fun toBigEndianBytes(): [UInt8]`
  
  Returns the byte array representation (`[UInt8]`) in big-endian order of the fixed-point number.
  
   `_10let fix = 1.23_10_10fix.toBigEndianBytes() // is `[0, 0, 0, 0, 7, 84, 212, 192]``

All fixed-point types support the following functions:

* `_10view fun T.fromString(_ input: String): T?`
  
  Attempts to parse a fixed-point value from a base-10 encoded string, returning `nil` if the string is invalid.
  
  For a given fixed-point numeral `n` of type `T`, `T.fromString(n.toString())` is equivalent to wrapping `n` up in an `optional`.
  
  Strings are invalid if:
  
  + they contain non-digit characters.
  + they don't fit in the target type.
  + they're missing a decimal or fractional component. For example, both "0." and ".1" are invalid strings, but "0.1" is accepted.
  
  For signed types like `Fix64`, the string may optionally begin with `+` or `-` sign prefix.
  
  For unsigned types like `UFix64`, sign prefices are not allowed.
  
  Examples:
  
   `_11let nil1: UFix64? = UFix64.fromString("0.") // nil, fractional part is required_11_11let nil2: UFix64? = UFix64.fromString(".1") // nil, decimal part is required_11_11let smol: UFix64? = UFix64.fromString("0.1") // ok_11_11let smolString: String = "-0.1"_11_11let nil3: UFix64? = UFix64.fromString(smolString) // nil, unsigned types don't allow a sign prefix_11_11let smolFix64: Fix64? = Fix64.fromString(smolString) // ok`
* `_10view fun T.fromBigEndianBytes(_ bytes: [UInt8]): T?`
  
  Attempts to parse an integer value from a byte array representation (`[UInt8]`) in big-endian order, returning `nil` if the input bytes are invalid.
  
  For a given integer `n` of type `T`, `T.fromBigEndianBytes(n.toBigEndianBytes())` is equivalent to wrapping `n` up in an [optional](#optionals).
  
  The bytes are invalid if:
  
  + length of the bytes array exceeds the number of bytes needed for the target type
  + they don't fit in the target type
  
  Examples:
  
   `_10let fortyTwo: UFix64? = UFix64.fromBigEndianBytes([0, 0, 0, 0, 250, 86, 234, 0]) // ok, 42.0_10_10let nilWord: UFix64? = UFix64.fromBigEndianBytes("[100, 22, 0, 0, 0, 0, 0, 0, 0]") // nil, out of bounds_10_10let nilWord2: Fix64? = Fix64.fromBigEndianBytes("[0, 22, 0, 0, 0, 0, 0, 0, 0]") // // nil, size (9) exceeds number of bytes needed for Fix64 (8)_10_10let negativeNumber: Fix64? = Fix64.fromBigEndianBytes([255, 255, 255, 255, 250, 10, 31, 0]) // ok, -1`

## Minimum and maximum values[​](#minimum-and-maximum-values "Direct link to Minimum and maximum values")

The minimum and maximum values for all integer and fixed-point number types are available through the fields `min` and `max`.

For example:

 `_10let max = UInt8.max_10// `max` is 255, the maximum value of the type `UInt8``
 `_10let max = UFix64.max_10// `max` is 184467440737.09551615, the maximum value of the type `UFix64``
## Saturation Arithmetic[​](#saturation-arithmetic "Direct link to Saturation Arithmetic")

Integers and fixed-point numbers support saturation arithmetic:
Arithmetic operations, such as addition or multiplications, are saturating at the numeric bounds instead of overflowing.

If the result of an operation is greater than the maximum value of the operands' type, the maximum is returned.
If the result is lower than the minimum of the operands' type, the minimum is returned.

Saturating addition, subtraction, multiplication, and division are provided as functions with the prefix `saturating`:

* `Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`, `Fix64`:
  
  + `saturatingAdd`
  + `saturatingSubtract`
  + `saturatingMultiply`
  + `saturatingDivide`
* `Int`:
  
  + none
* `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `UFix64`:
  
  + `saturatingAdd`
  + `saturatingSubtract`
  + `saturatingMultiply`
* `UInt`:
  
  + `saturatingSubtract`

 `_10let a: UInt8 = 200_10let b: UInt8 = 100_10let result = a.saturatingAdd(b)_10// `result` is 255, the maximum value of the type `UInt8``
## Floating-Point Numbers[​](#floating-point-numbers "Direct link to Floating-Point Numbers")

There is **no** support for floating point numbers.

Smart Contracts are not intended to work with values with error margins
and therefore floating point arithmetic is not appropriate here.

Instead, consider using [fixed point numbers](#fixed-point-numbers).

## Addresses[​](#addresses "Direct link to Addresses")

The type `Address` represents an address.
Addresses are unsigned integers with a size of 64 bits (8 bytes).
Hexadecimal integer literals can be used to create address values.

 `_13// Declare a constant that has type `Address`._13//_13let someAddress: Address = 0x436164656E636521_13_13// Invalid: Initial value is not compatible with type `Address`,_13// it is not a number._13//_13let notAnAddress: Address = ""_13_13// Invalid: Initial value is not compatible with type `Address`._13// The integer literal is valid, however, it is larger than 64 bits._13//_13let alsoNotAnAddress: Address = 0x436164656E63652146757265766572`

Integer literals are not inferred to be an address.

 `_10// Declare a number. Even though it happens to be a valid address,_10// it is not inferred as it._10//_10let aNumber = 0x436164656E636521_10_10// `aNumber` has type `Int``

Address can also be created using a byte array or string.

 `_17// Declare an address with hex representation as 0x436164656E636521._17let someAddress: Address = Address.fromBytes([67, 97, 100, 101, 110, 99, 101, 33])_17_17// Invalid: Provided value is not compatible with type `Address`. The function panics._17let invalidAddress: Address = Address.fromBytes([12, 34, 56, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111])_17_17// Declare an address with the string representation as "0x436164656E636521"._17let addressFromString: Address? = Address.fromString("0x436164656E636521")_17_17// Invalid: Provided value does not have the "0x" prefix. Returns Nil_17let addressFromStringWithoutPrefix: Address? = Address.fromString("436164656E636521")_17_17// Invalid: Provided value is an invalid hex string. Return Nil._17let invalidAddressForInvalidHex: Address? = Address.fromString("0xZZZ")_17_17// Invalid: Provided value is larger than 64 bits. Return Nil._17let invalidAddressForOverflow: Address? = Address.fromString("0x436164656E63652146757265766572")`
### Address Functions[​](#address-functions "Direct link to Address Functions")

Addresses have multiple built-in functions you can use.

* `_10view fun toString(): String`
  
  Returns the string representation of the address.
  The result has a `0x` prefix and is zero-padded.
  
   `_10let someAddress: Address = 0x436164656E636521_10someAddress.toString() // is "0x436164656E636521"_10_10let shortAddress: Address = 0x1_10shortAddress.toString() // is "0x0000000000000001"`
* `_10view fun toBytes(): [UInt8]`
  
  Returns the byte array representation (`[UInt8]`) of the address.
  
   `_10let someAddress: Address = 0x436164656E636521_10_10someAddress.toBytes() // is `[67, 97, 100, 101, 110, 99, 101, 33]``

## AnyStruct and AnyResource[​](#anystruct-and-anyresource "Direct link to AnyStruct and AnyResource")

`AnyStruct` is the top type of all non-resource types,
i.e., all non-resource types are a subtype of it.

`AnyResource` is the top type of all resource types.

 `_37// Declare a variable that has the type `AnyStruct`._37// Any non-resource typed value can be assigned to it, for example an integer,_37// but not resource-typed values._37//_37var someStruct: AnyStruct = 1_37_37// Assign a value with a different non-resource type, `Bool`._37someStruct = true_37_37// Declare a structure named `TestStruct`, create an instance of it,_37// and assign it to the `AnyStruct`-typed variable_37//_37struct TestStruct {}_37_37let testStruct = TestStruct()_37_37someStruct = testStruct_37_37// Declare a resource named `TestResource`_37_37resource TestResource {}_37_37// Declare a variable that has the type `AnyResource`._37// Any resource-typed value can be assigned to it,_37// but not non-resource typed values._37//_37var someResource: @AnyResource <- create TestResource()_37_37// Invalid: Resource-typed values can not be assigned_37// to `AnyStruct`-typed variables_37//_37someStruct <- create TestResource()_37_37// Invalid: Non-resource typed values can not be assigned_37// to `AnyResource`-typed variables_37//_37someResource = 1`

However, using `AnyStruct` and `AnyResource` does not opt-out of type checking.
It is invalid to access fields and call functions on these types,
as they have no fields and functions.

 `_10// Declare a variable that has the type `AnyStruct`._10// The initial value is an integer,_10// but the variable still has the explicit type `AnyStruct`._10//_10let a: AnyStruct = 1_10_10// Invalid: Operator cannot be used for an `AnyStruct` value (`a`, left-hand side)_10// and an `Int` value (`2`, right-hand side)._10//_10a + 2`

`AnyStruct` and `AnyResource` may be used like other types,
for example, they may be the element type of [arrays](#arrays)
or be the element type of an [optional type](#optionals).

 `_13// Declare a variable that has the type `[AnyStruct]`,_13// i.e. an array of elements of any non-resource type._13//_13let anyValues: [AnyStruct] = [1, "2", true]_13_13// Declare a variable that has the type `AnyStruct?`,_13// i.e. an optional type of any non-resource type._13//_13var maybeSomething: AnyStruct? = 42_13_13maybeSomething = "twenty-four"_13_13maybeSomething = nil`

`AnyStruct` is also the super-type of all non-resource optional types,
and `AnyResource` is the super-type of all resource optional types.

 `_10let maybeInt: Int? = 1_10let anything: AnyStruct = maybeInt`

[Conditional downcasting](/docs/language/operators#conditional-downcasting-operator-as) allows coercing
a value which has the type `AnyStruct` or `AnyResource` back to its original type.

## Optionals[​](#optionals "Direct link to Optionals")

Optionals are values which can represent the absence of a value. Optionals have two cases:
either there is a value, or there is nothing.

An optional type is declared using the `?` suffix for another type.
For example, `Int` is a non-optional integer, and `Int?` is an optional integer,
i.e. either nothing, or an integer.

The value representing nothing is `nil`.

 `_17// Declare a constant which has an optional integer type,_17// with nil as its initial value._17//_17let a: Int? = nil_17_17// Declare a constant which has an optional integer type,_17// with 42 as its initial value._17//_17let b: Int? = 42_17_17// Invalid: `b` has type `Int?`, which does not support arithmetic._17b + 23_17_17// Invalid: Declare a constant with a non-optional integer type `Int`,_17// but the initial value is `nil`, which in this context has type `Int?`._17//_17let x: Int = nil`

Optionals can be created for any value, not just for literals.

 `_15// Declare a constant which has a non-optional integer type,_15// with 1 as its initial value._15//_15let x = 1_15_15// Declare a constant which has an optional integer type._15// An optional with the value of `x` is created._15//_15let y: Int? = x_15_15// Declare a variable which has an optional any type, i.e. the variable_15// may be `nil`, or any other value._15// An optional with the value of `x` is created._15//_15var z: AnyStruct? = x`

A non-optional type is a subtype of its optional type.

 `_10var a: Int? = nil_10let b = 2_10a = b_10_10// `a` is `2``

Optional types may be contained in other types, for example [arrays](#arrays) or even optionals.

 `_10// Declare a constant which has an array type of optional integers._10let xs: [Int?] = [1, nil, 2, nil]_10_10// Declare a constant which has a double optional type._10//_10let doubleOptional: Int?? = nil`

See the [optional operators](/docs/language/operators#optional-operators) section for information
on how to work with optionals.

## Never[​](#never "Direct link to Never")

`Never` is the bottom type, i.e., it is a subtype of all types.
There is no value that has type `Never`.
`Never` can be used as the return type for functions that never return normally.
For example, it is the return type of the function [`panic`](/docs/language/built-in-functions#panic).

 `_17// Declare a function named `crashAndBurn` which will never return,_17// because it calls the function named `panic`, which never returns._17//_17fun crashAndBurn(): Never {_17 panic("An unrecoverable error occurred")_17}_17_17// Invalid: Declare a constant with a `Never` type, but the initial value is an integer._17//_17let x: Never = 1_17_17// Invalid: Declare a function which returns an invalid return value `nil`,_17// which is not a value of type `Never`._17//_17fun returnNever(): Never {_17 return nil_17}`
## Strings and Characters[​](#strings-and-characters "Direct link to Strings and Characters")

Strings are collections of characters.
Strings have the type `String`, and characters have the type `Character`.
Strings can be used to work with text in a Unicode-compliant way.
Strings are immutable.

String and character literals are enclosed in double quotation marks (`"`).

 `_10let someString = "Hello, world!"`

String literals may contain escape sequences. An escape sequence starts with a backslash (`\`):

* `\0`: Null character
* `\\`: Backslash
* `\t`: Horizontal tab
* `\n`: Line feed
* `\r`: Carriage return
* `\"`: Double quotation mark
* `\'`: Single quotation mark
* `\u`: A Unicode scalar value, written as `\u{x}`,
  where `x` is a 1–8 digit hexadecimal number
  which needs to be a valid Unicode scalar value,
  i.e., in the range 0 to 0xD7FF and 0xE000 to 0x10FFFF inclusive

 `_10// Declare a constant which contains two lines of text_10// (separated by the line feed character `\n`), and ends_10// with a thumbs up emoji, which has code point U+1F44D (0x1F44D)._10//_10let thumbsUpText =_10 "This is the first line.\nThis is the second line with an emoji: \u{1F44D}"`

The type `Character` represents a single, human-readable character.
Characters are extended grapheme clusters,
which consist of one or more Unicode scalars.

For example, the single character `ü` can be represented
in several ways in Unicode.
First, it can be represented by a single Unicode scalar value `ü`
("LATIN SMALL LETTER U WITH DIAERESIS", code point U+00FC).
Second, the same single character can be represented
by two Unicode scalar values:
`u` ("LATIN SMALL LETTER U", code point U+0075),
and "COMBINING DIAERESIS" (code point U+0308).
The combining Unicode scalar value is applied to the scalar before it,
which turns a `u` into a `ü`.

Still, both variants represent the same human-readable character `ü`.

 `_10let singleScalar: Character = "\u{FC}"_10// `singleScalar` is `ü`_10let twoScalars: Character = "\u{75}\u{308}"_10// `twoScalars` is `ü``

Another example where multiple Unicode scalar values are rendered as a single,
human-readable character is a flag emoji.
These emojis consist of two "REGIONAL INDICATOR SYMBOL LETTER" Unicode scalar values.

 `_10// Declare a constant for a string with a single character, the emoji_10// for the Canadian flag, which consists of two Unicode scalar values:_10// - REGIONAL INDICATOR SYMBOL LETTER C (U+1F1E8)_10// - REGIONAL INDICATOR SYMBOL LETTER A (U+1F1E6)_10//_10let canadianFlag: Character = "\u{1F1E8}\u{1F1E6}"_10// `canadianFlag` is `🇨🇦``
### String Fields and Functions[​](#string-fields-and-functions "Direct link to String Fields and Functions")

Strings have multiple built-in functions you can use:

* `_10let length: Int`
  
  Returns the number of characters in the string as an integer.
  
   `_10let example = "hello"_10_10// Find the number of elements of the string._10let length = example.length_10// `length` is `5``
* `_10let utf8: [UInt8]`
  
  The byte array of the UTF-8 encoding
  
   `_10let flowers = "Flowers \u{1F490}"_10let bytes = flowers.utf8_10// `bytes` is `[70, 108, 111, 119, 101, 114, 115, 32, 240, 159, 146, 144]``
* `_10view fun concat(_ other: String): String`
  
  Concatenates the string `other` to the end of the original string,
  but does not modify the original string.
  This function creates a new string whose length is the sum of the lengths
  of the string the function is called on and the string given as a parameter.
  
   `_10let example = "hello"_10let new = "world"_10_10// Concatenate the new string onto the example string and return the new string._10let helloWorld = example.concat(new)_10// `helloWorld` is now `"helloworld"``
* `_10view fun slice(from: Int, upTo: Int): String`
  
  Returns a string slice of the characters
  in the given string from start index `from` up to,
  but not including, the end index `upTo`.
  This function creates a new string whose length is `upTo - from`.
  It does not modify the original string.
  If either of the parameters are out of the bounds of the string,
  or the indices are invalid (`from > upTo`), then the function will fail.
  
   `_11let example = "helloworld"_11_11// Create a new slice of part of the original string._11let slice = example.slice(from: 3, upTo: 6)_11// `slice` is now `"low"`_11_11// Run-time error: Out of bounds index, the program aborts._11let outOfBounds = example.slice(from: 2, upTo: 10)_11_11// Run-time error: Invalid indices, the program aborts._11let invalidIndices = example.slice(from: 2, upTo: 1)`
* `_10view fun decodeHex(): [UInt8]`
  
  Returns an array containing the bytes represented by the given hexadecimal string.
  
  The given string must only contain hexadecimal characters and must have an even length.
  If the string is malformed, the program aborts
  
   `_10let example = "436164656e636521"_10_10example.decodeHex() // is `[67, 97, 100, 101, 110, 99, 101, 33]``
* `_10view fun toLower(): String`
  
  Returns a string where all upper case letters are replaced with lowercase characters
  
   `_10let example = "Flowers"_10_10example.toLower() // is `flowers``
* `_10view fun replaceAll(of: String, with: String): String`
  
  Returns a string where all occurences of `of` are replaced with `with`.
  If `of` is empty, it matches at the beginning of the string and after each UTF-8 sequence, yielding k+1 replacements for a string of length k.
  
   `_10let example = "abababa"_10_10example.replaceAll(of: "a", with: "o") // is `obobobo``
* `_10view fun split(separator: String): [String]`
  
  Returns the variable-sized array of strings created splitting the receiver string on the `separator`.
  
   `_10let example = "hello world"_10_10example.split(separator: " ") // is `["hello", "world"]``

The `String` type also provides the following functions:

* `_10view fun String.encodeHex(_ data: [UInt8]): String`
  
  Returns a hexadecimal string for the given byte array
  
   `_10let data = [1 as UInt8, 2, 3, 0xCA, 0xDE]_10_10String.encodeHex(data) // is `"010203cade"``
* `_10view fun String.join(_ strings: [String], separator: String): String`
  
  Returns the string created by joining the array of `strings` with the provided `separator`.
  
   `_10let strings = ["hello", "world"]_10String.join(strings, " ") // is "hello world"`

`String`s are also indexable, returning a `Character` value.

 `_10let str = "abc"_10let c = str[0] // is the Character "a"`

* `_10view fun String.fromUTF8(_ input: [UInt8]): String?`
  
  Attempts to convert a UTF-8 encoded byte array into a `String`. This function returns `nil` if the byte array contains invalid UTF-8,
  such as incomplete codepoint sequences or undefined graphemes.
  
  For a given string `s`, `String.fromUTF8(s.utf8)` is equivalent to wrapping `s` up in an [optional](#optionals).

### Character Fields and Functions[​](#character-fields-and-functions "Direct link to Character Fields and Functions")

`Character` values can be converted into `String` values using the `toString` function:

* `_10view fun toString(): String``
  
  Returns the string representation of the character.
  
   `_10let c: Character = "x"_10_10c.toString() // is "x"`
* `_10view fun String.fromCharacters(_ characters: [Character]): String`
  
  Builds a new `String` value from an array of `Character`s. Because `String`s are immutable, this operation makes a copy of the input array.
  
   `_10let rawUwU: [Character] = ["U", "w", "U"]_10let uwu: String = String.fromCharacters(rawUwU) // "UwU"`
* `_10let utf8: [UInt8]`
  
  The byte array of the UTF-8 encoding
  
   `_10let a: Character = "a"_10let a_bytes = a.utf8 // `a_bytes` is `[97]`_10_10let bouquet: Character = "\u{1F490}"_10let bouquet_bytes = bouquet.utf8 // `bouquet_bytes` is `[240, 159, 146, 144]``

## Arrays[​](#arrays "Direct link to Arrays")

Arrays are mutable, ordered collections of values.
Arrays may contain a value multiple times.
Array literals start with an opening square bracket `[` and end with a closing square bracket `]`.

 `_10// An empty array_10//_10[]_10_10// An array with integers_10//_10[1, 2, 3]`
### Array Types[​](#array-types "Direct link to Array Types")

Arrays either have a fixed size or are variably sized, i.e., elements can be added and removed.

Fixed-size array types have the form `[T; N]`, where `T` is the element type,
and `N` is the size of the array. `N` has to be statically known, meaning
that it needs to be an integer literal.
For example, a fixed-size array of 3 `Int8` elements has the type `[Int8; 3]`.

Variable-size array types have the form `[T]`, where `T` is the element type.
For example, the type `[Int16]` specifies a variable-size array of elements that have type `Int16`.

All values in an array must have a type which is a subtype of the array's element type (`T`).

It is important to understand that arrays are value types and are only ever copied
when used as an initial value for a constant or variable,
when assigning to a variable,
when used as function argument,
or when returned from a function call.

 `_26let size = 2_26// Invalid: Array-size must be an integer literal_26let numbers: [Int; size] = []_26_26// Declare a fixed-sized array of integers_26// which always contains exactly two elements._26//_26let array: [Int8; 2] = [1, 2]_26_26// Declare a fixed-sized array of fixed-sized arrays of integers._26// The inner arrays always contain exactly three elements,_26// the outer array always contains two elements._26//_26let arrays: [[Int16; 3]; 2] = [_26 [1, 2, 3],_26 [4, 5, 6]_26]_26_26// Declare a variable length array of integers_26var variableLengthArray: [Int] = []_26_26// Mixing values with different types is possible_26// by declaring the expected array type_26// with the common supertype of all values._26//_26let mixedValues: [AnyStruct] = ["some string", 42]`

Array types are covariant in their element types.
For example, `[Int]` is a subtype of `[AnyStruct]`.
This is safe because arrays are value types and not reference types.

### Array Indexing[​](#array-indexing "Direct link to Array Indexing")

To get the element of an array at a specific index, the indexing syntax can be used:
The array is followed by an opening square bracket `[`, the indexing value,
and ends with a closing square bracket `]`.

Indexes start at 0 for the first element in the array.

Accessing an element which is out of bounds results in a fatal error at run-time
and aborts the program.

 `_14// Declare an array of integers._14let numbers = [42, 23]_14_14// Get the first number of the array._14//_14numbers[0] // is `42`_14_14// Get the second number of the array._14//_14numbers[1] // is `23`_14_14// Run-time error: Index 2 is out of bounds, the program aborts._14//_14numbers[2]`
 `_10// Declare an array of arrays of integers, i.e. the type is `[[Int]]`._10let arrays = [[1, 2], [3, 4]]_10_10// Get the first number of the second array._10//_10arrays[1][0] // is `3``

To set an element of an array at a specific index, the indexing syntax can be used as well.

 `_12// Declare an array of integers._12let numbers = [42, 23]_12_12// Change the second number in the array._12//_12// NOTE: The declaration `numbers` is constant, which means that_12// the *name* is constant, not the *value* – the value, i.e. the array,_12// is mutable and can be changed._12//_12numbers[1] = 2_12_12// `numbers` is `[42, 2]``
### Array Fields and Functions[​](#array-fields-and-functions "Direct link to Array Fields and Functions")

Arrays have multiple built-in fields and functions
that can be used to get information about and manipulate the contents of the array.

The field `length`, and the functions `concat`, and `contains`
are available for both variable-sized and fixed-sized or variable-sized arrays.

* `_10let length: Int`
  
  The number of elements in the array.
  
   `_10// Declare an array of integers._10let numbers = [42, 23, 31, 12]_10_10// Find the number of elements of the array._10let length = numbers.length_10_10// `length` is `4``
* `_10access(all)_10view fun concat(_ array: T): T`
  
  Concatenates the parameter `array` to the end
  of the array the function is called on,
  but does not modify that array.
  
  Both arrays must be the same type `T`.
  
  This function creates a new array whose length is the sum of the length of the array
  the function is called on and the length of the array given as the parameter.
  
   `_12// Declare two arrays of integers._12let numbers = [42, 23, 31, 12]_12let moreNumbers = [11, 27]_12_12// Concatenate the array `moreNumbers` to the array `numbers`_12// and declare a new variable for the result._12//_12let allNumbers = numbers.concat(moreNumbers)_12_12// `allNumbers` is `[42, 23, 31, 12, 11, 27]`_12// `numbers` is still `[42, 23, 31, 12]`_12// `moreNumbers` is still `[11, 27]``
* `_10access(all)_10view fun contains(_ element: T): Bool`
  
  Returns true if the given element of type `T` is in the array.
  
   `_15// Declare an array of integers._15let numbers = [42, 23, 31, 12]_15_15// Check if the array contains 11._15let containsEleven = numbers.contains(11)_15// `containsEleven` is `false`_15_15// Check if the array contains 12._15let containsTwelve = numbers.contains(12)_15// `containsTwelve` is `true`_15_15// Invalid: Check if the array contains the string "Kitty"._15// This results in a type error, as the array only contains integers._15//_15let containsKitty = numbers.contains("Kitty")`
* `_10access(all)_10view fun firstIndex(of: T): Int?`
  
  Returns the index of the first element matching the given object in the array, nil if no match.
  Available if `T` is not resource-kinded and equatable.
  
   `_10 // Declare an array of integers._10 let numbers = [42, 23, 31, 12]_10_10 // Check if the array contains 31_10 let index = numbers.firstIndex(of: 31)_10 // `index` is 2_10_10 // Check if the array contains 22_10 let index = numbers.firstIndex(of: 22)_10 // `index` is nil`
* `_10access(all)_10view fun slice(from: Int, upTo: Int): [T]`
  
  Returns an array slice of the elements
  in the given array from start index `from` up to,
  but not including, the end index `upTo`.
  This function creates a new array whose length is `upTo - from`.
  It does not modify the original array.
  If either of the parameters are out of the bounds of the array,
  or the indices are invalid (`from > upTo`), then the function will fail.
  
   `_11let example = [1, 2, 3, 4]_11_11// Create a new slice of part of the original array._11let slice = example.slice(from: 1, upTo: 3)_11// `slice` is now `[2, 3]`_11_11// Run-time error: Out of bounds index, the program aborts._11let outOfBounds = example.slice(from: 2, upTo: 10)_11_11// Run-time error: Invalid indices, the program aborts._11let invalidIndices = example.slice(from: 2, upTo: 1)`
* `_10access(all)_10view fun reverse(): [T]`
  
  Returns a new array with contents in the reversed order.
  Available if `T` is not resource-kinded.
  
   `_10let example = [1, 2, 3, 4]_10_10// Create a new array which is the reverse of the original array._10let reversedExample = example.reverse()_10// `reversedExample` is now `[4, 3, 2, 1]``
   `_10access(all)_10view fun reverse(): [T; N]`
  
  Returns a new fixed-sized array of same size with contents in the reversed order.
  
   `_10let fixedSizedExample: [String; 3] = ["ABC", "XYZ", "PQR"]_10_10// Create a new array which is the reverse of the original array._10let fixedArrayReversedExample = fixedSizedExample.reverse()_10// `fixedArrayReversedExample` is now `["PQR", "XYZ", "ABC"]``
* `_10access(all)_10fun map(_ f: fun(T): U): [U]`
  
  Returns a new array whose elements are produced by applying the mapper function on each element
  of the original array.
  Available if `T` is not resource-kinded.
  
   `_18let example = [1, 2, 3]_18let trueForEven =_18 fun (_ x: Int): Bool {_18 return x % 2 == 0_18 }_18_18let mappedExample: [Bool] = example.map(trueForEven)_18// `mappedExample` is `[False, True, False]`_18// `example` still remains as `[1, 2, 3]`_18_18// Invalid: Map using a function which accepts a different type._18// This results in a type error, as the array contains `Int` values while function accepts _18// `Int64`._18let functionAcceptingInt64 =_18 fun (_ x: Int64): Bool {_18 return x % 2 == 0_18 }_18let invalidMapFunctionExample = example.map(functionAcceptingInt64)`
  
  `map` function is also available for fixed-sized arrays:
  
   `_10access(all)_10fun map(_ f: fun(T): U): [U; N]`
  
  Returns a new fixed-sized array whose elements are produced by applying the mapper function on
  each element of the original array.
  Available if `T` is not resource-kinded.
  
   `_18let fixedSizedExample: [String; 3] = ["ABC", "XYZYX", "PQR"]_18let lengthOfString =_18 fun (_ x: String): Int {_18 return x.length_18 }_18_18let fixedArrayMappedExample = fixedSizedExample.map(lengthOfString)_18// `fixedArrayMappedExample` is now `[3, 5, 3]`_18// `fixedSizedExample` still remains as ["ABC", "XYZYX", "PQR"]_18_18// Invalid: Map using a function which accepts a different type._18// This results in a type error, as the array contains `String` values while function accepts _18// `Bool`._18let functionAcceptingBool =_18 fun (_ x: Bool): Int {_18 return 0_18 }_18let invalidMapFunctionExample = fixedSizedExample.map(functionAcceptingBool)`
* `_10access(all)_10view fun filter(_ f: view fun(T): Bool): [T]`
  
  Returns a new array whose elements are filtered by applying the filter function on each element
  of the original array.
  Available if `T` is not resource-kinded.
  
   `_18let example = [1, 2, 3]_18let trueForEven =_18 fun (_ x: Int): Bool {_18 return x % 2 == 0_18 }_18_18let filteredExample: [Int] = example.filter(trueForEven)_18// `filteredExample` is `[2]`_18// `example` still remains as `[1, 2, 3]`_18_18// Invalid: Filter using a function which accepts a different type._18// This results in a type error, as the array contains `Int` values while function accepts _18// `Int64`._18let functionAcceptingInt64 =_18 fun (_ x: Int64): Bool {_18 return x % 2 == 0_18 }_18let invalidFilterFunctionExample = example.filter(functionAcceptingInt64)`
  
  `filter` function is also available for fixed-sized arrays:
  
   `_10access(all)_10view fun filter(_ f: view fun(T): Bool): [T]`
  
  Returns a new **variable-sized** array whose elements are filtered by applying the filter function on each element
  of the original array.
  Available if `T` is not resource-kinded.
  
   `_18let fixedSizedExample: [String; 3] = ["AB", "XYZYX", "PQR"]_18let lengthOfStringGreaterThanTwo =_18 fun (_ x: String): Bool {_18 return x.length > 2_18 }_18_18let fixedArrayFilteredExample = fixedSizedExample.filter(lengthOfStringGreaterThanTwo)_18// `fixedArrayFilteredExample` is `["XYZYX", "PQR"]`_18// `fixedSizedExample` still remains as ["AB", "XYZYX", "PQR"]_18_18// Invalid: Filter using a function which accepts a different type._18// This results in a type error, as the array contains `String` values while function accepts _18// `Bool`._18let functionAcceptingBool =_18 fun (_ x: Bool): Bool {_18 return True_18 }_18let invalidFilterFunctionExample = fixedSizedExample.filter(functionAcceptingBool)`

#### Variable-size Array Functions[​](#variable-size-array-functions "Direct link to Variable-size Array Functions")

The following functions can only be used on variable-sized arrays.
It is invalid to use one of these functions on a fixed-sized array.

* `_10access(Mutate | Insert)_10fun append(_ element: T): Void`
  
  Adds the new element `element` of type `T` to the end of the array.
  
  The new element must be the same type as all the other elements in the array.
  
  This function [mutates](/docs/language/access-control) the array.
  
   `_10// Declare an array of integers._10let numbers = [42, 23, 31, 12]_10_10// Add a new element to the array._10numbers.append(20)_10// `numbers` is now `[42, 23, 31, 12, 20]`_10_10// Invalid: The parameter has the wrong type `String`._10numbers.append("SneakyString")`
* `_10access(Mutate | Insert)_10fun appendAll(_ array: T): Void`
  
  Adds all the elements from `array` to the end of the array
  the function is called on.
  
  Both arrays must be the same type `T`.
  
  This function [mutates](/docs/language/access-control) the array.
  
   `_10// Declare an array of integers._10let numbers = [42, 23]_10_10// Add new elements to the array._10numbers.appendAll([31, 12, 20])_10// `numbers` is now `[42, 23, 31, 12, 20]`_10_10// Invalid: The parameter has the wrong type `[String]`._10numbers.appendAll(["Sneaky", "String"])`
* `_10access(Mutate | Insert)_10fun insert(at: Int, _ element: T): Void`
  
  Inserts the new element `element` of type `T`
  at the given `index` of the array.
  
  The new element must be of the same type as the other elements in the array.
  
  The `index` must be within the bounds of the array.
  If the index is outside the bounds, the program aborts.
  
  The existing element at the supplied index is not overwritten.
  
  All the elements after the new inserted element
  are shifted to the right by one.
  
  This function [mutates](/docs/language/access-control) the array.
  
   `_10// Declare an array of integers._10let numbers = [42, 23, 31, 12]_10_10// Insert a new element at position 1 of the array._10numbers.insert(at: 1, 20)_10// `numbers` is now `[42, 20, 23, 31, 12]`_10_10// Run-time error: Out of bounds index, the program aborts._10numbers.insert(at: 12, 39)`
* `_10access(Mutate | Remove)_10fun remove(at: Int): T`
  
  Removes the element at the given `index` from the array and returns it.
  
  The `index` must be within the bounds of the array.
  If the index is outside the bounds, the program aborts.
  
  This function [mutates](/docs/language/access-control) the array.
  
   `_10// Declare an array of integers._10let numbers = [42, 23, 31]_10_10// Remove element at position 1 of the array._10let twentyThree = numbers.remove(at: 1)_10// `numbers` is now `[42, 31]`_10// `twentyThree` is `23`_10_10// Run-time error: Out of bounds index, the program aborts._10numbers.remove(at: 19)`
* `_10access(Mutate | Remove)_10fun removeFirst(): T`
  
  Removes the first element from the array and returns it.
  
  The array must not be empty.
  If the array is empty, the program aborts.
  
  This function [mutates](/docs/language/access-control) the array.
  
   `_15// Declare an array of integers._15let numbers = [42, 23]_15_15// Remove the first element of the array._15let fortytwo = numbers.removeFirst()_15// `numbers` is now `[23]`_15// `fortywo` is `42`_15_15// Remove the first element of the array._15let twentyThree = numbers.removeFirst()_15// `numbers` is now `[]`_15// `twentyThree` is `23`_15_15// Run-time error: The array is empty, the program aborts._15numbers.removeFirst()`
* `_10access(Mutate | Remove)_10fun removeLast(): T`
  
  Removes the last element from the array and returns it.
  
  The array must not be empty.
  If the array is empty, the program aborts.
  
  This function [mutates](/docs/language/access-control) the array.
  
   `_15// Declare an array of integers._15let numbers = [42, 23]_15_15// Remove the last element of the array._15let twentyThree = numbers.removeLast()_15// `numbers` is now `[42]`_15// `twentyThree` is `23`_15_15// Remove the last element of the array._15let fortyTwo = numbers.removeLast()_15// `numbers` is now `[]`_15// `fortyTwo` is `42`_15_15// Run-time error: The array is empty, the program aborts._15numbers.removeLast()`

## Dictionaries[​](#dictionaries "Direct link to Dictionaries")

Dictionaries are mutable, unordered collections of key-value associations.
Dictionaries may contain a key only once
and may contain a value multiple times.

Dictionary literals start with an opening brace `{`
and end with a closing brace `}`.
Keys are separated from values by a colon,
and key-value associations are separated by commas.

 `_10// An empty dictionary_10//_10{}_10_10// A dictionary which associates integers with booleans_10//_10{_10 1: true,_10 2: false_10}`
### Dictionary Types[​](#dictionary-types "Direct link to Dictionary Types")

Dictionary types have the form `{K: V}`,
where `K` is the type of the key,
and `V` is the type of the value.
For example, a dictionary with `Int` keys and `Bool`
values has type `{Int: Bool}`.

In a dictionary, all keys must have a type that is a subtype of the dictionary's key type (`K`)
and all values must have a type that is a subtype of the dictionary's value type (`V`).

 `_24// Declare a constant that has type `{Int: Bool}`,_24// a dictionary mapping integers to booleans._24//_24let booleans = {_24 1: true,_24 0: false_24}_24_24// Declare a constant that has type `{Bool: Int}`,_24// a dictionary mapping booleans to integers._24//_24let integers = {_24 true: 1,_24 false: 0_24}_24_24// Mixing keys with different types, and mixing values with different types,_24// is possible by declaring the expected dictionary type with the common supertype_24// of all keys, and the common supertype of all values._24//_24let mixedValues: {String: AnyStruct} = {_24 "a": 1,_24 "b": true_24}`

Dictionary types are covariant in their key and value types.
For example, `{Int: String}` is a subtype of `{AnyStruct: String}`
and also a subtype of `{Int: AnyStruct}`.
This is safe because dictionaries are value types and not reference types.

### Dictionary Access[​](#dictionary-access "Direct link to Dictionary Access")

To get the value for a specific key from a dictionary,
the access syntax can be used:
The dictionary is followed by an opening square bracket `[`, the key,
and ends with a closing square bracket `]`.

Accessing a key returns an [optional](#optionals):
If the key is found in the dictionary, the value for the given key is returned,
and if the key is not found, `nil` is returned.

 `_17// Declare a constant that has type `{Int: Bool}`,_17// a dictionary mapping integers to booleans._17//_17let booleans = {_17 1: true,_17 0: false_17}_17_17// The result of accessing a key has type `Bool?`._17//_17booleans[1] // is `true`_17booleans[0] // is `false`_17booleans[2] // is `nil`_17_17// Invalid: Accessing a key which does not have type `Int`._17//_17booleans["1"]`
 `_12// Declare a constant that has type `{Bool: Int}`,_12// a dictionary mapping booleans to integers._12//_12let integers = {_12 true: 1,_12 false: 0_12}_12_12// The result of accessing a key has type `Int?`_12//_12integers[true] // is `1`_12integers[false] // is `0``

To set the value for a key of a dictionary,
the access syntax can be used as well.

 `_13// Declare a constant that has type `{Int: Bool}`,_13// a dictionary mapping booleans to integers._13//_13let booleans = {_13 1: true,_13 0: false_13}_13_13// Assign new values for the keys `1` and `0`._13//_13booleans[1] = false_13booleans[0] = true_13// `booleans` is `{1: false, 0: true}``
### Dictionary Fields and Functions[​](#dictionary-fields-and-functions "Direct link to Dictionary Fields and Functions")

* `_10let length: Int`
  
  The number of entries in the dictionary.
  
   `_10// Declare a dictionary mapping strings to integers._10let numbers = {"fortyTwo": 42, "twentyThree": 23}_10_10// Find the number of entries of the dictionary._10let length = numbers.length_10_10// `length` is `2``
* `_10access(Mutate | Insert)_10fun insert(key: K, _ value: V): V?`
  
  Inserts the given value of type `V` into the dictionary under the given `key` of type `K`.
  
  The inserted key must have the same type as the dictionary's key type, and the inserted value must have the same type as the dictionary's value type.
  
  Returns the previous value as an optional
  if the dictionary contained the key,
  otherwise `nil`.
  
  Updates the value if the dictionary already contained the key.
  
  This function [mutates](/docs/language/access-control) the dictionary.
  
   `_11// Declare a dictionary mapping strings to integers._11let numbers = {"twentyThree": 23}_11_11// Insert the key `"fortyTwo"` with the value `42` into the dictionary._11// The key did not previously exist in the dictionary,_11// so the result is `nil`_11//_11let old = numbers.insert(key: "fortyTwo", 42)_11_11// `old` is `nil`_11// `numbers` is `{"twentyThree": 23, "fortyTwo": 42}``
* `_10access(Mutate | Remove)_10fun remove(key: K): V?`
  
  Removes the value for the given `key` of type `K` from the dictionary.
  
  Returns the value of type `V` as an optional
  if the dictionary contained the key,
  otherwise `nil`.
  
  This function [mutates](/docs/language/access-control) the dictionary.
  
   `_19// Declare a dictionary mapping strings to integers._19let numbers = {"fortyTwo": 42, "twentyThree": 23}_19_19// Remove the key `"fortyTwo"` from the dictionary._19// The key exists in the dictionary,_19// so the value associated with the key is returned._19//_19let fortyTwo = numbers.remove(key: "fortyTwo")_19_19// `fortyTwo` is `42`_19// `numbers` is `{"twentyThree": 23}`_19_19// Remove the key `"oneHundred"` from the dictionary._19// The key does not exist in the dictionary, so `nil` is returned._19//_19let oneHundred = numbers.remove(key: "oneHundred")_19_19// `oneHundred` is `nil`_19// `numbers` is `{"twentyThree": 23}``
* `_10let keys: [K]`
  
  Returns an array of the keys of type `K` in the dictionary. This does not
  modify the dictionary, just returns a copy of the keys as an array.
  If the dictionary is empty, this returns an empty array. The ordering of the keys is undefined.
  
   `_10// Declare a dictionary mapping strings to integers._10let numbers = {"fortyTwo": 42, "twentyThree": 23}_10_10// Find the keys of the dictionary._10let keys = numbers.keys_10_10// `keys` has type `[String]` and is `["fortyTwo","twentyThree"]``
* `_10let values: [V]`
  
  Returns an array of the values of type `V` in the dictionary. This does not
  modify the dictionary, just returns a copy of the values as an array.
  If the dictionary is empty, this returns an empty array.
  
  This field is not available if `V` is a resource type.
  
   `_10// Declare a dictionary mapping strings to integers._10let numbers = {"fortyTwo": 42, "twentyThree": 23}_10_10// Find the values of the dictionary._10let values = numbers.values_10_10// `values` has type [Int] and is `[42, 23]``
* `_10access(all)_10view fun containsKey(key: K): Bool`
  
  Returns true if the given key of type `K` is in the dictionary.
  
   `_15// Declare a dictionary mapping strings to integers._15let numbers = {"fortyTwo": 42, "twentyThree": 23}_15_15// Check if the dictionary contains the key "twentyFive"._15let containsKeyTwentyFive = numbers.containsKey("twentyFive")_15// `containsKeyTwentyFive` is `false`_15_15// Check if the dictionary contains the key "fortyTwo"._15let containsKeyFortyTwo = numbers.containsKey("fortyTwo")_15// `containsKeyFortyTwo` is `true`_15_15// Invalid: Check if the dictionary contains the key 42._15// This results in a type error, as the key type of the dictionary is `String`._15//_15let containsKey42 = numbers.containsKey(42)`
* `_10access(all)_10fun forEachKey(_ function: fun(K): Bool): Void`
  
  Iterate through all the keys in the dictionary, exiting early if the passed function returns false.
  This is more efficient than calling `.keys` and iterating over the resulting array, since an intermediate allocation is avoided.
  The order of key iteration is undefined, similar to `.keys`.
  
   `_18// Take in a targetKey to look for, and a dictionary to iterate through._18fun myContainsKey(targetKey: String, dictionary: {String: Int}) {_18 // Declare an accumulator that we'll capture inside a closure._18 var found = false_18_18 // At each step, `key` will be bound to another key from `dictionary`._18 dictionary.forEachKey(fun (key: String): Bool {_18 found = key == targetKey_18_18 // The returned boolean value, signals whether to continue iterating._18 // This allows for control flow during the iteration process:_18 // true = `continue`_18 // false = `break`_18 return !found_18 })_18_18 return found_18}`

### Dictionary Keys[​](#dictionary-keys "Direct link to Dictionary Keys")

Dictionary keys must be hashable and equatable.

Most of the built-in types, like booleans and integers,
are hashable and equatable, so can be used as keys in dictionaries.

## InclusiveRange[​](#inclusiverange "Direct link to InclusiveRange")

An `InclusiveRange<T: Integer>` value represents a range of numerical values between two integers,
with the start and end numbers included in the range as suggested by the name.

A range value has a `start`, `end` and a `step`, which represents the interval at which the range's values are separated from `start` to `end`.

A range can be created using the `InclusiveRange` constructor, which can take two or three arguments.

In the case where the range is constructed with two arguments, the first argument is the `start` and the second is the `end`.
The `step` is inferred to be either `1` (when `end >= start`) or `-1` (when `end < start`). E.g.

 `_10// start is 1, end is 100, step is 1_10let range: InclusiveRange<UInt> = InclusiveRange(1, 100)`

Optionally a third, labeled, non-zero `step` argument can be provided to specify a step other than `1`. E.g., the following range contains
all odd numbers from 1 to 100:

 `_10// start is 1, end is 100, step is 2_10let range: InclusiveRange<UInt> = InclusiveRange(1, 100, step: 2)`

Note that in this example, even though the specified "end" of the range is 100, the last actual value the range can attain is 99.

If the specified `step` argument would progress the range away from the `end`, the creation will fail. E.g.

 `_10// Throws an error because a step of -2 cannot progress from 1 to 100_10let range: InclusiveRange<Int> = InclusiveRange(1, 100, step: -2)`

A range requires a type annotation when created.

### `InclusiveRange<T>` fields and functions[​](#inclusiveranget-fields-and-functions "Direct link to inclusiveranget-fields-and-functions")

A value of type `InclusiveRange<T>`, where `T` is a number type, has the following fields and functions:

* `_10let start: T`
  
  The start of the range.
  
   `_10// Declare a range of `Int`s_10let range = let r: InclusiveRange<Int> = InclusiveRange(3, 9)_10_10// Get the start of the range_10let start = range.start_10_10// `start` is `3``
* `_10let end: T`
  
  The end of the range.
  
   `_10// Declare a range of `Int`s_10let range: InclusiveRange<Int> = InclusiveRange(3, 9)_10_10// Get the end of the range_10let end = range.end_10_10// `end` is `9``
* `_10let step: T`
  
  The step of the range.
  
   `_15// Declare a range of `Int`s with a `step` of 2_15let rangeWithStep: InclusiveRange<Int> = InclusiveRange(3, 9, step: 2)_15_15// Get the step of the range_15var step = range.step_15_15// `step` is `2`_15_15// Declare a range of `Int`s without an explicit `step`_15let rangeWithStep: InclusiveRange<Int> = InclusiveRange(3, 9)_15_15/ Get the step of the range_15step = rangeWithStep.step_15_15// `step` is implicitly `1``
* `_10access(all)_10view fun contains(_ element: T): Bool`
  
  Returns `true` if the given integer is in the `InclusiveRange` sequence, and `false` otherwise.
  
  Specifically, for some `InclusiveRange` `r` defined with `start`, `step` and `end`, `r.contains(x)` returns true if either:
  
  + `start <= end` and there exists some integer `i >= 0` such that `start + i * step = x` and `x <= end`
  + `start > end` and there exists some integer `i >= 0` such that `start - i * step = x` and `x >= end` `_14// Declare a range of `Int`s with a `step` of 2_14let rangeWithStep: InclusiveRange<Int> = InclusiveRange(3, 9, step: 2)_14_14// `contains` is `true`_14var contains = range.contains(5)_14_14 // `contains` is `true`_14var contains = range.contains(9)_14_14// `contains` is `false`_14contains = range.contains(6)_14_14 // `contains` is `false`_14contains = range.contains(11)`
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types.mdx)[PreviousType Annotations](/docs/language/type-annotations)[NextOperators](/docs/language/operators)
###### Rate this page

😞😐😊

* [Booleans](#booleans)
* [Numeric Literals](#numeric-literals)
* [Integers](#integers)
  + [Integer Functions](#integer-functions)
* [Fixed-Point Numbers](#fixed-point-numbers)
  + [Fixed-Point Number Functions](#fixed-point-number-functions)
* [Minimum and maximum values](#minimum-and-maximum-values)
* [Saturation Arithmetic](#saturation-arithmetic)
* [Floating-Point Numbers](#floating-point-numbers)
* [Addresses](#addresses)
  + [Address Functions](#address-functions)
* [AnyStruct and AnyResource](#anystruct-and-anyresource)
* [Optionals](#optionals)
* [Never](#never)
* [Strings and Characters](#strings-and-characters)
  + [String Fields and Functions](#string-fields-and-functions)
  + [Character Fields and Functions](#character-fields-and-functions)
* [Arrays](#arrays)
  + [Array Types](#array-types)
  + [Array Indexing](#array-indexing)
  + [Array Fields and Functions](#array-fields-and-functions)
* [Dictionaries](#dictionaries)
  + [Dictionary Types](#dictionary-types)
  + [Dictionary Access](#dictionary-access)
  + [Dictionary Fields and Functions](#dictionary-fields-and-functions)
  + [Dictionary Keys](#dictionary-keys)
* [InclusiveRange](#inclusiverange)
  + [`InclusiveRange<T>` fields and functions](#inclusiveranget-fields-and-functions)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

