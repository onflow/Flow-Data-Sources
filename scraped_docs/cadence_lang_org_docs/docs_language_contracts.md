# Source: https://cadence-lang.org/docs/language/contracts

Contracts | Cadence



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
* Contracts

On this page

# Contracts

A contract is a collection of type definitions, data (its state), and code (its functions) that is stored in the contract storage area of an account.

Contracts also:

* are where all composite types' interfaces for these types must be defined. Therefore, an object of one of these types cannot exist without having been defined in a deployed Cadence contract.
* can be deployed to accounts, updated, and removed from accounts using the `contracts` object of [authorized accounts](/docs/language/accounts/). See the [account contracts](#accountcontracts) section below for more information about these operations.
* are types. They are similar to composite types, but are stored differently than structs or resources and cannot be used as values, copied, or moved like resources or structs.

Contracts stay in an account's contract storage area and can only be added, updated, or removed by the account owner with special commands.

Contracts are declared using the `contract` keyword. The keyword is followed by the name of the contract:

`_10

access(all)

_10

contract SomeContract {

_10

// ...

_10

}`

Contracts cannot be nested in each other:

`_10

access(all)

_10

contract Invalid {

_10

_10

// Invalid: Contracts cannot be nested in any other type.

_10

//

_10

access(all)

_10

contract Nested {

_10

// ...

_10

}

_10

}`

One of the simplest forms of a contract is one with a state field, a function, and an initializer that initializes the field:

`_20

access(all)

_20

contract HelloWorld {

_20

_20

// Declare a stored state field in HelloWorld

_20

//

_20

access(all)

_20

let greeting: String

_20

_20

// Declare a function that can be called by anyone

_20

// who imports the contract

_20

//

_20

access(all)

_20

fun hello(): String {

_20

return self.greeting

_20

}

_20

_20

init() {

_20

self.greeting = "Hello World!"

_20

}

_20

}`

Transactions and other contracts can interact with contracts by importing them at the beginning of a transaction or contract definition.

Anyone can call the above contract's `hello` function by importing the contract from the account it was deployed to and using the imported object to call the hello function:

`_18

import HelloWorld from 0x42

_18

_18

// Invalid: The contract does not know where hello comes from

_18

//

_18

log(hello()) // Error

_18

_18

// Valid: Using the imported contract object to call the hello

_18

// function

_18

//

_18

log(HelloWorld.hello()) // prints "Hello World!"

_18

_18

// Valid: Using the imported contract object to read the greeting

_18

// field

_18

log(HelloWorld.greeting) // prints "Hello World!"

_18

_18

// Invalid: Cannot call the init function after the contract has been created.

_18

//

_18

HelloWorld.init() // Error`

There can be any number of contracts per account, and they can include an arbitrary amount of data. This means that a contract can have any number of fields, functions, and type definitions, but they must be in the contract and not another top-level definition:

`_14

// Invalid: Top-level declarations are restricted to only be contracts

_14

// or contract interfaces. Therefore, all of these would be invalid

_14

// if they were deployed to the account contract storage and

_14

// the deployment would be rejected.

_14

//

_14

access(all)

_14

resource Vault {}

_14

_14

access(all)

_14

struct Hat {}

_14

_14

access(all)

_14

fun helloWorld(): String {}

_14

let num: Int`

Another important feature of contracts is that instances of resources and events that are declared in contracts can only be created/emitted within functions or types that are declared in the same contract.

It is not possible to create instances of resources and events outside the contract.

The following contract defines a resource interface `Receiver`, and a resource `Vault` that implements that interface. Due to how this example is written, there is no way to create this resource, so it would not be usable:

`_52

// Valid

_52

access(all)

_52

contract FungibleToken {

_52

_52

access(all)

_52

resource interface Receiver {

_52

_52

access(all)

_52

balance: Int

_52

_52

access(all)

_52

fun deposit(from: @{Receiver}) {

_52

pre {

_52

from.balance > 0:

_52

"Deposit balance needs to be positive!"

_52

}

_52

post {

_52

self.balance == before(self.balance) + before(from.balance):

_52

"Incorrect amount removed"

_52

}

_52

}

_52

}

_52

_52

access(all)

_52

resource Vault: Receiver {

_52

_52

// keeps track of the total balance of the accounts tokens

_52

access(all)

_52

var balance: Int

_52

_52

init(balance: Int) {

_52

self.balance = balance

_52

}

_52

_52

// withdraw subtracts amount from the vaults balance and

_52

// returns a vault object with the subtracted balance

_52

access(all)

_52

fun withdraw(amount: Int): @Vault {

_52

self.balance = self.balance - amount

_52

return <-create Vault(balance: amount)

_52

}

_52

_52

// deposit takes a vault object as a parameter and adds

_52

// its balance to the balance of the Account's vault, then

_52

// destroys the sent vault because its balance has been consumed

_52

access(all)

_52

fun deposit(from: @{Receiver}) {

_52

self.balance = self.balance + from.balance

_52

destroy from

_52

}

_52

}

_52

}`

If a user tried to run a transaction that created an instance of the `Vault` type, the type checker would not allow it because only code in the `FungibleToken` contract can create new `Vault`s:

`` _10

import FungibleToken from 0x42

_10

_10

// Invalid: Cannot create an instance of the `Vault` type outside

_10

// of the contract that defines `Vault`

_10

//

_10

let newVault <- create FungibleToken.Vault(balance: 10) ``

## Account access[​](#account-access "Direct link to Account access")

Contracts can access the account they are deployed to — contracts have the implicit field named `account`, which is only accessible within the contract:

`` _10

let account: auth(Storage, Keys, Contracts, Inbox, Capabilities) &Account`, ``

The account reference is fully entitled, so it grants access to the account's storage, keys, contracts, and so on.

For example, the following gives the contract the ability to write to the account's storage when the contract is initialized:

`_10

init(balance: Int) {

_10

self.account.storage.save(

_10

<-create Vault(balance: 1000),

_10

to: /storage/initialVault

_10

)

_10

}`

## Contract interfaces[​](#contract-interfaces "Direct link to Contract interfaces")

Like composite types, contracts can have [interfaces](/docs/language/interfaces) that specify rules about their behavior, their types, and the behavior of their types.

Contract interfaces have to be declared globally. Declarations cannot be nested in other types.

Contract interfaces may not declare concrete types (other than events), but they can declare interfaces. If a contract interface declares an interface type, the implementing contract does not have to also define that interface. They can refer to that nested interface by saying `{ContractInterfaceName}.{NestedInterfaceName}`:

`` _31

// Declare a contract interface that declares an interface and a resource

_31

// that needs to implement that interface in the contract implementation.

_31

//

_31

access(all)

_31

contract interface InterfaceExample {

_31

_31

// Implementations do not need to declare this

_31

// They refer to it as InterfaceExample.NestedInterface

_31

//

_31

access(all)

_31

resource interface NestedInterface {}

_31

_31

// Implementations must declare this type

_31

//

_31

access(all)

_31

resource Composite: NestedInterface {}

_31

}

_31

_31

access(all)

_31

contract ExampleContract: InterfaceExample {

_31

_31

// The contract doesn't need to redeclare the `NestedInterface` interface

_31

// because it is already declared in the contract interface

_31

_31

// The resource has to refer to the resource interface using the name

_31

// of the contract interface to access it

_31

//

_31

access(all)

_31

resource Composite: InterfaceExample.NestedInterface {

_31

}

_31

} ``

## `Account.Contracts`[​](#accountcontracts "Direct link to accountcontracts")

An account exposes its inbox through the `contracts` field, which has the type `Account.Contracts`:

`` _71

access(all)

_71

struct Contracts {

_71

_71

/// The names of all contracts deployed in the account.

_71

access(all)

_71

let names: [String]

_71

_71

/// Returns the deployed contract for the contract/contract interface with the given name in the account, if any.

_71

///

_71

/// Returns nil if no contract/contract interface with the given name exists in the account.

_71

access(all)

_71

view fun get(name: String): DeployedContract?

_71

_71

/// Returns a reference of the given type to the contract with the given name in the account, if any.

_71

///

_71

/// Returns nil if no contract with the given name exists in the account,

_71

/// or if the contract does not conform to the given type.

_71

access(all)

_71

view fun borrow<T: &Any>(name: String): T?

_71

_71

/// Adds the given contract to the account.

_71

///

_71

/// The `code` parameter is the UTF-8 encoded representation of the source code.

_71

/// The code must contain exactly one contract or contract interface,

_71

/// which must have the same name as the `name` parameter.

_71

///

_71

/// All additional arguments that are given are passed further to the initializer

_71

/// of the contract that is being deployed.

_71

///

_71

/// The function fails if a contract/contract interface with the given name already exists in the account,

_71

/// if the given code does not declare exactly one contract or contract interface,

_71

/// or if the given name does not match the name of the contract/contract interface declaration in the code.

_71

///

_71

/// Returns the deployed contract.

_71

access(Contracts | AddContract)

_71

fun add(

_71

name: String,

_71

code: [UInt8]

_71

): DeployedContract

_71

_71

/// Updates the code for the contract/contract interface in the account.

_71

///

_71

/// The `code` parameter is the UTF-8 encoded representation of the source code.

_71

/// The code must contain exactly one contract or contract interface,

_71

/// which must have the same name as the `name` parameter.

_71

///

_71

/// Does **not** run the initializer of the contract/contract interface again.

_71

/// The contract instance in the world state stays as is.

_71

///

_71

/// Fails if no contract/contract interface with the given name exists in the account,

_71

/// if the given code does not declare exactly one contract or contract interface,

_71

/// or if the given name does not match the name of the contract/contract interface declaration in the code.

_71

///

_71

/// Returns the deployed contract for the updated contract.

_71

access(Contracts | UpdateContract)

_71

fun update(name: String, code: [UInt8]): DeployedContract

_71

_71

/// Removes the contract/contract interface from the account which has the given name, if any.

_71

///

_71

/// Returns the removed deployed contract, if any.

_71

///

_71

/// Returns nil if no contract/contract interface with the given name exists in the account.

_71

access(Contracts | RemoveContract)

_71

fun remove(name: String): DeployedContract?

_71

}

_71

_71

entitlement Contracts

_71

_71

entitlement AddContract

_71

entitlement UpdateContract

_71

entitlement RemoveContract ``

## Deployed contract[​](#deployed-contract "Direct link to Deployed contract")

Accounts store *deployed contracts*, which is the code of the contract:

```` _32

access(all)

_32

struct DeployedContract {

_32

/// The address of the account where the contract is deployed at.

_32

access(all)

_32

let address: Address

_32

_32

/// The name of the contract.

_32

access(all)

_32

let name: String

_32

_32

/// The code of the contract.

_32

access(all)

_32

let code: [UInt8]

_32

_32

/// Returns an array of `Type` objects representing all the public type declarations in this contract

_32

/// (e.g. structs, resources, enums).

_32

///

_32

/// For example, given a contract

_32

/// ```

_32

/// contract Foo {

_32

///

_32

/// access(all)

_32

/// struct Bar {...}

_32

///

_32

/// access(all)

_32

/// resource Qux {...}

_32

/// }

_32

/// ```

_32

/// then `.publicTypes()` will return an array equivalent to the expression `[Type<Bar>(), Type<Qux>()]`

_32

access(all)

_32

view fun publicTypes(): [Type]

_32

} ````

note

This example is *type only*, which provides information about a deployed contract. it is not the contract instance, which is the result of importing a contract.

## Getting a deployed contract[​](#getting-a-deployed-contract "Direct link to Getting a deployed contract")

The function `contracts.get` retrieves a deployed contract:

`_10

access(all)

_10

view fun get(name: String): DeployedContract?`

The function returns the [deployed contract](#deployed-contract) with the given name, if any. If no contract with the given name exists in the account, the function returns `nil`.

For example, assuming that an account has a contract named `Test` deployed to it, the contract can be retrieved as follows:

`_10

let account = getAccount(0x1)

_10

let contract = account.contracts.get(name: "Test")`

## Borrowing a deployed contract[​](#borrowing-a-deployed-contract "Direct link to Borrowing a deployed contract")

Contracts can be *borrowed* to effectively perform a dynamic import dependent on a specific execution path.

This is in contrast to a typical import statement (e.g., `import T from 0x1`), which statically imports a contract.

The `contracts.borrow` function obtains a reference to a contract instance:

`_10

access(all)

_10

view fun borrow<T: &Any>(name: String): T?`

The functions returns a reference to the contract instance stored with that name on the account, if it exists, and if it has the provided type `T`. If no contract with the given name exists in the account, the function returns `nil`.

For example, assuming that a contract named `Test`, which conforms to the `TestInterface` interface is deployed to an account, a reference to the contract instance can be obtained as follows:

`_10

let account = getAccount(0x1)

_10

let contract: &TestInterface = account.contracts.borrow<&TestInterface>(name: "Test")`

This is similar to the import statement:

`_10

import Test from 0x1`

## Deploying a new contract[​](#deploying-a-new-contract "Direct link to Deploying a new contract")

The `contracts.add` function deploys a new contract to an account:

`_10

access(Contracts | AddContract)

_10

fun add(

_10

name: String,

_10

code: [UInt8],

_10

... contractInitializerArguments

_10

): DeployedContract`

Calling the `add` function requires access to an account via a reference that is authorized with the coarse-grained `Contracts` entitlement (`auth(Contracts) &Account`), or the fine-grained `AddContract` entitlement (`auth(AddContract) &Account`).

The `code` parameter is the UTF-8 encoded representation of the source code. The code must contain exactly one contract or contract interface, which must have the same name as the `name` parameter.

The `add` function passes all extra arguments of the call (`contractInitializerArguments`) to the initializer of the contract.

If a contract with the given name already exists in the account, if the given code does not declare exactly one contract or contract interface, or if the given name does not match the name of the contract declaration in the code, then the function aborts the program.

When the deployment succeeds, the function returns the [deployed contract](#deployed-contract).

For example, assume the following contract code should be deployed:

`_10

access(all)

_10

contract Test {

_10

_10

access(all)

_10

let message: String

_10

_10

init(message: String) {

_10

self.message = message

_10

}

_10

}`

The contract can then be deployed as follows:

`_10

transaction(code: String) {

_10

prepare(signer: auth(AddContract) &Account) {

_10

signer.contracts.add(

_10

name: "Test",

_10

code: code.utf8,

_10

message: "I'm a new contract in an existing account"

_10

)

_10

}

_10

}`

## Updating a deployed contract[​](#updating-a-deployed-contract "Direct link to Updating a deployed contract")

The `contracts.update` function updates the code of an existing contract:

`_10

access(Contracts | UpdateContract)

_10

fun update(name: String, code: [UInt8]): DeployedContract`

Calling the `update` function requires access to an account via a reference that is authorized with the coarse-grained `Contracts` entitlement (`auth(Contracts) &Account`), or the fine-grained `UpdateContract` entitlement (`auth(UpdateContract) &Account`).

The `code` parameter is the UTF-8 encoded representation of the source code. The code must contain exactly one contract or contract interface, which must have the same name as the `name` parameter.

If no contract with the given name exists in the account, if the given code does not declare exactly one contract or contract interface, or if the given name does not match the name of the contract declaration in the code, then the function aborts the program.

When the update succeeds, the function returns the [deployed contract](#deployed-contract).

warning

The `update` function does **not** run the initializer of the contract again.

Updating a contract does **not** change the contract instance and its existing stored data. A contract update only changes the code of a contract.

It is only possible to update contracts in ways that keep data consistency. [Certain restrictions apply](/docs/language/contract-updatability).

For example, assume that a contract named `Test` is already deployed to the account, and it should be updated with the following contract code:

`_10

access(all)

_10

contract Test {

_10

_10

access(all)

_10

let message: String

_10

_10

init(message: String) {

_10

self.message = message

_10

}

_10

}`

The contract can be updated as follows:

`_10

transaction(code: String) {

_10

prepare(signer: auth(UpdateContract) &Account) {

_10

signer.contracts.update(

_10

name: "Test",

_10

code: code

_10

)

_10

}

_10

}`

## Removing a deployed contract[​](#removing-a-deployed-contract "Direct link to Removing a deployed contract")

The `contracts.remove` function removes a deployed contract from an account:

`_10

access(Contracts | RemoveContract)

_10

fun remove(name: String): DeployedContract?`

Calling the `remove` function requires access to an account via a reference that is authorized with the coarse-grained `Contracts` entitlement (`auth(Contracts) &Account`), or the fine-grained `RemoveContract` entitlement (`auth(RemoveContract) &Account`).

The function removes the contract from the account that has the given name and returns it. If no contract with the given name exists in the account, the function returns `nil`.

For example, assuming that a contract named `Test` is deployed to an account, the contract can be removed as follows:

`_10

transaction(code: String) {

_10

prepare(signer: auth(RemoveContract) &Account) {

_10

signer.contracts.remove(name: "Test",)

_10

}

_10

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/contracts.mdx)

[Previous

Attachments](/docs/language/attachments)[Next

Contract Updatability](/docs/language/contract-updatability)

###### Rate this page

😞😐😊

* [Account access](#account-access)
* [Contract interfaces](#contract-interfaces)
* [`Account.Contracts`](#accountcontracts)
* [Deployed contract](#deployed-contract)
* [Getting a deployed contract](#getting-a-deployed-contract)
* [Borrowing a deployed contract](#borrowing-a-deployed-contract)
* [Deploying a new contract](#deploying-a-new-contract)
* [Updating a deployed contract](#updating-a-deployed-contract)
* [Removing a deployed contract](#removing-a-deployed-contract)