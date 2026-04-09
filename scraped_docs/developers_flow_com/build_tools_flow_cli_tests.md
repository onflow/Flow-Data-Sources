# Source: https://developers.flow.com/build/tools/flow-cli/tests

Running Cadence Tests | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                      - [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Running Cadence Tests

On this page

# Running Cadence Tests

The Flow CLI provides a straightforward command to execute Cadence tests, which allows developers to validate their scripts and smart contracts effectively.

To run all tests in your project, simply use:

`_10

flow test`

The `flow test` command automatically discovers and runs all test scripts in your project that end with `_test.cdc`.

info

The `test` command requires a properly initialized configuration. If you haven’t set up your Flow project yet, refer to the [flow init](/build/tools/flow-cli/flow.json/initialize-configuration) guide for assistance.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you run your tests, ensure that your contracts are properly configured in your `flow.json` file, particularly any necessary testing aliases.

### Set up testing aliases in contracts[​](#set-up-testing-aliases-in-contracts "Direct link to Set up testing aliases in contracts")

If your tests involve contract deployment or contract interaction, you need to add your contracts to the `contracts` section in the `flow.json` configuration file. Specifically, include the contract name, source location, and an address alias for the `testing` environment.

Example `flow.json` configuration:

`_19

{

_19

"contracts": {

_19

"Counter": {

_19

"source": "cadence/contracts/Counter.cdc",

_19

"aliases": {

_19

"testing": "0x0000000000000007"

_19

}

_19

}

_19

},

_19

"networks": {

_19

// ... your network configurations

_19

},

_19

"accounts": {

_19

// ... your account configurations

_19

},

_19

"deployments": {

_19

// ... your deployment configurations

_19

}

_19

}`

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

info

For more information on how to set up contracts and aliases, refer to the [Flow CLI Configuration](/build/tools/flow-cli/flow.json/initialize-configuration) documentation.

## Example use[​](#example-use "Direct link to Example use")

This example assumes you have a test script named `test_script_test.cdc` in your project directory, which verifies the functionality of a Cadence script executed in the testing environment:

`_14

// test_script_test.cdc

_14

import Test

_14

_14

access(all) fun testSumOfTwo() {

_14

let scriptResult = Test.executeScript(

_14

"access(all) fun main(a: Int, b: Int): Int { return a + b }",

_14

[2, 3]

_14

)

_14

_14

Test.expect(scriptResult, Test.beSucceeded())

_14

_14

let sum = scriptResult.returnValue! as! Int

_14

Test.assertEqual(5, sum)

_14

}`

This script defines a single test case, `testSumOfTwo`, which checks if a Cadence script that adds two integers `(a + b)` works as expected. The test passes if the result matches the expected value of `5`.

You can run all tests in your project with the CLI:

`_10

$ flow test`

The Flow CLI will discover all test scripts that end with `_test.cdc` and execute them. The results will be displayed in the terminal:

`_10

Test results:

_10

- PASS: test_script_test.cdc > testSumOfTwo`

To learn more about how to write tests in Cadence, visit the [Cadence Testing Framework](/build/cadence/smart-contracts/testing) documentation.

---

### Run specific tests and files[​](#run-specific-tests-and-files "Direct link to Run specific tests and files")

To run specific test scripts or directories, by provide their paths:

`_10

flow test path/to/your/test_script_test.cdc path/to/another_test.cdc tests/subsuite/`

This executes only the tests contained in the specified files and directories.

---

## Flags[​](#flags "Direct link to Flags")

The `flow test` command supports several flags that provide additional functionality to manage test execution and coverage reports.

### **Coverage report**[​](#coverage-report "Direct link to coverage-report")

* **Flag:** `--cover`
* **Default:** `false`

The `--cover` flag calculates the coverage of the code being tested, which helps you identify untested parts of your scripts and contracts.

`_10

$ flow test --cover`

Sample output:

`_10

Test results:

_10

- PASS: test_script_test.cdc > testSumOfTwo

_10

Coverage: 96.5% of statements`

---

### Coverage report output file[​](#coverage-report-output-file "Direct link to Coverage report output file")

* **Flag:** `--coverprofile`
* **Valid Inputs:** A valid filename with extension `.json` or `.lcov`
* **Default:** `"coverage.json"`

Use the `--coverprofile` flag to specify the output file for the coverage report.

Example:

`_10

$ flow test --cover --coverprofile="coverage.lcov"`

The generated coverage file can then be inspected:

`_10

$ cat coverage.lcov`

### Coverage code type[​](#coverage-code-type "Direct link to Coverage code type")

* **Flag:** `--covercode`
* **Valid Inputs:** `"all"` (default) or `"contracts"`
* **Default:** `"all"`

The `--covercode` flag lets you limit the coverage report to specific types of code. Set the value to `"contracts"` to exclude scripts and transactions from the coverage analysis.

`_10

$ flow test --cover --covercode="contracts"`

Sample output when no contracts are present:

`_10

Test results:

_10

- PASS: test_script_test.cdc > testSumOfTwo

_10

There are no statements to cover`

> **Note:** In this example, the coverage report is empty because the `--covercode` flag is set to `"contracts"`, and the test script only contains scripts, not contracts.

### Random execution of test cases[​](#random-execution-of-test-cases "Direct link to Random execution of test cases")

* **Flag:** `--random`
* **Default:** `false`

Use the `--random` flag to execute test cases in a random order. This can help identify issues that may arise due to test dependencies or the order in which tests are run.

`_10

flow test --random`

### Seed for random execution[​](#seed-for-random-execution "Direct link to Seed for random execution")

* **Flag:** `--seed`
* **Default:** `0`

Use the `--seed` flag to specify a seed value for the random execution order of test cases. This allows you to reproduce a specific random order when you use the same seed value, which is helpful to debug flaky tests.

`_10

flow test --seed=12345`

info

If both `--random` and `--seed` are provided, the `--random` flag will be ignored, and the seed value from `--seed` will be used for randomization.

---

### Run specific test by name[​](#run-specific-test-by-name "Direct link to Run specific test by name")

* **Flag:** `--name`
* **Default:** `""` (empty string)

Use the `--name` flag to run only tests that match the given name. This is useful when you want to execute a specific test function within your test scripts.

`_10

flow test --name=testSumOfTwo`

This command will run only the test function named `testSumOfTwo` across all test scripts that contain it.

To dive deeper into testing the functionality of your Cadence scripts and contracts, explore the [Cadence Testing Framework](/build/cadence/smart-contracts/testing) documentation.

---

### Fork testing flags[​](#fork-testing-flags "Direct link to Fork testing flags")

Run tests against forked mainnet or testnet state. For a step-by-step tutorial, see: [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing). For background and best practices, see the guide: [Testing Strategy on Flow](/build/cadence/smart-contracts/testing-strategy).

#### Configure fork tests[​](#configure-fork-tests "Direct link to Configure fork tests")

**Recommended**: Use the `#test_fork` pragma in your test file:

`_10

#test_fork(network: "mainnet", height: nil)

_10

_10

import Test

_10

_10

access(all) fun testAgainstMainnet() {

_10

// Test runs against mainnet state

_10

}`

Then run with:

`_10

flow test`

The pragma configures fork testing directly in your test files, which makes the tests self-documenting. You can also use CLI flags (documented below) to override or configure fork tests and not modify test files.

#### --fork[​](#--fork "Direct link to --fork")

* Type: `string`
* Default: `""` (empty). If provided without a value, defaults to `mainnet`.

Fork tests from a network defined in `flow.json`. The CLI resolves the GRPC access host and chain ID from the selected network configuration.

`_10

flow test --fork # Uses mainnet by default

_10

flow test --fork testnet # Uses testnet

_10

flow test --fork mynet # Uses a custom network defined in flow.json`

Requirements:

* The network must exist in `flow.json`.
* The network must have a valid `host` configured.

#### --fork-host[​](#--fork-host "Direct link to --fork-host")

* Type: `string`
* Default: `""`

Directly specify a GRPC access node host. This bypasses the `flow.json` network lookup.

`_10

flow test --fork-host access.mainnet.nodes.onflow.org:9000`

See public access node URLs in [Flow Networks](/protocol/flow-networks).

#### --fork-height[​](#--fork-height "Direct link to --fork-height")

* Type: `uint64`
* Default: `0`

Pin the fork to a specific block height for historical state testing. Only blocks from the current spork (since the most recent network upgrade) are available via public access nodes; earlier blocks are not accessible via public access nodes.

`_10

flow test --fork mainnet --fork-height 85432100`

note

Historical data beyond spork boundaries is not available via standard access nodes. See the [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/tests.md)

Last updated on **Apr 8, 2026** by **0xLisanAlGaib**

[Previous

Dependency Manager](/build/tools/flow-cli/dependency-manager)[Next

Generating Cadence Boilerplate](/build/tools/flow-cli/generate)

###### Rate this page

😞😐😊

Copy as Markdown

* [Prerequisites](#prerequisites)
  + [Set up testing aliases in contracts](#set-up-testing-aliases-in-contracts)* [Example use](#example-use)
    + [Run specific tests and files](#run-specific-tests-and-files)* [Flags](#flags)
      + [**Coverage report**](#coverage-report)+ [Coverage report output file](#coverage-report-output-file)+ [Coverage code type](#coverage-code-type)+ [Random execution of test cases](#random-execution-of-test-cases)+ [Seed for random execution](#seed-for-random-execution)+ [Run specific test by name](#run-specific-test-by-name)+ [Fork testing flags](#fork-testing-flags)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.