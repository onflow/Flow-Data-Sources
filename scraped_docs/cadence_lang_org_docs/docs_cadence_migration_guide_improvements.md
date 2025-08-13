# Source: https://cadence-lang.org/docs/cadence-migration-guide/improvements

Cadence 1.0 Improvements & New Features | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)

  + [Improvements & New Features](/docs/cadence-migration-guide/improvements)
  + [NFT Cadence 1.0 Guide](/docs/cadence-migration-guide/nft-guide)
  + [FT Cadence 1.0 Guide](/docs/cadence-migration-guide/ft-guide)
  + [Core Contracts Guide](/docs/cadence-migration-guide/core-contracts-guide)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* Improvements & New Features

On this page

# Cadence 1.0 Improvements & New Features

## 💫 New features[​](#-new-features "Direct link to 💫 New features")

View Functions added ([FLIP 1056](https://github.com/onflow/flips/blob/main/cadence/20220715-cadence-purity-analysis.md))

#### 💡 Motivation[​](#-motivation "Direct link to 💡 Motivation")

View functions enable developers to enhance the reliability and safety of their programs, facilitating a clearer understanding of the impacts of their own code and that of others.

Developers can mark their functions as `view`, which disallows the function from performing state changes. That also makes the intent of functions clear to other programmers, as it allows them to distinguish between functions that change state and ones that do not.

#### ℹ️ Description[​](#ℹ️-description "Direct link to ℹ️ Description")

Cadence has added support for annotating functions with the `view` keyword, which enforces that no “mutating” operations occur inside the body of the function. The `view` keyword is placed before the `fun` keyword in a function declaration or function expression.

If a function has no `view` annotation, it is considered “non-view”, and users should encounter no difference in behavior in these functions from what they are used to.

If a function does have a `view` annotation, then the following mutating operations are not allowed:

* Writing to, modifying, or destroying any resources
* Writing to or modifying any references
* Assigning to or modifying any variables that cannot be determined to have been created locally inside of the `view` function in question. In particular, this means that captured and global variables cannot be written in these functions
* Calling a non-`view` function

This feature was proposed in [FLIP 1056](https://github.com/onflow/flips/blob/main/cadence/20220715-cadence-purity-analysis.md). To learn more, please consult the FLIP and documentation.

#### 🔄 Adoption[​](#-adoption "Direct link to 🔄 Adoption")

You can adopt view functions by adding the `view` modifier to all functions that do not perform mutating operations.

#### ✨ Example[​](#-example "Direct link to ✨ Example")

Before:
The function `getCount` of a hypothetical NFT collection returns the number of NFTs in the collection.

`_17

access(all)

_17

resource Collection {

_17

_17

access(all)

_17

var ownedNFTs: @{UInt64: NonFungibleToken.NFT}

_17

_17

init () {

_17

self.ownedNFTs <- {}

_17

}

_17

_17

access(all)

_17

fun getCount(): Int {

_17

returnself.ownedNFTs.length

_17

}

_17

_17

/* ... rest of implementation ... */

_17

}`

After:
The function `getCount` does not perform any state changes, it only reads the length of the collection and returns it. Therefore it can be marked as `view.`

`_10

access(all)

_10

view fun getCount(): Int {

_10

// ^^^^ addedreturnself.ownedNFTs.length

_10

}`

Interface Inheritance Added ([FLIP 40](https://github.com/onflow/flips/blob/main/cadence/20221024-interface-inheritance.md))

#### 💡 Motivation[​](#-motivation-1 "Direct link to 💡 Motivation")

Previously, interfaces could not inherit from other interfaces, which required developers to repeat code.
Interface inheritance allows code abstraction and code reuse.

#### ℹ️ Description and ✨ Example[​](#ℹ️description-andexample "Direct link to ℹ️ Description and ✨ Example")

Interfaces can now inherit from other interfaces of the same kind. This makes it easier for developers to structure their conformances and reduces a lot of redundant code.

For example, suppose there are two resource interfaces `Receiver` and `Vault`, and suppose all implementations of the `Vault` would also need to conform to the interface `Receiver`.

Previously, there was no way to enforce this. Anyone who implements the `Vault` would have to explicitly specify that their concrete type also implements the `Receiver`. But it was not always guaranteed that all implementations would follow this informal agreement.
With interface inheritance, the `Vault` interface can now inherit/conform to the `Receiver` interface.

`_11

access(all)

_11

resource interface Receiver {

_11

access(all)

_11

fun deposit(_ something:@AnyResource)

_11

}

_11

_11

access(all)

_11

resource interface Vault: Receiver {

_11

access(all)

_11

fun withdraw(_ amount: Int):@Vault

_11

}`

Thus, anyone implementing the `Vault` interface would also have to implement the `Receiver` interface as well.

`_10

access(all)

_10

resource MyVault: Vault {

_10

// Required!

_10

access(all)

_10

fun withdraw(_ amount: Int):@Vault {}

_10

// Required!

_10

access(all)

_10

fun deposit(_ something:@AnyResource) {}

_10

}`

This feature was proposed in [FLIP 40](https://github.com/onflow/flips/blob/main/cadence/20221024-interface-inheritance.md). To learn more, please consult the FLIP and documentation.

## ⚡ Breaking Improvements[​](#-breaking-improvements "Direct link to ⚡ Breaking Improvements")

Many of the improvements of Cadence 1.0 are fundamentally changing how Cadence works and how it is used. However, that also means it is necessary to break existing code to release this version, which will guarantee stability (no more planned breaking changes) going forward.

Once Cadence 1.0 is live, breaking changes will simply not be acceptable.

So we have, and need to use, this last chance to fix and improve Cadence, so it can deliver on its promise of being a language that provides security and safety, while also providing composability and simplicity.

We fully recognize the frustration developers feel when updates break their code, necessitating revisions. Nonetheless, we are convinced that this inconvenience is justified by the substantial enhancements to Cadence development. These improvements not only make development more effective and enjoyable but also empower developers to write and deploy immutable contracts.

The improvements were intentionally bundled into one release to avoid breaking Cadence programs multiple times.

 **2024-04-24** Public Capability Acquisition No Longer Returns Optional Capabilities ([FLIP 242](https://github.com/onflow/flips/blob/main/cadence/20240123-capcon-get-capability-api-improvement.md))

**Note** This is a recent change that may not be reflected in emulated migrations or all tools yet. Likewise, this may affect existing staged contracts which do not conform to this new requirement. Please ensure your contracts are updated and re-staged, if necessary, to match this new requirement.

#### 💡 Motivation[​](#-motivation-2 "Direct link to 💡 Motivation")

In the initial implementation of the new Capability Controller API (a change that is new in Cadence 1.0, proposed in [FLIP 798](https://github.com/onflow/flips/blob/main/cadence/20220203-capability-controllers.md)), `capabilities.get<T>` would return an optional capability, `Capability<T>?`. When the no capability was published under the requested path, or when type argument `T` was not a subtype of the runtime type of the capability published under the requested path, the capability would be `nil`.

This was a source of confusion among developers, as previously `account.getCapability<T>` did not return an optional capability, but rather one that would simply fail `capability.borrow` if the capability was invalid.

It was concluded that this new behaviour was not ideal, and that there a benefit to an invalid Capability not being `nil`, even if it is not borrowable. A `nil` capability lacked information that was previously available with an invalid capability - primarily the type and address of the capability. Developers may have wanted to make use of this information, and react to the capability being invalid, as opposed to an uninformative `nil` value and encountering a panic scenario.

#### ℹ️ Description[​](#ℹ️-description-1 "Direct link to ℹ️ Description")

The `capabilities.get<T>` function now returns an invalid capability when no capability is published under the requested path, or when the type argument `T` is not a subtype of the runtime type of the capability published under the requested path.

This capability has the following properties:

* Always return `false` when `Capability<T>.check` is called.
* Always return `nil` when `Capability<T>.borrow` is called.
* Have an ID of `0`.
* Have a runtime type that is the same as the type requested in the type argument of `capabilities.get<T>`.

  

#### 🔄 Adoption[​](#-adoption-1 "Direct link to 🔄 Adoption")

If you have not updated your code to Cadence 1.0 yet, you will need to follow the same guidelines for updating to the Capability Controller API as you would have before, but will need to handle the new invalid capability type instead of an optional capability.

If you have already updated your code to use `capabilities.get<T>`, and are handling the capability as an optional type, you may need to update your code to handle the new non-optional invalid capability type instead.

#### ✨ Example[​](#-example-1 "Direct link to ✨ Example")

**Before:**

`_10

let capability = account.capabilities.get<&MyNFT.Collection>(/public/NFTCollection)

_10

if capability == nil {

_10

// Handle the case where the capability is nil

_10

}`

**After:**

`_10

let capability = account.capabilities.get<&MyNFT.Collection>(/public/NFTCollection)

_10

if !capability.check() {

_10

// Handle the case where the capability is invalid

_10

}`

**2024-04-23** Matching Access Modifiers for Interface Implementation Members are now Required ([FLIP 262](https://github.com/onflow/flips/blob/main/cadence/20240415-remove-non-public-entitled-interface-members.md))

**Note** This is a recent change that may not be reflected in emulated migrations or all tools yet. Likewise, this may affect existing staged contracts which do not conform to this new requirement. Please ensure your contracts are updated and re-staged, if necessary, to match this new requirement.

#### 💡 Motivation[​](#-motivation-3 "Direct link to 💡 Motivation")

Previously, the access modifier of a member in a type conforming to / implementing an interface
could not be more restrictive than the access modifier of the member in the interface.
That meant an implementation may have choosen to use a more permissive access modifier than the interface.

This may have been surprising to developers, as they may have assumed that the access modifier of the member
in the interface was a *requirement* / *maximum*, not just a minimum, especially when using
a non-public / non-entitled access modifier (e.g. `access(contract)`, `access(account)`).

Requiring access modifiers of members in the implementation to match the access modifiers
of members given in the interface, helps avoid confusion and potential footguns.

#### ℹ️ Description[​](#ℹ️-description-2 "Direct link to ℹ️ Description")

If an interface member has an access modifier, a composite type that conforms to it / implements
the interface must use exactly the same access modifier.

#### 🔄 Adoption[​](#-adoption-2 "Direct link to 🔄 Adoption")

Update the access modifiers of members in composite types that conform to / implement interfaces if they do not match the access modifiers of the members in the interface.

#### ✨ Example[​](#-example-2 "Direct link to ✨ Example")

**Before:**

`_11

access(all)

_11

resource interface I {

_11

access(account)

_11

fun foo()

_11

}

_11

_11

access(all)

_11

resource R: I {

_11

access(all)

_11

fun foo() {}

_11

}`

**After:**

`_11

access(all)

_11

resource interface I {

_11

access(account)

_11

fun foo()

_11

}

_11

_11

access(all)

_11

resource R: I {

_11

access(account)

_11

fun foo() {}

_11

}`

Conditions No Longer Allow State Changes ([FLIP 1056](https://github.com/onflow/flips/blob/main/cadence/20220715-cadence-purity-analysis.md))

#### 💡 Motivation[​](#-motivation-4 "Direct link to 💡 Motivation")

In the current version of Cadence, pre-conditions and post-conditions may perform state changes, e.g. by calling a function that performs a mutation. This may result in unexpected behavior, which might lead to bugs.

To make conditions predictable, they are no longer allowed to perform state changes.

#### ℹ️ Description[​](#ℹ️-description-3 "Direct link to ℹ️ Description")

Pre-conditions and post-conditions are now considered `view` contexts, meaning that any operations that would be prevented inside of a `view` function are also not permitted in a pre-condition or post-condition.

This is to prevent underhanded code wherein a user modifies global or contract state inside of a condition, where they are meant to simply be asserting properties of that state.

In particular, since only expressions were permitted inside conditions already, this means that if users wish to call any functions in conditions, these functions must now be made `view` functions.

This improvement was proposed in [FLIP 1056](https://github.com/onflow/flips/blob/main/cadence/20220715-cadence-purity-analysis.md). To learn more, please consult the FLIP and documentation.

#### 🔄 Adoption[​](#-adoption-3 "Direct link to 🔄 Adoption")

Conditions which perform mutations will now result in the error “Impure operation performed in view context”.
Adjust the code in the condition so it does not perform mutations.

The condition may be considered mutating, because it calls a mutating, i.e. non-`view` function. It might be possible to mark the called function as `view`, and the body of the function may need to get updated in turn.

#### ✨ Example[​](#-example-3 "Direct link to ✨ Example")

**Before:**

The function `withdraw` of a hypothetical NFT collection interface allows the withdrawal of an NFT with a specific ID. In its post-condition, the function states that at the end of the function, the collection should have exactly one fewer item than at the beginning of the function.

`_15

access(all)

_15

resource interface Collection {

_15

_15

access(all)

_15

fun getCount(): Int

_15

_15

access(all)

_15

fun withdraw(id: UInt64):@NFT {

_15

post {

_15

getCount() == before(getCount()) - 1

_15

}

_15

}

_15

_15

/* ... rest of interface ... */

_15

}`

**After:**

The calls to `getCount` in the post-condition are not allowed and result in the error “Impure operation performed in view context”, because the `getCount` function is considered a mutating function, as it does not have the `view` modifier.

Here, as the `getCount` function only performs a read-only operation and does not change any state, it can be marked as `view`.

`_10

access(all)

_10

view fun getCount(): Int

_10

// ^^^^`

Missing or Incorrect Argument Labels Get Reported

#### 💡 Motivation[​](#-motivation-5 "Direct link to 💡 Motivation")

Previously, missing or incorrect argument labels of function calls were not reported. This had the potential to confuse developers or readers of programs, and could potentially lead to bugs.

#### ℹ️ Description[​](#ℹ️-description-4 "Direct link to ℹ️ Description")

Function calls with missing argument labels are now reported with the error message “missing argument label”, and function calls with incorrect argument labels are now reported with the error message “incorrect argument label”.

#### 🔄 Adoption[​](#-adoption-4 "Direct link to 🔄 Adoption")

* Function calls with missing argument labels should be updated to include the required argument labels.
* Function calls with incorrect argument labels should be fixed by providing the correct argument labels.

#### ✨ Example[​](#-example-4 "Direct link to ✨ Example")

Contract `TestContract` deployed at address `0x1`:

`_18

access(all)

_18

contract TestContract {

_18

_18

access(all)

_18

structTestStruct {

_18

_18

access(all)

_18

let a: Int

_18

_18

access(all)

_18

let b: String

_18

_18

init(first: Int, second: String) {

_18

self.a = first

_18

self.b = second

_18

}

_18

}

_18

}`

**Incorrect program**:

The initializer of `TestContract.TestStruct` expects the argument labels `first` and `second`.

However, the call of the initializer provides the incorrect argument label `wrong` for the first argument, and is missing the label for the second argument.

`_10

// Script

_10

import TestContract from 0x1

_10

_10

access(all)

_10

fun main() {

_10

TestContract.TestStruct(wrong: 123, "abc")

_10

}`

This now results in the following errors:

`` _11

error: incorrect argument label

_11

--> script:4:34

_11

|

_11

4 | TestContract.TestStruct(wrong: 123, "abc")

_11

| ^^^^^ expected `first`, got `wrong`

_11

_11

error: missing argument label: `second`

_11

--> script:4:46

_11

|

_11

4 | TestContract.TestStruct(wrong: 123, "abc")

_11

| ^^^^^ ``

**Corrected program**:

`_10

// Script

_10

import TestContract from 0x1

_10

_10

access(all)

_10

fun main() {

_10

TestContract.TestStruct(first: 123, second: "abc")

_10

}`

We would like to thank community member @justjoolz for reporting this bug.

Incorrect Operators In Reference Expressions Get Reported ([FLIP 941](https://github.com/onflow/flips/blob/main/cadence/20220516-reference-creation-semantics.md))

#### 💡 Motivation[​](#-motivation-6 "Direct link to 💡 Motivation")

Previously, incorrect operators in reference expressions were not reported.

This had the potential to confuse developers or readers of programs, and could potentially lead to bugs.

#### ℹ️ Description[​](#ℹ️-description-5 "Direct link to ℹ️ Description")

The syntax for reference expressions is `&v as &T`, which represents taking a reference to value `v` as type `T`.
Reference expressions that used other operators, such as `as?` and `as!`, e.g. `&v as! &T`, were incorrect and were previously not reported as an error.

The syntax for reference expressions improved to just `&v`. The type of the resulting reference must still be provided explicitly.
If the type is not explicitly provided, the error “cannot infer type from reference expression: requires an explicit type annotation” is reported.

For example, existing expressions like `&v as &T` provide an explicit type, as they statically assert the type using `as &T`. Such expressions thus keep working and do *not* have to be changed.

Another way to provide the type for the reference is by explicitly typing the target of the expression, for example, in a variable declaration, e.g. via `let ref: &T = &v`.

This improvement was proposed in [FLIP 941](https://github.com/onflow/flips/blob/main/cadence/20220516-reference-creation-semantics.md). To learn more, please consult the FLIP and documentation.

#### 🔄 Adoption[​](#-adoption-5 "Direct link to 🔄 Adoption")

Reference expressions which use an operator other than `as` need to be changed to use the `as` operator.
In cases where the type is already explicit, the static type assertion (`as &T`) can be removed.

#### ✨ Example[​](#-example-5 "Direct link to ✨ Example")

**Incorrect program**:
The reference expression uses the incorrect operator `as!`.

`_10

let number = 1

_10

let ref = &number as! &Int`

This now results in the following error:

`_10

error: cannot infer type from reference expression: requires an explicit type annotation

_10

--> test:3:17

_10

|

_10

3 |let ref = &number as! &Int

_10

| ^`

**Corrected program**:

`_10

let number = 1

_10

let ref = &number as &Int`

Alternatively, the same code can now also be written as follows:

`_10

let number = 1

_10

let ref: &Int = &number`

Tightening Of Naming Rules

#### 💡 Motivation[​](#-motivation-7 "Direct link to 💡 Motivation")

Previously, Cadence allowed language keywords (e.g. `continue`, `for`, etc.) to be used as names. For example, the following program was allowed:

`_10

fun continue(import: Int, break: String) { ... }`

This had the potential to confuse developers or readers of programs, and could potentially lead to bugs.

#### ℹ️ Description[​](#ℹ️-description-6 "Direct link to ℹ️ Description")

Most language keywords are no longer allowed to be used as names.
Some keywords are still allowed to be used as names, as they have limited significance within the language. These allowed keywords are as follows:

* `from`: only used in import statements `import foo from ...`
* `account`: used in access modifiers `access(account) let ...`
* `all`: used in access modifier `access(all) let ...`
* `view`: used as modifier for function declarations and expressions `view fun foo()...`, let `f = view fun () ...`
  Any other keywords will raise an error during parsing, such as:

`_10

let break: Int = 0

_10

// ^ error: expected identifier after start of variable declaration, got keyword break`

#### 🔄 Adoption[​](#-adoption-6 "Direct link to 🔄 Adoption")

Names which use language keywords must be renamed.

#### ✨ Example[​](#-example-6 "Direct link to ✨ Example")

**Before:**
A variable is named after a language keyword.

`_10

let contract = signer.borrow<&MyContract>(name: "MyContract")

_10

// ^ error: expected identifier after start of variable declaration, got keyword contract`

**After:**
The variable is renamed to avoid the clash with the language keyword.

`_10

let myContract = signer.borrow<&MyContract>(name: "MyContract")`

Result of `toBigEndianBytes()` for `U?Int(128|256)` Fixed

#### 💡 Motivation[​](#-motivation-8 "Direct link to 💡 Motivation")

Previously, the implementation of `.toBigEndianBytes()` was incorrect for the large integer types `Int128`, `Int256`, `UInt128`, and `UInt256`.

This had the potential to confuse developers or readers of programs, and could potentially lead to bugs.

#### ℹ️ Description[​](#ℹ️-description-7 "Direct link to ℹ️ Description")

Calling the `toBigEndianBytes` function on smaller sized integer types returns the exact number of bytes that fit into the type, left-padded with zeros. For instance, `Int64(1).toBigEndianBytes()` returns an array of 8 bytes, as the size of `Int64` is 64 bits, 8 bytes.

Previously, the `toBigEndianBytes` function erroneously returned variable-length byte arrays without padding for the large integer types `Int128`, `Int256`, `UInt128`, and `UInt256`. This was inconsistent with the smaller fixed-size numeric types, such as `Int8`, and `Int32`.

To fix this inconsistency, `Int128` and `UInt128` now always return arrays of 16 bytes, while `Int256` and `UInt256` return 32 bytes.

#### ✨ Example[​](#-example-7 "Direct link to ✨ Example")

`_10

let someNum: UInt128 = 123456789

_10

let someBytes: [UInt8] = someNum.toBigEndianBytes()

_10

// OLD behavior;

_10

// someBytes = [7, 91, 205, 21]

_10

// NEW behavior:

_10

// someBytes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 91, 205, 21]`

#### 🔄 Adoption[​](#-adoption-7 "Direct link to 🔄 Adoption")

Programs that use `toBigEndianBytes` directly, or indirectly by depending on other programs, should be checked for how the result of the function is used. It might be necessary to adjust the code to restore existing behavior.

If a program relied on the previous behavior of truncating the leading zeros, then the old behavior can be recovered by first converting to a variable-length type, `Int` or `UInt`, as the `toBigEndianBytes` function retains the variable-length byte representations, i.e. the result has no padding bytes.

`_10

let someNum: UInt128 = 123456789

_10

let someBytes: [UInt8] = UInt(someNum).toBigEndianBytes()

_10

// someBytes = [7, 91, 205, 21]`

Syntax for Function Types Improved ([FLIP 43](https://github.com/onflow/flips/blob/main/cadence/20221018-change-fun-type-syntax.md))

#### 💡 Motivation[​](#-motivation-9 "Direct link to 💡 Motivation")

Previously, function types were expressed using a different syntax from function declarations or expressions. The previous syntax was unintuitive for developers, making it hard to write and read code that used function types.

#### ℹ️ Description and ✨ examples[​](#ℹ️-description-andexamples "Direct link to ℹ️ Description and ✨ examples")

Function types are now expressed using the `fun` keyword, just like expressions and declarations. This improves readability and makes function types more obvious.

For example, given the following function declaration:

`_10

fun foo(n: Int8, s: String): Int16 { /* ... */ }`

The function `foo` now has the type `fun(Int8, String): Int16`.
The `:` token is right-associative, so functions that return other functions can have their types written without nested parentheses:

`` _10

fun curriedAdd(_ x: Int): fun(Int): Int {

_10

return fun(_ y: Int): Int {

_10

return x+ y

_10

}

_10

}

_10

// function `curriedAdd` has the type `fun(Int): fun(Int): Int` ``

To further bring the syntax for function types closer to the syntax of function declarations expressions, it is now possible to omit the return type, in which case the return type defaults to `Void`.

`` _10

fun logTwice(_ value: AnyStruct) {// Return type is implicitly `Void`

_10

log(value)

_10

log(value)

_10

}

_10

_10

// The function types of these variables are equivalent

_10

let logTwice1: fun(AnyStruct): Void = logTwice

_10

let logTwice2: fun(AnyStruct) = logTwice ``

As a bonus consequence, it is now allowed for any type to be parenthesized. This is useful for complex type signatures, or for expressing optional functions:

`_10

// A function that returns an optional Int16

_10

let optFun1: fun (Int8): Int16? =

_10

fun (_: Int8): Int? { return nil }

_10

_10

// An optional function that returns an Int16

_10

let optFun2: (fun (Int8): Int16)? = nil`

This improvement was proposed in [FLIP 43](https://github.com/onflow/flips/blob/main/cadence/20221018-change-fun-type-syntax.md).

#### 🔄 Adoption[​](#-adoption-8 "Direct link to 🔄 Adoption")

Programs that use the old function type syntax need to be updated by replacing the surrounding parentheses of function types with the `fun` keyword.

**Before:**

`_10

let baz: ((Int8, String): Int16) = foo

_10

// ^ ^

_10

// surrounding parentheses of function type`

**After:**

`_10

let baz: fun (Int8, String): Int16 = foo`

Entitlements and Safe Down-casting ([FLIP 54](https://github.com/onflow/flips/blob/main/cadence/20221214-auth-remodel.md) & [FLIP 94](https://github.com/onflow/flips/blob/main/cadence/20230623-entitlement-improvements.md))

#### 💡 Motivation[​](#-motivation-10 "Direct link to 💡 Motivation")

Previously, Cadence’s main access-control mechanism, restricted reference types, has been a source of confusion and mistakes for contract developers.

Developers new to Cadence often were surprised and did not understand why access-restricted functions, like the `withdraw` function of the fungible token `Vault` resource type, were declared as `pub`, making the function publicly accessible – access would later be restricted through a restricted type.

It was too easy to accidentally give out a `Capability` with a more permissible type than intended, leading to security problems.
Additionally, because what fields and functions were available to a reference depended on what the type of the reference was, references could not be downcast, leading to ergonomic issues.

#### ℹ️ Description[​](#ℹ️-description-8 "Direct link to ℹ️ Description")

Access control has improved significantly.
When giving another user a reference or `Capability` to a value you own, the fields and functions that the user can access is determined by the type of the reference or `Capability`.

Previously, access to a value of type `T`, e.g. via a reference `&T`, would give access to all fields and functions of `T`. Access could be restricted, by using a restricted type. For example, a restricted reference `&T{I}` could only access members that were `pub` on `I`. Since references could not be downcast, any members defined on `T` but not on `I` were unavailable to this reference, even if they were `pub`.

Access control is now handled using a new feature called Entitlements, as originally proposed across [FLIP 54](https://github.com/onflow/flips/blob/main/cadence/20221214-auth-remodel.md) and [FLIP 94](https://github.com/onflow/flips/blob/main/cadence/20230623-entitlement-improvements.md).

A reference can now be “entitled” to certain facets of an object. For example, the reference `auth(Withdraw) &Vault` is entitled to access fields and functions of `Vault` which require the `Withdraw` entitlement.

Entitlements can be are declared using the new `entitlement` syntax.

Members can be made to require entitlements using the access modifier syntax `access(E)`, where `E` is an entitlement that the user must posses.

For example:

`_10

entitlement Withdraw

_10

_10

access(Withdraw)

_10

fun withdraw(amount: UFix64): @Vault`

References can now always be down-casted, the standalone `auth` modifier is not necessary anymore, and got removed.

For example, the reference `&{Provider}` can now be downcast to `&Vault`, so access control is now handled entirely through entitlements, rather than types.

To learn more, please refer to the [documentation](https://cadence-lang.org/docs/1.0/language/access-control#entitlements).

#### 🔄 Adoption[​](#-adoption-9 "Direct link to 🔄 Adoption")

The access modifiers of fields and functions need to be carefully audited and updated.

Fields and functions that have the `pub` access modifier are now callable by anyone with any reference to that type. If access to the member should be restricted, the `pub` access modifier needs to be replaced with an entitlement access modifier.

When creating a `Capability` or a reference to a value, **it must be carefully considered which entitlements are provided to the recipient of that `Capability` or reference** – only the entitlements which are necessary and not more should be include in the `auth` modifier of the reference type.

#### ✨ Example[​](#-example-8 "Direct link to ✨ Example")

**Before:**
The `Vault` resource was originally written like so:

`_23

access(all)

_23

resource interface Provider {

_23

access(all)

_23

funwithdraw(amount:UFix64): @Vault {

_23

// ...

_23

}

_23

}

_23

_23

access(all)

_23

resource Vault: Provider, Receiver, Balance {

_23

access(all)

_23

fun withdraw(amount:UFix64): @Vault {

_23

// ...

_23

}

_23

_23

access(all)

_23

fun deposit(from: @Vault) {

_23

// ...

_23

}

_23

_23

access(all)

_23

var balance: UFix64

_23

}`

**After:**
The `Vault` resource might now be written like this:

`_26

access(all) entitlement Withdraw

_26

_26

access(all)

_26

resource interface Provider {

_26

access(Withdraw)

_26

funwithdraw(amount:UFix64): @Vault {

_26

// ...

_26

}

_26

}

_26

_26

access(all)

_26

resource Vault: Provider, Receiver, Balance {

_26

_26

access(Withdraw)// withdrawal requires permission

_26

fun withdraw(amount:UFix64): @Vault {

_26

// ...

_26

}

_26

_26

access(all)

_26

fun deposit(from: @Vault) {

_26

// ...

_26

}

_26

_26

access(all)

_26

var balance: UFix64

_26

}`

Here, the `access(Withdraw)` syntax means that a reference to `Vault` must possess the `Withdraw` entitlement in order to be allowed to call the `withdraw` function, which can be given when a reference or `Capability` is created by using a new syntax: `auth(Withdraw) &Vault`.

This would allow developers to safely downcast `&{Provider}` references to `&Vault` references if they want to access functions like `deposit` and `balance`, without enabling them to call `withdraw`.

Removal of `pub` and `priv` Access Modifiers ([FLIP 84](https://github.com/onflow/flips/blob/main/cadence/20230505-remove-priv-and-pub.md))

#### 💡 Motivation[​](#-motivation-11 "Direct link to 💡 Motivation")

With the previously mentioned entitlements feature, which uses `access(E)` syntax to denote entitled access, the `pub`, `priv` and `pub(set)` modifiers became the only access modifiers that did not use the `access` syntax.

This made the syntax inconsistent, making it harder to read and understand programs.

In addition, `pub` and `priv` already had alternatives/equivalents: `access(all)` and `access(self)`.

#### ℹ️ Description[​](#ℹ️-description-9 "Direct link to ℹ️ Description")

The `pub`, `priv` and `pub(set)` access modifiers are being removed from the language, in favor of their more explicit `access(all)` and `access(self)` equivalents (for `pub` and `priv`, respectively).

This makes access modifiers more uniform and better match the new entitlements syntax.

This improvement was originally proposed in [FLIP 84](https://github.com/onflow/flips/blob/main/cadence/20230505-remove-priv-and-pub.md).

#### 🔄 Adoption[​](#-adoption-10 "Direct link to 🔄 Adoption")

Users should replace any `pub` modifiers with `access(all)`, and any `priv` modifiers with `access(self)`.

Fields that were defined as `pub(set)` will no longer be publicly assignable, and no access modifier now exists that replicates this old behavior. If the field should stay publicly assignable, a `access(all)` setter function that updates the field needs to be added, and users have to switch to using it instead of directly assigning to the field.

#### ✨ Example[​](#-example-9 "Direct link to ✨ Example")

**Before:**
Types and members could be declared with `pub` and `priv`:

`_10

pub resource interface Collection {

_10

pub fun getCount(): Int

_10

_10

priv fun myPrivateFunction()

_10

_10

pub(set) let settableInt: Int

_10

_10

/* ... rest of interface ... */

_10

}`

**After:**
The same behavior can be achieved with `access(all)` and `access(self)`

`_18

access(all)

_18

resource interface Collection {

_18

_18

access(all)

_18

fun getCount(): Int

_18

_18

access(self)

_18

fun myPrivateFunction()

_18

_18

access(all)

_18

let settableInt: Int

_18

_18

// Add a public setter method, replacing pub(set)

_18

access(all)

_18

fun setIntValue(_ i:Int): Int

_18

_18

/* ... rest of interface ... */

_18

}`

Replacement of Restricted Types with Intersection Types ([FLIP 85](https://github.com/onflow/flips/blob/main/cadence/20230505-remove-restricted-types.md))

#### 💡 Motivation[​](#-motivation-12 "Direct link to 💡 Motivation")

With the improvements to access control enabled by entitlements and safe down-casting, the restricted type feature is redundant.

#### ℹ️ Description[​](#ℹ️-description-10 "Direct link to ℹ️ Description")

Restricted types have been removed. All types, including references, can now be down-casted, restricted types are no longer used for access control.

At the same time intersection types got introduced. Intersection types have the syntax `{I1, I2, ... In}`, where all elements of the set of types (`I1, I2, ... In`) are interface types. A value is part of the intersection type if it conforms to all the interfaces in the intersection type’s interface set. This functionality is equivalent to restricted types that restricted `AnyStruct` and `AnyResource.`

This improvement was proposed in [FLIP 85](https://github.com/onflow/flips/blob/main/cadence/20230505-remove-restricted-types.md). To learn more, please consult the FLIP and documentation.

#### 🔄 Adoption[​](#-adoption-11 "Direct link to 🔄 Adoption")

Code that relies on the restriction behavior of restricted types can be safely changed to just use the concrete type directly, as entitlements will make this safe. For example, `&Vault{Balance}` can be replaced with just `&Vault`, as access to `&Vault` only provides access to safe operations, like getting the balance – **privileged operations, like withdrawal, need additional entitlements.**

Code that uses `AnyStruct` or `AnyResource` explicitly as the restricted type, e.g. in a reference, `&AnyResource{I}`, needs to remove the use of `AnyStruct` / `AnyResource`. Code that already uses the syntax `&{I}` can stay as-is.

#### ✨ Example[​](#-example-10 "Direct link to ✨ Example")

**Before:**

This function accepted a reference to a `T` value, but restricted what functions were allowed to be called on it to those defined on the `X`, `Y`, and `Z` interfaces.

`` _32

access(all)

_32

resource interface X {

_32

access(all)

_32

fun foo()

_32

}

_32

_32

access(all)

_32

resource interface Y {

_32

access(all)

_32

fun bar()

_32

}

_32

_32

access(all)

_32

resource interface Z {

_32

access(all)

_32

fun baz()

_32

}

_32

_32

access(all)

_32

resource T: X, Y, Z {

_32

// implement interfaces

_32

access(all)

_32

fun qux() {

_32

// ...

_32

}

_32

}

_32

_32

access(all)

_32

fun exampleFun(param: &T{X, Y, Z}) {

_32

// `param` cannot call `qux` here, because it is restricted to

_32

// `X`, `Y` and `Z`.

_32

} ``

**After:**
This function can be safely rewritten as:

`` _33

access(all)

_33

resource interface X {

_33

access(all)

_33

fun foo()

_33

}

_33

_33

access(all)

_33

resource interface Y {

_33

access(all)

_33

fun bar()

_33

}

_33

_33

resource interface Z {

_33

access(all)

_33

fun baz()

_33

}

_33

_33

access(all)

_33

entitlement Q

_33

_33

access(all)

_33

resource T: X, Y, Z {

_33

// implement interfaces

_33

access(Q)

_33

fun qux() {

_33

// ...

_33

}

_33

}

_33

_33

access(all)

_33

fun exampleFun(param: &T) {

_33

// `param` still cannot call `qux` here, because it lacks entitlement `Q`

_33

} ``

Any functions on `T` that the author of `T` does not want users to be able to call publicly should be defined with entitlements, and thus will not be accessible to the unauthorized `param` reference, like with `qux` above.

Account Access Got Improved ([FLIP 92](https://github.com/onflow/flips/blob/main/cadence/20230525-account-type.md))

#### 💡 Motivation[​](#-motivation-13 "Direct link to 💡 Motivation")

Previously, access to accounts was granted wholesale: Users would sign a transaction, authorizing the code of the transaction to perform any kind of operation, for example, write to storage, but also add keys or contracts.

Users had to trust that a transaction would only perform supposed access, e.g. storage access to withdraw tokens, but still had to grant full access, which would allow the transaction to perform other operations.

Dapp developers who require users to sign transactions should be able to request the minimum amount of access to perform the intended operation, i.e. developers should be able to follow the principle of least privilege (PoLA).

This allows users to trust the transaction and Dapp.

#### ℹ️ Description[​](#ℹ️-description-11 "Direct link to ℹ️ Description")

Previously, access to accounts was provided through the built-in types `AuthAccount` and `PublicAccount`: `AuthAccount` provided full *write* access to an account, whereas `PublicAccount` only provided *read* access.

With the introduction of entitlements, this access is now expressed using entitlements and references, and only a single `Account` type is necessary. In addition, storage related functionality were moved to the field `Account.storage`.

Access to administrative account operations, such as writing to storage, adding keys, or adding contracts, is now gated by both coarse grained entitlements (e.g. `Storage`, which grants access to all storage related functions, and `Keys`, which grants access to all key management functions), as well as fine-grained entitlements (e.g. `SaveValue` to save a value to storage, or `AddKey` to add a new key to the account).

Transactions can now request the particular entitlements necessary to perform the operations in the transaction.

This improvement was proposed in [FLIP 92](https://github.com/onflow/flips/blob/main/cadence/20230525-account-type.md). To learn more, consult the FLIP and the documentation.

#### 🔄 Adoption[​](#-adoption-12 "Direct link to 🔄 Adoption")

Code that previously used `PublicAccount` can simply be replaced with an unauthorized account reference, `&Account.`

Code that previously used `AuthAccount` must be replaced with an authorized account reference. Depending on what functionality of the account is accessed, the appropriate entitlements have to be specified.

For example, if the `save` function of `AuthAccount` was used before, the function call must be replaced with `storage.save`, and the `SaveValue` or `Storage` entitlement is required.

#### ✨ Example[​](#-example-11 "Direct link to ✨ Example")

**Before:**

The transactions wants to save a value to storage. It must request access to the whole account, even though it does not need access beyond writing to storage.

`_10

transaction {

_10

prepare(signer: AuthAccount) {

_10

signer.save("Test", to: /storage/test)

_10

}

_10

}`

**After:**

The transaction requests the fine-grained account entitlement `SaveValue`, which allows the transaction to call the `save` function.

`_10

transaction {

_10

prepare(signer: auth(SaveValue)&Account) {

_10

signer.storage.save("Test", to: /storage/test)

_10

}

_10

}`

If the transaction attempts to perform other operations, such as adding a new key, it is rejected:

`` _10

transaction {

_10

prepare(signer: auth(SaveValue)&Account) {

_10

signer.storage.save("Test", to: /storage/test)

_10

signer.keys.add(/* ... */)

_10

// ^^^ Error: Cannot call function, requires `AddKey` or `Keys` entitlement

_10

}

_10

} ``

Deprecated Key Management API Got Removed

#### 💡 Motivation[​](#-motivation-14 "Direct link to 💡 Motivation")

Cadence provides two key management APIs:

* The original, low-level API, which worked with RLP-encoded keys
* The improved, high-level API, which works with convenient data types like `PublicKey`, `HashAlgorithm`, and `SignatureAlgorithm`
  The improved API was introduced, as the original API was difficult to use and error-prone.
  The original API was deprecated in early 2022.

#### ℹ️ Description[​](#ℹ️-description-12 "Direct link to ℹ️ Description")

The original account key management API, got removed. Instead, the improved key management API should be used.
To learn more,

#### 🔄 Adoption[​](#-adoption-13 "Direct link to 🔄 Adoption")

Replace uses of the original account key management API functions with equivalents of the improved API:

| Removed | Replacement |
| --- | --- |
| AuthAccount.addPublicKey | Account.keys.add |
| AuthAccount.removePublicKey | Account.keys.revoke |

To learn more, please refer to the [documentation](https://developers.flow.com/cadence/language/accounts#account-keys).

#### ✨ Example[​](#-example-12 "Direct link to ✨ Example")

**Before:**

`_10

transaction(encodedPublicKey: [UInt8]) {

_10

prepare(signer: AuthAccount) {

_10

signer.addPublicKey(encodedPublicKey)

_10

}

_10

}`

**After:**

`_12

transaction(publicKey: [UInt8]) {

_12

prepare(signer: auth(Keys) &Account) {

_12

signer.keys.add(

_12

publicKey: PublicKey(

_12

publicKey: publicKey,

_12

signatureAlgorithm: SignatureAlgorithm.ECDSA_P256

_12

),

_12

hashAlgorithm: HashAlgorithm.SHA3_256,

_12

weight: 100.0

_12

)

_12

}

_12

}`

Resource Tracking for Optional Bindings Improved

#### 💡 Motivation[​](#-motivation-15 "Direct link to 💡 Motivation")

Previously, resource tracking for optional bindings (”if-let statements”) was implemented incorrectly, leading to errors for valid code.
This required developers to add workarounds to their code.

#### ℹ️ Description[​](#ℹ️-description-13 "Direct link to ℹ️ Description")

Resource tracking for optional bindings (”if-let statements”) was fixed.

For example, the following program used to be invalid, reporting a resource loss error for `optR`:

`_12

resource R {}

_12

fun asOpt(_ r: @R): @R? {

_12

return <-r

_12

}

_12

_12

fun test() {

_12

let r <- create R()

_12

let optR <- asOpt(<-r)

_12

if let r2 <- optR {

_12

destroy r2

_12

}

_12

}`

This program is now considered valid.

#### 🔄 Adoption[​](#-adoption-14 "Direct link to 🔄 Adoption")

New programs do not need workarounds anymore, and can be written naturally.

Programs that previously resolved the incorrect resource loss error with a workaround, for example by invalidating the resource also in the else-branch or after the if-statement, are now invalid:

`_10

fun test() {

_10

let r <- createR()

_10

let optR <-asOpt(<-r)

_10

if let r2 <- optR {

_10

destroy r2

_10

} else {

_10

destroy optR

_10

// unnecessary, but added to avoid error

_10

}

_10

}`

The unnecessary workaround needs to be removed.

Definite Return Analysis Got Improved

#### 💡 Motivation[​](#-motivation-16 "Direct link to 💡 Motivation")

Definite return analysis determines if a function always exits, in all possible execution paths, e.g. through a `return` statement, or by calling a function that never returns, like `panic`.

This analysis was incomplete and required developers to add workarounds to their code.

#### ℹ️ Description[​](#ℹ️-description-14 "Direct link to ℹ️ Description")

The definite return analysis got significantly improved.

This means that the following program is now accepted: both branches of the if-statement exit, one using a `return` statement, the other using a function that never returns, `panic`:

`_10

resource R {}

_10

_10

fun mint(id: UInt64):@R {

_10

if id > 100 {

_10

return <- create R()

_10

} else {

_10

panic("bad id")

_10

}

_10

}`

The program above was previously rejected with a “missing return statement” error – even though we can convince ourselves that the function will exit in both branches of the if-statement, and that any code after the if-statement is unreachable, the type checker was not able to detect that – it now does.

#### 🔄 Adoption[​](#-adoption-15 "Direct link to 🔄 Adoption")

New programs do not need workarounds anymore, and can be written naturally.
Programs that previously resolved the incorrect error with a workaround, for example by adding an additional exit at the end of the function, are now invalid:

`_12

resource R {}

_12

_12

fun mint(id: UInt64):@R {

_12

if id > 100 {

_12

return <- create R()

_12

} else {

_12

panic("bad id")

_12

}

_12

_12

// unnecessary, but added to avoid error

_12

panic("unreachable")

_12

}`

The improved type checker now detects and reports the unreachable code after the if-statement as an error:

`_10

error: unreachable statement

_10

--> test.cdc:12:4

_10

|

_10

12| panic("unreachable")

_10

| ^^^^^^^^^^^^^^^^^^^^

_10

exit status 1`

To make the code valid, simply remove the unreachable code.

Semantics for Variables in For-Loop Statements Got Improved ([FLIP 13](https://github.com/onflow/flips/blob/main/cadence/20221011-for-loop-semantics.md))

#### 💡 Motivation[​](#-motivation-17 "Direct link to 💡 Motivation")

Previously, the iteration variable of `for-in` loops was re-assigned on each iteration.

Even though this is a common behavior in many programming languages, it is surprising behavior and a source of bugs.

The behavior was improved to the often assumed/expected behavior of a new iteration variable being introduced for each iteration, which reduces the likelihood for a bug.

#### ℹ️ Description[​](#ℹ️-description-15 "Direct link to ℹ️ Description")

The behavior of `for-in` loops improved, so that a new iteration variable is introduced for each iteration.

This change only affects few programs, as the behavior change is only noticeable if the program captures the iteration variable in a function value (closure).

This improvement was proposed in [FLIP 13](https://github.com/onflow/flips/blob/main/cadence/20221011-for-loop-semantics.md). To learn more, consult the FLIP and documentation.

#### ✨ Example[​](#-example-13 "Direct link to ✨ Example")

Previously, `values` would result in `[3, 3, 3]`, which might be surprising and unexpected. This is because `x` was *reassigned* the current array element on each iteration, leading to each function in `fs` returning the last element of the array.

`_14

// Capture the values of the array [1, 2, 3]

_14

let fs: [((): Int)] = []

_14

for x in [1, 2, 3] {

_14

// Create a list of functions that return the array value

_14

fs.append(fun (): Int {

_14

return x

_14

})

_14

}

_14

_14

// Evaluate each function and gather all array values

_14

let values: [Int] = []

_14

for f in fs {

_14

values.append(f())

_14

}`

References to Resource-Kinded Values Get Invalidated When the Referenced Values Are Moved ([FLIP 1043](https://github.com/onflow/flips/blob/main/cadence/20220708-resource-reference-invalidation.md))

#### 💡 Motivation[​](#-motivation-18 "Direct link to 💡 Motivation")

Previously, when a reference is taken to a resource, that reference remains valid even if the resource was moved, for example when created and moved into an account, or moved from one account into another.

In other words, references to resources stayed alive forever. This could be a potential safety foot-gun, where one could gain/give/retain unintended access to resources through references.

#### ℹ️ Description[​](#ℹ️-description-16 "Direct link to ℹ️ Description")

References are now invalidated if the referenced resource is moved after the reference was taken. The reference is invalidated upon the first move, regardless of the origin and the destination.

This feature was proposed in [FLIP 1043](https://github.com/onflow/flips/blob/main/cadence/20220708-resource-reference-invalidation.md). To learn more, please consult the FLIP and documentation.

#### ✨ Example[​](#-example-14 "Direct link to ✨ Example")

`_11

// Create a resource.

_11

let r <-createR()

_11

_11

// And take a reference.

_11

let ref = &r as &R

_11

_11

// Then move the resource into an account.

_11

account.save(<-r, to: /storage/r)

_11

_11

// Update the reference.

_11

ref.id = 2`

Old behavior:

`_10

_10

// This will also update the referenced resource in the account.

_10

ref.id = 2`

The above operation will now result in a static error.

`_10

_10

// Trying to update/access the reference will produce a static error:

_10

// "invalid reference: referenced resource may have been moved or destroyed"

_10

ref.id = 2`

However, not all scenarios can be detected statically. e.g:

`_10

fun test(ref: &R) {

_10

ref.id = 2

_10

}`

In the above function, it is not possible to determine whether the resource to which the reference was taken has been moved or not. Therefore, such cases are checked at run-time, and a run-time error will occur if the resource has been moved.

#### 🔄 Adoption[​](#-adoption-16 "Direct link to 🔄 Adoption")

Review code that uses references to resources, and check for cases where the referenced resource is moved. Such code may now be reported as invalid, or result in the program being aborted with an error when a reference to a moved resource is de-referenced.

Capability Controller API Replaced Existing Linking-based Capability API ([FLIP 798](https://github.com/onflow/flips/blob/main/cadence/20220203-capability-controllers.md))

#### 💡 Motivation[​](#-motivation-19 "Direct link to 💡 Motivation")

Cadence encourages a capability-based security model. Capabilities are themselves a new concept that most Cadence programmers need to understand.

The existing API for capabilities was centered around “links” and “linking”, and the associated concepts of the public and private storage domains, led to capabilities being even confusing and awkward to use.
An better API is easier to understand and easier to work with.

#### ℹ️ Description[​](#ℹ️-description-17 "Direct link to ℹ️ Description")

The existing linking-based capability API has been replaced by a more powerful and easier to use API based on the notion of Capability Controllers. The new API makes the creation of new and the revocation of existing capabilities simpler.

This improvement was proposed in [FLIP 798](https://github.com/onflow/flips/blob/main/cadence/20220203-capability-controllers.md). To learn more, consult the FLIP and the documentation.

#### 🔄 Adoption[​](#-adoption-17 "Direct link to 🔄 Adoption")

Existing uses of the linking-based capability API must be replaced with the new Capability Controller API.

| Removed | Replacement |
| --- | --- |
| `AuthAccount.link`, with private path | `Account.capabilities.storage.issue` |
| `AuthAccount.link`, with public path | `Account.capabilities.storage.issue` and `Account.capabilities.publish` |
| `AuthAccount.linkAccount` | `AuthAccount.capabilities.account.issue` |
| `AuthAccount.unlink`, with private path | - Get capability controller: `Account.capabilities.storage/account.get`   - Revoke controller: `Storage/AccountCapabilityController.delete` |
| `AuthAccount.unlink`, with public path | - Get capability controller: `Account.capabilities.storage/account.get`   - Revoke controller: `Storage/AccountCapabilityController.delete`   - Unpublish capability: `Account.capabilities.unpublish` |
| `AuthAccount/PublicAccount.getCapability` | `Account.capabilities.get` |
| `AuthAccount/PublicAccount.getCapability` with followed borrow | `Account.capabilities.borrow` |
| `AuthAccount.getLinkTarget` | N/A |

#### ✨ Example[​](#-example-15 "Direct link to ✨ Example")

Assume there is a `Counter` resource which stores a count, and it implements an interface `HasCount` which is used to allow read access to the count.

`_15

access(all)

_15

resource interface HasCount {

_15

access(all)

_15

count: Int

_15

}

_15

_15

access(all)

_15

resource Counter: HasCount {

_15

access(all)

_15

var count: Int

_15

_15

init(count: Int) {

_15

self.count = count

_15

}

_15

}`

Granting access, before:

`_12

transaction {

_12

prepare(signer: AuthAccount) {

_12

signer.save(

_12

<-create Counter(count: 42),

_12

to: /storage/counter

_12

)

_12

signer.link<&{HasCount}>(

_12

/public/hasCount,

_12

target: /storage/counter

_12

)

_12

}

_12

}`

Granting access, after:

`_12

transaction {

_12

prepare(signer: auth(Storage, Capabilities)&Account) {

_12

signer.save(

_12

<-create Counter(count: 42),

_12

to: /storage/counter

_12

)

_12

let cap = signer.capabilities.storage.issue<&{HasCount}>(

_12

/storage/counter

_12

)

_12

signer.capabilities.publish(cap, at: /public/hasCount)

_12

}

_12

}`

Getting access, before:

`_10

access(all)

_10

fun main(): Int {

_10

let counterRef = getAccount(0x1)

_10

.getCapabilities<&{HasCount}>(/public/hasCount)

_10

.borrow()!

_10

return counterRef.count

_10

}`

Getting access, after:

`_10

access(all)

_10

fun main(): Int {

_10

let counterRef = getAccount(0x1)

_10

.capabilities

_10

.borrow<&{HasCount}>(/public/hasCount)!

_10

return counterRef.count

_10

}`

External Mutation Improvement ([FLIP 89](https://github.com/onflow/flips/blob/main/cadence/20230517-member-access-semnatics.md) & [FLIP 86](https://github.com/onflow/flips/blob/main/cadence/20230519-built-in-mutability-entitlements.md))

#### 💡 Motivation[​](#-motivation-20 "Direct link to 💡 Motivation")

A previous version of Cadence (“Secure Cadence”), attempted to prevent a common safety foot-gun: Developers might use the `let` keyword for a container-typed field, assuming it would be immutable.

Though Secure Cadence implements the [Cadence mutability restrictions FLIP](https://github.com/onflow/flips/blob/main/cadence/20211129-cadence-mutability-restrictions.md), it did not fully solve the problem / prevent the foot-gun and there were still ways to mutate such fields, so a proper solution was devised.

To learn more about the problem and motivation to solve it, please read the associated [Vision](https://github.com/onflow/flips/blob/main/cadence/vision/mutability-restrictions.md) document.

#### ℹ️ Description[​](#ℹ️-description-18 "Direct link to ℹ️ Description")

The mutability of containers (updating a field of a composite value, key of a map, or index of an array) through references has changed:
When a field/element is accessed through a reference, a reference to the accessed inner object is returned, instead of the actual object. These returned references are unauthorized by default, and the author of the object (struct/resource/etc.) can control what operations are permitted on these returned references by using entitlements and entitlement mappings.
This improvement was proposed in two FLIPs:

* [FLIP 89: Change Member Access Semantics](https://github.com/onflow/flips/blob/main/cadence/20230517-member-access-semnatics.md)
* [FLIP 86: Introduce Built-in Mutability Entitlements 1](https://github.com/onflow/flips/blob/main/cadence/20230519-built-in-mutability-entitlements.md)

To learn more, please consult the FLIPs and the documentation.

#### 🔄 Adoption[​](#-adoption-18 "Direct link to 🔄 Adoption")

As mentioned in the previous section, the most notable change in this improvement is that, when a field/element is accessed through a reference, a reference to the accessed inner object is returned, instead of the actual object. So developers would need to change their code to:

* Work with references, instead of the actual object, when accessing nested objects through a reference.
* Use proper entitlements for fields when they declare their own `struct` and `resource` types.

  

#### ✨ Example[​](#-example-16 "Direct link to ✨ Example")

Consider the below resource collection:

`_15

pub resource MasterCollection {

_15

pub let kittyCollection: @Collection

_15

pub let topshotCollection: @Collection

_15

}

_15

_15

pub resource Collection {

_15

pub(set)

_15

var id: String

_15

_15

access(all)

_15

var ownedNFTs: @{UInt64: NonFungibleToken.NFT}

_15

_15

access(all)

_15

fun deposit(token:@NonFungibleToken.NFT) {... }

_15

}`

Earlier, it was possible to mutate the inner collections, even if someone only had a reference to the `MasterCollection`. e.g:

`_10

var masterCollectionRef:&MasterCollection =... // Directly updating the field

_10

masterCollectionRef.kittyCollection.id = "NewID"

_10

_10

// Calling a mutating function

_10

masterCollectionRef.kittyCollection.deposit(<-nft)

_10

_10

// Updating via the referencelet ownedNFTsRef=&masterCollectionRef.kittyCollection.ownedNFTs as &{UInt64: NonFungibleToken.NFT}

_10

destroy ownedNFTsRef.insert(key: 1234, <-nft)`

Once this change is introduced, the above collection can be re-written as below:

`` _36

pub resource MasterCollection {

_36

access(KittyCollectorMapping)

_36

let kittyCollection: @Collection

_36

_36

access(TopshotCollectorMapping)

_36

let topshotCollection: @Collection

_36

}

_36

_36

pub resource Collection {

_36

pub(set)

_36

var id: String

_36

_36

access(Identity)

_36

var ownedNFTs: @{UInt64: NonFungibleToken.NFT}

_36

_36

access(Insert)

_36

fun deposit(token:@NonFungibleToken.NFT) { /* ... */ }

_36

}

_36

_36

// Entitlements and mappings for `kittyCollection`

_36

_36

entitlement KittyCollector

_36

_36

entitlement mapping KittyCollectorMapping {

_36

KittyCollector -> Insert

_36

KittyCollector -> Remove

_36

}

_36

_36

// Entitlements and mappings for `topshotCollection`

_36

_36

entitlement TopshotCollector

_36

_36

entitlement mapping TopshotCollectorMapping {

_36

TopshotCollector -> Insert

_36

TopshotCollector -> Remove

_36

} ``

Then for a reference with no entitlements, none of the previously mentioned operations would be allowed:

`` _13

var masterCollectionRef:&MasterCollection <- ... // Error: Cannot update the field. Doesn't have sufficient entitlements.

_13

masterCollectionRef.kittyCollection.id = "NewID"

_13

_13

// Error: Cannot directly update the dictionary. Doesn't have sufficient entitlements.

_13

destroy masterCollectionRef.kittyCollection.ownedNFTs.insert(key: 1234,<-nft)

_13

destroy masterCollectionRef.ownedNFTs.remove(key: 1234)

_13

_13

// Error: Cannot call mutating function. Doesn't have sufficient entitlements.

_13

masterCollectionRef.kittyCollection.deposit(<-nft)

_13

_13

// Error: `masterCollectionRef.kittyCollection.ownedNFTs` is already a non-auth reference.// Thus cannot update the dictionary. Doesn't have sufficient entitlements.

_13

let ownedNFTsRef = &masterCollectionRef.kittyCollection.ownedNFTsas&{UInt64: NonFungibleToken.NFT}

_13

destroy ownedNFTsRef.insert(key: 1234, <-nft) ``

To perform these operations on the reference, one would need to have obtained a reference with proper entitlements:

`_10

var masterCollectionRef: auth{KittyCollector} &MasterCollection <- ... // Directly updating the field

_10

masterCollectionRef.kittyCollection.id = "NewID"

_10

_10

// Updating the dictionary

_10

destroy masterCollectionRef.kittyCollection.ownedNFTs.insert(key: 1234, <-nft)

_10

destroy masterCollectionRef.kittyCollection.ownedNFTs.remove(key: 1234)

_10

_10

// Calling a mutating function

_10

masterCollectionRef.kittyCollection.deposit(<-nft)`

Removal Of Nested Type Requirements ([FLIP 118](https://github.com/onflow/flips/blob/main/cadence/20230711-remove-type-requirements.md))

#### 💡 Motivation[​](#-motivation-21 "Direct link to 💡 Motivation")

[Nested Type Requirements 3](https://docs.onflow.org/cadence/language/interfaces/#nested-type-requirements) were a fairly advanced concept of the language.

Just like an interface could require a conforming type to provide a certain field or function, it could also have required the conforming type to provide a nested type.

This is an uncommon feature in other programming languages and hard to understand.

In addition, the value of nested type requirements was never realized. While it was previously used in the FT and NFT contracts, the addition of other language features like interface inheritance and events being emittable from interfaces, there were no more uses case compelling enough to justify a feature of this complexity.

#### ℹ️ Description[​](#ℹ️-description-19 "Direct link to ℹ️ Description")

Contract interfaces can no longer declare any concrete types (`struct`, `resource` or `enum`) in their declarations, as this would create a type requirement. `event` declarations are still allowed, but these create an `event` type limited to the scope of that contract interface; this `event` is not inherited by any implementing contracts. Nested interface declarations are still permitted, however.

This improvement was proposed in [FLIP 118](https://github.com/onflow/flips/blob/main/cadence/20230711-remove-type-requirements.md).

#### 🔄 Adoption[​](#-adoption-19 "Direct link to 🔄 Adoption")

Any existing code that made use of the type requirements feature should be rewritten not to use this feature.

Event Definition And Emission In Interfaces ([FLIP 111](https://github.com/onflow/flips/blob/main/cadence/20230417-events-emitted-from-interfaces.md))

#### 💡 Motivation[​](#-motivation-22 "Direct link to 💡 Motivation")

In order to support the removal of nested type requirements, events have been made define-able and emit-able from contract interfaces, as events were among the only common uses of the type requirements feature.

#### ℹ️ Description[​](#ℹ️-description-20 "Direct link to ℹ️ Description")

Contract interfaces may now define event types, and these events can be emitted from function conditions and default implementations in those contract interfaces.

This improvement was proposed in [FLIP 111](https://github.com/onflow/flips/blob/main/cadence/20230417-events-emitted-from-interfaces.md).

#### 🔄 Adoption[​](#-adoption-20 "Direct link to 🔄 Adoption")

Contract interfaces that previously used type requirements to enforce that concrete contracts which implement the interface should also declare a specific event, should instead define and emit that event in the interface.

#### ✨ Example[​](#-example-17 "Direct link to ✨ Example")

**Before:**

A contract interface like the one below (`SomeInterface`) used a type requirement to enforce that contracts which implement the interface also define a certain event (`Foo`):

`_16

contract interface SomeInterface {

_16

event Foo()

_16

//^^^^^^^^^^^ type requirement

_16

_16

fun inheritedFunction()

_16

}

_16

_16

contract MyContract: SomeInterface {

_16

event Foo()

_16

//^^^^^^^^^^^ type definition to satisfy type requirement

_16

_16

fun inheritedFunction() {

_16

// ...

_16

emit Foo()

_16

}

_16

}`

**After:**

This can be rewritten to emit the event directly from the interface, so that any contracts that implement `Intf` will always emit `Foo` when `inheritedFunction` is called:

`_10

contract interface Intf {

_10

event Foo()

_10

//^^^^^^^^^^^ type definition

_10

_10

fun inheritedFunction() {

_10

pre {

_10

emit Foo()

_10

}

_10

}

_10

}`

Force Destruction of Resources ([FLIP 131](https://github.com/onflow/flips/pull/131))

#### 💡 Motivation[​](#-motivation-23 "Direct link to 💡 Motivation")

It was previously possible to panic in the body of a resource or attachment’s `destroy` method, effectively preventing the destruction or removal of that resource from an account. This could be used as an attack vector by handing people undesirable resources or hydrating resources to make them extremely large or otherwise contain undesirable content.

#### ℹ️ Description[​](#ℹ️-description-21 "Direct link to ℹ️ Description")

Contracts may no longer define `destroy` functions on their resources, and are no longer required to explicitly handle the destruction of resource fields. These will instead be implicitly destroyed whenever a resource is destroyed.
Additionally, developers may define a `ResourceDestroyed` event in the body of a resource definition using default arguments, which will be lazily evaluated and then emitted whenever a resource of that type is destroyed.
This improvement was proposed in [FLIP 131](https://github.com/onflow/flips/pull/131).

#### 🔄 Adoption[​](#-adoption-21 "Direct link to 🔄 Adoption")

Contracts that previously used destroy methods will need to remove them, and potentially define a ResourceDestroyed event to track destruction if necessary.

#### ✨ Example[​](#-example-18 "Direct link to ✨ Example")

A pair of resources previously written as:

`_24

event E(id: Int)

_24

_24

resource SubResource {

_24

let id: Int

_24

init(id: Int) {

_24

self.id = id

_24

}

_24

_24

destroy() {

_24

emit E(id: self.id)

_24

}

_24

}

_24

_24

resource R {

_24

let subR: @SubResource

_24

_24

init(id: Int) {

_24

self.subR <- create SubResource(id: id)

_24

}

_24

_24

destroy() {

_24

destroy self.subR

_24

}

_24

}`

can now be equivalently written as:

`_16

resource SubResource {

_16

event ResourceDestroyed(id: Int = self.id)

_16

let id: Int

_16

_16

init(id: Int) {

_16

self.id = id

_16

}

_16

}

_16

_16

resource R {

_16

let subR: @SubResource

_16

_16

init(id: Int) {

_16

self.subR <- create SubResource(id: id)

_16

}

_16

}`

New `domainSeparationTag` parameter added to `Crypto.KeyList.verify`

#### 💡 Motivation[​](#-motivation-24 "Direct link to 💡 Motivation")

`KeyList`’s `verify` function used to hardcode the domain separation tag (`"FLOW-V0.0-user"`) used to verify each signature from the list. This forced users to use the same domain tag and didn’t allow them to scope their signatures to specific use-cases and applications. Moreover, the `verify` function didn’t mirror the `PublicKey` signature verification behaviour which accepts a domain tag parameter.

#### ℹ️ Description[​](#ℹ️-description-22 "Direct link to ℹ️ Description")

`KeyList`’s `verify` function requires an extra parameter to specify the domain separation tag used to verify the input signatures. The tag is is a single `string` parameter and is used with all signatures. This mirrors the behaviour of the simple public key [signature verification](https://cadence-lang.org/docs/1.0/language/crypto#signature-verification).

#### 🔄 Adoption[​](#-adoption-22 "Direct link to 🔄 Adoption")

Contracts that use `KeyList` need to update the calls to `verify` by adding the new domain separation tag parameter. Using the tag as `"FLOW-V0.0-user"` would keep the exact same behaviour as before the breaking change. Applications may also define a new domain tag for their specific use-case and use it when generating valid signatures, for added security against signature replays. Check the [signature verification doc](https://cadence-lang.org/docs/1.0/language/crypto#signature-verification) and specifically [hashing with a tag](https://cadence-lang.org/docs/1.0/language/crypto#hashing-with-a-domain-tag) for details on how to generate valid signatures with a tag.

#### ✨ Example[​](#-example-19 "Direct link to ✨ Example")

A previous call to `KeyList`’s `verify` is written as:

`_10

let isValid = keyList.verify(

_10

signatureSet: signatureSet,

_10

signedData: signedData

_10

)`

can now be equivalently written as:

`_10

let isValid = keyList.verify(

_10

signatureSet: signatureSet,

_10

signedData: signedData,

_10

domainSeparationTag: "FLOW-V0.0-user"

_10

)`

Instead of the existing hardcoded domain separation tag, a new domain tag can be defined, but it has to be also used when generating valid signatures, e.g. `"my_app_custom_domain_tag"`.

## FT / NFT Standard changes[​](#ft--nft-standard-changes "Direct link to FT / NFT Standard changes")

In addition to the upcoming language changes, the Cadence 1.0 upgrade also includes breaking changes to core contracts - such as the FungibleToken and NonFungibleToken standards. All Fungible & Non-Fungible Token contracts will need to be updated to the new standard.

These interfaces are being upgraded to allow for multiple tokens per contract, fix some issues with the original standards, and introduce other various improvements suggested by the community.

* Original Proposal: <http://forum.flow.com/t/streamlined-token-standards-proposal/3075>
* Fungible Token Changes PR: [WIP: V2 FungibleToken Standard by joshuahannan · Pull Request #77 · onflow/flow-ft · GitHub 5](https://github.com/onflow/flow-ft/pull/77)
* NFT Changes PR: [https://github.com/onflow/flow-nft/pull/126 8](https://github.com/onflow/flow-nft/pull/126)

It will involve upgrading your token contracts with changes to events, function signatures, resource interface conformances, and other small changes.

There are some existing guides for upgrading your token contracts to the new standard:

* [Upgrading Fungible Token Contracts](/docs/cadence-migration-guide/ft-guide)
* [Upgrading Non-Fungible Token Contracts](/docs/cadence-migration-guide/nft-guide)

## More Resources[​](#more-resources "Direct link to More Resources")

If you have any questions or need help with the upgrade, feel free to reach out to the Flow team on the [Flow Discord](https://discord.gg/flowblockchain).

Help is also available during the [Cadence 1.0 Office Hours](https://calendar.google.com/calendar/ical/c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0%40group.calendar.google.com/public/basic.ics) each week at 10:00am PST on the Flow Developer Discord.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/cadence-migration-guide/improvements.md)

[Previous

Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)[Next

NFT Cadence 1.0 Guide](/docs/cadence-migration-guide/nft-guide)

###### Rate this page

😞😐😊

* [💫 New features](#-new-features)
* [⚡ Breaking Improvements](#-breaking-improvements)
* [FT / NFT Standard changes](#ft--nft-standard-changes)
* [More Resources](#more-resources)