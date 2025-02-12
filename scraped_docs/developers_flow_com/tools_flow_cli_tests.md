# Source: https://developers.flow.com/tools/flow-cli/tests




Running Cadence Tests | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* [Flow CLI](/tools/flow-cli)
* Running Cadence Tests
On this page
# Running Cadence Tests

The Flow CLI provides a straightforward command to execute Cadence tests, enabling developers to validate their scripts and smart contracts effectively.

To run all tests in your project, simply use:

 `_10flow test`

The `flow test` command automatically discovers and runs all test scripts in your project that end with `_test.cdc`.

> **Note:** The `test` command requires a properly initialized configuration. If you haven’t set up your Flow project yet, refer to the [flow init](/tools/flow-cli/flow.json/initialize-configuration) guide for assistance.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before running your tests, ensure that your contracts are properly configured in your `flow.json` file, including any necessary testing aliases.

### Setting Up Testing Aliases in Contracts[​](#setting-up-testing-aliases-in-contracts "Direct link to Setting Up Testing Aliases in Contracts")

If your tests involve deploying or interacting with contracts, you need to add your contracts to the `contracts` section in the `flow.json` configuration file. Specifically, include the contract name, source location, and an address alias for the `testing` environment.

Example `flow.json` configuration:

 `_19{_19 "contracts": {_19 "Counter": {_19 "source": "cadence/contracts/Counter.cdc",_19 "aliases": {_19 "testing": "0x0000000000000007"_19 }_19 }_19 },_19 "networks": {_19 // ... your network configurations_19 },_19 "accounts": {_19 // ... your account configurations_19 },_19 "deployments": {_19 // ... your deployment configurations_19 }_19}`

For the `testing` alias, you can use one of the following addresses:

* `0x0000000000000005`
* `0x0000000000000006`
* `0x0000000000000007`
* `0x0000000000000008`
* `0x0000000000000009`
* `0x000000000000000A`
* `0x000000000000000B`
* `0x000000000000000C`
* `0x000000000000000D`
* `0x000000000000000E`

> **Note**: For more information on setting up contracts and aliases, refer to the [Flow CLI Configuration](/tools/flow-cli/flow.json/initialize-configuration) documentation.

## Example Usage[​](#example-usage "Direct link to Example Usage")

Assuming you have a test script named `test_script_test.cdc` in your project directory, which verifies the functionality of a Cadence script executed in the testing environment:

 `_16// test_script_test.cdc_16import Test_16_16access(all) let blockchain = Test.newEmulatorBlockchain()_16_16access(all) fun testSumOfTwo() {_16 let scriptResult = blockchain.executeScript(_16 "access(all) fun main(a: Int, b: Int): Int { return a + b }",_16 [2, 3]_16 )_16_16 Test.expect(scriptResult, Test.beSucceeded())_16_16 let sum = scriptResult.returnValue! as! Int_16 Test.assertEqual(5, sum)_16}`

This script defines a single test case, `testSumOfTwo`, which checks if a Cadence script that adds two integers `(a + b)` works as expected. The test passes if the result matches the expected value of `5`.

You can run all tests in your project using the CLI:

 `_10$ flow test`

The Flow CLI will discover all test scripts ending with `_test.cdc` and execute them. The results will be displayed in the terminal:

 `_10Test results:_10- PASS: test_script_test.cdc > testSumOfTwo`

To learn more about writing tests in Cadence, visit the [Cadence Testing Framework](/build/smart-contracts/testing) documentation.

---

### Running Specific Tests[​](#running-specific-tests "Direct link to Running Specific Tests")

If you wish to run a specific test script rather than all tests, you can provide the path to the test file:

 `_10flow test path/to/your/test_script_test.cdc`

This will execute only the tests contained in the specified file.

---

## Flags[​](#flags "Direct link to Flags")

The `flow test` command supports several flags that provide additional functionality for managing test execution and coverage reporting.

### **Coverage Report**[​](#coverage-report "Direct link to coverage-report")

* **Flag:** `--cover`
* **Default:** `false`

The `--cover` flag calculates the coverage of the code being tested, helping you identify untested parts of your scripts and contracts.

 `_10$ flow test --cover`

Sample output:

 `_10Test results:_10- PASS: test_script_test.cdc > testSumOfTwo_10Coverage: 96.5% of statements`

---

### Coverage Report Output File[​](#coverage-report-output-file "Direct link to Coverage Report Output File")

* **Flag:** `--coverprofile`
* **Valid Inputs:** A valid filename with extension `.json` or `.lcov`
* **Default:** `"coverage.json"`

Use the `--coverprofile` flag to specify the output file for the coverage report.

Example:

 `_10$ flow test --cover --coverprofile="coverage.lcov"`

The generated coverage file can then be inspected:

 `_10$ cat coverage.lcov`
### Coverage Code Type[​](#coverage-code-type "Direct link to Coverage Code Type")

* **Flag:** `--covercode`
* **Valid Inputs:** `"all"` (default) or `"contracts"`
* **Default:** `"all"`

The `--covercode` flag lets you limit the coverage report to specific types of code. Setting the value to `"contracts"` excludes scripts and transactions from the coverage analysis.

 `_10$ flow test --cover --covercode="contracts"`

Sample output when no contracts are present:

 `_10Test results:_10- PASS: test_script_test.cdc > testSumOfTwo_10There are no statements to cover`
> **Note:** In this example, the coverage report is empty because the `--covercode` flag is set to `"contracts"`, and the test script only contains scripts, not contracts.

### Random Execution of Test Cases[​](#random-execution-of-test-cases "Direct link to Random Execution of Test Cases")

* **Flag:** `--random`
* **Default:** `false`

Use the `--random` flag to execute test cases in a random order. This can help identify issues that may arise due to test dependencies or the order in which tests are run.

 `_10flow test --random`
### Seed for Random Execution[​](#seed-for-random-execution "Direct link to Seed for Random Execution")

* **Flag:** `--seed`
* **Default:** `0`

Use the `--seed` flag to specify a seed value for the random execution order of test cases. This allows you to reproduce a specific random order by using the same seed value, which is helpful for debugging flaky tests.

 `_10flow test --seed=12345`
> **Note:** If both `--random` and `--seed` are provided, the `--random` flag will be ignored, and the seed value from `--seed` will be used for randomization.

---

### Run Specific Test by Name[​](#run-specific-test-by-name "Direct link to Run Specific Test by Name")

* **Flag:** `--name`
* **Default:** `""` (empty string)

Use the `--name` flag to run only tests that match the given name. This is useful when you want to execute a specific test function within your test scripts.

 `_10flow test --name=testSumOfTwo`

This command will run only the test function named `testSumOfTwo` across all test scripts that contain it.

To dive deeper into testing the functionality of your Cadence scripts and contracts, explore the [Cadence Testing Framework](https://cadence-lang.org/docs/testing-framework) documentation.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/tests.md)Last updated on **Jan 28, 2025** by **Giovanni Sanchez**[PreviousDependency Manager](/tools/flow-cli/dependency-manager)[NextCadence Linter](/tools/flow-cli/lint)
###### Rate this page

😞😐😊

* [Prerequisites](#prerequisites)
  + [Setting Up Testing Aliases in Contracts](#setting-up-testing-aliases-in-contracts)
* [Example Usage](#example-usage)
  + [Running Specific Tests](#running-specific-tests)
* [Flags](#flags)
  + [**Coverage Report**](#coverage-report)
  + [Coverage Report Output File](#coverage-report-output-file)
  + [Coverage Code Type](#coverage-code-type)
  + [Random Execution of Test Cases](#random-execution-of-test-cases)
  + [Seed for Random Execution](#seed-for-random-execution)
  + [Run Specific Test by Name](#run-specific-test-by-name)
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

