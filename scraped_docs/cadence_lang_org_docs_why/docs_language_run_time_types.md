# Source: https://cadence-lang.org/docs/language/run-time-types

Run-time Types | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

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
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Language Reference](/docs/language/)
* Run-time Types

On this page

# Run-time Types

Types can be represented at run-time.
To create a type value, use the constructor function `Type<T>()`, which accepts the static type as a type argument.

This is similar to e.g. `T.self` in Swift, `T::class`/`KClass<T>` in Kotlin, and `T.class`/`Class<T>` in Java.

For example, to represent the type `Int` at run-time:

`_10

let intType: Type = Type<Int>()`

This works for both built-in and user-defined types. For example, to get the type value for a resource:

`_10

resource Collectible {}

_10

_10

let collectibleType = Type<@Collectible>()

_10

_10

// `collectibleType` has type `Type``

Type values are comparable.

`_10

_10

Type<Int>() == Type<Int>()

_10

_10

Type<Int>() != Type<String>()`

The method `view fun isSubtype(of: Type): Bool` can be used to compare the run-time types of values.

`_10

Type<Int>().isSubtype(of: Type<Int>()) // true

_10

_10

Type<Int>().isSubtype(of: Type<String>()) // false

_10

_10

Type<Int>().isSubtype(of: Type<Int?>()) // true`

To get the run-time type's fully qualified type identifier, use the `let identifier: String` field:

`_10

let type = Type<Int>()

_10

type.identifier // is "Int"`

`_10

// in account 0x1

_10

_10

struct Test {}

_10

_10

let type = Type<Test>()

_10

type.identifier // is "A.0000000000000001.Test"`

### Getting the Type from a Value[​](#getting-the-type-from-a-value "Direct link to Getting the Type from a Value")

The method `view fun getType(): Type` can be used to get the runtime type of a value.

`_10

let something = "hello"

_10

_10

let type: Type = something.getType()

_10

// `type` is `Type<String>()``

This method returns the **concrete run-time type** of the object, **not** the static type.

`_10

// Declare a variable named `something` that has the *static* type `AnyResource`

_10

// and has a resource of type `Collectible`

_10

//

_10

let something: @AnyResource <- create Collectible()

_10

_10

// The resource's concrete run-time type is `Collectible`

_10

//

_10

let type: Type = something.getType()

_10

// `type` is `Type<@Collectible>()``

### Constructing a Run-time Type[​](#constructing-a-run-time-type "Direct link to Constructing a Run-time Type")

Run-time types can also be constructed from type identifier strings using built-in constructor functions.

`_10

view fun CompositeType(_ identifier: String): Type?

_10

view fun InterfaceType(_ identifier: String): Type?

_10

view fun IntersectionType(types: [String]): Type?`

Given a type identifier (or a list of identifiers for interfaces
in the case of `IntersectionType`), these functions will look up nominal types and
produce their run-time equivalents. If the provided identifiers do not correspond
to any types, or (in the case of `IntersectionType`) the provided combination of
identifiers would not type-check statically, these functions will produce `nil`.

`_10

struct Test: I {}

_10

struct interface I {}

_10

let type: Type = CompositeType("A.0000000000000001.Test")

_10

// `type` is `Type<Test>`

_10

_10

let type2: Type = IntersectionType(

_10

restrictions: ["A.0000000000000001.I"]

_10

)

_10

// `type2` is `Type<{I}>``

Other built-in functions will construct compound types from other run-types.

`_10

view fun OptionalType(_ type: Type): Type

_10

view fun VariableSizedArrayType(_ type: Type): Type

_10

view fun ConstantSizedArrayType(type: Type, size: Int): Type

_10

view fun FunctionType(parameters: [Type], return: Type): Type

_10

// returns `nil` if `key` is not valid dictionary key type

_10

view fun DictionaryType(key: Type, value: Type): Type?

_10

// returns `nil` if `type` is not a reference type

_10

view fun CapabilityType(_ type: Type): Type?

_10

view fun ReferenceType(entitlements: [String], type: Type): Type?`

### Asserting the Type of a Value[​](#asserting-the-type-of-a-value "Direct link to Asserting the Type of a Value")

The method `view fun isInstance(_ type: Type): Bool` can be used to check if a value has a certain type,
using the concrete run-time type, and considering subtyping rules,

`_19

// Declare a variable named `collectible` that has the *static* type `Collectible`

_19

// and has a resource of type `Collectible`

_19

//

_19

let collectible: @Collectible <- create Collectible()

_19

_19

// The resource is an instance of type `Collectible`,

_19

// because the concrete run-time type is `Collectible`

_19

//

_19

collectible.isInstance(Type<@Collectible>()) // is `true`

_19

_19

// The resource is an instance of type `AnyResource`,

_19

// because the concrete run-time type `Collectible` is a subtype of `AnyResource`

_19

//

_19

collectible.isInstance(Type<@AnyResource>()) // is `true`

_19

_19

// The resource is *not* an instance of type `String`,

_19

// because the concrete run-time type `Collectible` is *not* a subtype of `String`

_19

//

_19

collectible.isInstance(Type<String>()) // is `false``

Note that the **concrete run-time type** of the object is used, **not** the static type.

`_19

// Declare a variable named `something` that has the *static* type `AnyResource`

_19

// and has a resource of type `Collectible`

_19

//

_19

let something: @AnyResource <- create Collectible()

_19

_19

// The resource is an instance of type `Collectible`,

_19

// because the concrete run-time type is `Collectible`

_19

//

_19

something.isInstance(Type<@Collectible>()) // is `true`

_19

_19

// The resource is an instance of type `AnyResource`,

_19

// because the concrete run-time type `Collectible` is a subtype of `AnyResource`

_19

//

_19

something.isInstance(Type<@AnyResource>()) // is `true`

_19

_19

// The resource is *not* an instance of type `String`,

_19

// because the concrete run-time type `Collectible` is *not* a subtype of `String`

_19

//

_19

something.isInstance(Type<String>()) // is `false``

For example, this allows implementing a marketplace sale resource:

`_66

access(all)

_66

resource SimpleSale {

_66

_66

/// The resource for sale.

_66

/// Once the resource is sold, the field becomes `nil`.

_66

///

_66

access(all)

_66

var resourceForSale: @AnyResource?

_66

_66

/// The price that is wanted for the purchase of the resource.

_66

///

_66

access(all)

_66

let priceForResource: UFix64

_66

_66

/// The type of currency that is required for the purchase.

_66

///

_66

access(all)

_66

let requiredCurrency: Type

_66

access(all)

_66

let paymentReceiver: Capability<&{FungibleToken.Receiver}>

_66

_66

/// `paymentReceiver` is the capability that will be borrowed

_66

/// once a valid purchase is made.

_66

/// It is expected to target a resource that allows depositing the paid amount

_66

/// (a vault which has the type in `requiredCurrency`).

_66

///

_66

init(

_66

resourceForSale: @AnyResource,

_66

priceForResource: UFix64,

_66

requiredCurrency: Type,

_66

paymentReceiver: Capability<&{FungibleToken.Receiver}>

_66

) {

_66

self.resourceForSale <- resourceForSale

_66

self.priceForResource = priceForResource

_66

self.requiredCurrency = requiredCurrency

_66

self.paymentReceiver = paymentReceiver

_66

}

_66

_66

/// buyObject allows purchasing the resource for sale by providing

_66

/// the required funds.

_66

/// If the purchase succeeds, the resource for sale is returned.

_66

/// If the purchase fails, the program aborts.

_66

///

_66

access(all)

_66

fun buyObject(with funds: @FungibleToken.Vault): @AnyResource {

_66

pre {

_66

// Ensure the resource is still up for sale

_66

self.resourceForSale != nil: "The resource has already been sold"

_66

// Ensure the paid funds have the right amount

_66

funds.balance >= self.priceForResource: "Payment has insufficient amount"

_66

// Ensure the paid currency is correct

_66

funds.isInstance(self.requiredCurrency): "Incorrect payment currency"

_66

}

_66

_66

// Transfer the paid funds to the payment receiver

_66

// by borrowing the payment receiver capability of this sale resource

_66

// and depositing the payment into it

_66

_66

let receiver = self.paymentReceiver.borrow()

_66

?? panic("failed to borrow payment receiver capability")

_66

_66

receiver.deposit(from: <-funds)

_66

let resourceForSale <- self.resourceForSale <- nil

_66

return <-resourceForSale

_66

}

_66

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/run-time-types.md)

[Previous

Core Events](/docs/language/core-events)[Next

Built-in Functions](/docs/language/built-in-functions)

###### Rate this page

😞😐😊

* [Getting the Type from a Value](#getting-the-type-from-a-value)
* [Constructing a Run-time Type](#constructing-a-run-time-type)
* [Asserting the Type of a Value](#asserting-the-type-of-a-value)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.