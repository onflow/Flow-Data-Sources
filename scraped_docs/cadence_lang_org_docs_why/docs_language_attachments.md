# Source: https://cadence-lang.org/docs/language/attachments

Attachments | Cadence



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
* Attachments

On this page

# Attachments

Attachments are a feature of Cadence designed to allow developers to extend a struct or resource type
(even one that they did not declare) with new functionality,
without requiring the original author of the type to plan or account for the intended behavior.

## Declaring Attachments[​](#declaring-attachments "Direct link to Declaring Attachments")

Attachments are declared with the `attachment` keyword, which would be declared using a new form of composite declaration:
`attachment <Name> for <Type>: <Conformances> { ... }`, where the attachment functions and fields are declared in the body.
As such, the following would be examples of legal declarations of attachments:

`_12

access(all)

_12

attachment Foo for MyStruct {

_12

// ...

_12

}

_12

_12

attachment Bar for MyResource: MyResourceInterface {

_12

// ...

_12

}

_12

_12

attachment Baz for MyInterface: MyOtherInterface {

_12

// ...

_12

}`

Like all other type declarations, attachments may only be declared with `all` access.

Specifying the kind (struct or resource) of an attachment is not necessary, as its kind will necessarily be the same as the type it is extending.
Note that the base type may be either a concrete composite type or an interface.
In the former case, the attachment is only usable on values specifically of that base type,
while in the case of an interface the attachment is usable on any type that conforms to that interface.

The body of the attachment follows the same declaration rules as composites.
In particular, they may have both field and function members,
and any field members must be initialized in an initializer.
Only resource-kinded attachments may have resource members.

The `self` keyword is available in attachment bodies, but unlike in a composite,
`self` is a **reference** type, rather than a composite type:
In an attachment declaration for `A`, the type of `self` would be a reference to `A`, rather than `A` like in other composite declarations.
The specific entitlements that this reference has depends on the access modifier associated with the member function in which the `self` reference
appears, and is explained in more detail below.

If a resource with attachments on it is `destroy`ed, all its attachments are `destroy`ed in an unspecified order.
The only guarantee about the order in which attachments are destroyed in this case is that the base resource will be the last thing destroyed.

Within the body of an attachment, there is also a `base` keyword available,
which contains a reference to the attachment's base value;
that is, the composite to which the attachment is attached.
Its type, therefore, is a reference to the attachment's declared base type.
So, for an attachment declared `access(all) attachment Foo for Bar`, the `base` field of `Foo` would have type `&Bar`.

So, for example, this would be a valid declaration of an attachment:

`_29

access(all)

_29

resource R {

_29

_29

access(all)

_29

let x: Int

_29

_29

init (_ x: Int) {

_29

self.x = x

_29

}

_29

_29

access(all)

_29

fun foo() { ... }

_29

}

_29

_29

access(all)

_29

attachment A for R {

_29

_29

access(all)

_29

let derivedX: Int

_29

_29

init (_ scalar: Int) {

_29

self.derivedX = base.x * scalar

_29

}

_29

_29

access(all)

_29

fun foo() {

_29

base.foo()

_29

}

_29

}`

For the purposes of external mutation checks or [access control](/docs/language/access-control),
the attachment is considered a separate declaration from its base type.
A developer cannot, therefore, access any `access(self)` fields
(or `access(contract)` fields if the base was defined in a different contract to the attachment)
on the `base` value, nor can they mutate any array or dictionary typed fields.

`_31

access(all)

_31

resource interface SomeInterface {

_31

_31

access(all)

_31

let b: Bool

_31

_31

access(self)

_31

let i: Int

_31

_31

access(all)

_31

let a: [String]

_31

}

_31

access(all)

_31

attachment SomeAttachment for SomeContract.SomeStruct {

_31

_31

access(all)

_31

let i: Int

_31

_31

init(i: Int) {

_31

if base.b {

_31

self.i = base.i // cannot access `i` on the `base` value

_31

} else {

_31

self.i = i

_31

}

_31

}

_31

_31

access(all)

_31

fun foo() {

_31

base.a.append("hello") // cannot mutate `a` outside of the composite where it was defined

_31

}

_31

}`

Within an attachment's member function, the `base` and `self` references are entitled to the same entitlements that the function's access modifier specifies.
E.g., in an attachment declared as `access(all) attachment A for R`, within a definition of a function `access(E) fun foo()`,
the type of `base` would be `auth(E) &R`, and the type of `self` would be `auth(E) &A`. Thus the following definition would work:

`_14

resource R {

_14

access(E)

_14

fun foo() {

_14

//...

_14

}

_14

}

_14

_14

access(all)

_14

attachment A for R {

_14

access(E)

_14

fun bar() {

_14

base.foo() // available because `E` is required above, and thus `base` is type `auth(E) &R`.

_14

}

_14

}`

while this would not:

`_16

resource R {

_16

access(E)

_16

fun foo() {

_16

//...

_16

}

_16

}

_16

_16

access(all)

_16

attachment A for R {

_16

_16

access(self)

_16

fun bar() {

_16

base.foo() // unavailable because this function has `self` access, and thus `base` only is type `&R`.

_16

}

_16

_16

}`

Note that as a result of how entitlements are propagated to the `self` and `base` values here, attachment definitions can only support
the same entitlements that their base values support; i.e. some attachment `A` defined for `R` can only use an entitlement `E` in its definition
if `R` also uses `E` in its definition (or the definition of any interfaces to which it conforms).

### Attachment Types[​](#attachment-types "Direct link to Attachment Types")

An attachment declared with `access(all) attachment A for C { ... }` will have a nominal type `A`.

It is important to note that attachments are not first class values, and as such their usage is limited in certain ways.
In particular, their types cannot appear outside of a reference type.
So, for example, given an attachment declaration `attachment A for X {}`, the types `A`, `A?`, `[A]` and `fun(): A` are not valid type annotations,
while `&A`, `&A?`, `[&A]` and `fun(): &A` are valid.

## Creating Attachments[​](#creating-attachments "Direct link to Creating Attachments")

An attachment is created using an `attach` expression,
where the attachment is both initialized and attached to the base value in a single operation.
Attachments are not first-class values; they cannot exist independently of a base value,
nor can they be moved around on their own.
This means that an `attach` expression is the only place in which an attachment constructor can be called.
Tightly coupling the creation and attaching of attachment values helps to make reasoning about attachments simpler for the user.
Also for this reason, resource attachments do not need an explicit `<-` move operator when they appear in an `attach` expression.

An attach expression consists of the `attach` keyword, a constructor call for the attachment value,
the `to` keyword, and an expression that evaluates to the base value for that attachment.
Any arguments required by the attachment's initializer are provided in its constructor call.

`_13

access(all)

_13

resource R {}

_13

_13

access(all)

_13

attachment A for R {

_13

init(x: Int) {

_13

//...

_13

}

_13

}

_13

_13

// ...

_13

let r <- create R()

_13

let r2 <- attach A(x: 3) to <-r`

The expression on the right-hand side of the `to` keyword must evaluate to a composite value whose type is a subtype of the attachment's base,
and is evaluated before the call to the constructor on the left side of `to`.
This means that the `base` value is available inside of the attachment's initializer,
but it is important to note that the attachment being created will not be accessible on the `base`
(see the accessing attachments section below) until after the constructor finishes executing.

`_12

access(all)

_12

resource interface I {}

_12

_12

access(all)

_12

resource R: I {}

_12

_12

access(all)

_12

attachment A for I {}

_12

_12

// ...

_12

let r <- create R() // has type @R

_12

let r2 <- attach A() to <-r // ok, because `R` is a subtype of `I`, still has type @R`

Because attachments are stored on their bases by type, there can only be one attachment of each type present on a value at a time.
Cadence will raise a runtime error if a user attempts to add an attachment to a value when one it already exists on that value.
The type returned by the `attach` expression is the same type as the expression on the right-hand side of the `to`;
attaching an attachment to a value does not change its type.

## Accessing Attachments[​](#accessing-attachments "Direct link to Accessing Attachments")

Attachments are accessed on composites via type-indexing:
composite values function like a dictionary where the keys are types and the values are attachments.
So given a composite value `v`, one can look up the attachment named `A` on `v` using indexing syntax:

`_10

let a = v[A] // has type `&A?``

This syntax requires that `A` is a nominal attachment type,
and that `v` has a composite type that is a subtype of `A`'s declared base type.
As mentioned above, attachments are not first-class values,
so this indexing returns a reference to the attachment on `v`, rather than the attachment itself.
If the attachment with the given type does not exist on `v`, this expression returns `nil`.

The set of entitlements to which the result of an attachment access is authorized is the same as the set of entitlements to which the base
value is authorized. So, for example, given the following definition for `A`:

`_25

entitlement E

_25

entitlement F

_25

_25

resource R {

_25

access(E)

_25

fun foo() {

_25

// ...

_25

}

_25

_25

access(F)

_25

fun bar() {

_25

// ...

_25

}

_25

}

_25

_25

attachment A for R {

_25

access(E | F)

_25

fun qux() {

_25

// ...

_25

}

_25

}

_25

_25

// ...

_25

_25

let a = v[A]!`

When `v` has type `&R`, the resulting type of `a` will be an unauthorized `&A`.
Contrarily, if `v` has type `auth(E) &R`, then the type of `a` will be authorized to the same: `auth(E) &A`.
Finally, when `v` is not a reference (i.e. an owned value of type `R`), then `a` will be "fully entitled" to `A`; it will be granted
all the entitlements mentioned by `A`, i.e. in this case it will have type `auth(E, F) &A`.

This is roughly equivalent to the behavior of the `Identity` [entitlement mapping](/docs/language/access-control#entitlement-mappings); indeed, attachments can be thought of
as being `Identity`-mapped fields on their base value.

## Removing Attachments[​](#removing-attachments "Direct link to Removing Attachments")

Attachments can be removed from a value with a `remove` statement.
The statement consists of the `remove` keyword, the nominal type for the attachment to be removed,
the `from` keyword, and the value from which the attachment is meant to be removed.

The value on the right-hand side of `from` must be a composite value whose type is a subtype of the attachment type's declared base.

E.g., to remove an `A` attachment from some resource `r` whose type supports that attachment:

`_10

remove A from r`

After the statement executes, the composite value on the right-hand side of `from` will no longer contain the attachment.
If the value does not contain the attachment that appears after the `remove` keyword, this statement has no effect.

Attachments may be removed from a type in any order,
so users should take care not to design any attachments that rely on specific behaviors of other attachments,
as there is no to require that an attachment depend on another or to require that a type has a given attachment when another attachment is present.

If a resource containing attachments is `destroy`ed, all its attachments will be `destroy`ed in an arbitrary order.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/attachments.mdx)

[Previous

Inbox](/docs/language/accounts/inbox)[Next

Contracts](/docs/language/contracts)

###### Rate this page

😞😐😊

* [Declaring Attachments](#declaring-attachments)
  + [Attachment Types](#attachment-types)
* [Creating Attachments](#creating-attachments)
* [Accessing Attachments](#accessing-attachments)
* [Removing Attachments](#removing-attachments)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.