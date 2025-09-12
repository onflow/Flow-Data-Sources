# Source: https://cadence-lang.org/docs/language/values-and-types/strings-and-characters

Strings and Characters | Cadence



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
* Strings and Characters

On this page

# Strings and Characters

Strings and characters are used as follows:

* Strings are collections of characters.
* Strings have the type `String` and characters have the type `Character`.
* Strings can be used to work with text in a Unicode-compliant way.
* Strings are immutable.

String and character literals are enclosed in double quotation marks (`"`):

`_10

let someString = "Hello, world!"`

String literals may contain escape sequences. An escape sequence starts with a backslash (`\`):

* `\0`: Null character
* `\\`: Backslash
* `\t`: Horizontal tab
* `\n`: Line feed
* `\r`: Carriage return
* `\"`: Double quotation mark
* `\'`: Single quotation mark
* `\u`: A Unicode scalar value, written as `\u{x}`, where `x` is a 1–8 digit hexadecimal number, which needs to be a valid Unicode scalar value (i.e., in the range 0 to 0xD7FF and 0xE000 to 0x10FFFF inclusive).

`` _10

// Declare a constant which contains two lines of text

_10

// (separated by the line feed character `\n`), and ends

_10

// with a thumbs up emoji, which has code point U+1F44D (0x1F44D).

_10

//

_10

let thumbsUpText =

_10

"This is the first line.\nThis is the second line with an emoji: \u{1F44D}" ``

The type `Character` represents a single, human-readable character. Characters are extended grapheme clusters, which consist of one or more Unicode scalars.

For example, the single character `ü` can be represented in several ways in Unicode. First, it can be represented by a single Unicode scalar value `ü` ("LATIN SMALL LETTER U WITH DIAERESIS", code point U+00FC). Second, the same single character can be represented by two Unicode scalar values: `u` ("LATIN SMALL LETTER U", code point U+0075), and "COMBINING DIAERESIS" (code point U+0308). The combining Unicode scalar value is applied to the scalar before it, which turns a `u` into a `ü`.

Still, both variants represent the same human-readable character `ü`:

`` _10

let singleScalar: Character = "\u{FC}"

_10

// `singleScalar` is `ü`

_10

let twoScalars: Character = "\u{75}\u{308}"

_10

// `twoScalars` is `ü` ``

Another example where multiple Unicode scalar values are rendered as a single, human-readable character is a flag emoji. These emojis consist of two "REGIONAL INDICATOR SYMBOL LETTER" Unicode scalar values:

`` _10

// Declare a constant for a string with a single character, the emoji

_10

// for the Canadian flag, which consists of two Unicode scalar values:

_10

// - REGIONAL INDICATOR SYMBOL LETTER C (U+1F1E8)

_10

// - REGIONAL INDICATOR SYMBOL LETTER A (U+1F1E6)

_10

//

_10

let canadianFlag: Character = "\u{1F1E8}\u{1F1E6}"

_10

// `canadianFlag` is `🇨🇦` ``

## String templates / String Interpolation[​](#string-templates--string-interpolation "Direct link to String templates / String Interpolation")

String templates, or string interpolation, allow constants, variables, and expressions to be inlined into strings simplifying the process of constructing dynamic strings. String templates are currently supported in single-line literals by wrapping the target in parentheses and prefixing it with a backslash (`\`).

The target in the parentheses must support the built-in function `toString()`, meaning it must evaluate to a `String`, `Number`, `Address`, `Character`, `Bool` or `Path`. Carriage returns, line feeds and nested string literals are not supported inside the parentheses.

`` _10

let result = 2 + 2

_10

let template: String = "2 + 2 = \(result)" // `template` is `2 + 2 = 4`

_10

// Invalid: Empty string template

_10

let empty: String = "\()"

_10

// Invalid: Nested string template

_10

let nested: String = "outer string \( "\(inner template)" )"

_10

// Invalid: Unsupported type

_10

let x: [AnyStruct] = ["tmp", 1]

_10

let arr: String = "\(x)" ``

## String fields and functions[​](#string-fields-and-functions "Direct link to String fields and functions")

Strings have multiple built-in functions you can use:

* `_10

  let length: Int`

  Returns the number of characters in the string as an integer.

  `` _10

  let example = "hello"

  _10

  _10

  // Find the number of elements of the string.

  _10

  let length = example.length

  _10

  // `length` is `5` ``
* `_10

  let utf8: [UInt8]`

  The byte array of the UTF-8 encoding.

  `` _10

  let flowers = "Flowers \u{1F490}"

  _10

  let bytes = flowers.utf8

  _10

  // `bytes` is `[70, 108, 111, 119, 101, 114, 115, 32, 240, 159, 146, 144]` ``
* `_10

  view fun concat(_ other: String): String`

  Concatenates the string `other` to the end of the original string, but does not modify the original string. This function creates a new string whose length is the sum of the lengths of the string the function is called on and the string given as a parameter.

  `` _10

  let example = "hello"

  _10

  let new = "world"

  _10

  _10

  // Concatenate the new string onto the example string and return the new string.

  _10

  let helloWorld = example.concat(new)

  _10

  // `helloWorld` is now `"helloworld"` ``
* `_10

  view fun slice(from: Int, upTo: Int): String`

  Returns a string slice of the characters in the given string from start index `from` up to, but not including, the end index `upTo`. This function creates a new string whose length is `upTo - from`. It does not modify the original string. If either of the parameters are out of the bounds of the string, or the indices are invalid (`from > upTo`), then the function will fail.

  `` _11

  let example = "helloworld"

  _11

  _11

  // Create a new slice of part of the original string.

  _11

  let slice = example.slice(from: 3, upTo: 6)

  _11

  // `slice` is now `"low"`

  _11

  _11

  // Run-time error: Out of bounds index, the program aborts.

  _11

  let outOfBounds = example.slice(from: 2, upTo: 10)

  _11

  _11

  // Run-time error: Invalid indices, the program aborts.

  _11

  let invalidIndices = example.slice(from: 2, upTo: 1) ``
* `_10

  view fun decodeHex(): [UInt8]`

  Returns an array containing the bytes represented by the given hexadecimal string.

  The given string must only contain hexadecimal characters and must have an even length.
  If the string is malformed, the program aborts.

  `` _10

  let example = "436164656e636521"

  _10

  _10

  example.decodeHex() // is `[67, 97, 100, 101, 110, 99, 101, 33]` ``
* `_10

  view fun toLower(): String`

  Returns a string where all upper case letters are replaced with lowercase characters.

  `` _10

  let example = "Flowers"

  _10

  _10

  example.toLower() // is `flowers` ``
* `_10

  view fun replaceAll(of: String, with: String): String`

  Returns a string where all occurences of `of` are replaced with `with`. If `of` is empty, it matches at the beginning of the string and after each UTF-8 sequence yielding k+1 replacements for a string of length k.

  `` _10

  let example = "abababa"

  _10

  _10

  example.replaceAll(of: "a", with: "o") // is `obobobo` ``
* `_10

  view fun split(separator: String): [String]`

  Returns the variable-sized array of strings created splitting the receiver string on the `separator`.

  `` _10

  let example = "hello world"

  _10

  _10

  example.split(separator: " ") // is `["hello", "world"]` ``
* `_10

  view fun count(_ substr: String): Int`

  Returns the number of times the provided `substr` appears in the string. This function only counts each character once (see below).

  `_10

  let example = "11111"

  _10

  _10

  example.count("11") // is 2`
* `_10

  view fun index(of: String): Int`

  Returns the index of the first (leftmost) occurrence of `of` in the string or `-1` if `of` does not occur in the string.

  `_10

  let example = "abcabc"

  _10

  _10

  example.index(of: "a") // is 0

  _10

  example.index(of: "d") // is -1`
* `_10

  view fun contains(_ other: String): Bool`

  Returns `true` if the string contains `other`, `false` otherwise.

  `_10

  let example = "abcdef"

  _10

  _10

  example.contains("abcdefg") // is false`

The `String` type also provides the following functions:

* `_10

  view fun String.encodeHex(_ data: [UInt8]): String`

  Returns a hexadecimal string for the given byte array

  `` _10

  let data = [1 as UInt8, 2, 3, 0xCA, 0xDE]

  _10

  _10

  String.encodeHex(data) // is `"010203cade"` ``
* `_10

  view fun String.join(_ strings: [String], separator: String): String`

  Returns the string created by joining the array of `strings` with the provided `separator`.

  `_10

  let strings = ["hello", "world"]

  _10

  String.join(strings, separator: " ") // is "hello world"`

`String`s are also indexable, returning a `Character` value.

`_10

let str = "abc"

_10

let c = str[0] // is the Character "a"`

* `_10

  view fun String.fromUTF8(_ input: [UInt8]): String?`

  Attempts to convert a UTF-8 encoded byte array into a `String`. This function returns `nil` if the byte array contains invalid UTF-8,
  such as incomplete codepoint sequences or undefined graphemes.

  For a given string `s`, `String.fromUTF8(s.utf8)` is equivalent to wrapping `s` up in an [optional](/docs/language/values-and-types/anystruct-anyresource-opts-never#optionals).

## Character fields and functions[​](#character-fields-and-functions "Direct link to Character fields and functions")

`Character` values can be converted into `String` values using the `toString` function:

* `` _10

  view fun toString(): String` ``

  Returns the string representation of the character.

  `_10

  let c: Character = "x"

  _10

  _10

  c.toString() // is "x"`
* `_10

  view fun String.fromCharacters(_ characters: [Character]): String`

  Builds a new `String` value from an array of `Character`s. Because `String`s are immutable, this operation makes a copy of the input array.

  `_10

  let rawUwU: [Character] = ["U", "w", "U"]

  _10

  let uwu: String = String.fromCharacters(rawUwU) // "UwU"`
* `_10

  let utf8: [UInt8]`

  The byte array of the UTF-8 encoding.

  `` _10

  let a: Character = "a"

  _10

  let a_bytes = a.utf8 // `a_bytes` is `[97]`

  _10

  _10

  let bouquet: Character = "\u{1F490}"

  _10

  let bouquet_bytes = bouquet.utf8 // `bouquet_bytes` is `[240, 159, 146, 144]` ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/strings-and-characters.md)

[Previous

AnyStruct, AnyResource, Optionals, and Never](/docs/language/values-and-types/anystruct-anyresource-opts-never)[Next

Arrays](/docs/language/values-and-types/arrays)

###### Rate this page

😞😐😊

* [String templates / String Interpolation](#string-templates--string-interpolation)
* [String fields and functions](#string-fields-and-functions)
* [Character fields and functions](#character-fields-and-functions)