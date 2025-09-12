# Source: https://cadence-lang.org/docs/language/types-and-type-system/composite-types

Composite Types | Cadence



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
* Composite Types

On this page

# Composite Types

Composite types allow composing simpler types into more complex types. For example, they allow the composition of multiple values into one. Composite types have a name and consist of zero or more named fields and zero or more functions that operate on the data. Each field may have a different type.

Composite types can only be declared within a [contract](/docs/language/contracts) and nowhere else.

There are two kinds of composite types:

* [**Structures**](#structures) are *copied* — they are value types. Structures are useful when copies with an independent state are desired.
* [**Resources**](/docs/language/resources) are *moved* — they are linear types and **must** be used **exactly once**. Resources are useful when it is desired to model ownership (a value exists exactly in one location and it should not be lost).

Each kind differs in its usage and behavior, depending on when the value is:

* used as the initial value for a constant or variable
* assigned to a variable
* passed as an argument to a function, and
* returned from a function.

Certain constructs in a blockchain represent assets of real, tangible value, as much as a house, car, or bank account. We must consider the possiblity of literal loss and theft, perhaps even on the scale of millions of dollars.

Structures are not an ideal way to represent this ownership because they can be copied. This would mean that there could be a risk of having multiple copies of certain assets floating around, which breaks the scarcity requirements needed for these assets to have real value and calls into question who actually owns the property.

A structure is much more useful for representing information that can be grouped together in a logical way, but doesn't have value or a need to be able to be owned or transferred.

A structure could for example be used to contain the information associated with a division of a company, but a resource would be used to represent the assets that have been allocated to that organization for spending.

Nesting of resources is only allowed within other resource types, or in data structures like arrays and dictionaries, but not in structures, as that would allow resources to be copied.

## Composite type declaration and creation[​](#composite-type-declaration-and-creation "Direct link to Composite type declaration and creation")

Structures are declared using the `struct` keyword, and resources are declared using the `resource` keyword. The keyword is followed by the name:

`_10

access(all)

_10

struct SomeStruct {

_10

// ...

_10

}

_10

_10

access(all)

_10

resource SomeResource {

_10

// ...

_10

}`

* Structures and resources are types.
* Structures are created (instantiated) by calling the type like a function.

`_10

// instantiate a new struct object and assign it to a constant

_10

let a = SomeStruct()`

The constructor function may require parameters if the [initializer](#composite-type-fields) of the composite type requires them.

Composite types can only be declared within [contracts](/docs/language/contracts) and not locally in functions.

* A resource must be created (instantiated) by using the `create` keyword and calling the type like a function.
* Resources can only be created in functions and types that are declared in the same contract in which the resource is declared.

`_10

// instantiate a new resource object and assign it to a constant

_10

let b <- create SomeResource()`

## Composite type fields[​](#composite-type-fields "Direct link to Composite type fields")

Fields are declared like variables and constants. However, the initial values for fields are set in the initializer, **not** in the field declaration. All fields **must** be initialized in the initializer, exactly once.

Having to provide initial values in the initializer might seem restrictive, but this ensures that all fields are always initialized in one location, the initializer, and the initialization order is clear.

The initialization of all fields is checked statically and it is invalid to not initialize all fields in the initializer. Also, it is statically checked that a field is definitely initialized before it is used.

The initializer's main purpose is to initialize fields, though it may also contain other code. Just like a function, it may declare parameters and may contain arbitrary code. However, it has no return type (i.e., it is always `Void`).

* The initializer is declared using the `init` keyword.
* The initializer always follows any fields.

There are two kinds of fields:

* **Constant fields** — are also stored in the composite value, but after they have been initialized with a value, they **cannot** have new values assigned to them afterwards. A constant field must be initialized exactly once.

  Constant fields are declared using the `let` keyword.
* **Variable fields** — are stored in the composite value and can have new values assigned to them.

  Variable fields are declared using the `var` keyword.

  | Field Kind | Assignable | Keyword |
  | --- | --- | --- |
  | **Variable field** | Yes | `var` |
  | **Constant field** | **No** | `let` |

In initializers, the special constant `self` refers to the composite value that is to be initialized.

If a composite type is to be stored, all of its field types must be storable. Non-storable types are:

* [Functions](/docs/language/functions)
* [Accounts](/docs/language/accounts/) — `Account`
* [Transactions](/docs/language/transactions)
* [References](/docs/language/references) — References are ephemeral. Consider [storing a capability and borrowing it](/docs/language/capabilities) when needed instead.

Fields can be read (if they are constant or variable) and set (if they are variable), using the access syntax: the composite value is followed by a dot (`.`) and the name of the field.

`` _23

// Declare a structure named `Token`, which has a constant field

_23

// named `id` and a variable field named `balance`.

_23

//

_23

// Both fields are initialized through the initializer.

_23

//

_23

// The public access modifier `access(all)` is used in this example to allow

_23

// the fields to be read in outer scopes. Fields can also be declared

_23

// private so they cannot be accessed in outer scopes.

_23

//

_23

access(all)

_23

struct Token {

_23

_23

access(all)

_23

let id: Int

_23

_23

access(all)

_23

var balance: Int

_23

_23

init(id: Int, balance: Int) {

_23

self.id = id

_23

self.balance = balance

_23

}

_23

} ``

info

It is invalid to provide the initial value for a field in the field declaration.

`_10

access(all)

_10

struct StructureWithConstantField {

_10

// Invalid: It is invalid to provide an initial value in the field declaration.

_10

// The field must be initialized by setting the initial value in the initializer.

_10

//

_10

access(all)

_10

let id: Int = 1

_10

}`

The field access syntax must be used to access fields — fields are not available as variables.

`` _13

access(all)

_13

struct Token {

_13

_13

access(all)

_13

let id: Int

_13

_13

init(initialID: Int) {

_13

// Invalid: There is no variable with the name `id` available.

_13

// The field `id` must be initialized by setting `self.id`.

_13

//

_13

id = initialID

_13

}

_13

} ``

The initializer is **not** automatically derived from the fields. It must be explicitly declared.

`` _10

access(all)

_10

struct Token {

_10

_10

access(all)

_10

let id: Int

_10

_10

// Invalid: Missing initializer initializing field `id`.

_10

} ``

A composite value can be created by calling the constructor and providing the field values as arguments.

The value's fields can be accessed on the object after it is created:

`` _11

let token = Token(id: 42, balance: 1_000_00)

_11

_11

token.id // is `42`

_11

token.balance // is `1_000_000`

_11

_11

token.balance = 1

_11

// `token.balance` is `1`

_11

_11

// Invalid: assignment to constant field

_11

//

_11

token.id = 23 ``

Initializers do not support overloading.

Initializers can also be declared with the `view` keyword to indicate that they do not perform any mutating operations and to allow them to be called from within other `view` functions. In an initializer, writes to `self` are considered `view` (unlike within other composite functions), as the value being constructed here is by definition local to the context calling the initializer:

`_14

access(all)

_14

struct Token {

_14

_14

access(all)

_14

let id: Int

_14

_14

access(all)

_14

var balance: Int

_14

_14

view init(id: Int, balance: Int) {

_14

self.id = id

_14

self.balance = balance

_14

}

_14

}`

## Composite type functions[​](#composite-type-functions "Direct link to Composite type functions")

Composite types may contain functions. Just like in the initializer, the special constant `self` refers to the composite value that the function is called on:

`` _31

// Declare a structure named "Rectangle", which represents a rectangle

_31

// and has variable fields for the width and height.

_31

//

_31

access(all)

_31

struct Rectangle {

_31

_31

access(all)

_31

var width: Int

_31

_31

access(all)

_31

var height: Int

_31

_31

init(width: Int, height: Int) {

_31

self.width = width

_31

self.height = height

_31

}

_31

_31

// Declare a function named "scale", which scales

_31

// the rectangle by the given factor.

_31

//

_31

access(all)

_31

fun scale(factor: Int) {

_31

self.width = self.width * factor

_31

self.height = self.height * factor

_31

}

_31

}

_31

_31

let rectangle = Rectangle(width: 2, height: 3)

_31

rectangle.scale(factor: 4)

_31

// `rectangle.width` is `8`

_31

// `rectangle.height` is `12` ``

Functions do not support overloading.

## Composite type subtyping[​](#composite-type-subtyping "Direct link to Composite type subtyping")

Two composite types are compatible if and only if they refer to the same declaration by name (i.e., nominal typing applies instead of structural typing).

Even if two composite types declare the same fields and functions, the types are only compatible if their names match:

`` _28

// Declare a structure named `A` which has a function `test`

_28

// which has type `fun(): Void`.

_28

//

_28

struct A {

_28

fun test() {}

_28

}

_28

_28

// Declare a structure named `B` which has a function `test`

_28

// which has type `fun(): Void`.

_28

//

_28

struct B {

_28

fun test() {}

_28

}

_28

_28

// Declare a variable named which accepts values of type `A`.

_28

//

_28

var something: A = A()

_28

_28

// Invalid: Assign a value of type `B` to the variable.

_28

// Even though types `A` and `B` have the same declarations,

_28

// a function with the same name and type, the types' names differ,

_28

// so they are not compatible.

_28

//

_28

something = B()

_28

_28

// Valid: Reassign a new value of type `A`.

_28

//

_28

something = A() ``

## Composite type behavior[​](#composite-type-behavior "Direct link to Composite type behavior")

The following describes the behavior of composite types.

### Structures[​](#structures "Direct link to Structures")

Structures are **copied** when they are:

* used as an initial value for a constant or variable
* assigned to a different variable
* passed as an argument to a function, and
* returned from a function.

Accessing a field or calling a function of a structure does not copy it.

`` _30

// Declare a structure named `SomeStruct`, with a variable integer field.

_30

//

_30

access(all)

_30

struct SomeStruct {

_30

_30

access(all)

_30

var value: Int

_30

_30

init(value: Int) {

_30

self.value = value

_30

}

_30

_30

fun increment() {

_30

self.value = self.value + 1

_30

}

_30

}

_30

_30

// Declare a constant with value of structure type `SomeStruct`.

_30

//

_30

let a = SomeStruct(value: 0)

_30

_30

// *Copy* the structure value into a new constant.

_30

//

_30

let b = a

_30

_30

b.value = 1

_30

// NOTE: `b.value` is 1, `a.value` is *`0`*

_30

_30

b.increment()

_30

// `b.value` is 2, `a.value` is `0` ``

### Optional chaining[​](#optional-chaining "Direct link to Optional chaining")

You can access fields and functions of composite types by using optional chaining.

If a composite type with fields and functions is wrapped in an optional, optional chaining can be used to get those values or call the function without having to get the value of the optional first.

Optional chaining is used by adding a `?` before the `.` access operator for fields or functions of an optional composite type.

* When getting a field value or calling a function with a return value, the access returns the value as an optional. If the object doesn't exist, the value will always be `nil`.
* When calling a function on an optional like this, if the object doesn't exist, nothing will happen and the execution will continue.

It is still invalid to access an undeclared field of an optional composite type:

`_22

// Declare a struct with a field and method.

_22

access(all)

_22

struct Value {

_22

_22

access(all)

_22

var number: Int

_22

_22

init() {

_22

self.number = 2

_22

}

_22

_22

access(all)

_22

fun set(new: Int) {

_22

self.number = new

_22

}

_22

_22

access(all)

_22

fun setAndReturn(new: Int): Int {

_22

self.number = new

_22

return new

_22

}

_22

}`

1. Create a new instance of the struct as an optional:

   `_10

   let value: Value? = Value()`
2. Create another optional with the same type, but nil:

   `_10

   let noValue: Value? = nil`
3. Access the `number` field using optional chaining:

   `_10

   let twoOpt = value?.number`

   * Because `value` is an optional, `twoOpt` has type `Int?`:

   `_10

   let two = twoOpt ?? 0`

   * `two` is `2`.
4. Try to access the `number` field of `noValue`, which has type `Value?`. This still returns an `Int?`:

   `_10

   let nilValue = noValue?.number`

   * This time, since `noValue` is `nil`, `nilValue` will also be `nil`.
5. Try to call the `set` function of `value`. The function call is performed, as `value` is not nil:

   `_10

   value?.set(new: 4)`
6. Try to call the `set` function of `noValue`. The function call is *not* performed, as `noValue` is nil:

   `_10

   noValue?.set(new: 4)`
7. Call the `setAndReturn` function, which returns an `Int`. Because `value` is an optional, the return value is type `Int?`:

   `_10

   let sixOpt = value?.setAndReturn(new: 6)

   _10

   let six = sixOpt ?? 0`

   * `six` is `6`.

This is also possible by using the force-unwrap operator (`!`).

Forced-optional chaining is used by adding a `!` before the `.` access operator for fields or functions of an optional composite type.

When getting a field value or calling a function with a return value, the access returns the value. If the object doesn't exist, the execution will panic and revert.

It is still invalid to access an undeclared field of an optional composite type:

`_22

// Declare a struct with a field and method.

_22

access(all)

_22

struct Value {

_22

_22

access(all)

_22

var number: Int

_22

_22

init() {

_22

self.number = 2

_22

}

_22

_22

access(all)

_22

fun set(new: Int) {

_22

self.number = new

_22

}

_22

_22

access(all)

_22

fun setAndReturn(new: Int): Int {

_22

self.number = new

_22

return new

_22

}

_22

}`

1. Create a new instance of the struct as an optional:

   `_10

   let value: Value? = Value()`
2. Create another optional with the same type, but nil:

   `_10

   let noValue: Value? = nil`
3. Access the `number` field using force-optional chaining:

   `_10

   let two = value!.number`

   * `two` is `2`
4. Try to access the `number` field of `noValue`, which has type `Value?`.
   * Run-time error: This time, since `noValue` is `nil`, the program execution will revert.

   `_10

   let number = noValue!.number`
5. Call the `set` function of the struct.

   `_10

   value!.set(new: 4)`

   * This succeeds and sets the value to 4

   `_10

   noValue!.set(new: 4)`

   * Run-time error: Since `noValue` is nil, the value is not set and the program execution reverts.
6. Call the `setAndReturn` function, which returns an `Int`. Because we use force-unwrap before calling the function, the return value is type `Int`:

   `_10

   let six = value!.setAndReturn(new: 6)`

   * `six` is `6`

### Resources[​](#resources "Direct link to Resources")

Resources are explained in detail [in this article](/docs/language/resources).

## Unbound references and nulls[​](#unbound-references-and-nulls "Direct link to Unbound references and nulls")

There is **no** support for `null`.

## Inheritance and abstract types[​](#inheritance-and-abstract-types "Direct link to Inheritance and abstract types")

There is **no** support for inheritance. Inheritance is a feature common in other programming languages, which allows including the fields and functions of one type in another type.

Instead, follow the "composition over inheritance" principle, the idea of composing functionality from multiple individual parts, rather than building an inheritance tree.

Furthermore, there is also **no** support for abstract types. An abstract type is a feature common in other programming languages, that prevents creating values of the type and only allows the creation of values of a subtype. In addition, abstract types may declare functions, but omit the implementation of them and instead require subtypes to implement them.

Instead, consider using [interfaces](/docs/language/interfaces).

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/types-and-type-system/composite-types.mdx)

[Previous

Type Inference](/docs/language/types-and-type-system/type-inference)[Next

Intersection Types](/docs/language/types-and-type-system/intersection-types)

###### Rate this page

😞😐😊

* [Composite type declaration and creation](#composite-type-declaration-and-creation)
* [Composite type fields](#composite-type-fields)
* [Composite type functions](#composite-type-functions)
* [Composite type subtyping](#composite-type-subtyping)
* [Composite type behavior](#composite-type-behavior)
  + [Structures](#structures)
  + [Optional chaining](#optional-chaining)
  + [Resources](#resources)
* [Unbound references and nulls](#unbound-references-and-nulls)
* [Inheritance and abstract types](#inheritance-and-abstract-types)