# Source: https://cadence-lang.org/docs/language/type-inference




Type Inference | Cadence




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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Type Inference
On this page
# Type Inference

If a variable or constant declaration is not annotated explicitly with a type,
the declaration's type is inferred from the initial value.

### Basic Literals[​](#basic-literals "Direct link to Basic Literals")

Decimal integer literals and hex literals are inferred to type `Int`.

 `_10let a = 1_10// `a` has type `Int`_10_10let b = -45_10// `b` has type `Int`_10_10let c = 0x02_10// `c` has type `Int``

Unsigned fixed-point literals are inferred to type `UFix64`.
Signed fixed-point literals are inferred to type `Fix64`.

 `_10let a = 1.2_10// `a` has type `UFix64`_10_10let b = -1.2_10// `b` has type `Fix64``

Similarly, for other basic literals, the types are inferred in the following manner:

| Literal Kind | Example | Inferred Type (x) |
| --- | --- | --- |
| String literal | `let x = "hello"` | String |
| Boolean literal | `let x = true` | Bool |
| Nil literal | `let x = nil` | Never? |

### Array Literals[​](#array-literals "Direct link to Array Literals")

Array literals are inferred based on the elements of the literal, and to be variable-size.
The inferred element type is the *least common super-type* of all elements.

 `_14let integers = [1, 2]_14// `integers` has type `[Int]`_14_14let int8Array = [Int8(1), Int8(2)]_14// `int8Array` has type `[Int8]`_14_14let mixedIntegers = [UInt(65), 6, 275, Int128(13423)]_14// `mixedIntegers` has type `[Integer]`_14_14let nilableIntegers = [1, nil, 2, 3, nil]_14// `nilableIntegers` has type `[Int?]`_14_14let mixed = [1, true, 2, false]_14// `mixed` has type `[AnyStruct]``
### Dictionary Literals[​](#dictionary-literals "Direct link to Dictionary Literals")

Dictionary literals are inferred based on the keys and values of the literal.
The inferred type of keys and values is the *least common super-type* of all keys and values, respectively.

 `_20let booleans = {_20 1: true,_20 2: false_20}_20// `booleans` has type `{Int: Bool}`_20_20let mixed = {_20 Int8(1): true,_20 Int64(2): "hello"_20}_20// `mixed` has type `{Integer: AnyStruct}`_20_20// Invalid: mixed keys_20//_20let invalidMixed = {_20 1: true,_20 false: 2_20}_20// The least common super-type of the keys is `AnyStruct`._20// But it is not a valid type for dictionary keys.`
### Ternary Expression[​](#ternary-expression "Direct link to Ternary Expression")

Ternary expression type is inferred to be the least common super-type of the second and third operands.

 `_10let a = true ? 1 : 2_10// `a` has type `Int`_10_10let b = true ? 1 : nil_10// `b` has type `Int?`_10_10let c = true ? 5 : (false ? "hello" : nil)_10// `c` has type `AnyStruct``
### Functions[​](#functions "Direct link to Functions")

Functions are inferred based on the parameter types and the return type.

 `_10let add = (a: Int8, b: Int8): Int {_10 return a + b_10}_10_10// `add` has type `fun(Int8, Int8): Int``

Type inference is performed for each expression / statement, and not across statements.

## Ambiguities[​](#ambiguities "Direct link to Ambiguities")

There are cases where types cannot be inferred.
In these cases explicit type annotations are required.

 `_10// Invalid: not possible to infer type based on array literal's elements._10//_10let array = []_10_10// Instead, specify the array type and the concrete element type, e.g. `Int`._10//_10let array: [Int] = []_10_10// Or, use a simple-cast to annotate the expression with a type._10let array = [] as [Int]`
 `_11// Invalid: not possible to infer type based on dictionary literal's keys and values._11//_11let dictionary = {}_11_11// Instead, specify the dictionary type and the concrete key_11// and value types, e.g. `String` and `Int`._11//_11let dictionary: {String: Int} = {}_11_11// Or, use a simple-cast to annotate the expression with a type._11let dictionary = {} as {String: Int}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/type-inference.md)[PreviousType Safety](/docs/language/type-safety)[NextComposite Types](/docs/language/composite-types)
###### Rate this page

😞😐😊

* [Basic Literals](#basic-literals)
* [Array Literals](#array-literals)
* [Dictionary Literals](#dictionary-literals)
* [Ternary Expression](#ternary-expression)
* [Functions](#functions)
* [Ambiguities](#ambiguities)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

