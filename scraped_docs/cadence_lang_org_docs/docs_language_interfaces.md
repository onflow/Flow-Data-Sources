# Source: https://cadence-lang.org/docs/language/interfaces

Interfaces | Cadence



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
* Interfaces

On this page

# Interfaces

An interface is an abstract type that specifies the behavior of types that **implement** the interface. Interfaces declare the required functions and fields, the access control for those declarations, and [pre-conditions and post-conditions](/docs/language/pre-and-post-conditions) that implementing types need to provide.

There are three kinds of interfaces:

* **Structure interfaces** — implemented by [structures](/docs/language/types-and-type-system/composite-types#structures)
* **Resource interfaces** — implemented by [resources](/docs/language/types-and-type-system/composite-types#resources)
* **Contract interfaces** — implemented by [contracts](/docs/language/contracts)

Structure, resource, and contract types may implement multiple interfaces.

There is no support for event and enum interfaces.

Nominal typing applies to composite types that implement interfaces. This means that a type only implements an interface if it has explicitly declared the conformance; the composite type does not implicitly conform to an interface, even if it satisfies all requirements of the interface.

Interfaces consist of the function and field requirements that a type implementing the interface must provide implementations for. Interface requirements, and therefore also their implementations, must always be at least public.

Variable field requirements may be annotated to require them to be publicly settable.

Function requirements consist of the name of the function, parameter types, an optional return type, and optional [pre-conditions and post-conditions](/docs/language/pre-and-post-conditions).

Field requirements consist of the name and the type of the field. Field requirements may optionally declare a *getter* requirement and a *setter* requirement, each with pre-conditions and post-conditions.

Calling functions with pre-conditions and post-conditions on interfaces instead of concrete implementations can improve the security of a program, as it ensures that even if implementations change, some aspects of them will always hold.

## Interface declaration[​](#interface-declaration "Direct link to Interface declaration")

Interfaces are declared using the `struct`, `resource`, or `contract` keyword, followed by the `interface` keyword, the name of the interface, and the requirements, which must be enclosed in opening and closing braces.

Field requirements can be annotated to:

* require the implementation to be a variable field by using the `var` keyword;
* require the implementation to be a constant field by using the `let` keyword;
* or, the field requirement may specify nothing, in which case the implementation may either be a variable or a constant field.

Field requirements and function requirements must specify the required level of access. The access must be at least public, so the `access(all)` keyword must be provided.

Interfaces can be used in types. This is explained in detail in [Interfaces in types](#interfaces-in-types). For now, the syntax `{I}` can be read as the type of any value that implements the interface `I`.

Declare a resource interface for a fungible token. Only resources can implement this resource interface:

`` _78

access(all)

_78

resource interface FungibleToken {

_78

_78

// Require the implementing type to provide a field for the balance

_78

// that is readable in all scopes (`access(all)`).

_78

//

_78

// Neither the `var` keyword nor the `let` keyword is used,

_78

// so the field may be implemented as either a variable

_78

// or as a constant field.

_78

//

_78

access(all)

_78

balance: Int

_78

_78

// Require the implementing type to provide an initializer that

_78

// given the initial balance, must initialize the balance field.

_78

//

_78

init(balance: Int) {

_78

pre {

_78

balance >= 0:

_78

"Balances are always non-negative"

_78

}

_78

post {

_78

self.balance == balance:

_78

"the balance must be initialized to the initial balance"

_78

}

_78

_78

// NOTE: The declaration contains no implementation code.

_78

}

_78

_78

// Require the implementing type to provide a function that is

_78

// callable in all scopes, which withdraws an amount from

_78

// this fungible token and returns the withdrawn amount as

_78

// a new fungible token.

_78

//

_78

// The given amount must be positive, and the function implementation

_78

// must add the amount to the balance.

_78

//

_78

// The function must return a new fungible token.

_78

// The type `{FungibleToken}` is the type of any resource

_78

// that implements the resource interface `FungibleToken`.

_78

//

_78

access(all)

_78

fun withdraw(amount: Int): @{FungibleToken} {

_78

pre {

_78

amount > 0:

_78

"the amount must be positive"

_78

amount <= self.balance:

_78

"insufficient funds: the amount must be smaller or equal to the balance"

_78

}

_78

post {

_78

self.balance == before(self.balance) - amount:

_78

"the amount must be deducted from the balance"

_78

}

_78

_78

// NOTE: The declaration contains no implementation code.

_78

}

_78

_78

// Require the implementing type to provide a function that is

_78

// callable in all scopes, which deposits a fungible token

_78

// into this fungible token.

_78

//

_78

// No precondition is required to check the given token's balance

_78

// is positive, as this condition is already ensured by

_78

// the field requirement.

_78

//

_78

// The parameter type `{FungibleToken}` is the type of any resource

_78

// that implements the resource interface `FungibleToken`.

_78

//

_78

access(all)

_78

fun deposit(_ token: @{FungibleToken}) {

_78

post {

_78

self.balance == before(self.balance) + token.balance:

_78

"the amount must be added to the balance"

_78

}

_78

_78

// NOTE: The declaration contains no implementation code.

_78

}

_78

} ``

note

The required initializer and functions do not have any executable code.

Struct and resource interfaces can only be declared directly inside contracts (i.e., not inside of functions). Contract interfaces can only be declared globally and not inside contracts.

## Interface implementation[​](#interface-implementation "Direct link to Interface implementation")

Declaring that a type implements (conforms) to an interface is performed in the type declaration of the composite type (e.g., structure, resource): the kind and the name of the composite type is followed by a colon (`:`) and the name of one or more interfaces that the composite type implements.

This will tell the checker to enforce any requirements from the specified interfaces onto the declared type.

A type implements (conforms to) an interface if it declares the implementation in its signature, provides field declarations for all fields required by the interface, and provides implementations for all functions required by the interface.

The field declarations in the implementing type must match the field requirements in the interface in terms of name, type, and declaration kind (e.g., constant, variable), if given. For example, an interface may require a field with a certain name and type, but leaves it to the implementation what kind the field it is.

The function implementations must match the function requirements in the interface in terms of name, parameter argument labels, parameter types, and the return type.

Declare a resource named `ExampleToken` that implements the `FungibleToken` interface:

`` _69

// It has a variable field named `balance`, which can be written

_69

// by functions of the type, but outer scopes can only read it.

_69

//

_69

access(all)

_69

resource ExampleToken: FungibleToken {

_69

_69

// Implement the required field `balance` for the `FungibleToken` interface.

_69

// The interface does not specify if the field must be variable, constant,

_69

// so in order for this type (`ExampleToken`) to be able to write to the field,

_69

// but limit outer scopes to only read from the field, it is declared variable,

_69

// and only has public access (non-settable).

_69

//

_69

access(all)

_69

var balance: Int

_69

_69

// Implement the required initializer for the `FungibleToken` interface:

_69

// accept an initial balance and initialize the `balance` field.

_69

//

_69

// This implementation satisfies the required postcondition.

_69

//

_69

// NOTE: the postcondition declared in the interface

_69

// does not have to be repeated here in the implementation.

_69

//

_69

init(balance: Int) {

_69

self.balance = balance

_69

}

_69

_69

// Implement the required function named `withdraw` of the interface

_69

// `FungibleToken`, that withdraws an amount from the token's balance.

_69

//

_69

// The function must be public.

_69

//

_69

// This implementation satisfies the required postcondition.

_69

//

_69

// NOTE: neither the precondition nor the postcondition declared

_69

// in the interface have to be repeated here in the implementation.

_69

//

_69

access(all)

_69

fun withdraw(amount: Int): @ExampleToken {

_69

self.balance = self.balance - amount

_69

return create ExampleToken(balance: amount)

_69

}

_69

_69

// Implement the required function named `deposit` of the interface

_69

// `FungibleToken`, that deposits the amount from the given token

_69

// to this token.

_69

//

_69

// The function must be public.

_69

//

_69

// NOTE: the type of the parameter is `{FungibleToken}`,

_69

// i.e., any resource that implements the resource interface `FungibleToken`,

_69

// so any other token — however, we want to ensure that only tokens

_69

// of the same type can be deposited.

_69

//

_69

// This implementation satisfies the required postconditions.

_69

//

_69

// NOTE: neither the precondition nor the postcondition declared

_69

// in the interface have to be repeated here in the implementation.

_69

//

_69

access(all)

_69

fun deposit(_ token: @{FungibleToken}) {

_69

if let exampleToken <- token as? ExampleToken {

_69

self.balance = self.balance + exampleToken.balance

_69

destroy exampleToken

_69

} else {

_69

panic("cannot deposit token which is not an example token")

_69

}

_69

}

_69

} ``

Declare a constant that has type `ExampleToken`, and is initialized with such an example token:

`_10

let token <- create ExampleToken(balance: 100)`

Withdraw 10 units from the token:

`` _13

// The amount satisfies the precondition of the `withdraw` function

_13

// in the `FungibleToken` interface.

_13

//

_13

// Invoking a function of a resource does not destroy the resource,

_13

// so the resource `token` is still valid after the call of `withdraw`.

_13

//

_13

let withdrawn <- token.withdraw(amount: 10)

_13

_13

// The postcondition of the `withdraw` function in the `FungibleToken`

_13

// interface ensured the balance field of the token was updated properly.

_13

//

_13

// `token.balance` is `90`

_13

// `withdrawn.balance` is `10` ``

Deposit the withdrawn token into another one:

`` _13

let receiver: @ExampleToken <- // ...

_13

receiver.deposit(<-withdrawn)

_13

_13

// Run-time error: The precondition of function `withdraw` in interface

_13

// `FungibleToken` fails, the program aborts: the parameter `amount`

_13

// is larger than the field `balance` (100 > 90).

_13

//

_13

token.withdraw(amount: 100)

_13

_13

// Withdrawing tokens so that the balance is zero does not destroy the resource.

_13

// The resource has to be destroyed explicitly.

_13

//

_13

token.withdraw(amount: 90) ``

The access level for variable fields in an implementation may be less restrictive than the interface requires.

For example, an interface may require a field to be at least contract accessible (i.e., the `access(contract)` modifier is used), and an implementation may provide a variable field which is public (the `access(all)` modifier is used):

`` _22

access(all)

_22

struct interface AnInterface {

_22

// Require the implementing type to provide a contract-readable

_22

// field named `a` that has type `Int`. It may be a variable

_22

// or a constant field.

_22

//

_22

access(contract)

_22

a: Int

_22

}

_22

_22

access(all)

_22

struct AnImplementation: AnInterface {

_22

// Declare a public variable field named `a` that has type `Int`.

_22

// This implementation satisfies the requirement for interface `AnInterface`:

_22

//

_22

access(all)

_22

var a: Int

_22

_22

init(a: Int) {

_22

self.a = a

_22

}

_22

} ``

## Interfaces in types[​](#interfaces-in-types "Direct link to Interfaces in types")

Interfaces can be used in types: the type `{I}` is the type of all objects that implement the interface `I`.

This is called an [intersection type](/docs/language/types-and-type-system/intersection-types): only the functionality (members and functions) of the interface can be used when accessing a value of such a type.

Declare an interface named `Shape`:

`_12

// Require implementing types to provide a field which returns the area,

_12

// and a function which scales the shape by a given factor.

_12

//

_12

access(all)

_12

struct interface Shape {

_12

_12

access(all)

_12

fun getArea(): Int

_12

_12

access(all)

_12

fun scale(factor: Int)

_12

}`

Declare a structure named `Square` that implements the `Shape` interface:

`` _32

access(all)

_32

struct Square: Shape {

_32

// In addition to the required fields from the interface,

_32

// the type can also declare additional fields.

_32

//

_32

access(all)

_32

var length: Int

_32

_32

// Provided the field `area`, which is required to conform

_32

// to the interface `Shape`.

_32

//

_32

// Since `area` was not declared as a constant, variable,

_32

// field in the interface, it can be declared.

_32

//

_32

access(all)

_32

fun getArea(): Int {

_32

return self.length * self.length

_32

}

_32

_32

access(all)

_32

init(length: Int) {

_32

self.length = length

_32

}

_32

_32

// Provided the implementation of the function `scale`,

_32

// which is required to conform to the interface `Shape`.

_32

//

_32

access(all)

_32

fun scale(factor: Int) {

_32

self.length = self.length * factor

_32

}

_32

} ``

Declare a structure named `Rectangle` that also implements the `Shape` interface:

`` _32

access(all)

_32

struct Rectangle: Shape {

_32

_32

access(all)

_32

var width: Int

_32

_32

access(all)

_32

var height: Int

_32

_32

// Provided the field `area`, which is required to conform

_32

// to the interface `Shape`.

_32

//

_32

access(all)

_32

fun getArea(): Int {

_32

return self.width * self.height

_32

}

_32

_32

access(all)

_32

init(width: Int, height: Int) {

_32

self.width = width

_32

self.height = height

_32

}

_32

_32

// Provided the implementation of the function `scale`,

_32

// which is required to conform to the interface `Shape`.

_32

//

_32

access(all)

_32

fun scale(factor: Int) {

_32

self.width = self.width * factor

_32

self.height = self.height * factor

_32

}

_32

} ``

Declare a constant that has type `Shape`, which has a value with type `Rectangle`:

`_10

var shape: {Shape} = Rectangle(width: 10, height: 20)`

Values implementing an interface are assignable to variables that have the interface as their type.

Assign a value of type `Square` to the variable `shape` that has type `Shape`:

`` _10

shape = Square(length: 30)

_10

_10

// Invalid: cannot initialize a constant that has type `Rectangle`.

_10

// with a value that has type `Square`.

_10

//

_10

let rectangle: Rectangle = Square(length: 10) ``

Fields declared in an interface can be accessed and functions declared in an interface can be called on values of a type that implements the interface:

Declare a constant which has the type `Shape` and is initialized with a value that has type `Rectangle`:

`` _11

let shape: {Shape} = Rectangle(width: 2, height: 3)

_11

_11

// Access the field `area` declared in the interface `Shape`.

_11

//

_11

shape.area // is `6`

_11

_11

// Call the function `scale` declared in the interface `Shape`.

_11

//

_11

shape.scale(factor: 3)

_11

_11

shape.area // is `54` ``

## Interface nesting[​](#interface-nesting "Direct link to Interface nesting")

🚧 Status

Currently, only contracts and contract interfaces support nested interfaces.

Interfaces can be arbitrarily nested. Declaring an interface inside another does not require implementing types of the outer interface to provide an implementation of the inner interfaces.

Declare a resource interface `OuterInterface`, which declares a nested structure interface named `InnerInterface`:

`` _10

// Resources implementing `OuterInterface` do not need to provide

_10

// an implementation of `InnerInterface`.

_10

//

_10

// Structures may just implement `InnerInterface`.

_10

//

_10

resource interface OuterInterface {

_10

_10

struct interface InnerInterface {}

_10

} ``

Declare a resource named `SomeOuter` that implements the interface `OuterInterface`:

`` _10

// The resource is not required to implement `OuterInterface.InnerInterface`.

_10

//

_10

resource SomeOuter: OuterInterface {} ``

Declare a structure named `SomeInner` that implements `InnerInterface`, which is nested in interface `OuterInterface`:

`_10

struct SomeInner: OuterInterface.InnerInterface {}`

Contract interfaces may also declare [events](/docs/language/events), which also do not require implementing types of the outer interface to *implement* the event. The event can be emitted in the declaring interface, in a condition or in a default implementation of a function.

For example, declare a contract interface:

`` _25

contract interface ContractInterface {

_25

// some event declaration

_25

//

_25

event SomeEvent()

_25

_25

// some function that emits `SomeEvent` when called

_25

//

_25

fun eventEmittingFunction() {

_25

pre {

_25

emit SomeEvent()

_25

}

_25

}

_25

}

_25

_25

// A contract implementing `ContractInterface`

_25

// Note that no declaration of `SomeEvent` is required

_25

//

_25

contract ImplementingContract: ContractInterface {

_25

// implementation of `eventEmittingFunction`;

_25

// this will emit `SomeEvent` when called

_25

//

_25

fun eventEmittingFunction() {

_25

// ...

_25

}

_25

} ``

## Interface default functions[​](#interface-default-functions "Direct link to Interface default functions")

Interfaces can provide default functions: if the concrete type implementing the interface does not provide an implementation for the function required by the interface, then the interface's default function is used in the implementation.

Declare a struct interface `Container`, which declares a default function `getCount`:

`_10

struct interface Container {

_10

_10

let items: [AnyStruct]

_10

_10

fun getCount(): Int {

_10

return self.items.length

_10

}

_10

}`

Declare a concrete struct named `Numbers` that implements the interface `Container`:

`` _13

// The struct does not implement the function `getCount` of the interface `Container`,

_13

// so the default function for `getCount` is used.

_13

//

_13

struct Numbers: Container {

_13

let items: [AnyStruct]

_13

_13

init() {

_13

self.items = []

_13

}

_13

}

_13

_13

let numbers = Numbers()

_13

numbers.getCount() // is 0 ``

Interfaces cannot provide default initializers, and only one conformance may provide a default function.

## Interface inheritance[​](#interface-inheritance "Direct link to Interface inheritance")

An interface can inherit from (conform to) other interfaces of the same kind. For example, a resource interface can inherit from another resource interface, but cannot inherit from a struct interface. When an interface inherits from another, all the fields, functions, and types of the parent interface are implicitly available to the inheriting interface:

`` _12

access(all)

_12

resource interface Receiver {

_12

access(all)

_12

fun deposit(_ something: @AnyResource)

_12

}

_12

_12

// `Vault` interface inherits from `Receiver` interface.

_12

access(all)

_12

resource interface Vault: Receiver {

_12

access(all)

_12

fun withdraw(_ amount: Int): @Vault

_12

} ``

In the example above, `Vault` inherits `Receiver`. Anyone implementing the `Vault` interface would also have to implement the `Receiver` interface.

`` _10

access(all)

_10

resource MyVault: Vault {

_10

_10

// Must implement all the methods coming from both `Vault` and `Receiver` interfaces.

_10

access(all)

_10

fun deposit(_ something: @AnyResource) {}

_10

_10

access(all)

_10

fun withdraw(_ amount: Int): @Vault {}

_10

} ``

### Duplicate interface members[​](#duplicate-interface-members "Direct link to Duplicate interface members")

When an interface implements another interface, it is possible for the two interfaces to have members with the same name.

The following sections describe how these ambiguities are resolved for different scenarios, including:

* Fields
* Functions
* Functions with conditions
* Default functions
* Conditions with default functions
* Types and event definitions

**Fields**

If two fields with identical names have identical types, then it will be valid:

`` _12

access(all)

_12

resource interface Receiver {

_12

access(all)

_12

var id: UInt64

_12

}

_12

_12

access(all)

_12

resource interface Vault: Receiver {

_12

// `id` field has the same type as the `Receiver.id`. Hence, this is valid.

_12

access(all)

_12

var id: UInt64

_12

} ``

Otherwise, interface conformance is not valid:

`` _12

access(all)

_12

resource interface Receiver {

_12

access(all)

_12

var id: Int

_12

}

_12

_12

access(all)

_12

resource interface Vault: Receiver {

_12

// `id` field has a different type than the `Receiver.id`. Hence, this is invalid.

_12

access(all)

_12

var id: UInt64

_12

} ``

**Functions**

If two functions with identical names also have identical signatures, that is valid:

`` _14

access(all)

_14

resource interface Receiver {

_14

access(all)

_14

fun deposit(_ something: @AnyResource)

_14

}

_14

_14

access(all)

_14

resource interface Vault: Receiver {

_14

// `deposit` function has the same signature as the `Receiver.deposit`.

_14

// Also none of them have any default implementations.

_14

// Hence, this is valid.

_14

access(all)

_14

fun deposit(_ something: @AnyResource)

_14

} ``

If the signatures of the two functions are different, then the interface conformance is not valid:

`` _13

access(all)

_13

resource interface Receiver {

_13

access(all)

_13

fun deposit(_ something: @AnyResource)

_13

}

_13

_13

access(all)

_13

resource interface Vault: Receiver {

_13

// Error: `deposit` function has a different signature compared to the `Receiver.deposit`.

_13

// So these two cannot co-exist.

_13

access(all)

_13

fun deposit()

_13

} ``

**Functions with conditions**

If the two functions with identical names and signatures have [pre/post-conditions](/docs/language/pre-and-post-conditions), then it will still be valid. However, the pre/post-conditions are linearized (see [Linearizing conditions](#linearizing-conditions) for more information) to determine the order of the execution of the conditions. Given the pre/post-conditions are `view` only, the order of execution would not have an impact on the conditions:

`` _18

access(all)

_18

resource interface Receiver {

_18

access(all)

_18

fun deposit(_ something: @AnyResource) {

_18

pre{ self.balance > 100 }

_18

}

_18

}

_18

_18

access(all)

_18

resource interface Vault: Receiver {

_18

// `deposit` function has the same signature as the `Receiver.deposit`.

_18

// Having pre/post condition is valid.

_18

// Both conditions would be executed in a pre-determined order.

_18

access(all)

_18

fun deposit(_ something: @AnyResource) {

_18

pre{ self.balance > 50 }

_18

}

_18

} ``

**Default functions**

An interface can provide a default implementation to an inherited function:

`` _14

access(all)

_14

resource interface Receiver {

_14

access(all)

_14

fun log(_ message: String)

_14

}

_14

_14

access(all)

_14

resource interface Vault: Receiver {

_14

// Valid: Provides the implementation for `Receiver.log` method.

_14

access(all)

_14

fun log(_ message: String) {

_14

log(message.append("from Vault"))

_14

}

_14

} ``

However, an interface cannot override an inherited default implementation of a function:

`` _16

access(all)

_16

resource interface Receiver {

_16

access(all)

_16

fun log(_ message: String) {

_16

log(message.append("from Receiver"))

_16

}

_16

}

_16

_16

access(all)

_16

resource interface Vault: Receiver {

_16

// Invalid: Cannot override the `Receiver.log` method.

_16

access(all)

_16

fun log(_ message: String) {

_16

log(message.append("from Vault"))

_16

}

_16

} ``

It is also invalid to have two or more inherited default implementations for an interface:

`_19

access(all)

_19

resource interface Receiver {

_19

access(all)

_19

fun log(_ message: String) {

_19

log(message.append("from Receiver"))

_19

}

_19

}

_19

_19

access(all)

_19

resource interface Provider {

_19

access(all)

_19

fun log(_ message: String) {

_19

log(message.append("from Provider"))

_19

}

_19

}

_19

_19

// Invalid: Two default functions from two interfaces.

_19

access(all)

_19

resource interface Vault: Receiver, Provider {}`

Having said that, there can be situations where the same default function can be available via different inheritance paths:

`` _18

access(all)

_18

resource interface Logger {

_18

access(all)

_18

fun log(_ message: String) {

_18

log(message.append("from Logger"))

_18

}

_18

}

_18

_18

access(all)

_18

resource interface Receiver: Logger {}

_18

_18

access(all)

_18

resource interface Provider: Logger {}

_18

_18

// Valid: `Logger.log()` default function is visible to the `Vault` interface

_18

// via both `Receiver` and `Provider`.

_18

access(all)

_18

resource interface Vault: Receiver, Provider {} ``

In the above example, the `Logger.log()` default function is visible to the `Vault` interface via both `Receiver` and `Provider`. Even though it is available from two different interfaces, they are both referring to the same default implementation. Therefore, the above code is valid.

**Conditions with default functions**

A more complex situation is when a default function is available via one inheritance path and a pre/post-condition is available via another inheritance path:

`_19

access(all)

_19

resource interface Receiver {

_19

access(all)

_19

fun log(_ message: String) {

_19

log(message.append("from Receiver"))

_19

}

_19

}

_19

_19

access(all)

_19

resource interface Provider {

_19

access(all)

_19

fun log(_ message: String) {

_19

pre{ message != "" }

_19

}

_19

}

_19

_19

// Valid: Both the default function and the condition would be available.

_19

access(all)

_19

resource interface Vault: Receiver, Provider {}`

In these situations, all rules applicable for the default functions inheritance as well as condition inheritance would be applied. Thus, the default function coming from the `Receiver` interface, and the condition coming from the `Provider` interface, would be made available for the inherited interface.

**Types and event definitions**

Type and event definitions would also behave similarly to the default functions. Inherited interfaces can override type definitions and event definitions:

`` _19

access(all)

_19

contract interface Token {

_19

access(all)

_19

struct Foo {}

_19

}

_19

_19

access(all)

_19

contract interface NonFungibleToken: Token {

_19

access(all)

_19

struct Foo {}

_19

}

_19

_19

access(all)

_19

contract MyToken: NonFungibleToken {

_19

access(all)

_19

fun test() {

_19

let foo: Foo // This will refer to the `NonFungibleToken.Foo`

_19

}

_19

} ``

If a user needed to access the `Foo` struct coming from the super interface `Token`, then they can access it using the fully qualified name (e.g., `let foo: Token.Foo`).

However, it is not allowed to have two or more inherited type/event definitions with identical names for an interface:

`_16

access(all)

_16

contract interface Token {

_16

access(all)

_16

struct Foo {}

_16

}

_16

_16

access(all)

_16

contract interface Collectible {

_16

access(all)

_16

struct Foo {}

_16

}

_16

_16

// Invalid: Two type definitions with the same name from two interfaces.

_16

access(all)

_16

contract NonFungibleToken: Token, Collectible {

_16

}`

Similar to default functions, there can be situations where the same type/event definition can be available via different inheritance paths:

`` _15

access(all)

_15

contract interface Logger {

_15

access(all)

_15

struct Foo {}

_15

}

_15

_15

access(all)

_15

contract interface Token: Logger {}

_15

_15

access(all)

_15

contract interface Collectible: Logger {}

_15

_15

// Valid: `Logger.Foo` struct is visible to the `NonFungibleToken` interface via both `Token` and `Collectible`.

_15

access(all)

_15

contract interface NonFungibleToken: Token, Collectible {} ``

In the above example, `Logger.Foo` type definition is visible to the `NonFungibleToken` interface via both `Token` and `Collectible`. Even though it is available from two different interfaces, they are both referring to the same type definition. Therefore, the above code is valid.

However, if at least one of the interfaces in the middle of the chain also overrides the type definition `Foo`, then the code becomes invalid, as there are multiple implementations present now, which leads to ambiguity:

`` _21

access(all)

_21

contract interface Logger {

_21

access(all)

_21

struct Foo {}

_21

}

_21

_21

access(all)

_21

contract interface Token: Logger {

_21

access(all)

_21

struct Foo {}

_21

}

_21

_21

access(all)

_21

contract interface Collectible: Logger {}

_21

_21

// Invalid: The default implementation of the `Foo` struct by the `Logger`

_21

// interface is visible to the `NonFungibleToken` via the `Collectible` interface.

_21

// Another implementation of `Foo` struct is visible to the `NonFungibleToken` via the `Token` interface.

_21

// This creates ambiguity.

_21

access(all)

_21

resource interface NonFungibleToken: Token, Provider {} ``

### Linearizing conditions[​](#linearizing-conditions "Direct link to Linearizing conditions")

As mentioned in [Functions with conditions](#duplicate-interface-members), it is required to linearize the function conditions to determine the order in which pre/post-conditions are executed. This is accomplished by linearizing the interfaces, and hence conditions, in a **depth-first pre-ordered manner, without duplicates**.

For example, consider an interface inheritance hierarchy as follows:

`_10

A

_10

/ \

_10

B C

_10

/ \ /

_10

D E

_10

where an edge from A (top) to B (bottom) means A inherits B.`

This would convert to a Cadence implementation similar to:

`_34

struct interface A: B, C {

_34

access(all)

_34

fun test() {

_34

pre { print("A") }

_34

}

_34

}

_34

_34

struct interface B: D, E {

_34

access(all)

_34

fun test() {

_34

pre { print("B") }

_34

}

_34

}

_34

_34

struct interface C: E {

_34

access(all)

_34

fun test() {

_34

pre { print("C") }

_34

}

_34

}

_34

_34

struct interface D {

_34

access(all)

_34

fun test() {

_34

pre { print("D") }

_34

}

_34

}

_34

_34

struct interface E {

_34

access(all)

_34

fun test() {

_34

pre { print("E") }

_34

}

_34

}`

Any concrete type implementing interface `A` would be equivalent to implementing all interfaces from `A` to `E`, linearized:

`_10

struct Foo: A {

_10

access(all)

_10

fun test() {

_10

pre { print("Foo") }

_10

}

_10

}`

The linearized interface order would be: [A, B, D, E, C]. In other words, it's the same as having:

`_10

struct Foo: A, B, D, C, E {

_10

access(all)

_10

fun test() {

_10

pre { print("Foo") }

_10

}

_10

}`

Thus, invoking the `test` method of `Foo` would first invoke the pre-conditions of [A, B, D, E, C], in that particular order, and eventually run the pre-condition of the concrete implementation `Foo`:

`_10

let foo = Foo()

_10

foo.test()`

The above then prints:

`_10

A

_10

B

_10

D

_10

E

_10

C

_10

Foo`

Similarly, for post-conditions, the same linearization of interfaces would be used, and the post-conditions are executed in the reverse order. For example, replacing the `pre` conditions in the above example with `post` conditions with the exact same content would result in an output similar to:

`_10

Foo

_10

C

_10

E

_10

D

_10

B

_10

A`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/interfaces.mdx)

[Previous

Capabilities](/docs/language/capabilities)[Next

Enumerations](/docs/language/enumerations)

###### Rate this page

😞😐😊

* [Interface declaration](#interface-declaration)
* [Interface implementation](#interface-implementation)
* [Interfaces in types](#interfaces-in-types)
* [Interface nesting](#interface-nesting)
* [Interface default functions](#interface-default-functions)
* [Interface inheritance](#interface-inheritance)
  + [Duplicate interface members](#duplicate-interface-members)
  + [Linearizing conditions](#linearizing-conditions)