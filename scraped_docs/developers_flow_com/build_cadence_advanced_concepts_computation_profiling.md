# Source: https://developers.flow.com/build/cadence/advanced-concepts/computation-profiling

Cadence Computation Profiling | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              - [Cadence Computation Profiling](/build/cadence/advanced-concepts/computation-profiling)- [Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)- [Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions)- [Passkeys](/build/cadence/advanced-concepts/passkeys)- [FLIX (Flow Interaction Templates)](/build/cadence/advanced-concepts/flix)- [NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)- [VRF (Randomness) in Cadence](/build/cadence/advanced-concepts/randomness)- [Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)+ [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Advanced Concepts* Cadence Computation Profiling

On this page

# Cadence Computation Profiling

This guide provides comprehensive instructions for using the computation profiling and reporting features in the Flow Emulator. These tools help Cadence developers analyze and optimize their smart contracts by understanding computational costs and identifying performance bottlenecks.

## Overview[​](#overview "Direct link to Overview")

When developing smart contracts on Flow, understanding computational costs is essential for:

* **Performance Optimization**: Identify slow operations and optimize your code
* **Cost Awareness**: Understand how much computation your transactions and scripts consume
* **Bottleneck Identification**: Pinpoint exactly where your code spends the most resources

The Flow Emulator provides two complementary tools for this purpose:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Feature Output Best For|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | **Computation Reporting** JSON report with detailed intensities Quick numerical analysis, CI/CD integration, automated testing|  |  |  | | --- | --- | --- | | **Computation Profiling** pprof profile Visual analysis (e.g. flame graphs), deep-dive debugging, call stack exploration | | | | | | | | |

note

Before getting started, make sure you have the [Flow CLI installed](/build/tools/flow-cli/install).

## Computation Reporting[​](#computation-reporting "Direct link to Computation Reporting")

Computation reporting provides a JSON-based view of computational costs for all executed transactions and scripts.

### Enabling Computation Reporting[​](#enabling-computation-reporting "Direct link to Enabling Computation Reporting")

Start the emulator with the `--computation-reporting` flag:

`_10

flow emulator --computation-reporting`

info

For more accurate computation numbers that reflect real network conditions, consider using [emulator fork testing](/blockchain-development-tutorials/cadence/emulator-fork-testing). Forking allows you to profile against actual Mainnet or Testnet state without requiring a full emulator environment setup.

### Viewing Computation Reports[​](#viewing-computation-reports "Direct link to Viewing Computation Reports")

Once enabled, access the computation report at:

`_10

http://localhost:8080/emulator/computationReport`

The report returns a JSON object with the following structure:

`_30

{

_30

"scripts": {

_30

"<script-id>": {

_30

"path": "scripts/myScript.cdc",

_30

"computation": 1250,

_30

"intensities": {

_30

"Statement": 45,

_30

"FunctionInvocation": 12,

_30

"GetValue": 8

_30

},

_30

"memory": 2048,

_30

"source": "access(all) fun main(): Int { ... }",

_30

"arguments": ["0x1"]

_30

}

_30

},

_30

"transactions": {

_30

"<transaction-id>": {

_30

"path": "transactions/myTransaction.cdc",

_30

"computation": 3500,

_30

"intensities": {

_30

"Statement": 120,

_30

"EmitEvent": 5,

_30

"SetValue": 15

_30

},

_30

"memory": 8192,

_30

"source": "transaction { ... }",

_30

"arguments": ["100.0"]

_30

}

_30

}

_30

}`

#### Report Fields[​](#report-fields "Direct link to Report Fields")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Field Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `path` Source file path (set via `#sourceFile` pragma)| `computation` Total computation units used|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `intensities` Count of each operation type performed|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `memory` Estimated memory usage|  |  |  |  | | --- | --- | --- | --- | | `source` Original Cadence source code|  |  | | --- | --- | | `arguments` Arguments passed to the transaction/script | | | | | | | | | | | | | |

### Understanding Computation Intensities[​](#understanding-computation-intensities "Direct link to Understanding Computation Intensities")

The `intensities` map shows how many times each operation type was performed. The keys are human-readable names like `Statement`, `Loop`, `FunctionInvocation`, `GetValue`, `SetValue`, `EmitEvent`, etc.

The total `computation` value is calculated by multiplying each intensity by its corresponding weight (defined by the network) and summing the results. When optimizing, look for operations with high counts - reducing these will lower your total computation cost.

## Computation Profiling (pprof)[​](#computation-profiling-pprof "Direct link to Computation Profiling (pprof)")

Computation profiling generates pprof-compatible profiles that can be visualized as flame graphs, providing a powerful way to understand your code's execution patterns.

### Installing pprof[​](#installing-pprof "Direct link to Installing pprof")

To visualize computation profiles, you'll need the [pprof tool](https://github.com/google/pprof). See the [pprof installation guide](https://github.com/google/pprof#building-pprof) for instructions.

### Enabling Computation Profiling[​](#enabling-computation-profiling "Direct link to Enabling Computation Profiling")

Start the emulator with the `--computation-profiling` flag:

`_10

flow emulator --computation-profiling`

> **Note**: You can enable both `--computation-reporting` and `--computation-profiling` simultaneously if you need both types of analysis.

### Downloading the Profile[​](#downloading-the-profile "Direct link to Downloading the Profile")

After executing transactions and scripts, download the profile from:

`_10

http://localhost:8080/emulator/computationProfile`

This downloads a `profile.pprof` file containing the aggregated computation profile.

Using curl:

`_10

curl -o profile.pprof http://localhost:8080/emulator/computationProfile`

### Viewing Profiles with pprof[​](#viewing-profiles-with-pprof "Direct link to Viewing Profiles with pprof")

Open the profile in an interactive web interface:

`_10

pprof -http=:8081 profile.pprof`

Then navigate to `http://localhost:8081` in your browser.

#### Available Views[​](#available-views "Direct link to Available Views")

The pprof web interface provides several visualization options:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| View Description|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Flame Graph** Visual representation of call stacks with computation costs|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | **Graph** Directed graph showing call relationships|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | **Top** List of functions sorted by computation usage|  |  |  |  | | --- | --- | --- | --- | | **Source** Source code annotated with computation costs|  |  | | --- | --- | | **Peek** Callers and callees of selected functions | | | | | | | | | | | |

### Viewing Source Code in pprof[​](#viewing-source-code-in-pprof "Direct link to Viewing Source Code in pprof")

To see Cadence source code annotated with computation costs:

1. **Download all deployed contracts**:

   `_10

   curl -o contracts.zip http://localhost:8080/emulator/allContracts`
2. **Extract the ZIP file into a `contracts` folder**:

   `_10

   mkdir -p contracts

   _10

   unzip contracts.zip -d contracts`
3. **Run pprof with the source path**:

   `_10

   pprof -source_path=contracts -http=:8081 profile.pprof`

Now when you view the "Source" tab in pprof, you'll see your Cadence code with line-by-line computation annotations.

### Resetting Computation Profiles[​](#resetting-computation-profiles "Direct link to Resetting Computation Profiles")

To clear the accumulated profile data (useful between test runs):

`_10

curl -X PUT http://localhost:8080/emulator/computationProfile/reset`

## Using Source File Pragmas[​](#using-source-file-pragmas "Direct link to Using Source File Pragmas")

The `#sourceFile` pragma improves computation report readability by associating your code with meaningful file paths. Without it, reports show generic identifiers.

> **Note**: The `#sourceFile` pragma currently only affects **Computation Reporting** (JSON reports). It does not change filenames in **Computation Profiling** (pprof profiles).

### Usage[​](#usage "Direct link to Usage")

Add the pragma at the beginning of your transaction or script:

`_10

#sourceFile("transactions/transfer_tokens.cdc")

_10

_10

transaction(amount: UFix64, recipient: Address) {

_10

prepare(signer: auth(Storage) &Account) {

_10

// Transfer logic

_10

}

_10

}`

For scripts:

`_10

#sourceFile("scripts/get_balance.cdc")

_10

_10

access(all) fun main(address: Address): UFix64 {

_10

return getAccount(address).balance

_10

}`

### Benefits[​](#benefits "Direct link to Benefits")

* Computation reports show file paths instead of generic IDs
* Easier to correlate computation costs with source files
* Useful for tracking costs across multiple files in a project

## Practical Examples[​](#practical-examples "Direct link to Practical Examples")

### Profiling a Simple Transaction[​](#profiling-a-simple-transaction "Direct link to Profiling a Simple Transaction")

Let's profile a simple NFT minting transaction.

**1. Start the emulator with profiling enabled:**

`_10

flow emulator --computation-profiling --computation-reporting`

**2. Create a transaction file (`transactions/mint_nft.cdc`):**

`_14

#sourceFile("transactions/mint_nft.cdc")

_14

_14

import NonFungibleToken from 0xf8d6e0586b0a20c7

_14

import ExampleNFT from 0xf8d6e0586b0a20c7

_14

_14

transaction {

_14

prepare(signer: auth(Storage) &Account) {

_14

let collection = signer.storage.borrow<&ExampleNFT.Collection>(

_14

from: ExampleNFT.CollectionStoragePath

_14

) ?? panic("Could not borrow collection")

_14

_14

collection.deposit(token: <- ExampleNFT.mintNFT())

_14

}

_14

}`

**3. Execute the transaction:**

`_10

flow transactions send transactions/mint_nft.cdc`

**4. View the computation report:**

`_10

curl http://localhost:8080/emulator/computationReport | jq`

**5. Analyze with pprof:**

`_10

curl -o profile.pprof http://localhost:8080/emulator/computationProfile

_10

pprof -http=:8081 profile.pprof`

### Identifying Performance Bottlenecks[​](#identifying-performance-bottlenecks "Direct link to Identifying Performance Bottlenecks")

Consider a script that iterates over a large collection:

`_21

#sourceFile("scripts/find_expensive.cdc")

_21

_21

access(all) fun main(address: Address): [UInt64] {

_21

let account = getAccount(address)

_21

let collection = account.capabilities.borrow<&{NonFungibleToken.Collection}>(

_21

/public/NFTCollection

_21

) ?? panic("Could not borrow collection")

_21

_21

let ids = collection.getIDs()

_21

var result: [UInt64] = []

_21

_21

// Potentially expensive loop

_21

for id in ids {

_21

let nft = collection.borrowNFT(id)

_21

if nft != nil {

_21

result.append(id)

_21

}

_21

}

_21

_21

return result

_21

}`

After profiling, you might see high values for:

* `Loop`: Many iterations
* `FunctionInvocation`: Repeated `borrowNFT` calls
* `GetValue`: Multiple storage reads

**Optimization strategies:**

* Use pagination to limit iterations per call
* Cache results when possible
* Consider restructuring data for more efficient access

### Comparing Computation Costs[​](#comparing-computation-costs "Direct link to Comparing Computation Costs")

You can compare two implementation approaches by downloading and comparing profiles:

**1. Reset the profile:**

`_10

curl -X PUT http://localhost:8080/emulator/computationProfile/reset`

**2. Run implementation A and save the profile:**

`_10

flow transactions send approach_a.cdc

_10

curl -o profile_a.pprof http://localhost:8080/emulator/computationProfile`

**3. Reset and test implementation B:**

`_10

curl -X PUT http://localhost:8080/emulator/computationProfile/reset

_10

flow transactions send approach_b.cdc

_10

curl -o profile_b.pprof http://localhost:8080/emulator/computationProfile`

**4. Compare using pprof:**

`_10

# View profile A

_10

pprof -top profile_a.pprof

_10

_10

# View profile B

_10

pprof -top profile_b.pprof`

The `-top` view shows total computation, making it easy to compare the two approaches.

## API Reference[​](#api-reference "Direct link to API Reference")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Endpoint Method Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `/emulator/computationReport` GET View computation report (JSON)|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `/emulator/computationProfile` GET Download pprof profile|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `/emulator/computationProfile/reset` PUT Reset computation profile|  |  |  | | --- | --- | --- | | `/emulator/allContracts` GET Download all deployed contracts (ZIP) | | | | | | | | | | | | | | |

### Example API Calls[​](#example-api-calls "Direct link to Example API Calls")

`_11

# Get computation report

_11

curl http://localhost:8080/emulator/computationReport

_11

_11

# Download pprof profile

_11

curl -o profile.pprof http://localhost:8080/emulator/computationProfile

_11

_11

# Reset computation profile

_11

curl -X PUT http://localhost:8080/emulator/computationProfile/reset

_11

_11

# Download all contracts

_11

curl -o contracts.zip http://localhost:8080/emulator/allContracts`

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Profile endpoint returns 404[​](#profile-endpoint-returns-404 "Direct link to Profile endpoint returns 404")

**Problem**: Accessing `/emulator/computationProfile` returns a 404 error.

**Solution**: Make sure you started the emulator with `--computation-profiling`:

`_10

flow emulator --computation-profiling`

### Empty profile[​](#empty-profile "Direct link to Empty profile")

**Problem**: The downloaded profile is empty or has no useful data.

**Solution**: Make sure you've executed at least one transaction or script after starting the emulator. The profile only contains data for executed code.

### Source code not showing in pprof[​](#source-code-not-showing-in-pprof "Direct link to Source code not showing in pprof")

**Problem**: The pprof source view doesn't display your Cadence code.

**Solution**:

1. Download the contracts ZIP: `curl -o contracts.zip http://localhost:8080/emulator/allContracts`
2. Extract to a `contracts` folder in your working directory
3. Run pprof with the source path: `pprof -source_path=contracts -http=:8081 profile.pprof`

### High memory usage[​](#high-memory-usage "Direct link to High memory usage")

**Problem**: The emulator uses increasing memory over time.

**Solution**: Periodically reset computation profiles to free accumulated data:

`_10

curl -X PUT http://localhost:8080/emulator/computationProfile/reset`

### Computation reports not showing file paths[​](#computation-reports-not-showing-file-paths "Direct link to Computation reports not showing file paths")

**Problem**: The `path` field in computation reports is empty.

**Solution**: Add the `#sourceFile` pragma to your transactions and scripts:

`_10

#sourceFile("path/to/your/file.cdc")`

## Related Features[​](#related-features "Direct link to Related Features")

### Code Coverage Reporting[​](#code-coverage-reporting "Direct link to Code Coverage Reporting")

The emulator also supports Cadence code coverage reporting, which complements computation profiling:

`_10

flow emulator --coverage-reporting`

View coverage at: `http://localhost:8080/emulator/codeCoverage`

Learn more in the [Flow Emulator documentation](/build/tools/emulator).

### Debugger[​](#debugger "Direct link to Debugger")

For step-through debugging of Cadence code, use the `#debug()` pragma:

`_10

#debug()

_10

_10

transaction {

_10

prepare(signer: &Account) {

_10

// Execution pauses here for debugging

_10

}

_10

}`

This works with VSCode and Flow CLI debugging tools.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/advanced-concepts/computation-profiling.md)

Last updated on **Jan 8, 2026** by **Chase Fleming**

[Previous

Development Standards](/build/cadence/smart-contracts/best-practices/project-development-tips)[Next

Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Computation Reporting](#computation-reporting)
    + [Enabling Computation Reporting](#enabling-computation-reporting)+ [Viewing Computation Reports](#viewing-computation-reports)+ [Understanding Computation Intensities](#understanding-computation-intensities)* [Computation Profiling (pprof)](#computation-profiling-pprof)
      + [Installing pprof](#installing-pprof)+ [Enabling Computation Profiling](#enabling-computation-profiling)+ [Downloading the Profile](#downloading-the-profile)+ [Viewing Profiles with pprof](#viewing-profiles-with-pprof)+ [Viewing Source Code in pprof](#viewing-source-code-in-pprof)+ [Resetting Computation Profiles](#resetting-computation-profiles)* [Using Source File Pragmas](#using-source-file-pragmas)
        + [Usage](#usage)+ [Benefits](#benefits)* [Practical Examples](#practical-examples)
          + [Profiling a Simple Transaction](#profiling-a-simple-transaction)+ [Identifying Performance Bottlenecks](#identifying-performance-bottlenecks)+ [Comparing Computation Costs](#comparing-computation-costs)* [API Reference](#api-reference)
            + [Example API Calls](#example-api-calls)* [Troubleshooting](#troubleshooting)
              + [Profile endpoint returns 404](#profile-endpoint-returns-404)+ [Empty profile](#empty-profile)+ [Source code not showing in pprof](#source-code-not-showing-in-pprof)+ [High memory usage](#high-memory-usage)+ [Computation reports not showing file paths](#computation-reports-not-showing-file-paths)* [Related Features](#related-features)
                + [Code Coverage Reporting](#code-coverage-reporting)+ [Debugger](#debugger)

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