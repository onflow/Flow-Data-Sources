# Source: https://cadence-lang.org/docs/language/functions

Functions | Cadence



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
* Functions

On this page

# Functions

Functions are sequences of statements that perform a specific task.
Functions have parameters (inputs) and an optional return value (output).
Functions are typed: the function type consists of the parameter types and the return type.

Functions are values, i.e., they can be assigned to constants and variables,
and can be passed as arguments to other functions.
This behavior is often called "first-class functions".

## Function Declarations[​](#function-declarations "Direct link to Function Declarations")

Functions can be declared by using the `fun` keyword, followed by the name of the declaration,
the parameters, the optional return type,
and the code that should be executed when the function is called.

The parameters need to be enclosed in parentheses.
The return type, if any, is separated from the parameters by a colon (`:`).
The function code needs to be enclosed in opening and closing braces.

Each parameter must have a name, which is the name that the argument value
will be available as within the function.

An additional argument label can be provided to require function calls to use the label
to provide an argument value for the parameter.

Argument labels make code more explicit and readable.
For example, they avoid confusion about the order of arguments
when there are multiple arguments that have the same type.

Argument labels should be named so they make sense from the perspective of the function call.

Argument labels precede the parameter name.
The special argument label `_` indicates
that a function call can omit the argument label.
If no argument label is declared in the function declaration,
the parameter name is the argument label of the function declaration,
and function calls must use the parameter name as the argument label.

Each parameter needs to have a type annotation,
which follows the parameter name after a colon.

Function calls may provide arguments for parameters
which are subtypes of the parameter types.

There is **no** support for optional parameters,
i.e. default values for parameters,
and variadic functions,
i.e. functions that take an arbitrary amount of arguments.

`_15

// Declare a function named `double`, which multiples a number by two.

_15

//

_15

// The special argument label _ is specified for the parameter,

_15

// so no argument label has to be provided in a function call.

_15

//

_15

fun double(_ x: Int): Int {

_15

return x * 2

_15

}

_15

_15

// Call the function named `double` with the value 4 for the first parameter.

_15

//

_15

// The argument label can be omitted in the function call as the declaration

_15

// specifies the special argument label _ for the parameter.

_15

//

_15

double(2) // is `4``

It is possible to require argument labels for some parameters,
and not require argument labels for other parameters.

`_38

// Declare a function named `clamp`. The function takes an integer value,

_38

// the lower limit, and the upper limit. It returns an integer between

_38

// the lower and upper limit.

_38

//

_38

// For the first parameter the special argument label _ is used,

_38

// so no argument label has to be given for it in a function call.

_38

//

_38

// For the second and third parameter no argument label is given,

_38

// so the parameter names are the argument labels, i.e., the parameter names

_38

// have to be given as argument labels in a function call.

_38

//

_38

fun clamp(_ value: Int, min: Int, max: Int): Int {

_38

if value > max {

_38

return max

_38

}

_38

_38

if value < min {

_38

return min

_38

}

_38

_38

return value

_38

}

_38

_38

// Declare a constant which has the result of a call to the function

_38

// named `clamp` as its initial value.

_38

//

_38

// For the first argument no label is given, as it is not required by

_38

// the function declaration (the special argument label `_` is specified).

_38

//

_38

// For the second and this argument the labels must be provided,

_38

// as the function declaration does not specify the special argument label `_`

_38

// for these two parameters.

_38

//

_38

// As the function declaration also does not specify argument labels

_38

// for these parameters, the parameter names must be used as argument labels.

_38

//

_38

let clamped = clamp(123, min: 0, max: 100)

_38

// `clamped` is `100``

`_51

// Declare a function named `send`, which transfers an amount

_51

// from one account to another.

_51

//

_51

// The implementation is omitted for brevity.

_51

//

_51

// The first two parameters of the function have the same type, so there is

_51

// a potential that a function call accidentally provides arguments in

_51

// the wrong order.

_51

//

_51

// While the parameter names `senderAddress` and `receiverAddress`

_51

// are descriptive inside the function, they might be too verbose

_51

// to require them as argument labels in function calls.

_51

//

_51

// For this reason the shorter argument labels `from` and `to` are specified,

_51

// which still convey the meaning of the two parameters without being overly

_51

// verbose.

_51

//

_51

// The name of the third parameter, `amount`, is both meaningful inside

_51

// the function and also in a function call, so no argument label is given,

_51

// and the parameter name is required as the argument label in a function call.

_51

//

_51

fun send(from senderAddress: Address, to receivingAddress: Address, amount: Int) {

_51

// The function code is omitted for brevity.

_51

// ...

_51

}

_51

_51

// Declare a constant which refers to the sending account's address.

_51

//

_51

// The initial value is omitted for brevity.

_51

//

_51

let sender: Address = // ...

_51

_51

// Declare a constant which refers to the receiving account's address.

_51

//

_51

// The initial value is omitted for brevity.

_51

//

_51

let receiver: Address = // ...

_51

_51

// Call the function named `send`.

_51

//

_51

// The function declaration requires argument labels for all parameters,

_51

// so they need to be provided in the function call.

_51

//

_51

// This avoids ambiguity. For example, in some languages (like C) it is

_51

// a convention to order the parameters so that the receiver occurs first,

_51

// followed by the sender. In other languages, it is common to have

_51

// the sender be the first parameter, followed by the receiver.

_51

//

_51

// Here, the order is clear – send an amount from an account to another account.

_51

//

_51

send(from: sender, to: receiver, amount: 100)`

The order of the arguments in a function call must
match the order of the parameters in the function declaration.

`_10

// Declare a function named `test`, which accepts two parameters, named `first` and `second`

_10

//

_10

fun test(first: Int, second: Int) {

_10

// ...

_10

}

_10

_10

// Invalid: the arguments are provided in the wrong order,

_10

// even though the argument labels are provided correctly.

_10

//

_10

test(second: 1, first: 2)`

Functions can be nested,
i.e., the code of a function may declare further functions.

`_14

// Declare a function which multiplies a number by two, and adds one.

_14

//

_14

fun doubleAndAddOne(_ x: Int): Int {

_14

_14

// Declare a nested function which multiplies a number by two.

_14

//

_14

fun double(_ x: Int) {

_14

return x * 2

_14

}

_14

_14

return double(x) + 1

_14

}

_14

_14

doubleAndAddOne(2) // is `5``

Functions do not support overloading.

## Function Expressions[​](#function-expressions "Direct link to Function Expressions")

Functions can be also used as expressions.
The syntax is the same as for function declarations,
except that function expressions have no name, i.e., they are anonymous.

`_10

// Declare a constant named `double`, which has a function as its value.

_10

//

_10

// The function multiplies a number by two when it is called.

_10

//

_10

// This function's type is `fun (Int): Int`.

_10

//

_10

let double =

_10

fun (_ x: Int): Int {

_10

return x * 2

_10

}`

## Function Calls[​](#function-calls "Direct link to Function Calls")

Functions can be called (invoked). Function calls
need to provide exactly as many argument values as the function has parameters.

`_15

fun double(_ x: Int): Int {

_15

return x * 2

_15

}

_15

_15

// Valid: the correct amount of arguments is provided.

_15

//

_15

double(2) // is `4`

_15

_15

// Invalid: too many arguments are provided.

_15

//

_15

double(2, 3)

_15

_15

// Invalid: too few arguments are provided.

_15

//

_15

double()`

## Function Types[​](#function-types "Direct link to Function Types")

Function types consist of the `fun` keyword, the function's parameter types
and the function's return type.

The parameter types need to be enclosed in parentheses,
followed by a colon (`:`), and end with the return type.

Optionally, the `view` keyword can be included before the `fun` keyword to indicate that the type is that of a `view` function.

`_10

// Declare a function named `add`, with the function type `fun(Int, Int): Int`.

_10

//

_10

fun add(a: Int, b: Int): Int {

_10

return a + b

_10

}`

`_10

// Declare a constant named `add`, with the function type `fun(Int, Int): Int`

_10

//

_10

let add: fun(Int, Int): Int =

_10

fun (a: Int, b: Int): Int {

_10

return a + b

_10

}`

If the function has no return type, it implicitly has the return type `Void`.

`_10

// Declare a constant named `doNothing`, which is a function

_10

// that takes no parameters and returns nothing.

_10

//

_10

let doNothing: fun(): Void =

_10

fun () {}`

Parentheses also control precedence.
For example, a function type `fun(Int): fun(): Int` is the type
for a function which accepts one argument with type `Int`,
and which returns another function,
that takes no arguments and returns an `Int`.

The type `[fun(Int): Int; 2]` specifies an array type of two functions,
which accept one integer and return one integer.

Argument labels are not part of the function type.
This has the advantage that functions with different argument labels,
potentially written by different authors are compatible
as long as the parameter types and the return type match.
It has the disadvantage that function calls to plain function values,
cannot accept argument labels.

`_36

// Declare a function which takes one argument that has type `Int`.

_36

// The function has type `fun(Int): Void`.

_36

//

_36

fun foo1(x: Int) {}

_36

_36

// Call function `foo1`. This requires an argument label.

_36

foo1(x: 1)

_36

_36

// Declare another function which takes one argument that has type `Int`.

_36

// The function also has type `fun(Int): Void`.

_36

//

_36

fun foo2(y: Int) {}

_36

_36

// Call function `foo2`. This requires an argument label.

_36

foo2(y: 2)

_36

_36

// Declare a variable which has type `fun(Int): Void` and use `foo1`

_36

// as its initial value.

_36

//

_36

var someFoo: fun(Int): Void = foo1

_36

_36

// Call the function assigned to variable `someFoo`.

_36

// This is valid as the function types match.

_36

// This does neither require nor allow argument labels.

_36

//

_36

someFoo(3)

_36

_36

// Assign function `foo2` to variable `someFoo`.

_36

// This is valid as the function types match.

_36

//

_36

someFoo = foo2

_36

_36

// Call the function assigned to variable `someFoo`.

_36

// This does neither require nor allow argument labels.

_36

//

_36

someFoo(4)`

## Closures[​](#closures "Direct link to Closures")

A function may refer to variables and constants of its outer scopes
in which it is defined.
It is called a closure, because
it is closing over those variables and constants.
A closure can read from the variables and constants
and assign to the variables it refers to.

`_17

// Declare a function named `makeCounter` which returns a function that

_17

// each time when called, returns the next integer, starting at 1.

_17

//

_17

fun makeCounter(): fun(): Int {

_17

var count = 0

_17

return fun (): Int {

_17

// NOTE: read from and assign to the non-local variable

_17

// `count`, which is declared in the outer function.

_17

//

_17

count = count + 1

_17

return count

_17

}

_17

}

_17

_17

let test = makeCounter()

_17

test() // is `1`

_17

test() // is `2``

## Argument Passing Behavior[​](#argument-passing-behavior "Direct link to Argument Passing Behavior")

When arguments are passed to a function, they are copied.
Therefore, values that are passed into a function
are unchanged in the caller's scope when the function returns.
This behavior is known as
[call-by-value](https://en.wikipedia.org/w/index.php?title=Evaluation_strategy&oldid=896280571#Call_by_value).

`_16

// Declare a function that changes the first two elements

_16

// of an array of integers.

_16

//

_16

fun change(_ numbers: [Int]) {

_16

// Change the elements of the passed in array.

_16

// The changes are only local, as the array was copied.

_16

//

_16

numbers[0] = 1

_16

numbers[1] = 2

_16

// `numbers` is `[1, 2]`

_16

}

_16

_16

let numbers = [0, 1]

_16

_16

change(numbers)

_16

// `numbers` is still `[0, 1]``

Parameters are constant, i.e., it is not allowed to assign to them.

`_10

fun test(x: Int) {

_10

// Invalid: cannot assign to a parameter (constant)

_10

//

_10

x = 2

_10

}`

## Function Preconditions and Postconditions[​](#function-preconditions-and-postconditions "Direct link to Function Preconditions and Postconditions")

Functions may have preconditions and may have postconditions.
Preconditions and postconditions can be used to restrict the inputs (values for parameters)
and output (return value) of a function.

Preconditions must be true right before the execution of the function.
Preconditions are part of the function and introduced by the `pre` keyword,
followed by the condition block.

Postconditions must be true right after the execution of the function.
Postconditions are part of the function and introduced by the `post` keyword,
followed by the condition block.
Postconditions may only occur after preconditions, if any.

A conditions block consists of one or more conditions.
Conditions are expressions evaluating to a boolean.

Conditions may be written on separate lines,
or multiple conditions can be written on the same line,
separated by a semicolon.
This syntax follows the syntax for [statements](/docs/language/syntax#semicolons).

Following each condition, an optional description can be provided after a colon.
The condition description is used as an error message when the condition fails.

In postconditions, the special constant `result` refers to the result of the function.

`_27

fun factorial(_ n: Int): Int {

_27

pre {

_27

// Require the parameter `n` to be greater than or equal to zero.

_27

//

_27

n >= 0:

_27

"factorial is only defined for integers greater than or equal to zero"

_27

}

_27

post {

_27

// Ensure the result will be greater than or equal to 1.

_27

//

_27

result >= 1:

_27

"the result must be greater than or equal to 1"

_27

}

_27

_27

if n < 1 {

_27

return 1

_27

}

_27

_27

return n * factorial(n - 1)

_27

}

_27

_27

factorial(5) // is `120`

_27

_27

// Run-time error: The given argument does not satisfy

_27

// the precondition `n >= 0` of the function, the program aborts.

_27

//

_27

factorial(-2)`

In postconditions, the special function `before` can be used
to get the value of an expression just before the function is called.

`_12

var n = 0

_12

_12

fun incrementN() {

_12

post {

_12

// Require the new value of `n` to be the old value of `n`, plus one.

_12

//

_12

n == before(n) + 1:

_12

"n must be incremented by 1"

_12

}

_12

_12

n = n + 1

_12

}`

Both preconditions and postconditions are considered [`view` contexts](#view-functions);
any operations that are not legal in functions with `view` annotations are also not allowed in conditions.
In particular, this means that if you wish to call a function in a condition, that function must be `view`.

## View Functions[​](#view-functions "Direct link to View Functions")

Functions can be annotated as `view` to indicate that they do not modify any external state or any account state.
A `view` annotation can be added to the beginning of a function declaration or expression like so:

`_13

access(all)

_13

view fun foo(): Void {}

_13

_13

let x = view fun(): Void {}

_13

_13

access(all)

_13

struct S {

_13

_13

access(all)

_13

view fun foo(): Void {}

_13

_13

view init()

_13

}`

All functions that do not have a `view` annotation are considered non-view,
and cannot be called inside of `view` contexts,
like inside of a `view` function or in a precondition or postcondition.

Function types can also have `view` annotations,
to be placed after the opening parenthesis but before the parameter list.
So, for example, these are valid types:

`_10

let f: view fun (Int): Int = ...

_10

let h: view fun (): (view fun (): Void) = ...`

Any function types without a `view` annotation will be considered non-view.

Functions are covariant with respect to `view` annotations,
so a `view` function is a subtype of an non-view function with the same parameters and return types.
So, the following declarations would typecheck:

`_10

let a: view fun (): Void = view fun() {}

_10

let b: fun (): Void = view fun() {}

_10

let c: fun (): Void = fun() {}

_10

let d: fun(view fun(): Void): Void = fun (x: fun(): Void) {} // contravariance`

while these would not:

`_10

let x: view fun (): Void = fun() {}

_10

let y: fun(fun(): Void): Void = fun(f: view fun(): Void) {} // contravariance`

The operations that are not permitted in `view` contexts are:

* Calling a non-view function (including any functions that modify account state or storage like `save` or `load`)
* Writing to or modifying any resources
* Writing to or modifying any references
* Indexed assignment or writes to any variables not statically knowable to have been defined in the current function's scope,
  or to any resources or references

So, for example, this code would be allowed:

`_10

view fun foo(): Int {

_10

let a: [Int] = []

_10

a[0] = 3

_10

return a.length

_10

}`

while this would not:

`_10

let a: [Int] = []

_10

view fun foo(): Int {

_10

a[0] = 3

_10

return a.length

_10

}`

A caveat to this is that in some cases a non-`view` function that only performs a mutation that would be allowed in a `view` context will be rejected as a limitation of the analysis.
In particular, users may encounter this with arrays or dictionaries, where a function like:

`_10

view fun foo(): Int {

_10

let a: [Int] = [0]

_10

a[0] = 1

_10

}`

is acceptable, because `a` is local to this function, while

`_10

view fun foo(): Int {

_10

let a: [Int] = [0]

_10

a.append(1)

_10

}`

will be rejected, because `append` is not `view`.

## Functions are Values[​](#functions-are-values "Direct link to Functions are Values")

Functions are values ("first-class"), so they may be assigned to variables and fields
or passed to functions as arguments.

`_19

// Declare a function named `transform` which applies a function to each element

_19

// of an array of integers and returns a new array of the results.

_19

//

_19

access(all)

_19

fun transform(function: fun(Int): Int, integers: [Int]): [Int] {

_19

var newIntegers: [Int] = []

_19

for integer in integers {

_19

newIntegers.append(function(integer))

_19

}

_19

return newIntegers

_19

}

_19

_19

access(all)

_19

fun double(_ integer: Int): Int {

_19

return integer * 2

_19

}

_19

_19

let newIntegers = transform(function: double, integers: [1, 2, 3])

_19

// `newIntegers` is `[2, 4, 6]``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/functions.mdx)

[Previous

Operators](/docs/language/operators)[Next

Control Flow](/docs/language/control-flow)

###### Rate this page

 😞😐😊

* [Function Declarations](#function-declarations)
* [Function Expressions](#function-expressions)
* [Function Calls](#function-calls)
* [Function Types](#function-types)
* [Closures](#closures)
* [Argument Passing Behavior](#argument-passing-behavior)
* [Function Preconditions and Postconditions](#function-preconditions-and-postconditions)
* [View Functions](#view-functions)
* [Functions are Values](#functions-are-values)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.