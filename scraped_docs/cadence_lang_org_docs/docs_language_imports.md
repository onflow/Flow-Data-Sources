# Source: https://cadence-lang.org/docs/language/imports

Imports | Cadence



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
* Imports

On this page

# Imports

Programs can import declarations (types, functions, variables, and so on) from other programs.

## Importing contracts[​](#importing-contracts "Direct link to Importing contracts")

Imports are declared using the `import` keyword. You can import your contracts using **one** of the following three options:

1. Import your contracts by name, which you must use if you're using the [Flow CLI](https://developers.flow.com/tools/flow-cli/index.md). For example:

   `_10

   import "HelloWorld"`

   This will automatically import the contract, based on the configuration found `flow.json`. It will automatically handle address changes between mainnet, testnet, and emulator, as long as those are present in `flow.json`.
2. Import your contracts by an address, which imports all declarations. Both [Flow playground](https://play.flow.com/) and [Flow runner](https://run.dnz.dev/) require importing by address.
3. Import your contracts by the names of the declarations that should be imported, followed by the `from` keyword, and then followed by the address.

   * If importing a local file, the location is a string literal, as well as the path to the file. Deployment of code with file imports requires usage of the [Flow CLI](https://developers.flow.com/tools/flow-cli/index.md).
   * If importing an external type in a different account, the location is an address literal, as well as the address of the account where the declarations are deployed to and published.

   `` _10

   // Import the type `Counter` from a local file.

   _10

   //

   _10

   import Counter from "./examples/counter.cdc"

   _10

   _10

   // Import the type `Counter` from an external account.

   _10

   //

   _10

   import Counter from 0x299F20A29311B9248F12 ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/imports.mdx)

[Previous

References](/docs/language/references)[Next

Attachments](/docs/language/attachments)

###### Rate this page

😞😐😊

* [Importing contracts](#importing-contracts)