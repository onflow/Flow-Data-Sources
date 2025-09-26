# Source: https://developers.flow.com/build/getting-started/quickstarts/hello-world

Smart Contract Interaction | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Forte Network Upgrade](/blockchain-development-tutorials/forte)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

  + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

    - [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)
    - [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
    - [Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)
    - [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)
  + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)
  + [Account Linking](/blockchain-development-tutorials/cadence/account-management)
  + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)
* Smart Contract Interaction

On this page

# Smart Contract Interaction

Building on your local development setup from the previous tutorial, you'll now master advanced Flow development skills that every professional developer needs. This tutorial focuses on working with external dependencies, building sophisticated transactions, and establishing robust testing practices.

Flow's composability is one of its greatest strengths—contracts can easily import and use functionality from other contracts. You'll learn to leverage this power while building reliable, well-tested applications that interact seamlessly with the broader Flow ecosystem.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

After completing this tutorial, you'll be able to:

* **Manage external dependencies** using Flow's dependency manager and integrate third-party contracts
* **Build sophisticated transactions** that interact with multiple contracts and handle complex state changes
* **Master transaction anatomy** and understand how Cadence transactions work under the hood
* **Implement comprehensive testing** strategies including edge cases and error conditions
* **Apply test-driven development** workflows to ensure code quality and reliability
* **Handle transaction monitoring** and error management in production scenarios

## What You'll Build[​](#what-youll-build "Direct link to What You'll Build")

Building on your Counter contract, you'll enhance it with external dependencies and create a comprehensive testing suite. By the end of this tutorial, you'll have:

* **Enhanced Counter app** that uses the NumberFormatter contract for better display
* **Complex transactions** that demonstrate advanced interaction patterns
* **Comprehensive test suite** covering normal operations, edge cases, and error conditions
* **Professional workflow** for developing, testing, and deploying contract interactions

**Prerequisites:**

* Completed Environment Setup tutorial
* Flow CLI, emulator running, and Counter contract deployed
* Basic understanding of Cadence syntax

## Managing Dependencies[​](#managing-dependencies "Direct link to Managing Dependencies")

In addition to creating your own contracts, you can also install contracts that have already been deployed to the network by using the [Dependency Manager](https://developers.flow.com/build/tools/flow-cli/dependency-manager). This is useful for interacting with contracts that are part of the Flow ecosystem or that have been deployed by other developers.

Flow's dependency manager allows you to:

* Install contracts deployed on any Flow network (mainnet, testnet, emulator)
* Automatically manage contract addresses across different environments
* Keep your code portable and environment-independent

For example, let's say we want to format the result of our `GetCounter` script so that we display the number with commas if it's greater than 999. To do that we can install a contract called [`NumberFormatter`](https://contractbrowser.com/A.8a4dce54554b225d.NumberFormatter) from `testnet` that has a function to format numbers.

### Install NumberFormatter Contract[​](#install-numberformatter-contract "Direct link to Install NumberFormatter Contract")

The [`NumberFormatter`](https://contractbrowser.com/A.8a4dce54554b225d.NumberFormatter) contract provides utilities for formatting numbers with commas, making large numbers more readable. Let's install it from testnet:

`_10

flow dependencies install testnet://8a4dce54554b225d.NumberFormatter`

When prompted:

1. **Account to deploy to:** Select `emulator-account` (this will deploy it locally for development)
2. **Alias for mainnet:** You can skip this by pressing Enter

This command:

* Downloads the NumberFormatter contract from testnet and any of its dependencies
* Adds it to your `imports/` directory
* Configures deployment settings in [`flow.json`](https://developers.flow.com/build/tools/flow-cli/flow.json/configuration)
* Sets up automatic address resolution

### Configure Dependencies in flow.json[​](#configure-dependencies-in-flowjson "Direct link to Configure Dependencies in flow.json")

Open your `flow.json` file and notice the new sections:

`_24

{

_24

.

_24

.

_24

.

_24

"dependencies": {

_24

"NumberFormatter": {

_24

"source": "testnet://8a4dce54554b225d.NumberFormatter",

_24

"hash": "dc7043832da46dbcc8242a53fa95b37f020bc374df42586a62703b2651979fb9",

_24

"aliases": {

_24

"testnet": "8a4dce54554b225d"

_24

}

_24

}

_24

},

_24

.

_24

.

_24

.

_24

"deployments": {

_24

"emulator": {

_24

"emulator-account": [

_24

"NumberFormatter"

_24

]

_24

}

_24

}

_24

}`

This configuration:

* Maps the `NumberFormatter` dependency to its testnet source
* Sets up deployment to your emulator account
* Enables automatic address resolution in your code

### Deploy External Dependencies[​](#deploy-external-dependencies "Direct link to Deploy External Dependencies")

Now we can deploy the `NumberFormatter` contract to the emulator by running:

`_10

flow project deploy`

You should see output like:

`_10

Deploying 1 contracts for accounts: emulator-account

_10

_10

NumberFormatter -> 0xf8d6e0586b0a20c7 (66e6c4210ae8263370fc3661f148f750175bb4cf2e80637fb42eafe2d6c5b385)

_10

_10

🎉 All contracts deployed successfully`

### Integrate External Contract[​](#integrate-external-contract "Direct link to Integrate External Contract")

Now let's update your `GetCounter.cdc` script to use the NumberFormatter. Open `cadence/scripts/GetCounter.cdc` and update it:

`_14

import "Counter"

_14

import "NumberFormatter"

_14

_14

access(all)

_14

fun main(): String {

_14

// Retrieve the count from the Counter contract

_14

let count: Int = Counter.getCount()

_14

_14

// Format the count using NumberFormatter

_14

let formattedCount = NumberFormatter.formatWithCommas(number: count)

_14

_14

// Return the formatted count

_14

return formattedCount

_14

}`

**Key Points:**

* **Import syntax**: `import "Counter"` and `import "NumberFormatter"` don't require addresses
* **Contract interaction**: We call `NumberFormatter.formatWithCommas()` just like any other function
* **Return type change**: The script now returns a `String` instead of an `Int`

### Test the Integration[​](#test-the-integration "Direct link to Test the Integration")

Run your updated script:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc`

You should see:

`_10

Result: "1"`

The number is now formatted as a string. Let's create a more impressive example by adding a transaction that increments by 1000.

### Create a Bulk Increment Transaction[​](#create-a-bulk-increment-transaction "Direct link to Create a Bulk Increment Transaction")

Generate a new transaction to demonstrate the NumberFormatter's power:

`_10

flow generate transaction IncrementBy1000`

Open `cadence/transactions/IncrementBy1000.cdc` and replace the content with:

`_20

import "Counter"

_20

_20

transaction {

_20

prepare(acct: &Account) {

_20

// Authorization handled automatically

_20

}

_20

_20

execute {

_20

// Increment the counter 1000 times

_20

var i = 0

_20

while i < 1000 {

_20

Counter.increment()

_20

i = i + 1

_20

}

_20

_20

// Retrieve the new count and log it

_20

let newCount = Counter.getCount()

_20

log("New count after incrementing by 1000: ".concat(newCount.toString()))

_20

}

_20

}`

Execute the transaction:

`_10

flow transactions send cadence/transactions/IncrementBy1000.cdc --signer test-account`

Now run your formatted script to see the NumberFormatter in action:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc`

Result:

`_10

Result: "1,001"`

Perfect! The NumberFormatter automatically adds commas to make large numbers readable.

info

**The Power of Composability**: Notice what just happened—you enhanced your Counter contract's functionality **without modifying the original contract**. This is the power of Flow's composability: you can extend functionality by combining contracts, enabling rapid development and code reuse. Even more importantly, we did this **without needing access or permission.**

## Building Transactions[​](#building-transactions "Direct link to Building Transactions")

Transactions are the foundation of blockchain state changes. Unlike scripts (which only read data), transactions can modify contract state, transfer tokens, and emit events. Let's master advanced transaction patterns.

### Understanding Transaction Anatomy[​](#understanding-transaction-anatomy "Direct link to Understanding Transaction Anatomy")

Every Cadence transaction has the same basic structure:

`_21

import "OtherContract"

_21

_21

transaction {

_21

// Optional: Declare variables available throughout the transaction

_21

let initialCount: Int

_21

_21

// This phase has access to account storage and capabilities

_21

// Used for authorization and accessing private data

_21

prepare(acct: &Account) {

_21

}

_21

_21

// This phase contains the main transaction logic

_21

// No access to account storage, only to data from prepare phase

_21

execute {

_21

}

_21

_21

// Optional: Conditions that must be true after execution

_21

// Used for verification and ensuring transaction success

_21

post {

_21

}

_21

}`

### Transaction Phases Explained[​](#transaction-phases-explained "Direct link to Transaction Phases Explained")

1. **Import Phase**: Declare contract dependencies
2. **Parameter Declaration**: Define inputs the transaction accepts
3. **Variable Declaration**: Declare transaction-scoped variables
4. **Prepare Phase**: Access account storage and capabilities (authorized)
5. **Execute Phase**: Main logic execution (no storage access)
6. **Post Phase**: Verify transaction success conditions

#### Transaction with Parameters[​](#transaction-with-parameters "Direct link to Transaction with Parameters")

Create a transaction that accepts a custom increment value:

`_10

flow generate transaction IncrementByAmount`

Open `cadence/transactions/IncrementByAmount.cdc`:

`_39

import "Counter"

_39

_39

transaction(amount: Int) {

_39

_39

// Store initial value

_39

let initialCount: Int

_39

_39

prepare(acct: &Account) {

_39

// Verify the account is authorized to make this change

_39

log("Account ".concat(acct.address.toString()).concat(" is incrementing by ").concat(amount.toString()))

_39

_39

prepare(acct: &Account) {

_39

self.initialCount = Counter.getCount() // Capture initial state

_39

log("Account".concat(acct.address.toString()).concat(" is incrementing by").concat(amount.toString()))

_39

}

_39

_39

execute {

_39

// Validate input

_39

if amount <= 0 {

_39

panic("Amount must be positive")

_39

}

_39

_39

// Increment the specified number of times

_39

var i = 0

_39

while i < amount {

_39

Counter.increment()

_39

i = i + 1

_39

}

_39

_39

let newCount = Counter.getCount()

_39

log("Counter incremented by ".concat(amount.toString()).concat(", new value: ").concat(newCount.toString()))

_39

}

_39

_39

post {

_39

// Verify the counter increased correctly

_39

Counter.getCount() == (self.initialCount + amount): "Counter must equal initial count plus increment amount"

_39

}

_39

}

_39

}`

Execute with a parameter:

`_10

flow transactions send cadence/transactions/IncrementByAmount.cdc <amount> --network emulator --signer test-account`

## Testing Your Code[​](#testing-your-code "Direct link to Testing Your Code")

Testing is crucial for smart contract development. Flow provides powerful testing capabilities built into the CLI that enable comprehensive test coverage and test-driven development workflows.

Execute the test suite:

`_10

flow test`

You should see output confirming the tests pass:

`_10

Test results: "Counter_test.cdc"

_10

- PASS: testContract

_10

_10

All tests passed`

### Understanding Existing Tests[​](#understanding-existing-tests "Direct link to Understanding Existing Tests")

Open `cadence/tests/Counter_test.cdc` to see the existing test:

`_13

import Test

_13

_13

access(all) let account = Test.createAccount()

_13

_13

access(all) fun testContract() {

_13

let err = Test.deployContract(

_13

name: "Counter",

_13

path: "../contracts/Counter.cdc",

_13

arguments: []

_13

)

_13

_13

Test.expect(err, Test.beNil())

_13

}`

This basic test:

1. **Creates a test account** using `Test.createAccount()`
2. **Deploys the Counter contract** to the test environment
3. **Verifies deployment succeeded** by checking that no error occurred

### Test Integration with Dependencies[​](#test-integration-with-dependencies "Direct link to Test Integration with Dependencies")

Test the NumberFormatter integration:

`_24

import Test

_24

_24

access(all) let account = Test.createAccount()

_24

_24

access(all) fun testNumberFormatterLogic() {

_24

// Test NumberFormatter logic inline without contract deployment

_24

// Test small number (under 1000) - should have no comma

_24

let smallNumberScript = Test.executeScript(

_24

"access(all) fun formatWithCommas(number: Int): String { let isNegative = number < 0; let absNumber = number < 0 ? -number : number; let numberString = absNumber.toString(); var formatted = \"\"; var count = 0; let numberLength = numberString.length; var i = numberLength - 1; while i >= 0 { let digit = numberString.slice(from: i, upTo: i + 1); formatted = digit.concat(formatted); count = count + 1; if count % 3 == 0 && i != 0 { formatted = \",\".concat(formatted) }; i = i - 1 }; if isNegative { formatted = \"-\".concat(formatted) }; return formatted }; access(all) fun main(): String { return formatWithCommas(number: 123) }",

_24

[]

_24

)

_24

Test.expect(smallNumberScript, Test.beSucceeded())

_24

let smallResult = smallNumberScript.returnValue! as! String

_24

Test.expect(smallResult, Test.equal("123"))

_24

_24

// Test large number (over 999) - should have comma

_24

let largeNumberScript = Test.executeScript(

_24

"access(all) fun formatWithCommas(number: Int): String { let isNegative = number < 0; let absNumber = number < 0 ? -number : number; let numberString = absNumber.toString(); var formatted = \"\"; var count = 0; let numberLength = numberString.length; var i = numberLength - 1; while i >= 0 { let digit = numberString.slice(from: i, upTo: i + 1); formatted = digit.concat(formatted); count = count + 1; if count % 3 == 0 && i != 0 { formatted = \",\".concat(formatted) }; i = i - 1 }; if isNegative { formatted = \"-\".concat(formatted) }; return formatted }; access(all) fun main(): String { return formatWithCommas(number: 1234) }",

_24

[]

_24

)

_24

Test.expect(largeNumberScript, Test.beSucceeded())

_24

let largeResult = largeNumberScript.returnValue! as! String

_24

Test.expect(largeResult, Test.equal("1,234"))

_24

}`

The Formatter\_test.cdc test validates that number formatting with commas works correctly by testing two scenarios: numbers under 1,000 (which should have no commas) and numbers over 999 (which should have commas). The test is constructed with two main assertions - first testing that 123 formats as "123" without commas, and second testing that 1234 formats as "1,234" with a comma.

### Run Your Enhanced Test Suite[​](#run-your-enhanced-test-suite "Direct link to Run Your Enhanced Test Suite")

Execute the complete test suite with your new comprehensive tests:

`_10

flow test`

You should see output like:

`_10

Running tests...

_10

_10

Test results: "cadence/tests/Formatter_test.cdc"

_10

- PASS: testNumberFormatterLogic

_10

Test results: "cadence/tests/Counter_test.cdc"

_10

- PASS: testContract

_10

_10

All tests passed`

tip

For a more detailed guide on Cadence testing patterns and advanced techniques, check out the [tests documentation](/build/tools/flow-cli/tests).

---

## Conclusion[​](#conclusion "Direct link to Conclusion")

Through this tutorial, you've accomplished:

✅ **Dependency Management**

* Successfully integrated the NumberFormatter contract from testnet
* Learned about Flow's dependency management system and automatic address resolution
* Demonstrated contract composability by enhancing functionality without modifying source code
* Configured multi-contract deployments across different environments

✅ **Transaction Development**

* Understood transaction anatomy including prepare, execute, and post phases
* Implemented proper input validation and error handling patterns

✅ **Testing**

* Implemented test coverage for contract functionality
* Created integration tests that verify multi-contract interactions

### What You've Learned[​](#what-youve-learned "Direct link to What You've Learned")

You have learned how to use Flow's dependency management system to install and integrate external contracts (like NumberFormatter), understand the structure of Cadence transactions including their prepare, execute, and post phases, and implement basic testing for contract functionality. You can now work with multi-contract applications and understand how contracts can be composed together to extend functionality.

### Next Steps[​](#next-steps "Direct link to Next Steps")

With these skills, you're ready to:

* Build frontend applications that interact with your smart contracts
* Deploy contracts to live networks (testnet and mainnet)
* Explore advanced Flow patterns and ecosystem contracts
* Contribute to the growing Flow developer community

You've made significant progress in becoming a proficient Flow developer!

### Resources for Continued Learning[​](#resources-for-continued-learning "Direct link to Resources for Continued Learning")

Continue your Flow mastery with these advanced resources:

* **[Flow Discord Community](https://discord.gg/flow-blockchain)**: Connect with other developers building sophisticated Flow applications
* **[Cadence Language Reference](https://cadence-lang.org)**: Master advanced language features including resources, capabilities, and access control
* **[Flow GitHub](https://github.com/onflow)**: Explore production contract examples and contribute to the ecosystem

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction.md)

Last updated on **Sep 25, 2025** by **Brian Doyle**

[Previous

Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)[Next

Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)
* [What You'll Build](#what-youll-build)
* [Managing Dependencies](#managing-dependencies)
  + [Install NumberFormatter Contract](#install-numberformatter-contract)
  + [Configure Dependencies in flow.json](#configure-dependencies-in-flowjson)
  + [Deploy External Dependencies](#deploy-external-dependencies)
  + [Integrate External Contract](#integrate-external-contract)
  + [Test the Integration](#test-the-integration)
  + [Create a Bulk Increment Transaction](#create-a-bulk-increment-transaction)
* [Building Transactions](#building-transactions)
  + [Understanding Transaction Anatomy](#understanding-transaction-anatomy)
  + [Transaction Phases Explained](#transaction-phases-explained)
* [Testing Your Code](#testing-your-code)
  + [Understanding Existing Tests](#understanding-existing-tests)
  + [Test Integration with Dependencies](#test-integration-with-dependencies)
  + [Run Your Enhanced Test Suite](#run-your-enhanced-test-suite)
* [Conclusion](#conclusion)
  + [What You've Learned](#what-youve-learned)
  + [Next Steps](#next-steps)
  + [Resources for Continued Learning](#resources-for-continued-learning)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.