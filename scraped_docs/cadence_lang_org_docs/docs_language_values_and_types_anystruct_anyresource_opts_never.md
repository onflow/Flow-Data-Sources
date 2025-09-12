# Source: https://cadence-lang.org/docs/language/values-and-types/anystruct-anyresource-opts-never

AnyStruct, AnyResource, Optionals, and Never | Cadence



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
* AnyStruct, AnyResource, Optionals, and Never

On this page

# AnyStruct, AnyResource, Optionals, and Never

`AnyStruct` is the top type of all non-resource types (i.e., all non-resource types are a subtype of it).

`AnyResource` is the top type of all resource types.

`` _37

// Declare a variable that has the type `AnyStruct`.

_37

// Any non-resource typed value can be assigned to it, for example an integer,

_37

// but not resource-typed values.

_37

//

_37

var someStruct: AnyStruct = 1

_37

_37

// Assign a value with a different non-resource type, `Bool`.

_37

someStruct = true

_37

_37

// Declare a structure named `TestStruct`, create an instance of it,

_37

// and assign it to the `AnyStruct`-typed variable

_37

//

_37

struct TestStruct {}

_37

_37

let testStruct = TestStruct()

_37

_37

someStruct = testStruct

_37

_37

// Declare a resource named `TestResource`

_37

_37

resource TestResource {}

_37

_37

// Declare a variable that has the type `AnyResource`.

_37

// Any resource-typed value can be assigned to it,

_37

// but not non-resource typed values.

_37

//

_37

var someResource: @AnyResource <- create TestResource()

_37

_37

// Invalid: Resource-typed values can not be assigned

_37

// to `AnyStruct`-typed variables

_37

//

_37

someStruct <- create TestResource()

_37

_37

// Invalid: Non-resource typed values can not be assigned

_37

// to `AnyResource`-typed variables

_37

//

_37

someResource = 1 ``

However, using `AnyStruct` and `AnyResource` does not allow you to opt out of type checking. It is invalid to access fields and call functions on these types, as they have no fields and functions.

`` _10

// Declare a variable that has the type `AnyStruct`.

_10

// The initial value is an integer,

_10

// but the variable still has the explicit type `AnyStruct`.

_10

//

_10

let a: AnyStruct = 1

_10

_10

// Invalid: Operator cannot be used for an `AnyStruct` value (`a`, left-hand side)

_10

// and an `Int` value (`2`, right-hand side).

_10

//

_10

a + 2 ``

`AnyStruct` and `AnyResource` may be used like other types. For example, they may be the element type of [arrays](/docs/language/values-and-types/arrays) or be the element type of an [optional type](/docs/language/values-and-types/anystruct-anyresource-opts-never#optionals).

`` _13

// Declare a variable that has the type `[AnyStruct]`,

_13

// i.e. an array of elements of any non-resource type.

_13

//

_13

let anyValues: [AnyStruct] = [1, "2", true]

_13

_13

// Declare a variable that has the type `AnyStruct?`,

_13

// i.e. an optional type of any non-resource type.

_13

//

_13

var maybeSomething: AnyStruct? = 42

_13

_13

maybeSomething = "twenty-four"

_13

_13

maybeSomething = nil ``

`AnyStruct` is also the super-type of all non-resource optional types, and `AnyResource` is the super-type of all resource optional types.

`_10

let maybeInt: Int? = 1

_10

let anything: AnyStruct = maybeInt`

[Conditional downcasting](/docs/language/operators/casting-operators#conditional-downcasting-operator-as) allows coercing a value that has the type `AnyStruct` or `AnyResource` back to its original type.

## Optionals[​](#optionals "Direct link to Optionals")

Optionals are values which can represent the absence of a value. Optionals have two cases: either there is a value or there is nothing.

An optional type is declared using the `?` suffix for another type. For example, `Int` is a non-optional integer and `Int?` is an optional integer (i.e., either nothing or an integer).

The value representing nothing is `nil`.

`` _17

// Declare a constant which has an optional integer type,

_17

// with nil as its initial value.

_17

//

_17

let a: Int? = nil

_17

_17

// Declare a constant which has an optional integer type,

_17

// with 42 as its initial value.

_17

//

_17

let b: Int? = 42

_17

_17

// Invalid: `b` has type `Int?`, which does not support arithmetic.

_17

b + 23

_17

_17

// Invalid: Declare a constant with a non-optional integer type `Int`,

_17

// but the initial value is `nil`, which in this context has type `Int?`.

_17

//

_17

let x: Int = nil ``

Optionals can be created for any value, not just for literals.

`` _15

// Declare a constant which has a non-optional integer type,

_15

// with 1 as its initial value.

_15

//

_15

let x = 1

_15

_15

// Declare a constant which has an optional integer type.

_15

// An optional with the value of `x` is created.

_15

//

_15

let y: Int? = x

_15

_15

// Declare a variable which has an optional any type, i.e. the variable

_15

// may be `nil`, or any other value.

_15

// An optional with the value of `x` is created.

_15

//

_15

var z: AnyStruct? = x ``

A non-optional type is a subtype of its optional type.

`` _10

var a: Int? = nil

_10

let b = 2

_10

a = b

_10

_10

// `a` is `2` ``

Optional types may be contained in other types (e.g., [arrays](/docs/language/values-and-types/arrays) or even optionals.)

`_10

// Declare a constant which has an array type of optional integers.

_10

let xs: [Int?] = [1, nil, 2, nil]

_10

_10

// Declare a constant which has a double optional type.

_10

//

_10

let doubleOptional: Int?? = nil`

See the [optional operators](/docs/language/operators/optional-operators) section for information on how to work with optionals.

## Never[​](#never "Direct link to Never")

`Never` is the bottom type (i.e., it is a subtype of all types). There is no value that has type `Never`.

`Never` can be used as the return type for functions that never return normally. For example, it is the return type of the function [`panic`](/docs/language/built-in-functions#panic).

`` _17

// Declare a function named `crashAndBurn` which will never return,

_17

// because it calls the function named `panic`, which never returns.

_17

//

_17

fun crashAndBurn(): Never {

_17

panic("An unrecoverable error occurred")

_17

}

_17

_17

// Invalid: Declare a constant with a `Never` type, but the initial value is an integer.

_17

//

_17

let x: Never = 1

_17

_17

// Invalid: Declare a function which returns an invalid return value `nil`,

_17

// which is not a value of type `Never`.

_17

//

_17

fun returnNever(): Never {

_17

return nil

_17

} ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/anystruct-anyresource-opts-never.md)

[Previous

Addresses and Address Functions](/docs/language/values-and-types/addresses-functions)[Next

Strings and Characters](/docs/language/values-and-types/strings-and-characters)

###### Rate this page

😞😐😊

* [Optionals](#optionals)
* [Never](#never)