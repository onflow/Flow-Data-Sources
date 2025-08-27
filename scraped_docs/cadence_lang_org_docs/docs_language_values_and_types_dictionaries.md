# Source: https://cadence-lang.org/docs/language/values-and-types/dictionaries

Dictionaries | Cadence



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

    - [Booleans, Numeric Literals, and Integers](/docs/language/values-and-types/booleans-numlits-ints)
    - [Fixed-Point Numbers and Functions](/docs/language/values-and-types/fixed-point-nums-ints)
    - [Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers](/docs/language/values-and-types/min-max-saturation-floating-pt-nums)
    - [Addresses and Address Functions](/docs/language/values-and-types/addresses-functions)
    - [AnyStruct, AnyResource, Optionals, and Never](/docs/language/values-and-types/anystruct-anyresource-opts-never)
    - [Strings and Characters](/docs/language/values-and-types/strings-and-characters)
    - [Arrays](/docs/language/values-and-types/arrays)
    - [Dictionaries](/docs/language/values-and-types/dictionaries)
    - [InclusiveRange](/docs/language/values-and-types/inclusive-range)
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
* [Values and Types](/docs/language/values-and-types/)
* Dictionaries

On this page

# Dictionaries

Dictionaries are mutable, unordered collections of key-value associations. Dictionaries may contain a key only once and may contain a value multiple times.

* Dictionary literals start with an opening brace `{` and end with a closing brace `}`.
* Keys are separated from values by a colon, and key-value associations are separated by commas.

`_10

// An empty dictionary

_10

//

_10

{}

_10

_10

// A dictionary which associates integers with booleans

_10

//

_10

{

_10

1: true,

_10

2: false

_10

}`

## Dictionary types[​](#dictionary-types "Direct link to Dictionary types")

Dictionary types have the form `{K: V}`, where `K` is the type of the key, and `V` is the type of the value. For example, a dictionary with `Int` keys and `Bool` values has type `{Int: Bool}`.

In a dictionary, all keys must have a type that is a subtype of the dictionary's key type (`K`), and all values must have a type that is a subtype of the dictionary's value type (`V`).

`` _24

// Declare a constant that has type `{Int: Bool}`,

_24

// a dictionary mapping integers to booleans.

_24

//

_24

let booleans = {

_24

1: true,

_24

0: false

_24

}

_24

_24

// Declare a constant that has type `{Bool: Int}`,

_24

// a dictionary mapping booleans to integers.

_24

//

_24

let integers = {

_24

true: 1,

_24

false: 0

_24

}

_24

_24

// Mixing keys with different types, and mixing values with different types,

_24

// is possible by declaring the expected dictionary type with the common supertype

_24

// of all keys, and the common supertype of all values.

_24

//

_24

let mixedValues: {String: AnyStruct} = {

_24

"a": 1,

_24

"b": true

_24

} ``

Dictionary types are covariant in their key and value types. For example, `{Int: String}` is a subtype of `{AnyStruct: String}` and also a subtype of `{Int: AnyStruct}`. This is safe because dictionaries are value types and not reference types.

## Dictionary Access[​](#dictionary-access "Direct link to Dictionary Access")

To get the value for a specific key from a dictionary, the following access syntax can be used: the dictionary is followed by an opening square bracket `[`, the key, and ends with a closing square bracket `]`.

Accessing a key returns an [optional](/docs/language/values-and-types/anystruct-anyresource-opts-never#optionals): if the key is found in the dictionary, the value for the given key is returned; and if the key is not found, `nil` is returned.

`` _17

// Declare a constant that has type `{Int: Bool}`,

_17

// a dictionary mapping integers to booleans.

_17

//

_17

let booleans = {

_17

1: true,

_17

0: false

_17

}

_17

_17

// The result of accessing a key has type `Bool?`.

_17

//

_17

booleans[1] // is `true`

_17

booleans[0] // is `false`

_17

booleans[2] // is `nil`

_17

_17

// Invalid: Accessing a key which does not have type `Int`.

_17

//

_17

booleans["1"] ``

`` _12

// Declare a constant that has type `{Bool: Int}`,

_12

// a dictionary mapping booleans to integers.

_12

//

_12

let integers = {

_12

true: 1,

_12

false: 0

_12

}

_12

_12

// The result of accessing a key has type `Int?`

_12

//

_12

integers[true] // is `1`

_12

integers[false] // is `0` ``

To set the value for a key of a dictionary, the access syntax can be used as well.

`` _13

// Declare a constant that has type `{Int: Bool}`,

_13

// a dictionary mapping booleans to integers.

_13

//

_13

let booleans = {

_13

1: true,

_13

0: false

_13

}

_13

_13

// Assign new values for the keys `1` and `0`.

_13

//

_13

booleans[1] = false

_13

booleans[0] = true

_13

// `booleans` is `{1: false, 0: true}` ``

## Dictionary fields and functions[​](#dictionary-fields-and-functions "Direct link to Dictionary fields and functions")

* `_10

  let length: Int`

  The number of entries in the dictionary.

  `` _10

  // Declare a dictionary mapping strings to integers.

  _10

  let numbers = {"fortyTwo": 42, "twentyThree": 23}

  _10

  _10

  // Find the number of entries of the dictionary.

  _10

  let length = numbers.length

  _10

  _10

  // `length` is `2` ``
* `_10

  access(Mutate | Insert)

  _10

  fun insert(key: K, _ value: V): V?`

  Inserts the given value of type `V` into the dictionary under the given `key` of type `K`.

  The inserted key must have the same type as the dictionary's key type, and the inserted value must have the same type as the dictionary's value type.

  Returns the previous value as an optional if the dictionary contained the key; otherwise, returns `nil`.

  Updates the value if the dictionary already contained the key.

  This function [mutates](/docs/language/access-control) the dictionary.

  `` _11

  // Declare a dictionary mapping strings to integers.

  _11

  let numbers = {"twentyThree": 23}

  _11

  _11

  // Insert the key `"fortyTwo"` with the value `42` into the dictionary.

  _11

  // The key did not previously exist in the dictionary,

  _11

  // so the result is `nil`

  _11

  //

  _11

  let old = numbers.insert(key: "fortyTwo", 42)

  _11

  _11

  // `old` is `nil`

  _11

  // `numbers` is `{"twentyThree": 23, "fortyTwo": 42}` ``
* `_10

  access(Mutate | Remove)

  _10

  fun remove(key: K): V?`

  Removes the value for the given `key` of type `K` from the dictionary.

  Returns the value of type `V` as an optional if the dictionary contained the key; otherwise, returns `nil`.

  This function [mutates](/docs/language/access-control) the dictionary.

  `` _19

  // Declare a dictionary mapping strings to integers.

  _19

  let numbers = {"fortyTwo": 42, "twentyThree": 23}

  _19

  _19

  // Remove the key `"fortyTwo"` from the dictionary.

  _19

  // The key exists in the dictionary,

  _19

  // so the value associated with the key is returned.

  _19

  //

  _19

  let fortyTwo = numbers.remove(key: "fortyTwo")

  _19

  _19

  // `fortyTwo` is `42`

  _19

  // `numbers` is `{"twentyThree": 23}`

  _19

  _19

  // Remove the key `"oneHundred"` from the dictionary.

  _19

  // The key does not exist in the dictionary, so `nil` is returned.

  _19

  //

  _19

  let oneHundred = numbers.remove(key: "oneHundred")

  _19

  _19

  // `oneHundred` is `nil`

  _19

  // `numbers` is `{"twentyThree": 23}` ``
* `_10

  let keys: [K]`

  Returns an array of the keys of type `K` in the dictionary. This does not modify the dictionary — it just returns a copy of the keys as an array. If the dictionary is empty, this returns an empty array. The ordering of the keys is undefined.

  `` _10

  // Declare a dictionary mapping strings to integers.

  _10

  let numbers = {"fortyTwo": 42, "twentyThree": 23}

  _10

  _10

  // Find the keys of the dictionary.

  _10

  let keys = numbers.keys

  _10

  _10

  // `keys` has type `[String]` and is `["fortyTwo","twentyThree"]` ``
* `_10

  let values: [V]`

  Returns an array of the values of type `V` in the dictionary. This does not modify the dictionary — it just returns a copy of the values as an array. If the dictionary is empty, this returns an empty array.

  This field is not available if `V` is a resource type.

  `` _10

  // Declare a dictionary mapping strings to integers.

  _10

  let numbers = {"fortyTwo": 42, "twentyThree": 23}

  _10

  _10

  // Find the values of the dictionary.

  _10

  let values = numbers.values

  _10

  _10

  // `values` has type [Int] and is `[42, 23]` ``
* `_10

  access(all)

  _10

  view fun containsKey(key: K): Bool`

  Returns true if the given key of type `K` is in the dictionary.

  `` _15

  // Declare a dictionary mapping strings to integers.

  _15

  let numbers = {"fortyTwo": 42, "twentyThree": 23}

  _15

  _15

  // Check if the dictionary contains the key "twentyFive".

  _15

  let containsKeyTwentyFive = numbers.containsKey("twentyFive")

  _15

  // `containsKeyTwentyFive` is `false`

  _15

  _15

  // Check if the dictionary contains the key "fortyTwo".

  _15

  let containsKeyFortyTwo = numbers.containsKey("fortyTwo")

  _15

  // `containsKeyFortyTwo` is `true`

  _15

  _15

  // Invalid: Check if the dictionary contains the key 42.

  _15

  // This results in a type error, as the key type of the dictionary is `String`.

  _15

  //

  _15

  let containsKey42 = numbers.containsKey(42) ``
* `_10

  access(all)

  _10

  fun forEachKey(_ function: fun(K): Bool): Void`

  Iterates through all the keys in the dictionary, exiting early if the passed function returns false. This is more efficient than calling `.keys` and iterating over the resulting array, since an intermediate allocation is avoided. The order of key iteration is undefined, similar to `.keys`.

  `` _18

  // Take in a targetKey to look for, and a dictionary to iterate through.

  _18

  fun myContainsKey(targetKey: String, dictionary: {String: Int}) {

  _18

  // Declare an accumulator that we'll capture inside a closure.

  _18

  var found = false

  _18

  _18

  // At each step, `key` will be bound to another key from `dictionary`.

  _18

  dictionary.forEachKey(fun (key: String): Bool {

  _18

  found = key == targetKey

  _18

  _18

  // The returned boolean value, signals whether to continue iterating.

  _18

  // This allows for control flow during the iteration process:

  _18

  // true = `continue`

  _18

  // false = `break`

  _18

  return !found

  _18

  })

  _18

  _18

  return found

  _18

  } ``

## Dictionary keys[​](#dictionary-keys "Direct link to Dictionary keys")

Dictionary keys must be hashable and equatable.

Most of the built-in types, like booleans and integers, are hashable and equatable, so can be used as keys in dictionaries.

A comprehensive list of valid dictionary key types:

* [Address](/docs/language/values-and-types/addresses-functions)
* [Bool](/docs/language/values-and-types/booleans-numlits-ints#booleans)
* [Character](/docs/language/values-and-types/strings-and-characters)
* [Enum](/docs/language/enumerations)
* [Numbers](/docs/language/values-and-types/booleans-numlits-ints#numeric-literals)
* [Paths](/docs/language/accounts/paths)
* [Runtime-types](/docs/language/types-and-type-system/run-time-types)
* [String](/docs/language/values-and-types/strings-and-characters)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/dictionaries.md)

[Previous

Arrays](/docs/language/values-and-types/arrays)[Next

InclusiveRange](/docs/language/values-and-types/inclusive-range)

###### Rate this page

😞😐😊

* [Dictionary types](#dictionary-types)
* [Dictionary Access](#dictionary-access)
* [Dictionary fields and functions](#dictionary-fields-and-functions)
* [Dictionary keys](#dictionary-keys)