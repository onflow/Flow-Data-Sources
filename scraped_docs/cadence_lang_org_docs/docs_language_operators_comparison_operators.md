# Source: https://cadence-lang.org/docs/language/operators/comparison-operators

Comparison Operators | Cadence



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

    - [Assignment, Move, Force-Assignment, and Swapping Operators](/docs/language/operators/assign-move-force-swap)
    - [Arithmetic and Logical Operators](/docs/language/operators/arithmetic-logical-operators)
    - [Comparison Operators](/docs/language/operators/comparison-operators)
    - [Bitwise and Ternary Conditional Operators](/docs/language/operators/bitwise-ternary-operators)
    - [Casting Operators](/docs/language/operators/casting-operators)
    - [Optional Operators](/docs/language/operators/optional-operators)
    - [Prescedence and Associativity](/docs/language/operators/prescedence-associativity)
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
* [Operators](/docs/language/operators/)
* Comparison Operators

On this page

# Comparison Operators

Comparison operators work with boolean and integer values.

## Equality `==`[​](#equality- "Direct link to equality-")

* Equality: `==` is supported for booleans, numbers, addresses, strings, characters, enums, paths, `Type` values, references, and `Void` values (`()`). Variable-sized arrays, fixed-size arrays, dictionaries, and optionals also support equality tests if their inner types do.

  Both sides of the equality operator may be optional, even of different levels; for example, it is possible to compare a non-optional with a double-optional (`??`):

  `` _10

  1 == 1 // is `true`

  _10

  _10

  1 == 2 // is `false` ``

  `` _10

  true == true // is `true`

  _10

  _10

  true == false // is `false` ``

  `` _10

  let x: Int? = 1

  _10

  x == nil // is `false` ``

  `` _10

  let x: Int = 1

  _10

  x == nil // is `false` ``

  `` _10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = nil

  _10

  x == y // is `false` ``

  `` _10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = 2

  _10

  x == y // is `true` ``

  `` _10

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

  xss == yss // is `true` ``

  `` _10

  // Equality also applies to fixed-size arrays. If their lengths differ, the result is a type error.

  _10

  let xs: [Int; 2] = [1, 2]

  _10

  let ys: [Int; 2] = [0 + 1, 1 + 1]

  _10

  xs == ys // is `true` ``

  `` _10

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

  d3 == d4 // is `true` ``

## Inequality `!=`[​](#inequality- "Direct link to inequality-")

* Inequality: `!=` is supported for booleans, numbers, addresses, strings, characters, enums, paths, `Type` values, references, and `Void` values (`()`). Variable-sized arrays, fixed-size arrays, dictionaries, and optionals also support inequality tests if their inner types do.

  Both sides of the inequality operator may be optional, even of different levels; for example, it is possible to compare a non-optional with a double-optional (`??`):

  `` _10

  1 != 1 // is `false`

  _10

  _10

  1 != 2 // is `true` ``

  `` _10

  true != true // is `false`

  _10

  _10

  true != false // is `true` ``

  `` _10

  let x: Int? = 1

  _10

  x != nil // is `true` ``

  `` _10

  let x: Int = 1

  _10

  x != nil // is `true` ``

  `` _10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = nil

  _10

  x != y // is `true` ``

  `` _10

  // Comparisons of different levels of optionals are possible.

  _10

  let x: Int? = 2

  _10

  let y: Int?? = 2

  _10

  x != y // is `false` ``

  `` _10

  // Inequality tests of arrays are possible if their inner types are equatable.

  _10

  let xs: [Int] = [1, 2, 3]

  _10

  let ys: [Int] = [4, 5, 6]

  _10

  xs != ys // is `true` ``

  `` _10

  // Inequality also applies to fixed-size arrays. If their lengths differ, the result is a type error.

  _10

  let xs: [Int; 2] = [1, 2]

  _10

  let ys: [Int; 2] = [1, 2]

  _10

  xs != ys // is `false` ``

  `` _10

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

  d3 != d4 // is `false` ``

## Less than `<`[​](#less-than- "Direct link to less-than-")

* Less than: `<` is supported for integers, booleans, characters, and strings:

  `` _23

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

  "xAB" < "Xab" // is `false` ``

## Less or equal than `<=`[​](#less-or-equal-than- "Direct link to less-or-equal-than-")

* Less or equal than: `<=` is supported for integers, booleans, characters, and strings:

  `` _25

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

  "xAB" <= "Xab" // is `false` ``

## Greater than `>`[​](#greater-than- "Direct link to greater-than-")

* Greater than: `>` is supported for integers, booleans, characters, and strings:

  `` _25

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

  "xAB" > "Xab" // is `true` ``

## Greater or equal than `>=`[​](#greater-or-equal-than- "Direct link to greater-or-equal-than-")

* Greater or equal than: `>=` is supported for integers, booleans, characters, and strings:

  `` _25

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

  "xAB" >= "Xab" // is `false` ``

### Comparing number super-types[​](#comparing-number-super-types "Direct link to Comparing number super-types")

Similar to arithmetic operators, comparison operators are also not supported for number supertypes (`Number`, `SignedNumber` `FixedPoint`, `SignedFixedPoint`, `Integer`, and `SignedInteger`), as they may or may not succeed at run-time:

`_10

let x: Integer = 3 as Int8

_10

let y: Integer = 4 as Int8

_10

_10

let z: Bool = x > y // Static error`

Values of these types must be cast to the desired type before performing the arithmetic operation:

`_10

let z: Bool = (x as! Int8) > (y as! Int8)`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/comparison-operators.md)

[Previous

Arithmetic and Logical Operators](/docs/language/operators/arithmetic-logical-operators)[Next

Bitwise and Ternary Conditional Operators](/docs/language/operators/bitwise-ternary-operators)

###### Rate this page

😞😐😊

* [Equality `==`](#equality-)
* [Inequality `!=`](#inequality-)
* [Less than `<`](#less-than-)
* [Less or equal than `<=`](#less-or-equal-than-)
* [Greater than `>`](#greater-than-)
* [Greater or equal than `>=`](#greater-or-equal-than-)
  + [Comparing number super-types](#comparing-number-super-types)