# Source: https://developers.flow.com/evm/fees

Fees | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Solidity (EVM)* Fees

On this page

# Fees

info

Are you a Cadence developer looking for information about Fees on Cadence? If so, check out the Cadence specific documentation [here](/build/cadence/basics/fees)

EVM transactions are ultra low-cost and use the native FLOW token as gas. [Externally Owned Accounts (EOAs)](/build/evm/accounts) function the same on Flow as other EVM networks like Ethereum.

## How Transaction Fees are Computed on EVM

With Flow EVM, EVM operations can now be called within Cadence transactions. EVM operations also have an associated effort measured in gas which needs to be factored into the execution effort calculation in addition to the Flow computation for any EVM transaction.

`_10

Transaction fee on EVM = surge x [inclusion fee + (execution effort * unit cost)]`

* `Surge' factor` dynamically accounts for network pressure and market conditions. This is currently constant at 1.0 but subject to change with community approval.
* `Inclusion fee` accounts for the resources required to process a transaction due to its core properties (byte size, signatures). This is currently constant at 1E-6 FLOW, but subject to change with community approval.
* `Execution fee` The fee that accounts for the operational cost of running the transaction script, processing the results, sending results for verification, generating verification receipts, etc. and is calculated as a product of `execution effort units` and the `cost per unit`.
  + `Execution Effort (computation)` is based on transaction type and operations that are called during the execution of a transaction. The weights determine how “costly” (time consuming) each operation is.
  + `Execution Effort Unit Cost` = `2.49E-07 FLOW` (currently constant, but subject to change with community approval)

### Calculation of Execution Effort

`_10

Execution Effort (computation) =

_10

0.00478 * function_or_loop_call +

_10

0.00246 * GetValue +

_10

0.00234 * SetValue +

_10

8.65988 * CreateAccount +

_10

EVMGasUsageCost * EVMGasUsage`

where

`` _10

`EVMGasUsage` is reported by EVM as the cost in gas for executing the transaction within the EVM, for instance, 21K gas for a simple send transaction. ``

`` _10

`EVMGasUsageCost` - The ratio that converts EVM gas into Flow computation units (execution effort) is currently set at `1/5000` but subject to revision by community approval ``

**Note**: The weights and unit cost mentioned above have been updated recently to accommodate an increased computation limit on Flow, which now supports the deployment of larger EVM contracts. For detailed information, refer to the relevant [FLIP](https://github.com/onflow/flips/blob/main/governance/20240508-computation-limit-hike.md) and join the ongoing discussion on the community [forum post](https://forum.flow.com/t/proposing-transaction-fee-changes-and-flow-evm-gas-charges-for-flow-crescendo-launch/5817). These values may be adjusted in the future based on community feedback and evolving requirements.



## Demonstration of Transaction Fees on EVM

Assume a simple NFT transfer transaction that makes 31 cadence loop calls, reads 5668 bytes from the storage register, and saves 1668 bytes to the storage register.

* 'function\_or\_loop\_call' = 31
* 'GetValue' = 5688
* 'SetValue' = 1668
* 'CreateAccount' = 0

**Scenario 1 - Cadence-only Transaction**

`_10

Execution Effort = 0.00478 * (31) + 0.00246 * (5668) + 0.00234 *(1668) + 8.65988 *(0) + EVMGasUsageCost * EVMGasUsage`

But since `EVMGasUsage` is 0 for a Cadence transaction,

`_10

Execution Effort = 18.04378`

Thus

`_10

Transaction fee = [1E-6 FLOW + (18.04378 * 2.49E-07 FLOW)] x 1 = 5.5E-06 FLOW`

**Scenario 2 - EVM Transaction**
If the EVMGasUsage can be assumed to be 21,000 gas (typical for a simple transfer),

`_10

Execution Effort = 0.00478 * (31) + 0.00246 * (5668) + 0.00234 *(1668) + 8.65988 *(0) + 1/5000 * 21000 = 22.24378`

Thus

`_10

Transaction fee = [1E-6 FLOW + (110.97 * 2.49E-07 FLOW)] x 1 = 6.55E-06 FLOW`

**Note**: Please be aware that this example serves solely for illustrative purposes to elucidate the calculations. Actual transaction fees may differ due to various factors, including the byte size of the transaction.

## Gasless Transactions[​](#gasless-transactions "Direct link to Gasless Transactions")

Fees needed to execute transactions on a Web3 app are often a major challenge for new users and can be a barrier to adoption. Builders can easily extend their apps with Cadence to create ‘gasless’ experiences by specifying their app as the [sponsor](/build/cadence/advanced-concepts/account-abstraction#sponsored-transactions) instead of the user.

To learn more about storage fee and transaction fee, visit [Flow Tokenomics page](https://flow.com/flow-tokenomics/technical-overview).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/evm/fees.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Network Information](/build/evm/networks)[Next

Accounts](/build/evm/accounts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Gasless Transactions](#gasless-transactions)

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