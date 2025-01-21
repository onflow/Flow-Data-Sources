# Source: https://developers.flow.com/cadence/language/interfaces




Interfaces | Cadence




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
* Interfaces
On this page
# Interfaces

An interface is an abstract type that specifies the behavior of types
that *implement* the interface.
Interfaces declare the required functions and fields,
the access control for those declarations,
and preconditions and postconditions that implementing types need to provide.

There are three kinds of interfaces:

* **Structure interfaces**: implemented by [structures](/docs/language/composite-types#structures)
* **Resource interfaces**: implemented by [resources](/docs/language/composite-types#resources)
* **Contract interfaces**: implemented by [contracts](/docs/language/contracts)

Structure, resource, and contract types may implement multiple interfaces.

There is no support for event and enum interfaces.

Nominal typing applies to composite types that implement interfaces.
This means that a type only implements an interface
if it has explicitly declared the conformance,
the composite type does not implicitly conform to an interface,
even if it satisfies all requirements of the interface.

Interfaces consist of the function and field requirements
that a type implementing the interface must provide implementations for.
Interface requirements, and therefore also their implementations,
must always be at least public.

Variable field requirements may be annotated
to require them to be publicly settable.

Function requirements consist of the name of the function,
parameter types, an optional return type,
and optional preconditions and postconditions.

Field requirements consist of the name and the type of the field.
Field requirements may optionally declare a getter requirement and a setter requirement,
each with preconditions and postconditions.

Calling functions with preconditions and postconditions on interfaces
instead of concrete implementations can improve the security of a program,
as it ensures that even if implementations change,
some aspects of them will always hold.

## Interface Declaration[​](#interface-declaration "Direct link to Interface Declaration")

Interfaces are declared using the `struct`, `resource`, or `contract` keyword,
followed by the `interface` keyword,
the name of the interface,
and the requirements, which must be enclosed in opening and closing braces.

Field requirements can be annotated to
require the implementation to be a variable field, by using the `var` keyword;
require the implementation to be a constant field, by using the `let` keyword;
or the field requirement may specify nothing,
in which case the implementation may either be a variable or a constant field.

Field requirements and function requirements must specify the required level of access.
The access must be at least be public, so the `access(all)` keyword must be provided.

Interfaces can be used in types.
This is explained in detail in the section [Interfaces in Types](#interfaces-in-types).
For now, the syntax `{I}` can be read as the type of any value that implements the interface `I`.

 `_81// Declare a resource interface for a fungible token._81// Only resources can implement this resource interface._81//_81access(all)_81resource interface FungibleToken {_81_81 // Require the implementing type to provide a field for the balance_81 // that is readable in all scopes (`access(all)`)._81 //_81 // Neither the `var` keyword, nor the `let` keyword is used,_81 // so the field may be implemented as either a variable_81 // or as a constant field._81 //_81 access(all)_81 balance: Int_81_81 // Require the implementing type to provide an initializer that_81 // given the initial balance, must initialize the balance field._81 //_81 init(balance: Int) {_81 pre {_81 balance >= 0:_81 "Balances are always non-negative"_81 }_81 post {_81 self.balance == balance:_81 "the balance must be initialized to the initial balance"_81 }_81_81 // NOTE: The declaration contains no implementation code._81 }_81_81 // Require the implementing type to provide a function that is_81 // callable in all scopes, which withdraws an amount from_81 // this fungible token and returns the withdrawn amount as_81 // a new fungible token._81 //_81 // The given amount must be positive and the function implementation_81 // must add the amount to the balance._81 //_81 // The function must return a new fungible token._81 // The type `{FungibleToken}` is the type of any resource_81 // that implements the resource interface `FungibleToken`._81 //_81 access(all)_81 fun withdraw(amount: Int): @{FungibleToken} {_81 pre {_81 amount > 0:_81 "the amount must be positive"_81 amount <= self.balance:_81 "insufficient funds: the amount must be smaller or equal to the balance"_81 }_81 post {_81 self.balance == before(self.balance) - amount:_81 "the amount must be deducted from the balance"_81 }_81_81 // NOTE: The declaration contains no implementation code._81 }_81_81 // Require the implementing type to provide a function that is_81 // callable in all scopes, which deposits a fungible token_81 // into this fungible token._81 //_81 // No precondition is required to check the given token's balance_81 // is positive, as this condition is already ensured by_81 // the field requirement._81 //_81 // The parameter type `{FungibleToken}` is the type of any resource_81 // that implements the resource interface `FungibleToken`._81 //_81 access(all)_81 fun deposit(_ token: @{FungibleToken}) {_81 post {_81 self.balance == before(self.balance) + token.balance:_81 "the amount must be added to the balance"_81 }_81_81 // NOTE: The declaration contains no implementation code._81 }_81}`

Note that the required initializer and functions do not have any executable code.

Struct and resource Interfaces can only be declared directly inside contracts,
i.e. not inside of functions.
Contract interfaces can only be declared globally and not inside contracts.

## Interface Implementation[​](#interface-implementation "Direct link to Interface Implementation")

Declaring that a type implements (conforms) to an interface
is done in the type declaration of the composite type (e.g., structure, resource):
The kind and the name of the composite type is followed by a colon (`:`)
and the name of one or more interfaces that the composite type implements.

This will tell the checker to enforce any requirements from the specified interfaces
onto the declared type.

A type implements (conforms to) an interface if it declares
the implementation in its signature, provides field declarations
for all fields required by the interface,
and provides implementations for all functions required by the interface.

The field declarations in the implementing type must match the field requirements
in the interface in terms of name, type, and declaration kind (e.g. constant, variable)
if given. For example, an interface may require a field with a certain name and type,
but leaves it to the implementation what kind the field is.

The function implementations must match the function requirements in the interface
in terms of name, parameter argument labels, parameter types, and the return type.

 `_108// Declare a resource named `ExampleToken` that has to implement_108// the `FungibleToken` interface._108//_108// It has a variable field named `balance`, that can be written_108// by functions of the type, but outer scopes can only read it._108//_108access(all)_108resource ExampleToken: FungibleToken {_108_108 // Implement the required field `balance` for the `FungibleToken` interface._108 // The interface does not specify if the field must be variable, constant,_108 // so in order for this type (`ExampleToken`) to be able to write to the field,_108 // but limit outer scopes to only read from the field, it is declared variable,_108 // and only has public access (non-settable)._108 //_108 access(all)_108 var balance: Int_108_108 // Implement the required initializer for the `FungibleToken` interface:_108 // accept an initial balance and initialize the `balance` field._108 //_108 // This implementation satisfies the required postcondition._108 //_108 // NOTE: the postcondition declared in the interface_108 // does not have to be repeated here in the implementation._108 //_108 init(balance: Int) {_108 self.balance = balance_108 }_108_108 // Implement the required function named `withdraw` of the interface_108 // `FungibleToken`, that withdraws an amount from the token's balance._108 //_108 // The function must be public._108 //_108 // This implementation satisfies the required postcondition._108 //_108 // NOTE: neither the precondition nor the postcondition declared_108 // in the interface have to be repeated here in the implementation._108 //_108 access(all)_108 fun withdraw(amount: Int): @ExampleToken {_108 self.balance = self.balance - amount_108 return create ExampleToken(balance: amount)_108 }_108_108 // Implement the required function named `deposit` of the interface_108 // `FungibleToken`, that deposits the amount from the given token_108 // to this token._108 //_108 // The function must be public._108 //_108 // NOTE: the type of the parameter is `{FungibleToken}`,_108 // i.e., any resource that implements the resource interface `FungibleToken`,_108 // so any other token – however, we want to ensure that only tokens_108 // of the same type can be deposited._108 //_108 // This implementation satisfies the required postconditions._108 //_108 // NOTE: neither the precondition nor the postcondition declared_108 // in the interface have to be repeated here in the implementation._108 //_108 access(all)_108 fun deposit(_ token: @{FungibleToken}) {_108 if let exampleToken <- token as? ExampleToken {_108 self.balance = self.balance + exampleToken.balance_108 destroy exampleToken_108 } else {_108 panic("cannot deposit token which is not an example token")_108 }_108 }_108}_108_108// Declare a constant which has type `ExampleToken`,_108// and is initialized with such an example token._108//_108let token <- create ExampleToken(balance: 100)_108_108// Withdraw 10 units from the token._108//_108// The amount satisfies the precondition of the `withdraw` function_108// in the `FungibleToken` interface._108//_108// Invoking a function of a resource does not destroy the resource,_108// so the resource `token` is still valid after the call of `withdraw`._108//_108let withdrawn <- token.withdraw(amount: 10)_108_108// The postcondition of the `withdraw` function in the `FungibleToken`_108// interface ensured the balance field of the token was updated properly._108//_108// `token.balance` is `90`_108// `withdrawn.balance` is `10`_108_108// Deposit the withdrawn token into another one._108let receiver: @ExampleToken <- // ..._108receiver.deposit(<-withdrawn)_108_108// Run-time error: The precondition of function `withdraw` in interface_108// `FungibleToken` fails, the program aborts: the parameter `amount`_108// is larger than the field `balance` (100 > 90)._108//_108token.withdraw(amount: 100)_108_108// Withdrawing tokens so that the balance is zero does not destroy the resource._108// The resource has to be destroyed explicitly._108//_108token.withdraw(amount: 90)`

The access level for variable fields in an implementation
may be less restrictive than the interface requires.
For example, an interface may require a field to be
at least contract-accessible (i.e. the `access(contract)` modifier is used),
and an implementation may provide a variable field which is public,
(the `access(all)` modifier is used).

 `_22access(all)_22struct interface AnInterface {_22 // Require the implementing type to provide a contract-readable_22 // field named `a` that has type `Int`. It may be a variable_22 // or a constant field._22 //_22 access(contract)_22 a: Int_22}_22_22access(all)_22struct AnImplementation: AnInterface {_22 // Declare a public variable field named `a` that has type `Int`._22 // This implementation satisfies the requirement for interface `AnInterface`:_22 //_22 access(all)_22 var a: Int_22_22 init(a: Int) {_22 self.a = a_22 }_22}`
## Interfaces in Types[​](#interfaces-in-types "Direct link to Interfaces in Types")

Interfaces can be used in types: The type `{I}` is the type of all objects
that implement the interface `I`.

This is called a [intersection type](/docs/language/intersection-types):
Only the functionality (members and functions) of the interface can be used
when accessing a value of such a type.

 `_88// Declare an interface named `Shape`._88//_88// Require implementing types to provide a field which returns the area,_88// and a function which scales the shape by a given factor._88//_88access(all)_88struct interface Shape {_88_88 access(all)_88 fun getArea(): Int_88_88 access(all)_88 fun scale(factor: Int)_88}_88_88// Declare a structure named `Square` the implements the `Shape` interface._88//_88access(all)_88struct Square: Shape {_88 // In addition to the required fields from the interface,_88 // the type can also declare additional fields._88 //_88 access(all)_88 var length: Int_88_88 // Provided the field `area` which is required to conform_88 // to the interface `Shape`._88 //_88 // Since `area` was not declared as a constant, variable,_88 // field in the interface, it can be declared._88 //_88 access(all)_88 fun getArea(): Int {_88 return self.length * self.length_88 }_88_88 access(all)_88 init(length: Int) {_88 self.length = length_88 }_88_88 // Provided the implementation of the function `scale`_88 // which is required to conform to the interface `Shape`._88 //_88 access(all)_88 fun scale(factor: Int) {_88 self.length = self.length * factor_88 }_88}_88_88// Declare a structure named `Rectangle` that also implements the `Shape` interface._88//_88access(all)_88struct Rectangle: Shape {_88_88 access(all)_88 var width: Int_88_88 access(all)_88 var height: Int_88_88 // Provided the field `area which is required to conform_88 // to the interface `Shape`._88 //_88 access(all)_88 fun getArea(): Int {_88 return self.width * self.height_88 }_88_88 access(all)_88 init(width: Int, height: Int) {_88 self.width = width_88 self.height = height_88 }_88_88 // Provided the implementation of the function `scale`_88 // which is required to conform to the interface `Shape`._88 //_88 access(all)_88 fun scale(factor: Int) {_88 self.width = self.width * factor_88 self.height = self.height * factor_88 }_88}_88_88// Declare a constant that has type `Shape`, which has a value that has type `Rectangle`._88//_88var shape: {Shape} = Rectangle(width: 10, height: 20)`

Values implementing an interface are assignable to variables that have the interface as their type.

 `_10// Assign a value of type `Square` to the variable `shape` that has type `Shape`._10//_10shape = Square(length: 30)_10_10// Invalid: cannot initialize a constant that has type `Rectangle`._10// with a value that has type `Square`._10//_10let rectangle: Rectangle = Square(length: 10)`

Fields declared in an interface can be accessed
and functions declared in an interface
can be called on values of a type that implements the interface.

 `_14// Declare a constant which has the type `Shape`._14// and is initialized with a value that has type `Rectangle`._14//_14let shape: {Shape} = Rectangle(width: 2, height: 3)_14_14// Access the field `area` declared in the interface `Shape`._14//_14shape.area // is `6`_14_14// Call the function `scale` declared in the interface `Shape`._14//_14shape.scale(factor: 3)_14_14shape.area // is `54``
## Interface Nesting[​](#interface-nesting "Direct link to Interface Nesting")

🚧 Status

Currently only contracts and contract interfaces support nested interfaces.

Interfaces can be arbitrarily nested.
Declaring an interface inside another does not require implementing types
of the outer interface to provide an implementation of the inner interfaces.

 `_23// Declare a resource interface `OuterInterface`, which declares_23// a nested structure interface named `InnerInterface`._23//_23// Resources implementing `OuterInterface` do not need to provide_23// an implementation of `InnerInterface`._23//_23// Structures may just implement `InnerInterface`._23//_23resource interface OuterInterface {_23_23 struct interface InnerInterface {}_23}_23_23// Declare a resource named `SomeOuter` that implements the interface `OuterInterface`._23//_23// The resource is not required to implement `OuterInterface.InnerInterface`._23//_23resource SomeOuter: OuterInterface {}_23_23// Declare a structure named `SomeInner` that implements `InnerInterface`,_23// which is nested in interface `OuterInterface`._23//_23struct SomeInner: OuterInterface.InnerInterface {}`

Contract interfaces may also declare [events](/docs/language/events),
which also do not require implementing types of the outer interface to "implement" the event.
The event can be emitted in the declaring interface, in a condition or in a default implementation of a function. E.g.

 `_27// Declare a contract interface_27//_27contract interface ContractInterface {_27 // some event declaration_27 //_27 event SomeEvent()_27_27 // some function that emits `SomeEvent` when called_27 //_27 fun eventEmittingFunction() {_27 pre {_27 emit SomeEvent()_27 }_27 }_27}_27_27// A contract implementing `ContractInterface`_27// Note that no declaration of `SomeEvent` is required_27//_27contract ImplementingContract: ContractInterface {_27 // implementation of `eventEmittingFunction`;_27 // this will emit `SomeEvent` when called_27 //_27 fun eventEmittingFunction() {_27 // ..._27 }_27}`
## Interface Default Functions[​](#interface-default-functions "Direct link to Interface Default Functions")

Interfaces can provide default functions:
If the concrete type implementing the interface does not provide an implementation
for the function required by the interface,
then the interface's default function is used in the implementation.

 `_27// Declare a struct interface `Container`,_27// which declares a default function `getCount`._27//_27struct interface Container {_27_27 let items: [AnyStruct]_27_27 fun getCount(): Int {_27 return self.items.length_27 }_27}_27_27// Declare a concrete struct named `Numbers` that implements the interface `Container`._27//_27// The struct does not implement the function `getCount` of the interface `Container`,_27// so the default function for `getCount` is used._27//_27struct Numbers: Container {_27 let items: [AnyStruct]_27_27 init() {_27 self.items = []_27 }_27}_27_27let numbers = Numbers()_27numbers.getCount() // is 0`

Interfaces cannot provide default initializers.

Only one conformance may provide a default function.

## Interface inheritance[​](#interface-inheritance "Direct link to Interface inheritance")

An interface can inherit from (conform to) other interfaces of the same kind.
For example, a resource interface can inherit from another resource interface, but cannot inherit from a struct interface.
When an interface inherits from another, all the fields, functions, and types of the parent interface are implicitly
available to the inheriting interface.

 `_12access(all)_12resource interface Receiver {_12 access(all)_12 fun deposit(_ something: @AnyResource)_12}_12_12// `Vault` interface inherits from `Receiver` interface._12access(all)_12resource interface Vault: Receiver {_12 access(all)_12 fun withdraw(_ amount: Int): @Vault_12}`

In the example above, `Vault` inherits `Receiver`. Anyone implementing the `Vault` interface would also have to
implement the `Receiver` interface.

 `_10access(all)_10resource MyVault: Vault {_10 _10 // Must implement all the methods coming from both `Vault` and `Receiver` interfaces._10 access(all)_10 fun deposit(_ something: @AnyResource) {}_10_10 access(all)_10 fun withdraw(_ amount: Int): @Vault {}_10}`
### Duplicate interface members[​](#duplicate-interface-members "Direct link to Duplicate interface members")

When an interface implements another interface, it is possible for the two interfaces to have members with the same name.
The following sections explain how these ambiguities are resolved for different scenarios.

#### Fields[​](#fields "Direct link to Fields")

If two fields with identical names have identical types, then it will be valid.

 `_12access(all)_12resource interface Receiver {_12 access(all)_12 var id: UInt64_12}_12_12access(all)_12resource interface Vault: Receiver {_12 // `id` field has the same type as the `Receiver.id`. Hence this is valid._12 access(all)_12 var id: UInt64_12}`

Otherwise, interface conformance is not valid.

 `_12access(all)_12resource interface Receiver {_12 access(all)_12 var id: Int_12}_12_12access(all)_12resource interface Vault: Receiver {_12 // `id` field has a different type than the `Receiver.id`. Hence this is invalid._12 access(all)_12 var id: UInt64_12}`
#### Functions[​](#functions "Direct link to Functions")

If two functions with identical names also have identical signatures, that is valid.

 `_14access(all)_14resource interface Receiver {_14 access(all)_14 fun deposit(_ something: @AnyResource)_14}_14_14access(all)_14resource interface Vault: Receiver {_14 // `deposit` function has the same signature as the `Receiver.deposit`._14 // Also none of them have any default implementations._14 // Hence this is valid._14 access(all)_14 fun deposit(_ something: @AnyResource)_14}`

If the signatures of the two functions are different, then the interface conformance is not valid.

 `_13access(all)_13resource interface Receiver {_13 access(all)_13 fun deposit(_ something: @AnyResource)_13}_13_13access(all)_13resource interface Vault: Receiver {_13 // Error: `deposit` function has a different signature compared to the `Receiver.deposit`._13 // So these two cannot co-exist._13 access(all)_13 fun deposit()_13}`
#### Functions with conditions[​](#functions-with-conditions "Direct link to Functions with conditions")

If the two functions with identical names and signatures have pre/post conditions, then it will still be valid.
However, the pre/post conditions are linearized (refer to the [linearizing conditions section](#linearizing-conditions))
to determine the order of the execution of the conditions.
Given the pre/post conditions are `view` only, the order of execution would not have an impact on the conditions.

 `_18access(all)_18resource interface Receiver {_18 access(all)_18 fun deposit(_ something: @AnyResource) {_18 pre{ self.balance > 100 }_18 }_18}_18_18access(all)_18resource interface Vault: Receiver {_18 // `deposit` function has the same signature as the `Receiver.deposit`._18 // Having pre/post condition is valid._18 // Both conditions would be executed, in a pre-determined order._18 access(all)_18 fun deposit(_ something: @AnyResource) {_18 pre{ self.balance > 50 }_18 }_18}`
#### Default functions[​](#default-functions "Direct link to Default functions")

An interface can provide a default implementation to an inherited function.

 `_14access(all)_14resource interface Receiver {_14 access(all)_14 fun log(_ message: String)_14}_14_14access(all)_14resource interface Vault: Receiver {_14 // Valid: Provides the implementation for `Receiver.log` method._14 access(all)_14 fun log(_ message: String) {_14 log(message.append("from Vault"))_14 }_14}`

However, an interface cannot override an inherited default implementation of a function.

 `_16access(all)_16resource interface Receiver {_16 access(all)_16 fun log(_ message: String) {_16 log(message.append("from Receiver"))_16 }_16}_16_16access(all)_16resource interface Vault: Receiver {_16 // Invalid: Cannot override the `Receiver.log` method._16 access(all)_16 fun log(_ message: String) {_16 log(message.append("from Vault"))_16 }_16}`

It is also invalid to have two or more inherited default implementations for an interface.

 `_19access(all)_19resource interface Receiver {_19 access(all)_19 fun log(_ message: String) {_19 log(message.append("from Receiver"))_19 }_19}_19_19access(all)_19resource interface Provider {_19 access(all)_19 fun log(_ message: String) {_19 log(message.append("from Provider"))_19 }_19}_19_19// Invalid: Two default functions from two interfaces._19access(all)_19resource interface Vault: Receiver, Provider {}`

Having said that, there can be situations where the same default function can be available via different
inheritance paths.

 `_18access(all)_18resource interface Logger {_18 access(all)_18 fun log(_ message: String) {_18 log(message.append("from Logger"))_18 }_18}_18_18access(all)_18resource interface Receiver: Logger {}_18_18access(all)_18resource interface Provider: Logger {}_18_18// Valid: `Logger.log()` default function is visible to the `Vault` interface_18// via both `Receiver` and `Provider`._18access(all)_18resource interface Vault: Receiver, Provider {}`

In the above example, `Logger.log()` default function is visible to the `Vault` interface via both `Receiver` and `Provider`.
Even though it is available from two different interfaces, they are both referring to the same
default implementation.
Therefore, the above code is valid.

#### Conditions with Default functions[​](#conditions-with-default-functions "Direct link to Conditions with Default functions")

A more complex situation is where a default function is available via one inheritance path and a pre/post condition
is available via another inheritance path.

 `_19access(all)_19resource interface Receiver {_19 access(all)_19 fun log(_ message: String) {_19 log(message.append("from Receiver"))_19 }_19}_19_19access(all)_19resource interface Provider {_19 access(all)_19 fun log(_ message: String) {_19 pre{ message != "" }_19 }_19}_19_19// Valid: Both the default function and the condition would be available._19access(all)_19resource interface Vault: Receiver, Provider {}`

In such situations, all rules applicable for default functions inheritance as well as condition inheritance
would be applied.
Thus, the default function from coming from the `Receiver` interface, and the condition comes from the `Provider`
interface would be made available for the inherited interface.

#### Types and event definitions[​](#types-and-event-definitions "Direct link to Types and event definitions")

Type and event definitions would also behave similarly to the default functions.
Inherited interfaces can override type definitions and event definitions.

 `_19access(all)_19contract interface Token {_19 access(all)_19 struct Foo {}_19}_19_19access(all)_19contract interface NonFungibleToken: Token {_19 access(all)_19 struct Foo {}_19}_19_19access(all)_19contract MyToken: NonFungibleToken {_19 access(all)_19 fun test() {_19 let foo: Foo // This will refer to the `NonFungibleToken.Foo`_19 }_19}`

If a user needed to access the `Foo` struct coming from the super interface `Token`, then they can
access it using the fully qualified name. e.g: `let foo: Token.Foo`.

However, it is not allowed to have two or more inherited type/events definitions with identical names for an interface.

 `_16access(all)_16contract interface Token {_16 access(all)_16 struct Foo {}_16}_16_16access(all)_16contract interface Collectible {_16 access(all)_16 struct Foo {}_16}_16_16// Invalid: Two type definitions with the same name from two interfaces._16access(all)_16contract NonFungibleToken: Token, Collectible {_16}`

Similar to default functions, there can be situations where the same type/event definition can be available
via different inheritance paths.

 `_15access(all)_15contract interface Logger {_15 access(all)_15 struct Foo {}_15}_15_15access(all)_15contract interface Token: Logger {}_15_15access(all)_15contract interface Collectible: Logger {}_15_15// Valid: `Logger.Foo` struct is visible to the `NonFungibleToken` interface via both `Token` and `Collectible`._15access(all)_15contract interface NonFungibleToken: Token, Collectible {}`

In the above example, `Logger.Foo` type definition is visible to the `NonFungibleToken` interface via both `Token`
and `Collectible`.
Even though it is available from two different interfaces, they are both referring to the same
type definition.
Therefore, the above code is valid.

However, if at least one of the interfaces in the middle of the chain also overrides the type definition `Foo`,
then the code becomes invalid, as there are multiple implementations present now, which leads to ambiguity.

 `_21access(all)_21contract interface Logger {_21 access(all)_21 struct Foo {}_21}_21_21access(all)_21contract interface Token: Logger {_21 access(all)_21 struct Foo {}_21}_21_21access(all)_21contract interface Collectible: Logger {}_21_21// Invalid: The default implementation of the `Foo` struct by the `Logger`_21// interface is visible to the `NonFungibleToken` via the `Collectible` interface._21// Another implementation of `Foo` struct is visible to the `NonFungibleToken` via the `Token` interface._21// This creates ambiguity._21access(all)_21resource interface NonFungibleToken: Token, Provider {}`
### Linearizing Conditions[​](#linearizing-conditions "Direct link to Linearizing Conditions")

As mentioned in the [functions with conditions](#functions-with-conditions) section, it would be required to linearize
the function conditions, to determine the order in which pre- and post-conditions are executed.
This is done by linearizing the interfaces, and hence conditions, in a **depth-first pre-ordered manner, without duplicates**.

For example, consider an interface inheritance hierarchy as below:

 `_10 A_10 / \_10 B C_10 / \ /_10 D E_10where an edge from A (top) to B (bottom) means A inherits B.`

This would convert to a Cadence implementation similar to:

 `_34struct interface A: B, C {_34 access(all)_34 fun test() {_34 pre { print("A") }_34 }_34}_34_34struct interface B: D, E {_34 access(all)_34 fun test() {_34 pre { print("B") }_34 }_34}_34_34struct interface C: E {_34 access(all)_34 fun test() {_34 pre { print("C") }_34 }_34}_34_34struct interface D {_34 access(all)_34 fun test() {_34 pre { print("D") }_34 }_34}_34_34struct interface E {_34 access(all)_34 fun test() {_34 pre { print("E") }_34 }_34}`

Any concrete type implementing interface `A` would be equivalent to implementing all interfaces from `A` to `E`, linearized.

 `_10struct Foo: A {_10 access(all)_10 fun test() {_10 pre { print("Foo") }_10 }_10}`

The linearized interface order would be: [A, B, D, E, C].

i.e: same as having:

 `_10struct Foo: A, B, D, C, E {_10 access(all)_10 fun test() {_10 pre { print("Foo") }_10 }_10}`

Thus, invoking `test` method of `Foo` would first invoke the pre-conditions of [A, B, D, E, C], in that particular order,
and eventually runs the pre-condition of the concrete implementation `Foo`.

 `_10let foo = Foo()_10foo.test()`

Above will print:

 `_10A_10B_10D_10E_10C_10Foo`

Similarly, for post-conditions, the same linearization of interfaces would be used, and the post-conditions are executed
in the reverse order.
For example, replacing the `pre` conditions in the above example with `post` conditions with the exact same content would
result in an output similar to:

 `_10Foo_10C_10E_10D_10B_10A`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/interfaces.mdx)[PreviousCapabilities](/docs/language/capabilities)[NextEnumerations](/docs/language/enumerations)
###### Rate this page

😞😐😊

* [Interface Declaration](#interface-declaration)
* [Interface Implementation](#interface-implementation)
* [Interfaces in Types](#interfaces-in-types)
* [Interface Nesting](#interface-nesting)
* [Interface Default Functions](#interface-default-functions)
* [Interface inheritance](#interface-inheritance)
  + [Duplicate interface members](#duplicate-interface-members)
  + [Linearizing Conditions](#linearizing-conditions)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

