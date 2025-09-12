# Source: https://cadence-lang.org/docs/language/transactions

Transactions | Cadence



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
* Transactions

On this page

# Transactions

Transactions are objects that are signed with keys of one or more [accounts](/docs/language/accounts/) and are sent to the chain to interact with it and perform state changes.

Transactions can [import](/docs/language/imports) any number of types from any account using the import syntax:

`_10

import FungibleToken from 0x01`

A transaction is declared using the `transaction` keyword and its contents are contained in curly braces.

The body of the transaction can declare local variables that are valid throughout the whole of the transaction:

`_10

transaction {

_10

// transaction contents

_10

let localVar: Int

_10

_10

// ...

_10

}`

## Transaction parameters[​](#transaction-parameters "Direct link to Transaction parameters")

Transactions can have parameters and they are declared like function parameters. The arguments for the transaction are passed along with the transaction.

Transaction parameters are accessible throughout the whole of the transaction:

`` _10

// Declare a transaction which has one parameter named `amount`

_10

// that has the type `UFix64`

_10

//

_10

transaction(amount: UFix64) {

_10

_10

} ``

## Transaction phases[​](#transaction-phases "Direct link to Transaction phases")

Transactions are executed in four phases: preparation, pre-conditions, execution, and post-conditions, in that order. The preparation and execution phases are blocks of code that execute sequentially. The pre-conditions and post-condition are just like [conditions in functions](/docs/language/pre-and-post-conditions#function-pre-conditions-and-post-conditions).

The following empty Cadence transaction has no logic, but demonstrates the syntax for each phase, in the order these phases are executed:

`_17

transaction {

_17

prepare(signer1: &Account, signer2: &Account) {

_17

// ...

_17

}

_17

_17

pre {

_17

// ...

_17

}

_17

_17

execute {

_17

// ...

_17

}

_17

_17

post {

_17

// ...

_17

}

_17

}`

Although optional, each phase serves a specific purpose when executing a transaction. It's recommended that developers use these phases when creating their transactions. These phases **must** be defined in this order.

### Prepare phase[​](#prepare-phase "Direct link to Prepare phase")

The `prepare` phase is used when the transaction needs access to the accounts that signed (authorized) the transaction.

Access to the signing accounts is **only possible inside the `prepare` phase**.

For each signer of the transaction, a [reference](/docs/language/references) to the signing account is passed as an argument to the `prepare` phase. The reference may be authorized, requesting certain [access to the account](/docs/language/accounts/#accessing-an-account).

For example, if the transaction has two signers, the prepare **must** have two parameters of type `&Account`:

`_10

prepare(signer1: &Account, signer2: &Account) {

_10

// ...

_10

}`

For instance, to request write access to an [account's storage](/docs/language/accounts/storage), the transaction can request an authorized reference:

`_10

prepare(signer: auth(Storage) &Account) {

_10

// ...

_10

}`

As a best practice, only use the `prepare` phase to define and execute logic that requires [write access](/docs/language/accounts/#write-operations) to the signing accounts, and *move all other logic elsewhere*.

Modifications to accounts can have significant implications, so keep this phase clear of unrelated logic. This ensures that users can easily read and understand the logic of the transaction and how it affects their account.

The prepare phase serves a similar purpose as the [initializer of a composite](/docs/language/types-and-type-system/composite-types#composite-type-fields).

For example, if a transaction performs a token transfer, put the withdrawal in the `prepare` phase since it requires access to the account storage, but perform the deposit in the `execute` phase.

### Pre-conditions[​](#pre-conditions "Direct link to Pre-conditions")

Pre-conditions are optional and are declared in a `pre` block and are executed after the `prepare` phase. For example, a pre-condition might check the balance before transferring tokens between accounts:

`_10

pre {

_10

sendingAccount.balance > 0

_10

}`

If any of the pre-conditions fail, then the remainder of the transaction is not executed and it is completely reverted.

See [pre-conditions](/docs/language/pre-and-post-conditions#transaction-pre-conditions) for more information.

### Execute phase[​](#execute-phase "Direct link to Execute phase")

The `execute` block executes the main logic of the transaction. This phase is optional, but it is a best practice to add your main transaction logic in this section so it is explicit.

It is impossible to access the references to the transaction's signing accounts in the `execute` phase:

`` _12

transaction {

_12

prepare(signer: auth(LoadValue) &Account) {}

_12

_12

execute {

_12

// Invalid: Cannot access the `signer` account reference, as it is not in scope

_12

let resource <- signer.storage.load<@Resource>(from: /storage/resource)

_12

destroy resource

_12

_12

// Valid: Can obtain an unauthorized reference to any account

_12

let otherAccount = getAccount(0x3)

_12

}

_12

} ``

### Post-conditions[​](#post-conditions "Direct link to Post-conditions")

Transaction post-conditions are just like [post-conditions of functions](/docs/language/pre-and-post-conditions#transaction-post-conditions).

Post-conditions are optional and are declared in a `post` block. They are executed after the execution phase and are used to verify that the transaction logic has been executed properly. The block can have zero or more conditions.

For example, a token transfer transaction can ensure that the final balance has a certain value:

`_10

post {

_10

signer.balance == 30.0: "Balance after transaction is incorrect!"

_10

}`

If any of the post-conditions fail, then the transaction fails and is completely reverted.

See [post-conditions](/docs/language/pre-and-post-conditions#transaction-post-conditions) for details.

## Summary[​](#summary "Direct link to Summary")

Transactions use phases to make the transaction's code/intent more readable. They provide a way for developers to separate the transaction logic. Transactions also provide a way to check the state prior/after transaction execution, to prevent the transaction from running, or reverting changes made by the transaction if needed.

The following is a brief summary of how to use the `prepare`, `pre`, `execute`, and `post` blocks in a transaction to implement the transaction's phases:

`_33

transaction {

_33

prepare(signer1: &Account) {

_33

// Access signing accounts of the transaction.

_33

//

_33

// Avoid logic that does not need access to the signing accounts.

_33

//

_33

// The signing accounts can't be accessed anywhere else in the transaction.

_33

}

_33

_33

pre {

_33

// Define conditions that must be true

_33

// for the transaction to execute.

_33

//

_33

// Define the expected state of things

_33

// as they should be before the transaction is executed.

_33

}

_33

_33

execute {

_33

// The main transaction logic goes here, but you can access

_33

// any public information or resources published by any account.

_33

}

_33

_33

post {

_33

// Define conditions that must be true

_33

// for the transaction to be committed.

_33

//

_33

// Define the expected state of things

_33

// as they should be after the transaction executed.

_33

//

_33

// Also used to provide information about what changes

_33

// the transaction will make to the signing accounts.

_33

}

_33

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/transactions.md)

[Previous

Contract Updatability](/docs/language/contract-updatability)[Next

Events](/docs/language/events)

###### Rate this page

😞😐😊

* [Transaction parameters](#transaction-parameters)
* [Transaction phases](#transaction-phases)
  + [Prepare phase](#prepare-phase)
  + [Pre-conditions](#pre-conditions)
  + [Execute phase](#execute-phase)
  + [Post-conditions](#post-conditions)
* [Summary](#summary)