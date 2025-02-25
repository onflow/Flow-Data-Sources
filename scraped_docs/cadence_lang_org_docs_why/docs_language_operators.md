# Source: https://cadence-lang.org/docs/language/operators

Operators | Cadence



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
* Operators

On this page

# Operators

Operators are special symbols that perform a computation
for one or more values.
They are either unary, binary, or ternary.

* Unary operators perform an operation for a single value.
  The unary operator symbol appears before the value.
* Binary operators operate on two values.
  The binary operator symbol appears between the two values (infix).
* Ternary operators operate on three values.
  The first operator symbol appears between the first and second value,
  the second operator symbol appears between the second and third value (infix).

## Assignment Operator (`=`)[​](#assignment-operator- "Direct link to assignment-operator-")

The binary assignment operator `=` can be used
to assign a new value to a variable.
It is only allowed in a statement and is not allowed in expressions.

`_14

var a = 1

_14

a = 2

_14

// `a` is `2`

_14

_14

_14

var b = 3

_14

var c = 4

_14

_14

// Invalid: The assignment operation cannot be used in an expression.

_14

a = b = c

_14

_14

// Instead, the intended assignment must be written in multiple statements.

_14

b = c

_14

a = b`

Assignments to constants are invalid.

`_10

let a = 1

_10

// Invalid: Assignments are only for variables, not constants.

_10

a = 2`

The left-hand side of the assignment operand must be an identifier.
For arrays and dictionaries, this identifier can be followed
by one or more index or access expressions.

`_10

// Declare an array of integers.

_10

let numbers = [1, 2]

_10

_10

// Change the first element of the array.

_10

//

_10

numbers[0] = 3

_10

_10

// `numbers` is `[3, 2]``

`_10

// Declare an array of arrays of integers.

_10

let arrays = [[1, 2], [3, 4]]

_10

_10

// Change the first element in the second array

_10

//

_10

arrays[1][0] = 5

_10

_10

// `arrays` is `[[1, 2], [5, 4]]``

`_11

let dictionaries = {

_11

true: {1: 2},

_11

false: {3: 4}

_11

}

_11

_11

dictionaries[false][3] = 0

_11

_11

// `dictionaries` is `{

_11

// true: {1: 2},

_11

// false: {3: 0}

_11

//}``

## Move Operator (`<-`)[​](#move-operator-- "Direct link to move-operator--")

The move operator (`<-`) is unique to Cadence and is used to move [resource types](/docs/language/resources) from one location to another. It works similar to the assignment operator (`=`) you're used to from most programming languages, except that the data in the location on the right side of the statement is **destroyed** by the operation.

`_29

// Declare a resource named `SomeResource`, with a variable integer field.

_29

_29

access(all)

_29

resource SomeResource {

_29

_29

access(all)

_29

var value: Int

_29

_29

init(value: Int) {

_29

self.value = value

_29

}

_29

}

_29

_29

// Declare a constant with value of resource type `SomeResource`.

_29

_29

let a: @SomeResource <- create SomeResource(value: 5)

_29

_29

// *Move* the resource value to a new constant.

_29

_29

let b <- a

_29

_29

// Invalid Line Below: Cannot use constant `a` anymore as the resource that it

_29

// referred to was moved to constant `b`.

_29

_29

a.value

_29

_29

// Constant `b` owns the resource.

_29

_29

b.value // equals 5`

## Force-assignment Operator (`<-!`)[​](#force-assignment-operator-- "Direct link to force-assignment-operator--")

The force-assignment operator (`<-!`) assigns a resource-typed value
to an optional-typed variable if the variable is nil.
If the variable being assigned to is non-nil,
the execution of the program aborts.

The force-assignment operator is only used for [resource types](/docs/language/resources).

## Swapping Operator (`<->`)[​](#swapping-operator-- "Direct link to swapping-operator--")

The binary swap operator `<->` can be used
to exchange the values of two variables.
It is only allowed in a statement and is not allowed in expressions.

`_14

var a = 1

_14

var b = 2

_14

a <-> b

_14

// `a` is `2`

_14

// `b` is `1`

_14

_14

var c = 3

_14

_14

// Invalid: The swap operation cannot be used in an expression.

_14

a <-> b <-> c

_14

_14

// Instead, the intended swap must be written in multiple statements.

_14

b <-> c

_14

a <-> b`

Both sides of the swap operation must be variable,
assignment to constants is invalid.

`_10

var a = 1

_10

let b = 2

_10

_10

// Invalid: Swapping is only possible for variables, not constants.

_10

a <-> b`

Both sides of the swap operation must be an identifier,
followed by one or more index or access expressions.

## Arithmetic Operators[​](#arithmetic-operators "Direct link to Arithmetic Operators")

The unary pefix operator `-` negates an integer:

`_10

let a = 1

_10

-a // is `-1``

There are four binary arithmetic operators:

* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Remainder: `%`

`_10

let a = 1 + 2

_10

// `a` is `3``

The arguments for the operators need to be of the same type.
The result is always the same type as the arguments.

The division and remainder operators abort the program when the divisor is zero.

Arithmetic operations on the signed integer types
`Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`,
and on the unsigned integer types
`UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`,
do not cause values to overflow or underflow.

`_10

let a: UInt8 = 255

_10

_10

// Run-time error: The result `256` does not fit in the range of `UInt8`,

_10

// thus a fatal overflow error is raised and the program aborts

_10

//

_10

let b = a + 1`

`_10

let a: Int8 = 100

_10

let b: Int8 = 100

_10

_10

// Run-time error: The result `10000` does not fit in the range of `Int8`,

_10

// thus a fatal overflow error is raised and the program aborts

_10

//

_10

let c = a * b`

`_10

let a: Int8 = -128

_10

_10

// Run-time error: The result `128` does not fit in the range of `Int8`,

_10

// thus a fatal overflow error is raised and the program aborts

_10

//

_10

let b = -a`

Arithmetic operations on the unsigned integer types
`Word8`, `Word16`, `Word32`, `Word64`
may cause values to overflow or underflow.

For example, the maximum value of an unsigned 8-bit integer is 255 (binary 11111111).
Adding 1 results in an overflow, truncation to 8 bits, and the value 0.

`_10

// 11111111 = 255

_10

// + 1

_10

// = 100000000 = 0`

`_10

let a: Word8 = 255

_10

a + 1 // is `0``

Similarly, for the minimum value 0,
subtracting 1 wraps around and results in the maximum value 255.

`_10

// 00000000

_10

// - 1

_10

// = 11111111 = 255`

`_10

let b: Word8 = 0

_10

b - 1 // is `255``

### Arithmetics on number super-types[​](#arithmetics-on-number-super-types "Direct link to Arithmetics on number super-types")

Arithmetic operators are not supported for number supertypes
(`Number`, `SignedNumber`, `FixedPoint`, `SignedFixedPoint`, `Integer`, `SignedInteger`),
as they may or may not succeed at run-time.

`_10

let x: Integer = 3 as Int8

_10

let y: Integer = 4 as Int8

_10

_10

let z: Integer = x + y // Static error`

Values of these types need to be cast to the desired type before performing the arithmetic operation.

`_10

let z: Integer = (x as! Int8) + (y as! Int8)`

## Logical Operators[​](#logical-operators "Direct link to Logical Operators")

Logical operators work with the boolean values `true` and `false`.

* Logical NOT: `!a`

  This unary prefix operator logically negates a boolean:

  `_10

  let a = true

  _10

  !a // is `false``
* Logical AND: `a && b`

  `_10

  true && true // is `true`

  _10

  _10

  true && false // is `false`

  _10

  _10

  false && true // is `false`

  _10

  _10

  false && false // is `false``

  If the left-hand side is false, the right-hand side is not evaluated.
* Logical OR: `a || b`

  `_10

  true || true // is `true`

  _10

  _10

  true || false // is `true`

  _10

  _10

  false || true // is `true`

  _10

  _10

  false || false // is `false``

  If the left-hand side is true, the right-hand side is not evaluated.

## Comparison Operators[​](#comparison-operators "Direct link to Comparison Operators")

Comparison operators work with boolean and integer values.

* Equality: `==`, is supported for booleans, numbers, addresses, strings, characters, enums, paths, `Type` values, references, and `Void` values (`()`). Variable-sized arrays, fixed-size arrays, dictionaries, and optionals also support equality tests if their inner types do.

  Both sides of the equality operator may be optional, even of different levels,
  so it is for example possible to compare a non-optional with a double-optional (`??`).

  `_10

  1 == 1 // is `true`

  _10

  _10

  1 == 2 // is `false``

  `_10

  true == true // is `true`

  _10

  _10

  true == false // is `false``

  `_10

  let x: Int? = 1

  _10

  x == nil // is `false``

  `_10

  let x: Int = 1

  _10

  x == nil // is `false``

  `_10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = nil

  _10

  x == y // is `false``

  `_10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = 2

  _10

  x == y // is `true``

  `_10

  // Equality tests of arrays are possible if their inner types are equatable.

  _10

  let xs: [Int] = [1, 2, 3]

  _10

  let ys: [Int] = [1, 2, 3]

  _10

  xs == ys // is `true`

  _10

  _10

  let xss: [[Int]] = [xs, xs, xs]

  _10

  let yss: [[Int]] = [ys, ys, ys]

  _10

  xss == yss // is `true``

  `_10

  // Equality also applies to fixed-size arrays. If their lengths differ, the result is a type error.

  _10

  let xs: [Int; 2] = [1, 2]

  _10

  let ys: [Int; 2] = [0 + 1, 1 + 1]

  _10

  xs == ys // is `true``

  `_10

  // Equality tests of dictionaries are possible if the key and value types are equatable.

  _10

  let d1 = {"abc": 1, "def": 2}

  _10

  let d2 = {"abc": 1, "def": 2}

  _10

  d1 == d2 // is `true`

  _10

  _10

  let d3 = {"abc": {1: {"a": 1000}, 2: {"b": 2000}}, "def": {4: {"c": 1000}, 5: {"d": 2000}}}

  _10

  let d4 = {"abc": {1: {"a": 1000}, 2: {"b": 2000}}, "def": {4: {"c": 1000}, 5: {"d": 2000}}}

  _10

  d3 == d4 // is `true``
* Inequality: `!=`, is supported for booleans, numbers, addresses, strings, characters, enums, paths, `Type` values, references, and `Void` values (`()`).
  Variable-sized arrays, fixed-size arrays, dictionaries, and optionals also support inequality tests if their inner types do.

  Both sides of the inequality operator may be optional, even of different levels,
  so it is for example possible to compare a non-optional with a double-optional (`??`).

  `_10

  1 != 1 // is `false`

  _10

  _10

  1 != 2 // is `true``

  `_10

  true != true // is `false`

  _10

  _10

  true != false // is `true``

  `_10

  let x: Int? = 1

  _10

  x != nil // is `true``

  `_10

  let x: Int = 1

  _10

  x != nil // is `true``

  `_10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = nil

  _10

  x != y // is `true``

  `_10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = 2

  _10

  x != y // is `false``

  `_10

  // Inequality tests of arrays are possible if their inner types are equatable.

  _10

  let xs: [Int] = [1, 2, 3]

  _10

  let ys: [Int] = [4, 5, 6]

  _10

  xs != ys // is `true``

  `_10

  // Inequality also applies to fixed-size arrays. If their lengths differ, the result is a type error.

  _10

  let xs: [Int; 2] = [1, 2]

  _10

  let ys: [Int; 2] = [1, 2]

  _10

  xs != ys // is `false``

  `_10

  // Inequality tests of dictionaries are possible if the key and value types are equatable.

  _10

  let d1 = {"abc": 1, "def": 2}

  _10

  let d2 = {"abc": 1, "def": 500}

  _10

  d1 != d2 // is `true`

  _10

  _10

  let d3 = {"abc": {1: {"a": 1000}, 2: {"b": 2000}}, "def": {4: {"c": 1000}, 5: {"d": 2000}}}

  _10

  let d4 = {"abc": {1: {"a": 1000}, 2: {"b": 2000}}, "def": {4: {"c": 1000}, 5: {"d": 2000}}}

  _10

  d3 != d4 // is `false``
* Less than: `<`, for integers, booleans, characters and strings

  `_23

  1 < 1 // is `false`

  _23

  _23

  1 < 2 // is `true`

  _23

  _23

  2 < 1 // is `false`

  _23

  _23

  false < true // is `true`

  _23

  _23

  true < true // is `false`

  _23

  _23

  "a" < "b" // is `true`

  _23

  _23

  "z" < "a" // is `false`

  _23

  _23

  "a" < "A" // is `false`

  _23

  _23

  "" < "" // is `false`

  _23

  _23

  "" < "a" // is `true`

  _23

  _23

  "az" < "b" // is `true`

  _23

  _23

  "xAB" < "Xab" // is `false``
* Less or equal than: `<=`, for integers, booleans, characters and strings

  `_25

  1 <= 1 // is `true`

  _25

  _25

  1 <= 2 // is `true`

  _25

  _25

  2 <= 1 // is `false`

  _25

  _25

  false <= true // is `true`

  _25

  _25

  true <= true // is `true`

  _25

  _25

  true <= false // is `false`

  _25

  _25

  "c" <= "a" // is `false`

  _25

  _25

  "z" <= "z" // is `true`

  _25

  _25

  "a" <= "A" // is `false`

  _25

  _25

  "" <= "" // is `true`

  _25

  _25

  "" <= "a" // is `true`

  _25

  _25

  "az" <= "b" // is `true`

  _25

  _25

  "xAB" <= "Xab" // is `false``
* Greater than: `>`, for integers, booleans, characters and strings

  `_25

  1 > 1 // is `false`

  _25

  _25

  1 > 2 // is `false`

  _25

  _25

  2 > 1 // is `true`

  _25

  _25

  false > true // is `false`

  _25

  _25

  true > true // is `false`

  _25

  _25

  true > false // is `true`

  _25

  _25

  "c" > "a" // is `true`

  _25

  _25

  "g" > "g" // is `false`

  _25

  _25

  "a" > "A" // is `true`

  _25

  _25

  "" > "" // is `false`

  _25

  _25

  "" > "a" // is `false`

  _25

  _25

  "az" > "b" // is `false`

  _25

  _25

  "xAB" > "Xab" // is `true``
* Greater or equal than: `>=`, for integers, booleans, characters and strings

  `_25

  1 >= 1 // is `true`

  _25

  _25

  1 >= 2 // is `false`

  _25

  _25

  2 >= 1 // is `true`

  _25

  _25

  false >= true // is `false`

  _25

  _25

  true >= true // is `true`

  _25

  _25

  true >= false // is `true`

  _25

  _25

  "c" >= "a" // is `true`

  _25

  _25

  "q" >= "q" // is `true`

  _25

  _25

  "a" >= "A" // is `true`

  _25

  _25

  "" >= "" // is `true`

  _25

  _25

  "" >= "a" // is `true`

  _25

  _25

  "az" >= "b" // is `true`

  _25

  _25

  "xAB" >= "Xab" // is `false``

### Comparing number super-types[​](#comparing-number-super-types "Direct link to Comparing number super-types")

Similar to arithmetic operators, comparison operators are also not supported for number supertypes
(`Number`, `SignedNumber` `FixedPoint`, `SignedFixedPoint`, `Integer`, `SignedInteger`),
as they may or may not succeed at run-time.

`_10

let x: Integer = 3 as Int8

_10

let y: Integer = 4 as Int8

_10

_10

let z: Bool = x > y // Static error`

Values of these types need to be cast to the desired type before performing the arithmetic operation.

`_10

let z: Bool = (x as! Int8) > (y as! Int8)`

## Bitwise Operators[​](#bitwise-operators "Direct link to Bitwise Operators")

Bitwise operators enable the manipulation of individual bits of unsigned and signed integers.
They're often used in low-level programming.

* Bitwise AND: `a & b`

  Returns a new integer whose bits are 1 only if the bits were 1 in *both* input integers:

  `_10

  let firstFiveBits = 0b11111000

  _10

  let lastFiveBits = 0b00011111

  _10

  let middleTwoBits = firstFiveBits & lastFiveBits // is 0b00011000`
* Bitwise OR: `a | b`

  Returns a new integer whose bits are 1 only if the bits were 1 in *either* input integers:

  `_10

  let someBits = 0b10110010

  _10

  let moreBits = 0b01011110

  _10

  let combinedbits = someBits | moreBits // is 0b11111110`
* Bitwise XOR: `a ^ b`

  Returns a new integer whose bits are 1 where the input bits are different,
  and are 0 where the input bits are the same:

  `_10

  let firstBits = 0b00010100

  _10

  let otherBits = 0b00000101

  _10

  let outputBits = firstBits ^ otherBits // is 0b00010001`

### Bitwise Shifting Operators[​](#bitwise-shifting-operators "Direct link to Bitwise Shifting Operators")

* Bitwise LEFT SHIFT: `a << b`

  Returns a new integer with all bits moved to the left by a certain number of places.

  `_10

  let someBits = 4 // is 0b00000100

  _10

  let shiftedBits = someBits << 2 // is 0b00010000`
* Bitwise RIGHT SHIFT: `a >> b`

  Returns a new integer with all bits moved to the right by a certain number of places.

  `_10

  let someBits = 8 // is 0b00001000

  _10

  let shiftedBits = someBits >> 2 // is 0b00000010`

For unsigned integers, the bitwise shifting operators perform [logical shifting](https://en.wikipedia.org/wiki/Logical_shift),
for signed integers, they perform [arithmetic shifting](https://en.wikipedia.org/wiki/Arithmetic_shift).
Also note that for `a << b` or `a >> b`, `b` must fit into a 64-bit integer.

## Ternary Conditional Operator[​](#ternary-conditional-operator "Direct link to Ternary Conditional Operator")

There is only one ternary conditional operator, the ternary conditional operator (`a ? b : c`).

It behaves like an if-statement, but is an expression:
If the first operator value is true, the second operator value is returned.
If the first operator value is false, the third value is returned.

The first value must be a boolean (must have the type `Bool`).
The second value and third value can be of any type.
The result type is the least common supertype of the second and third value.

`_10

let x = 1 > 2 ? 3 : 4

_10

// `x` is `4` and has type `Int`

_10

_10

let y = 1 > 2 ? nil : 3

_10

// `y` is `3` and has type `Int?``

## Casting Operators[​](#casting-operators "Direct link to Casting Operators")

### Static Casting Operator (`as`)[​](#static-casting-operator-as "Direct link to static-casting-operator-as")

The static casting operator `as` can be used to statically type cast a value to a type.

If the static type of the value is a subtype of the given type (the "target" type),
the operator returns the value as the given type.

The cast is performed statically, i.e. when the program is type-checked.
Only the static type of the value is considered, not the run-time type of the value.

This means it is not possible to downcast using this operator.
Consider using the [conditional downcasting operator `as?`](#conditional-downcasting-operator-as) instead.

`_22

// Declare a constant named `integer` which has type `Int`.

_22

//

_22

let integer: Int = 1

_22

_22

// Statically cast the value of `integer` to the supertype `Number`.

_22

// The cast succeeds, because the type of the variable `integer`,

_22

// the type `Int`, is a subtype of type `Number`.

_22

// This is an upcast.

_22

//

_22

let number = integer as Number

_22

// `number` is `1` and has type `Number`

_22

_22

// Declare a constant named `something` which has type `AnyStruct`,

_22

// with an initial value which has type `Int`.

_22

//

_22

let something: AnyStruct = 1

_22

_22

// Statically cast the value of `something` to `Int`.

_22

// This is invalid, the cast fails, because the static type of the value is type `AnyStruct`,

_22

// which is not a subtype of type `Int`.

_22

//

_22

let result = something as Int`

### Conditional Downcasting Operator (`as?`)[​](#conditional-downcasting-operator-as "Direct link to conditional-downcasting-operator-as")

The conditional downcasting operator `as?` can be used to dynamically type cast a value to a type.
The operator returns an optional.
If the value has a run-time type that is a subtype of the target type
the operator returns the value as the target type,
otherwise the result is `nil`.

The cast is performed at run-time, i.e. when the program is executed,
not statically, i.e. when the program is checked.

`_17

// Declare a constant named `something` which has type `AnyStruct`,

_17

// with an initial value which has type `Int`.

_17

//

_17

let something: AnyStruct = 1

_17

_17

// Conditionally downcast the value of `something` to `Int`.

_17

// The cast succeeds, because the value has type `Int`.

_17

//

_17

let number = something as? Int

_17

// `number` is `1` and has type `Int?`

_17

_17

// Conditionally downcast the value of `something` to `Bool`.

_17

// The cast fails, because the value has type `Int`,

_17

// and `Bool` is not a subtype of `Int`.

_17

//

_17

let boolean = something as? Bool

_17

// `boolean` is `nil` and has type `Bool?``

Downcasting works for concrete types, but also works e.g. for nested types (e.g. arrays), interfaces, optionals, etc.

`_10

// Declare a constant named `values` which has type `[AnyStruct]`,

_10

// i.e. an array of arbitrarily typed values.

_10

//

_10

let values: [AnyStruct] = [1, true]

_10

_10

let first = values[0] as? Int

_10

// `first` is `1` and has type `Int?`

_10

_10

let second = values[1] as? Bool

_10

// `second` is `true` and has type `Bool?``

### Force-downcasting Operator (`as!`)[​](#force-downcasting-operator-as "Direct link to force-downcasting-operator-as")

The force-downcasting operator `as!` behaves like the
[conditional downcasting operator `as?`](#conditional-downcasting-operator-as).
However, if the cast succeeds, it returns a value of the given type instead of an optional,
and if the cast fails, it aborts the program instead of returning `nil`,

`_17

// Declare a constant named `something` which has type `AnyStruct`,

_17

// with an initial value which has type `Int`.

_17

//

_17

let something: AnyStruct = 1

_17

_17

// Force-downcast the value of `something` to `Int`.

_17

// The cast succeeds, because the value has type `Int`.

_17

//

_17

let number = something as! Int

_17

// `number` is `1` and has type `Int`

_17

_17

// Force-downcast the value of `something` to `Bool`.

_17

// The cast fails, because the value has type `Int`,

_17

// and `Bool` is not a subtype of `Int`.

_17

//

_17

let boolean = something as! Bool

_17

// Run-time error`

## Optional Operators[​](#optional-operators "Direct link to Optional Operators")

### Nil-Coalescing Operator (`??`)[​](#nil-coalescing-operator- "Direct link to nil-coalescing-operator-")

The nil-coalescing operator `??` returns
the value inside an optional if it contains a value,
or returns an alternative value if the optional has no value,
i.e., the optional value is `nil`.

If the left-hand side is non-nil, the right-hand side is not evaluated.

`_10

// Declare a constant which has an optional integer type

_10

//

_10

let a: Int? = nil

_10

_10

// Declare a constant with a non-optional integer type,

_10

// which is initialized to `a` if it is non-nil, or 42 otherwise.

_10

//

_10

let b: Int = a ?? 42

_10

// `b` is 42, as `a` is nil`

The nil-coalescing operator can only be applied
to values which have an optional type.

`_10

// Declare a constant with a non-optional integer type.

_10

//

_10

let a = 1

_10

_10

// Invalid: nil-coalescing operator is applied to a value which has a non-optional type

_10

// (a has the non-optional type `Int`).

_10

//

_10

let b = a ?? 2`

`_10

// Invalid: nil-coalescing operator is applied to a value which has a non-optional type

_10

// (the integer literal is of type `Int`).

_10

//

_10

let c = 1 ?? 2`

The type of the right-hand side of the operator (the alternative value) must be a subtype
of the type of left-hand side, i.e. the right-hand side of the operator must
be the non-optional or optional type matching the type of the left-hand side.

`_11

// Declare a constant with an optional integer type.

_11

//

_11

let a: Int? = nil

_11

let b: Int? = 1

_11

let c = a ?? b

_11

// `c` is `1` and has type `Int?`

_11

_11

// Invalid: nil-coalescing operator is applied to a value of type `Int?`,

_11

// but the alternative has type `Bool`.

_11

//

_11

let d = a ?? false`

### Force Unwrap Operator (`!`)[​](#force-unwrap-operator- "Direct link to force-unwrap-operator-")

The force-unwrap operator (`!`) returns
the value inside an optional if it contains a value,
or panics and aborts the execution if the optional has no value,
i.e., the optional value is `nil`.

`_19

// Declare a constant which has an optional integer type

_19

//

_19

let a: Int? = nil

_19

_19

// Declare a constant with a non-optional integer type,

_19

// which is initialized to `a` if `a` is non-nil.

_19

// If `a` is nil, the program aborts.

_19

//

_19

let b: Int = a!

_19

// The program aborts because `a` is nil.

_19

_19

// Declare another optional integer constant

_19

let c: Int? = 3

_19

_19

// Declare a non-optional integer

_19

// which is initialized to `c` if `c` is non-nil.

_19

// If `c` is nil, the program aborts.

_19

let d: Int = c!

_19

// `d` is initialized to 3 because c isn't nil.`

The force-unwrap operator can only be applied
to values which have an optional type.

`_10

// Declare a constant with a non-optional integer type.

_10

//

_10

let a = 1

_10

_10

// Invalid: force-unwrap operator is applied to a value which has a

_10

// non-optional type (`a` has the non-optional type `Int`).

_10

//

_10

let b = a!`

`_10

// Invalid: The force-unwrap operator is applied

_10

// to a value which has a non-optional type

_10

// (the integer literal is of type `Int`).

_10

//

_10

let c = 1!`

## Precedence and Associativity[​](#precedence-and-associativity "Direct link to Precedence and Associativity")

Operators have the following precedences, highest to lowest:

* Unary precedence: `-`, `!`, `<-`
* Cast precedence: `as`, `as?`, `as!`
* Multiplication precedence: `*`, `/`, `%`
* Addition precedence: `+`, `-`
* Bitwise shift precedence: `<<`, `>>`
* Bitwise conjunction precedence: `&`
* Bitwise exclusive disjunction precedence: `^`
* Bitwise disjunction precedence: `|`
* Nil-Coalescing precedence: `??`
* Relational precedence: `<`, `<=`, `>`, `>=`
* Equality precedence: `==`, `!=`
* Logical conjunction precedence: `&&`
* Logical disjunction precedence: `||`
* Ternary precedence: `? :`

All operators are left-associative, except for the following operators which are right-associative:

* Ternary operator
* Nil-coalescing operator

Expressions can be wrapped in parentheses to override precedence conventions,
i.e. an alternate order should be indicated, or when the default order should be emphasized
e.g. to avoid confusion.
For example, `(2 + 3) * 4` forces addition to precede multiplication,
and `5 + (6 * 7)` reinforces the default order.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators.md)

[Previous

Values and Types](/docs/language/values-and-types)[Next

Functions](/docs/language/functions)

###### Rate this page

😞😐😊

* [Assignment Operator (`=`)](#assignment-operator-)
* [Move Operator (`<-`)](#move-operator--)
* [Force-assignment Operator (`<-!`)](#force-assignment-operator--)
* [Swapping Operator (`<->`)](#swapping-operator--)
* [Arithmetic Operators](#arithmetic-operators)
  + [Arithmetics on number super-types](#arithmetics-on-number-super-types)
* [Logical Operators](#logical-operators)
* [Comparison Operators](#comparison-operators)
  + [Comparing number super-types](#comparing-number-super-types)
* [Bitwise Operators](#bitwise-operators)
  + [Bitwise Shifting Operators](#bitwise-shifting-operators)
* [Ternary Conditional Operator](#ternary-conditional-operator)
* [Casting Operators](#casting-operators)
  + [Static Casting Operator (`as`)](#static-casting-operator-as)
  + [Conditional Downcasting Operator (`as?`)](#conditional-downcasting-operator-as)
  + [Force-downcasting Operator (`as!`)](#force-downcasting-operator-as)
* [Optional Operators](#optional-operators)
  + [Nil-Coalescing Operator (`??`)](#nil-coalescing-operator-)
  + [Force Unwrap Operator (`!`)](#force-unwrap-operator-)
* [Precedence and Associativity](#precedence-and-associativity)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.