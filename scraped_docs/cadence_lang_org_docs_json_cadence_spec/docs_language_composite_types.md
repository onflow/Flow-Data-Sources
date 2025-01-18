# Source: https://cadence-lang.org/docs/language/composite-types




Composite Types | Cadence




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
* Composite Types
On this page
# Composite Types

Composite types allow composing simpler types into more complex types,
i.e., they allow the composition of multiple values into one.
Composite types have a name and consist of zero or more named fields,
and zero or more functions that operate on the data.
Each field may have a different type.

Composite types can only be declared within a [contract](/docs/language/contracts) and nowhere else.

There are two kinds of composite types.
The kinds differ in their usage and the behaviour
when a value is used as the initial value for a constant or variable,
when the value is assigned to a variable,
when the value is passed as an argument to a function,
and when the value is returned from a function:

* [**Structures**](#structures) are **copied**, they are value types.
  
  Structures are useful when copies with independent state are desired.
* [**Resources**](#resources) are **moved**, they are linear types and **must** be used **exactly once**.
  
  Resources are useful when it is desired to model ownership
  (a value exists exactly in one location and it should not be lost).
  
  Certain constructs in a blockchain represent assets of real, tangible value,
  as much as a house or car or bank account.
  We have to worry about literal loss and theft,
  perhaps even on the scale of millions of dollars.
  
  Structures are not an ideal way to represent this ownership because they are copied.
  This would mean that there could be a risk of having multiple copies
  of certain assets floating around,
  which breaks the scarcity requirements needed for these assets to have real value.
  
  A structure is much more useful for representing information
  that can be grouped together in a logical way,
  but doesn't have value or a need to be able to be owned or transferred.
  
  A structure could for example be used to contain the information associated
  with a division of a company,
  but a resource would be used to represent the assets that have been allocated
  to that organization for spending.

Nesting of resources is only allowed within other resource types,
or in data structures like arrays and dictionaries,
but not in structures, as that would allow resources to be copied.

## Composite Type Declaration and Creation[​](#composite-type-declaration-and-creation "Direct link to Composite Type Declaration and Creation")

Structures are declared using the `struct` keyword
and resources are declared using the `resource` keyword.
The keyword is followed by the name.

 `_10access(all)_10struct SomeStruct {_10 // ..._10}_10_10access(all)_10resource SomeResource {_10 // ..._10}`

Structures and resources are types.

Structures are created (instantiated) by calling the type like a function.

 `_10// instantiate a new struct object and assign it to a constant_10let a = SomeStruct()`

The constructor function may require parameters if the [initializer](#composite-type-fields)
of the composite type requires them.

Composite types can only be declared within [contracts](/docs/language/contracts)
and not locally in functions.

Resource must be created (instantiated) by using the `create` keyword
and calling the type like a function.

Resources can only be created in functions and types
that are declared in the same contract in which the resource is declared.

 `_10// instantiate a new resource object and assign it to a constant_10let b <- create SomeResource()`
## Composite Type Fields[​](#composite-type-fields "Direct link to Composite Type Fields")

Fields are declared like variables and constants.
However, the initial values for fields are set in the initializer,
**not** in the field declaration.
All fields **must** be initialized in the initializer, exactly once.

Having to provide initial values in the initializer might seem restrictive,
but this ensures that all fields are always initialized in one location, the initializer,
and the initialization order is clear.

The initialization of all fields is checked statically
and it is invalid to not initialize all fields in the initializer.
Also, it is statically checked that a field is definitely initialized before it is used.

The initializer's main purpose is to initialize fields, though it may also contain other code.
Just like a function, it may declare parameters and may contain arbitrary code.
However, it has no return type, i.e., it is always `Void`.

The initializer is declared using the `init` keyword.

The initializer always follows any fields.

There are two kinds of fields:

* **Constant fields** are also stored in the composite value,
  but after they have been initialized with a value
  they **cannot** have new values assigned to them afterwards.
  A constant field must be initialized exactly once.
  
  Constant fields are declared using the `let` keyword.
* **Variable fields** are stored in the composite value
  and can have new values assigned to them.
  
  Variable fields are declared using the `var` keyword.

| Field Kind | Assignable | Keyword |
| --- | --- | --- |
| **Variable field** | Yes | `var` |
| **Constant field** | **No** | `let` |

In initializers, the special constant `self` refers to the composite value
that is to be initialized.

If a composite type is to be stored, all its field types must be storable. Non-storable types are:

* Functions
* [Accounts (`Account`)](/docs/language/accounts/)
* [Transactions](/docs/language/transactions)
* [References](/docs/language/references): References are ephemeral.
  Consider [storing a capability and borrowing it](/docs/language/capabilities) when needed instead.

Fields can be read (if they are constant or variable) and set (if they are variable),
using the access syntax: the composite value is followed by a dot (`.`)
and the name of the field.

 `_24// Declare a structure named `Token`, which has a constant field_24// named `id` and a variable field named `balance`._24//_24// Both fields are initialized through the initializer._24//_24// The public access modifier `access(all)` is used in this example to allow_24// the fields to be read in outer scopes. Fields can also be declared_24// private so they cannot be accessed in outer scopes._24// Access control will be explained in a later section._24//_24access(all)_24struct Token {_24_24 access(all)_24 let id: Int_24_24 access(all)_24 var balance: Int_24_24 init(id: Int, balance: Int) {_24 self.id = id_24 self.balance = balance_24 }_24}`

Note that it is invalid to provide the initial value for a field in the field declaration.

 `_10access(all)_10struct StructureWithConstantField {_10 // Invalid: It is invalid to provide an initial value in the field declaration._10 // The field must be initialized by setting the initial value in the initializer._10 //_10 access(all)_10 let id: Int = 1_10}`

The field access syntax must be used to access fields – fields are not available as variables.

 `_13access(all)_13struct Token {_13_13 access(all)_13 let id: Int_13_13 init(initialID: Int) {_13 // Invalid: There is no variable with the name `id` available._13 // The field `id` must be initialized by setting `self.id`._13 //_13 id = initialID_13 }_13}`

The initializer is **not** automatically derived from the fields, it must be explicitly declared.

 `_10access(all)_10struct Token {_10_10 access(all)_10 let id: Int_10_10 // Invalid: Missing initializer initializing field `id`._10}`

A composite value can be created by calling the constructor and providing
the field values as arguments.

The value's fields can be accessed on the object after it is created.

 `_11let token = Token(id: 42, balance: 1_000_00)_11_11token.id // is `42`_11token.balance // is `1_000_000`_11_11token.balance = 1_11// `token.balance` is `1`_11_11// Invalid: assignment to constant field_11//_11token.id = 23`

Initializers do not support overloading.

Initializers can also be declared with the `view` keyword, to indicate that they do not perform any mutating operations,
and to allow them to be called from within other `view` functions.
In an initializer, writes to `self` are considered `view` (unlike within other composite functions),
as the value being constructed here is by definition local to the context calling the initializer.

 `_14access(all)_14struct Token {_14_14 access(all)_14 let id: Int_14_14 access(all)_14 var balance: Int_14_14 view init(id: Int, balance: Int) {_14 self.id = id_14 self.balance = balance_14 }_14}`
## Composite Type Functions[​](#composite-type-functions "Direct link to Composite Type Functions")

Composite types may contain functions.
Just like in the initializer, the special constant `self` refers to the composite value
that the function is called on.

 `_31// Declare a structure named "Rectangle", which represents a rectangle_31// and has variable fields for the width and height._31//_31access(all)_31struct Rectangle {_31_31 access(all)_31 var width: Int_31_31 access(all)_31 var height: Int_31_31 init(width: Int, height: Int) {_31 self.width = width_31 self.height = height_31 }_31_31 // Declare a function named "scale", which scales_31 // the rectangle by the given factor._31 //_31 access(all)_31 fun scale(factor: Int) {_31 self.width = self.width * factor_31 self.height = self.height * factor_31 }_31}_31_31let rectangle = Rectangle(width: 2, height: 3)_31rectangle.scale(factor: 4)_31// `rectangle.width` is `8`_31// `rectangle.height` is `12``

Functions do not support overloading.

## Composite Type Subtyping[​](#composite-type-subtyping "Direct link to Composite Type Subtyping")

Two composite types are compatible if and only if they refer to the same declaration by name,
i.e., nominal typing applies instead of structural typing.

Even if two composite types declare the same fields and functions,
the types are only compatible if their names match.

 `_28// Declare a structure named `A` which has a function `test`_28// which has type `fun(): Void`._28//_28struct A {_28 fun test() {}_28}_28_28// Declare a structure named `B` which has a function `test`_28// which has type `fun(): Void`._28//_28struct B {_28 fun test() {}_28}_28_28// Declare a variable named which accepts values of type `A`._28//_28var something: A = A()_28_28// Invalid: Assign a value of type `B` to the variable._28// Even though types `A` and `B` have the same declarations,_28// a function with the same name and type, the types' names differ,_28// so they are not compatible._28//_28something = B()_28_28// Valid: Reassign a new value of type `A`._28//_28something = A()`
## Composite Type Behaviour[​](#composite-type-behaviour "Direct link to Composite Type Behaviour")

### Structures[​](#structures "Direct link to Structures")

Structures are **copied** when
used as an initial value for constant or variable,
when assigned to a different variable,
when passed as an argument to a function,
and when returned from a function.

Accessing a field or calling a function of a structure does not copy it.

 `_30// Declare a structure named `SomeStruct`, with a variable integer field._30//_30access(all)_30struct SomeStruct {_30 _30 access(all)_30 var value: Int_30_30 init(value: Int) {_30 self.value = value_30 }_30_30 fun increment() {_30 self.value = self.value + 1_30 }_30}_30_30// Declare a constant with value of structure type `SomeStruct`._30//_30let a = SomeStruct(value: 0)_30_30// *Copy* the structure value into a new constant._30//_30let b = a_30_30b.value = 1_30// NOTE: `b.value` is 1, `a.value` is *`0`*_30_30b.increment()_30// `b.value` is 2, `a.value` is `0``
### Accessing Fields and Functions of Composite Types Using Optional Chaining[​](#accessing-fields-and-functions-of-composite-types-using-optional-chaining "Direct link to Accessing Fields and Functions of Composite Types Using Optional Chaining")

If a composite type with fields and functions is wrapped in an optional,
optional chaining can be used to get those values or call the function without
having to get the value of the optional first.

Optional chaining is used by adding a `?`
before the `.` access operator for fields or
functions of an optional composite type.

When getting a field value or
calling a function with a return value, the access returns
the value as an optional.
If the object doesn't exist, the value will always be `nil`

When calling a function on an optional like this, if the object doesn't exist,
nothing will happen and the execution will continue.

It is still invalid to access an undeclared field
of an optional composite type.

 `_52// Declare a struct with a field and method._52access(all)_52struct Value {_52_52 access(all)_52 var number: Int_52_52 init() {_52 self.number = 2_52 }_52_52 access(all)_52 fun set(new: Int) {_52 self.number = new_52 }_52_52 access(all)_52 fun setAndReturn(new: Int): Int {_52 self.number = new_52 return new_52 }_52}_52_52// Create a new instance of the struct as an optional_52let value: Value? = Value()_52// Create another optional with the same type, but nil_52let noValue: Value? = nil_52_52// Access the `number` field using optional chaining_52let twoOpt = value?.number_52// Because `value` is an optional, `twoOpt` has type `Int?`_52let two = twoOpt ?? 0_52// `two` is `2`_52_52// Try to access the `number` field of `noValue`, which has type `Value?`._52// This still returns an `Int?`_52let nilValue = noValue?.number_52// This time, since `noValue` is `nil`, `nilValue` will also be `nil`_52_52// Try to call the `set` function of `value`._52// The function call is performed, as `value` is not nil_52value?.set(new: 4)_52_52// Try to call the `set` function of `noValue`._52// The function call is *not* performed, as `noValue` is nil_52noValue?.set(new: 4)_52_52// Call the `setAndReturn` function, which returns an `Int`._52// Because `value` is an optional, the return value is type `Int?`_52let sixOpt = value?.setAndReturn(new: 6)_52let six = sixOpt ?? 0_52// `six` is `6``

This is also possible by using the force-unwrap operator (`!`).

Forced-Optional chaining is used by adding a `!`
before the `.` access operator for fields or
functions of an optional composite type.

When getting a field value or calling a function with a return value,
the access returns the value.
If the object doesn't exist, the execution will panic and revert.

It is still invalid to access an undeclared field
of an optional composite type.

 `_51// Declare a struct with a field and method._51access(all)_51struct Value {_51_51 access(all)_51 var number: Int_51_51 init() {_51 self.number = 2_51 }_51_51 access(all)_51 fun set(new: Int) {_51 self.number = new_51 }_51_51 access(all)_51 fun setAndReturn(new: Int): Int {_51 self.number = new_51 return new_51 }_51}_51_51// Create a new instance of the struct as an optional_51let value: Value? = Value()_51// Create another optional with the same type, but nil_51let noValue: Value? = nil_51_51// Access the `number` field using force-optional chaining_51let two = value!.number_51// `two` is `2`_51_51// Try to access the `number` field of `noValue`, which has type `Value?`_51// Run-time error: This time, since `noValue` is `nil`,_51// the program execution will revert_51let number = noValue!.number_51_51// Call the `set` function of the struct_51_51// This succeeds and sets the value to 4_51value!.set(new: 4)_51_51// Run-time error: Since `noValue` is nil, the value is not set_51// and the program execution reverts._51noValue!.set(new: 4)_51_51// Call the `setAndReturn` function, which returns an `Int`_51// Because we use force-unwrap before calling the function,_51// the return value is type `Int`_51let six = value!.setAndReturn(new: 6)_51// `six` is `6``
### Resources[​](#resources "Direct link to Resources")

Resources are explained in detail [in the following page](/docs/language/resources).

## Unbound References / Nulls[​](#unbound-references--nulls "Direct link to Unbound References / Nulls")

There is **no** support for `null`.

## Inheritance and Abstract Types[​](#inheritance-and-abstract-types "Direct link to Inheritance and Abstract Types")

There is **no** support for inheritance.
Inheritance is a feature common in other programming languages,
that allows including the fields and functions of one type in another type.

Instead, follow the "composition over inheritance" principle,
the idea of composing functionality from multiple individual parts,
rather than building an inheritance tree.

Furthermore, there is also **no** support for abstract types.
An abstract type is a feature common in other programming languages,
that prevents creating values of the type and only
allows the creation of values of a subtype.
In addition, abstract types may declare functions,
but omit the implementation of them
and instead require subtypes to implement them.

Instead, consider using [interfaces](/docs/language/interfaces).

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/composite-types.mdx)[PreviousType Inference](/docs/language/type-inference)[NextResources](/docs/language/resources)
###### Rate this page

😞😐😊

* [Composite Type Declaration and Creation](#composite-type-declaration-and-creation)
* [Composite Type Fields](#composite-type-fields)
* [Composite Type Functions](#composite-type-functions)
* [Composite Type Subtyping](#composite-type-subtyping)
* [Composite Type Behaviour](#composite-type-behaviour)
  + [Structures](#structures)
  + [Accessing Fields and Functions of Composite Types Using Optional Chaining](#accessing-fields-and-functions-of-composite-types-using-optional-chaining)
  + [Resources](#resources)
* [Unbound References / Nulls](#unbound-references--nulls)
* [Inheritance and Abstract Types](#inheritance-and-abstract-types)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

