# Source: https://cadence-lang.org/docs/language/syntax




Syntax | Cadence




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
* Syntax
On this page
# Syntax

## Comments[​](#comments "Direct link to Comments")

Comments can be used to document code.
A comment is text that is not executed.

*Single-line comments* start with two slashes (`//`).
These comments can go on a line by themselves or they can go directly after a line of code.

 `_10// This is a comment on a single line._10// Another comment line that is not executed._10_10let x = 1 // Here is another comment after a line of code.`

*Multi-line comments* start with a slash and an asterisk (`/*`)
and end with an asterisk and a slash (`*/`):

 `_10/* This is a comment which_10spans multiple lines. */`

Comments may be nested.

 `_10/* /* this */ is a valid comment */`

Multi-line comments are balanced.

 `_10/* this is a // comment up to here */ this is not part of the comment */`
### Documentation Comments[​](#documentation-comments "Direct link to Documentation Comments")

Documentation comments (also known as "doc-strings" or "doc-comment") are a special set of comments that can be
processed by tools, for example to generate human-readable documentation, or provide documentation in an IDE.

Doc-comments either start with three slashes (`///`) on each line,
or are surrounded by `/**` and `**/`.

 `_10/// This is a documentation comment for `x`._10/// It spans multiple lines._10_10let x = 1`
 `_10/**_10 This is a documentation comment_10 which also spans multiple lines._10**/`
## Identifiers[​](#identifiers "Direct link to Identifiers")

Identifiers may start with any upper or lowercase letter (A-Z, a-z)
or an underscore (`_`).
This may be followed by zero or more upper and lower case letters,
underscores, and numbers (0-9).
Identifiers may not begin with a number.

 `_29// Valid: title-case_29//_29PersonID_29_29// Valid: with underscore_29//_29token_name_29_29// Valid: leading underscore and characters_29//_29_balance_29_29// Valid: leading underscore and numbers_29_8264_29_29// Valid: characters and number_29//_29account2_29_29// Invalid: leading number_29//_291something_29_29// Invalid: invalid character #_29_#1_29_29// Invalid: various invalid characters_29//_29!@#$%^&*`
### Reserved identifiers[​](#reserved-identifiers "Direct link to Reserved identifiers")

The following identifiers are reserved, as they are keywords of the language:

* `if`, `else`, `while`, `for`, `in`, `as`
* `break`, `continue`, `return`
* `true`, `false`, `nil`
* `let`, `var`
* `create`, `destroy`, `emit`
* `fun`, `pre`, `post`,
* `auth`, `access`
* `self`, `init`
* `contract`, `event`, `struct`, `resource`, `interface`,
  `entitlement`, `enum`, `mapping`, `attachment`, `result`
* `transaction`, `prepare`, `execute`
* `switch`, `case`, `default`
* `import`, `include`
* `require`, `requires`, `static`, `native`, `pub`, `priv`, `try`, `catch`, `finally`,
  `goto`, `const`, `export`, `throw`, `throws`, `where`, `final`, `internal`, `typealias`,
  `repeat`, `guard`, `is`

### Conventions[​](#conventions "Direct link to Conventions")

By convention, variables, constants, and functions have lowercase identifiers;
and types have title-case identifiers.

## Semicolons[​](#semicolons "Direct link to Semicolons")

Semicolons (;) are used as separators between declarations and statements.
A semicolon can be placed after any declaration and statement,
but can be omitted between declarations and if only one statement appears on the line.

Semicolons must be used to separate multiple statements if they appear on the same line.

 `_11// Declare a constant, without a semicolon._11//_11let a = 1_11_11// Declare a variable, with a semicolon._11//_11var b = 2;_11_11// Declare a constant and a variable on a single line, separated by semicolons._11//_11let d = 1; var e = 2`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/syntax.md)[PreviousLanguage Reference](/docs/language/)[NextConstants and Variable Declarations](/docs/language/constants-and-variables)
###### Rate this page

😞😐😊

* [Comments](#comments)
  + [Documentation Comments](#documentation-comments)
* [Identifiers](#identifiers)
  + [Reserved identifiers](#reserved-identifiers)
  + [Conventions](#conventions)
* [Semicolons](#semicolons)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

