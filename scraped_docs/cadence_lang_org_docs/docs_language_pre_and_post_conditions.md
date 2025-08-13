# Source: https://cadence-lang.org/docs/language/pre-and-post-conditions

Pre- and Post-Conditions | Cadence



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
* Pre- and Post-Conditions

On this page

# Pre- and Post-Conditions

Pre-conditions and post-conditions are a unique and powerful feature of Cadence that allow you to specify conditions for execution that must be met for transactions and functions. If they're not met, execution stops and the transaction is reverted. One use is to define specific inputs and outputs for a transaction that make it easy to see what will be transferred, regardless of how complex the transaction execution becomes. This property is particularly useful in using code written by an AI.

To mock out an example:

> **Pre-condition**: The user has 50 Flow.

> **Execution**: Massively complex operation involving swaps between three different currencies, two dexes, and an NFT marketplace.

> **Post-condition**: The user has at least 30 Flow remaining, and owns SuperCoolCollection NFT #54.

## Function pre-conditions and post-conditions[​](#function-pre-conditions-and-post-conditions "Direct link to Function pre-conditions and post-conditions")

Functions may have pre-conditions and may have post-conditions. They can be used to restrict the inputs (values for parameters) and output (return value) of a function.

* Pre-conditions must be true right before the execution of the function. They are part of the function and introduced by the `pre` keyword, followed by the condition block.
* Post-conditions must be true right after the execution of the function. Post-conditions are part of the function and introduced by the `post` keyword, followed by the condition block.
* A conditions block consists of one or more conditions. Conditions are expressions evaluating to a boolean.
* Conditions may be written on separate lines, or multiple conditions can be written on the same line, separated by a semicolon. This syntax follows the syntax for [statements](/docs/language/syntax#semicolons).
* Following each condition, an optional description can be provided after a colon. The condition description is used as an error message when the condition fails.

In post-conditions, the special constant `result` refers to the result of the function:

`` _27

fun factorial(_ n: Int): Int {

_27

pre {

_27

// Require the parameter `n` to be greater than or equal to zero.

_27

//

_27

n >= 0:

_27

"factorial is only defined for integers greater than or equal to zero"

_27

}

_27

post {

_27

// Ensure the result will be greater than or equal to 1.

_27

//

_27

result >= 1:

_27

"the result must be greater than or equal to 1"

_27

}

_27

_27

if n < 1 {

_27

return 1

_27

}

_27

_27

return n * factorial(n - 1)

_27

}

_27

_27

factorial(5) // is `120`

_27

_27

// Run-time error: The given argument does not satisfy

_27

// the pre-condition `n >= 0` of the function, the program aborts.

_27

//

_27

factorial(-2) ``

In post-conditions, the special function `before` can be used to get the value of an expression just before the function is called:

`` _12

var n = 0

_12

_12

fun incrementN() {

_12

post {

_12

// Require the new value of `n` to be the old value of `n`, plus one.

_12

//

_12

n == before(n) + 1:

_12

"n must be incremented by 1"

_12

}

_12

_12

n = n + 1

_12

} ``

Both pre-conditions and post-conditions are considered [`view` contexts](/docs/language/functions#view-functions); any operations that are not legal in functions with `view` annotations are also not allowed in conditions. In particular, this means that if you wish to call a function in a condition, that function must be `view`.

## Transaction pre-conditions[​](#transaction-pre-conditions "Direct link to Transaction pre-conditions")

Transaction pre-conditions function in the same way as [pre-conditions of functions](#function-pre-conditions-and-post-conditions).

Pre-conditions are optional and are declared in a `pre` block. They are executed after the `prepare` phase, and are used for checking if explicit conditions hold before executing the remainder of the transaction. The block can have zero or more conditions.

For example, a pre-condition might check the balance before transferring tokens between accounts:

`_10

pre {

_10

sendingAccount.balance > 0

_10

}`

If any of the pre-conditions fail, then the remainder of the transaction is not executed and it is completely reverted.

## Transaction post-conditions[​](#transaction-post-conditions "Direct link to Transaction post-conditions")

Transaction post-conditions are just like [post-conditions of functions](#function-pre-conditions-and-post-conditions).

Post-conditions are optional and are declared in a `post` block. They are executed after the execution phase, and are used to verify that the transaction logic has been executed properly. The block can have zero or more conditions.

For example, a token transfer transaction can ensure that the final balance has a certain value:

`_10

post {

_10

signer.balance == 30.0: "Balance after transaction is incorrect!"

_10

}`

If any of the post-conditions fail, then the transaction fails and is completely reverted.

## Pre- and post-conditions in interfaces[​](#pre--and-post-conditions-in-interfaces "Direct link to Pre- and post-conditions in interfaces")

Interfaces can also define pre- and post-conditions. See the [interfaces](/docs/language/interfaces) article for more information.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/pre-and-post-conditions.md)

[Previous

Functions](/docs/language/functions)[Next

Built-in Functions](/docs/language/built-in-functions)

###### Rate this page

😞😐😊

* [Function pre-conditions and post-conditions](#function-pre-conditions-and-post-conditions)
* [Transaction pre-conditions](#transaction-pre-conditions)
* [Transaction post-conditions](#transaction-post-conditions)
* [Pre- and post-conditions in interfaces](#pre--and-post-conditions-in-interfaces)