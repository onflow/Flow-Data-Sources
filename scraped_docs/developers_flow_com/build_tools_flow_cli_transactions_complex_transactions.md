# Source: https://developers.flow.com/build/tools/flow-cli/transactions/complex-transactions

Build a Complex Transaction | Flow Developer Portal



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

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                    - [Keys](/build/tools/flow-cli/keys/generate-keys)

                      - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                        - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                          - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                            * [Send a Transaction](/build/tools/flow-cli/transactions/send-transactions)* [Get a Transaction](/build/tools/flow-cli/transactions/get-transactions)* [Build a Transaction](/build/tools/flow-cli/transactions/build-transactions)* [Build a Complex Transaction](/build/tools/flow-cli/transactions/complex-transactions)* [Sign a Transaction](/build/tools/flow-cli/transactions/sign-transaction)* [Send Signed Transaction](/build/tools/flow-cli/transactions/send-signed-transactions)* [Build a Complex Transaction](/build/tools/flow-cli/transactions/decode-transactions)* [Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)- [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                              - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Transactions* Build a Complex Transaction

On this page

# Build a Complex Transaction

**Simple Transactions**

Sending a transaction using the Flow CLI can simply be
achieved by using the [send command documented here](/build/tools/flow-cli/transactions/send-transactions).

**Complex Transactions**

If you would like to build more complex transactions the Flow CLI provides
commands to build, sign and send transactions allowing you to specify different
authorizers, signers and proposers.

The process of sending a complex transactions includes three steps:

1. [build a transaction](/build/tools/flow-cli/transactions/build-transactions)
2. [sign the built transaction](/build/tools/flow-cli/transactions/sign-transaction)
3. [send signed transaction](/build/tools/flow-cli/transactions/send-signed-transactions)

Read more about each command flags and arguments in the above links.

## Examples[​](#examples "Direct link to Examples")

We will describe common examples for complex transactions. All examples are using an [example configuration](/build/tools/flow-cli/transactions/complex-transactions#configuration).

### Single payer, proposer and authorizer[​](#single-payer-proposer-and-authorizer "Direct link to Single payer, proposer and authorizer")

The simplest Flow transaction declares a single account as the proposer, payer and authorizer.

Build the transaction:

`_10

> flow transactions build tx.cdc

_10

--proposer alice

_10

--payer alice

_10

--authorizer alice

_10

--filter payload --save tx1`

Sign the transaction:

`_10

> flow transactions sign tx1 --signer alice

_10

--filter payload --save tx2`

Submit the signed transaction:

`_10

> flow transactions send-signed tx2`

Transaction content (`tx.cdc`):

`_10

transaction {

_10

prepare(signer: &Account) {}

_10

execute { ... }

_10

}`

### Single payer and proposer, multiple authorizers[​](#single-payer-and-proposer-multiple-authorizers "Direct link to Single payer and proposer, multiple authorizers")

A transaction that declares same payer and proposer but multiple authorizers each required to sign the transaction. Please note that the order of signing is important, and [the payer must sign last](/build/cadence/basics/transactions#payer-signs-last).

Build the transaction:

`_10

> flow transactions build tx.cdc

_10

--proposer alice

_10

--payer alice

_10

--authorizer bob

_10

--authorizer charlie

_10

--filter payload --save tx1`

Sign the transaction with authorizers:

`_10

> flow transactions sign tx1 --signer bob

_10

--filter payload --save tx2`

`_10

> flow transactions sign tx2 --signer charlie

_10

--filter payload --save tx3`

Sign the transaction with payer:

`_10

> flow transactions sign tx3 --signer alice

_10

--filter payload --save tx4`

Submit the signed transaction:

`_10

> flow transactions send-signed tx4`

Transaction content (`tx.cdc`):

`_10

transaction {

_10

prepare(bob: &Account, charlie: &Account) {}

_10

execute { ... }

_10

}`

### Different payer, proposer and authorizer[​](#different-payer-proposer-and-authorizer "Direct link to Different payer, proposer and authorizer")

A transaction that declares different payer, proposer and authorizer each signing separately.
Please note that the order of signing is important, and [the payer must sign last](/build/cadence/basics/transactions#payer-signs-last).

Build the transaction:

`_10

> flow transactions build tx.cdc

_10

--proposer alice

_10

--payer bob

_10

--authorizer charlie

_10

--filter payload --save tx1`

Sign the transaction with proposer:

`_10

> flow transactions sign tx1 --signer alice

_10

--filter payload --save tx2`

Sign the transaction with authorizer:

`_10

> flow transactions sign tx2 --signer charlie

_10

--filter payload --save tx3`

Sign the transaction with payer:

`_10

> flow transactions sign tx3 --signer bob

_10

--filter payload --save tx4`

Submit the signed transaction:

`_10

> flow transactions send-signed tx4`

Transaction content (`tx.cdc`):

`_10

transaction {

_10

prepare(charlie: &Account) {}

_10

execute { ... }

_10

}`

### Single payer, proposer and authorizer but multiple keys[​](#single-payer-proposer-and-authorizer-but-multiple-keys "Direct link to Single payer, proposer and authorizer but multiple keys")

A transaction that declares same payer, proposer and authorizer but the signer account has two keys with half weight, required to sign with both.

Build the transaction:

`_10

> flow transactions build tx.cdc

_10

--proposer dylan1

_10

--payer dylan1

_10

--authorizer dylan1

_10

--filter payload --save tx1`

Sign the transaction with the first key:

`_10

> flow transactions sign tx1 --signer dylan1

_10

--filter payload --save tx2`

Sign the transaction with the second key:

`_10

> flow transactions sign tx2 --signer dylan2

_10

--filter payload --save tx3`

Submit the signed transaction:

`_10

> flow transactions send-signed tx3`

Transaction content (`tx.cdc`):

`_10

transaction {

_10

prepare(signer: &Account) {}

_10

execute { ... }

_10

}`

### Configuration[​](#configuration "Direct link to Configuration")

This is an example configuration using mock values:

`_26

{

_26

...

_26

"accounts": {

_26

"alice": {

_26

"address": "0x1",

_26

"key": "111...111"

_26

},

_26

"bob": {

_26

"address": "0x2",

_26

"key": "222...222"

_26

},

_26

"charlie": {

_26

"address": "0x3",

_26

"key": "333...333"

_26

},

_26

"dylan1": {

_26

"address": "0x4",

_26

"key": "444...444"

_26

},

_26

"dylan2": {

_26

"address": "0x4",

_26

"key": "555...555"

_26

}

_26

}

_26

...

_26

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/complex-transactions.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Build a Transaction](/build/tools/flow-cli/transactions/build-transactions)[Next

Sign a Transaction](/build/tools/flow-cli/transactions/sign-transaction)

###### Rate this page

😞😐😊

Copy as Markdown

* [Examples](#examples)
  + [Single payer, proposer and authorizer](#single-payer-proposer-and-authorizer)+ [Single payer and proposer, multiple authorizers](#single-payer-and-proposer-multiple-authorizers)+ [Different payer, proposer and authorizer](#different-payer-proposer-and-authorizer)+ [Single payer, proposer and authorizer but multiple keys](#single-payer-proposer-and-authorizer-but-multiple-keys)+ [Configuration](#configuration)

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