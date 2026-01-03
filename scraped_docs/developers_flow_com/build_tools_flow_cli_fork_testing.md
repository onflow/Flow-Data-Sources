# Source: https://developers.flow.com/build/tools/flow-cli/fork-testing

Fork Testing | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

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

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Fork Testing

On this page

# Fork Testing

Fork testing allows you to run tests and development environments against a **local copy of mainnet or testnet state**. This gives you access to real contracts, accounts, and data without deploying to live networks or affecting production state.

## What is Fork Testing?[​](#what-is-fork-testing "Direct link to What is Fork Testing?")

Fork testing creates a local Flow network that mirrors the state of a real network (mainnet or testnet). Your code runs locally, but can read from and interact with production contract implementations, real account balances, and actual on-chain data.

**Key Benefits:**

* ✅ **Test against real production contracts** - No need to mock complex dependencies
* ✅ **Access real account state** - Test with actual balances, NFTs, and storage
* ✅ **Reproduce production issues** - Debug problems at specific block heights
* ✅ **Test contract upgrades safely** - Verify changes work with real mainnet state
* ✅ **Safe testing environment** - All changes stay local, never affect the real network
* ✅ **Fast iteration** - No deployment costs or wait times

Fork testing is an essential part of a comprehensive testing strategy. It complements unit tests and integration tests by letting you validate your contracts against real-world state and dependencies. Learn more about building a complete testing approach in the [Testing Strategy guide](/build/cadence/smart-contracts/testing-strategy).

## Two Fork Testing Modes[​](#two-fork-testing-modes "Direct link to Two Fork Testing Modes")

The Flow CLI provides two different fork testing modes for different use cases:

### 1. Emulator Fork Mode (`flow emulator --fork`)[​](#1-emulator-fork-mode-flow-emulator---fork "Direct link to 1-emulator-fork-mode-flow-emulator---fork")

**Best for:**

* Frontend and app development
* E2E testing (Cypress, Playwright)
* Manual testing and exploration
* Wallet integration testing
* Bot and indexer development

**How it works:**
Starts a full emulator with REST and gRPC APIs that you can connect to with FCL, dev wallet, or any Flow SDK.

`_10

flow emulator --fork mainnet`

**Learn more:** [Interactive Testing with Forked Emulator](/blockchain-development-tutorials/cadence/emulator-fork-testing)

### 2. Test Framework Fork Mode (`flow test` + `#test_fork`)[​](#2-test-framework-fork-mode-flow-test--test_fork "Direct link to 2-test-framework-fork-mode-flow-test--test_fork")

**Best for:**

* Cadence integration tests
* Contract testing against real dependencies
* Testing contract logic with real mainnet state

**How it works:**
Runs your `*_test.cdc` files against a forked network using the [Cadence Testing Framework](/build/cadence/smart-contracts/testing). Add the `#test_fork` pragma to your test file, then run:

`_10

flow test`

**Learn more:** [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing)

## Quick Comparison[​](#quick-comparison "Direct link to Quick Comparison")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Feature `flow emulator --fork` `flow test` + `#test_fork`|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Use for** App E2E, manual testing, debugging Cadence integration tests|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Connects to** Frontend, wallets, bots, E2E tools Cadence Testing Framework|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Run with** FCL, Cypress, Playwright, manual clicks `flow test` command| **Best for** User flows, UI testing, exploration Contract logic validation|  |  |  | | --- | --- | --- | | **Examples** React app, wallet flows, E2E suites `*_test.cdc` files | | | | | | | | | | | | | | | | | |

## Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

### DeFi Protocol Testing[​](#defi-protocol-testing "Direct link to DeFi Protocol Testing")

Test your DeFi contracts against real mainnet state - real DEX liquidity, real oracle prices, real token supplies.

### Contract Upgrade Testing[​](#contract-upgrade-testing "Direct link to Contract Upgrade Testing")

Deploy your upgraded contract to a fork and verify it works with real mainnet state before deploying to production.

### Bug Reproduction[​](#bug-reproduction "Direct link to Bug Reproduction")

Fork to the exact block height where a bug occurred and debug with the actual state that caused the issue.

### Integration Testing[​](#integration-testing "Direct link to Integration Testing")

Test how your contracts interact with production versions of core contracts (FungibleToken, NFT standards, etc).

## Getting Started[​](#getting-started "Direct link to Getting Started")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Flow CLI](/build/tools/flow-cli/install) v2.12.0 or later
* Basic understanding of Flow development

### Quick Start: Emulator Fork[​](#quick-start-emulator-fork "Direct link to Quick Start: Emulator Fork")

`_11

# 1. Initialize a Flow project

_11

flow init

_11

_11

# 2. Install dependencies (e.g., FlowToken)

_11

flow dependencies install FlowToken FungibleToken

_11

_11

# 3. Start the forked emulator

_11

flow emulator --fork mainnet

_11

_11

# 4. In another terminal, run scripts/transactions

_11

flow scripts execute myScript.cdc --network mainnet-fork`

**Next steps:** Follow the [complete emulator fork tutorial](/blockchain-development-tutorials/cadence/emulator-fork-testing)

### Quick Start: Cadence Test Fork[​](#quick-start-cadence-test-fork "Direct link to Quick Start: Cadence Test Fork")

Add the fork pragma to your test file:

`_10

#test_fork(network: "mainnet", height: nil)

_10

_10

import Test

_10

_10

access(all) fun testExample() {

_10

// Your test code here

_10

}`

Then run the test:

`_10

flow test tests/MyContract_test.cdc`

**Next steps:** Follow the [complete Cadence fork testing tutorial](/blockchain-development-tutorials/cadence/fork-testing)

## Key Features[​](#key-features "Direct link to Key Features")

### Pin to Block Heights[​](#pin-to-block-heights "Direct link to Pin to Block Heights")

Fork to specific block heights for reproducible testing:

`_10

# Emulator fork with block height

_10

flow emulator --fork mainnet --fork-height <BLOCK_HEIGHT>`

`_10

// Test with block height - add to your test file

_10

#test_fork(network: "mainnet", height: <BLOCK_HEIGHT>)`

`_10

# Then run the test

_10

flow test test_file.cdc`

Replace `<BLOCK_HEIGHT>` with the specific block number you want to test against. Note that block heights are only available within the current spork.

### Account Impersonation[​](#account-impersonation "Direct link to Account Impersonation")

Fork mode disables signature verification, allowing you to execute transactions as any mainnet account for testing.

### Dependency Mocking[​](#dependency-mocking "Direct link to Dependency Mocking")

Override specific mainnet contracts with your own versions while keeping all other contracts unchanged - perfect for testing contract upgrades.

### Automatic Configuration[​](#automatic-configuration "Direct link to Automatic Configuration")

Fork networks are automatically configured when you run fork commands. Contract aliases from the parent network (mainnet/testnet) are automatically inherited.

Learn more: [flow.json Configuration - Fork Networks](/build/tools/flow-cli/flow.json/configuration#networks)

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Pin block heights in CI/CD** - Ensures reproducible test results
2. **Test on testnet first** - Avoid mainnet rate limits during development
3. **Use the right mode** - Emulator fork for apps, test fork for Cadence contracts
4. **Mock external services** - Fork only mirrors Flow state, not external APIs
5. **Document your fork heights** - Keep track of which blocks work for testing

## Network Requirements[​](#network-requirements "Direct link to Network Requirements")

Fork testing requires network access to Flow's public access nodes:

* **Mainnet:** `access.mainnet.nodes.onflow.org:9000`
* **Testnet:** `access.devnet.nodes.onflow.org:9000`

Data is fetched on-demand and cached locally for performance.

## Limitations[​](#limitations "Direct link to Limitations")

* **Spork boundaries:** Historical data is only available within the current spork
* **Off-chain services:** Oracles, IPFS, and cross-chain bridges must be mocked
* **Network latency:** First access to accounts/contracts requires network fetch

Learn more: [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade)

## Tutorials[​](#tutorials "Direct link to Tutorials")

* [Interactive Testing with Forked Emulator](/blockchain-development-tutorials/cadence/emulator-fork-testing) - Complete guide to `flow emulator --fork`
* [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing) - Complete guide to `flow test` with `#test_fork`

## Related Documentation[​](#related-documentation "Direct link to Related Documentation")

* [Flow Emulator](/build/tools/emulator) - Learn more about the Flow emulator
* [Cadence Testing Framework](/build/cadence/smart-contracts/testing) - Write and run Cadence tests
* [flow.json Configuration](/build/tools/flow-cli/flow.json/configuration) - Configure fork networks
* [Testing Strategy](/build/cadence/smart-contracts/testing-strategy) - Overall testing approach
* [Dependency Manager](/build/tools/flow-cli/dependency-manager) - Install and manage contract dependencies

## Need Help?[​](#need-help "Direct link to Need Help?")

* Review the [complete tutorials](/blockchain-development-tutorials/cadence/emulator-fork-testing) for step-by-step guidance
* Check the [troubleshooting sections](/blockchain-development-tutorials/cadence/emulator-fork-testing#troubleshooting) in the tutorials
* Ask questions in the [Flow Discord](https://discord.gg/flow)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/fork-testing.md)

Last updated on **Dec 16, 2025** by **Jordan Ribbink**

[Previous

Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)[Next

Data Collection](/build/tools/flow-cli/data-collection)

###### Rate this page

😞😐😊

Copy as Markdown

* [What is Fork Testing?](#what-is-fork-testing)* [Two Fork Testing Modes](#two-fork-testing-modes)
    + [1. Emulator Fork Mode (`flow emulator --fork`)](#1-emulator-fork-mode-flow-emulator---fork)+ [2. Test Framework Fork Mode (`flow test` + `#test_fork`)](#2-test-framework-fork-mode-flow-test--test_fork)* [Quick Comparison](#quick-comparison)* [Common Use Cases](#common-use-cases)
        + [DeFi Protocol Testing](#defi-protocol-testing)+ [Contract Upgrade Testing](#contract-upgrade-testing)+ [Bug Reproduction](#bug-reproduction)+ [Integration Testing](#integration-testing)* [Getting Started](#getting-started)
          + [Prerequisites](#prerequisites)+ [Quick Start: Emulator Fork](#quick-start-emulator-fork)+ [Quick Start: Cadence Test Fork](#quick-start-cadence-test-fork)* [Key Features](#key-features)
            + [Pin to Block Heights](#pin-to-block-heights)+ [Account Impersonation](#account-impersonation)+ [Dependency Mocking](#dependency-mocking)+ [Automatic Configuration](#automatic-configuration)* [Best Practices](#best-practices)* [Network Requirements](#network-requirements)* [Limitations](#limitations)* [Tutorials](#tutorials)* [Related Documentation](#related-documentation)* [Need Help?](#need-help)

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