# Source: https://cadence-lang.org/docs/language/types-and-type-system/type-inference

Type Inference | Cadence



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
  + [Types and Type System](/docs/language/types-and-type-system/)

    - [Type Annotations](/docs/language/types-and-type-system/type-annotations)
    - [Type Safety](/docs/language/types-and-type-system/type-safety)
    - [Type Inference](/docs/language/types-and-type-system/type-inference)
    - [Composite Types](/docs/language/types-and-type-system/composite-types)
    - [Intersection Types](/docs/language/types-and-type-system/intersection-types)
    - [Run-time Types](/docs/language/types-and-type-system/run-time-types)
    - [Type Hierarchy](/docs/language/types-and-type-system/type-hierarchy)
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
* [Types and Type System](/docs/language/types-and-type-system/)
* Type Inference

On this page

# Type Inference

If a variable or constant declaration is not annotated explicitly with a type, the declaration's type is inferred from the initial value.

### Basic literals[​](#basic-literals "Direct link to Basic literals")

Decimal integer literals and hex literals are inferred to type `Int`:

`` _10

let a = 1

_10

// `a` has type `Int`

_10

_10

let b = -45

_10

// `b` has type `Int`

_10

_10

let c = 0x02

_10

// `c` has type `Int` ``

Unsigned fixed-point literals are inferred to type `UFix64`. Signed fixed-point literals are inferred to type `Fix64`:

`` _10

let a = 1.2

_10

// `a` has type `UFix64`

_10

_10

let b = -1.2

_10

// `b` has type `Fix64` ``

Similarly, for other basic literals, the types are inferred in the following manner:

| Literal Kind | Example | Inferred Type (x) |
| --- | --- | --- |
| String literal | `let x = "hello"` | String |
| Boolean literal | `let x = true` | Bool |
| Nil literal | `let x = nil` | Never? |

### Array literals[​](#array-literals "Direct link to Array literals")

Array literals are inferred based on the elements of the literal, and to be variable-size. The inferred element type is the *least common super-type* of all elements:

`` _14

let integers = [1, 2]

_14

// `integers` has type `[Int]`

_14

_14

let int8Array = [Int8(1), Int8(2)]

_14

// `int8Array` has type `[Int8]`

_14

_14

let mixedIntegers = [UInt(65), 6, 275, Int128(13423)]

_14

// `mixedIntegers` has type `[Integer]`

_14

_14

let nilableIntegers = [1, nil, 2, 3, nil]

_14

// `nilableIntegers` has type `[Int?]`

_14

_14

let mixed = [1, true, 2, false]

_14

// `mixed` has type `[AnyStruct]` ``

### Dictionary literals[​](#dictionary-literals "Direct link to Dictionary literals")

Dictionary literals are inferred based on the keys and values of the literal. The inferred type of keys and values is the *least common super-type* of all keys and values, respectively:

`` _20

let booleans = {

_20

1: true,

_20

2: false

_20

}

_20

// `booleans` has type `{Int: Bool}`

_20

_20

let mixed = {

_20

Int8(1): true,

_20

Int64(2): "hello"

_20

}

_20

// `mixed` has type `{Integer: AnyStruct}`

_20

_20

// Invalid: mixed keys

_20

//

_20

let invalidMixed = {

_20

1: true,

_20

false: 2

_20

}

_20

// The least common super-type of the keys is `AnyStruct`.

_20

// But it is not a valid type for dictionary keys. ``

### Ternary expression[​](#ternary-expression "Direct link to Ternary expression")

The ternary expression type is inferred to be the least common super-type of the second and third operands:

`` _10

let a = true ? 1 : 2

_10

// `a` has type `Int`

_10

_10

let b = true ? 1 : nil

_10

// `b` has type `Int?`

_10

_10

let c = true ? 5 : (false ? "hello" : nil)

_10

// `c` has type `AnyStruct` ``

### Functions[​](#functions "Direct link to Functions")

Functions are inferred based on the parameter types and the return type:

`` _10

let add = (a: Int8, b: Int8): Int {

_10

return a + b

_10

}

_10

_10

// `add` has type `fun(Int8, Int8): Int` ``

Type inference is performed for each expression and statement, and not across statements.

## Ambiguities[​](#ambiguities "Direct link to Ambiguities")

There are cases where types cannot be inferred. In these cases, explicit type annotations are required:

`` _10

// Invalid: not possible to infer type based on array literal's elements.

_10

//

_10

let array = []

_10

_10

// Instead, specify the array type and the concrete element type, e.g. `Int`.

_10

//

_10

let array: [Int] = []

_10

_10

// Or, use a simple-cast to annotate the expression with a type.

_10

let array = [] as [Int] ``

`` _11

// Invalid: not possible to infer type based on dictionary literal's keys and values.

_11

//

_11

let dictionary = {}

_11

_11

// Instead, specify the dictionary type and the concrete key

_11

// and value types, e.g. `String` and `Int`.

_11

//

_11

let dictionary: {String: Int} = {}

_11

_11

// Or, use a simple-cast to annotate the expression with a type.

_11

let dictionary = {} as {String: Int} ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/types-and-type-system/type-inference.md)

[Previous

Type Safety](/docs/language/types-and-type-system/type-safety)[Next

Composite Types](/docs/language/types-and-type-system/composite-types)

###### Rate this page

😞😐😊

* [Basic literals](#basic-literals)
* [Array literals](#array-literals)
* [Dictionary literals](#dictionary-literals)
* [Ternary expression](#ternary-expression)
* [Functions](#functions)
* [Ambiguities](#ambiguities)