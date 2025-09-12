# Source: https://cadence-lang.org/docs/language/operators/assign-move-force-swap

Assignment, Move, Force-Assignment, and Swapping Operators | Cadence



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
* Assignment, Move, Force-Assignment, and Swapping Operators

On this page

# Assignment, Move, Force-Assignment, and Swapping Operators

## Assignment operator (`=`)[​](#assignment-operator- "Direct link to assignment-operator-")

The binary assignment operator `=` can be used to assign a new value to a variable. It is only allowed in a statement and is not allowed in expressions:

`` _14

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

a = b ``

Assignments to constants are invalid.

`_10

let a = 1

_10

// Invalid: Assignments are only for variables, not constants.

_10

a = 2`

The left-hand side of the assignment operand must be an identifier. For arrays and dictionaries, this identifier can be followed by one or more index or access expressions.

`` _10

// Declare an array of integers.

_10

let numbers = [1, 2]

_10

_10

// Change the first element of the array.

_10

numbers[0] = 3

_10

_10

// `numbers` is `[3, 2]` ``

`` _10

// Declare an array of arrays of integers.

_10

let arrays = [[1, 2], [3, 4]]

_10

_10

// Change the first element in the second array

_10

arrays[1][0] = 5

_10

_10

// `arrays` is `[[1, 2], [5, 4]]` ``

`` _11

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

//}` ``

## Move operator (`<-`)[​](#move-operator-- "Direct link to move-operator--")

The move operator (`<-`) is unique to Cadence and is used to move [resource types](/docs/language/resources) from one location to another. It works similar to the assignment operator (`=`) you're used to from most programming languages, except that the data in the location on the right side of the statement is **destroyed** by the operation:

`` _29

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

a.value // Error: a no longer exists

_29

_29

// Constant `b` owns the resource.

_29

_29

b.value // equals 5 ``

## Force-assignment operator (`<-!`)[​](#force-assignment-operator-- "Direct link to force-assignment-operator--")

The force-assignment operator (`<-!`) assigns a resource-typed value to an optional-typed variable if the variable is nil. If the variable being assigned to is non-nil, the execution of the program aborts.

The force-assignment operator is only used for [resource types](/docs/language/resources).

## Swapping operator (`<->`)[​](#swapping-operator-- "Direct link to swapping-operator--")

The binary swap operator `<->` can be used to exchange the values of two variables. It is only allowed in a statement and is not allowed in expressions:

`` _14

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

a <-> b ``

Both sides of the swap operation must be variable, assignment to constants is invalid.

`_10

var a = 1

_10

let b = 2

_10

_10

// Invalid: Swapping is only possible for variables, not constants.

_10

a <-> b`

Both sides of the swap operation must be an identifier, followed by one or more index or access expressions.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/assign-move-force-swap.md)

[Previous

Operators](/docs/language/operators/)[Next

Arithmetic and Logical Operators](/docs/language/operators/arithmetic-logical-operators)

###### Rate this page

😞😐😊

* [Assignment operator (`=`)](#assignment-operator-)
* [Move operator (`<-`)](#move-operator--)
* [Force-assignment operator (`<-!`)](#force-assignment-operator--)
* [Swapping operator (`<->`)](#swapping-operator--)