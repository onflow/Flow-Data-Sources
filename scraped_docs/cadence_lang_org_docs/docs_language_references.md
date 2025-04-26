# Source: https://cadence-lang.org/docs/language/references

References | Cadence



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

`_17

let hello = "Hello"

_17

_17

// Create a reference to the `String` `hello`.

_17

// Provide the reference type `&String` using a type assertion

_17

//

_17

let helloRef = &hello as &String

_17

_17

helloRef.length // is `5`

_17

_17

// Create another reference to the `String` `hello`.

_17

// Provide the reference type `&String` using a type annotation instead

_17

//

_17

let alsoHelloRef: &String = &hello

_17

_17

// Invalid: Cannot create a reference without an explicit type

_17

//

_17

let unknownRef = &hello`

The reference type must be a supertype of the referenced object's type.

`_10

// Invalid: Cannot create a reference to `hello`

_10

// typed as `&Int`, as it has type `String`

_10

//

_10

let intRef = &hello as &Int`

When creating a reference to an optional value, the result is an optional reference.
If the referenced value is nil, the resulting reference itself will be nil.
If the referenced value exists, then forcing the optional reference will yield a reference to that value:

`_10

let nilValue: String? = nil

_10

let nilRef = &nilValue as &String? // r has type &String?

_10

let n = nilRef! // error, forced nil value

_10

_10

let strValue: String? = ""

_10

let strRef = &strValue as &String? // r has type &String?

_10

let n = strRef! // n has type &String`

References are covariant in their base types.
For example, `&T` is a subtype of `&U`, if `T` is a subtype of `U`.

`_39

_39

// Declare a resource interface named `HasCount`,

_39

// that has a field `count`

_39

//

_39

resource interface HasCount {

_39

count: Int

_39

}

_39

_39

// Declare a resource named `Counter` that conforms to `HasCount`

_39

//

_39

resource Counter: HasCount {

_39

_39

access(all)

_39

var count: Int

_39

_39

access(all)

_39

init(count: Int) {

_39

self.count = count

_39

}

_39

_39

access(all)

_39

fun increment() {

_39

self.count = self.count + 1

_39

}

_39

}

_39

_39

// Create a new instance of the resource type `Counter`

_39

// and create a reference to it, typed as `&Counter`,

_39

// so the reference allows access to all fields and functions

_39

// of the counter

_39

//

_39

let counter <- create Counter(count: 42)

_39

let counterRef: &Counter = &counter as &Counter

_39

_39

counterRef.count // is `42`

_39

_39

counterRef.increment()

_39

_39

counterRef.count // is `43``

References can be freely upcasted and downcasted, and are covariant in their referenced type.
So, for example, for some struct `S`, `&S` is a subtype of `&AnyStruct`, but not of `&Int`.

`_18

// Create an reference to the counter,

_18

// typed with the intersection type `&{HasCount}`,

_18

// i.e. some resource that conforms to the `HasCount` interface

_18

//

_18

let countRef = &counter as &{HasCount}

_18

_18

countRef.count // is `43`

_18

_18

// Invalid: The function `increment` is not available

_18

// for the type `&{HasCount}`

_18

//

_18

countRef.increment()

_18

_18

// We can conditionally downcast `countRef` to a `Counter` if it has

_18

// that type at runtime.

_18

//

_18

let counterRef2: &Counter = countRef as? &Counter

_18

counterRef2.increment()`

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

`_10

entitlement Reset

_10

_10

resource interface HasCount {

_10

count: Int

_10

_10

access(Reset)

_10

fun resetCount()

_10

}`

Then an unauthorized reference of type `&{HasCount}` would be unable to call `resetCount`.
However, we can create a reference that can, like so:

`_10

let authCountRef: auth(Reset) &{HasCount} = &counter

_10

_10

// Valid, because `authCountRef` is authorized to `Reset`

_10

authCountRef.resetCount()`

It is important to note that while references are covariant (and downcastable) with respect to their reference type,
the authorization portion of the reference can never be downcast.
In fact, the only way to "add" entitlements to a reference is to do so at the time of its creation, like in the example above.
A reference will never have any more entitlements than the set with which it was created,
and the set of entitlements on a reference at runtime will always match the set expressed in its static type.
One implication of this is that upcasting an authorized reference actually changes its runtime type:

`_10

let authCountRef: auth(Reset) &{HasCount} = &counter

_10

let unauthCountRef = authCountRef as &{HasCount}

_10

let authCountRef2 = unauthCountRef as? auth(Reset) &{HasCount}

_10

_10

// Invalid: `authCountRef2` is `nil`, as the upcast of `authCountRef` cleared the

_10

// `Reset` entitlement from the reference, meaning that it cannot be regained on downcasting.

_10

authCountRef2.resetCount()`

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

`_24

let eRef: auth(E) &T = ...

_24

let efRef: auth(E, F) &T = ...

_24

let eOrFRef: auth(E | F) &T = ...

_24

_24

// Invalid, `eRef` only has `E` but `F` is required

_24

eRef as auth(F) &T

_24

_24

// Invalid, `eRef` only has `E` but both `E` and `F` are required

_24

eRef as auth(E, F) &T

_24

_24

// Valid, `eRef` definitely has `E` and either `E` or `F` is sufficient

_24

eRef as auth(E | F) &T

_24

_24

// Valid, `efRef` both `E` and `F` but only `F` is required

_24

efRef as auth(F) &T

_24

_24

// Valid, `efRef` both `E` and `F`, and either is sufficient

_24

efRef as auth(E | F) &T

_24

_24

// Invalid, `eOrFRef` has one of `E` or `F` but we need to definitely have `F`

_24

eOrFRef as auth(F) &T

_24

_24

// Invalid, `eOrFRef` has one of `E` or `F` but we need both

_24

eOrFRef as auth(E, F) &T`

### References and Entitlement Mappings[​](#references-and-entitlement-mappings "Direct link to References and Entitlement Mappings")

In most situations, an [entitlement mapping](/docs/language/access-control#entitlement-mappings) is valid in the `auth` portion of a reference type.
However, in certain specific circumstances in the definition of a field or function on a composite type, an entitlement mapping may be used in an `auth` modifier.

When a field is defined with an entitlement mapping:

`_10

entitlement mapping M {

_10

// omitted

_10

}

_10

resource interface I {

_10

access(M)

_10

let foo: auth(M) &T

_10

}`

Here, the `M` in `auth(M) &T` indicates that the entitlements that the reference produced by an `iRef.foo` access will have
are determined by the entitlements to `I` that `iRef` has, for some `iRef` value that is a reference to `{I}`. Conceptually,
it creates a correspondence between the "output" reference's type and the "input" access modifier.

When an accessor function is defined with an entitlement mapping:

`_12

entitlement mapping M {

_12

// omitted

_12

}

_12

resource I {

_12

access(self)

_12

let myField: T

_12

_12

access(M)

_12

fun getMyField(): auth(M) &T {

_12

return &self.myField as auth(M) &T

_12

}

_12

}`

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

`_10

resource Collection {

_10

_10

// Primitive-typed field

_10

access(all)

_10

var id: String

_10

_10

// Dictionary typed field

_10

access(all)

_10

var ownedNFTs: @{UInt64: NFT}

_10

}`

Thus,

`_10

var collectionRef: &Collection = ...

_10

_10

// `collectionRef.ownedNFTs` would return a reference of type `&{UInt64: NFT}`.

_10

var ownedNFTsRef: &{UInt64: NFT} = collectionRef.ownedNFTs

_10

_10

// Whereas, `collectionRef.id` would return the value, since it is a primitive type.

_10

var id: String = collectionRef.id`

Similarly, accessing an element of an array/dictionary will return a reference.

`_10

// Index-access to an array reference would return a reference to the element.

_10

var resourceArrayRef: &[AnyResource] = ...

_10

var elementRef: &AnyResource = collectionArrayRef[2]

_10

_10

// Whereas, if the array is of a primitive type, it will return the concrete value.

_10

var intArrayRef: &[Int] = ...

_10

var element: Int = intArrayRef[2]`

`_10

// Index-access to a dictionary reference would return a reference to the value.

_10

var resourceDictionaryRef: &{String: AnyResource} = ...

_10

var valueRef: &AnyResource? = resourceDictionaryRef["two"]

_10

_10

// Whereas, if the dictionary values are of a primitive type, it will return the concrete value.

_10

var intDictionaryRef: &{String: Int} = ...

_10

var value: Int? = intDictionaryRef["two"]`

It is also important to note that, in the above examples, the returned references have no entitlements.
i.e: they are non-auth references.

To get entitled references for struct/resource fields, they must be defined with [entitlement mappings](/docs/language/access-control#entitlement-mappings).
However, accessing a value at an index/key of an array/dictionary reference would always return a non-auth reference.

### Index Assignment[​](#index-assignment "Direct link to Index Assignment")

Assigning to an index of an array or a dictionary reference is an entitled-operation.
In other words, the assignment operator for arrays/dictionaries would also have the `Mutate` and `Insert`
[built-in entitlements](/docs/language/access-control#built-in-mutability-entitlements).

Think of assignment as a built-in function with `Mutate` or `(Insert, Remove)` entitlements. e.g:

`_10

access(Mutate | (Insert, Remove))

_10

set(keyOrIndex, value) { ... }`

Note that the syntax for having nested entitlements in access modifiers like `(Mutate | (Insert, Remove))`
is not currently supported, but this is for illustration purpose only.

Thus,

`_14

var arrayRef = &array as &[String]

_14

arrayRef[2] = "John" // Static Error: updating via a read-only reference

_14

_14

var mutableArrayRef = &array as auth(Mutate) &[String]

_14

mutableArrayRef[2] = "John" // OK

_14

_14

var insertableArrayRef = &array as auth(Insert) &[String]

_14

insertableArrayRef[2] = "John" // Static Error: doesn't have the required entitlement

_14

_14

var removableArrayRef = &array as auth(Remove) &[String]

_14

removableArrayRef[2] = "John" // Static Error: doesn't have the required entitlement

_14

_14

var insertableAndRemovableArrayRef = &array as auth(Insert, Remove) &[String]

_14

insertableAndRemovableArrayRef[2] = "John" // OK`

## Reference Validity[​](#reference-validity "Direct link to Reference Validity")

Ephemeral references stay valid throughout the course of the program.
However, **references to resources** can become invalid during the execution of a program,
if the referenced resource is moved or destroyed after taking the reference.

`_11

let r <-create R()

_11

_11

// Take a reference to resource.

_11

let ref = &r as &R

_11

_11

// Then transfer the resource into an account.

_11

// This will invalidate all the references taken to the resource `r`.

_11

account.storage.save(<-r, to: /storage/r)

_11

_11

// Static error, since the referenced resource has been moved.

_11

ref.id = 2`

A reference is invalidated upon the first transfer of the underlying resource,
regardless of the origin and the destination.

`_10

let ref = &r as &R

_10

_10

// Moving a resource to a different variable invalidates all references to it.

_10

let r2 <- r

_10

_10

// Static error, since the referenced resource has been moved.

_10

ref.id = 2`

tip

Invalidations of storage references are not statically caught, but only at run-time.

## Dereferencing values[​](#dereferencing-values "Direct link to Dereferencing values")

Primitive values (and arrays or dictionaries of primitive values) can be "de-referenced" using the unary `*` operator.
This operation produces a copy of the referenced value, so e.g. given some example code:

`_10

var x = 3

_10

let ref: &Int = &x

_10

var y = *ref

_10

y = y + 1`

At the end of the execution of this code, `y` will clearly be `4`, but `x` will still be `3`, as the `*ref` operation copies
the value. This can be seen even more clearly using an example with arrays:

`_10

let x = [0]

_10

let ref: &[Int] = &x

_10

var y = *ref

_10

y.append(1)`

At the end of this execution, `y` will contain `[0, 1]`, while `x` will remain `[0]` only.

References to non-primitive values (e.g. structs, resources, contracts and enums) cannot be dereferenced.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/references.mdx)

[Previous

Intersection Types](/docs/language/intersection-types)[Next

Imports](/docs/language/imports)

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