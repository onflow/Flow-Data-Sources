# Source: https://cadence-lang.org/docs/language/glossary

Glossary | Cadence



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
* Glossary

On this page

# Glossary

This glossary provides clear explanations and code examples for the most important symbols and operators in Cadence. Each entry describes the symbol's purpose, usage, and common scenarios, helping both new and experienced developers quickly understand Cadence syntax.

Use this guide as a handy reference to navigate Cadence's unique features and operator behaviors.

tip

To search for a term, press `CTRL`/`⌘` + `F` and type in the symbol or operator you want to look up.

## `&` (ampersand)[​](#-ampersand "Direct link to -ampersand")

The `&` (ampersand) symbol has several uses.

### Reference[​](#reference "Direct link to Reference")

If an expression starts with the `&` (ampersand) symbol, it creates a [reference](/docs/language/references).

`_10

let a: String = "hello"

_10

let refOfA: &String = &a as &String`

References may also be authorized if the `&` symbol is preceded by `auth`. Otherwise, the reference is unauthorized.

Authorized references have the `auth` modifier, along with the set of entitlements to which the reference is authorized (i.e., the full syntax is `auth(E, F) &T`, whereas unauthorized references do not have a modifier).

`_10

let a: String = "hello"

_10

let refOfA: auth(X) &String = &a as auth(X) &String`

### Logical operator[​](#logical-operator "Direct link to Logical operator")

The `&` (ampersand) symbol can be also used as a [logical operator (AND)](/docs/language/operators/arithmetic-logical-operators#logical-operators), by appearing twice in succession (i.e., `&&`):

`_10

let a = true

_10

let b = false

_10

_10

let c = a && b // false`

## `@` (at)[​](#-at "Direct link to -at")

The `@` (at) symbol before a type is used to annotate whether the type is a [resource](/docs/language/resources).

The `@` symbol must appear at the beginning of the type, not inside. For example, an array of `NFT`s is `@[NFT]`, not `[@NFT]`. This emphasizes that the whole type acts like a resource.

`` _20

// Declare a resource named `SomeResource`

_20

access(all)

_20

resource SomeResource {

_20

_20

access(all)

_20

var value: Int

_20

_20

init(value: Int) {

_20

self.value = value

_20

}

_20

}

_20

_20

// we use the '@' symbol to reference a resource type

_20

let a: @SomeResource <- create SomeResource(value: 0)

_20

_20

// also in function declarations

_20

access(all)

_20

fun use(resource: @SomeResource) {

_20

destroy resource

_20

} ``

## `:` (colon)[​](#-colon "Direct link to -colon")

The `:` (colon) symbol has several uses.

### Type declaration[​](#type-declaration "Direct link to Type declaration")

If a `:` (colon) follows a variable/constant/function declaration, it is used to declare its type.

`` _10

let a: Bool = true // declares variable `a` with type `Bool`

_10

_10

// or

_10

_10

fun addOne(x: Int): Int { // return type of Int

_10

return x + 1

_10

} ``

### Ternary conditional operator[​](#ternary-conditional-operator "Direct link to Ternary conditional operator")

The `:` (colon) can also be used in [ternary operations](/docs/language/operators/bitwise-ternary-operators#ternary-conditional-operator) to represent the "otherwise" section, such as the following:

`_10

let a = 1 > 2 ? 3 : 4

_10

// should be read as:

_10

// "is 1 greater than 2?"

_10

// "if YES, then set a = 3,

_10

// "otherwise, set a = 4.`

## `=` (equals)[​](#-equals "Direct link to -equals")

The `=` (equals) symbol has several uses.

### Variable declaration[​](#variable-declaration "Direct link to Variable declaration")

`` _10

let a = 1 // declares a variable `a` with value `1` ``

### Assignment[​](#assignment "Direct link to Assignment")

`` _10

a = 1 // assigns the value `1` to variable `a ` ``

## `!` (exclamation mark)[​](#-exclamation-mark "Direct link to -exclamation-mark")

The `!` (exclamation mark) symbol has a different effect depending on whether it precedes or succeeds a variable.

When it immediately **precedes** a boolean-type variable, it negates it:

`_10

let a: Bool = true

_10

let b: Bool = !a

_10

_10

// b is false`

When it immediately **succeeds** an *optional* variable, it [force unwraps](/docs/language/operators/optional-operators#force-unwrap-operator-) it. Force unwrapping returns the value inside an optional if it contains a value, or panics and aborts the execution if the optional has no value (i.e., the optional value is nil):

`_10

let a: Int? = nil

_10

let b: Int? = 3

_10

_10

let c: Int = a! // panics, because = nil

_10

let d: Int = b! // initialized correctly as 3`

## `/` (forward slash)[​](#-forward-slash "Direct link to -forward-slash")

The `/` (forward slash) symbol has several uses.

### Division operator[​](#division-operator "Direct link to Division operator")

Between two expressions, the forward slash acts as the [division operator](/docs/language/operators/arithmetic-logical-operators#arithmetic-operators):

`_10

let result = 4 / 2`

### Path separator[​](#path-separator "Direct link to Path separator")

In a [path](/docs/language/accounts/paths), the forward slash separates the domain, `storage` or `public`, and the identifier:

`_10

let storagePath = /storage/path

_10

storagePath.toString() // is "/storage/path"`

## `<-` (lower than, hyphen) (Move operator)[​](#--lower-than-hyphen-move-operator "Direct link to --lower-than-hyphen-move-operator")

The [move operator `<-`](/docs/language/resources#the-move-operator--) is like the assignment operator `=`, but must be used when the value is a [resource](/docs/language/resources). To make the assignment of resources explicit, the move operator `<-` must be used when the resource is:

* the initial value of a constant or variable,
* moved to a different variable in an assignment,
* moved to a function as an argument, or
* returned from a function.

`_10

resource R {}

_10

_10

let a <- create R() // we instantiate a new resource and move it into a`

## `<-!` (lower than, hyphen, exclamation mark) (Force-assignment move operator)[​](#--lower-than-hyphen-exclamation-mark-force-assignment-move-operator "Direct link to --lower-than-hyphen-exclamation-mark-force-assignment-move-operator")

The [force-assignment move operator `<-!`](/docs/language/operators/assign-move-force-swap#force-assignment-operator--) moves a resource value to an optional variable. If the variable is `nil`, the move succeeds. If it is not nil, the program aborts.

`_10

access(all)

_10

resource R {}

_10

_10

var a: @R? <- nil

_10

a <-! create R()`

## `<->` (lower than, hyphen, greater than) (Swap operator)[​](#--lower-than-hyphen-greater-than-swap-operator "Direct link to --lower-than-hyphen-greater-than-swap-operator")

The [swapping operator `<->`](/docs/language/operators/assign-move-force-swap#swapping-operator--) swaps two resources between the variables to the left and right of it.

## `+` (plus), `-` (minus), `*` (asterisk), `%` (percentage sign)[​](#-plus---minus--asterisk--percentage-sign "Direct link to -plus---minus--asterisk--percentage-sign")

These are all typical [arithmetic operators](/docs/language/operators/arithmetic-logical-operators#arithmetic-operators):

* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Remainder: `%`

## `?` (question mark)[​](#-question-mark "Direct link to -question-mark")

The `?` (question mark) symbol has several uses.

### Optional[​](#optional "Direct link to Optional")

If a `?` (question mark) follows a variable/constant, it represents an optional. An optional can either have a value or *nothing at all*:

`_10

// Declare a constant which has an optional integer type

_10

//

_10

let a: Int? = nil`

### Ternary conditional operator[​](#ternary-conditional-operator-1 "Direct link to Ternary conditional operator")

The `?` (question mark) can also be used in [ternary operations](/docs/language/operators/bitwise-ternary-operators#ternary-conditional-operator) to represent the *then* section, such as the following:

`_10

let a = 1 > 2 ? 3 : 4

_10

// should be read as:

_10

// "is 1 greater than 2?"

_10

// "if YES, then set a = 3,

_10

// "otherwise, set a = 4.`

### Nil-coalescing operator[​](#nil-coalescing-operator "Direct link to Nil-coalescing operator")

The `?` (question mark) is also used in the [nil-coalescing operator `??`](/docs/language/operators/optional-operators#nil-coalescing-operator-).

It returns the value inside the optional if the optional contains a value, or returns an alternative value if the optional has no value (i.e., the optional value is nil):

`` _15

// Declare a constant which has an optional integer type

_15

//

_15

let a: Int? = nil

_15

_15

// Declare a constant with a non-optional integer type,

_15

// which is initialized to `a` if it is non-nil, or 42 otherwise.

_15

//

_15

let b: Int = a ?? 42

_15

// `b` is 42, as `a` is nil

_15

_15

_15

// Invalid: nil-coalescing operator is applied to a value which has a non-optional type

_15

// (the integer literal is of type `Int`).

_15

//

_15

let c = 1 ?? 2 ``

## `_` (underscore)[​](#_-underscore "Direct link to _-underscore")

The `_` (underscore) symbol has several uses.

### Names[​](#names "Direct link to Names")

The `_` (underscore) can be used in names (e.g., in variables and types):

`_10

let _a = true // used as a variable name

_10

let another_one = false`

### Number literals[​](#number-literals "Direct link to Number literals")

The `_` (underscore) can also be used to split up numerical components:

`_10

let b = 100_000_000 // used to split up a number (supports all number types, e.g. 0b10_11_01)`

### Argument labels[​](#argument-labels "Direct link to Argument labels")

The `_` (underscore) can also be used to indicate that a parameter in a [function](/docs/language/functions) has no argument label:

`_10

// The special argument label _ is specified for the parameter,

_10

// so no argument label has to be provided in a function call.

_10

_10

fun double(_ x: Int): Int {

_10

return x * 2

_10

}

_10

_10

let result = double(4)`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/glossary.mdx)

[Previous

Crypto](/docs/language/crypto)[Next

Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)

###### Rate this page

😞😐😊

* [`&` (ampersand)](#-ampersand)
  + [Reference](#reference)
  + [Logical operator](#logical-operator)
* [`@` (at)](#-at)
* [`:` (colon)](#-colon)
  + [Type declaration](#type-declaration)
  + [Ternary conditional operator](#ternary-conditional-operator)
* [`=` (equals)](#-equals)
  + [Variable declaration](#variable-declaration)
  + [Assignment](#assignment)
* [`!` (exclamation mark)](#-exclamation-mark)
* [`/` (forward slash)](#-forward-slash)
  + [Division operator](#division-operator)
  + [Path separator](#path-separator)
* [`<-` (lower than, hyphen) (Move operator)](#--lower-than-hyphen-move-operator)
* [`<-!` (lower than, hyphen, exclamation mark) (Force-assignment move operator)](#--lower-than-hyphen-exclamation-mark-force-assignment-move-operator)
* [`<->` (lower than, hyphen, greater than) (Swap operator)](#--lower-than-hyphen-greater-than-swap-operator)
* [`+` (plus), `-` (minus), `*` (asterisk), `%` (percentage sign)](#-plus---minus--asterisk--percentage-sign)
* [`?` (question mark)](#-question-mark)
  + [Optional](#optional)
  + [Ternary conditional operator](#ternary-conditional-operator-1)
  + [Nil-coalescing operator](#nil-coalescing-operator)
* [`_` (underscore)](#_-underscore)
  + [Names](#names)
  + [Number literals](#number-literals)
  + [Argument labels](#argument-labels)