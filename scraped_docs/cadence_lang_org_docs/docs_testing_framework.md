# Source: https://cadence-lang.org/docs/testing-framework

Cadence Testing Framework | Cadence



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
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Testing

On this page

# Cadence Testing Framework

The Cadence testing framework provides a convenient way to write tests for Cadence programs in Cadence. This functionality is provided by the built-in `Test` contract.

tip

The testing framework can only be used offchain (e.g., by using the [Flow CLI](https://developers.flow.com/tools/flow-cli)).

Tests must be written in the form of a Cadence script. A test script may contain testing functions that starts with the `test` prefix, a `setup` function that always runs before the tests, a `tearDown` function that always runs at the end of all test cases, a `beforeEach` function that runs before each test case, and an `afterEach` function that runs after each test case. All of the above four functions are optional.

`` _42

// A `setup` function that always runs before the rest of the test cases.

_42

// Can be used to initialize things that would be used across the test cases.

_42

// e.g: initialling a blockchain backend, initializing a contract, etc.

_42

access(all)

_42

fun setup() {

_42

}

_42

_42

// The `beforeEach` function runs before each test case. Can be used to perform

_42

// some state cleanup before each test case, among other things.

_42

access(all)

_42

fun beforeEach() {

_42

}

_42

_42

// The `afterEach` function runs after each test case. Can be used to perform

_42

// some state cleanup after each test case, among other things.

_42

access(all)

_42

fun afterEach() {

_42

}

_42

_42

// Valid test functions start with the 'test' prefix.

_42

access(all)

_42

fun testSomething() {

_42

}

_42

_42

access(all)

_42

fun testAnotherThing() {

_42

}

_42

_42

access(all)

_42

fun testMoreThings() {

_42

}

_42

_42

// Test functions cannot have any arguments or return values.

_42

access(all)

_42

fun testInvalidSignature(message: String): Bool {

_42

}

_42

_42

// A `tearDown` function that always runs at the end of all test cases.

_42

// e.g: Can be used to stop the blockchain back-end used for tests, etc. or any cleanup.

_42

access(all)

_42

fun tearDown() {

_42

} ``

## Test standard library[​](#test-standard-library "Direct link to Test standard library")

The testing framework can be used by importing the built-in `Test` contract:

`_10

import Test`

## Assertions[​](#assertions "Direct link to Assertions")

### Test.assert[​](#testassert "Direct link to Test.assert")

`_10

view fun assert(_ condition: Bool, message: String)`

Fails a test case if the given condition is false, and reports a message that explains why the condition is false.

The message argument is optional.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

Test.assert(2 == 2)

_10

Test.assert([1, 2, 3].length == 0, message: "Array length is not 0")

_10

}`

### Test.fail[​](#testfail "Direct link to Test.fail")

`_10

view fun fail(message: String)`

Immediately fails a test case, with a message explaining the reason to fail the test.

The message argument is optional.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

let array = [1, 2, 3]

_10

_10

if array.length != 0 {

_10

Test.fail(message: "Array length is not 0")

_10

}

_10

}`

### Test.expect[​](#testexpect "Direct link to Test.expect")

`_10

fun expect(_ value: AnyStruct, _ matcher: Matcher)`

The `expect` function tests a value against a matcher (see [matchers](#matchers) section), and fails the test if it's not a match.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

let array = [1, 2, 3]

_10

_10

Test.expect(array.length, Test.equal(3))

_10

}`

### Test.assertEqual[​](#testassertequal "Direct link to Test.assertEqual")

`_10

fun assertEqual(_ expected: AnyStruct, _ actual: AnyStruct)`

The `assertEqual` function fails the test case if the given values are not equal, and reports a message that explains how the two values differ.

`_40

import Test

_40

_40

access(all)

_40

struct Foo {

_40

_40

access(all)

_40

let answer: Int

_40

_40

init(answer: Int) {

_40

self.answer = answer

_40

}

_40

}

_40

_40

access(all)

_40

fun testExample() {

_40

Test.assertEqual("this string", "this string")

_40

Test.assertEqual(21, 21)

_40

Test.assertEqual(true, true)

_40

Test.assertEqual([1, 2, 3], [1, 2, 3])

_40

Test.assertEqual(

_40

{1: true, 2: false, 3: true},

_40

{1: true, 2: false, 3: true}

_40

)

_40

_40

let address1 = Address(0xf8d6e0586b0a20c7)

_40

let address2 = Address(0xf8d6e0586b0a20c7)

_40

Test.assertEqual(address1, address2)

_40

_40

let foo1 = Foo(answer: 42)

_40

let foo2 = Foo(answer: 42)

_40

_40

Test.assertEqual(foo1, foo2)

_40

_40

let number1: Int64 = 100

_40

let number2: UInt64 = 100

_40

// Note that the two values need to have exactly the same type,

_40

// and not just value, otherwise the assertion fails:

_40

// assertion failed: not equal: expected: 100, actual: 100

_40

Test.assertEqual(number1, number2)

_40

}`

### Test.expectFailure[​](#testexpectfailure "Direct link to Test.expectFailure")

`_10

fun expectFailure(_ functionWrapper: ((): Void), errorMessageSubstring: String)`

The `expectFailure` function wraps a function call in a closure and expects it to fail with an error message that contains the given error message portion.

`_28

import Test

_28

_28

access(all)

_28

struct Foo {

_28

access(self)

_28

let answer: UInt8

_28

_28

init(answer: UInt8) {

_28

self.answer = answer

_28

}

_28

_28

access(all)

_28

fun correctAnswer(_ input: UInt8): Bool {

_28

if self.answer != input {

_28

panic("wrong answer!")

_28

}

_28

return true

_28

}

_28

}

_28

_28

access(all)

_28

fun testExample() {

_28

let foo = Foo(answer: 42)

_28

_28

Test.expectFailure(fun(): Void {

_28

foo.correctAnswer(43)

_28

}, errorMessageSubstring: "wrong answer!")

_28

}`

## Matchers[​](#matchers "Direct link to Matchers")

A matcher is an object that consists of a test function and associated utility functionality.

`_31

access(all)

_31

struct Matcher {

_31

_31

access(all)

_31

let test: fun(AnyStruct): Bool

_31

_31

access(all)

_31

init(test: fun(AnyStruct): Bool) {

_31

self.test = test

_31

}

_31

_31

/// Combine this matcher with the given matcher.

_31

/// Returns a new matcher that succeeds if this and the given matcher succeed.

_31

///

_31

access(all)

_31

fun and(_ other: Matcher): Matcher {

_31

return Matcher(test: fun (value: AnyStruct): Bool {

_31

return self.test(value) && other.test(value)

_31

})

_31

}

_31

_31

/// Combine this matcher with the given matcher.

_31

/// Returns a new matcher that succeeds if this or the given matcher succeeds.

_31

///

_31

access(all)

_31

fun or(_ other: Matcher): Matcher {

_31

return Matcher(test: fun (value: AnyStruct): Bool {

_31

return self.test(value) || other.test(value)

_31

})

_31

}

_31

}`

The `test` function defines the evaluation criteria for a value and returns a boolean indicating whether the value conforms to the test criteria defined in the function.

The `and` and `or` functions can be used to combine this matcher with another matcher to produce a new matcher with multiple testing criteria. The `and` method returns a new matcher that succeeds if both this and the given matcher are succeeded. The `or` method returns a new matcher that succeeds if at least this or the given matcher is succeeded.

A matcher that accepts a generic-typed test function can be constructed using the `newMatcher` function.

`_10

view fun newMatcher<T: AnyStruct>(_ test: fun(T): Bool): Test.Matcher`

The type parameter `T` is bound to `AnyStruct` type. It is also optional.

For example, a matcher that checks whether a given integer value is negative can be defined as follows:

`` _34

import Test

_34

_34

access(all)

_34

fun testExample() {

_34

let isNegative = Test.newMatcher(fun (_ value: Int): Bool {

_34

return value < 0

_34

})

_34

_34

Test.expect(-15, isNegative)

_34

// Alternatively, we can use `Test.assert` and the matcher's `test` function.

_34

Test.assert(isNegative.test(-15), message: "number is not negative")

_34

}

_34

_34

access(all)

_34

fun testCustomMatcherUntyped() {

_34

let matcher = Test.newMatcher(fun (_ value: AnyStruct): Bool {

_34

if !value.getType().isSubtype(of: Type<Int>()) {

_34

return false

_34

}

_34

_34

return (value as! Int) > 5

_34

})

_34

_34

Test.expect(8, matcher)

_34

}

_34

_34

access(all)

_34

fun testCustomMatcherTyped() {

_34

let matcher = Test.newMatcher<Int>(fun (_ value: Int): Bool {

_34

return value == 7

_34

})

_34

_34

Test.expect(7, matcher)

_34

} ``

The `Test` contract provides some built-in matcher functions for convenience.

### Test.equal[​](#testequal "Direct link to Test.equal")

`_10

view fun equal(_ value: AnyStruct): Matcher`

The `equal` function returns a matcher that succeeds if the tested value is equal to the given value. Accepts an `AnyStruct` value.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

let array = [1, 2, 3]

_10

_10

Test.expect([1, 2, 3], Test.equal(array))

_10

}`

### Test.beGreaterThan[​](#testbegreaterthan "Direct link to Test.beGreaterThan")

`_10

view fun beGreaterThan(_ value: Number): Matcher`

The `beGreaterThan` function returns a matcher that succeeds if the tested value is a number and greater than the given number.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

let str = "Hello, there"

_10

_10

Test.expect(str.length, Test.beGreaterThan(5))

_10

}`

### Test.beLessThan[​](#testbelessthan "Direct link to Test.beLessThan")

`_10

view fun beLessThan(_ value: Number): Matcher`

The `beLessThan` function returns a matcher that succeeds if the tested value is a number and less than the given number.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

let str = "Hello, there"

_10

_10

Test.expect(str.length, Test.beLessThan(15))

_10

}`

### Test.beNil[​](#testbenil "Direct link to Test.beNil")

`_10

view fun beNil(): Matcher`

The `beNil` function returns a new matcher that checks if the given test value is nil.

`_10

import Test

_10

_10

access(all)

_10

fun testExample() {

_10

let message: String? = nil

_10

_10

Test.expect(message, Test.beNil())

_10

}`

### Test.beEmpty[​](#testbeempty "Direct link to Test.beEmpty")

`_10

view fun beEmpty(): Matcher`

The `beEmpty` function returns a matcher that succeeds if the tested value is an array or dictionary and the tested value contains no elements.

`_12

import Test

_12

_12

access(all)

_12

fun testExample() {

_12

let array: [String] = []

_12

_12

Test.expect(array, Test.beEmpty())

_12

_12

let dictionary: {String: String} = {}

_12

_12

Test.expect(dictionary, Test.beEmpty())

_12

}`

### Test.haveElementCount[​](#testhaveelementcount "Direct link to Test.haveElementCount")

`_10

view fun haveElementCount(_ count: Int): Matcher`

The `haveElementCount` function returns a matcher that succeeds if the tested value is an array or dictionary and has the given number of elements.

`_12

import Test

_12

_12

access(all)

_12

fun testExample() {

_12

let array: [String] = ["one", "two", "three"]

_12

_12

Test.expect(array, Test.haveElementCount(3))

_12

_12

let dictionary: {String: Int} = {"one": 1, "two": 2, "three": 3}

_12

_12

Test.expect(dictionary, Test.haveElementCount(3))

_12

}`

### Test.contain[​](#testcontain "Direct link to Test.contain")

`_10

view fun contain(_ element: AnyStruct): Matcher`

The `contain` function returns a matcher that succeeds if the tested value is an array that contains a value that is equal to the given value, or the tested value is a dictionary that contains an entry where the key is equal to the given value.

`_10

access(all)

_10

fun testExample() {

_10

let array: [String] = ["one", "two", "three"]

_10

_10

Test.expect(array, Test.contain("one"))

_10

_10

let dictionary: {String: Int} = {"one": 1, "two": 2, "three": 3}

_10

_10

Test.expect(dictionary, Test.contain("two"))

_10

}`

### Test.beSucceeded[​](#testbesucceeded "Direct link to Test.beSucceeded")

`_10

fun beSucceeded(): Matcher`

The `beSucceeded` function returns a new matcher that checks if the given test value is either a ScriptResult or TransactionResult and the ResultStatus is succeeded. Returns false in any other case.

`_13

import Test

_13

_13

access(all)

_13

fun testExample() {

_13

let blockchain = Test.newEmulatorBlockchain()

_13

let result = blockchain.executeScript(

_13

"access(all) fun main(): Int { return 2 + 3 }",

_13

[]

_13

)

_13

_13

Test.expect(result, Test.beSucceeded())

_13

Test.assertEqual(5, result.returnValue! as! Int)

_13

}`

### Test.beFailed[​](#testbefailed "Direct link to Test.beFailed")

`_10

fun beFailed(): Matcher`

The `beFailed` function returns a new matcher that checks if the given test value is either a ScriptResult or TransactionResult and the ResultStatus is failed. Returns false in any other case.

`_18

import Test

_18

_18

access(all)

_18

fun testExample() {

_18

let blockchain = Test.newEmulatorBlockchain()

_18

let account = blockchain.createAccount()

_18

_18

let tx = Test.Transaction(

_18

code: "transaction { execute{ panic(\"some error\") } }",

_18

authorizers: [],

_18

signers: [account],

_18

arguments: [],

_18

)

_18

_18

let result = blockchain.executeTransaction(tx)

_18

_18

Test.expect(result, Test.beFailed())

_18

}`

## Matcher combinators[​](#matcher-combinators "Direct link to Matcher combinators")

The built-in matchers, as well as custom matchers, can be combined with the three available combinators:

* `not`
* `or`
* `and`

This assures more elaborate matchers and increases re-usability.

### not[​](#not "Direct link to not")

`_10

fun not(_ matcher: Matcher): Matcher`

The `not` function returns a new matcher that negates the test of the given matcher.

`_15

import Test

_15

_15

access(all)

_15

fun testExample() {

_15

let isEven = Test.newMatcher<Int>(fun (_ value: Int): Bool {

_15

return value % 2 == 0

_15

})

_15

_15

Test.expect(8, isEven)

_15

Test.expect(7, Test.not(isEven))

_15

_15

let isNotEmpty = Test.not(Test.beEmpty())

_15

_15

Test.expect([1, 2, 3], isNotEmpty)

_15

}`

### or[​](#or "Direct link to or")

`_10

fun or(_ other: Matcher): Matcher`

The `Matcher.or` function combines this matcher with the given matcher. Returns a new matcher that succeeds if this or the given matcher succeed. If this matcher succeeds, then the other matcher would not be tested.

`_11

import Test

_11

_11

access(all)

_11

fun testExample() {

_11

let one = Test.equal(1)

_11

let two = Test.equal(2)

_11

_11

let oneOrTwo = one.or(two)

_11

_11

Test.expect(2, oneOrTwo)

_11

}`

### and[​](#and "Direct link to and")

`_10

fun and(_ other: Matcher): Matcher`

The `Matcher.and` function combines this matcher with the given matcher. Returns a new matcher that succeeds if this and the given matcher succeed.

`_15

import Test

_15

_15

access(all)

_15

fun testExample() {

_15

let sevenOrMore = Test.newMatcher<Int>(fun (_ value: Int): Bool {

_15

return value >= 7

_15

})

_15

let lessThanTen = Test.newMatcher<Int>(fun (_ value: Int): Bool {

_15

return value <= 10

_15

})

_15

_15

let betweenSevenAndTen = sevenOrMore.and(lessThanTen)

_15

_15

Test.expect(8, betweenSevenAndTen)

_15

}`

## Blockchain[​](#blockchain "Direct link to Blockchain")

A blockchain is an environment to which transactions can be submitted to, and against which scripts can be run. It imitates the behavior of a real network for testing.

`` _148

/// Blockchain emulates a real network.

_148

///

_148

access(all)

_148

struct Blockchain {

_148

_148

access(all)

_148

let backend: AnyStruct{BlockchainBackend}

_148

_148

init(backend: AnyStruct{BlockchainBackend}) {

_148

self.backend = backend

_148

}

_148

_148

/// Executes a script and returns the script return value and the status.

_148

/// `returnValue` field of the result will be `nil` if the script failed.

_148

///

_148

access(all)

_148

fun executeScript(_ script: String, _ arguments: [AnyStruct]): ScriptResult {

_148

return self.backend.executeScript(script, arguments)

_148

}

_148

_148

/// Creates a signer account by submitting an account creation transaction.

_148

/// The transaction is paid by the service account.

_148

/// The returned account can be used to sign and authorize transactions.

_148

///

_148

access(all)

_148

fun createAccount(): Account {

_148

return self.backend.createAccount()

_148

}

_148

_148

/// Add a transaction to the current block.

_148

///

_148

access(all)

_148

fun addTransaction(_ tx: Transaction) {

_148

self.backend.addTransaction(tx)

_148

}

_148

_148

/// Executes the next transaction in the block, if any.

_148

/// Returns the result of the transaction, or nil if no transaction was scheduled.

_148

///

_148

access(all)

_148

fun executeNextTransaction(): TransactionResult? {

_148

return self.backend.executeNextTransaction()

_148

}

_148

_148

/// Commit the current block.

_148

/// Committing will fail if there are un-executed transactions in the block.

_148

///

_148

access(all)

_148

fun commitBlock() {

_148

self.backend.commitBlock()

_148

}

_148

_148

/// Executes a given transaction and commits the current block.

_148

///

_148

access(all)

_148

fun executeTransaction(_ tx: Transaction): TransactionResult {

_148

self.addTransaction(tx)

_148

let txResult = self.executeNextTransaction()!

_148

self.commitBlock()

_148

return txResult

_148

}

_148

_148

/// Executes a given set of transactions and commits the current block.

_148

///

_148

access(all)

_148

fun executeTransactions(_ transactions: [Transaction]): [TransactionResult] {

_148

for tx in transactions {

_148

self.addTransaction(tx)

_148

}

_148

_148

var results: [TransactionResult] = []

_148

for tx in transactions {

_148

let txResult = self.executeNextTransaction()!

_148

results.append(txResult)

_148

}

_148

_148

self.commitBlock()

_148

return results

_148

}

_148

_148

/// Deploys a given contract, and initializes it with the arguments.

_148

///

_148

access(all)

_148

fun deployContract(

_148

name: String,

_148

path: String,

_148

arguments: [AnyStruct]

_148

): Error? {

_148

return self.backend.deployContract(

_148

name: name,

_148

path: path,

_148

arguments: arguments

_148

)

_148

}

_148

_148

/// Set the configuration to be used by the blockchain.

_148

/// Overrides any existing configuration.

_148

///

_148

access(all)

_148

fun useConfiguration(_ configuration: Configuration) {

_148

self.backend.useConfiguration(configuration)

_148

}

_148

_148

/// Returns all the logs from the blockchain, up to the calling point.

_148

///

_148

access(all)

_148

fun logs(): [String] {

_148

return self.backend.logs()

_148

}

_148

_148

/// Returns the service account of the blockchain. Can be used to sign

_148

/// transactions with this account.

_148

///

_148

access(all)

_148

fun serviceAccount(): Account {

_148

return self.backend.serviceAccount()

_148

}

_148

_148

/// Returns all events emitted from the blockchain.

_148

///

_148

access(all)

_148

fun events(): [AnyStruct] {

_148

return self.backend.events(nil)

_148

}

_148

_148

/// Returns all events emitted from the blockchain,

_148

/// filtered by type.

_148

///

_148

access(all)

_148

fun eventsOfType(_ type: Type): [AnyStruct] {

_148

return self.backend.events(type)

_148

}

_148

_148

/// Resets the state of the blockchain to the given height.

_148

///

_148

access(all)

_148

fun reset(to height: UInt64) {

_148

self.backend.reset(to: height)

_148

}

_148

_148

/// Moves the time of the blockchain by the given delta,

_148

/// which should be passed in the form of seconds.

_148

///

_148

access(all)

_148

fun moveTime(by delta: Fix64) {

_148

self.backend.moveTime(by: delta)

_148

}

_148

} ``

The `BlockchainBackend` provides the actual functionality of the blockchain.

`_45

/// BlockchainBackend is the interface to be implemented by the backend providers.

_45

///

_45

access(all)

_45

struct interface BlockchainBackend {

_45

_45

access(all)

_45

fun executeScript(_ script: String, _ arguments: [AnyStruct]): ScriptResult

_45

_45

access(all)

_45

fun createAccount(): Account

_45

_45

access(all)

_45

fun addTransaction(_ tx: Transaction)

_45

_45

access(all)

_45

fun executeNextTransaction(): TransactionResult?

_45

_45

access(all)

_45

fun commitBlock()

_45

_45

access(all)

_45

fun deployContract(

_45

name: String,

_45

path: String,

_45

arguments: [AnyStruct]

_45

): Error?

_45

_45

access(all)

_45

fun useConfiguration(_ configuration: Configuration)

_45

_45

access(all)

_45

fun logs(): [String]

_45

_45

access(all)

_45

fun serviceAccount(): Account

_45

_45

access(all)

_45

fun events(_ type: Type?): [AnyStruct]

_45

_45

access(all)

_45

fun reset(to height: UInt64)

_45

_45

access(all)

_45

fun moveTime(by delta: Fix64)

_45

}`

### Creating a blockchain[​](#creating-a-blockchain "Direct link to Creating a blockchain")

A new blockchain instance can be created using the `Test.newEmulatorBlockchain` method. It returns a `Blockchain`, which is backed by a new [Flow Emulator](https://developers.flow.com/tools/emulator) instance.

`_10

import Test

_10

_10

access(all)

_10

let blockchain = Test.newEmulatorBlockchain()`

### Creating accounts[​](#creating-accounts "Direct link to Creating accounts")

It may be necessary to create accounts during tests for various reasons, such as for deploying contracts, signing transactions, and so on. An account can be created using the `createAccount` function.

`_12

import Test

_12

_12

access(all)

_12

let blockchain = Test.newEmulatorBlockchain()

_12

_12

access(all)

_12

let account = blockchain.createAccount()

_12

_12

access(all)

_12

fun testExample() {

_12

log(account.address)

_12

}`

The following response is returned when running the above command from the command line:

`_10

flow test tests/test_sample_usage.cdc

_10

3:31PM DBG LOG: 0x01cf0e2f2f715450

_10

_10

Test results: "tests/test_sample_usage.cdc"

_10

- PASS: testExample`

The returned account consists of the `address` of the account and a `publicKey` associated with it.

`_16

/// Account represents info about the account created on the blockchain.

_16

///

_16

access(all)

_16

struct Account {

_16

_16

access(all)

_16

let address: Address

_16

_16

access(all)

_16

let publicKey: PublicKey

_16

_16

init(address: Address, publicKey: PublicKey) {

_16

self.address = address

_16

self.publicKey = publicKey

_16

}

_16

}`

### Executing scripts[​](#executing-scripts "Direct link to Executing scripts")

Scripts can be run with the `executeScript` function, which returns a `ScriptResult`. The function takes script code as the first argument, and the script arguments as an array as the second argument.

`` _21

import Test

_21

_21

access(all)

_21

let blockchain = Test.newEmulatorBlockchain()

_21

_21

access(all)

_21

fun testExample() {

_21

let code = "access(all) fun main(name: String): String { return \"Hello, \".concat(name) }"

_21

let args = ["Peter"]

_21

_21

let scriptResult = blockchain.executeScript(code, args)

_21

_21

// Assert that the script was successfully executed.

_21

Test.expect(scriptResult, Test.beSucceeded())

_21

_21

// returnValue has always the type `AnyStruct`,

_21

// so we need to type-cast accordingly.

_21

let returnValue = scriptResult.returnValue! as! String

_21

_21

Test.assertEqual("Hello, Peter", returnValue)

_21

} ``

The script result consists of the `status` of the script execution, a `returnValue` if the script execution was successful, or an `error` otherwise (see [errors](#errors) section for more details on errors).

`_20

/// The result of a script execution.

_20

///

_20

access(all)

_20

struct ScriptResult {

_20

_20

access(all)

_20

let status: ResultStatus

_20

_20

access(all)

_20

let returnValue: AnyStruct?

_20

_20

access(all)

_20

let error: Error?

_20

_20

init(status: ResultStatus, returnValue: AnyStruct?, error: Error?) {

_20

self.status = status

_20

self.returnValue = returnValue

_20

self.error = error

_20

}

_20

}`

### Executing transactions[​](#executing-transactions "Direct link to Executing transactions")

A transaction must be created with the transaction code, a list of authorizes, a list of signers that would sign the transaction, and the transaction arguments.

`_24

/// Transaction that can be submitted and executed on the blockchain.

_24

///

_24

access(all)

_24

struct Transaction {

_24

_24

access(all)

_24

let code: String

_24

_24

access(all)

_24

let authorizers: [Address]

_24

_24

access(all)

_24

let signers: [Account]

_24

_24

access(all)

_24

let arguments: [AnyStruct]

_24

_24

init(code: String, authorizers: [Address], signers: [Account], arguments: [AnyStruct]) {

_24

self.code = code

_24

self.authorizers = authorizers

_24

self.signers = signers

_24

self.arguments = arguments

_24

}

_24

}`

The number of authorizers must match the number of `&Account` parameters in the `prepare` block of the transaction.

`_44

import Test

_44

_44

access(all)

_44

let blockchain = Test.newEmulatorBlockchain()

_44

_44

access(all)

_44

let account = blockchain.createAccount()

_44

_44

// There are two ways to execute the created transaction.

_44

_44

access(all)

_44

fun testExample() {

_44

let tx = Test.Transaction(

_44

code: "transaction { prepare(acct: &Account) {} execute{} }",

_44

authorizers: [account.address],

_44

signers: [account],

_44

arguments: [],

_44

)

_44

_44

// Executing the transaction immediately

_44

// This may fail if the current block contains

_44

// transactions that have not being executed yet.

_44

let txResult = blockchain.executeTransaction(tx)

_44

_44

Test.expect(txResult, Test.beSucceeded())

_44

}

_44

_44

access(all)

_44

fun testExampleTwo() {

_44

let tx = Test.Transaction(

_44

code: "transaction { prepare(acct: &Account) {} execute{} }",

_44

authorizers: [account.address],

_44

signers: [account],

_44

arguments: [],

_44

)

_44

_44

// Add to the current block

_44

blockchain.addTransaction(tx)

_44

_44

// Execute the next transaction in the block

_44

let txResult = blockchain.executeNextTransaction()!

_44

_44

Test.expect(txResult, Test.beSucceeded())

_44

}`

The result of a transaction consists of the status of the execution, and an `Error` if the transaction failed.

`_16

/// The result of a transaction execution.

_16

///

_16

access(all)

_16

struct TransactionResult {

_16

_16

access(all)

_16

let status: ResultStatus

_16

_16

access(all)

_16

let error: Error?

_16

_16

init(status: ResultStatus, error: Error?) {

_16

self.status = status

_16

self.error = error

_16

}

_16

}`

### Commit block[​](#commit-block "Direct link to Commit block")

`commitBlock` block commits the current block and will fail if there are any unexecuted transactions in the block.

`` _24

import Test

_24

_24

access(all)

_24

let blockchain = Test.newEmulatorBlockchain()

_24

_24

access(all)

_24

let account = blockchain.createAccount()

_24

_24

access(all)

_24

fun testExample() {

_24

let tx = Test.Transaction(

_24

code: "transaction { prepare(acct: &Account) {} execute{} }",

_24

authorizers: [account.address],

_24

signers: [account],

_24

arguments: [],

_24

)

_24

_24

blockchain.commitBlock()

_24

_24

blockchain.addTransaction(tx)

_24

_24

// This will fail with `error: internal error: pending block with ID 1f9...c0b7740d2 cannot be committed before execution`

_24

blockchain.commitBlock()

_24

} ``

### Deploying contracts[​](#deploying-contracts "Direct link to Deploying contracts")

A contract can be deployed using the `deployContract` function of the `Blockchain`.

Suppose we have this contract (`Foo.cdc`):

`_15

access(all)

_15

contract Foo {

_15

_15

access(all)

_15

let msg: String

_15

_15

init(_ msg: String) {

_15

self.msg = msg

_15

}

_15

_15

access(all)

_15

fun sayHello(): String {

_15

return self.msg

_15

}

_15

}`

`_18

import Test

_18

_18

access(all)

_18

let blockchain = Test.newEmulatorBlockchain()

_18

_18

access(all)

_18

let account = blockchain.createAccount()

_18

_18

access(all)

_18

fun testExample() {

_18

let err = blockchain.deployContract(

_18

name: "Foo",

_18

path: "./Foo.cdc",

_18

arguments: ["hello from args"],

_18

)

_18

_18

Test.expect(err, Test.beNil())

_18

}`

An `Error` is returned if the contract deployment fails. Otherwise, a `nil` is returned.

### Configuring import addresses[​](#configuring-import-addresses "Direct link to Configuring import addresses")

A common pattern in Cadence projects is to define the imports as file locations and specify the addresses corresponding to each network in the [Flow CLI configuration file](https://developers.flow.com/tools/flow-cli/flow.json/configuration.md#contracts). When writing tests for such a project, it may also require to specify the addresses to be used during the tests as well. However, during tests, since accounts are created dynamically and the addresses are also generated dynamically, specifying the addresses statically in a configuration file is not an option.

Hence, the test framework provides a way to specify the addresses using the `useConfiguration(_ configuration: Test.Configuration)` function in `Blockchain`.

The `Configuration` struct consists of a mapping of import locations to their addresses.

`_13

/// Configuration to be used by the blockchain.

_13

/// Can be used to set the address mapping.

_13

///

_13

access(all)

_13

struct Configuration {

_13

_13

access(all)

_13

let addresses: {String: Address}

_13

_13

init(addresses: {String: Address}) {

_13

self.addresses = addresses

_13

}

_13

}`

tip

The `Blockchain.useConfiguration` is a run-time alternative for [statically defining contract addresses](https://developers.flow.com/tools/flow-cli/flow.json/configuration.md#advanced-format) in the flow.json config file.

The configurations can be specified during the test setup as a best practice.

For example, assume running a script that imports the above `Foo.cdc` contract. The import location for the contract can be specified using the placeholder `"Foo"`. This placeholder can be any unique string.

Suppose this script is saved in `say_hello.cdc`:

`_10

import "Foo"

_10

_10

access(all)

_10

fun main(): String {

_10

return Foo.sayHello()

_10

}`

Then, before executing the script, the address mapping can be specified as follows:

`_34

import Test

_34

_34

access(all)

_34

let blockchain = Test.newEmulatorBlockchain()

_34

_34

access(all)

_34

let account = blockchain.createAccount()

_34

_34

access(all)

_34

fun setup() {

_34

blockchain.useConfiguration(Test.Configuration({

_34

"Foo": account.address

_34

}))

_34

_34

let err = blockchain.deployContract(

_34

name: "Foo",

_34

path: "./Foo.cdc",

_34

arguments: ["hello from args"],

_34

)

_34

_34

Test.expect(err, Test.beNil())

_34

}

_34

_34

access(all)

_34

fun testExample() {

_34

let script = Test.readFile("say_hello.cdc")

_34

let scriptResult = blockchain.executeScript(script, [])

_34

_34

Test.expect(scriptResult, Test.beSucceeded())

_34

_34

let returnValue = scriptResult.returnValue! as! String

_34

_34

Test.assertEqual("hello from args", returnValue)

_34

}`

The subsequent operations on the blockchain (e.g., contract deployment and script/transaction execution) will resolve the
import locations to the provided addresses.

### Errors[​](#errors "Direct link to Errors")

An `Error` maybe returned when an operation (such as executing a script, executing a transaction, and so on) has failed. It contains a message indicating why the operation failed.

`_12

// Error is returned if something has gone wrong.

_12

//

_12

access(all)

_12

struct Error {

_12

_12

access(all)

_12

let message: String

_12

_12

init(_ message: String) {

_12

self.message = message

_12

}

_12

}`

An `Error` can be asserted against its presence or absence.

`_33

import Test

_33

_33

access(all)

_33

let blockchain = Test.newEmulatorBlockchain()

_33

_33

access(all)

_33

let account = blockchain.createAccount()

_33

_33

access(all)

_33

fun testExample() {

_33

let script = Test.readFile("say_hello.cdc")

_33

let scriptResult = blockchain.executeScript(script, [])

_33

_33

// If we expect a script to fail, we can use Test.beFailed() instead

_33

Test.expect(scriptResult, Test.beSucceeded())

_33

_33

let tx = Test.Transaction(

_33

code: "transaction { prepare(acct: &Account) {} execute{} }",

_33

authorizers: [account.address],

_33

signers: [account],

_33

arguments: [],

_33

)

_33

let txResult = blockchain.executeTransaction(tx)

_33

_33

// If we expect a transaction to fail, we can use Test.beFailed() instead

_33

Test.expect(txResult, Test.beSucceeded())

_33

_33

let err: Test.Error? = txResult.error

_33

_33

if err != nil {

_33

log(err!.message)

_33

}

_33

}`

## Blockchain events[​](#blockchain-events "Direct link to Blockchain events")

We can also assert that certain events were emitted from the blockchain, up to the latest block.

Suppose we have this contract (`Foo.cdc`):

`_19

access(all)

_19

contract Foo {

_19

_19

access(all)

_19

let msg: String

_19

_19

access(all)

_19

event ContractInitialized(msg: String)

_19

_19

init(_ msg: String) {

_19

self.msg = msg

_19

emit ContractInitialized(msg: self.msg)

_19

}

_19

_19

access(all)

_19

fun sayHello(): String {

_19

return self.msg

_19

}

_19

}`

`_33

import Test

_33

_33

access(all)

_33

let blockchain = Test.newEmulatorBlockchain()

_33

_33

access(all)

_33

let account = blockchain.createAccount()

_33

_33

access(all)

_33

fun setup() {

_33

blockchain.useConfiguration(Test.Configuration({

_33

"Foo": account.address

_33

}))

_33

_33

let err = blockchain.deployContract(

_33

name: "Foo",

_33

path: "./Foo.cdc",

_33

arguments: ["hello from args"],

_33

)

_33

_33

Test.expect(err, Test.beNil())

_33

_33

// As of now, we have to construct the composite type by hand,

_33

// until the testing framework allows developers to import

_33

// contract types, e.g.:

_33

// let typ = Type<FooContract.ContractInitialized>()

_33

let typ = CompositeType("A.01cf0e2f2f715450.Foo.ContractInitialized")!

_33

let events = blockchain.eventsOfType(typ)

_33

Test.assertEqual(1, events.length)

_33

_33

// We can also fetch all events emitted from the blockchain

_33

log(blockchain.events())

_33

}`

## Commonly used contracts[​](#commonly-used-contracts "Direct link to Commonly used contracts")

The commonly used contracts are already deployed on the blockchain and can be imported without any additional setup.

Suppose this script is saved in `get_type_ids.cdc`:

`_17

import "FungibleToken"

_17

import "FlowToken"

_17

import "NonFungibleToken"

_17

import "MetadataViews"

_17

import "ViewResolver"

_17

import "ExampleNFT"

_17

import "NFTStorefrontV2"

_17

import "NFTStorefront"

_17

_17

access(all)

_17

fun main(): [String] {

_17

return [

_17

Type<FlowToken>().identifier,

_17

Type<NonFungibleToken>().identifier,

_17

Type<MetadataViews>().identifier

_17

]

_17

}`

`_22

import Test

_22

_22

access(all)

_22

let blockchain = Test.newEmulatorBlockchain()

_22

_22

access(all)

_22

fun testExample() {

_22

let script = Test.readFile("get_type_ids.cdc")

_22

let scriptResult = blockchain.executeScript(script, [])

_22

_22

Test.expect(scriptResult, Test.beSucceeded())

_22

_22

let returnValue = scriptResult.returnValue! as! [String]

_22

_22

let expected = [

_22

"A.0ae53cb6e3f42a79.FlowToken",

_22

"A.f8d6e0586b0a20c7.NonFungibleToken",

_22

"A.f8d6e0586b0a20c7.MetadataViews"

_22

]

_22

_22

Test.assertEqual(expected, returnValue)

_22

}`

## Reading from files[​](#reading-from-files "Direct link to Reading from files")

Writing tests often require constructing source code of contracts/transactions/scripts in the test script. Testing framework provides a convenient way to load programs from a local file, without having to manually construct them within the test script.

`_10

let contractCode = Test.readFile("./sample/contracts/FooContract.cdc")`

`readFile` returns the content of the file as a string.

## Logging[​](#logging "Direct link to Logging")

The `log` function is available for usage both in test scripts, as well as contracts/scripts/transactions.

The `Blockchain.logs()` method aggregates all logs from contracts/scripts/transactions.

`_22

import Test

_22

_22

access(all)

_22

let blockchain = Test.newEmulatorBlockchain()

_22

_22

access(all)

_22

let account = blockchain.createAccount()

_22

_22

access(all)

_22

fun testExample() {

_22

let tx = Test.Transaction(

_22

code: "transaction { prepare(acct: &Account) {} execute{ log(\"in a transaction\") } }",

_22

authorizers: [account.address],

_22

signers: [account],

_22

arguments: [],

_22

)

_22

_22

let txResult = blockchain.executeTransaction(tx)

_22

_22

Test.expect(txResult, Test.beSucceeded())

_22

Test.assertEqual(["in a transaction"], blockchain.logs())

_22

}`

## Examples[​](#examples "Direct link to Examples")

This [repository](https://github.com/m-Peter/flow-code-coverage) contains some functional examples that demonstrate most of the above features, both for contrived and real-world smart contracts. It also contains a detailed explanation about using code coverage from within the testing framework.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/testing-framework.mdx)

[Previous

Measuring Time](/docs/measuring-time)

###### Rate this page

😞😐😊

* [Test standard library](#test-standard-library)
* [Assertions](#assertions)
  + [Test.assert](#testassert)
  + [Test.fail](#testfail)
  + [Test.expect](#testexpect)
  + [Test.assertEqual](#testassertequal)
  + [Test.expectFailure](#testexpectfailure)
* [Matchers](#matchers)
  + [Test.equal](#testequal)
  + [Test.beGreaterThan](#testbegreaterthan)
  + [Test.beLessThan](#testbelessthan)
  + [Test.beNil](#testbenil)
  + [Test.beEmpty](#testbeempty)
  + [Test.haveElementCount](#testhaveelementcount)
  + [Test.contain](#testcontain)
  + [Test.beSucceeded](#testbesucceeded)
  + [Test.beFailed](#testbefailed)
* [Matcher combinators](#matcher-combinators)
  + [not](#not)
  + [or](#or)
  + [and](#and)
* [Blockchain](#blockchain)
  + [Creating a blockchain](#creating-a-blockchain)
  + [Creating accounts](#creating-accounts)
  + [Executing scripts](#executing-scripts)
  + [Executing transactions](#executing-transactions)
  + [Commit block](#commit-block)
  + [Deploying contracts](#deploying-contracts)
  + [Configuring import addresses](#configuring-import-addresses)
  + [Errors](#errors)
* [Blockchain events](#blockchain-events)
* [Commonly used contracts](#commonly-used-contracts)
* [Reading from files](#reading-from-files)
* [Logging](#logging)
* [Examples](#examples)