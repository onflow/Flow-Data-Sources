# Source: https://developers.flow.com/build/evm/fees

Fees | Flow Developer Portal



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

* `Surge' factor` dynamically accounts for network pressure and market conditions.
* `Inclusion fee` accounts for the resources required to process a transaction due to its core properties (byte size, signatures). This is currently constant at 1E-4 FLOW, but subject to change with community approval.
* `Execution fee` The fee that accounts for the operational cost of running the transaction script, processing the results, sending results for verification, generating verification receipts, etc. and is calculated as a product of `computation units` and the `cost per unit`.
  + `Execution Effort (measured in computation units)` is based on transaction type and operations that are called during the execution of a transaction. The weights determine how costly (time-consuming) each operation is.
  + `Execution Effort Unit Cost` = `4E-05 FLOW` (currently constant, but subject to change with community approval)

### Calculation of Execution Effort

`_44

Execution Effort (computation) =

_44

3.271E+01 * create_account +

_44

2.348E+01 * blsverify_pop +

_44

7.408E+00 * get_account_balance +

_44

6.145E+00 * blsaggregate_public_keys +

_44

6.059E+00 * get_storage_capacity +

_44

5.726E+00 * get_account_available_balance +

_44

5.637E+00 * update_account_contract_code +

_44

4.964E+00 * blsaggregate_signatures +

_44

1.152E+00 * generate_account_local_id +

_44

5.000E-01 * get_account_contract_names +

_44

3.878E-01 * get_storage_used +

_44

3.770E-01 * account_keys_count +

_44

2.346E-01 * allocate_slab_index +

_44

1.348E-01 * atree_map_get +

_44

1.125E-01 * atree_map_remove +

_44

6.659E-02 * create_array_value +

_44

5.826E-02 * create_dictionary_value +

_44

5.579E-02 * atree_map_set +

_44

5.573E-02 * atree_array_insert +

_44

5.074E-02 * atree_map_read_iteration +

_44

4.442E-02 * encode_event +

_44

3.598E-02 * transfer_composite_value +

_44

2.910E-02 * atree_array_append +

_44

2.701E-02 * statement +

_44

2.650E-02 * atree_array_set +

_44

2.135E-02 * function_invocation +

_44

1.846E-02 * atree_map_pop_iteration +

_44

1.123E-02 * atree_array_pop_iteration +

_44

7.874E-03 * rlpdecoding +

_44

4.242E-03 * graphemes_iteration +

_44

3.922E-03 * ufix_parse +

_44

3.403E-03 * fix_parse +

_44

2.731E-03 * loop +

_44

2.701E-03 * atree_array_batch_construction +

_44

1.907E-03 * transfer_dictionary_value +

_44

1.053E-03 * big_int_parse +

_44

7.324E-04 * transfer_array_value +

_44

7.324E-04 * set_value +

_44

4.730E-04 * uint_parse +

_44

4.272E-04 * int_parse +

_44

3.510E-04 * get_value +

_44

7.629E-05 * string_to_lower +

_44

4.578E-05 * evmgas_usage`

where

`` _10

`evmgas_usage` is reported by EVM as the cost in gas for executing the transaction within the EVM, for instance, 21K gas for a simple send transaction. ``



## Demonstration of Transaction Fees on EVM

Assume a simple Token transfer transaction:

**Scenario 1 - Cadence-only Transaction**

The token transfer transaction:

* makes 76 atree\_map\_get calls,
* reads 9431 bytes (get\_value),
* sets 2448 bytes (set\_value),
* invokes 55 cadence statements,
* makes 2 get\_storage\_used calls,
* makes 28 cadence function\_invocation calls,
* makes 8 transfer\_composite\_value calls,
* makes 5 atree\_map\_set calls,
* makes 4 encode\_event calls,
* makes 2 create\_array\_value calls,
* makes 2 atree\_array\_append calls,
* makes 4 atree\_array\_batch\_construction calls,
* makes 2 loop calls,
* makes 2 transfer\_array\_value calls

`_15

Compute Units =

_15

76 * 0.135 +

_15

9431 * 0.000 +

_15

2448 * 0.001 +

_15

55 * 0.027 +

_15

2 * 0.388 +

_15

28 * 0.021 +

_15

8 * 0.036 +

_15

5 * 0.056 +

_15

4 * 0.044 +

_15

2 * 0.067 +

_15

2 * 0.029 +

_15

4 * 0.003 +

_15

2 * 0.003 +

_15

2 * 0.001`

But since `EVMGasUsage` is 0 for a Cadence transaction,

`_10

Compute Units = 19.2`

Thus

`_10

Transaction fee = [1E-4 FLOW + (19.2 * 4E-05 FLOW)] x 1 = 8.68E-04`

**Scenario 2 - EVM Transaction**
If the EVMGasUsage can be assumed to be 21,000 gas (typical for a simple transfer):

* uses 377806 evm gas (evmgas\_usage),
* reads 22840 bytes (get\_value),
* makes 1676 atree\_array\_batch\_construction calls,
* makes 30 atree\_map\_get calls,
* makes 325 atree\_array\_pop\_iteration calls,
* sets 3182 bytes (set\_value),
* makes 273 rlpdecoding calls,
* makes 20 atree\_map\_read\_iteration calls,
* makes 1329 transfer\_array\_value calls,
* invokes 25 cadence statements,
* makes 12 atree\_map\_set calls,
* makes 17 transfer\_composite\_value calls,
* makes 8 create\_array\_value calls,
* makes 19 function\_invocation calls,
* makes 1 get\_storage\_used calls,
* makes 87 graphemes\_iteration calls,
* makes 2 encode\_event calls,
* makes 2 atree\_array\_append calls,
* makes 1 atree\_map\_pop\_iteration calls,
* makes 2 loop calls,
* makes 40 string\_to\_lower calls

`_23

Compute Units =

_23

377806 * 0.00005 +

_23

22840 * 0.00035 +

_23

1676 * 0.00270 +

_23

30 * 0.13484 +

_23

325 * 0.01123 +

_23

3182 * 0.00073 +

_23

273 * 0.00787 +

_23

20 * 0.05074 +

_23

1329 * 0.00073 +

_23

25 * 0.02701 +

_23

12 * 0.05579 +

_23

17 * 0.03598 +

_23

8 * 0.06659 +

_23

19 * 0.02135 +

_23

1 * 0.38782 +

_23

87 * 0.00424 +

_23

2 * 0.04442 +

_23

2 * 0.02910 +

_23

1 * 0.01846 +

_23

2 * 0.00273 +

_23

40 * 0.00008

_23

= 47.8`

Thus

`_10

Transaction fee = [1E-4 FLOW + (47.8 * 4E-05 FLOW)] x 1 = 2.012E-03 FLOW`

**Note**: Please be aware that this example serves solely for illustrative purposes to elucidate the calculations. Actual transaction fees may differ due to various factors, including the byte size of the transaction.

## Gasless Transactions[​](#gasless-transactions "Direct link to Gasless Transactions")

Fees needed to execute transactions on a Web3 app are often a major challenge for new users and can be a barrier to adoption. Builders can easily extend their apps with Cadence to create ‘gasless’ experiences by specifying their app as the [sponsor](/build/cadence/advanced-concepts/account-abstraction#sponsored-transactions) instead of the user.

To learn more about storage fee and transaction fee, visit [Flow Tokenomics page](https://flow.com/flow-tokenomics/technical-overview).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/evm/fees.md)

Last updated on **Dec 5, 2025** by **Vishal**

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

Copyright © 2026 Flow Foundation. All Rights Reserved.