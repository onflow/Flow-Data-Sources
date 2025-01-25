# Source: https://cadence-lang.org/docs/language/references




References | Cadence




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
* References
On this page
# References

It is possible to create references to objects, i.e. resources or structures.
A reference can be used to access fields and call functions on the referenced object.

References are **copied**, i.e. they are value types.

References have the type `&T`, where `T` is the type of the referenced object.

References are created using the `&` operator.
The reference type must be explicitly provided,
for example through a type annotation on a variable declaration,
or a type assertion using the `as` operator.

 `_17let hello = "Hello"_17_17// Create a reference to the `String` `hello`._17// Provide the reference type `&String` using a type assertion_17//_17let helloRef = &hello as &String_17_17helloRef.length // is `5`_17_17// Create another reference to the `String` `hello`._17// Provide the reference type `&String` using a type annotation instead_17//_17let alsoHelloRef: &String = &hello_17_17// Invalid: Cannot create a reference without an explicit type_17//_17let unknownRef = &hello`

The reference type must be a supertype of the referenced object's type.

 `_10// Invalid: Cannot create a reference to `hello`_10// typed as `&Int`, as it has type `String`_10//_10let intRef = &hello as &Int`

When creating a reference to an optional value, the result is an optional reference.
If the referenced value is nil, the resulting reference itself will be nil.
If the referenced value exists, then forcing the optional reference will yield a reference to that value:

 `_10let nilValue: String? = nil_10let nilRef = &nilValue as &String? // r has type &String?_10let n = nilRef! // error, forced nil value_10_10let strValue: String? = ""_10let strRef = &strValue as &String? // r has type &String?_10let n = strRef! // n has type &String`

References are covariant in their base types.
For example, `&T` is a subtype of `&U`, if `T` is a subtype of `U`.

 `_39_39// Declare a resource interface named `HasCount`,_39// that has a field `count`_39//_39resource interface HasCount {_39 count: Int_39}_39_39// Declare a resource named `Counter` that conforms to `HasCount`_39//_39resource Counter: HasCount {_39 _39 access(all)_39 var count: Int_39_39 access(all)_39 init(count: Int) {_39 self.count = count_39 }_39_39 access(all)_39 fun increment() {_39 self.count = self.count + 1_39 }_39}_39_39// Create a new instance of the resource type `Counter`_39// and create a reference to it, typed as `&Counter`,_39// so the reference allows access to all fields and functions_39// of the counter_39//_39let counter <- create Counter(count: 42)_39let counterRef: &Counter = &counter as &Counter_39_39counterRef.count // is `42`_39_39counterRef.increment()_39_39counterRef.count // is `43``

References can be freely upcasted and downcasted, and are covariant in their referenced type.
So, for example, for some struct `S`, `&S` is a subtype of `&AnyStruct`, but not of `&Int`.

 `_18// Create an reference to the counter,_18// typed with the intersection type `&{HasCount}`,_18// i.e. some resource that conforms to the `HasCount` interface_18//_18let countRef = &counter as &{HasCount}_18_18countRef.count // is `43`_18_18// Invalid: The function `increment` is not available_18// for the type `&{HasCount}`_18//_18countRef.increment()_18_18// We can conditionally downcast `countRef` to a `Counter` if it has_18// that type at runtime._18//_18let counterRef2: &Counter = countRef as? &Counter_18counterRef2.increment()`

References are ephemeral, i.e. they cannot be [stored](/docs/language/accounts/storage).
Instead, consider [storing a capability and borrowing it](/docs/language/capabilities) when needed.

## Authorized References[​](#authorized-references "Direct link to Authorized References")

By default, references are **unauthorized**.
However, they may also be **authorized** to a set of [entitlements](/docs/language/access-control#entitlements)

Authorized references have the `auth` modifier,
along with the set of entitlements to which they are authorized. The full syntax is:
`auth(E, F, G) &T` for a reference authorized to `E`, `F` and `G`,
or `auth(E | F | G) &T` for a refernece authorized to `E`, `F`, **or** `G`.
Authorized references are subtypes of unauthorized references.

Entitlements can only be given to references when they are created,
and references to a value can only be created by the owner of the value.
When creating a reference, that reference can be given any set of entitlements the value owner wishes to add.

Possessing an entitlement allows a reference to have access to functions and fields on its referenced type
that require that entitlement. E.g, if we extended the `HasCount` interface with a function:

 `_10entitlement Reset_10_10resource interface HasCount {_10 count: Int_10 _10 access(Reset)_10 fun resetCount()_10}`

Then an unauthorized reference of type `&{HasCount}` would be unable to call `resetCount`.
However, we can create a reference that can, like so:

 `_10let authCountRef: auth(Reset) &{HasCount} = &counter_10_10// Valid, because `authCountRef` is authorized to `Reset`_10authCountRef.resetCount()`

It is important to note that while references are covariant (and downcastable) with respect to their reference type,
the authorization portion of the reference can never be downcast.
In fact, the only way to "add" entitlements to a reference is to do so at the time of its creation, like in the example above.
A reference will never have any more entitlements than the set with which it was created,
and the set of entitlements on a reference at runtime will always match the set expressed in its static type.
One implication of this is that upcasting an authorized reference actually changes its runtime type:

 `_10let authCountRef: auth(Reset) &{HasCount} = &counter_10let unauthCountRef = authCountRef as &{HasCount}_10let authCountRef2 = unauthCountRef as? auth(Reset) &{HasCount}_10_10// Invalid: `authCountRef2` is `nil`, as the upcast of `authCountRef` cleared the_10// `Reset` entitlement from the reference, meaning that it cannot be regained on downcasting._10authCountRef2.resetCount()`

The benefit of this is that there is never any "surprising" behavior with regards to entitlements,
every reference value is transparent about what it is capable of at runtime.

While entitlement sets on references cannot be downcast, they can be upcast, or used in places expecting supertypes,
and have special subtyping rules based on whether they are `|` or `,`-separated sets.

In general, an entitlement set `{Us}` is a subtype of an entitlement set `{Vs}` when `{Us}` has more entitlements
in it than `{Vs}`, and when both are `,`-separated (as they will be in most cases), this is the rule exactly:
`{Us}` is a subset of `{Vs}` when it is a superset of `{Vs}`.

Conversely, if both are `|`-separated, the rule is reversed:
`{Us}` is a subset of `{Vs}` when it is a subset of `{Vs}`.
It may be helpful to think of this as saying that `{Us}` is more specific than `{Vs}` in this case;
`{Vs}` expresses a set of entitlements that the reference **might** possess,
while `{Us}` is expressing a more specific set of potential entitlements.

Lastly, if `{Us}` is `,`-separated while `{Vs}` is `|`-separated,
then `{Us}` is a subset of `{Vs}` when any of the `Us` also appears in `{Vs}`.
To see why, consider again that `{Vs}` expresses a set of entitlements that the reference **might** possess,
and as long as at least one of these entitlements is in `{Us}` (which is a set of entitlements that we **know** the reference has),
then the description provided by `{Vs}` is correct.

As an example to illustrate these rules:

 `_24let eRef: auth(E) &T = ..._24let efRef: auth(E, F) &T = ..._24let eOrFRef: auth(E | F) &T = ..._24_24// Invalid, `eRef` only has `E` but `F` is required_24eRef as auth(F) &T_24_24// Invalid, `eRef` only has `E` but both `E` and `F` are required_24eRef as auth(E, F) &T_24_24// Valid, `eRef` definitely has `E` and either `E` or `F` is sufficient_24eRef as auth(E | F) &T_24_24// Valid, `efRef` both `E` and `F` but only `F` is required_24efRef as auth(F) &T_24_24// Valid, `efRef` both `E` and `F`, and either is sufficient_24efRef as auth(E | F) &T_24_24// Invalid, `eOrFRef` has one of `E` or `F` but we need to definitely have `F`_24eOrFRef as auth(F) &T_24_24// Invalid, `eOrFRef` has one of `E` or `F` but we need both_24eOrFRef as auth(E, F) &T`
### References and Entitlement Mappings[​](#references-and-entitlement-mappings "Direct link to References and Entitlement Mappings")

In most situations, an [entitlement mapping](/docs/language/access-control#entitlement-mappings) is valid in the `auth` portion of a reference type.
However, in certain specific circumstances in the definition of a field or function on a composite type, an entitlement mapping may be used in an `auth` modifier.

When a field is defined with an entitlement mapping:

 `_10entitlement mapping M {_10 // omitted_10}_10resource interface I {_10 access(M)_10 let foo: auth(M) &T_10}`

Here, the `M` in `auth(M) &T` indicates that the entitlements that the reference produced by an `iRef.foo` access will have
are determined by the entitlements to `I` that `iRef` has, for some `iRef` value that is a reference to `{I}`. Conceptually,
it creates a correspondence between the "output" reference's type and the "input" access modifier.

When an accessor function is defined with an entitlement mapping:

 `_12entitlement mapping M {_12 // omitted_12}_12resource I {_12 access(self)_12 let myField: T_12_12 access(M)_12 fun getMyField(): auth(M) &T {_12 return &self.myField as auth(M) &T_12 }_12}`

The `M` in the `auth(M) &T` of the function's return type annotation indicates the same thing as in the field case.
However, in this example `M` is also used in a reference type within the body of the function.
Inside the body of function with entitlement-mapped access,
the name of the entitlement mapping may be used as a stand-in for the output entitlements of the map.

## Field and Index Access[​](#field-and-index-access "Direct link to Field and Index Access")

References to container types (structs/resources, dictionaries and arrays) can be used to access (read/write) fields
or elements of the container.

When a field/index is read through a reference, it will return:

* A reference, if the field / value at index is also container-typed.
* Or, the concrete value, if the value is a primitive type.

For example, consider the below `Collection` resource which has two fields: one (id) is String-typed,
and the other (ownedNFTs) is dictionary-typed.

 `_10resource Collection {_10_10 // Primitive-typed field_10 access(all)_10 var id: String_10_10 // Dictionary typed field_10 access(all)_10 var ownedNFTs: @{UInt64: NFT}_10}`

Thus,

 `_10var collectionRef: &Collection = ..._10_10// `collectionRef.ownedNFTs` would return a reference of type `&{UInt64: NFT}`._10var ownedNFTsRef: &{UInt64: NFT} = collectionRef.ownedNFTs_10_10// Whereas, `collectionRef.id` would return the value, since it is a primitive type._10var id: String = collectionRef.id`

Similarly, accessing an element of an array/dictionary will return a reference.

 `_10// Index-access to an array reference would return a reference to the element._10var resourceArrayRef: &[AnyResource] = ..._10var elementRef: &AnyResource = collectionArrayRef[2]_10_10// Whereas, if the array is of a primitive type, it will return the concrete value._10var intArrayRef: &[Int] = ..._10var element: Int = intArrayRef[2]`
 `_10// Index-access to a dictionary reference would return a reference to the value._10var resourceDictionaryRef: &{String: AnyResource} = ..._10var valueRef: &AnyResource? = resourceDictionaryRef["two"]_10_10// Whereas, if the dictionary values are of a primitive type, it will return the concrete value._10var intDictionaryRef: &{String: Int} = ..._10var value: Int? = intDictionaryRef["two"]`

It is also important to note that, in the above examples, the returned references have no entitlements.
i.e: they are non-auth references.

To get entitled references for struct/resource fields, they must be defined with [entitlement mappings](/docs/language/access-control#entitlement-mappings).
However, accessing a value at an index/key of an array/dictionary reference would always return a non-auth reference.

### Index Assignment[​](#index-assignment "Direct link to Index Assignment")

Assigning to an index of an array or a dictionary reference is an entitled-operation.
In other words, the assignment operator for arrays/dictionaries would also have the `Mutate` and `Insert`
[built-in entitlements](/docs/language/access-control#built-in-mutability-entitlements).

Think of assignment as a built-in function with `Mutate` or `(Insert, Remove)` entitlements. e.g:

 `_10access(Mutate | (Insert, Remove))_10set(keyOrIndex, value) { ... }`

Note that the syntax for having nested entitlements in access modifiers like `(Mutate | (Insert, Remove))`
is not currently supported, but this is for illustration purpose only.

Thus,

 `_14var arrayRef = &array as &[String]_14arrayRef[2] = "John" // Static Error: updating via a read-only reference_14_14var mutableArrayRef = &array as auth(Mutate) &[String]_14mutableArrayRef[2] = "John" // OK_14_14var insertableArrayRef = &array as auth(Insert) &[String]_14insertableArrayRef[2] = "John" // Static Error: doesn't have the required entitlement_14_14var removableArrayRef = &array as auth(Remove) &[String]_14removableArrayRef[2] = "John" // Static Error: doesn't have the required entitlement_14_14var insertableAndRemovableArrayRef = &array as auth(Insert, Remove) &[String]_14insertableAndRemovableArrayRef[2] = "John" // OK`
## Reference Validity[​](#reference-validity "Direct link to Reference Validity")

Ephemeral references stay valid throughout the course of the program.
However, **references to resources** can become invalid during the execution of a program,
if the referenced resource is moved or destroyed after taking the reference.

 `_11let r <-create R()_11_11// Take a reference to resource._11let ref = &r as &R_11_11// Then transfer the resource into an account._11// This will invalidate all the references taken to the resource `r`._11account.storage.save(<-r, to: /storage/r)_11_11// Static error, since the referenced resource has been moved._11ref.id = 2`

A reference is invalidated upon the first transfer of the underlying resource,
regardless of the origin and the destination.

 `_10let ref = &r as &R_10_10// Moving a resource to a different variable invalidates all references to it._10let r2 <- r_10_10// Static error, since the referenced resource has been moved._10ref.id = 2`
tip

Invalidations of storage references are not statically caught, but only at run-time.

## Dereferencing values[​](#dereferencing-values "Direct link to Dereferencing values")

Primitive values (and arrays or dictionaries of primitive values) can be "de-referenced" using the unary `*` operator.
This operation produces a copy of the referenced value, so e.g. given some example code:

 `_10var x = 3_10let ref: &Int = &x_10var y = *ref_10y = y + 1`

At the end of the execution of this code, `y` will clearly be `4`, but `x` will still be `3`, as the `*ref` operation copies
the value. This can be seen even more clearly using an example with arrays:

 `_10let x = [0]_10let ref: &[Int] = &x_10var y = *ref_10y.append(1)`

At the end of this execution, `y` will contain `[0, 1]`, while `x` will remain `[0]` only.

References to non-primitive values (e.g. structs, resources, contracts and enums) cannot be dereferenced.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/references.mdx)[PreviousIntersection Types](/docs/language/intersection-types)[NextImports](/docs/language/imports)
###### Rate this page

😞😐😊

* [Authorized References](#authorized-references)
  + [References and Entitlement Mappings](#references-and-entitlement-mappings)
* [Field and Index Access](#field-and-index-access)
  + [Index Assignment](#index-assignment)
* [Reference Validity](#reference-validity)
* [Dereferencing values](#dereferencing-values)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

