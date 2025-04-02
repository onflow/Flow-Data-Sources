# Source: https://developers.flow.com/build/smart-contracts/testing

Testing Your Contracts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)

  + [Learn Cadence ↗️](/build/learn-cadence)
  + [Smart Contracts on Flow](/build/smart-contracts/overview)
  + [Deploying Contracts](/build/smart-contracts/deploying)
  + [Testing Your Contracts](/build/smart-contracts/testing)
  + [Best Practices](/build/smart-contracts/best-practices/security-best-practices)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Writing and Deploying Smart Contracts
* Testing Your Contracts

On this page

# Testing Your Contracts

Testing is an essential part of smart contract development to ensure the correctness and reliability of your code. The Cadence Testing Framework provides a convenient way to write tests for your contracts, scripts and transactions which allows you to verify the functionality and correctness of your smart contracts.

## Install Flow CLI[​](#install-flow-cli "Direct link to Install Flow CLI")

The [Flow CLI](/tools/flow-cli) is the primary tool for developing, testing, and deploying smart contracts to the Flow network.

If you haven't installed the Flow CLI yet and have [homebrew](https://brew.sh/) installed, simply run `brew install flow-cli`. Alternatively, refer to the Flow CLI [installation instructions](/tools/flow-cli/install).

## Create a new project[​](#create-a-new-project "Direct link to Create a new project")

In your preferred code editor, create a new directory for your project and navigate to it in the terminal. Then initialize a new Flow project by running the command `flow init`. This will create a `flow.json` config file that contains the [project's configuration](/tools/flow-cli/flow.json/configuration).

`_10

mkdir test-cadence

_10

cd test-cadence

_10

flow init`

## Write a simple smart contract[​](#write-a-simple-smart-contract "Direct link to Write a simple smart contract")

In your code editor, create a new file called `calculator.cdc` and add the following code:

calculator.cdc

`_16

access(all) contract Calculator {

_16

access(all)

_16

fun add(a: Int, b: Int): Int {

_16

return a + b

_16

}

_16

_16

access(all)

_16

fun subtract(a: Int, b: Int): Int {

_16

return a - b

_16

}

_16

_16

access(all)

_16

fun multiply(a: Int, b: Int): Int {

_16

return a * b

_16

}

_16

}`

## Add the smart contract to the config[​](#add-the-smart-contract-to-the-config "Direct link to Add the smart contract to the config")

Next up, we need to add our new contract in the `contracts` key in the `flow.json` config file. More specifically, we need to add the contract name, location and an address alias for the `testing` environment.

`_13

{

_13

"contracts": {

_13

"Calculator": {

_13

"source": "./calculator.cdc",

_13

"aliases": {

_13

"testing": "0x0000000000000007"

_13

}

_13

}

_13

},

_13

"networks": {...},

_13

"accounts": {...},

_13

"deployments": {...}

_13

}`

For the time being, the address for the `testing` alias, can be one of:

* `0x0000000000000005`
* `0x0000000000000006`
* `0x0000000000000007`
* `0x0000000000000008`
* `0x0000000000000009`
* `0x000000000000000a`
* `0x000000000000000b`
* `0x000000000000000c`
* `0x000000000000000d`
* `0x000000000000000e`

In the next release, there will be `20` addresses for contract deployment during testing.

## Write unit tests[​](#write-unit-tests "Direct link to Write unit tests")

In the same directory, create a new file called `calculator_test.cdc` and add the following code:

calculator\_test.cdc

`_22

import Test

_22

import "Calculator" // contract name from the previous step

_22

_22

access(all)

_22

fun setup() {

_22

let err = Test.deployContract(

_22

name: "Calculator",

_22

path: "./calculator.cdc",

_22

arguments: []

_22

)

_22

Test.expect(err, Test.beNil())

_22

}

_22

_22

access(all)

_22

fun testAdd() {

_22

Test.assertEqual(5, Calculator.add(a: 2, b: 3))

_22

}

_22

_22

access(all)

_22

fun testSubtract() {

_22

Test.assertEqual(2, Calculator.subtract(a: 5, b: 3))

_22

}`

This code:

* imports the `Calculator` contract from the `calculator.cdc` file (according to `flow.json`)
* deploys the `Calculator` contract to the address specified in the `testing` alias
* defines two test cases: `testAdd()` and `testSubtract()`
* calls `add()` and `subtract()` methods with different input values respectively.

## Running the test cases[​](#running-the-test-cases "Direct link to Running the test cases")

To run the test cases, use the following command in the terminal:

`_10

flow test --cover --covercode="contracts" calculator_test.cdc`

This command uses the Flow CLI to run the test cases and display the output. You should see the following output:

`_10

Test results: "calculator_test.cdc"

_10

- PASS: testAdd

_10

- PASS: testSubtract

_10

Coverage: 66.7% of statements`

This output indicates that both test cases ran successfully, and the two smart contract methods are functioning as expected. With the supplied flags (`--cover` & `--covercode="contracts"`), we also get code coverage insights for the contracts under testing. The code coverage percentage is `66.7%`, because we have not added a test case for the `multiply` method. By viewing the auto-generated `coverage.json` file, we see:

`_16

{

_16

"coverage": {

_16

"A.0000000000000007.Calculator": {

_16

"line_hits": {

_16

"14": 0,

_16

"4": 1,

_16

"9": 1

_16

},

_16

"missed_lines": [

_16

14

_16

],

_16

"statements": 3,

_16

"percentage": "66.7%"

_16

}

_16

}

_16

}`

Line 14 from the `Calculator` smart contract is marked as missed. This is the line:

`_10

return a * b`

which is the `multiply` method.

By adding a test case for the above method:

calculator\_test.cdc

`_10

...

_10

_10

access(all)

_10

fun testMultiply() {

_10

Test.assertEqual(10, Calculator.multiply(a: 2, b: 5))

_10

}`

our code coverage percentage goes to `100%`:

`_10

flow test --cover --covercode="contracts" calculator_test.cdc

_10

_10

Test results: "calculator_test.cdc"

_10

- PASS: testAdd

_10

- PASS: testSubtract

_10

- PASS: testMultiply

_10

Coverage: 100.0% of statements`

## Advanced Testing Techniques[​](#advanced-testing-techniques "Direct link to Advanced Testing Techniques")

The Cadence testing framework provides various features and techniques for writing comprehensive test scenarios. Some of these include:

* [**Code Coverage**](https://github.com/m-Peter/flow-code-coverage): You can use the `--cover` flag with the `flow test` command to view code coverage results when running your tests. This allows you to identify areas of your code that are not adequately covered by your test inputs.
* **Test Helpers**: Test helpers are reusable functions that help you set up the initial state for your test files. You can define test helpers in a Cadence program and use them in your test files by importing it whenever needed.
* [**Assertions**](https://cadence-lang.org/docs/testing-framework#assertions): The testing framework provides built-in assertion functions, such as `assertEqual`, `beNil`, `beEmpty`, `contain`, to help you verify the expected behavior of your smart contracts.
* **Test Suites**: You can organize your test files into test suites to improve the readability and maintainability of your test code. Test suites allow you to group related test cases and set up common test helpers for all the tests in the suite.
* [**Integration tests**](https://github.com/bjartek/overflow): In our previous example, we would directly call the available methods on the contract under test. This is generally categorized as unit testing. You can also write integration tests, by executing scripts & transactions to interact with the contracts under testing. If you would like to write your tests in Go, instead of Cadence, you can use [Overflow tool](https://github.com/bjartek/overflow) to run integration tests against either an local emulator, testnet, mainnet or an in memory instance of the flow-emulator.

By leveraging these advanced testing techniques, you can write more robust and reliable smart contracts in Cadence. In this example, we set up a basic testing environment, wrote a simple smart contract in Cadence, and created a test file to verify its functionality. We then used the Flow CLI to run the test file and confirm that the smart contract is working correctly.

This is a basic example, and there are many more advanced features and techniques you can explore when working with the Cadence Testing Framework.

For more in-depth tutorials and documentation, refer to the official [Cadence language documentation](https://cadence-lang.org/) and the [Flow CLI documentation](/tools/flow-cli).

## Testing Requirements[​](#testing-requirements "Direct link to Testing Requirements")

It is suggested to follow the following best practices:

* Every publicly exposed feature of a contract and its resources should have unit tests that check both for success with correct input *and* for failure with incorrect input.
  These tests should be capable of being run locally with the Flow emulator, with no or minimal extra resources or configuration, and with a single command.
* Each user story or workflow that uses the smart contracts should have an integration test that ensures that the series of steps required to complete it does so successfully with test data.

Make sure you test all contracts - and the integration into your application extensively before proceeding to the mainnet.
You should aim to replicate all conditions as closely as possible to the usage patterns on mainnet.

## Writing Tests[​](#writing-tests "Direct link to Writing Tests")

There are official SDKs/frameworks for Flow in Cadence, Go and JavaScript.

In all three cases, the test code will need to deploy the contracts, configure accounts to interact with them and send transactions to them. It will then have to wait for the transactions to be sealed and check the results by catching exceptions, checking for events, and querying state using scripts.

### Cadence tests[​](#cadence-tests "Direct link to Cadence tests")

Cadence comes with built-in support for code coverage, as well as a native testing framework which allows developers to write their tests using Cadence.
This framework is bundled with the [Flow CLI](/tools/flow-cli) tool, which includes a dedicated command for running tests (`flow test`).

You can find examples of Cadence tests in the following projects: [hybrid-custody](https://github.com/onflow/hybrid-custody/tree/main/test), [flow-nft](https://github.com/onflow/flow-nft/tree/master/tests), [flow-ft](https://github.com/onflow/flow-ft/tree/master/tests).
Visit the [documentation](https://cadence-lang.org/docs/testing-framework) to view all the available features.

The [Hybrid Custody](https://github.com/onflow/hybrid-custody#readme) project is a prime example which utilizes both the Cadence testing framework and code coverage in its CI.

![Hybrid Custody CI](/assets/images/hybrid-custody-ci-95f5b0c24d57f3e8eb2bb20ed0632035.png)

There is also a [repository](https://github.com/m-Peter/flow-code-coverage#readme) which contains some sample contracts and their tests.

![Automated CI Coverage Report](/assets/images/codecov-in-pr-3fdef235a4f0f8d639c73c585700ec91.png)

![Coverage Report Visualization](/assets/images/codecov-insights-8de85dd4cb9c215441180bd4071ba697.png)

info

The Cadence testing framework utilizes the emulator under the hood.

### Go Tests[​](#go-tests "Direct link to Go Tests")

Tests in Go can be written using [flow-go-sdk](https://github.com/onflow/flow-go-sdk) and the go test command.

You can find examples of Go tests in the following projects: [flow-core-contracts](https://github.com/onflow/flow-core-contracts/tree/master/lib/go/test), [flow-nft](https://github.com/onflow/flow-nft/tree/master/lib/go/test), [flow-ft](https://github.com/onflow/flow-ft/tree/master/lib/go/test).

info

These tests are tied to the emulator but can be refactored to run on testnet

## Testing Your Application[​](#testing-your-application "Direct link to Testing Your Application")

### Automated Testing of Contract Code[​](#automated-testing-of-contract-code "Direct link to Automated Testing of Contract Code")

All contracts should include test coverage for *all contract functions*. Make sure you've accounted for success and failure cases appropriately.

Tests should also be runnable in automated environments (CI). You can use the [Cadence testing utils](https://cadence-lang.org/docs/testing-framework) to create tests for your smart contract code.

### Stress Testing Live Applications Before Mainnet[​](#stress-testing-live-applications-before-mainnet "Direct link to Stress Testing Live Applications Before Mainnet")

Once you deployed your application to the testnet, you should record how your application handles non-trivial amounts of traffic to ensure there are no issues.

tip

Get familiar with the [Cadence anti-patterns](https://cadence-lang.org/docs/anti-patterns) to avoid avoid problematic or unintended behavior.

## References[​](#references "Direct link to References")

* [Reference documentation for Cadence testing](https://cadence-lang.org/docs/testing-framework)
* [Overflow](https://github.com/bjartek/overflow) is a powerful Golang-based DSL for efficient testing and execution of blockchain interactions
* projects that have good examples of robust test cases:
  + [hybrid-custody](https://github.com/onflow/hybrid-custody/tree/main/test),
  + [flow-nft](https://github.com/onflow/flow-nft/tree/master/tests),
  + [flow-ft](https://github.com/onflow/flow-ft/tree/master/tests).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/smart-contracts/testing.md)

Last updated on **Mar 27, 2025** by **Brian Doyle**

[Previous

Deploying Contracts](/build/smart-contracts/deploying)[Next

Security Best Practices](/build/smart-contracts/best-practices/security-best-practices)

###### Rate this page

😞😐😊

* [Install Flow CLI](#install-flow-cli)
* [Create a new project](#create-a-new-project)
* [Write a simple smart contract](#write-a-simple-smart-contract)
* [Add the smart contract to the config](#add-the-smart-contract-to-the-config)
* [Write unit tests](#write-unit-tests)
* [Running the test cases](#running-the-test-cases)
* [Advanced Testing Techniques](#advanced-testing-techniques)
* [Testing Requirements](#testing-requirements)
* [Writing Tests](#writing-tests)
  + [Cadence tests](#cadence-tests)
  + [Go Tests](#go-tests)
* [Testing Your Application](#testing-your-application)
  + [Automated Testing of Contract Code](#automated-testing-of-contract-code)
  + [Stress Testing Live Applications Before Mainnet](#stress-testing-live-applications-before-mainnet)
* [References](#references)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.