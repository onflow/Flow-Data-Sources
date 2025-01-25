# Source: https://cadence-lang.org/docs/language/access-control




Access control | Cadence




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
* Access control
On this page
# Access control

Access control allows making certain parts of a program accessible/visible
and making other parts inaccessible/invisible.

In Cadence, access control consists of:

1. Access control on objects in account storage,
   using [capability security](/docs/language/capabilities).

A user is not able to access an object
unless they own the object or have a reference to that object.
This means that nothing is truly public by default.

Other accounts can not read or write the objects in an account
unless the owner of the account has granted them access
by providing references to the objects.

This kind of access control is covered in the pages
on [capabilities](/docs/language/capabilities)
and [capability management](/docs/language/accounts/capabilities).

2. Access control within contracts and objects,
   using access modifiers (`access` keyword).

This page covers the second part of access control,
using access modifiers.

All declarations, such as [function](/docs/language/functions), [composite types](/docs/language/composite-types), and fields,
must be prefixed with an access modifier, using the `access` keyword.

The access modifier determines where the declaration is accessible/visible.
Fields can only be assigned to and mutated from within the same or inner scope.

For example, to make a function publicly accessible (`access(all)` is explained below):

 `_10access(all)_10fun test() {}`

There are five levels of access control:

* **Public access** means the declaration is accessible/visible in all scopes.
  This includes the current scope, inner scopes, and the outer scopes.
  
  A declaration is made publicly accessible using the `access(all)` modifier.
  
  For example, a public field in a type can be accessed
  on an instance of the type in an outer scope.
* **Entitled access** means the declaration is only accessible/visible
  to the owner of the object, or to [references](/docs/language/references)
  that are authorized to the required [entitlements](#entitlements).
  
  A declaration is made accessible through entitlements by using the `access(E)` syntax,
  where `E` is a set of one or more entitlements,
  or a single [entitlement mapping](#entitlement-mappings).
  
  A reference is considered authorized to an entitlement
  if that entitlement appears in the `auth` portion of the reference type.
  
  For example, an `access(E, F)` field on a resource `R` can only be accessed by an owned (`@R`-typed) value,
  or a reference to `R` that is authorized to the `E` and `F` entitlements (`auth(E, F) &R`).
* **Account access** means the declaration is only accessible/visible
  in the scope of the entire account where it is defined.
  This means that other contracts in the account are able to access it.
  
  A declaration is made accessible by code in the same account,
  for example other contracts, by using the `access(account)` keyword.
* **Contract access** means the declaration is only accessible/visible
  in the scope of the contract that defined it.
  This means that other declarations that are defined in the same contract can access it,
  but not other contracts in the same account.
  
  A declaration is made accessible by code in the same contract
  by using the `access(contract)` keyword.
* **Private access** means the declaration is only accessible/visible
  in the current and inner scopes.
  
  A declaration is made accessible by code in the same containing type
  by using the `access(self)` keyword.
  
  For example, an `access(self)` field can only be accessed
  by functions of the type is part of, not by code in an outer scope.

To summarize the behavior for variable declarations, constant declarations, and fields:

| Declaration kind | Access modifier | Accessible in | Assignable in | Mutable in |
| --- | --- | --- | --- | --- |
| `let` | `access(self)` | Current and inner | *None* | Current and inner |
| `let` | `access(contract)` | Current, inner, and containing contract | *None* | Current and inner |
| `let` | `access(account)` | Current, inner, and other contracts in same account | *None* | Current and inner |
| `let` | `access(all)` | **All** | *None* | Current and inner |
| `let` | `access(E)` | **All** with required entitlements | *None* | Current and inner |
| `var` | `access(self)` | Current and inner | Current and inner | Current and inner |
| `var` | `access(contract)` | Current, inner, and containing contract | Current and inner | Current and inner |
| `var` | `access(account)` | Current, inner, and other contracts in same account | Current and inner | Current and inner |
| `var` | `access(all)` | **All** | Current and inner | Current and inner |
| `var` | `access(E)` | **All** with required entitlements | Current and inner | Current and inner |

Declarations of [composite types](/docs/language/composite-types) must be public.
However, even though the declarations/types are publicly visible,
resources can only be created, and events can only be emitted
from inside the contract they are declared in.

 `_10// Declare a private constant, inaccessible/invisible in outer scope._10//_10access(self)_10let a = 1_10_10// Declare a public constant, accessible/visible in all scopes._10//_10access(all)_10let b = 2`
 `_99// Declare a public struct, accessible/visible in all scopes._99//_99access(all)_99struct SomeStruct {_99_99 // Declare a private constant field which is only readable_99 // in the current and inner scopes._99 //_99 access(self)_99 let a: Int_99_99 // Declare a public constant field which is readable in all scopes._99 //_99 access(all)_99 let b: Int_99_99 // Declare a private variable field which is only readable_99 // and writable in the current and inner scopes._99 //_99 access(self)_99 var c: Int_99_99 // Declare a public variable field which is not settable,_99 // so it is only writable in the current and inner scopes,_99 // and readable in all scopes._99 //_99 access(all)_99 var d: Int_99_99 // Arrays and dictionaries declared without (set) cannot be_99 // mutated in external scopes_99 access(all)_99 let arr: [Int]_99_99 // The initializer is omitted for brevity._99_99 // Declare a private function which is only callable_99 // in the current and inner scopes._99 //_99 access(self)_99 fun privateTest() {_99 // ..._99 }_99_99 // Declare a public function which is callable in all scopes._99 //_99 access(all)_99 fun publicTest() {_99 // ..._99 }_99_99 // The initializer is omitted for brevity._99_99}_99_99let some = SomeStruct()_99_99// Invalid: cannot read private constant field in outer scope._99//_99some.a_99_99// Invalid: cannot set private constant field in outer scope._99//_99some.a = 1_99_99// Valid: can read public constant field in outer scope._99//_99some.b_99_99// Invalid: cannot set public constant field in outer scope._99//_99some.b = 2_99_99// Invalid: cannot read private variable field in outer scope._99//_99some.c_99_99// Invalid: cannot set private variable field in outer scope._99//_99some.c = 3_99_99// Valid: can read public variable field in outer scope._99//_99some.d_99_99// Invalid: cannot set public variable field in outer scope._99//_99some.d = 4_99_99// Invalid: cannot mutate a public field in outer scope._99//_99some.f.append(0)_99_99// Invalid: cannot mutate a public field in outer scope._99//_99some.f[3] = 1_99_99// Valid: can call non-mutating methods on a public field in outer scope_99some.f.contains(0)`
## Entitlements[​](#entitlements "Direct link to Entitlements")

Entitlements provide granular access control to each member of a composite.
Entitlements are declared using the syntax `entitlement E`,
where `E` is the name of the entitlement.

For example, the following code declares two entitlements called `E` and `F`:

 `_10entitlement E_10entitlement F`

Entitlements can be imported from other contracts and used the same way as other types.
When using entitlements defined in another contract, the same qualified name syntax is used as for other types:

 `_10contract C {_10 entitlement E_10}`

Outside of `C`, `E` is used with `C.E` syntax.

Entitlements exist in the same namespace as types, so if a contract declares a resource called `R`,
it is impossible to declare an entitlement that is also called `R`.

Entitlements can be used in access modifiers of composite members (fields and functions)
to specify which references to those composites are allowed to access those members.

An access modifier can include more than one entitlement,
joined with either an `|`, to indicate disjunction ("or"),
or a `,`, to indicate conjunction ("and").
The two kinds of separators cannot be combined in the same set.

For example:

 `_18access(all)_18resource SomeResource {_18_18 // requires a reference to have an `E` entitlement to read this field_18 access(E)_18 let a: Int_18_18 // requires a reference to have either an `E` OR an `F` entitlement to read this field._18 access(E | F)_18 let b: Int_18_18 // requires a reference to have both an `E` AND an `F` entitlement to read this field_18 access(E, F)_18 let c: Int_18_18 // intializers omitted for brevity_18 // ..._18}`

Assuming the following constants exist,
which have owned or [reference](/docs/language/references) types:

 `_10let r: @SomeResource = // ..._10let refE: auth(E) &SomeResource = // ..._10let refF: auth(F) &SomeResource = // ..._10let refEF: auth(E, F) &SomeResource = // ..._10let refEOrF: auth(E | F) &SomeResource = // ...`

The references can be used as follows:

 `_34// valid, because `r` is owned and thus is "fully entitled"_34r.a_34// valid, because `r` is owned and thus is "fully entitled"_34r.b_34// valid, because `r` is owned and thus is "fully entitled"_34r.c_34_34// valid, because `refE` has an `E` entitlement as required_34refE.a_34// valid, because `refE` has one of the two required entitlements_34refE.b_34// invalid, because `refE` only has one of the two required entitlements_34refE.c_34_34// invalid, because `refF` has an `E` entitlement, not an `F`_34refF.a_34// valid, because `refF` has one of the two required entitlements_34refF.b_34// invalid, because `refF` only has one of the two required entitlements_34refF.c_34_34// valid, because `refEF` has an `E` entitlement_34refEF.a_34// valid, because `refEF` has both of the two required entitlements_34refEF.b_34// valid, because `refEF` has both of the two required entitlements_34refEF.c_34_34// invalid, because `refEOrF` might not have an `E` entitlement (it may have `F` instead)_34refEOrF.a_34// valid, because `refEOrF` has one of the two entitlements necessary_34refEOrF.b_34// invalid, because `refEOrF` is only known to have one of the two required entitlements_34refEOrF.c`

Note particularly in this example how the owned value `r` can access all entitled members on `SomeResource`.
Owned values are not affected by entitled declarations.

Further details about authorized references can be found [here](/docs/language/references#authorized-references).

### Entitlement mappings[​](#entitlement-mappings "Direct link to Entitlement mappings")

Entitlement mappings are a way to statically declare how entitlements are propagated
from parents to child objects in a nesting hierarchy.

When objects have fields that are child objects,
entitlement mappings can be used
to grant access to the inner object based on the entitlements of the reference to the parent object.

Consider the following example,
which uses entitlements to control access to an inner resource:

 `_43entitlement OuterEntitlement_43entitlement InnerEntitlement_43_43resource InnerResource {_43_43 access(all)_43 fun foo() { ... }_43_43 access(InnerEntitlement)_43 fun bar() { ... }_43}_43_43resource OuterResource {_43 access(self)_43 let childResource: @InnerResource_43_43 init(childResource: @InnerResource) {_43 self.childResource <- childResource_43 }_43_43 // The parent resource has to provide two accessor functions_43 // which return a reference to the inner resource._43 //_43 // If the reference to the outer resource is unauthorized_43 // and does not have the OuterEntitlement entitlement,_43 // the outer resource allows getting an unauthorized reference_43 // to the inner resource._43 //_43 // If the reference to the outer resource is authorized_43 // and it has the OuterEntitlement entitlement,_43 // the outer resource allows getting an authorized reference_43 // to the inner resource._43_43 access(all)_43 fun getPubRef(): &InnerResource {_43 return &self.childResource as &InnerResource_43 }_43_43 access(OuterEntitlement)_43 fun getEntitledRef(): auth(InnerEntitlement) &InnerResource {_43 return &self.childResource as auth(InnerEntitlement) &InnerResource_43 }_43}`

With this pattern, it is possible to store a `InnerResource` in an `OuterResource`,
and create different ways to access that nested resource depending on the entitlement one possesses.

An unauthorized reference to `OuterResource` can only be used to call the `getPubRef` function,
and thus can only obtain an unauthorized reference to `InnerResource`.
That reference to the `InnerResource` then only allows calling the function `foo`, which is publicly accessible,
but not function `bar`, as it needs the `InnerEntitlement` entitlement, which is not granted.

However an `OuterEntitlement`-authorized reference to the `OuterResource` can be used to call the `getEntitledRef` function,
which returns a `InnerEntitlement`-authorized reference to `InnerResource`,
which in turn can be used to call function `bar`.

This pattern is functional, but it is unfortunate that the accessor functions to `InnerResource` have to be "duplicated".

Entitlement mappings should be used to avoid this duplication.

Entitlement mappings are declared using the syntax:

 `_10entitlement mapping M {_10 // ..._10}`

Where `M` is the name of the mapping.

The body of the mapping contains zero or more rules of the form `A -> B`,
where `A` and `B` are entitlements.
Each rule declares that, given a reference with the entitlement on the left,
a reference with the entitlement on the right is produced.

An entitlement mapping thus defines a function from an input set of entitlements (called the domain)
to an output set (called the range or the image).

Using entitlement mappings, the above example could be more concisely written as:

 `_51entitlement OuterEntitlement_51entitlement InnerEntitlement_51_51// Specify a mapping for entitlements called `OuterToInnerMap`,_51// which maps the entitlement `OuterEntitlement` to the entitlement `InnerEntitlement`._51entitlement mapping OuterToInnerMap {_51 OuterEntitlement -> InnerEntitlement_51}_51_51resource InnerResource {_51 _51 access(all)_51 fun foo() { ... }_51_51 access(InnerEntitlement)_51 fun bar() { ... }_51}_51_51resource OuterResource {_51 // Use the entitlement mapping `OuterToInnerMap`._51 //_51 // This declares that when the field `childResource` is accessed_51 // using a reference authorized with the entitlement `OuterEntitlement`,_51 // then a reference with the entitlement `InnerEntitlement` is returned._51 //_51 // This is equivalent to the two accessor functions_51 // that were necessary in the previous example._51 //_51 access(mapping OuterToInnerMap)_51 let childResource: @InnerResource_51_51 init(childResource: @InnerResource) {_51 self.childResource <- childResource_51 }_51_51 // No accessor functions are needed._51}_51_51// given some value `r` of type `@OuterResource`_51_51let pubRef = &r as &OuterResource_51let pubInnerRef = pubRef.childResource // has type `&InnerResource`_51_51let entitledRef = &r as auth(OuterEntitlement) &OuterResource_51let entitledInnerRef = entitledRef.childResource // has type `auth(InnerEntitlement) &InnerResource`,_51 // as `OuterEntitlement` is defined to map to `InnerEntitlement`._51_51// `r` is an owned value, and is thus considered "fully-entitled" to `OuterResource`,_51// so this access yields a value authorized to the entire image of `OuterToInnerMap`,_51// in this case `InnerEntitlement`, and thus can call `bar`_51r.childResource.bar()`

Entitlement mappings can be used either in accessor functions (as in the example above),
or in fields whose types are either references, or containers (composite types, dictionaries, and arrays).

Entitlement mappings need not be 1:1.
It is valid to define a mapping where many inputs map to the same output,
or where one input maps to many outputs.

Entitlement mappings preserve the "kind" of the set they are mapping.
That is, mapping a conjunction ("and") set produces a conjunction set,
and mapping a disjunction ("or") set produces a disjunction set.

Because entitlement separators cannot be combined in the same set,
attempting to map disjunction ("or") sets through certain complex mappings can result in a type error.

For example, given the following entitlement mapping:

 `_10entitlement mapping M {_10 A -> B_10 A -> C_10 D -> E_10}`

Attempting to map `(A | D)` through `M` will fail,
since `A` should map to `(B, C)` and `D` should map to `E`,
but these two outputs cannot be combined into a disjunction ("or") set.

A good example for how entitlement mappings can be used is the [`Account` type](/docs/language/accounts/).

### The `Identity` entitlement mapping[​](#the-identity-entitlement-mapping "Direct link to the-identity-entitlement-mapping")

`Identity` is a special built-in entitlement mapping that maps every input to itself as the output.
Any entitlement set passed through the `Identity` map will come out unchanged in the output.

For instance:

 `_24entitlement X_24_24resource InnerResource {_24 // ..._24}_24_24resource OuterResource {_24 access(mapping Identity)_24 let childResource: @InnerResource_24_24 access(mapping Identity)_24 getChildResource(): auth(mapping Identity) &InnerResource {_24 return &self.childResource_24 }_24_24 init(childResource: @InnerResource) {_24 self.childResource <- childResource_24 }_24}_24_24fun example(outerRef: auth(X) &OuterResource) {_24 let innerRef = outerRef.childResource // `innerRef` has type `auth(X) &InnerResource`,_24 // as `outerRef` was authorized with entitlement `X`_24}`

One important point to note about the `Identity` mapping, however,
is that its full output range is unknown, and theoretically infinite.
Because of that,
accessing an `Identity`-mapped field or function with an owned value will yield an empty output set.

For example, calling `getChildResource()` on an owned `OuterResource` value,
will produce an unauthorized `&InnerResource` reference.

### Mapping composition[​](#mapping-composition "Direct link to Mapping composition")

Entitlement mappings can be composed.
In the definition of an entitlement mapping,
it is possible to include the definition of one or more other mappings,
to copy over their mapping relations.

An entitlement mapping is included into another entitlement mapping using the `include M` syntax,
where `M` is the name of the entitlement mapping to be included.

In general, an `include M` statement in the definition of an entitlement mapping `N`
is equivalent to simply copy-pasting all the relations defined in `M` into `N`'s definition.

Support for `include` is provided primarily to reduce code-reuse and promote composition.

For example:

 `_14entitlement mapping M {_14 X -> Y_14 Y -> Z_14}_14_14entitlement mapping N {_14 E -> F_14}_14_14entitlement mapping P {_14 include M_14 include N_14 F -> G_14}`

The entitlement mapping `P` includes all of the relations defined in `M` and `N`,
along with the additional relations defined in its own definition.

It is also possible to include the `Identity` mapping.
Any mapping `M` that includes the `Identity` mapping will map its input set to itself,
along with any additional relations defined in the mapping,
or in other included mappings.

For instance:

 `_10entitlement mapping M {_10 include Identity_10 X -> Y_10}`

The mapping `M` maps the entitlement set `(X)` to `(X, Y)`,
and `(Y)` to `(Y)`.

Includes that produce a cyclical mapping are rejected by the type-checker.

### Built-in mutability entitlements[​](#built-in-mutability-entitlements "Direct link to Built-in mutability entitlements")

A prominent use-case of entitlements is to control access to object based on mutability.

For example, in a composite, the author would want to control the access to certain fields to be read-only,
and some fields to be mutable, etc.

In order to support this, the following built-in entitlements can be used:

* `Insert`
* `Remove`
* `Mutate`

These are primarily used by the built-in [array](/docs/language/values-and-types#arrays)
and [dictionary](/docs/language/values-and-types#dictionaries) functions,
but are available to be used in access modifiers of any declaration.

While Cadence does not support entitlement composition or inheritance,
the `Mutate` entitlement is intended to be used as an equivalent form
to the conjunction of the `(Insert, Remove)` entitlement set.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/access-control.md)[PreviousResources](/docs/language/resources)[NextCapabilities](/docs/language/capabilities)
###### Rate this page

😞😐😊

* [Entitlements](#entitlements)
  + [Entitlement mappings](#entitlement-mappings)
  + [The `Identity` entitlement mapping](#the-identity-entitlement-mapping)
  + [Mapping composition](#mapping-composition)
  + [Built-in mutability entitlements](#built-in-mutability-entitlements)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

