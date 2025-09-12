# Source: https://cadence-lang.org/docs/language/resources

Resources | Cadence



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
* Resources

On this page

# Resources

Resources are types that can only exist in **one** location at a time and **must** be used **exactly once**.

Resources **must** be created (instantiated) by using the `create` keyword.

Before the closing bracket of a function that has resources created or moved into scope, those resources **must** explicitly be either **moved** to a valid storage location or **destroyed**.

They are **moved** when used as an initial value for a constant or variable, when assigned to a different variable, when passed as an argument to a function, and when returned from a function.

Resources can be explicitly **destroyed** using the `destroy` keyword.

Accessing a field or calling a function of a resource does not move or destroy it.

When the resource is moved, the constant or variable that referred to the resource before the move becomes **invalid**. An **invalid** resource cannot be used again.

To make the usage and behavior of resource types explicit, the prefix `@` must be used in type annotations of variable or constant declarations, parameters, and return types.

## The move operator (`<-`)[​](#the-move-operator-- "Direct link to the-move-operator--")

To make moves of resources explicit, the move operator `<-` must be used when the resource is the initial value of a constant or variable, when it is moved to a different variable, when it is moved to a function as an argument, and when it is returned from a function.

Declare a resource named `SomeResource`, with a variable-integer field:

`_10

access(all)

_10

resource SomeResource {

_10

_10

access(all)

_10

var value: Int

_10

_10

init(value: Int) {

_10

self.value = value

_10

}

_10

}`

Declare a constant with a value of resource type `SomeResource`:

`_10

let a: @SomeResource <- create SomeResource(value: 5)`

*Move* the resource value to a new constant:

`` _11

let b <- a

_11

_11

_11

// Invalid Line Below: Cannot use constant `a` anymore as the resource that it

_11

// referred to was moved to constant `b`.

_11

_11

a.value

_11

_11

// Constant `b` owns the resource.

_11

_11

b.value // equals 5 ``

Declare a function that accepts a resource. The parameter has a resource type, so the type annotation must be prefixed with `@`:

`_10

access(all)

_10

fun use(resource: @SomeResource) {

_10

// ...

_10

}`

Call function `use`, and move the resource into it:

`` _10

use(resource: <-b)

_10

_10

// Invalid Line Below: Cannot use constant `b` anymore as the resource it

_10

// referred to was moved into function `use`.

_10

_10

b.value ``

A resource object cannot go out of scope and be dynamically lost. The program must either explicitly destroy it or move it to another context.

Declare another, unrelated value of resource type `SomeResource`:

`` _10

{

_10

let c <- create SomeResource(value: 10)

_10

_10

// Invalid: `c` is not moved or destroyed before the end of the scope, but must be.

_10

// It cannot be lost.

_10

} ``

Declare another, unrelated value of resource type `SomeResource`:

`_10

_10

let d <- create SomeResource(value: 20)`

Destroy the resource referred to by constant `d`:

`` _10

destroy d

_10

_10

// Invalid: Cannot use constant `d` anymore as the resource

_10

// it referred to was destroyed.

_10

//

_10

d.value ``

To make it explicit that the type is a resource type and must follow the rules associated with resources, it must be prefixed with `@` in all type annotations (e.g., for variable declarations, parameters, or return types).

Declare a constant with an explicit type annotation. The constant has a resource type, so the type annotation must be prefixed with `@`:

`_10

let someResource: @SomeResource <- create SomeResource(value: 5)`

Declare a function that consumes a resource and destroys it. The parameter has a resource type, so the type annotation must be prefixed with `@`:

`_10

access(all)

_10

fun use(resource: @SomeResource) {

_10

destroy resource

_10

}`

Declare a function that returns a resource:

* The return type is a resource type, so the type annotation must be prefixed with `@`.
* The return statement must also use the `<-` operator to make it explicit the resource is moved.

`_10

access(all)

_10

fun get(): @SomeResource {

_10

let newResource <- create SomeResource()

_10

return <-newResource

_10

}`

Resources **must** be used exactly once.

Declare a function that consumes a resource but does not use it:

`` _10

// This function is invalid, because it would cause a loss of the resource.

_10

access(all)

_10

fun forgetToUse(resource: @SomeResource) {

_10

// Invalid: The resource parameter `resource` is not used, but must be.

_10

} ``

Declare a constant named `res` that has the resource type `SomeResource`:

`_10

let res <- create SomeResource()`

Call the function `use` and move the resource `res` into it:

`` _11

use(resource: <-res)

_11

_11

// Invalid: The resource constant `res` cannot be used again,

_11

// as it was moved in the previous function call.

_11

//

_11

use(resource: <-res)

_11

_11

// Invalid: The resource constant `res` cannot be used again,

_11

// as it was moved in the previous function call.

_11

//

_11

res.value ``

Declare a function that has a resource parameter:

`` _11

// This function is invalid, because it does not always use the resource parameter,

_11

// which would cause a loss of the resource:

_11

access(all)

_11

fun sometimesDestroy(resource: @SomeResource, destroyResource: Bool) {

_11

if destroyResource {

_11

destroy resource

_11

}

_11

// Invalid: The resource parameter `resource` is not always used, but must be.

_11

// The destroy statement is not always executed, so at the end of this function

_11

// it might have been destroyed or not.

_11

} ``

Declare a function which has a resource parameter:

`_11

// This function is valid, as it always uses the resource parameter,

_11

// and does not cause a loss of the resource.

_11

//

_11

access(all)

_11

fun alwaysUse(resource: @SomeResource, destroyResource: Bool) {

_11

if destroyResource {

_11

destroy resource

_11

} else {

_11

use(resource: <-resource)

_11

}

_11

}`

At the end of the function, the resource parameter was definitely used. It was either destroyed or moved in the call of function `use`.

Declare a function that has a resource parameter:

`` _19

// This function is invalid, because it does not always use the resource parameter,

_19

// which would cause a loss of the resource.

_19

//

_19

access(all)

_19

fun returnBeforeDestroy(move: Bool) {

_19

let res <- create SomeResource(value: 1)

_19

if move {

_19

use(resource: <-res)

_19

return

_19

} else {

_19

// Invalid: When this function returns here, the resource variable

_19

// `res` was not used, but must be.

_19

return

_19

}

_19

// Invalid: the resource variable `res` was potentially moved in the

_19

// previous if-statement, and both branches definitely return,

_19

// so this statement is unreachable.

_19

destroy res

_19

} ``

## Resource variables[​](#resource-variables "Direct link to Resource variables")

Resource variables cannot be assigned to, as that would lead to the loss of the variable's current resource value.

Instead, use a swap statement (`<->`) or shift statement (`<- target <-`) to replace the resource variable with another resource:

`` _10

access(all)

_10

resource R {}

_10

_10

var x <- create R()

_10

var y <- create R()

_10

_10

// Invalid: Cannot assign to resource variable `x`,

_10

// as its current resource would be lost

_10

//

_10

x <- y ``

Instead, use a swap statement:

`` _10

var replacement <- create R()

_10

x <-> replacement

_10

// `x` is the new resource.

_10

// `replacement` is the old resource. ``

Or, use the shift statement (`<- target <-`):

`` _10

// This statement moves the resource out of `x` and into `oldX`,

_10

// and at the same time assigns `x` with the new value on the right-hand side.

_10

let oldX <- x <- create R()

_10

// oldX still needs to be explicitly handled after this statement

_10

destroy oldX ``

## Nested resources[​](#nested-resources "Direct link to Nested resources")

Fields in composite types behave differently when they have a resource type.

Accessing a field or calling a function on a resource field is valid, however, moving a resource out of a variable resource field is **not** allowed. Instead, use a swap statement to replace the resource with another resource. For example:

`_10

let child <- create Child(name: "Child 1")

_10

child.name // is "Child 1"

_10

_10

let parent <- create Parent(name: "Parent", child: <-child)

_10

parent.child.name // is "Child 1"

_10

_10

// Invalid: Cannot move resource out of variable resource field.

_10

let childAgain <- parent.child`

Instead, use a swap statement:

`` _10

var otherChild <- create Child(name: "Child 2")

_10

parent.child <-> otherChild

_10

// `parent.child` is the second child, Child 2.

_10

// `otherChild` is the first child, Child 1. ``

When a resource containing nested resources in fields is destroyed with a `destroy` statement, all the nested resources are also destroyed:

`_11

// Declare a resource with resource fields

_11

//

_11

access(all)

_11

resource Parent {

_11

var child1: @Child

_11

var child2: @Child

_11

init(child1: @Child, child2: @Child) {

_11

self.child1 <- child1

_11

self.child2 <- child2

_11

}

_11

}`

The order in which the nested resources are destroyed is deterministic but unspecified, and cannot be influenced by the developer. In this example, when `Parent` is destroyed, the `child1` and `child2` fields are also both destroyed in some unspecified order.

In previous versions of Cadence, it was possible to define a special `destroy` function that would execute arbitrary code when a resource was destroyed, but this is no longer the case.

## Destroy events[​](#destroy-events "Direct link to Destroy events")

While it is not possible to specify arbitrary code to execute upon the destruction of a resource, it is possible to specify a special [event](/docs/language/events) to be automatically emitted when a resource is destroyed. The event has a reserved name — `ResourceDestroyed` — and it uses a special syntax:

`_10

resource R {

_10

event ResourceDestroyed(id: UInt64 = self.id)

_10

_10

let id: UInt64

_10

_10

init(_ id: UInt64) {

_10

self.id = id

_10

}

_10

}`

Whenever a value of type `R` defined this way is destroyed, a special `R.ResourceDestroyed` event is emitted. The special syntax used in the definition of the `ResourceDestroyed` specifies what the values associated with each event parameter will be; in this case, the `id` field of the `R.ResourceDestroyed` event will be the value that the `id` field held immediately before the resource was destroyed. In general, for a `ResourceDestroyed` event defined as:

`_10

event ResourceDestroyed(field1: T1 = e1, field2: T2 = e2, ...)`

* The value of `field1` on the event will be the result of evaluating `e1` before destroying the resource.
* The value of `field2` on the event will be the result of evaluating `e2` before destroying the resource, and so on.

As one might expect, `e1` and `e2` must also be expressions of type `T1` and `T2`, respectively.

In order to guarantee that these events can be emitted with no chance of failure at runtime, there are restrictions placed on which kinds of types and expressions can be used in their definitions. In general, an expression defining the value of a field (the `e` in the general definition above) can only be a member or indexed access on `self` (or, `base` in the case of an [attachment](/docs/language/attachments)), or a literal. The types of event fields are restricted to number types, `String`s, `Boolean`s, `Address`es, and `Path`s.

## Resources in closures[​](#resources-in-closures "Direct link to Resources in closures")

Resources cannot be captured in closures, as that could potentially result in duplications:

`` _13

resource R {}

_13

_13

// Invalid: Declare a function which returns a closure which refers to

_13

// the resource parameter `resource`. Each call to the returned function

_13

// would return the resource, which should not be possible.

_13

//

_13

fun makeCloner(resource: @R): fun(): @R {

_13

return fun (): @R {

_13

return <-resource

_13

}

_13

}

_13

_13

let test = makeCloner(resource: <-create R()) ``

## Resources in arrays and dictionaries[​](#resources-in-arrays-and-dictionaries "Direct link to Resources in arrays and dictionaries")

Arrays and dictionaries behave differently when they contain resources: it is **not** allowed to index into an array to read an element at a certain index or assign to it, or index into a dictionary to read a value for a certain key or set a value for the key.

Instead, use a swap statement (`<->`) or shift statement (`<- target <-`) to replace the accessed resource with another resource.

Declare a constant for an array of resources. Then, create two resources and move them into the array (`resources` has type `@[R]`):

`_15

resource R {}

_15

_15

let resources <- [

_15

<-create R(),

_15

<-create R()

_15

]

_15

_15

// Invalid: Reading an element from a resource array is not allowed.

_15

//

_15

let firstResource <- resources[0]

_15

_15

// Invalid: Setting an element in a resource array is not allowed,

_15

// as it would result in the loss of the current value.

_15

//

_15

resources[0] <- create R()`

Instead, when attempting to either read an element or update an element in a resource array, use a swap statement with a variable to replace the accessed element:

`` _10

var res <- create R()

_10

resources[0] <-> res

_10

// `resources[0]` now contains the new resource.

_10

// `res` now contains the old resource. ``

Use the shift statement to move the new resource into the array at the same time that the old resource is being moved out:

`_10

let oldRes <- resources[0] <- create R()

_10

// The old object still needs to be handled

_10

destroy oldRes`

The same applies to dictionaries.

Declare a constant for a dictionary of resources. Then, create two resources and move them into the dictionary (`resources` has type `@{String: R}`):

`_10

let resources <- {

_10

"r1": <-create R(),

_10

"r2": <-create R()

_10

}

_10

_10

// Invalid: Reading an element from a resource dictionary is not allowed.

_10

// It's not obvious that an access like this would have to remove

_10

// the key from the dictionary.

_10

//

_10

let firstResource <- resources["r1"]`

Instead, make the removal explicit by using the `remove` function:

`_10

let firstResource <- resources.remove(key: "r1")

_10

_10

// Invalid: Setting an element in a resource dictionary is not allowed,

_10

// as it would result in the loss of the current value.

_10

//

_10

resources["r1"] <- create R()`

When attempting to either read an element or update an element in a resource dictionary, use a swap statement with a variable to replace the accessed element.

The result of a dictionary read is optional, as the given key might not exist in the dictionary. The types on both sides of the swap operator must be the same, so also declare the variable as an optional:

`` _10

var res: @R? <- create R()

_10

resources["r1"] <-> res

_10

// `resources["r1"]` now contains the new resource.

_10

// `res` now contains the old resource. ``

Use the shift statement to move the new resource into the dictionary at the same time that the old resource is being moved out:

`_10

let oldRes <- resources["r2"] <- create R()

_10

// The old object still needs to be handled

_10

destroy oldRes`

Resources cannot be moved into arrays and dictionaries multiple times, as that would cause a duplication:

`` _10

let resource <- create R()

_10

_10

// Invalid: The resource variable `resource` can only be moved into the array once.

_10

//

_10

let resources <- [

_10

<-resource,

_10

<-resource

_10

] ``

`` _10

let resource <- create R()

_10

_10

// Invalid: The resource variable `resource` can only be moved into the dictionary once.

_10

let resources <- {

_10

"res1": <-resource,

_10

"res2": <-resource

_10

} ``

Resource arrays and dictionaries can be destroyed:

`_10

let resources <- [

_10

<-create R(),

_10

<-create R()

_10

]

_10

destroy resources`

`_10

let resources <- {

_10

"r1": <-create R(),

_10

"r2": <-create R()

_10

}

_10

destroy resources`

The variable array functions, like `append`, `insert`, and `remove`, behave like non-resource arrays. Please note, however, that the result of the `remove` functions must be used:

`` _18

let resources <- [<-create R()]

_18

// `resources.length` is `1`

_18

_18

resources.append(<-create R())

_18

// `resources.length` is `2`

_18

_18

let first <- resource.remove(at: 0)

_18

// `resources.length` is `1`

_18

destroy first

_18

_18

resources.insert(at: 0, <-create R())

_18

// `resources.length` is `2`

_18

_18

// Invalid: The statement ignores the result of the call to `remove`,

_18

// which would result in a loss.

_18

resource.remove(at: 0)

_18

_18

destroy resources ``

* The variable array function `contains` is not available, as it is impossible: if the resource can be passed to the `contains` function, it is by definition not in the array.
* The variable array function `concat` is not available, as it would result in the duplication of resources.
* The dictionary functions like `insert` and `remove` behave like non-resource dictionaries. Please note, however, that the result of these functions must be used:

`` _18

let resources <- {"r1": <-create R()}

_18

// `resources.length` is `1`

_18

_18

let first <- resource.remove(key: "r1")

_18

// `resources.length` is `0`

_18

destroy first

_18

_18

let old <- resources.insert(key: "r1", <-create R())

_18

// `old` is nil, as there was no value for the key "r1"

_18

// `resources.length` is `1`

_18

_18

let old2 <- resources.insert(key: "r1", <-create R())

_18

// `old2` is the old value for the key "r1"

_18

// `resources.length` is `1`

_18

_18

destroy old

_18

destroy old2

_18

destroy resources ``

## Resource identifier[​](#resource-identifier "Direct link to Resource identifier")

Resources have an implicit unique identifier associated with them, implemented by a predeclared public field `let uuid: UInt64` on each resource.

This identifier is automatically set when the resource is created, before the resource's initializer is called (i.e., the identifier can be used in the initializer), and will be unique even after the resource is destroyed (i.e., no two resources will ever have the same identifier).

1. Declare a resource without any fields:

   `_10

   resource R {}`
2. Create two resources:

   `_10

   let r1 <- create R()

   _10

   let r2 <- create R()`
3. Get each resource's unique identifier:

   `_10

   let id1 = r1.uuid

   _10

   let id2 = r2.uuid`
4. Destroy the first resource:

   `_10

   destroy r1`
5. Create a third resource:

   `_10

   let r3 <- create R()

   _10

   _10

   let id3 = r3.uuid

   _10

   _10

   id1 != id2 // true

   _10

   id2 != id3 // true

   _10

   id3 != id1 // true`

warning

The details of how the identifiers are generated is an implementation detail.

Do not rely on or assume any particular behavior in Cadence programs.

## Resource owner[​](#resource-owner "Direct link to Resource owner")

Resources have the implicit field `let owner: &Account?`. If the resource is currently [stored in an account](/docs/language/accounts/storage), then the field contains the publicly accessible portion of the account. Otherwise the field is `nil`.

The field's value changes when the resource is moved from outside account storage into account storage, when it is moved from the storage of one account to the storage of another account, and when it is moved out of account storage.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/resources.mdx)

[Previous

Scope](/docs/language/scope)[Next

Access Control](/docs/language/access-control)

###### Rate this page

😞😐😊

* [The move operator (`<-`)](#the-move-operator--)
* [Resource variables](#resource-variables)
* [Nested resources](#nested-resources)
* [Destroy events](#destroy-events)
* [Resources in closures](#resources-in-closures)
* [Resources in arrays and dictionaries](#resources-in-arrays-and-dictionaries)
* [Resource identifier](#resource-identifier)
* [Resource owner](#resource-owner)