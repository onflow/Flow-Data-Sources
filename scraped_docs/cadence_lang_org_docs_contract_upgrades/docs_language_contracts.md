# Source: https://cadence-lang.org/docs/language/contracts




Contracts | Cadence




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
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Contracts
On this page
# Contracts

A contract is a collection of type definitions,
data (its state), and code (its functions),
that is stored in the contract storage area of an account.

Contracts are where all composite types interfaces for these types have to be defined.
Therefore, an object of one of these types cannot exist
without having been defined in a deployed Cadence contract.

Contracts can be deployed to accounts, updated, and removed from accounts
using the `contracts` object of [authorized accounts](/docs/language/accounts/).
See the [account contracts page](/docs/language/accounts/contracts)
for more information about these operations.

Contracts are types.
They are similar to composite types, but are stored differently than
structs or resources and cannot be used as values, copied, or moved
like resources or structs.

Contracts stay in an account's contract storage area
and can only be added, updated, or removed by the account owner with special commands.

Contracts are declared using the `contract` keyword.
The keyword is followed by the name of the contract.

 `_10access(all)_10contract SomeContract {_10 // ..._10}`

Contracts cannot be nested in each other.

 `_10access(all)_10contract Invalid {_10_10 // Invalid: Contracts cannot be nested in any other type._10 //_10 access(all)_10 contract Nested {_10 // ..._10 }_10}`

One of the simplest forms of a contract would just be one with a state field,
a function, and an initializer that initializes the field:

 `_20access(all)_20contract HelloWorld {_20_20 // Declare a stored state field in HelloWorld_20 //_20 access(all)_20 let greeting: String_20_20 // Declare a function that can be called by anyone_20 // who imports the contract_20 //_20 access(all)_20 fun hello(): String {_20 return self.greeting_20 }_20_20 init() {_20 self.greeting = "Hello World!"_20 }_20}`

Transactions and other contracts can interact with contracts
by importing them at the beginning of a transaction or contract definition.

Anyone could call the above contract's `hello` function by importing
the contract from the account it was deployed to and using the imported
object to call the hello function.

 `_18import HelloWorld from 0x42_18_18// Invalid: The contract does not know where hello comes from_18//_18log(hello()) // Error_18_18// Valid: Using the imported contract object to call the hello_18// function_18//_18log(HelloWorld.hello()) // prints "Hello World!"_18_18// Valid: Using the imported contract object to read the greeting_18// field._18log(HelloWorld.greeting) // prints "Hello World!"_18_18// Invalid: Cannot call the init function after the contract has been created._18//_18HelloWorld.init() // Error`

There can be any number of contracts per account
and they can include an arbitrary amount of data.
This means that a contract can have any number of fields, functions, and type definitions,
but they have to be in the contract and not another top-level definition.

 `_14// Invalid: Top-level declarations are restricted to only be contracts_14// or contract interfaces. Therefore, all of these would be invalid_14// if they were deployed to the account contract storage and_14// the deployment would be rejected._14//_14access(all)_14resource Vault {}_14_14access(all)_14struct Hat {}_14_14access(all)_14fun helloWorld(): String {}_14let num: Int`

Another important feature of contracts is that instances of resources and events
that are declared in contracts can only be created/emitted within functions or types
that are declared in the same contract.

It is not possible create instances of resources and events outside the contract.

The contract below defines a resource interface `Receiver` and a resource `Vault`
that implements that interface. The way this example is written,
there is no way to create this resource, so it would not be usable.

 `_52// Valid_52access(all)_52contract FungibleToken {_52_52 access(all)_52 resource interface Receiver {_52_52 access(all)_52 balance: Int_52_52 access(all)_52 fun deposit(from: @{Receiver}) {_52 pre {_52 from.balance > 0:_52 "Deposit balance needs to be positive!"_52 }_52 post {_52 self.balance == before(self.balance) + before(from.balance):_52 "Incorrect amount removed"_52 }_52 }_52 }_52_52 access(all)_52 resource Vault: Receiver {_52_52 // keeps track of the total balance of the accounts tokens_52 access(all)_52 var balance: Int_52_52 init(balance: Int) {_52 self.balance = balance_52 }_52_52 // withdraw subtracts amount from the vaults balance and_52 // returns a vault object with the subtracted balance_52 access(all)_52 fun withdraw(amount: Int): @Vault {_52 self.balance = self.balance - amount_52 return <-create Vault(balance: amount)_52 }_52_52 // deposit takes a vault object as a parameter and adds_52 // its balance to the balance of the Account's vault, then_52 // destroys the sent vault because its balance has been consumed_52 access(all)_52 fun deposit(from: @{Receiver}) {_52 self.balance = self.balance + from.balance_52 destroy from_52 }_52 }_52}`

If a user tried to run a transaction that created an instance of the `Vault` type,
the type checker would not allow it because only code in the `FungibleToken`
contract can create new `Vault`s.

 `_10import FungibleToken from 0x42_10_10// Invalid: Cannot create an instance of the `Vault` type outside_10// of the contract that defines `Vault`_10//_10let newVault <- create FungibleToken.Vault(balance: 10)`
## Account access[​](#account-access "Direct link to Account access")

Contracts can access the account they are deployed to:
contracts have the implicit field named `account`
which is only accessible within the contract.

 `_10let account: auth(Storage, Keys, Contracts, Inbox, Capabilities) &Account`,`

The account reference is fully entitled,
so grants access to the account's storage, keys, contracts, etc.

For example, this gives the contract the ability to write to the account's storage
when the contract is initialized.

 `_10init(balance: Int) {_10 self.account.storage.save(_10 <-create Vault(balance: 1000),_10 to: /storage/initialVault_10 )_10}`
## Contract interfaces[​](#contract-interfaces "Direct link to Contract interfaces")

Like composite types, contracts can have interfaces that specify rules
about their behavior, their types, and the behavior of their types.

Contract interfaces have to be declared globally.
Declarations cannot be nested in other types.

Contract interfaces may not declare concrete types (other than events), but they can declare interfaces.
If a contract interface declares an interface type, the implementing contract
does not have to also define that interface.
They can refer to that nested interface by saying `{ContractInterfaceName}.{NestedInterfaceName}`

 `_31// Declare a contract interface that declares an interface and a resource_31// that needs to implement that interface in the contract implementation._31//_31access(all)_31contract interface InterfaceExample {_31_31 // Implementations do not need to declare this_31 // They refer to it as InterfaceExample.NestedInterface_31 //_31 access(all)_31 resource interface NestedInterface {}_31_31 // Implementations must declare this type_31 //_31 access(all)_31 resource Composite: NestedInterface {}_31}_31_31access(all)_31contract ExampleContract: InterfaceExample {_31_31 // The contract doesn't need to redeclare the `NestedInterface` interface_31 // because it is already declared in the contract interface_31_31 // The resource has to refer to the resource interface using the name_31 // of the contract interface to access it_31 //_31 access(all)_31 resource Composite: InterfaceExample.NestedInterface {_31 }_31}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/contracts.mdx)[PreviousAttachments](/docs/language/attachments)[NextContract Updatability](/docs/language/contract-updatability)
###### Rate this page

😞😐😊

* [Account access](#account-access)
* [Contract interfaces](#contract-interfaces)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

