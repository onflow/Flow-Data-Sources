# Source: https://cadence-lang.org/docs/testing-framework




Cadence Testing Framework | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Testing
On this page
# Cadence Testing Framework

The Cadence testing framework provides a convenient way to write tests for Cadence programs in Cadence.
This functionality is provided by the built-in `Test` contract.

tip

The testing framework can only be used off-chain, e.g. by using the [Flow CLI](https://developers.flow.com/tools/flow-cli).

Tests must be written in the form of a Cadence script.
A test script may contain testing functions that starts with the `test` prefix,
a `setup` function that always runs before the tests,
a `tearDown` function that always runs at the end of all test cases,
a `beforeEach` function that runs before each test case,
and an `afterEach` function that runs after each test case.
All the above four functions are optional.

 `_42// A `setup` function that always runs before the rest of the test cases._42// Can be used to initialize things that would be used across the test cases._42// e.g: initialling a blockchain backend, initializing a contract, etc._42access(all)_42fun setup() {_42}_42_42// The `beforeEach` function runs before each test case. Can be used to perform_42// some state cleanup before each test case, among other things._42access(all)_42fun beforeEach() {_42}_42_42// The `afterEach` function runs after each test case. Can be used to perform_42// some state cleanup after each test case, among other things._42access(all)_42fun afterEach() {_42}_42_42// Valid test functions start with the 'test' prefix._42access(all)_42fun testSomething() {_42}_42_42access(all)_42fun testAnotherThing() {_42}_42_42access(all)_42fun testMoreThings() {_42}_42_42// Test functions cannot have any arguments or return values._42access(all)_42fun testInvalidSignature(message: String): Bool {_42}_42_42// A `tearDown` function that always runs at the end of all test cases._42// e.g: Can be used to stop the blockchain back-end used for tests, etc. or any cleanup._42access(all)_42fun tearDown() {_42}`
## Test Standard Library[​](#test-standard-library "Direct link to Test Standard Library")

The testing framework can be used by importing the built-in `Test` contract:

 `_10import Test`
## Assertions[​](#assertions "Direct link to Assertions")

### Test.assert[​](#testassert "Direct link to Test.assert")

 `_10view fun assert(_ condition: Bool, message: String)`

Fails a test-case if the given condition is false, and reports a message which explains why the condition is false.

The message argument is optional.

 `_10import Test_10_10access(all)_10fun testExample() {_10 Test.assert(2 == 2)_10 Test.assert([1, 2, 3].length == 0, message: "Array length is not 0")_10}`
### Test.fail[​](#testfail "Direct link to Test.fail")

 `_10view fun fail(message: String)`

Immediately fails a test-case, with a message explaining the reason to fail the test.

The message argument is optional.

 `_10import Test_10_10access(all)_10fun testExample() {_10 let array = [1, 2, 3]_10_10 if array.length != 0 {_10 Test.fail(message: "Array length is not 0")_10 }_10}`
### Test.expect[​](#testexpect "Direct link to Test.expect")

 `_10fun expect(_ value: AnyStruct, _ matcher: Matcher)`

The `expect` function tests a value against a matcher (see [matchers](#matchers) section), and fails the test if it's not a match.

 `_10import Test_10_10access(all)_10fun testExample() {_10 let array = [1, 2, 3]_10_10 Test.expect(array.length, Test.equal(3))_10}`
### Test.assertEqual[​](#testassertequal "Direct link to Test.assertEqual")

 `_10fun assertEqual(_ expected: AnyStruct, _ actual: AnyStruct)`

The `assertEqual` function fails the test-case if the given values are not equal, and
reports a message which explains how the two values differ.

 `_40import Test_40_40access(all)_40struct Foo {_40_40 access(all)_40 let answer: Int_40_40 init(answer: Int) {_40 self.answer = answer_40 }_40}_40_40access(all)_40fun testExample() {_40 Test.assertEqual("this string", "this string")_40 Test.assertEqual(21, 21)_40 Test.assertEqual(true, true)_40 Test.assertEqual([1, 2, 3], [1, 2, 3])_40 Test.assertEqual(_40 {1: true, 2: false, 3: true},_40 {1: true, 2: false, 3: true}_40 )_40_40 let address1 = Address(0xf8d6e0586b0a20c7)_40 let address2 = Address(0xf8d6e0586b0a20c7)_40 Test.assertEqual(address1, address2)_40_40 let foo1 = Foo(answer: 42)_40 let foo2 = Foo(answer: 42)_40_40 Test.assertEqual(foo1, foo2)_40_40 let number1: Int64 = 100_40 let number2: UInt64 = 100_40 // Note that the two values need to have exactly the same type,_40 // and not just value, otherwise the assertion fails:_40 // assertion failed: not equal: expected: 100, actual: 100_40 Test.assertEqual(number1, number2)_40}`
### Test.expectFailure[​](#testexpectfailure "Direct link to Test.expectFailure")

 `_10fun expectFailure(_ functionWrapper: ((): Void), errorMessageSubstring: String)`

The `expectFailure` function wraps a function call in a closure, and expects it to fail with
an error message that contains the given error message portion.

 `_28import Test_28_28access(all)_28struct Foo {_28 access(self)_28 let answer: UInt8_28_28 init(answer: UInt8) {_28 self.answer = answer_28 }_28_28 access(all)_28 fun correctAnswer(_ input: UInt8): Bool {_28 if self.answer != input {_28 panic("wrong answer!")_28 }_28 return true_28 }_28}_28_28access(all)_28fun testExample() {_28 let foo = Foo(answer: 42)_28_28 Test.expectFailure(fun(): Void {_28 foo.correctAnswer(43)_28 }, errorMessageSubstring: "wrong answer!")_28}`
## Matchers[​](#matchers "Direct link to Matchers")

A matcher is an object that consists of a test function and associated utility functionality.

 `_31access(all)_31struct Matcher {_31_31 access(all)_31 let test: fun(AnyStruct): Bool_31_31 access(all)_31 init(test: fun(AnyStruct): Bool) {_31 self.test = test_31 }_31_31 /// Combine this matcher with the given matcher._31 /// Returns a new matcher that succeeds if this and the given matcher succeed._31 ///_31 access(all)_31 fun and(_ other: Matcher): Matcher {_31 return Matcher(test: fun (value: AnyStruct): Bool {_31 return self.test(value) && other.test(value)_31 })_31 }_31_31 /// Combine this matcher with the given matcher._31 /// Returns a new matcher that succeeds if this or the given matcher succeeds._31 ///_31 access(all)_31 fun or(_ other: Matcher): Matcher {_31 return Matcher(test: fun (value: AnyStruct): Bool {_31 return self.test(value) || other.test(value)_31 })_31 }_31}`

The `test` function defines the evaluation criteria for a value, and returns a boolean indicating whether the value
conforms to the test criteria defined in the function.

The `and` and `or` functions can be used to combine this matcher with another matcher to produce a new matcher with
multiple testing criteria.
The `and` method returns a new matcher that succeeds if both this and the given matcher are succeeded.
The `or` method returns a new matcher that succeeds if at-least this or the given matcher is succeeded.

A matcher that accepts a generic-typed test function can be constructed using the `newMatcher` function.

 `_10view fun newMatcher<T: AnyStruct>(_ test: fun(T): Bool): Test.Matcher`

The type parameter `T` is bound to `AnyStruct` type. It is also optional.

For example, a matcher that checks whether a given integer value is negative can be defined as follows:

 `_34import Test_34_34access(all)_34fun testExample() {_34 let isNegative = Test.newMatcher(fun (_ value: Int): Bool {_34 return value < 0_34 })_34_34 Test.expect(-15, isNegative)_34 // Alternatively, we can use `Test.assert` and the matcher's `test` function._34 Test.assert(isNegative.test(-15), message: "number is not negative")_34}_34_34access(all)_34fun testCustomMatcherUntyped() {_34 let matcher = Test.newMatcher(fun (_ value: AnyStruct): Bool {_34 if !value.getType().isSubtype(of: Type<Int>()) {_34 return false_34 }_34_34 return (value as! Int) > 5_34 })_34_34 Test.expect(8, matcher)_34}_34_34access(all)_34fun testCustomMatcherTyped() {_34 let matcher = Test.newMatcher<Int>(fun (_ value: Int): Bool {_34 return value == 7_34 })_34_34 Test.expect(7, matcher)_34}`

The `Test` contract provides some built-in matcher functions for convenience.

### Test.equal[​](#testequal "Direct link to Test.equal")

 `_10view fun equal(_ value: AnyStruct): Matcher`

The `equal` function returns a matcher that succeeds if the tested value is equal to the given value.
Accepts an `AnyStruct` value.

 `_10import Test_10_10access(all)_10fun testExample() {_10 let array = [1, 2, 3]_10_10 Test.expect([1, 2, 3], Test.equal(array))_10}`
### Test.beGreaterThan[​](#testbegreaterthan "Direct link to Test.beGreaterThan")

 `_10view fun beGreaterThan(_ value: Number): Matcher`

The `beGreaterThan` function returns a matcher that succeeds if the tested value is a number and
greater than the given number.

 `_10import Test_10_10access(all)_10fun testExample() {_10 let str = "Hello, there"_10_10 Test.expect(str.length, Test.beGreaterThan(5))_10}`
### Test.beLessThan[​](#testbelessthan "Direct link to Test.beLessThan")

 `_10view fun beLessThan(_ value: Number): Matcher`

The `beLessThan` function returns a matcher that succeeds if the tested value is a number and
less than the given number.

 `_10import Test_10_10access(all)_10fun testExample() {_10 let str = "Hello, there"_10_10 Test.expect(str.length, Test.beLessThan(15))_10}`
### Test.beNil[​](#testbenil "Direct link to Test.beNil")

 `_10view fun beNil(): Matcher`

The `beNil` function returns a new matcher that checks if the given test value is nil.

 `_10import Test_10_10access(all)_10fun testExample() {_10 let message: String? = nil_10_10 Test.expect(message, Test.beNil())_10}`
### Test.beEmpty[​](#testbeempty "Direct link to Test.beEmpty")

 `_10view fun beEmpty(): Matcher`

The `beEmpty` function returns a matcher that succeeds if the tested value is an array or dictionary,
and the tested value contains no elements.

 `_12import Test_12_12access(all)_12fun testExample() {_12 let array: [String] = []_12_12 Test.expect(array, Test.beEmpty())_12_12 let dictionary: {String: String} = {}_12_12 Test.expect(dictionary, Test.beEmpty())_12}`
### Test.haveElementCount[​](#testhaveelementcount "Direct link to Test.haveElementCount")

 `_10view fun haveElementCount(_ count: Int): Matcher`

The `haveElementCount` function returns a matcher that succeeds if the tested value is an array or dictionary,
and has the given number of elements.

 `_12import Test_12_12access(all)_12fun testExample() {_12 let array: [String] = ["one", "two", "three"]_12_12 Test.expect(array, Test.haveElementCount(3))_12_12 let dictionary: {String: Int} = {"one": 1, "two": 2, "three": 3}_12_12 Test.expect(dictionary, Test.haveElementCount(3))_12}`
### Test.contain[​](#testcontain "Direct link to Test.contain")

 `_10view fun contain(_ element: AnyStruct): Matcher`

The `contain` function returns a matcher that succeeds if the tested value is an array that contains
a value that is equal to the given value, or the tested value is a dictionary
that contains an entry where the key is equal to the given value.

 `_10access(all)_10fun testExample() {_10 let array: [String] = ["one", "two", "three"]_10_10 Test.expect(array, Test.contain("one"))_10_10 let dictionary: {String: Int} = {"one": 1, "two": 2, "three": 3}_10_10 Test.expect(dictionary, Test.contain("two"))_10}`
### Test.beSucceeded[​](#testbesucceeded "Direct link to Test.beSucceeded")

 `_10fun beSucceeded(): Matcher`

The `beSucceeded` function returns a new matcher that checks if the given test value is either
a ScriptResult or TransactionResult and the ResultStatus is succeeded.
Returns false in any other case.

 `_13import Test_13_13access(all)_13fun testExample() {_13 let blockchain = Test.newEmulatorBlockchain()_13 let result = blockchain.executeScript(_13 "access(all) fun main(): Int { return 2 + 3 }",_13 []_13 )_13_13 Test.expect(result, Test.beSucceeded())_13 Test.assertEqual(5, result.returnValue! as! Int)_13}`
### Test.beFailed[​](#testbefailed "Direct link to Test.beFailed")

 `_10fun beFailed(): Matcher`

The `beFailed` function returns a new matcher that checks if the given test value is either
a ScriptResult or TransactionResult and the ResultStatus is failed.
Returns false in any other case.

 `_18import Test_18_18access(all)_18fun testExample() {_18 let blockchain = Test.newEmulatorBlockchain()_18 let account = blockchain.createAccount()_18_18 let tx = Test.Transaction(_18 code: "transaction { execute{ panic(\"some error\") } }",_18 authorizers: [],_18 signers: [account],_18 arguments: [],_18 )_18_18 let result = blockchain.executeTransaction(tx)_18_18 Test.expect(result, Test.beFailed())_18}`
## Matcher combinators[​](#matcher-combinators "Direct link to Matcher combinators")

The built-in matchers, as well as custom matchers, can be combined with the three available combinators:

* `not`,
* `or`,
* `and`

in order to create more elaborate matchers and increase re-usability.

### not[​](#not "Direct link to not")

 `_10fun not(_ matcher: Matcher): Matcher`

The `not` function returns a new matcher that negates the test of the given matcher.

 `_15import Test_15_15access(all)_15fun testExample() {_15 let isEven = Test.newMatcher<Int>(fun (_ value: Int): Bool {_15 return value % 2 == 0_15 })_15_15 Test.expect(8, isEven)_15 Test.expect(7, Test.not(isEven))_15_15 let isNotEmpty = Test.not(Test.beEmpty())_15_15 Test.expect([1, 2, 3], isNotEmpty)_15}`
### or[​](#or "Direct link to or")

 `_10fun or(_ other: Matcher): Matcher`

The `Matcher.or` function combines this matcher with the given matcher.
Returns a new matcher that succeeds if this or the given matcher succeed.
If this matcher succeeds, then the other matcher would not be tested.

 `_11import Test_11_11access(all)_11fun testExample() {_11 let one = Test.equal(1)_11 let two = Test.equal(2)_11_11 let oneOrTwo = one.or(two)_11_11 Test.expect(2, oneOrTwo)_11}`
### and[​](#and "Direct link to and")

 `_10fun and(_ other: Matcher): Matcher`

The `Matcher.and` function combines this matcher with the given matcher.
Returns a new matcher that succeeds if this and the given matcher succeed.

 `_15import Test_15_15access(all)_15fun testExample() {_15 let sevenOrMore = Test.newMatcher<Int>(fun (_ value: Int): Bool {_15 return value >= 7_15 })_15 let lessThanTen = Test.newMatcher<Int>(fun (_ value: Int): Bool {_15 return value <= 10_15 })_15_15 let betweenSevenAndTen = sevenOrMore.and(lessThanTen)_15_15 Test.expect(8, betweenSevenAndTen)_15}`
## Blockchain[​](#blockchain "Direct link to Blockchain")

A blockchain is an environment to which transactions can be submitted to, and against which scripts can be run.
It imitates the behavior of a real network, for testing.

 `_150/// Blockchain emulates a real network._150///_150access(all)_150struct Blockchain {_150_150 access(all)_150 let backend: AnyStruct{BlockchainBackend}_150_150 init(backend: AnyStruct{BlockchainBackend}) {_150 self.backend = backend_150 }_150_150 /// Executes a script and returns the script return value and the status._150 /// `returnValue` field of the result will be `nil` if the script failed._150 ///_150 access(all)_150 fun executeScript(_ script: String, _ arguments: [AnyStruct]): ScriptResult {_150 return self.backend.executeScript(script, arguments)_150 }_150_150 /// Creates a signer account by submitting an account creation transaction._150 /// The transaction is paid by the service account._150 /// The returned account can be used to sign and authorize transactions._150 ///_150 access(all)_150 fun createAccount(): Account {_150 return self.backend.createAccount()_150 }_150_150 /// Add a transaction to the current block._150 ///_150 access(all)_150 fun addTransaction(_ tx: Transaction) {_150 self.backend.addTransaction(tx)_150 }_150_150 /// Executes the next transaction in the block, if any._150 /// Returns the result of the transaction, or nil if no transaction was scheduled._150 ///_150 access(all)_150 fun executeNextTransaction(): TransactionResult? {_150 return self.backend.executeNextTransaction()_150 }_150_150 /// Commit the current block._150 /// Committing will fail if there are un-executed transactions in the block._150 ///_150 access(all)_150 fun commitBlock() {_150 self.backend.commitBlock()_150 }_150_150 /// Executes a given transaction and commits the current block._150 ///_150 access(all)_150 fun executeTransaction(_ tx: Transaction): TransactionResult {_150 self.addTransaction(tx)_150 let txResult = self.executeNextTransaction()!_150 self.commitBlock()_150 return txResult_150 }_150_150 /// Executes a given set of transactions and commits the current block._150 ///_150 access(all)_150 fun executeTransactions(_ transactions: [Transaction]): [TransactionResult] {_150 for tx in transactions {_150 self.addTransaction(tx)_150 }_150_150 var results: [TransactionResult] = []_150 for tx in transactions {_150 let txResult = self.executeNextTransaction()!_150 results.append(txResult)_150 }_150_150 self.commitBlock()_150 return results_150 }_150_150 /// Deploys a given contract, and initializes it with the arguments._150 ///_150 access(all)_150 fun deployContract(_150 name: String,_150 code: String,_150 account: Account,_150 arguments: [AnyStruct]_150 ): Error? {_150 return self.backend.deployContract(_150 name: name,_150 code: code,_150 account: account,_150 arguments: arguments_150 )_150 }_150_150 /// Set the configuration to be used by the blockchain._150 /// Overrides any existing configuration._150 ///_150 access(all)_150 fun useConfiguration(_ configuration: Configuration) {_150 self.backend.useConfiguration(configuration)_150 }_150_150 /// Returns all the logs from the blockchain, up to the calling point._150 ///_150 access(all)_150 fun logs(): [String] {_150 return self.backend.logs()_150 }_150_150 /// Returns the service account of the blockchain. Can be used to sign_150 /// transactions with this account._150 ///_150 access(all)_150 fun serviceAccount(): Account {_150 return self.backend.serviceAccount()_150 }_150_150 /// Returns all events emitted from the blockchain._150 ///_150 access(all)_150 fun events(): [AnyStruct] {_150 return self.backend.events(nil)_150 }_150_150 /// Returns all events emitted from the blockchain,_150 /// filtered by type._150 ///_150 access(all)_150 fun eventsOfType(_ type: Type): [AnyStruct] {_150 return self.backend.events(type)_150 }_150_150 /// Resets the state of the blockchain to the given height._150 ///_150 access(all)_150 fun reset(to height: UInt64) {_150 self.backend.reset(to: height)_150 }_150_150 /// Moves the time of the blockchain by the given delta,_150 /// which should be passed in the form of seconds._150 ///_150 access(all)_150 fun moveTime(by delta: Fix64) {_150 self.backend.moveTime(by: delta)_150 }_150}`

The `BlockchainBackend` provides the actual functionality of the blockchain.

 `_46/// BlockchainBackend is the interface to be implemented by the backend providers._46///_46access(all)_46struct interface BlockchainBackend {_46_46 access(all)_46 fun executeScript(_ script: String, _ arguments: [AnyStruct]): ScriptResult_46_46 access(all)_46 fun createAccount(): Account_46_46 access(all)_46 fun addTransaction(_ tx: Transaction)_46_46 access(all)_46 fun executeNextTransaction(): TransactionResult?_46_46 access(all)_46 fun commitBlock()_46_46 access(all)_46 fun deployContract(_46 name: String,_46 code: String,_46 account: Account,_46 arguments: [AnyStruct]_46 ): Error?_46_46 access(all)_46 fun useConfiguration(_ configuration: Configuration)_46_46 access(all)_46 fun logs(): [String]_46_46 access(all)_46 fun serviceAccount(): Account_46_46 access(all)_46 fun events(_ type: Type?): [AnyStruct]_46_46 access(all)_46 fun reset(to height: UInt64)_46_46 access(all)_46 fun moveTime(by delta: Fix64)_46}`
### Creating a blockchain[​](#creating-a-blockchain "Direct link to Creating a blockchain")

A new blockchain instance can be created using the `Test.newEmulatorBlockchain` method.
It returns a `Blockchain` which is backed by a new [Flow Emulator](https://developers.flow.com/tools/emulator) instance.

 `_10import Test_10_10access(all)_10let blockchain = Test.newEmulatorBlockchain()`
### Creating accounts[​](#creating-accounts "Direct link to Creating accounts")

It may be necessary to create accounts during tests for various reasons, such as for deploying contracts, signing transactions, etc.
An account can be created using the `createAccount` function.

 `_12import Test_12_12access(all)_12let blockchain = Test.newEmulatorBlockchain()_12_12access(all)_12let account = blockchain.createAccount()_12_12access(all)_12fun testExample() {_12 log(account.address)_12}`

Running the above command, from the command-line, we would get:

 `_10flow test tests/test_sample_usage.cdc_103:31PM DBG LOG: 0x01cf0e2f2f715450_10_10Test results: "tests/test_sample_usage.cdc"_10- PASS: testExample`

The returned account consists of the `address` of the account, and a `publicKey` associated with it.

 `_16/// Account represents info about the account created on the blockchain._16///_16access(all)_16struct Account {_16_16 access(all)_16 let address: Address_16_16 access(all)_16 let publicKey: PublicKey_16_16 init(address: Address, publicKey: PublicKey) {_16 self.address = address_16 self.publicKey = publicKey_16 }_16}`
### Executing scripts[​](#executing-scripts "Direct link to Executing scripts")

Scripts can be run with the `executeScript` function, which returns a `ScriptResult`.
The function takes script-code as the first argument, and the script-arguments as an array as the second argument.

 `_21import Test_21_21access(all)_21let blockchain = Test.newEmulatorBlockchain()_21_21access(all)_21fun testExample() {_21 let code = "access(all) fun main(name: String): String { return \"Hello, \".concat(name) }"_21 let args = ["Peter"]_21_21 let scriptResult = blockchain.executeScript(code, args)_21_21 // Assert that the script was successfully executed._21 Test.expect(scriptResult, Test.beSucceeded())_21_21 // returnValue has always the type `AnyStruct`,_21 // so we need to type-cast accordingly._21 let returnValue = scriptResult.returnValue! as! String_21_21 Test.assertEqual("Hello, Peter", returnValue)_21}`

The script result consists of the `status` of the script execution, and a `returnValue` if the script execution was
successful, or an `error` otherwise (see [errors](#errors) section for more details on errors).

 `_20/// The result of a script execution._20///_20access(all)_20struct ScriptResult {_20_20 access(all)_20 let status: ResultStatus_20_20 access(all)_20 let returnValue: AnyStruct?_20_20 access(all)_20 let error: Error?_20_20 init(status: ResultStatus, returnValue: AnyStruct?, error: Error?) {_20 self.status = status_20 self.returnValue = returnValue_20 self.error = error_20 }_20}`
### Executing transactions[​](#executing-transactions "Direct link to Executing transactions")

A transaction must be created with the transaction code, a list of authorizes,
a list of signers that would sign the transaction, and the transaction arguments.

 `_24/// Transaction that can be submitted and executed on the blockchain._24///_24access(all)_24struct Transaction {_24_24 access(all)_24 let code: String_24_24 access(all)_24 let authorizers: [Address]_24_24 access(all)_24 let signers: [Account]_24_24 access(all)_24 let arguments: [AnyStruct]_24_24 init(code: String, authorizers: [Address], signers: [Account], arguments: [AnyStruct]) {_24 self.code = code_24 self.authorizers = authorizers_24 self.signers = signers_24 self.arguments = arguments_24 }_24}`

The number of authorizers must match the number of `&Account` parameters in the `prepare` block of the transaction.

 `_44import Test_44_44access(all)_44let blockchain = Test.newEmulatorBlockchain()_44_44access(all)_44let account = blockchain.createAccount()_44_44// There are two ways to execute the created transaction._44_44access(all)_44fun testExample() {_44 let tx = Test.Transaction(_44 code: "transaction { prepare(acct: &Account) {} execute{} }",_44 authorizers: [account.address],_44 signers: [account],_44 arguments: [],_44 )_44_44 // Executing the transaction immediately_44 // This may fail if the current block contains_44 // transactions that have not being executed yet._44 let txResult = blockchain.executeTransaction(tx)_44_44 Test.expect(txResult, Test.beSucceeded())_44}_44_44access(all)_44fun testExampleTwo() {_44 let tx = Test.Transaction(_44 code: "transaction { prepare(acct: &Account) {} execute{} }",_44 authorizers: [account.address],_44 signers: [account],_44 arguments: [],_44 )_44_44 // Add to the current block_44 blockchain.addTransaction(tx)_44_44 // Execute the next transaction in the block_44 let txResult = blockchain.executeNextTransaction()!_44_44 Test.expect(txResult, Test.beSucceeded())_44}`

The result of a transaction consists of the status of the execution, and an `Error` if the transaction failed.

 `_16/// The result of a transaction execution._16///_16access(all)_16struct TransactionResult {_16_16 access(all)_16 let status: ResultStatus_16_16 access(all)_16 let error: Error?_16_16 init(status: ResultStatus, error: Error?) {_16 self.status = status_16 self.error = error_16 }_16 }`
### Commit block[​](#commit-block "Direct link to Commit block")

`commitBlock` block will commit the current block, and will fail if there are any un-executed transactions in the block.

 `_24import Test_24_24access(all)_24let blockchain = Test.newEmulatorBlockchain()_24_24access(all)_24let account = blockchain.createAccount()_24_24access(all)_24fun testExample() {_24 let tx = Test.Transaction(_24 code: "transaction { prepare(acct: &Account) {} execute{} }",_24 authorizers: [account.address],_24 signers: [account],_24 arguments: [],_24 )_24_24 blockchain.commitBlock()_24_24 blockchain.addTransaction(tx)_24_24 // This will fail with `error: internal error: pending block with ID 1f9...c0b7740d2 cannot be committed before execution`_24 blockchain.commitBlock()_24}`
### Deploying contracts[​](#deploying-contracts "Direct link to Deploying contracts")

A contract can be deployed using the `deployContract` function of the `Blockchain`.

Suppose we have this contract (`Foo.cdc`):

 `_15access(all)_15contract Foo {_15_15 access(all)_15 let msg: String_15_15 init(_ msg: String) {_15 self.msg = msg_15 }_15_15 access(all)_15 fun sayHello(): String {_15 return self.msg_15 }_15}`
 `_20import Test_20_20access(all)_20let blockchain = Test.newEmulatorBlockchain()_20_20access(all)_20let account = blockchain.createAccount()_20_20access(all)_20fun testExample() {_20 let contractCode = Test.readFile("Foo.cdc")_20 let err = blockchain.deployContract(_20 name: "Foo",_20 code: contractCode,_20 account: account,_20 arguments: ["hello from args"],_20 )_20_20 Test.expect(err, Test.beNil())_20}`

An `Error` is returned if the contract deployment fails. Otherwise, a `nil` is returned.

### Configuring import addresses[​](#configuring-import-addresses "Direct link to Configuring import addresses")

A common pattern in Cadence projects is to define the imports as file locations and specify the addresses
corresponding to each network in the [Flow CLI configuration file](https://developers.flow.com/tools/flow-cli/flow.json/configuration.md#contracts).
When writing tests for such a project, it may also require to specify the addresses to be used during the tests as well.
However, during tests, since accounts are created dynamically and the addresses are also generated dynamically,
specifying the addresses statically in a configuration file is not an option.

Hence, the test framework provides a way to specify the addresses using the
`useConfiguration(_ configuration: Test.Configuration)` function in `Blockchain`.

The `Configuration` struct consists of a mapping of import locations to their addresses.

 `_13/// Configuration to be used by the blockchain._13/// Can be used to set the address mapping._13///_13access(all)_13struct Configuration {_13_13 access(all)_13 let addresses: {String: Address}_13_13 init(addresses: {String: Address}) {_13 self.addresses = addresses_13 }_13}`
tip

The `Blockchain.useConfiguration` is a run-time alternative for
[statically defining contract addresses in the flow.json config file](https://developers.flow.com/tools/flow-cli/flow.json/configuration.md#advanced-format).

The configurations can be specified during the test setup as a best-practice.

e.g: Assume running a script that imports the above `Foo.cdc` contract.
The import location for the contract can be specified using the placeholder `"Foo"`.
This placeholder can be any unique string.

Suppose this script is saved in `say_hello.cdc`.

 `_10import "Foo"_10_10access(all)_10fun main(): String {_10 return Foo.sayHello()_10}`

Then, before executing the script, the address mapping can be specified as follows:

 `_36import Test_36_36access(all)_36let blockchain = Test.newEmulatorBlockchain()_36_36access(all)_36let account = blockchain.createAccount()_36_36access(all)_36fun setup() {_36 blockchain.useConfiguration(Test.Configuration({_36 "Foo": account.address_36 }))_36_36 let contractCode = Test.readFile("Foo.cdc")_36 let err = blockchain.deployContract(_36 name: "Foo",_36 code: contractCode,_36 account: account,_36 arguments: ["hello from args"],_36 )_36_36 Test.expect(err, Test.beNil())_36}_36_36access(all)_36fun testExample() {_36 let script = Test.readFile("say_hello.cdc")_36 let scriptResult = blockchain.executeScript(script, [])_36_36 Test.expect(scriptResult, Test.beSucceeded())_36_36 let returnValue = scriptResult.returnValue! as! String_36_36 Test.assertEqual("hello from args", returnValue)_36}`

The subsequent operations on the blockchain (e.g: contract deployment, script/transaction execution) will resolve the
import locations to the provided addresses.

### Errors[​](#errors "Direct link to Errors")

An `Error` maybe returned when an operation (such as executing a script, executing a transaction, etc.) has failed.
It contains a message indicating why the operation failed.

 `_12// Error is returned if something has gone wrong._12//_12access(all)_12struct Error {_12_12 access(all)_12 let message: String_12_12 init(_ message: String) {_12 self.message = message_12 }_12}`

An `Error` can be asserted against its presence or absence.

 `_33import Test_33_33access(all)_33let blockchain = Test.newEmulatorBlockchain()_33_33access(all)_33let account = blockchain.createAccount()_33_33access(all)_33fun testExample() {_33 let script = Test.readFile("say_hello.cdc")_33 let scriptResult = blockchain.executeScript(script, [])_33_33 // If we expect a script to fail, we can use Test.beFailed() instead_33 Test.expect(scriptResult, Test.beSucceeded())_33_33 let tx = Test.Transaction(_33 code: "transaction { prepare(acct: &Account) {} execute{} }",_33 authorizers: [account.address],_33 signers: [account],_33 arguments: [],_33 )_33 let txResult = blockchain.executeTransaction(tx)_33_33 // If we expect a transaction to fail, we can use Test.beFailed() instead_33 Test.expect(txResult, Test.beSucceeded())_33_33 let err: Test.Error? = txResult.error_33_33 if err != nil {_33 log(err!.message)_33 }_33}`
## Blockchain events[​](#blockchain-events "Direct link to Blockchain events")

We can also assert that certain events were emitted from the blockchain, up to the latest block.

Suppose we have this contract (`Foo.cdc`):

 `_19access(all)_19contract Foo {_19 _19 access(all)_19 let msg: String_19_19 access(all)_19 event ContractInitialized(msg: String)_19_19 init(_ msg: String) {_19 self.msg = msg_19 emit ContractInitialized(msg: self.msg)_19 }_19_19 access(all)_19 fun sayHello(): String {_19 return self.msg_19 }_19}`
 `_35import Test_35_35access(all)_35let blockchain = Test.newEmulatorBlockchain()_35_35access(all)_35let account = blockchain.createAccount()_35_35access(all)_35fun setup() {_35 blockchain.useConfiguration(Test.Configuration({_35 "Foo": account.address_35 }))_35_35 let contractCode = Test.readFile("Foo.cdc")_35 let err = blockchain.deployContract(_35 name: "Foo",_35 code: contractCode,_35 account: account,_35 arguments: ["hello from args"],_35 )_35_35 Test.expect(err, Test.beNil())_35_35 // As of now, we have to construct the composite type by hand,_35 // until the testing framework allows developers to import_35 // contract types, e.g.:_35 // let typ = Type<FooContract.ContractInitialized>()_35 let typ = CompositeType("A.01cf0e2f2f715450.Foo.ContractInitialized")!_35 let events = blockchain.eventsOfType(typ)_35 Test.assertEqual(1, events.length)_35_35 // We can also fetch all events emitted from the blockchain_35 log(blockchain.events())_35}`
## Commonly used contracts[​](#commonly-used-contracts "Direct link to Commonly used contracts")

The commonly used contracts are already deployed on the blockchain, and can be imported without any
additional setup.

Suppose this script is saved in `get_type_ids.cdc`.

 `_17import "FungibleToken"_17import "FlowToken"_17import "NonFungibleToken"_17import "MetadataViews"_17import "ViewResolver"_17import "ExampleNFT"_17import "NFTStorefrontV2"_17import "NFTStorefront"_17_17access(all)_17fun main(): [String] {_17 return [_17 Type<FlowToken>().identifier,_17 Type<NonFungibleToken>().identifier,_17 Type<MetadataViews>().identifier_17 ]_17}`
 `_22import Test_22_22access(all)_22let blockchain = Test.newEmulatorBlockchain()_22_22access(all)_22fun testExample() {_22 let script = Test.readFile("get_type_ids.cdc")_22 let scriptResult = blockchain.executeScript(script, [])_22_22 Test.expect(scriptResult, Test.beSucceeded())_22_22 let returnValue = scriptResult.returnValue! as! [String]_22_22 let expected = [_22 "A.0ae53cb6e3f42a79.FlowToken",_22 "A.f8d6e0586b0a20c7.NonFungibleToken",_22 "A.f8d6e0586b0a20c7.MetadataViews"_22 ]_22_22 Test.assertEqual(expected, returnValue)_22}`
## Reading from files[​](#reading-from-files "Direct link to Reading from files")

Writing tests often require constructing source-code of contracts/transactions/scripts in the test script.
Testing framework provides a convenient way to load programs from a local file, without having to manually construct
them within the test script.

 `_10let contractCode = Test.readFile("./sample/contracts/FooContract.cdc")`

`readFile` returns the content of the file as a string.

## Logging[​](#logging "Direct link to Logging")

The `log` function is available for usage both in test scripts, as well as contracts/scripts/transactions.

The `Blockchain.logs()` method aggregates all logs from contracts/scripts/transactions.

 `_22import Test_22_22access(all)_22let blockchain = Test.newEmulatorBlockchain()_22_22access(all)_22let account = blockchain.createAccount()_22_22access(all)_22fun testExample() {_22 let tx = Test.Transaction(_22 code: "transaction { prepare(acct: &Account) {} execute{ log(\"in a transaction\") } }",_22 authorizers: [account.address],_22 signers: [account],_22 arguments: [],_22 )_22_22 let txResult = blockchain.executeTransaction(tx)_22_22 Test.expect(txResult, Test.beSucceeded())_22 Test.assertEqual(["in a transaction"], blockchain.logs())_22}`
## Examples[​](#examples "Direct link to Examples")

This [repository](https://github.com/m-Peter/flow-code-coverage) contains some functional examples
that demonstrate most of the above features, both for contrived and real-world smart contracts.
It also contains a detailed explanation on using code coverage from within the testing framework.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/testing-framework.mdx)[PreviousMeasuring Time](/docs/measuring-time)
###### Rate this page

😞😐😊

* [Test Standard Library](#test-standard-library)
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
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

