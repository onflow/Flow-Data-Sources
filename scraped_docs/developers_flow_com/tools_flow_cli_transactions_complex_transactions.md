# Source: https://developers.flow.com/tools/flow-cli/transactions/complex-transactions

Build a Complex Transaction | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

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

    - [Send a Transaction](/tools/flow-cli/transactions/send-transactions)
    - [Get a Transaction](/tools/flow-cli/transactions/get-transactions)
    - [Build a Transaction](/tools/flow-cli/transactions/build-transactions)
    - [Build a Complex Transaction](/tools/flow-cli/transactions/complex-transactions)
    - [Sign a Transaction](/tools/flow-cli/transactions/sign-transaction)
    - [Send Signed Transaction](/tools/flow-cli/transactions/send-signed-transactions)
    - [Build a Complex Transaction](/tools/flow-cli/transactions/decode-transactions)
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
* Transactions
* Build a Complex Transaction

On this page

# Build a Complex Transaction

**Simple Transactions**

Sending a transaction using the Flow CLI can simply be
achieved by using the [send command documented here](/tools/flow-cli/transactions/send-transactions).

**Complex Transactions**

If you would like to build more complex transactions the Flow CLI provides
commands to build, sign and send transactions allowing you to specify different
authorizers, signers and proposers.

The process of sending a complex transactions includes three steps:

1. [build a transaction](/tools/flow-cli/transactions/build-transactions)
2. [sign the built transaction](/tools/flow-cli/transactions/sign-transaction)
3. [send signed transaction](/tools/flow-cli/transactions/send-signed-transactions)

Read more about each command flags and arguments in the above links.

## Examples[​](#examples "Direct link to Examples")

We will describe common examples for complex transactions. All examples are using an [example configuration](/tools/flow-cli/transactions/complex-transactions#configuration).

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

A transaction that declares same payer and proposer but multiple authorizers each required to sign the transaction. Please note that the order of signing is important, and [the payer must sign last](/build/basics/transactions#payer-signs-last).

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
Please note that the order of signing is important, and [the payer must sign last](/build/basics/transactions#payer-signs-last).

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/transactions/complex-transactions.md)

Last updated on **Feb 22, 2025** by **bz**

[Previous

Build a Transaction](/tools/flow-cli/transactions/build-transactions)[Next

Sign a Transaction](/tools/flow-cli/transactions/sign-transaction)

###### Rate this page

😞😐😊

* [Examples](#examples)
  + [Single payer, proposer and authorizer](#single-payer-proposer-and-authorizer)
  + [Single payer and proposer, multiple authorizers](#single-payer-and-proposer-multiple-authorizers)
  + [Different payer, proposer and authorizer](#different-payer-proposer-and-authorizer)
  + [Single payer, proposer and authorizer but multiple keys](#single-payer-proposer-and-authorizer-but-multiple-keys)
  + [Configuration](#configuration)

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