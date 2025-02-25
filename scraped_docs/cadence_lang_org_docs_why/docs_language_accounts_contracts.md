# Source: https://cadence-lang.org/docs/language/accounts/contracts

Contracts | Cadence



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

    - [Paths](/docs/language/accounts/paths)
    - [Storage](/docs/language/accounts/storage)
    - [Capabilities](/docs/language/accounts/capabilities)
    - [Keys](/docs/language/accounts/keys)
    - [Contracts](/docs/language/accounts/contracts)
    - [Inbox](/docs/language/accounts/inbox)
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
* [Accounts](/docs/language/accounts/)
* Contracts

On this page

# Contracts

Accounts store [contracts](/docs/language/contracts).
A contract can also just be an [interface](/docs/language/interfaces).

An account exposes its inbox through the `contracts` field,
which has the type `Account.Contracts`.

## `Account.Contracts`[​](#accountcontracts "Direct link to accountcontracts")

`_71

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

entitlement RemoveContract`

## Deployed contract[​](#deployed-contract "Direct link to Deployed contract")

Accounts store "deployed contracts," that is, the code of the contract:

`_32

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

}`

Note that this is type only provides information about a deployed contract,
it is not the contract instance, the result of importing a contract.

## Getting a deployed contract[​](#getting-a-deployed-contract "Direct link to Getting a deployed contract")

The function `contracts.get` retrieves a deployed contract:

`_10

access(all)

_10

view fun get(name: String): DeployedContract?`

The function returns the [deployed contract](#deployed-contract) with the given name, if any.
If no contract with the given name exists in the account, the function returns `nil`.

For example, assuming that an account has a contract named `Test` deployed to it,
the contract can be retrieved as follows:

`_10

let account = getAccount(0x1)

_10

let contract = account.contracts.get(name: "Test")`

## Borrowing a deployed contract[​](#borrowing-a-deployed-contract "Direct link to Borrowing a deployed contract")

Contracts can be "borrowed" to effectively perform a dynamic import dependent on a specific execution path.

This is in contrast to a typical import statement, for example `import T from 0x1`,
which statically imports a contract.

The `contracts.borrow` function obtains a reference to a contract instance:

`_10

access(all)

_10

view fun borrow<T: &Any>(name: String): T?`

The functions returns a reference to the contract instance stored with that name on the account,
if it exists, and if it has the provided type `T`.
If no contract with the given name exists in the account, the function returns `nil`.

For example, assuming that a contract named `Test`
which conforms to the `TestInterface` interface is deployed to an account,
a reference to the contract instance can obtained be as follows:

`_10

let account = getAccount(0x1)

_10

let contract: &TestInterface = account.contracts.borrow<&TestInterface>(name: "Test")`

This is similar to the import statement

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

Calling the `add` function requires access to an account via a reference which is authorized
with the coarse-grained `Contracts` entitlement (`auth(Contracts) &Account`),
or the fine-grained `AddContract` entitlement (`auth(AddContract) &Account`).

The `code` parameter is the UTF-8 encoded representation of the source code.
The code must contain exactly one contract or contract interface,
which must have the same name as the `name` parameter.

The `add` function passes all extra arguments of the call (`contractInitializerArguments`)
to the initializer of the contract.

If a contract with the given name already exists in the account,
if the given code does not declare exactly one contract or contract interface,
or if the given name does not match the name of the contract declaration in the code,
then the function aborts the program.

When the deployment succeeded, the function returns the [deployed contract](#deployed-contract).

For example, assuming the following contract code should be deployed:

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

The contract can be deployed as follows:

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

Calling the `update` function requires access to an account via a reference which is authorized
with the coarse-grained `Contracts` entitlement (`auth(Contracts) &Account`),
or the fine-grained `UpdateContract` entitlement (`auth(UpdateContract) &Account`).

The `code` parameter is the UTF-8 encoded representation of the source code.
The code must contain exactly one contract or contract interface,
which must have the same name as the `name` parameter.

If no contract with the given name exists in the account,
if the given code does not declare exactly one contract or contract interface,
or if the given name does not match the name of the contract declaration in the code,
then the function aborts the program.

When the update succeeded, the function returns the [deployed contract](#deployed-contract).

warning

The `update` function does **not** run the initializer of the contract again.

Updating a contract does **not** change the contract instance and its existing stored data.
A contract update only changes the code a contract.

Is only possible to update contracts in ways that keep data consistency.
[Certain restrictions apply](/docs/language/contract-updatability).

For example, assuming that a contract named `Test` is already deployed to the account,
and it should be updated with the following contract code:

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

Calling the `remove` function requires access to an account via a reference which is authorized
with the coarse-grained `Contracts` entitlement (`auth(Contracts) &Account`),
or the fine-grained `RemoveContract` entitlement (`auth(RemoveContract) &Account`).

The function removes the contract from the account which has the given name and returns it.
If no contract with the given name exists in the account, the function returns `nil`.

For example, assuming that a contract named `Test` is deployed to an account,
the contract can be removed as follows:

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

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/contracts.mdx)

[Previous

Keys](/docs/language/accounts/keys)[Next

Inbox](/docs/language/accounts/inbox)

###### Rate this page

😞😐😊

* [`Account.Contracts`](#accountcontracts)
* [Deployed contract](#deployed-contract)
* [Getting a deployed contract](#getting-a-deployed-contract)
* [Borrowing a deployed contract](#borrowing-a-deployed-contract)
* [Deploying a new contract](#deploying-a-new-contract)
* [Updating a deployed contract](#updating-a-deployed-contract)
* [Removing a deployed contract](#removing-a-deployed-contract)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.