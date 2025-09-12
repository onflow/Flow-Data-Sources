# Source: https://cadence-lang.org/docs/language/syntax

Syntax and Glossary | Cadence



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
* Syntax and Glossary

On this page

# Syntax and Glossary

This comprehensive glossary provides detailed explanations and code examples for the most important syntax, symbols, operators, keywords, functions, and concepts in Cadence. Each entry includes a clear description of the feature's purpose, usage patterns, and common scenarios, helping both new and experienced developers quickly understand Cadence's unique resource-oriented programming model.

Use this guide as a complete reference to navigate Cadence's syntax, resource management, access control, and blockchain-specific features.

## Comments[​](#comments "Direct link to Comments")

Comments can be used to document code. A comment is text that is not executed.

*Single-line comments* start with two slashes (`//`). These comments can go on a line by themselves, or they can go directly after a line of code:

`_10

// This is a comment on a single line.

_10

// Another comment line that is not executed.

_10

_10

let x = 1 // Here is another comment after a line of code.`

*Multi-line comments* start with a slash and an asterisk (`/*`) and end with an asterisk and a slash (`*/`):

`_10

/* This is a comment which

_10

spans multiple lines. */`

Comments may be nested:

`_10

/* /* this */ is a valid comment */`

Multi-line comments are balanced:

`_10

/* this is a // comment up to here */ this is not part of the comment */`

### Documentation comments[​](#documentation-comments "Direct link to Documentation comments")

Documentation comments (also known as *doc-strings* or *doc-comment*) are a special set of comments that can be processed by tools (e.g., to generate human-readable documentation or provide documentation in an IDE).

Doc-comments either start with three slashes (`///`) on each line or are surrounded by `/**` and `**/`:

`` _10

/// This is a documentation comment for `x`.

_10

/// It spans multiple lines.

_10

_10

let x = 1 ``

`_10

/**

_10

This is a documentation comment

_10

which also spans multiple lines.

_10

**/`

## Identifiers[​](#identifiers "Direct link to Identifiers")

Identifiers can start with any upper or lowercase letter (A-Z, a-z) or an underscore (`_`). This may be followed by zero or more upper and lower case letters, underscores, and numbers (0-9). Identifiers can **not** begin with a number:

`_29

// Valid: title-case

_29

//

_29

PersonID

_29

_29

// Valid: with underscore

_29

//

_29

token_name

_29

_29

// Valid: leading underscore and characters

_29

//

_29

_balance

_29

_29

// Valid: leading underscore and numbers

_29

_8264

_29

_29

// Valid: characters and number

_29

//

_29

account2

_29

_29

// Invalid: leading number

_29

//

_29

1something

_29

_29

// Invalid: invalid character #

_29

_#1

_29

_29

// Invalid: various invalid characters

_29

//

_29

!@#$%^&*`

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
* `contract`, `event`, `struct`, `resource`, `interface`, `entitlement`, `enum`, `mapping`, `attachment`, `result`
* `transaction`, `prepare`, `execute`
* `switch`, `case`, `default`
* `import`, `include`
* `require`, `requires`, `static`, `native`, `pub`, `priv`, `try`, `catch`, `finally`, `goto`, `const`, `export`, `throw`, `throws`, `where`, `final`, `internal`, `typealias`, `repeat`, `guard`, `is`

### Conventions[​](#conventions "Direct link to Conventions")

By convention, variables, constants, and functions have lowercase identifiers, and types have title-case identifiers.

## Symbols and operators[​](#symbols-and-operators "Direct link to Symbols and operators")

### `&` (ampersand)[​](#-ampersand "Direct link to -ampersand")

The `&` (ampersand) symbol creates [references](/docs/language/references) to values in Cadence, allowing you to access data without moving it. When used at the beginning of an expression, it creates a reference to a value, which can be either authorized (with the `auth` modifier) or unauthorized. Authorized references include entitlements that specify what operations can be performed on the referenced value, while unauthorized references provide read-only access. The ampersand is also used in [logical AND operations](/docs/language/operators/arithmetic-logical-operators#logical-operators) when doubled (`&&`), allowing boolean expressions to be combined with short-circuit evaluation.

`_10

let a: String = "hello"

_10

let refOfA: &String = &a as &String

_10

let authRef: auth(X) &String = &a as auth(X) &String

_10

let result = true && false // logical AND`

### `@` (at symbol)[​](#-at-symbol "Direct link to -at-symbol")

The `@` (at) symbol is a crucial resource type annotation in Cadence that indicates a type is a [resource](/docs/language/resources) rather than a regular value. Resources in Cadence are unique, non-copyable types that must be explicitly moved between variables, functions, and storage locations. The `@` symbol must appear at the beginning of the type declaration, emphasizing that the entire type acts as a resource. This annotation is required for resource instantiation, function parameters, return types, and variable declarations involving resources.

`_10

resource NFT {

_10

access(all) var id: UInt64

_10

access(all) var metadata: String

_10

}

_10

_10

let myNFT: @NFT <- create NFT(id: 1, metadata: "Rare item")

_10

fun transfer(nft: @NFT) { /* resource handling */ }`

### `:` (colon)[​](#-colon "Direct link to -colon")

The `:` (colon) symbol serves multiple purposes in Cadence syntax. It's primarily used for type annotations, allowing you to explicitly declare the type of variables, constants, function parameters, and return types. The colon also appears in [ternary conditional operators](/docs/language/operators/bitwise-ternary-operators#ternary-conditional-operator) to separate the *then* and *else* branches, providing a concise way to write conditional expressions. Additionally, colons are used in access modifiers and entitlement declarations to specify access control and authorization requirements.

`_10

let value: Int = 42 // type annotation

_10

fun calculate(x: Int, y: Int): Int { return x + y } // parameter and return types

_10

let result = condition ? value1 : value2 // ternary operator`

### `=` (equals)[​](#-equals "Direct link to -equals")

The `=` (equals) symbol is the assignment operator in Cadence, used to assign values to variables and constants. For regular values (non-resources), the equals sign performs a copy assignment, creating a new copy of the value. For resources, the equals sign cannot be used directly; instead, the move operator `<-` must be used to explicitly transfer ownership. The equals sign is also used in constant declarations with `let` and variable declarations with `var`, and it appears in comparison operations when doubled (`==`) for equality testing.

`_10

let constant = 5 // constant declaration

_10

var mutable = 10 // variable declaration

_10

mutable = 15 // assignment

_10

let isEqual = a == b // equality comparison`

### `!` (exclamation mark)[​](#-exclamation-mark "Direct link to -exclamation-mark")

The `!` (exclamation mark) symbol has two distinct uses depending on its position relative to a value. When placed before a boolean expression, it performs logical negation, inverting the truth value of the expression. When placed after an optional value, it performs [force unwrapping](/docs/language/operators/optional-operators#force-unwrap-operator-), extracting the contained value from the optional or causing a runtime panic if the optional is nil. Force unwrapping should be used carefully as it can cause program termination, and safer alternatives like nil-coalescing (`??`) or optional binding should be preferred when possible.

`_10

let isTrue = true

_10

let isFalse = !isTrue // logical negation

_10

let optionalValue: Int? = 42

_10

let unwrapped = optionalValue! // force unwrap (dangerous if nil)`

### `/` (forward slash)[​](#-forward-slash "Direct link to -forward-slash")

The `/` (forward slash) symbol serves as both a mathematical [division operator](/docs/language/operators/arithmetic-logical-operators#arithmetic-operators) and a path separator in Cadence. In arithmetic expressions, it performs division between numeric values, returning the quotient. In [path](/docs/language/accounts/paths) expressions, it separates the components of storage paths, which are used to access data in account storage. Paths follow the format `/domain/identifier` where domain can be `storage` or `public`, and the identifier specifies the specific storage location or capability.

`_10

let quotient = 10 / 2 // arithmetic division

_10

let storagePath = /storage/myResource // storage path

_10

let publicPath = /public/myCapability // public path`

### `<-` (move operator)[​](#--move-operator "Direct link to --move-operator")

The [`<-` (move operator)](/docs/language/resources#the-move-operator--) is essential for resource management in Cadence, explicitly indicating when a [resource](/docs/language/resources) is being transferred from one location to another. Unlike regular values that are copied, resources must be moved using this operator to maintain their uniqueness and prevent accidental duplication. The move operator is required when creating resources, assigning them to variables, passing them as function arguments, returning them from functions, or storing them in account storage. This explicit movement ensures that resources follow Cadence's linear type system and prevents resource leaks or double-spending scenarios.

`_10

resource Token {

_10

access(all) var amount: UInt64

_10

}

_10

_10

let token <- create Token(amount: 100) // resource creation

_10

let newOwner <- token // resource transfer

_10

fun mint(): @Token { return <- create Token(amount: 50) } // resource return`

### `<-!` (force-assignment move operator)[​](#--force-assignment-move-operator "Direct link to --force-assignment-move-operator")

The [`<-!` (force-assignment move operator)](/docs/language/operators/assign-move-force-swap#force-assignment-operator--) is a specialized move operator that moves a resource into an optional variable, but only if the variable is currently nil. If the target variable already contains a resource, the operation will abort the program execution. This operator is useful for ensuring that optional resource variables are only assigned once, providing a safety mechanism against accidental overwrites. It's commonly used in initialization patterns where you want to guarantee that a resource is only moved into an empty optional container.

`_10

resource NFT {

_10

access(all) var id: UInt64

_10

}

_10

_10

var myNFT: @NFT? <- nil

_10

myNFT <-! create NFT(id: 1) // succeeds because myNFT is nil

_10

// myNFT <-! create NFT(id: 2) // would abort because myNFT is not nil`

### `<->` (swap operator)[​](#--swap-operator "Direct link to --swap-operator")

The [`<->` (swap operator)](/docs/language/operators/assign-move-force-swap#swapping-operator--) exchanges two resources between variables without requiring a temporary variable. This operator is particularly useful for resource management scenarios where you need to swap ownership of two resources atomically. The swap operation is guaranteed to be atomic and cannot fail, making it ideal for scenarios where you need to exchange resources in a single operation. This operator is commonly used in trading scenarios, resource reallocation, or any situation where two parties need to exchange resources simultaneously.

`_10

resource Coin {

_10

access(all) var value: UInt64

_10

}

_10

_10

let coinA: @Coin <- create Coin(value: 10)

_10

let coinB: @Coin <- create Coin(value: 20)

_10

coinA <-> coinB // now coinA has value 20, coinB has value 10`

### `+`, `-`, `*`, `%` (arithmetic operators)[​](#-----arithmetic-operators "Direct link to -----arithmetic-operators")

The [arithmetic operators](/docs/language/operators/arithmetic-logical-operators#arithmetic-operators) `+`, `-`, `*`, and `%` perform standard mathematical operations on numeric types in Cadence. The plus operator (`+`) adds two values, the minus operator (`-`) subtracts the right operand from the left, the asterisk operator (`*`) multiplies two values, and the percentage sign (`%`) returns the remainder of division. These operators work with all numeric types including `Int`, `UInt`, `Int8`, `UInt8`, and so on, and follow standard operator precedence rules. Cadence also supports compound assignment operators like `+=`, `-=`, `*=`, and `%=` for more concise code. Cadence does not support the increment/decrement operators `++`, `--`.

`_10

let sum = 5 + 3 // addition

_10

let difference = 10 - 4 // subtraction

_10

let product = 6 * 7 // multiplication

_10

let remainder = 17 % 5 // modulo

_10

var value = 10

_10

value += 5 // compound assignment`

### `?` (question mark)[​](#-question-mark "Direct link to -question-mark")

The `?` (question mark) symbol has multiple uses in Cadence, primarily for optional types and conditional operations. When following a type, it creates an optional type that can either contain a value or be nil, providing a safe way to handle potentially missing values. In [ternary conditional expressions](/docs/language/operators/bitwise-ternary-operators#ternary-conditional-operator), the question mark separates the condition from the *then* branch. The question mark is also used in the [nil-coalescing operator (`??`)](/docs/language/operators/optional-operators#nil-coalescing-operator-) to provide a default value when an optional is nil, and in optional chaining to safely access properties or call methods on optional values.

`_10

let optionalInt: Int? = nil // optional type

_10

let result = condition ? value1 : value2 // ternary operator

_10

let safeValue = optionalInt ?? 0 // nil-coalescing

_10

let length = optionalString?.length // optional chaining`

### `_` (underscore)[​](#_-underscore "Direct link to _-underscore")

The `_` (underscore) symbol serves multiple purposes in Cadence syntax. It can be used in identifiers and variable names to improve readability, particularly for separating words in compound names. In numeric literals, underscores can be used as separators to make large numbers more readable without affecting their value. When used as an argument label in [function](/docs/language/functions) declarations, the underscore indicates that no argument label is required when calling the function, allowing for more natural function calls. The underscore is also used in pattern matching to ignore specific values or in unused variable declarations.

`_10

let user_name = "Alice" // identifier separator

_10

let large_number = 1_000_000 // numeric separator

_10

fun double(_ x: Int): Int { return x * 2 } // no argument label

_10

let result = double(5) // no label needed`

### `;` (semicolon)[​](#-semicolon "Direct link to -semicolon")

The `;` (semicolon) symbol is used as a separator between declarations and statements. A semicolon can be placed after any declaration and statement, but can be omitted between declarations if only one statement appears on the line.

`_11

// Declare a constant, without a semicolon.

_11

//

_11

let a = 1

_11

_11

// Declare a variable, with a semicolon.

_11

//

_11

var b = 2;

_11

_11

// Declare a constant and a variable on a single line, separated by semicolons.

_11

//

_11

let d = 1; var e = 2`

## Punctuation marks[​](#punctuation-marks "Direct link to Punctuation marks")

### `.` (dot/period)[​](#-dotperiod "Direct link to -dotperiod")

The `.` (dot) symbol serves multiple purposes in Cadence syntax. It's primarily used for member access, allowing you to access properties, methods, and nested types of objects and types. The dot operator is used to call functions on objects, access struct and resource fields, and navigate through nested structures. Dots are also used in decimal numbers to separate the integer and fractional parts, and in qualified type names to specify the namespace or module where a type is defined.

`_10

let length = "hello".length // member access

_10

let balance = token.balance // property access

_10

token.transfer(amount: 10) // method call

_10

let decimal = 3.14 // decimal number

_10

let nft: MyContract.NFT // qualified type name`

### `,` (comma)[​](#-comma "Direct link to -comma")

The `,` (comma) symbol is used to separate multiple items in lists, function parameters, type parameters, and other multi-item contexts in Cadence. Commas separate function arguments, array elements, dictionary key-value pairs, and type parameters in generic declarations. They're also used to separate multiple variable declarations in a single statement and to separate multiple return values in tuple types. Proper comma usage is essential for clear, readable code structure.

`_10

fun add(a: Int, b: Int, c: Int): Int { return a + b + c } // function parameters

_10

let array = [1, 2, 3, 4, 5] // array elements

_10

let dict = {"key1": "value1", "key2": "value2"} // dictionary pairs

_10

let a, b, c = 1, 2, 3 // multiple declarations

_10

let tuple: (Int, String, Bool) // tuple type`

### `()` (parentheses)[​](#-parentheses "Direct link to -parentheses")

The `()` (parentheses) symbol has multiple uses in Cadence syntax. They're used to group expressions and control operator precedence in mathematical and logical expressions. Parentheses are required around function parameters in function calls. They also serve to group conditions in control flow statements and to create type annotations for function types. Parentheses are essential for disambiguating complex expressions and ensuring proper evaluation order.

`_10

let result = (a + b) * c // expression grouping

_10

fun calculate(x: Int, y: Int): Int { return x + y } // function parameters

_10

let functionType: (Int, Int) -> Int // function type

_10

if (condition1 && condition2) { /* code */ } // grouped condition`

### `<>` (angle brackets)[​](#-angle-brackets "Direct link to -angle-brackets")

Angle brackets (`<>`) are *not* used for generics like in many other languages — Cadence doesn't have traditional generic functions or structs — but they *are* used in a few specific syntactic contexts related to type parameters and type instantiation. Specifically, angle brackets are used to specify type parameters for certain built-in or standard library types that are type constructors. Angle brackets are also used to specify the borrow type when working with capabilities and when specifying the authorized type with some Cadence APIs. You can also use angle brackets to define explicit element types for collections.

`_26

// FungibleToken.Vault is a generic composite type in the standard interface.

_26

// <ExampleToken.Vault> tells Cadence the concrete vault type to use:

_26

_26

let vault: FungibleToken.Vault<ExampleToken.Vault>

_26

_26

// The Capability<...> is a generic capability type:

_26

let cap: Capability<&ExampleToken.Vault{FungibleToken.Receiver}>

_26

_26

// Inside <...>, you define the type that will be borrowed when

_26

// using the capability. For example:

_26

let receiverCap: Capability<&ExampleToken.Vault{FungibleToken.Receiver}>

_26

= account.getCapability<&ExampleToken.Vault{FungibleToken.Receiver}>(/public/receiver)

_26

_26

// No < > = Cadence infers; With < > = you're explicitly

_26

// telling it the type:

_26

let vaultRef = account

_26

.getCapability<&ExampleToken.Vault{FungibleToken.Receiver}>(/public/receiver)

_26

.borrow()

_26

let numbers: [Int] = []

_26

let moreNumbers = [] as [Int]

_26

_26

// The type annotation uses square brackets for collections,

_26

// but when inside other parameterized types, < > is used:

_26

let dict: {String: Int} = {}

_26

let capDict: {String: Capability<&ExampleToken.Vault>} = {}

_26

// Here, the < > is within Capability<...> inside the dictionary value type.`

### `{}` (curly brackets)[​](#-curly-brackets "Direct link to -curly-brackets")

The `{}` (curly brackets) symbol is used to define code blocks, scopes, and composite data structures in Cadence. They're used to group statements in functions, control flow statements, and resource/struct definitions. Curly brackets are also used to create dictionary literals and to define the body of functions, initializers, and methods. They establish the scope for variable declarations and control the lifetime of local variables and borrowed references.

`_15

fun example() {

_15

let localVar = 42 // code block

_15

if condition {

_15

// nested block

_15

}

_15

}

_15

_15

resource NFT {

_15

access(all) var id: UInt64 // resource definition

_15

init(id: UInt64) {

_15

self.id = id // initializer block

_15

}

_15

}

_15

_15

let dict = {"key": "value"} // dictionary literal`

### `[]` (square brackets)[​](#-square-brackets "Direct link to -square-brackets")

The `[]` (square brackets) symbol is used for array operations and type annotations in Cadence. They're used to create array literals, access array elements by index, and specify array types in type annotations. Square brackets are also used in dictionary key access and to specify the size of fixed-size arrays. They're essential for working with collections and implementing array-based data structures and algorithms.

`_10

let array = [1, 2, 3, 4, 5] // array literal

_10

let firstElement = array[0] // array access

_10

let arrayType: [String] // array type annotation

_10

let fixedArray: [Int; 5] // fixed-size array

_10

let dict = {"key": "value"}

_10

let value = dict["key"] // dictionary access`

### `` ` `` (backtick)[​](#-backtick "Direct link to -backtick")

The `` ` `` (backtick) symbol is *not* used and has no syntactic meaning at all in Cadence syntax.

When working with string declarations, use double quotes (`" "`) instead:

`` _10

let s = `hello` // Error: use double quotes for strings

_10

let s = "hello" ``

### Whitespace[​](#whitespace "Direct link to Whitespace")

Whitespace has no semantic meaning in Cadence syntax. It is used only to separate tokens.

## Keywords and access control[​](#keywords-and-access-control "Direct link to Keywords and access control")

### `access`[​](#access "Direct link to access")

The `access` keyword is fundamental to Cadence's access control system, specifying who can access and modify declarations like variables, functions, and types. Access modifiers include `access(all)` for public access, `access(contract)` for contract-scoped access, `access(account)` for account-scoped access, and `access(self)` for private access. The access keyword can also be used with entitlements to create fine-grained authorization systems, allowing specific operations only when the caller has the required entitlements. This system ensures that resources and sensitive data are protected according to the principle of least privilege.

`_10

access(all) var publicVariable: String

_10

access(contract) fun contractOnlyFunction() { }

_10

access(account) resource PrivateResource { }

_10

access(E) fun authorizedFunction() { } // requires entitlement E`

### `let`[​](#let "Direct link to let")

The `let` keyword declares immutable constants in Cadence, creating values that cannot be modified after initialization. Constants declared with `let` must be initialized with a value when declared, and their type can be explicitly specified or inferred from the initial value. For resources, `let` constants still require the move operator (`<-`) for assignment, and the resource cannot be moved out of the constant once assigned. The `let` keyword is preferred over `var` when a value doesn't need to change, as it provides compile-time guarantees about immutability and can enable compiler optimizations.

`_10

let constantValue = 42 // immutable constant

_10

let typedConstant: String = "Hello" // explicit type

_10

let resourceConstant: @NFT <- create NFT(id: 1) // immutable resource`

### `var`[​](#var "Direct link to var")

The `var` keyword declares mutable variables in Cadence, allowing values to be modified after initialization. Variables declared with `var` can be reassigned new values of the same type, and for resources, they can be moved in and out using the move operators. The `var` keyword is essential for maintaining state in contracts and resources, allowing data to be updated as the program executes. Like `let`, the type can be explicitly specified or inferred, and access modifiers can be applied to control who can read or modify the variable.

`_10

var mutableValue = 10 // mutable variable

_10

mutableValue = 20 // can be reassigned

_10

var resourceVariable: @Token? <- nil // mutable resource variable

_10

resourceVariable <- create Token(amount: 100) // can be assigned`

### `fun`[​](#fun "Direct link to fun")

The `fun` keyword declares functions in Cadence, which are reusable blocks of code that can accept parameters and return values. Functions can be declared at the top level, within contracts, resources, or structs, and their access level determines who can call them. Functions can accept both regular values and resources as parameters, and they can return values, resources, or nothing (void). The function signature includes parameter types, return type, and access modifiers, and functions can be overloaded based on parameter types and labels.

`_10

access(all) fun add(a: Int, b: Int): Int {

_10

return a + b

_10

}

_10

_10

access(contract) fun transfer(token: @Token, to: Address) {

_10

// resource transfer logic

_10

}`

### `resource`[​](#resource "Direct link to resource")

The `resource` keyword declares resource types in Cadence, which are unique, non-copyable types that represent digital assets or scarce resources. Resources must be explicitly created, moved, and destroyed, and they cannot be duplicated or lost accidentally. Resources can contain both regular values and other resources, and they can define functions (methods) that operate on the resource's data. The resource keyword is central to Cadence's resource-oriented programming model, ensuring that digital assets follow the same rules as physical assets in terms of ownership and transfer.

`_13

resource NFT {

_13

access(all) var id: UInt64

_13

access(all) var owner: Address

_13

_13

init(id: UInt64, owner: Address) {

_13

self.id = id

_13

self.owner = owner

_13

}

_13

_13

access(all) fun transfer(to: Address) {

_13

self.owner = to

_13

}

_13

}`

### `struct`[​](#struct "Direct link to struct")

The `struct` keyword declares structure types in Cadence, which are composite types that group related data together. Unlike resources, structs are copyable and follow value semantics, meaning they are duplicated when assigned or passed as parameters. Structs can contain fields of various types, including other structs, and they can define functions that operate on the struct's data. Structs are commonly used for organizing data that doesn't represent unique assets, such as metadata, configuration, or temporary data structures.

`_11

struct Metadata {

_11

access(all) var name: String

_11

access(all) var description: String

_11

access(all) var tags: [String]

_11

_11

init(name: String, description: String, tags: [String]) {

_11

self.name = name

_11

self.description = description

_11

self.tags = tags

_11

}

_11

}`

### `contract`[​](#contract "Direct link to contract")

The `contract` keyword declares smart contracts in Cadence, which are the primary unit of deployment and organization for blockchain code. Contracts can contain resources, structs, functions, and other declarations, and they provide a namespace for organizing related functionality. Contracts are deployed to specific accounts and can interact with each other through interfaces and capabilities. The contract keyword is essential for creating reusable, composable blockchain applications that can be deployed and upgraded independently.

`_10

access(all) contract MyContract {

_10

access(all) resource NFT {

_10

access(all) var id: UInt64

_10

init(id: UInt64) { self.id = id }

_10

}

_10

_10

access(all) fun mintNFT(id: UInt64): @NFT {

_10

return <- create NFT(id: id)

_10

}

_10

}`

### `interface`[​](#interface "Direct link to interface")

The `interface` keyword declares interface types in Cadence, which define a contract for what methods and properties a type must implement. Interfaces enable polymorphism and allow different types to be used interchangeably as long as they implement the required interface. Interfaces can declare function signatures, property requirements, and resource requirements, and they can be used as types for parameters, return values, and variables. The interface keyword is crucial for creating flexible, reusable code that can work with multiple implementations.

`_12

access(all) interface Transferable {

_12

access(all) fun transfer(to: Address)

_12

access(all) var owner: Address

_12

}

_12

_12

access(all) resource NFT: Transferable {

_12

access(all) var owner: Address

_12

_12

access(all) fun transfer(to: Address) {

_12

self.owner = to

_12

}

_12

}`

### `attachment`[​](#attachment "Direct link to attachment")

The `attachment` keyword declares [attachment types](/docs/language/attachments) in Cadence, which allow developers to extend struct or resource types (even ones they did not create) with new functionality without requiring the original author to plan for the intended behavior. Attachments are declared using the syntax `attachment <Name> for <Type>: <Conformances> { ... }` and can only be declared with `all` access. The attachment's kind (struct or resource) is automatically determined by the type it extends. Attachments are not first-class values and cannot exist independently of their base value, but they can be created using `attach` expressions, accessed via type indexing, and removed using `remove` statements.

`_16

access(all) resource R {

_16

access(all) let x: Int

_16

init(x: Int) { self.x = x }

_16

}

_16

_16

access(all) attachment A for R {

_16

access(all) let derivedX: Int

_16

init(scalar: Int) {

_16

self.derivedX = base.x * scalar

_16

}

_16

}

_16

_16

// Creating and using attachments

_16

let r <- create R(x: 5)

_16

let r2 <- attach A(scalar: 3) to <-r

_16

let attachmentRef = r2[A] // access attachment via type indexing`

### `enum`[​](#enum "Direct link to enum")

The `enum` keyword declares [enumeration](/docs/language/enumerations) types in Cadence, which define a set of named constant values. Enums can contain simple cases, and they provide [type safety](/docs/language/types-and-type-system/type-safety) by ensuring only valid enum values can be used. Enums are commonly used for representing states, types, or categories in a program. The enum keyword helps create more readable and maintainable code by replacing magic numbers or strings with meaningful named constants.

`_13

access(all) enum Status: UInt8 {

_13

_13

access(all)

_13

case pending

_13

_13

access(all)

_13

case active

_13

_13

access(all)

_13

case completed

_13

}

_13

_13

let status: Status = Status.active`

## Resource management functions[​](#resource-management-functions "Direct link to Resource management functions")

### `create`[​](#create "Direct link to create")

The `create` keyword is used to instantiate new resources in Cadence, calling the resource's initializer to set up the new instance. The create keyword must be used with the move operator (`<-`) to assign the newly created resource to a variable or return it from a function. Resources can only be created within the contract that defines them or through authorized functions, ensuring that resource creation is controlled and auditable. The create keyword is essential for minting new digital assets, creating new instances of resources, and initializing resource hierarchies.

`_10

resource Token {

_10

access(all) var amount: UInt64

_10

init(amount: UInt64) { self.amount = amount }

_10

}

_10

_10

let newToken <- create Token(amount: 100) // resource creation

_10

fun mint(): @Token { return <- create Token(amount: 50) } // creation in function`

### `destroy`[​](#destroy "Direct link to destroy")

The `destroy` keyword is used to explicitly destroy resources in Cadence, permanently removing them from the system and freeing up any associated storage. The destroy keyword must be used with the move operator (`<-`) to consume the resource being destroyed. Destroying a resource is irreversible and should be done carefully, typically only when the resource is no longer needed or when implementing burning mechanisms for digital assets. The destroy keyword ensures that resources follow a complete lifecycle from creation to destruction, preventing resource leaks.

`_10

resource Token {

_10

access(all) var amount: UInt64

_10

init(amount: UInt64) { self.amount = amount }

_10

}

_10

_10

let token: @Token <- create Token(amount: 100)

_10

destroy token // permanently removes the resource`

### `.borrow`[​](#borrow "Direct link to borrow")

The `.borrow` function provides temporary access to a resource without moving it, returning a reference that can be used to read or modify the resource's properties and call its functions. The borrow function is essential for resource management when you need to access a resource's data without transferring ownership. Borrowed references can be either authorized or unauthorized, depending on the access requirements, and they automatically become invalid when the borrowing scope ends. The borrow function is commonly used for reading resource state, calling resource methods, and implementing complex resource interactions.

`_13

resource NFT {

_13

access(all) var id: UInt64

_13

access(all) var metadata: String

_13

_13

access(all) fun updateMetadata(newMetadata: String) {

_13

self.metadata = newMetadata

_13

}

_13

}

_13

_13

let nft: @NFT <- create NFT(id: 1, metadata: "Original")

_13

let ref = &nft as &NFT

_13

ref.updateMetadata("Updated") // borrow and modify

_13

let id = ref.id // borrow and read`

### `.link`[​](#link "Direct link to link")

The `.link` function creates a capability that provides controlled access to a resource or function, allowing other accounts to interact with it through the capability system. The link function specifies the target path, the type of access being granted, and the restrictions on that access. Capabilities can be linked to either public or private storage paths, and they can include entitlements that define what operations are allowed. The link function is fundamental to Cadence's capability-based security model, enabling secure cross-account interactions while maintaining access control.

`_10

resource NFT {

_10

access(all) var id: UInt64

_10

access(all) fun transfer(to: Address) { /* transfer logic */ }

_10

}

_10

_10

let nft: @NFT <- create NFT(id: 1)

_10

account.storage.save(<- nft, to: /storage/myNFT)

_10

account.link<&NFT>(/public/myNFTCap, target: /storage/myNFT) // create capability`

### `.unlink`[​](#unlink "Direct link to unlink")

The `.unlink` function removes a capability from account storage, revoking the access that was previously granted through the capability. The unlink function takes the path where the capability was stored and removes it, making the linked resource or function no longer accessible through that capability. This function is important for access control management, allowing accounts to revoke permissions when they're no longer needed or when security requirements change. The unlink function is commonly used in permission management systems and when cleaning up temporary access grants.

`_10

// Remove a previously linked capability

_10

account.unlink(/public/myNFTCap)`

### `.getCapability`[​](#getcapability "Direct link to getcapability")

The `.getCapability` function retrieves a capability from account storage, allowing you to access the capability's target resource or function. The getCapability function returns an optional capability, which will be nil if no capability exists at the specified path. This function is essential for capability-based programming, allowing accounts to access resources and functions that have been shared with them through the capability system. The getCapability function is commonly used in cross-account interactions and when implementing permission-based access patterns.

`_10

let capability = account.getCapability<&NFT>(/public/myNFTCap)

_10

if let nftRef = capability.borrow() {

_10

// Use the borrowed reference

_10

nftRef.transfer(to: newOwner)

_10

}`

## Storage and account functions[​](#storage-and-account-functions "Direct link to Storage and account functions")

### `account.storage.save`[​](#accountstoragesave "Direct link to accountstoragesave")

The `account.storage.save` function stores a value or resource in account storage at a specified path. This function is essential for persisting data on the blockchain, allowing resources and values to be stored permanently in an account's storage space. The save function requires the move operator (`<-`) for resources and can store both regular values and resources. The storage path must be unique within the account, and the function will overwrite any existing value at that path. This function is commonly used for storing NFTs, tokens, and other digital assets in user accounts.

`_10

resource NFT {

_10

access(all) var id: UInt64

_10

init(id: UInt64) { self.id = id }

_10

}

_10

_10

let nft: @NFT <- create NFT(id: 1)

_10

account.storage.save(<- nft, to: /storage/myNFT) // save resource

_10

account.storage.save("metadata", to: /storage/metadata) // save value`

### `account.storage.load`[​](#accountstorageload "Direct link to accountstorageload")

The `account.storage.load` function retrieves a value or resource from account storage at a specified path. This function returns an optional value, which will be nil if no value exists at the specified path or if the type doesn't match. For resources, the load function requires the move operator (`<-`) to transfer ownership from storage to the variable. The load function is essential for accessing stored data and is commonly used in conjunction with save to implement persistent storage patterns.

`_10

let nft <- account.storage.load<@NFT>(from: /storage/myNFT)

_10

let metadata = account.storage.load<String>(from: /storage/metadata)`

### `account.storage.borrow`[​](#accountstorageborrow "Direct link to accountstorageborrow")

The `account.storage.borrow` function provides temporary access to a stored resource without moving it from storage. This function returns a reference to the resource that can be used to read or modify the resource's properties and call its functions. The borrow function is useful when you need to access a resource's data without removing it from storage, and it's commonly used for reading resource state or calling resource methods. The borrowed reference becomes invalid when the borrowing scope ends.

`_10

let nftRef = account.storage.borrow<&NFT>(from: /storage/myNFT)

_10

if let ref = nftRef {

_10

let id = ref.id // read property

_10

ref.updateMetadata("New metadata") // call method

_10

}`

## Type system keywords[​](#type-system-keywords "Direct link to Type system keywords")

### `AnyStruct`[​](#anystruct "Direct link to anystruct")

The `AnyStruct` type is a top type in Cadence that can hold any struct value, providing maximum flexibility when you need to work with different struct types. AnyStruct is commonly used in generic containers, event parameters, and situations where you need to store or pass around different types of structs. When using AnyStruct, you typically need to perform type checking or type casting to access the specific properties or methods of the underlying struct. This type is essential for creating flexible, reusable code that can work with various struct types.

`_10

let anyValue: AnyStruct = "Hello" // can hold any struct

_10

let anotherValue: AnyStruct = 42 // can hold different types`

### `AnyResource`[​](#anyresource "Direct link to anyresource")

The `AnyResource` type is a top type in Cadence that can hold any resource value, allowing you to work with different resource types in a generic way. AnyResource is commonly used in generic containers, capability systems, and situations where you need to store or pass around different types of resources. When using AnyResource, you typically need to perform type checking or type casting to access the specific properties or methods of the underlying resource. This type is essential for creating flexible resource management systems.

`_10

let anyResource: AnyResource <- create SomeResource()

_10

let anotherResource: AnyResource <- create AnotherResource()`

### `Void`[​](#void "Direct link to void")

The `Void` type represents the absence of a value in Cadence, used when a function doesn't return anything or when you need to explicitly indicate that no value is expected. Functions that don't have a return statement or explicitly return Void are said to return nothing. The Void type is commonly used in function signatures, event definitions, and situations where you need to explicitly indicate that no value is being returned or expected. This type helps make code intentions clear and provides type safety.

`_10

fun doSomething(): Void {

_10

// function that doesn't return a value

_10

}

_10

_10

fun anotherFunction() { // implicitly returns Void

_10

// function body

_10

}`

### `Never`[​](#never "Direct link to never")

The `Never` type represents a function that never returns normally, typically because it always throws an error or aborts execution. The Never type is used in function signatures to indicate that the function will not complete successfully and return a value. This type is commonly used in error handling functions, assertion functions, and functions that perform critical operations that must succeed or fail completely. The Never type helps make error handling explicit and provides compile-time guarantees about function behavior.

`_10

fun assert(condition: Bool): Never {

_10

if !condition {

_10

panic("Assertion failed")

_10

}

_10

}`

## Control flow keywords[​](#control-flow-keywords "Direct link to Control flow keywords")

### `if`[​](#if "Direct link to if")

The `if` keyword provides conditional execution in Cadence, allowing code to be executed only when a specified condition is true. If statements can include optional else clauses to handle the case when the condition is false, and they can be chained with else if clauses for multiple conditions. The condition in an if statement must evaluate to a boolean value, and the code blocks can contain any valid Cadence code including variable declarations, function calls, and resource operations. If statements are fundamental to implementing business logic and conditional behavior in smart contracts.

`_10

if condition {

_10

// execute when condition is true

_10

} else if anotherCondition {

_10

// execute when anotherCondition is true

_10

} else {

_10

// execute when no conditions are true

_10

}`

### `while`[​](#while "Direct link to while")

The `while` keyword creates loops that execute a block of code repeatedly as long as a specified condition remains true. The condition is evaluated before each iteration, and the loop continues until the condition becomes false. While loops are useful for iterating over data structures, implementing retry logic, and performing operations that need to continue until a certain state is reached. Care must be taken to ensure that while loops eventually terminate to prevent infinite loops that could consume excessive gas.

`_10

var counter = 0

_10

while counter < 10 {

_10

// execute while counter is less than 10

_10

counter = counter + 1

_10

}`

### `for`[​](#for "Direct link to for")

The `for` keyword creates loops for iterating over collections like arrays, dictionaries, and ranges in Cadence. For loops can iterate over the elements of a collection, providing access to each element in sequence. The for keyword is commonly used with the `in` keyword to specify the collection being iterated over, and the loop variable can be used to access the current element. For loops are essential for processing collections of data, implementing batch operations, and performing operations on multiple items.

`_10

let numbers = [1, 2, 3, 4, 5]

_10

for number in numbers {

_10

// process each number

_10

}

_10

_10

for i in 0...5 {

_10

// iterate over range

_10

}`

### `return`[​](#return "Direct link to return")

The `return` keyword exits a function and optionally provides a value to be returned to the caller. The return keyword can be used with or without a value, depending on the function's return type. When used with a value, the value must match the function's declared return type. The return keyword immediately terminates function execution, making it useful for early exits and conditional returns. For functions that return resources, the return keyword must be used with the move operator (`<-`) to transfer ownership of the resource.

`_10

fun add(a: Int, b: Int): Int {

_10

return a + b // return with value

_10

}

_10

_10

fun earlyExit(condition: Bool) {

_10

if condition {

_10

return // early exit without value

_10

}

_10

// continue execution

_10

}`

## Error handling[​](#error-handling "Direct link to Error handling")

### `panic`[​](#panic "Direct link to panic")

The `panic` function immediately aborts the execution of the current transaction with an optional error message. The panic function is used for critical errors that cannot be recovered from, such as assertion failures, invalid state conditions, or security violations. When panic is called, the entire transaction is rolled back, and any changes made during the transaction are discarded. The panic function is commonly used in assertion functions, input validation, and error conditions that indicate a fundamental problem with the program's logic or state.

`_12

fun assert(condition: Bool, message: String) {

_12

if !condition {

_12

panic(message) // abort with error message

_12

}

_12

}

_12

_12

fun divide(a: Int, b: Int): Int {

_12

if b == 0 {

_12

panic("Division by zero") // critical error

_12

}

_12

return a / b

_12

}`

### `pre` and `post`[​](#pre-and-post "Direct link to pre-and-post")

The `pre` and `post` keywords are used for function [pre-conditions and post-conditions](/docs/language/pre-and-post-conditions) in Cadence, providing a way to specify requirements and guarantees about function behavior. Pre-conditions (`pre`) specify conditions that must be true before a function is called, while post-conditions (`post`) specify conditions that must be true after the function completes. These conditions are checked at runtime and will cause a panic if they are not satisfied. Pre and post conditions help ensure function correctness and provide documentation about function requirements and guarantees.

`_10

fun transfer(amount: UInt64): UInt64 {

_10

pre {

_10

amount > 0: "Amount must be positive"

_10

}

_10

post {

_10

result > 0: "Result must be positive"

_10

}

_10

return amount

_10

}`

## Events and logging[​](#events-and-logging "Direct link to Events and logging")

### `event`[​](#event "Direct link to event")

The `event` keyword declares event types in Cadence, which are used to emit structured data that can be indexed and queried by blockchain clients. Events are essential for creating transparent, auditable blockchain applications that can communicate state changes and important occurrences to external systems. Events can contain various data types including structs, resources, and primitive types, and they are emitted using the `emit` keyword. Events are commonly used for tracking transactions, state changes, and important business events in smart contracts.

`_10

access(all) event TransferEvent(

_10

from: Address,

_10

to: Address,

_10

amount: UInt64

_10

)

_10

_10

fun transfer(to: Address, amount: UInt64) {

_10

// transfer logic

_10

emit TransferEvent(from: self.owner, to: to, amount: amount)

_10

}`

### `emit`[​](#emit "Direct link to emit")

The `emit` keyword is used to emit events in Cadence, broadcasting structured data to the blockchain network for indexing and querying by external systems. The emit keyword is followed by an event instance and any parameters that the event requires. Emitted events are permanently recorded on the blockchain and can be used for auditing, analytics, and triggering external processes. The emit keyword is commonly used in conjunction with the event keyword to create transparent, auditable blockchain applications.

`_10

access(all) event NFTMinted(id: UInt64, owner: Address)

_10

_10

fun mintNFT(id: UInt64): @NFT {

_10

let nft <- create NFT(id: id)

_10

emit NFTMinted(id: id, owner: self.owner) // emit event

_10

return <- nft

_10

}`

## Composite type keywords[​](#composite-type-keywords "Direct link to Composite type keywords")

### `init`[​](#init "Direct link to init")

The `init` keyword declares initializer functions in Cadence, which are special functions that set up new instances of types when they are created. Initializers are called automatically when creating new instances using the `create` keyword for resources or when declaring structs and other types. The init function can accept parameters to configure the new instance, and it's responsible for setting up the initial state of the object. Initializers are essential for ensuring that objects are properly initialized with valid state.

`_10

resource NFT {

_10

access(all) var id: UInt64

_10

access(all) var owner: Address

_10

_10

init(id: UInt64, owner: Address) {

_10

self.id = id

_10

self.owner = owner

_10

}

_10

}`

### `self`[​](#self "Direct link to self")

The `self` keyword refers to the current instance of a type within its methods and initializers. The self keyword is used to access the current object's properties and methods, distinguishing them from local variables or parameters with the same names. In resource and struct methods, self is used to modify the object's state, access its properties, and call other methods on the same object. The self keyword is essential for object-oriented programming patterns in Cadence.

`_11

resource Token {

_11

access(all) var balance: UInt64

_11

_11

access(all) fun transfer(amount: UInt64) {

_11

self.balance = self.balance - amount // access own property

_11

}

_11

_11

access(all) fun getBalance(): UInt64 {

_11

return self.balance // return own property

_11

}

_11

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/syntax.md)

[Previous

Language Reference](/docs/language/)[Next

Constants and Variable Declarations](/docs/language/constants-and-variables)

###### Rate this page

😞😐😊

* [Comments](#comments)
  + [Documentation comments](#documentation-comments)
* [Identifiers](#identifiers)
  + [Reserved identifiers](#reserved-identifiers)
  + [Conventions](#conventions)
* [Symbols and operators](#symbols-and-operators)
  + [`&` (ampersand)](#-ampersand)
  + [`@` (at symbol)](#-at-symbol)
  + [`:` (colon)](#-colon)
  + [`=` (equals)](#-equals)
  + [`!` (exclamation mark)](#-exclamation-mark)
  + [`/` (forward slash)](#-forward-slash)
  + [`<-` (move operator)](#--move-operator)
  + [`<-!` (force-assignment move operator)](#--force-assignment-move-operator)
  + [`<->` (swap operator)](#--swap-operator)
  + [`+`, `-`, `*`, `%` (arithmetic operators)](#-----arithmetic-operators)
  + [`?` (question mark)](#-question-mark)
  + [`_` (underscore)](#_-underscore)
  + [`;` (semicolon)](#-semicolon)
* [Punctuation marks](#punctuation-marks)
  + [`.` (dot/period)](#-dotperiod)
  + [`,` (comma)](#-comma)
  + [`()` (parentheses)](#-parentheses)
  + [`<>` (angle brackets)](#-angle-brackets)
  + [`{}` (curly brackets)](#-curly-brackets)
  + [`[]` (square brackets)](#-square-brackets)
  + [`` ` `` (backtick)](#-backtick)
  + [Whitespace](#whitespace)
* [Keywords and access control](#keywords-and-access-control)
  + [`access`](#access)
  + [`let`](#let)
  + [`var`](#var)
  + [`fun`](#fun)
  + [`resource`](#resource)
  + [`struct`](#struct)
  + [`contract`](#contract)
  + [`interface`](#interface)
  + [`attachment`](#attachment)
  + [`enum`](#enum)
* [Resource management functions](#resource-management-functions)
  + [`create`](#create)
  + [`destroy`](#destroy)
  + [`.borrow`](#borrow)
  + [`.link`](#link)
  + [`.unlink`](#unlink)
  + [`.getCapability`](#getcapability)
* [Storage and account functions](#storage-and-account-functions)
  + [`account.storage.save`](#accountstoragesave)
  + [`account.storage.load`](#accountstorageload)
  + [`account.storage.borrow`](#accountstorageborrow)
* [Type system keywords](#type-system-keywords)
  + [`AnyStruct`](#anystruct)
  + [`AnyResource`](#anyresource)
  + [`Void`](#void)
  + [`Never`](#never)
* [Control flow keywords](#control-flow-keywords)
  + [`if`](#if)
  + [`while`](#while)
  + [`for`](#for)
  + [`return`](#return)
* [Error handling](#error-handling)
  + [`panic`](#panic)
  + [`pre` and `post`](#pre-and-post)
* [Events and logging](#events-and-logging)
  + [`event`](#event)
  + [`emit`](#emit)
* [Composite type keywords](#composite-type-keywords)
  + [`init`](#init)
  + [`self`](#self)