# Source: https://cadence-lang.org/docs/language/control-flow

Control Flow | Cadence



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
* Control Flow

On this page

# Control Flow

Control flow statements control the flow of execution in a function.

## Conditional branching: if-statement[​](#conditional-branching-if-statement "Direct link to Conditional branching: if-statement")

If-statements allow a certain piece of code to be executed only when a given condition is true.

The if-statement starts with the `if` keyword, followed by the condition,
and the code that should be executed if the condition is true
inside opening and closing braces.
The condition expression must be boolean.
The braces are required and not optional.
Parentheses around the condition are optional.

`_13

let a = 0

_13

var b = 0

_13

_13

if a == 0 {

_13

b = 1

_13

}

_13

_13

// Parentheses can be used around the condition, but are not required.

_13

if (a != 0) {

_13

b = 2

_13

}

_13

_13

// `b` is `1``

An additional, optional else-clause can be added to execute another piece of code
when the condition is false.
The else-clause is introduced by the `else` keyword followed by braces
that contain the code that should be executed.

`_10

let a = 0

_10

var b = 0

_10

_10

if a == 1 {

_10

b = 1

_10

} else {

_10

b = 2

_10

}

_10

_10

// `b` is `2``

The else-clause can contain another if-statement, i.e., if-statements can be chained together.
In this case the braces can be omitted.

`_22

let a = 0

_22

var b = 0

_22

_22

if a == 1 {

_22

b = 1

_22

} else if a == 2 {

_22

b = 2

_22

} else {

_22

b = 3

_22

}

_22

_22

// `b` is `3`

_22

_22

if a == 1 {

_22

b = 1

_22

} else {

_22

if a == 0 {

_22

b = 2

_22

}

_22

}

_22

_22

// `b` is `2``

## Optional Binding[​](#optional-binding "Direct link to Optional Binding")

Optional binding allows getting the value inside an optional.
It is a variant of the if-statement.

If the optional contains a value, the first branch is executed
and a temporary constant or variable is declared and set to the value contained in the optional;
otherwise, the else branch (if any) is executed.

Optional bindings are declared using the `if` keyword like an if-statement,
but instead of the boolean test value, it is followed by the `let` or `var` keywords,
to either introduce a constant or variable, followed by a name,
the equal sign (`=`), and the optional value.

`_10

let maybeNumber: Int? = 1

_10

_10

if let number = maybeNumber {

_10

// This branch is executed as `maybeNumber` is not `nil`.

_10

// The constant `number` is `1` and has type `Int`.

_10

} else {

_10

// This branch is *not* executed as `maybeNumber` is not `nil`

_10

}`

`_10

let noNumber: Int? = nil

_10

_10

if let number = noNumber {

_10

// This branch is *not* executed as `noNumber` is `nil`.

_10

} else {

_10

// This branch is executed as `noNumber` is `nil`.

_10

// The constant `number` is *not* available.

_10

}`

## Switch[​](#switch "Direct link to Switch")

Switch-statements compare a value against several possible values of the same type, in order.
When an equal value is found, the associated block of code is executed.

The switch-statement starts with the `switch` keyword, followed by the tested value,
followed by the cases inside opening and closing braces.
The test expression must be equatable.
The braces are required and not optional.

Each case is a separate branch of code execution
and starts with the `case` keyword,
followed by a possible value, a colon (`:`),
and the block of code that should be executed
if the case's value is equal to the tested value.

The block of code associated with a switch case
[does not implicitly fall through](#no-implicit-fallthrough),
and must contain at least one statement.
Empty blocks are invalid.

An optional default case may be given by using the `default` keyword.
The block of code of the default case is executed
when none of the previous case tests succeeded.
It must always appear last.

`_22

fun word(_ n: Int): String {

_22

// Test the value of the parameter `n`

_22

switch n {

_22

case 1:

_22

// If the value of variable `n` is equal to `1`,

_22

// then return the string "one"

_22

return "one"

_22

case 2:

_22

// If the value of variable `n` is equal to `2`,

_22

// then return the string "two"

_22

return "two"

_22

default:

_22

// If the value of variable `n` is neither equal to `1` nor to `2`,

_22

// then return the string "other"

_22

return "other"

_22

}

_22

}

_22

_22

word(1) // returns "one"

_22

word(2) // returns "two"

_22

word(3) // returns "other"

_22

word(4) // returns "other"`

### Duplicate cases[​](#duplicate-cases "Direct link to Duplicate cases")

Cases are tested in order, so if a case is duplicated,
the block of code associated with the first case that succeeds is executed.

`_20

fun test(_ n: Int): String {

_20

// Test the value of the parameter `n`

_20

switch n {

_20

case 1:

_20

// If the value of variable `n` is equal to `1`,

_20

// then return the string "one"

_20

return "one"

_20

case 1:

_20

// If the value of variable `n` is equal to `1`,

_20

// then return the string "also one".

_20

// This is a duplicate case for the one above.

_20

return "also one"

_20

default:

_20

// If the value of variable `n` is neither equal to `1` nor to `2`,

_20

// then return the string "other"

_20

return "other"

_20

}

_20

}

_20

_20

word(1) // returns "one", not "also one"`

### `break`[​](#break "Direct link to break")

The block of code associated with a switch case may contain a `break` statement.
It ends the execution of the switch statement immediately
and transfers control to the code after the switch statement

### No Implicit Fallthrough[​](#no-implicit-fallthrough "Direct link to No Implicit Fallthrough")

Unlike switch statements in some other languages,
switch statements in Cadence do not "fall through":
execution of the switch statement finishes as soon as the block of code
associated with the first matching case is completed.
No explicit `break` statement is required.

This makes the switch statement safer and easier to use,
avoiding the accidental execution of more than one switch case.

Some other languages implicitly fall through
to the block of code associated with the next case,
so it is common to write cases with an empty block
to handle multiple values in the same way.

To prevent developers from writing switch statements
that assume this behaviour, blocks must have at least one statement.
Empty blocks are invalid.

`_27

fun words(_ n: Int): [String] {

_27

// Declare a variable named `result`, an array of strings,

_27

// which stores the result

_27

let result: [String] = []

_27

_27

// Test the value of the parameter `n`

_27

switch n {

_27

case 1:

_27

// If the value of variable `n` is equal to `1`,

_27

// then append the string "one" to the result array

_27

result.append("one")

_27

case 2:

_27

// If the value of variable `n` is equal to `2`,

_27

// then append the string "two" to the result array

_27

result.append("two")

_27

default:

_27

// If the value of variable `n` is neither equal to `1` nor to `2`,

_27

// then append the string "other" to the result array

_27

result.append("other")

_27

}

_27

return result

_27

}

_27

_27

words(1) // returns `["one"]`

_27

words(2) // returns `["two"]`

_27

words(3) // returns `["other"]`

_27

words(4) // returns `["other"]``

## Looping[​](#looping "Direct link to Looping")

### while-statement[​](#while-statement "Direct link to while-statement")

While-statements allow a certain piece of code to be executed repeatedly,
as long as a condition remains true.

The while-statement starts with the `while` keyword, followed by the condition,
and the code that should be repeatedly
executed if the condition is true inside opening and closing braces.
The condition must be boolean and the braces are required.

The while-statement will first evaluate the condition.
If it is true, the piece of code is executed and the evaluation of the condition is repeated.
If the condition is false, the piece of code is not executed
and the execution of the whole while-statement is finished.
Thus, the piece of code is executed zero or more times.

`_10

var a = 0

_10

while a < 5 {

_10

a = a + 1

_10

}

_10

_10

// `a` is `5``

### For-in statement[​](#for-in-statement "Direct link to For-in statement")

For-in statements allow a certain piece of code to be executed repeatedly for
each element in an array.

The for-in statement starts with the `for` keyword, followed by the name of
the element that is used in each iteration of the loop,
followed by the `in` keyword, and then followed by the array
that is being iterated through in the loop.

Then, the code that should be repeatedly executed in each iteration of the loop
is enclosed in curly braces.

If there are no elements in the data structure, the code in the loop will not
be executed at all. Otherwise, the code will execute as many times
as there are elements in the array.

`_11

let array = ["Hello", "World", "Foo", "Bar"]

_11

_11

for element in array {

_11

log(element)

_11

}

_11

_11

// The loop would log:

_11

// "Hello"

_11

// "World"

_11

// "Foo"

_11

// "Bar"`

Optionally, developers may include an additional variable preceding the element name,
separated by a comma.
When present, this variable contains the current
index of the array being iterated through
during each repeated execution (starting from 0).

`_11

let array = ["Hello", "World", "Foo", "Bar"]

_11

_11

for index, element in array {

_11

log(index)

_11

}

_11

_11

// The loop would log:

_11

// 0

_11

// 1

_11

// 2

_11

// 3`

To iterate over a dictionary's entries (keys and values),
use a for-in loop over the dictionary's keys and get the value for each key:

`_12

let dictionary = {"one": 1, "two": 2}

_12

for key in dictionary.keys {

_12

let value = dictionary[key]!

_12

log(key)

_12

log(value)

_12

}

_12

_12

// The loop would log:

_12

// "one"

_12

// 1

_12

// "two"

_12

// 2`

Alternatively, dictionaries carry a method `forEachKey` that avoids allocating an intermediate array for keys:

`_10

let dictionary = {"one": 1, "two": 2, "three": 3}

_10

dictionary.forEachKey(fun (key: String): Bool {

_10

let value = dictionary[key]

_10

log(key)

_10

log(value)

_10

_10

return key != "two" // stop iteration if this returns false

_10

})`

### Ranges in Loops[​](#ranges-in-loops "Direct link to Ranges in Loops")

An [`InclusiveRange` value](#../values-and-types/InclusiveRange) can be used in a for-in statement in place of an array or dictionary. In this case,
the loop will iterate over all the values contained in the range, beginning with `range.start` and ending with `range.end`. E.g.

`_10

let range: InclusiveRange<UInt> = InclusiveRange(1, 100, step: 2)

_10

var elements : [UInt] = []

_10

for element in range {

_10

elements.append(element)

_10

}

_10

// after this loop, `elements` contains all the odd integers from 1 to 99`

Note that in this example, even though `100` is the end of the `range`, it is not included in the loop because it cannot be reached with the given `start` and `step`.

The above loop is equivalent to:

`_10

let range: InclusiveRange<UInt> = InclusiveRange(1, 100, step: 2)

_10

var elements : [UInt] = []

_10

var index = range.start

_10

while index <= range.end {

_10

elements.append(element)

_10

index = index + range.step

_10

}

_10

// after this loop, `elements` contains all the odd integers from 1 to 99`

In general, a for-in loop over an increasing range (a positive `step`) is equivalent to:

`_10

var index = range.start

_10

while index <= range.end {

_10

// loop body

_10

index = index + range.step

_10

}`

While a for-in loop over a decreasing range (a negative `step`) is equivalent to:

`_10

var index = range.start

_10

while index >= range.end {

_10

// loop body

_10

index = index + range.step // `range.step` here is negative, so this decreases `index`

_10

}`

Both can be equivalently rewritten to:

`_10

var index = range.start

_10

while range.contains(index) {

_10

// loop body

_10

index = index + range.step

_10

}`

### `continue` and `break`[​](#continue-and-break "Direct link to continue-and-break")

In for-loops and while-loops, the `continue` statement can be used to stop
the current iteration of a loop and start the next iteration.

`_22

var i = 0

_22

var x = 0

_22

while i < 10 {

_22

i = i + 1

_22

if i < 3 {

_22

continue

_22

}

_22

x = x + 1

_22

}

_22

// `x` is `8`

_22

_22

_22

let array = [2, 2, 3]

_22

var sum = 0

_22

for element in array {

_22

if element == 2 {

_22

continue

_22

}

_22

sum = sum + element

_22

}

_22

_22

// `sum` is `3``

The `break` statement can be used to stop the execution
of a for-loop or a while-loop.

`_20

var x = 0

_20

while x < 10 {

_20

x = x + 1

_20

if x == 5 {

_20

break

_20

}

_20

}

_20

// `x` is `5`

_20

_20

_20

let array = [1, 2, 3]

_20

var sum = 0

_20

for element in array {

_20

if element == 2 {

_20

break

_20

}

_20

sum = sum + element

_20

}

_20

_20

// `sum` is `1``

## Immediate function return: return-statement[​](#immediate-function-return-return-statement "Direct link to Immediate function return: return-statement")

The return-statement causes a function to return immediately,
i.e., any code after the return-statement is not executed.
The return-statement starts with the `return` keyword
and is followed by an optional expression that should be the return value of the function call.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/control-flow.md)

[Previous

Functions](/docs/language/functions)[Next

Scope](/docs/language/scope)

###### Rate this page

😞😐😊

* [Conditional branching: if-statement](#conditional-branching-if-statement)
* [Optional Binding](#optional-binding)
* [Switch](#switch)
  + [Duplicate cases](#duplicate-cases)
  + [`break`](#break)
  + [No Implicit Fallthrough](#no-implicit-fallthrough)
* [Looping](#looping)
  + [while-statement](#while-statement)
  + [For-in statement](#for-in-statement)
  + [Ranges in Loops](#ranges-in-loops)
  + [`continue` and `break`](#continue-and-break)
* [Immediate function return: return-statement](#immediate-function-return-return-statement)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.