# Source: https://cadence-lang.org/docs/language/values-and-types/arrays

Arrays | Cadence



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
* Arrays

On this page

# Arrays

Arrays consist of the following:

* Arrays are mutable, ordered collections of values.
* Arrays may contain a value multiple times.
* Array literals start with an opening square bracket `[` and end with a closing square bracket `]`.

`_10

// An empty array

_10

//

_10

[]

_10

_10

// An array with integers

_10

//

_10

[1, 2, 3]`

## Array types[​](#array-types "Direct link to Array types")

Arrays either have a fixed size or are variably sized (i.e., elements can be added and removed).

Fixed-size array types have the form `[T; N]`, where `T` is the element type and `N` is the size of the array. `N` must be statically known, meaning that it needs to be an integer literal. For example, a fixed-size array of 3 `Int8` elements has the type `[Int8; 3]`.

Variable-size array types have the form `[T]`, where `T` is the element type. For example, the type `[Int16]` specifies a variable-size array of elements that have type `Int16`.

All values in an array must have a type, which is a subtype of the array's element type (`T`).

It is important to understand that arrays are value types and are only ever copied when used as an initial value for a constant or variable, when assigning to a variable, when used as function argument, or when returned from a function call.

`_26

let size = 2

_26

// Invalid: Array-size must be an integer literal

_26

let numbers: [Int; size] = []

_26

_26

// Declare a fixed-sized array of integers

_26

// which always contains exactly two elements.

_26

//

_26

let array: [Int8; 2] = [1, 2]

_26

_26

// Declare a fixed-sized array of fixed-sized arrays of integers.

_26

// The inner arrays always contain exactly three elements,

_26

// the outer array always contains two elements.

_26

//

_26

let arrays: [[Int16; 3]; 2] = [

_26

[1, 2, 3],

_26

[4, 5, 6]

_26

]

_26

_26

// Declare a variable length array of integers

_26

var variableLengthArray: [Int] = []

_26

_26

// Mixing values with different types is possible

_26

// by declaring the expected array type

_26

// with the common supertype of all values.

_26

//

_26

let mixedValues: [AnyStruct] = ["some string", 42]`

Array types are covariant in their element types. For example, `[Int]` is a subtype of `[AnyStruct]`. This is safe because arrays are value types and not reference types.

## Array indexing[​](#array-indexing "Direct link to Array indexing")

To get the element of an array at a specific index, the following indexing syntax can be used: the array is followed by an opening square bracket `[`, the indexing value, and ends with a closing square bracket `]`.

Indexes start at 0 for the first element in the array.

Accessing an element which is out of bounds results in a fatal error at run-time and aborts the program.

`` _14

// Declare an array of integers.

_14

let numbers = [42, 23]

_14

_14

// Get the first number of the array.

_14

//

_14

numbers[0] // is `42`

_14

_14

// Get the second number of the array.

_14

//

_14

numbers[1] // is `23`

_14

_14

// Run-time error: Index 2 is out of bounds, the program aborts.

_14

//

_14

numbers[2] ``

`` _10

// Declare an array of arrays of integers, i.e. the type is `[[Int]]`.

_10

let arrays = [[1, 2], [3, 4]]

_10

_10

// Get the first number of the second array.

_10

//

_10

arrays[1][0] // is `3` ``

To set an element of an array at a specific index, the indexing syntax can be used as well.

`` _12

// Declare an array of integers.

_12

let numbers = [42, 23]

_12

_12

// Change the second number in the array.

_12

//

_12

// NOTE: The declaration `numbers` is constant, which means that

_12

// the *name* is constant, not the *value* – the value, i.e. the array,

_12

// is mutable and can be changed.

_12

//

_12

numbers[1] = 2

_12

_12

// `numbers` is `[42, 2]` ``

## Array fields and functions[​](#array-fields-and-functions "Direct link to Array fields and functions")

Arrays have multiple built-in fields and functions that can be used to get information about and manipulate the contents of the array.

The field `length`, and the functions `concat`, and `contains` are available for both variable-sized and fixed-sized or variable-sized arrays.

* `_10

  let length: Int`

  The number of elements in the array.

  `` _10

  // Declare an array of integers.

  _10

  let numbers = [42, 23, 31, 12]

  _10

  _10

  // Find the number of elements of the array.

  _10

  let length = numbers.length

  _10

  _10

  // `length` is `4` ``
* `_10

  access(all)

  _10

  view fun concat(_ array: T): T`

  Concatenates the parameter `array` to the end of the array the function is called on, but does not modify that array.

  Both arrays must be the same type `T`.

  This function creates a new array whose length is the sum of the length of the array the function is called on and the length of the array given as the parameter.

  `` _12

  // Declare two arrays of integers.

  _12

  let numbers = [42, 23, 31, 12]

  _12

  let moreNumbers = [11, 27]

  _12

  _12

  // Concatenate the array `moreNumbers` to the array `numbers`

  _12

  // and declare a new variable for the result.

  _12

  //

  _12

  let allNumbers = numbers.concat(moreNumbers)

  _12

  _12

  // `allNumbers` is `[42, 23, 31, 12, 11, 27]`

  _12

  // `numbers` is still `[42, 23, 31, 12]`

  _12

  // `moreNumbers` is still `[11, 27]` ``
* `_10

  access(all)

  _10

  view fun contains(_ element: T): Bool`

  Returns true if the given element of type `T` is in the array.

  `` _15

  // Declare an array of integers.

  _15

  let numbers = [42, 23, 31, 12]

  _15

  _15

  // Check if the array contains 11.

  _15

  let containsEleven = numbers.contains(11)

  _15

  // `containsEleven` is `false`

  _15

  _15

  // Check if the array contains 12.

  _15

  let containsTwelve = numbers.contains(12)

  _15

  // `containsTwelve` is `true`

  _15

  _15

  // Invalid: Check if the array contains the string "Kitty".

  _15

  // This results in a type error, as the array only contains integers.

  _15

  //

  _15

  let containsKitty = numbers.contains("Kitty") ``
* `_10

  access(all)

  _10

  view fun firstIndex(of: T): Int?`

  Returns the index of the first element matching the given object in the array, nil if no match. Available if `T` is not resource-kinded and equatable.

  `` _10

  // Declare an array of integers.

  _10

  let numbers = [42, 23, 31, 12]

  _10

  _10

  // Check if the array contains 31

  _10

  let index = numbers.firstIndex(of: 31)

  _10

  // `index` is 2

  _10

  _10

  // Check if the array contains 22

  _10

  let index = numbers.firstIndex(of: 22)

  _10

  // `index` is nil ``
* `_10

  access(all)

  _10

  view fun slice(from: Int, upTo: Int): [T]`

  Returns an array slice of the elements in the given array from start index `from` up to, but not including, the end index `upTo`. This function creates a new array whose length is `upTo - from`. It does not modify the original array. If either of the parameters are out of the bounds of the array, or the indices are invalid (`from > upTo`), then the function will fail.

  `` _11

  let example = [1, 2, 3, 4]

  _11

  _11

  // Create a new slice of part of the original array.

  _11

  let slice = example.slice(from: 1, upTo: 3)

  _11

  // `slice` is now `[2, 3]`

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

  access(all)

  _10

  view fun reverse(): [T]`

  Returns a new array with contents in the reversed order. Available if `T` is not resource-kinded.

  `` _10

  let example = [1, 2, 3, 4]

  _10

  _10

  // Create a new array which is the reverse of the original array.

  _10

  let reversedExample = example.reverse()

  _10

  // `reversedExample` is now `[4, 3, 2, 1]` ``

  `_10

  access(all)

  _10

  view fun reverse(): [T; N]`

  Returns a new fixed-sized array of same size with contents in the reversed order.

  `` _10

  let fixedSizedExample: [String; 3] = ["ABC", "XYZ", "PQR"]

  _10

  _10

  // Create a new array which is the reverse of the original array.

  _10

  let fixedArrayReversedExample = fixedSizedExample.reverse()

  _10

  // `fixedArrayReversedExample` is now `["PQR", "XYZ", "ABC"]` ``
* `_10

  access(all)

  _10

  fun map(_ f: fun(T): U): [U]`

  Returns a new array whose elements are produced by applying the mapper function on each element of the original array. Available if `T` is not resource-kinded.

  `` _18

  let example = [1, 2, 3]

  _18

  let trueForEven =

  _18

  fun (_ x: Int): Bool {

  _18

  return x % 2 == 0

  _18

  }

  _18

  _18

  let mappedExample: [Bool] = example.map(trueForEven)

  _18

  // `mappedExample` is `[False, True, False]`

  _18

  // `example` still remains as `[1, 2, 3]`

  _18

  _18

  // Invalid: Map using a function which accepts a different type.

  _18

  // This results in a type error, as the array contains `Int` values while function accepts

  _18

  // `Int64`.

  _18

  let functionAcceptingInt64 =

  _18

  fun (_ x: Int64): Bool {

  _18

  return x % 2 == 0

  _18

  }

  _18

  let invalidMapFunctionExample = example.map(functionAcceptingInt64) ``

  The `map` function is also available for fixed-sized arrays:

  `_10

  access(all)

  _10

  fun map(_ f: fun(T): U): [U; N]`

  Returns a new fixed-sized array whose elements are produced by applying the mapper function on each element of the original array. Available if `T` is not resource-kinded.

  `` _18

  let fixedSizedExample: [String; 3] = ["ABC", "XYZYX", "PQR"]

  _18

  let lengthOfString =

  _18

  fun (_ x: String): Int {

  _18

  return x.length

  _18

  }

  _18

  _18

  let fixedArrayMappedExample = fixedSizedExample.map(lengthOfString)

  _18

  // `fixedArrayMappedExample` is now `[3, 5, 3]`

  _18

  // `fixedSizedExample` still remains as ["ABC", "XYZYX", "PQR"]

  _18

  _18

  // Invalid: Map using a function which accepts a different type.

  _18

  // This results in a type error, as the array contains `String` values while function accepts

  _18

  // `Bool`.

  _18

  let functionAcceptingBool =

  _18

  fun (_ x: Bool): Int {

  _18

  return 0

  _18

  }

  _18

  let invalidMapFunctionExample = fixedSizedExample.map(functionAcceptingBool) ``
* `_10

  access(all)

  _10

  view fun filter(_ f: view fun(T): Bool): [T]`

  Returns a new array whose elements are filtered by applying the filter function on each element of the original array. Available if `T` is not resource-kinded.

  `` _18

  let example = [1, 2, 3]

  _18

  let trueForEven =

  _18

  fun (_ x: Int): Bool {

  _18

  return x % 2 == 0

  _18

  }

  _18

  _18

  let filteredExample: [Int] = example.filter(trueForEven)

  _18

  // `filteredExample` is `[2]`

  _18

  // `example` still remains as `[1, 2, 3]`

  _18

  _18

  // Invalid: Filter using a function which accepts a different type.

  _18

  // This results in a type error, as the array contains `Int` values while function accepts

  _18

  // `Int64`.

  _18

  let functionAcceptingInt64 =

  _18

  fun (_ x: Int64): Bool {

  _18

  return x % 2 == 0

  _18

  }

  _18

  let invalidFilterFunctionExample = example.filter(functionAcceptingInt64) ``

  The `filter` function is also available for fixed-sized arrays:

  `_10

  access(all)

  _10

  view fun filter(_ f: view fun(T): Bool): [T]`

  Returns a new **variable-sized** array whose elements are filtered by applying the filter function on each element of the original array. Available if `T` is not resource-kinded.

  `` _18

  let fixedSizedExample: [String; 3] = ["AB", "XYZYX", "PQR"]

  _18

  let lengthOfStringGreaterThanTwo =

  _18

  fun (_ x: String): Bool {

  _18

  return x.length > 2

  _18

  }

  _18

  _18

  let fixedArrayFilteredExample = fixedSizedExample.filter(lengthOfStringGreaterThanTwo)

  _18

  // `fixedArrayFilteredExample` is `["XYZYX", "PQR"]`

  _18

  // `fixedSizedExample` still remains as ["AB", "XYZYX", "PQR"]

  _18

  _18

  // Invalid: Filter using a function which accepts a different type.

  _18

  // This results in a type error, as the array contains `String` values while function accepts

  _18

  // `Bool`.

  _18

  let functionAcceptingBool =

  _18

  fun (_ x: Bool): Bool {

  _18

  return True

  _18

  }

  _18

  let invalidFilterFunctionExample = fixedSizedExample.filter(functionAcceptingBool) ``

## Variable-size array functions[​](#variable-size-array-functions "Direct link to Variable-size array functions")

The following functions can only be used on variable-sized arrays. It is invalid to use one of these functions on a fixed-sized array.

* `_10

  access(Mutate | Insert)

  _10

  fun append(_ element: T): Void`

  Adds the new element `element` of type `T` to the end of the array.

  The new element must be the same type as all the other elements in the array.

  This function [mutates](/docs/language/access-control) the array.

  `` _10

  // Declare an array of integers.

  _10

  let numbers = [42, 23, 31, 12]

  _10

  _10

  // Add a new element to the array.

  _10

  numbers.append(20)

  _10

  // `numbers` is now `[42, 23, 31, 12, 20]`

  _10

  _10

  // Invalid: The parameter has the wrong type `String`.

  _10

  numbers.append("SneakyString") ``
* `_10

  access(Mutate | Insert)

  _10

  fun appendAll(_ array: T): Void`

  Adds all the elements from `array` to the end of the array the function is called on.

  Both arrays must be the same type `T`.

  This function [mutates](/docs/language/access-control) the array.

  `` _10

  // Declare an array of integers.

  _10

  let numbers = [42, 23]

  _10

  _10

  // Add new elements to the array.

  _10

  numbers.appendAll([31, 12, 20])

  _10

  // `numbers` is now `[42, 23, 31, 12, 20]`

  _10

  _10

  // Invalid: The parameter has the wrong type `[String]`.

  _10

  numbers.appendAll(["Sneaky", "String"]) ``
* `_10

  access(Mutate | Insert)

  _10

  fun insert(at: Int, _ element: T): Void`

  Inserts the new element `element` of type `T` at the given `index` of the array.

  The new element must be of the same type as the other elements in the array.

  The `index` must be within the bounds of the array. If the index is outside the bounds, the program aborts.

  The existing element at the supplied index is not overwritten.

  All the elements after the new inserted element are shifted to the right by one.

  This function [mutates](/docs/language/access-control) the array.

  `` _10

  // Declare an array of integers.

  _10

  let numbers = [42, 23, 31, 12]

  _10

  _10

  // Insert a new element at position 1 of the array.

  _10

  numbers.insert(at: 1, 20)

  _10

  // `numbers` is now `[42, 20, 23, 31, 12]`

  _10

  _10

  // Run-time error: Out of bounds index, the program aborts.

  _10

  numbers.insert(at: 12, 39) ``
* `_10

  access(Mutate | Remove)

  _10

  fun remove(at: Int): T`

  Removes the element at the given `index` from the array and returns it.

  The `index` must be within the bounds of the array. If the index is outside the bounds, the program aborts.

  This function [mutates](/docs/language/access-control) the array.

  `` _10

  // Declare an array of integers.

  _10

  let numbers = [42, 23, 31]

  _10

  _10

  // Remove element at position 1 of the array.

  _10

  let twentyThree = numbers.remove(at: 1)

  _10

  // `numbers` is now `[42, 31]`

  _10

  // `twentyThree` is `23`

  _10

  _10

  // Run-time error: Out of bounds index, the program aborts.

  _10

  numbers.remove(at: 19) ``
* `_10

  access(Mutate | Remove)

  _10

  fun removeFirst(): T`

  Removes the first element from the array and returns it.

  The array must not be empty. If the array is empty, the program aborts.

  This function [mutates](/docs/language/access-control) the array.

  `` _15

  // Declare an array of integers.

  _15

  let numbers = [42, 23]

  _15

  _15

  // Remove the first element of the array.

  _15

  let fortytwo = numbers.removeFirst()

  _15

  // `numbers` is now `[23]`

  _15

  // `fortywo` is `42`

  _15

  _15

  // Remove the first element of the array.

  _15

  let twentyThree = numbers.removeFirst()

  _15

  // `numbers` is now `[]`

  _15

  // `twentyThree` is `23`

  _15

  _15

  // Run-time error: The array is empty, the program aborts.

  _15

  numbers.removeFirst() ``
* `_10

  access(Mutate | Remove)

  _10

  fun removeLast(): T`

  Removes the last element from the array and returns it.

  The array must not be empty. If the array is empty, the program aborts.

  This function [mutates](/docs/language/access-control) the array.

  `` _15

  // Declare an array of integers.

  _15

  let numbers = [42, 23]

  _15

  _15

  // Remove the last element of the array.

  _15

  let twentyThree = numbers.removeLast()

  _15

  // `numbers` is now `[42]`

  _15

  // `twentyThree` is `23`

  _15

  _15

  // Remove the last element of the array.

  _15

  let fortyTwo = numbers.removeLast()

  _15

  // `numbers` is now `[]`

  _15

  // `fortyTwo` is `42`

  _15

  _15

  // Run-time error: The array is empty, the program aborts.

  _15

  numbers.removeLast() ``
* `_10

  access(all)

  _10

  fun toConstantSized<[T; N]>(): [T; N]?`

  Converts a variable-sized array to a constant-sized array if the number of elements matches the target size `N` and the original variable-sized array has type `T`. Available if `T` is not resource-kinded.

  Returns nil if the number of elements does not match the target size `N`.

  `_10

  // Declare an array of integers.

  _10

  let numbers = [42, 23]

  _10

  _10

  // Change to a constant-sized array

  _10

  let numbersConst = numbers.toConstantSized<[Int; 2]>()

  _10

  // numbersConst has the type [Int; 2]?`

## Constant-size array functions[​](#constant-size-array-functions "Direct link to Constant-size array functions")

* `_10

  access(all)

  _10

  fun toVariableSized(): [T]`

  Converts a constant-sized array to a variable-sized array of the same type `T`. Available if `T` is not resource-kinded.

  `_10

  // Declare an array of integers.

  _10

  let numbers: [Int16; 3] = [1, 2, 3]

  _10

  _10

  // Change to a constant-sized array

  _10

  let numbersVar = numbers.toVariableSized()

  _10

  // numbersVar has the type [Int]`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/arrays.md)

[Previous

Strings and Characters](/docs/language/values-and-types/strings-and-characters)[Next

Dictionaries](/docs/language/values-and-types/dictionaries)

###### Rate this page

😞😐😊

* [Array types](#array-types)
* [Array indexing](#array-indexing)
* [Array fields and functions](#array-fields-and-functions)
* [Variable-size array functions](#variable-size-array-functions)
* [Constant-size array functions](#constant-size-array-functions)