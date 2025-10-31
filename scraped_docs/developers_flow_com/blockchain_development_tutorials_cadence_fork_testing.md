# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/fork-testing

Fork Testing with Cadence | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* Fork Testing

On this page

# Fork Testing with Cadence

This tutorial teaches you how to run your Cadence tests against a snapshot of Flow mainnet using `flow test --fork`. You'll learn how to test your contracts against real deployed contracts and production data without needing to deploy anything to a live network or bootstrap test accounts.

Fork testing bridges the gap between isolated local unit tests and testnet deployments. It enables you to validate your contracts work correctly with real on-chain state, test integrations with deployed contracts, and debug issues using historical blockchain data—all in a safe, local environment.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

After completing this tutorial, you'll be able to:

* **Run Cadence tests against forked networks** using `flow test --fork`
* **Test contracts that depend on real mainnet contracts** without manual setup
* **Use account impersonation** to execute transactions as any mainnet account
* **Read from production blockchain state** in your test suite
* **Pin tests to specific block heights** for historical debugging
* **Integrate fork testing** into your development workflow

## What You'll Build[​](#what-youll-build "Direct link to What You'll Build")

You'll create a complete fork testing setup that demonstrates:

* Reading from the live FlowToken contract on mainnet
* Deploying your own contract that interacts with mainnet contracts
* Testing custom logic against real account balances and state
* Executing transactions using impersonated mainnet accounts
* A reusable pattern for integration testing your Flow applications

### Reproducibility first[​](#reproducibility-first "Direct link to Reproducibility first")

Pin a specific block height when you need reproducible results:

`_10

flow test --fork mainnet --fork-height <BLOCK_HEIGHT>`

Document the pin heights you rely on (for example in CI variables or a simple file in the repo) and update them via a dedicated freshness PR. For best results, keep a per‑spork stable pin and also run a "latest" freshness job.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Flow CLI[​](#flow-cli "Direct link to Flow CLI")

This tutorial requires [Flow CLI](/build/tools/flow-cli) v1.8.0 or later installed. If you haven't installed it yet and have [homebrew](https://brew.sh) installed, run:

`_10

brew install flow-cli`

For other operating systems, refer to the [installation guide](/build/tools/flow-cli/install).

### Basic Cadence Testing Knowledge[​](#basic-cadence-testing-knowledge "Direct link to Basic Cadence Testing Knowledge")

You should be familiar with writing basic Cadence tests. If you're new to Cadence testing, start with [Testing Smart Contracts](/build/cadence/smart-contracts/testing-strategy) first.

### Network Access[​](#network-access "Direct link to Network Access")

You'll need network access to Flow's public access nodes. The tutorial uses these endpoints, which are freely available:

* Mainnet: `access.mainnet.nodes.onflow.org:9000`
* Testnet: `access.devnet.nodes.onflow.org:9000`

info

This tutorial covers `flow test --fork` (running tests against forked network state), which is different from `flow emulator --fork` (starting the emulator in fork mode for manual interaction).

## Create Your Project[​](#create-your-project "Direct link to Create Your Project")

Navigate to your development directory and create a new Flow project:

`_10

mkdir fork-testing-demo

_10

cd fork-testing-demo

_10

flow init --yes`

The `--yes` flag accepts defaults non-interactively. `flow init` is interactive by default and can scaffold various templates.

Alternatively, create the directory and initialize in one command:

`_10

flow init fork-testing-demo --yes

_10

cd fork-testing-demo`

## Install Dependencies[​](#install-dependencies "Direct link to Install Dependencies")

Use the [Dependency Manager](/build/tools/flow-cli/dependency-manager) to install the `FlowToken` and `FungibleToken` contracts:

`_10

flow dependencies install FlowToken FungibleToken`

This downloads the contracts and their dependencies into the `imports/` folder and updates your `flow.json` with the correct addresses and aliases across all networks (mainnet, testnet, emulator).

Your `flow.json` will now include an entry like:

`_12

{

_12

"dependencies": {

_12

"FlowToken": {

_12

"source": "mainnet://1654653399040a61.FlowToken",

_12

"aliases": {

_12

"emulator": "0ae53cb6e3f42a79",

_12

"mainnet": "1654653399040a61",

_12

"testnet": "7e60df042a9c0868"

_12

}

_12

}

_12

}

_12

}`

Your `flow.json` should now have the mainnet and testnet networks configured from `flow init`. In fork mode, contract imports automatically resolve to the correct network addresses.

## Test Reading Live State[​](#test-reading-live-state "Direct link to Test Reading Live State")

Generate a script to read `FlowToken` supply:

`_10

flow generate script GetFlowTokenSupply`

Open `cadence/scripts/GetFlowTokenSupply.cdc` and replace its contents with:

cadence/scripts/GetFlowTokenSupply.cdc

`_10

import "FlowToken"

_10

_10

access(all) fun main(): UFix64 {

_10

return FlowToken.totalSupply

_10

}`

Generate the test file:

`_10

flow generate test FlowToken`

Open `cadence/tests/FlowToken_test.cdc` and replace its contents with:

cadence/tests/FlowToken\_test.cdc

`_13

import Test

_13

_13

access(all) fun testFlowTokenSupplyIsPositive() {

_13

let scriptResult = Test.executeScript(

_13

Test.readFile("../scripts/GetFlowTokenSupply.cdc"),

_13

[]

_13

)

_13

_13

Test.expect(scriptResult, Test.beSucceeded())

_13

_13

let supply = scriptResult.returnValue! as! UFix64

_13

Test.assert(supply > 0.0, message: "FlowToken supply should be positive")

_13

}`

Notes:

* Use `Test.executeScript()` to read contract state
* The script imports `FlowToken` by name - the dependency manager handles address resolution
* In fork mode, this automatically uses the mainnet FlowToken contract
* Extract the return value with proper type casting and assert on it
* File paths in `Test.readFile()` are relative to the test file location (use `../scripts/` from `cadence/tests/`)

#### Quick verify[​](#quick-verify "Direct link to Quick verify")

Run just this test file against a fork to confirm your setup works:

`_10

flow test cadence/tests/FlowToken_test.cdc --fork mainnet`

Target testnet instead:

`_10

flow test cadence/tests/FlowToken_test.cdc --fork testnet`

You should see the test PASS. If not, verify your network host in `flow.json` and that dependencies are installed.

## Deploy and Test Your Contract[​](#deploy-and-test-your-contract "Direct link to Deploy and Test Your Contract")

Now you'll create a contract that depends on FlowToken and test it against the forked mainnet state—no need to bootstrap tokens or set up test accounts.

### Create a Test Account[​](#create-a-test-account "Direct link to Create a Test Account")

Create a new account for deploying your contract:

`_10

flow accounts create`

Follow the prompts:

* Select "mainnet" for the network
* Name your account as desired

This will output the new account address. Use this address as the mainnet alias for your contract in flow.json.

note

This creates a local account with a mainnet-format address for fork testing. When you're ready to deploy to actual mainnet, you'll use this same account—see the [Deploying Contracts guide](/build/cadence/smart-contracts/deploying) for details.

### Create a Contract that Uses `FlowToken`[​](#create-a-contract-that-uses-flowtoken "Direct link to create-a-contract-that-uses-flowtoken")

Generate a new contract:

`_10

flow generate contract TokenChecker`

This creates `cadence/contracts/TokenChecker.cdc` and adds it to `flow.json`. Now update the contract with your logic:

cadence/contracts/TokenChecker.cdc

`_18

import "FlowToken"

_18

_18

access(all) contract TokenChecker {

_18

_18

access(all) fun checkBalance(address: Address): UFix64 {

_18

let account = getAccount(address)

_18

_18

let vaultRef = account.capabilities

_18

.borrow<&FlowToken.Vault>(/public/flowTokenBalance)

_18

?? panic("Could not borrow FlowToken Vault reference")

_18

_18

return vaultRef.balance

_18

}

_18

_18

access(all) fun hasMinimumBalance(address: Address, minimum: UFix64): Bool {

_18

return self.checkBalance(address: address) >= minimum

_18

}

_18

}`

### Configure Contract in flow.json[​](#configure-contract-in-flowjson "Direct link to Configure Contract in flow.json")

Add the `TokenChecker` contract configuration to `flow.json`. The contract needs a **mainnet alias** so that imports can resolve properly during fork testing.

Update your `flow.json` to include the contract with aliases, using the address you generated in the previous step:

`_16

{

_16

"contracts": {

_16

"TokenChecker": {

_16

"source": "cadence/contracts/TokenChecker.cdc",

_16

"aliases": {

_16

"testing": "0000000000000008",

_16

"mainnet": "<from_previous_step>"

_16

}

_16

}

_16

},

_16

"accounts": {

_16

"mainnet-test": {

_16

"address": "<from_previous_step>"

_16

}

_16

}

_16

}`

**Note:** No local private key is required for forked tests. The accounts entry above is included so you can copy/reference the address in your config; keys can be omitted for fork tests. Contracts deploy to the testing environment at `testing` alias, and transactions that interact with forked state can use impersonation. The `Test.deployContract` function will automatically deploy your contract to the testing environment during test execution.

### Create Scripts for Testing[​](#create-scripts-for-testing "Direct link to Create Scripts for Testing")

Generate the scripts:

`_10

flow generate script CheckBalance

_10

flow generate script HasMinimumBalance`

Open `cadence/scripts/CheckBalance.cdc` and replace its contents with:

cadence/scripts/CheckBalance.cdc

`_10

import "TokenChecker"

_10

_10

access(all) fun main(addr: Address): UFix64 {

_10

return TokenChecker.checkBalance(address: addr)

_10

}`

Open `cadence/scripts/HasMinimumBalance.cdc` and replace its contents with:

cadence/scripts/HasMinimumBalance.cdc

`_10

import "TokenChecker"

_10

_10

access(all) fun main(addr: Address, min: UFix64): Bool {

_10

return TokenChecker.hasMinimumBalance(address: addr, minimum: min)

_10

}`

### Test Your Contract with Forked State[​](#test-your-contract-with-forked-state "Direct link to Test Your Contract with Forked State")

Generate the test file:

`_10

flow generate test TokenChecker`

Open `cadence/tests/TokenChecker_test.cdc` and replace its contents with:

cadence/tests/TokenChecker\_test.cdc

`_37

import Test

_37

_37

access(all) fun setup() {

_37

// Deploy TokenChecker to the test account

_37

let err = Test.deployContract(

_37

name: "TokenChecker",

_37

path: "../contracts/TokenChecker.cdc",

_37

arguments: []

_37

)

_37

Test.expect(err, Test.beNil())

_37

}

_37

_37

access(all) fun testCheckBalanceOnRealAccount() {

_37

// Test against a real mainnet account (Flow service account)

_37

let scriptResult = Test.executeScript(

_37

Test.readFile("../scripts/CheckBalance.cdc"),

_37

[Address(0x1654653399040a61)] // Flow service account on mainnet

_37

)

_37

_37

Test.expect(scriptResult, Test.beSucceeded())

_37

_37

let balance = scriptResult.returnValue! as! UFix64

_37

// The Flow service account should have a balance

_37

Test.assert(balance > 0.0, message: "Service account should have FLOW tokens")

_37

}

_37

_37

access(all) fun testHasMinimumBalance() {

_37

let scriptResult = Test.executeScript(

_37

Test.readFile("../scripts/HasMinimumBalance.cdc"),

_37

[Address(0x1654653399040a61), 1.0]

_37

)

_37

_37

Test.expect(scriptResult, Test.beSucceeded())

_37

_37

let hasMinimum = scriptResult.returnValue! as! Bool

_37

Test.assert(hasMinimum == true, message: "Service account should have at least 1 FLOW")

_37

}`

### What's Happening Here[​](#whats-happening-here "Direct link to What's Happening Here")

1. **Your contract uses FlowToken**: `TokenChecker` imports and interacts with the real FlowToken contract
2. **No bootstrapping needed**: When you run with `--fork`, real mainnet accounts (like `0x1654653399040a61`, the Flow service account) already have balances
3. **Test against real state**: You can query actual accounts and verify your contract logic works with production data
4. **Local deployment**: Your `TokenChecker` contract is deployed locally to the test environment, but it reads from forked mainnet state

## Execute Transactions with Account Impersonation[​](#execute-transactions-with-account-impersonation "Direct link to Execute Transactions with Account Impersonation")

Fork testing includes built-in account impersonation—you can execute transactions as **any mainnet account** without needing private keys. This lets you test interactions with real accounts and their existing state.

### Create Transactions[​](#create-transactions "Direct link to Create Transactions")

Generate the transactions:

`_10

flow generate transaction SetupFlowTokenVault

_10

flow generate transaction TransferTokens`

Open `cadence/transactions/SetupFlowTokenVault.cdc` and replace its contents with:

cadence/transactions/SetupFlowTokenVault.cdc

`_13

import "FungibleToken"

_13

import "FlowToken"

_13

_13

transaction {

_13

prepare(signer: auth(Storage, Capabilities) &Account) {

_13

if signer.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault) == nil {

_13

signer.storage.save(<-FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>()), to: /storage/flowTokenVault)

_13

let cap = signer.capabilities.storage.issue<&FlowToken.Vault>(/storage/flowTokenVault)

_13

signer.capabilities.publish(cap, at: /public/flowTokenReceiver)

_13

signer.capabilities.publish(cap, at: /public/flowTokenBalance)

_13

}

_13

}

_13

}`

Open `cadence/transactions/TransferTokens.cdc` and replace its contents with:

cadence/transactions/TransferTokens.cdc

`_23

import "FungibleToken"

_23

import "FlowToken"

_23

_23

transaction(amount: UFix64, to: Address) {

_23

let sentVault: @{FungibleToken.Vault}

_23

_23

prepare(signer: auth(Storage) &Account) {

_23

let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_23

from: /storage/flowTokenVault

_23

) ?? panic("Could not borrow reference to the owner's Vault")

_23

_23

self.sentVault <- vaultRef.withdraw(amount: amount)

_23

}

_23

_23

execute {

_23

let recipient = getAccount(to)

_23

let receiverRef = recipient.capabilities

_23

.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)

_23

?? panic("Could not borrow receiver reference")

_23

_23

receiverRef.deposit(from: <-self.sentVault)

_23

}

_23

}`

### Test Transaction Execution with Impersonation[​](#test-transaction-execution-with-impersonation "Direct link to Test Transaction Execution with Impersonation")

Add this test function to the existing `cadence/tests/TokenChecker_test.cdc` file:

`_61

access(all) fun testTransactionAsMainnetAccount() {

_61

// Impersonate the Flow service account (or any mainnet account)

_61

// No private keys needed - fork testing has built-in impersonation

_61

let serviceAccount = Test.getAccount(0x1654653399040a61)

_61

_61

// Check initial balance

_61

let initialBalanceScript = Test.executeScript(

_61

Test.readFile("../scripts/CheckBalance.cdc"),

_61

[serviceAccount.address]

_61

)

_61

Test.expect(initialBalanceScript, Test.beSucceeded())

_61

let initialBalance = initialBalanceScript.returnValue! as! UFix64

_61

_61

// Create a test recipient account and set up FlowToken vault

_61

let recipient = Test.createAccount()

_61

_61

// Set up the recipient's FlowToken vault

_61

let setupResult = Test.executeTransaction(

_61

Test.Transaction(

_61

code: Test.readFile("../transactions/SetupFlowTokenVault.cdc"),

_61

authorizers: [recipient.address],

_61

signers: [recipient],

_61

arguments: []

_61

)

_61

)

_61

Test.expect(setupResult, Test.beSucceeded())

_61

_61

// Execute transaction AS the mainnet service account

_61

// This works because fork testing allows impersonating any account

_61

let txResult = Test.executeTransaction(

_61

Test.Transaction(

_61

code: Test.readFile("../transactions/TransferTokens.cdc"),

_61

authorizers: [serviceAccount.address],

_61

signers: [serviceAccount],

_61

arguments: [10.0, recipient.address]

_61

)

_61

)

_61

_61

Test.expect(txResult, Test.beSucceeded())

_61

_61

// Verify the sender's balance decreased

_61

let newBalanceScript = Test.executeScript(

_61

Test.readFile("../scripts/CheckBalance.cdc"),

_61

[serviceAccount.address]

_61

)

_61

Test.expect(newBalanceScript, Test.beSucceeded())

_61

let newBalance = newBalanceScript.returnValue! as! UFix64

_61

_61

// Balance should have decreased by exactly the transfer amount

_61

Test.assertEqual(initialBalance - 10.0, newBalance)

_61

_61

// Verify the recipient received the tokens

_61

let recipientBalanceScript = Test.executeScript(

_61

Test.readFile("../scripts/CheckBalance.cdc"),

_61

[recipient.address]

_61

)

_61

Test.expect(recipientBalanceScript, Test.beSucceeded())

_61

let recipientBalance = recipientBalanceScript.returnValue! as! UFix64

_61

// Recipient should have at least 10.0 (may be slightly more due to storage refunds)

_61

Test.assert(recipientBalance >= 10.0, message: "Recipient should have at least 10 FLOW")

_61

}`

### Key Points About Account Impersonation[​](#key-points-about-account-impersonation "Direct link to Key Points About Account Impersonation")

1. **Any account can be used**: Call `Test.getAccount(address)` with any mainnet address
2. **No private keys needed**: Fork testing has built-in impersonation—you can sign transactions as any account
3. **Real account state**: The account has its actual mainnet balance, storage, and capabilities
4. **Mutations are local**: Changes only affect your test environment, not the real network
5. **Test complex scenarios**: Impersonate whale accounts, protocol accounts, or any user to test edge cases

## Run All Tests Together[​](#run-all-tests-together "Direct link to Run All Tests Together")

Now that you have multiple test files, run them all against the forked network:

`_10

flow test --fork mainnet`

This runs all `*_test.cdc` files in your project against mainnet. You should see:

`_10

Test results: "cadence/tests/FlowToken_test.cdc"

_10

- PASS: testFlowTokenSupplyIsPositive

_10

_10

Test results: "cadence/tests/TokenChecker_test.cdc"

_10

- PASS: testCheckBalanceOnRealAccount

_10

- PASS: testHasMinimumBalance

_10

- PASS: testTransactionAsMainnetAccount`

### Additional Options[​](#additional-options "Direct link to Additional Options")

You can also fork from testnet (`flow test --fork testnet`) or pin to a specific block height (`--fork-height`). See the [Fork Testing Flags](/build/tools/flow-cli/tests#fork-testing-flags) reference for all available options.

See also:

* Strategy: [Testing Strategy on Flow](/build/cadence/smart-contracts/testing-strategy)
* Emulator (fork mode for interactive E2E): [Flow Emulator](/build/tools/emulator)
* Networks and access nodes: [Flow Networks](/protocol/flow-networks)

info

External oracles and off-chain systems

Fork tests run against Flow chain state only:

* No live off-chain/API calls or cross-chain reads
* Price feeds, bridges, indexers, and similar must be mocked (stub contracts or fixtures)
* For end-to-end, combine with `flow emulator --fork` and a local stub service

### Select Tests Quickly[​](#select-tests-quickly "Direct link to Select Tests Quickly")

* Run specific files or directories:

`_10

flow test cadence/tests/FlowToken_test.cdc cadence/tests/TokenChecker_test.cdc --fork mainnet`

* Optional: narrow by function name with `--name`:

`_10

flow test cadence/tests/TokenChecker_test.cdc --name _smoke --fork mainnet`

* Optional: suffix a few functions with `_smoke` for quick PR runs; run the full suite nightly or on protected branches.

## When to Use Fork Testing[​](#when-to-use-fork-testing "Direct link to When to Use Fork Testing")

Fork testing is most valuable for:

* Integration testing with real onchain contracts and data
* Pre-deployment validation before mainnet releases
* Upgrade testing against production state
* Reproducing issues at a specific block height
* Testing interactions with high-value or protocol accounts
* Validating contract behavior with real-world data patterns

For strategy, limitations, and best practices, see the guide: [Testing Smart Contracts](/build/cadence/smart-contracts/testing-strategy).

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to use fork testing to validate your Cadence contracts against live Flow network state. You created tests that read from real mainnet contracts, deployed custom contracts that interact with production data, and executed transactions using account impersonation—all without deploying to a live network or bootstrapping test accounts.

Now that you have completed this tutorial, you should be able to:

* **Run Cadence tests against forked networks** using `flow test --fork`
* **Test contracts that depend on real mainnet contracts** without manual setup
* **Use account impersonation** to execute transactions as any mainnet account
* **Read from production blockchain state** in your test suite
* **Pin tests to specific block heights** for historical debugging
* **Integrate fork testing** into your development workflow

Fork testing bridges the gap between local unit tests and testnet deployments, enabling you to catch integration issues early and test against real-world conditions. Use it as part of your pre-deployment validation process, alongside emulator unit tests for determinism and isolation, and testnet deployments for final verification.

### Next Steps[​](#next-steps "Direct link to Next Steps")

* Explore additional assertions and helpers in the [Cadence Testing Framework](https://cadence-lang.org/docs/testing-framework)
* Add more real-world tests that read from standard contracts like Flow NFT
* Keep unit tests on the emulator for determinism and isolation; run forked integration tests selectively in CI
* Review the [Fork Testing Flags](/build/tools/flow-cli/tests#fork-testing-flags) reference for advanced options
* Learn about [Flow Networks](/protocol/flow-networks) and public access nodes

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/fork-testing/index.md)

Last updated on **Oct 30, 2025** by **Chase Fleming**

[Previous

Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)[Next

Flow EVM Guides](/blockchain-development-tutorials/evm)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)* [What You'll Build](#what-youll-build)
    + [Reproducibility first](#reproducibility-first)* [Prerequisites](#prerequisites)
      + [Flow CLI](#flow-cli)+ [Basic Cadence Testing Knowledge](#basic-cadence-testing-knowledge)+ [Network Access](#network-access)* [Create Your Project](#create-your-project)* [Install Dependencies](#install-dependencies)* [Test Reading Live State](#test-reading-live-state)* [Deploy and Test Your Contract](#deploy-and-test-your-contract)
              + [Create a Test Account](#create-a-test-account)+ [Create a Contract that Uses `FlowToken`](#create-a-contract-that-uses-flowtoken)+ [Configure Contract in flow.json](#configure-contract-in-flowjson)+ [Create Scripts for Testing](#create-scripts-for-testing)+ [Test Your Contract with Forked State](#test-your-contract-with-forked-state)+ [What's Happening Here](#whats-happening-here)* [Execute Transactions with Account Impersonation](#execute-transactions-with-account-impersonation)
                + [Create Transactions](#create-transactions)+ [Test Transaction Execution with Impersonation](#test-transaction-execution-with-impersonation)+ [Key Points About Account Impersonation](#key-points-about-account-impersonation)* [Run All Tests Together](#run-all-tests-together)
                  + [Additional Options](#additional-options)+ [Select Tests Quickly](#select-tests-quickly)* [When to Use Fork Testing](#when-to-use-fork-testing)* [Conclusion](#conclusion)
                      + [Next Steps](#next-steps)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.