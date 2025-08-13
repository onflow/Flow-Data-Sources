# Source: https://cadence-lang.org/docs/language/values-and-types/inclusive-range

InclusiveRange | Cadence



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
* InclusiveRange

On this page

# InclusiveRange

An `InclusiveRange<T: Integer>` value represents a range of numerical values between two integers, with the start and end numbers included in the range as suggested by the name.

A range value has a `start`, `end`, and a `step`, which represents the interval at which the range's values are separated from `start` to `end`.

A range can be created using the `InclusiveRange` constructor, which can take two or three arguments.

In the case where the range is constructed with two arguments, the first argument is the `start` and the second is the `end`. The `step` is inferred to be either `1` (when `end >= start`) or `-1` (when `end < start`). For example:

`_10

// start is 1, end is 100, step is 1

_10

let range: InclusiveRange<UInt> = InclusiveRange(1, 100)`

Optionally a third, labeled, non-zero `step` argument can be provided to specify a step other than `1`. For example, the following range contains all odd numbers from 1 to 100:

`_10

// start is 1, end is 100, step is 2

_10

let range: InclusiveRange<UInt> = InclusiveRange(1, 100, step: 2)`

Note that in this example, even though the specified *end* of the range is 100, the last actual value the range can attain is 99.

If the specified `step` argument would progress the range away from the `end`, the creation will fail. For example:

`_10

// Throws an error because a step of -2 cannot progress from 1 to 100

_10

let range: InclusiveRange<Int> = InclusiveRange(1, 100, step: -2)`

A range requires a type annotation when created.

## InclusiveRange fields and functions[​](#inclusiverange-fields-and-functions "Direct link to InclusiveRange fields and functions")

A value of type `InclusiveRange<T>`, where `T` is a number type, has the following fields and functions:

* `_10

  let start: T`

  The start of the range.

  `` _10

  // Declare a range of `Int`s

  _10

  let range = let r: InclusiveRange<Int> = InclusiveRange(3, 9)

  _10

  _10

  // Get the start of the range

  _10

  let start = range.start

  _10

  _10

  // `start` is `3` ``
* `_10

  let end: T`

  The end of the range.

  `` _10

  // Declare a range of `Int`s

  _10

  let range: InclusiveRange<Int> = InclusiveRange(3, 9)

  _10

  _10

  // Get the end of the range

  _10

  let end = range.end

  _10

  _10

  // `end` is `9` ``
* `_10

  let step: T`

  The step of the range.

  `` _15

  // Declare a range of `Int`s with a `step` of 2

  _15

  let rangeWithStep: InclusiveRange<Int> = InclusiveRange(3, 9, step: 2)

  _15

  _15

  // Get the step of the range

  _15

  var step = range.step

  _15

  _15

  // `step` is `2`

  _15

  _15

  // Declare a range of `Int`s without an explicit `step`

  _15

  let rangeWithStep: InclusiveRange<Int> = InclusiveRange(3, 9)

  _15

  _15

  / Get the step of the range

  _15

  step = rangeWithStep.step

  _15

  _15

  // `step` is implicitly `1` ``
* `_10

  access(all)

  _10

  view fun contains(_ element: T): Bool`

  Returns `true` if the given integer is in the `InclusiveRange` sequence, and `false` otherwise.

  Specifically, for some `InclusiveRange` `r` defined with `start`, `step`, and `end`, `r.contains(x)` returns true if either:

  + `start <= end` and there exists some integer `i >= 0` such that `start + i * step = x` and `x <= end`
  + `start > end` and there exists some integer `i >= 0` such that `start - i * step = x` and `x >= end`

  `` _14

  // Declare a range of `Int`s with a `step` of 2

  _14

  let rangeWithStep: InclusiveRange<Int> = InclusiveRange(3, 9, step: 2)

  _14

  _14

  // `contains` is `true`

  _14

  var contains = range.contains(5)

  _14

  _14

  // `contains` is `true`

  _14

  var contains = range.contains(9)

  _14

  _14

  // `contains` is `false`

  _14

  contains = range.contains(6)

  _14

  _14

  // `contains` is `false`

  _14

  contains = range.contains(11) ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/inclusive-range.md)

[Previous

Dictionaries](/docs/language/values-and-types/dictionaries)[Next

Types and Type System](/docs/language/types-and-type-system/)

###### Rate this page

😞😐😊

* [InclusiveRange fields and functions](#inclusiverange-fields-and-functions)