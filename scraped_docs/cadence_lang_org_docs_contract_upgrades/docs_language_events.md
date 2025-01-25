# Source: https://cadence-lang.org/docs/language/events




Events | Cadence




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
* Events
On this page
# Events

Events are special values that can be emitted during the execution of a program.

An event type can be declared with the `event` keyword.

 `_10event FooEvent(x: Int, y: Int)`

The syntax of an event declaration is similar to that of
a [function declaration](/docs/language/functions#function-declarations);
events contain named parameters, each of which has an optional argument label.

Event parameters may only have a valid event parameter type.
Valid types are boolean, string, integer, arrays and dictionaries of these types,
and structures where all fields have a valid event parameter type.
Resource types are not allowed, because when a resource is used as an argument, it is moved.

Events can only be declared within a [contract](/docs/language/contracts) body.
Events cannot be declared globally or within resource or struct types.

 `_15// Invalid: An event cannot be declared globally_15//_15event GlobalEvent(field: Int)_15_15access(all)_15contract Events {_15 // Event with explicit argument labels_15 //_15 event BarEvent(labelA fieldA: Int, labelB fieldB: Int)_15_15 // Invalid: A resource type is not allowed to be used_15 // because it would be moved and lost_15 //_15 event ResourceEvent(resourceField: @Vault)_15}`
### Emitting events[​](#emitting-events "Direct link to Emitting events")

To emit an event from a program, use the `emit` statement:

 `_16access(all)_16contract Events {_16 event FooEvent(x: Int, y: Int)_16_16 // Event with argument labels_16 event BarEvent(labelA fieldA: Int, labelB fieldB: Int)_16_16 fun events() {_16 emit FooEvent(x: 1, y: 2)_16_16 // Emit event with explicit argument labels_16 // Note that the emitted event will only contain the field names,_16 // not the argument labels used at the invocation site._16 emit BarEvent(labelA: 1, labelB: 2)_16 }_16}`

Emitting events has the following restrictions:

* Events can only be invoked in an `emit` statement.
  
  This means events cannot be assigned to variables or used as function parameters.
* Events can only be emitted from the location in which they are declared.
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/events.md)[PreviousTransactions](/docs/language/transactions)[NextCore Events](/docs/language/core-events)
###### Rate this page

😞😐😊

* [Emitting events](#emitting-events)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

