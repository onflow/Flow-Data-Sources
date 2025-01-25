# Source: https://cadence-lang.org/docs/language/resources




Resources | Cadence




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
* Resources
On this page
# Resources

Resources are types that can only exist in **one** location at a time
and **must** be used **exactly once**.

Resources **must** be created (instantiated) by using the `create` keyword.

At the end of a function which has resources (variables, constants, parameters) in scope,
the resources **must** be either **moved** or **destroyed**.

They are **moved** when used as an initial value for a constant or variable, when assigned to a different variable, when passed as an argument to a function, and when returned from a function.

Resources can be explicitly **destroyed** using the `destroy` keyword.

Accessing a field or calling a function of a resource does not move or destroy it.

When the resource is moved, the constant or variable that referred to the resource before the move becomes **invalid**. An **invalid** resource cannot be used again.

To make the usage and behaviour of resource types explicit,
the prefix `@` must be used in type annotations
of variable or constant declarations, parameters, and return types.

### The Move Operator (`<-`)[​](#the-move-operator-- "Direct link to the-move-operator--")

To make moves of resources explicit, the move operator `<-` must be used
when the resource is the initial value of a constant or variable,
when it is moved to a different variable,
when it is moved to a function as an argument,
and when it is returned from a function.

 `_47// Declare a resource named `SomeResource`, with a variable integer field._47_47access(all)_47resource SomeResource {_47 _47 access(all)_47 var value: Int_47_47 init(value: Int) {_47 self.value = value_47 }_47}_47_47// Declare a constant with value of resource type `SomeResource`._47_47let a: @SomeResource <- create SomeResource(value: 5)_47_47// *Move* the resource value to a new constant._47_47let b <- a_47_47// Invalid Line Below: Cannot use constant `a` anymore as the resource that it_47// referred to was moved to constant `b`._47_47a.value_47_47// Constant `b` owns the resource._47_47b.value // equals 5_47_47// Declare a function which accepts a resource._47_47// The parameter has a resource type, so the type annotation must be prefixed with `@`._47_47access(all)_47fun use(resource: @SomeResource) {_47 // ..._47}_47_47// Call function `use` and move the resource into it._47_47use(resource: <-b)_47_47// Invalid Line Below: Cannot use constant `b` anymore as the resource it_47// referred to was moved into function `use`._47_47b.value`

A resource object cannot go out of scope and be dynamically lost.
The program must either explicitly destroy it or move it to another context.

 `_10{_10 // Declare another, unrelated value of resource type `SomeResource`._10 _10 let c <- create SomeResource(value: 10)_10_10 // Invalid: `c` is not used before the end of the scope, but must be._10 // It cannot be lost._10}`
 `_12// Declare another, unrelated value of resource type `SomeResource`._12//_12let d <- create SomeResource(value: 20)_12_12// Destroy the resource referred to by constant `d`._12//_12destroy d_12_12// Invalid: Cannot use constant `d` anymore as the resource_12// it referred to was destroyed._12//_12d.value`

To make it explicit that the type is a resource type
and must follow the rules associated with resources,
it must be prefixed with `@` in all type annotations,
e.g. for variable declarations, parameters, or return types.

 `_25// Declare a constant with an explicit type annotation._25//_25// The constant has a resource type, so the type annotation must be prefixed with `@`._25//_25let someResource: @SomeResource <- create SomeResource(value: 5)_25_25// Declare a function which consumes a resource and destroys it._25//_25// The parameter has a resource type, so the type annotation must be prefixed with `@`._25//_25access(all)_25fun use(resource: @SomeResource) {_25 destroy resource_25}_25_25// Declare a function which returns a resource._25//_25// The return type is a resource type, so the type annotation must be prefixed with `@`._25// The return statement must also use the `<-` operator to make it explicit the resource is moved._25//_25access(all)_25fun get(): @SomeResource {_25 let newResource <- create SomeResource()_25 return <-newResource_25}`

Resources **must** be used exactly once.

 `_10// Declare a function which consumes a resource but does not use it._10// This function is invalid, because it would cause a loss of the resource._10//_10access(all)_10fun forgetToUse(resource: @SomeResource) {_10 // Invalid: The resource parameter `resource` is not used, but must be._10}`
 `_15// Declare a constant named `res` which has the resource type `SomeResource`._15let res <- create SomeResource()_15_15// Call the function `use` and move the resource `res` into it._15use(resource: <-res)_15_15// Invalid: The resource constant `res` cannot be used again,_15// as it was moved in the previous function call._15//_15use(resource: <-res)_15_15// Invalid: The resource constant `res` cannot be used again,_15// as it was moved in the previous function call._15//_15res.value`
 `_13// Declare a function which has a resource parameter._13// This function is invalid, because it does not always use the resource parameter,_13// which would cause a loss of the resource._13//_13access(all)_13fun sometimesDestroy(resource: @SomeResource, destroyResource: Bool) {_13 if destroyResource {_13 destroy resource_13 }_13 // Invalid: The resource parameter `resource` is not always used, but must be._13 // The destroy statement is not always executed, so at the end of this function_13 // it might have been destroyed or not._13}`
 `_14// Declare a function which has a resource parameter._14// This function is valid, as it always uses the resource parameter,_14// and does not cause a loss of the resource._14//_14access(all)_14fun alwaysUse(resource: @SomeResource, destroyResource: Bool) {_14 if destroyResource {_14 destroy resource_14 } else {_14 use(resource: <-resource)_14 }_14 // At the end of the function the resource parameter was definitely used:_14 // It was either destroyed or moved in the call of function `use`._14}`
 `_20// Declare a function which has a resource parameter._20// This function is invalid, because it does not always use the resource parameter,_20// which would cause a loss of the resource._20//_20access(all)_20fun returnBeforeDestroy(move: Bool) {_20 let res <- create SomeResource(value: 1)_20 if move {_20 use(resource: <-res)_20 return_20 } else {_20 // Invalid: When this function returns here, the resource variable_20 // `res` was not used, but must be._20 return_20 }_20 // Invalid: the resource variable `res` was potentially moved in the_20 // previous if-statement, and both branches definitely return,_20 // so this statement is unreachable._20 destroy res_20}`
### Resource Variables[​](#resource-variables "Direct link to Resource Variables")

Resource variables cannot be assigned to,
as that would lead to the loss of the variable's current resource value.

Instead, use a swap statement (`<->`) or shift statement (`<- target <-`)
to replace the resource variable with another resource.

 `_24access(all)_24resource R {}_24_24var x <- create R()_24var y <- create R()_24_24// Invalid: Cannot assign to resource variable `x`,_24// as its current resource would be lost_24//_24x <- y_24_24// Instead, use a swap statement._24//_24var replacement <- create R()_24x <-> replacement_24// `x` is the new resource._24// `replacement` is the old resource._24_24// Or use the shift statement (`<- target <-`)_24// This statement moves the resource out of `x` and into `oldX`,_24// and at the same time assigns `x` with the new value on the right-hand side._24let oldX <- x <- create R()_24// oldX still needs to be explicitly handled after this statement_24destroy oldX`
### Nested Resources[​](#nested-resources "Direct link to Nested Resources")

Fields in composite types behave differently when they have a resource type.

Accessing a field or calling function on a resource field is valid,
however moving a resource out of a variable resource field is **not** allowed.
Instead, use a swap statement to replace the resource with another resource.

 `_15let child <- create Child(name: "Child 1")_15child.name // is "Child 1"_15_15let parent <- create Parent(name: "Parent", child: <-child)_15parent.child.name // is "Child 1"_15_15// Invalid: Cannot move resource out of variable resource field._15let childAgain <- parent.child_15_15// Instead, use a swap statement._15//_15var otherChild <- create Child(name: "Child 2")_15parent.child <-> otherChild_15// `parent.child` is the second child, Child 2._15// `otherChild` is the first child, Child 1.`

When a resource containing nested resources in fields is destroyed with a `destroy` statement,
all the nested resources are also destroyed.

 `_11// Declare a resource with resource fields_11//_11access(all)_11resource Parent {_11 var child1: @Child_11 var child2: @Child_11 init(child1: @Child, child2: @Child) {_11 self.child1 <- child1_11 self.child2 <- child2_11 }_11}`

The order in which the nested resources are destroyed is deterministic but unspecified,
and cannot be influenced by the developer. E.g., in this example, when `Parent` is destroyed,
the `child1` and `child2` fields are both also destroyed in some unspecified order.

In previous versions of Cadence it was possible to define a special `destroy` function that
would execute arbitrary code when a resource was destroyed, but this is no longer the case.

### Destroy Events[​](#destroy-events "Direct link to Destroy Events")

While it is not possible to specify arbitrary code to execute upon the destruction of a resource,
it is possible to specify a special [event](/docs/language/events) to be automatically emitted when a resource is destroyed.
The event has a reserved name: `ResourceDestroyed`, and uses special syntax:

 `_10resource R {_10 event ResourceDestroyed(id: UInt64 = self.id) _10_10 let id: UInt64_10_10 init(_ id: UInt64) {_10 self.id = id_10 }_10}`

Whenever a value of type `R` defined this way is destroyed, a special `R.ResourceDestroyed` event will be emitted.
The special syntax used in the definition of the `ResourceDestroyed` specifies what the values associated with each event
parameter will be; in this case the `id` field of the `R.ResourceDestroyed` event will be the value that the `id` field held
immediately before the resource was destroyed. In general, for some `ResourceDestroyed` event defined as:

 `_10event ResourceDestroyed(field1: T1 = e1, field2: T2 = e2, ...)`

The value of `field1` on the event will be the result of evaluating `e1` before destroying the resource,
the value of `field2` on the event will be the result of evaluating `e2` before destroying the resource,
and so on. As one might expect, `e1` and `e2` must also be expressions of type `T1` and `T2` respectively.

In order to guarantee that these events can be emitted with no chance of failure at runtime, there are restrictions
placed on which kinds of types and expressions can be used in their definitions. In general, an expression
defining the value of a field (the `e` in the general definition above) can only be a member or indexed access on `self`
(or `base` in the case of an [attachment](/docs/language/attachments)) or a literal. The types of event fields are restricted to
number types, `String`s, `Boolean`s, `Address`es and `Path`s.

### Resources in Closures[​](#resources-in-closures "Direct link to Resources in Closures")

Resources can not be captured in closures, as that could potentially result in duplications.

 `_13resource R {}_13_13// Invalid: Declare a function which returns a closure which refers to_13// the resource parameter `resource`. Each call to the returned function_13// would return the resource, which should not be possible._13//_13fun makeCloner(resource: @R): fun(): @R {_13 return fun (): @R {_13 return <-resource_13 }_13}_13_13let test = makeCloner(resource: <-create R())`
### Resources in Arrays and Dictionaries[​](#resources-in-arrays-and-dictionaries "Direct link to Resources in Arrays and Dictionaries")

Arrays and dictionaries behave differently when they contain resources:
It is **not** allowed to index into an array to read an element at a certain index or assign to it,
or index into a dictionary to read a value for a certain key or set a value for the key.

Instead, use a swap statement (`<->`) or shift statement (`<- target <-`)
to replace the accessed resource with another resource.

 `_34resource R {}_34_34// Declare a constant for an array of resources._34// Create two resources and move them into the array._34// `resources` has type `@[R]`_34//_34let resources <- [_34 <-create R(),_34 <-create R()_34]_34_34// Invalid: Reading an element from a resource array is not allowed._34//_34let firstResource <- resources[0]_34_34// Invalid: Setting an element in a resource array is not allowed,_34// as it would result in the loss of the current value._34//_34resources[0] <- create R()_34_34// Instead, when attempting to either read an element or update an element_34// in a resource array, use a swap statement with a variable to replace_34// the accessed element._34//_34var res <- create R()_34resources[0] <-> res_34// `resources[0]` now contains the new resource._34// `res` now contains the old resource._34_34// Use the shift statement to move the new resource into_34// the array at the same time that the old resource is being moved out_34let oldRes <- resources[0] <- create R()_34// The old object still needs to be handled_34destroy oldRes`

The same applies to dictionaries.

 `_42// Declare a constant for a dictionary of resources._42// Create two resources and move them into the dictionary._42// `resources` has type `@{String: R}`_42//_42let resources <- {_42 "r1": <-create R(),_42 "r2": <-create R()_42}_42_42// Invalid: Reading an element from a resource dictionary is not allowed._42// It's not obvious that an access like this would have to remove_42// the key from the dictionary._42//_42let firstResource <- resources["r1"]_42_42// Instead, make the removal explicit by using the `remove` function._42let firstResource <- resources.remove(key: "r1")_42_42// Invalid: Setting an element in a resource dictionary is not allowed,_42// as it would result in the loss of the current value._42//_42resources["r1"] <- create R()_42_42// Instead, when attempting to either read an element or update an element_42// in a resource dictionary, use a swap statement with a variable to replace_42// the accessed element._42//_42// The result of a dictionary read is optional, as the given key might not_42// exist in the dictionary._42// The types on both sides of the swap operator must be the same,_42// so also declare the variable as an optional._42//_42var res: @R? <- create R()_42resources["r1"] <-> res_42// `resources["r1"]` now contains the new resource._42// `res` now contains the old resource._42_42// Use the shift statement to move the new resource into_42// the dictionary at the same time that the old resource is being moved out_42let oldRes <- resources["r2"] <- create R()_42// The old object still needs to be handled_42destroy oldRes`

Resources cannot be moved into arrays and dictionaries multiple times,
as that would cause a duplication.

 `_10let resource <- create R()_10_10// Invalid: The resource variable `resource` can only be moved into the array once._10//_10let resources <- [_10 <-resource,_10 <-resource_10]`
 `_10let resource <- create R()_10_10// Invalid: The resource variable `resource` can only be moved into the dictionary once._10let resources <- {_10 "res1": <-resource,_10 "res2": <-resource_10}`

Resource arrays and dictionaries can be destroyed.

 `_10let resources <- [_10 <-create R(),_10 <-create R()_10]_10destroy resources`
 `_10let resources <- {_10 "r1": <-create R(),_10 "r2": <-create R()_10}_10destroy resources`

The variable array functions like `append`, `insert`, and `remove`
behave like for non-resource arrays.
Note however, that the result of the `remove` functions must be used.

 `_18let resources <- [<-create R()]_18// `resources.length` is `1`_18_18resources.append(<-create R())_18// `resources.length` is `2`_18_18let first <- resource.remove(at: 0)_18// `resources.length` is `1`_18destroy first_18_18resources.insert(at: 0, <-create R())_18// `resources.length` is `2`_18_18// Invalid: The statement ignores the result of the call to `remove`,_18// which would result in a loss._18resource.remove(at: 0)_18_18destroy resources`

The variable array function `contains` is not available, as it is impossible:
If the resource can be passed to the `contains` function,
it is by definition not in the array.

The variable array function `concat` is not available,
as it would result in the duplication of resources.

The dictionary functions like `insert` and `remove`
behave like for non-resource dictionaries.
Note however, that the result of these functions must be used.

 `_18let resources <- {"r1": <-create R()}_18// `resources.length` is `1`_18_18let first <- resource.remove(key: "r1")_18// `resources.length` is `0`_18destroy first_18_18let old <- resources.insert(key: "r1", <-create R())_18// `old` is nil, as there was no value for the key "r1"_18// `resources.length` is `1`_18_18let old2 <- resources.insert(key: "r1", <-create R())_18// `old2` is the old value for the key "r1"_18// `resources.length` is `1`_18_18destroy old_18destroy old2_18destroy resources`
### Resource Identifier[​](#resource-identifier "Direct link to Resource Identifier")

Resources have an implicit unique identifier associated with them,
implemented by a predeclared public field `let uuid: UInt64` on each resource.

This identifier will be automatically set when the resource is created, before the resource's initializer is called
(i.e. the identifier can be used in the initializer),
and will be unique even after the resource is destroyed,
i.e. no two resources will ever have the same identifier.

 `_22// Declare a resource without any fields._22resource R {}_22_22// Create two resources_22let r1 <- create R()_22let r2 <- create R()_22_22// Get each resource's unique identifier_22let id1 = r1.uuid_22let id2 = r2.uuid_22_22// Destroy the first resource_22destroy r1_22_22// Create a third resource_22let r3 <- create R()_22_22let id3 = r3.uuid_22_22id1 != id2 // true_22id2 != id3 // true_22id3 != id1 // true`
warning

The details of how the identifiers are generated is an implementation detail.

Do not rely on or assume any particular behaviour in Cadence programs.

## Resource Owner[​](#resource-owner "Direct link to Resource Owner")

Resources have the implicit field `let owner: &Account?`.
If the resource is currently [stored in an account](/docs/language/accounts/storage),
then the field contains the publicly accessible portion of the account.
Otherwise the field is `nil`.

The field's value changes when the resource is moved from outside account storage
into account storage, when it is moved from the storage of one account
to the storage of another account, and when it is moved out of account storage.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/resources.mdx)[PreviousComposite Types](/docs/language/composite-types)[NextAccess control](/docs/language/access-control)
###### Rate this page

😞😐😊

* [The Move Operator (`<-`)](#the-move-operator--)
* [Resource Variables](#resource-variables)
* [Nested Resources](#nested-resources)
* [Destroy Events](#destroy-events)
* [Resources in Closures](#resources-in-closures)
* [Resources in Arrays and Dictionaries](#resources-in-arrays-and-dictionaries)
* [Resource Identifier](#resource-identifier)
* [Resource Owner](#resource-owner)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

