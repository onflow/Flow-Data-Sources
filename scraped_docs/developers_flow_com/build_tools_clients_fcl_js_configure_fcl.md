# Source: https://developers.flow.com/build/tools/clients/fcl-js/configure-fcl

How to Configure FCL | Flow Developer Portal



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

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                          * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                                * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* How to Configure FCL

On this page

# How to Configure FCL

## Configuration[​](#configuration "Direct link to Configuration")

Flow Client Library (FCL) provides a mechanism to configure various aspects of its behavior. The key principle is that when you switch between different Flow Blockchain environments (for example, Local Emulator → Testnet → Mainnet), the only required change should be your FCL configuration.

## Set configuration values[​](#set-configuration-values "Direct link to Set configuration values")

Values only need to be set once. We recommend that you do this once and as early in the life cycle as possible.

To set a configuration value, the `put` method on the `config` instance needs to be called, the `put` method returns the `config` instance so they can be chained.

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl

_10

.config() // returns the config instance

_10

.put('foo', 'bar') // configures "foo" to be "bar"

_10

.put('baz', 'buz'); // configures "baz" to be "buz"`

info

For advanced use cases that require scoped configuration, isolated client instances, or multi-tenancy support, see the [`createFlowClient` reference documentation](/build/tools/clients/fcl-js/packages-docs/fcl/createFlowClient).

## Get configuration values[​](#get-configuration-values "Direct link to Get configuration values")

The `config` instance has an asynchronous `get` method. You can also pass it a fallback value in case the configuration state does not include what you want.

`_15

import * as fcl from '@onflow/fcl';

_15

_15

fcl.config().put('foo', 'bar').put('woot', 5).put('rawr', 7);

_15

_15

const FALLBACK = 1;

_15

_15

async function addStuff() {

_15

var woot = await fcl.config().get('woot', FALLBACK); // will be 5 -- set in the config before

_15

var rawr = await fcl.config().get('rawr', FALLBACK); // will be 7 -- set in the config before

_15

var hmmm = await fcl.config().get('hmmm', FALLBACK); // will be 1 -- uses fallback because this isnt in the config

_15

_15

return woot + rawr + hmmm;

_15

}

_15

_15

addStuff().then((d) => console.log(d)); // 13 (5 + 7 + 1)`

## Common configuration keys[​](#common-configuration-keys "Direct link to Common configuration keys")

* `accessNode.api` -- API URL for the Flow Blockchain Access Node you want to communicate with.
* `app.detail.title` - **(INTRODUCED `@onflow/fcl@0.0.68`)** Your applications title, can be requested by wallets and other services. Used by WalletConnect plugin and Wallet Discovery service.
* `app.detail.icon` - **(INTRODUCED `@onflow/fcl@0.0.68`)** URL for your applications icon, can be requested by wallets and other services. Used by WalletConnect plugin and Wallet Discovery service.
* `app.detail.description` - **(INTRODUCED `@onflow/fcl@1.11.0`)** Your applications description, can be requested by wallets and other services. Used by WalletConnect plugin and Wallet Discovery service.
* `app.detail.url` - **(INTRODUCED `@onflow/fcl@1.11.0`)** Your applications URL, can be requested by wallets and other services. Used by WalletConnect plugin and Wallet Discovery service.
* `challenge.handshake` -- **(DEPRECATED `@onflow/fcl@0.0.68`)** Points FCL at the Wallet or Wallet Discovery mechanism.
* `discovery.wallet` -- **(INTRODUCED `@onflow/fcl@0.0.68`)** Points FCL at the Wallet or Wallet Discovery mechanism.
* `discovery.wallet.method` -- Describes which service strategy a wallet should use: `IFRAME/RPC`, `POP/RPC`, `TAB/RPC`, `HTTP/POST`, `EXT/RPC`
* `env` -- **(DEPRECATED `@onflow/fcl@1.0.0`)** Used in conjunction with stored interactions. Possible values: `local`, `testnet`, `mainnet`
* `fcl.limit` -- Specifies fallback compute limit if not provided in transaction. Provided as integer.
* `flow.network` (recommended) -- **(INTRODUCED `@onflow/fcl@1.0.0`)** Used in conjunction with stored interactions and provides FCLCryptoContract address for `testnet` and `mainnet`. Possible values: `local`, `testnet`, `mainnet`.
* `service.OpenID.scopes` - **(INTRODUCED `@onflow/fcl@0.0.68`)** Open ID Connect claims for Wallets and OpenID services.
* `walletconnect.projectId` -- **(INTRODUCED `@onflow/fcl@1.11.0`)** Your app's WalletConnect project ID. See [WalletConnect Cloud](https://cloud.walletconnect.com/sign-in) to obtain a project ID for your application.
* `walletconnect.disableNotifications` -- **(INTRODUCED `@onflow/fcl@1.13.0`)** Flag to disable pending WalletConnect request notifications within the application's UI. Default is `false`.

## Use contracts in scripts and transactions[​](#use-contracts-in-scripts-and-transactions "Direct link to Use contracts in scripts and transactions")

### Address replacement[​](#address-replacement "Direct link to Address replacement")

Configuration keys that start with `0x` will be replaced in FCL scripts and transactions. This allows you to write your script or transaction Cadence code once and not have to change it when you point your application at a difference instance of the Flow Blockchain.

`` _27

import * as fcl from '@onflow/fcl';

_27

_27

fcl.config().put('0xFungibleToken', '0xf233dcee88fe0abe');

_27

_27

async function myScript() {

_27

return fcl

_27

.send([

_27

fcl.script`

_27

import FungibleToken from 0xFungibleToken // will be replaced with 0xf233dcee88fe0abe because of the configuration

_27

_27

access(all) fun main() { /* Rest of the script goes here */ }

_27

`,

_27

])

_27

.then(fcl.decode);

_27

}

_27

_27

async function myTransaction() {

_27

return fcl

_27

.send([

_27

fcl.transaction`

_27

import FungibleToken from 0xFungibleToken // will be replaced with 0xf233dcee88fe0abe because of the configuration

_27

_27

transaction { /* Rest of the transaction goes here */ }

_27

`,

_27

])

_27

.then(fcl.decode);

_27

} ``

#### Example[​](#example "Direct link to Example")

`_13

import * as fcl from '@onflow/fcl';

_13

_13

fcl

_13

.config()

_13

.put('flow.network', 'testnet')

_13

.put('accessNode.api', 'https://rest-testnet.onflow.org')

_13

.put('discovery.wallet', 'https://fcl-discovery.onflow.org/testnet/authn')

_13

.put('walletconnect.projectId', 'YOUR_PROJECT_ID')

_13

.put('app.detail.title', 'Test Harness')

_13

.put('app.detail.icon', 'https://i.imgur.com/r23Zhvu.png')

_13

.put('app.detail.description', 'A test harness for FCL')

_13

.put('app.detail.url', 'https://myapp.com')

_13

.put('0xFlowToken', '0x7e60df042a9c0868');`

### Use `flow.json`[​](#use-flowjson "Direct link to use-flowjson")

A simpler way to import contracts in scripts and transactions is to use the `config.load` method to ingest your contracts from your `flow.json` file. This keeps the import syntax unified across tools and lets FCL figure out which address to use for what network based on the network provided in the config. To use `config.load` you must first import your `flow.json` file and then pass it to `config.load` as a parameter.

`` _10

import { config } from '@onflow/fcl';

_10

import flowJSON from '../flow.json';

_10

_10

config({

_10

'flow.network': 'testnet',

_10

'accessNode.api': 'https://rest-testnet.onflow.org',

_10

'discovery.wallet': `https://fcl-discovery.onflow.org/testnet/authn`,

_10

}).load({ flowJSON }); ``

Let's say your `flow.json` file looks like this:

`_10

{

_10

"contracts": {

_10

"HelloWorld": "cadence/contracts/HelloWorld.cdc"

_10

}

_10

}`

Then in your scripts and transactions, all you have to do is:

`_10

import "HelloWorld"`

FCL will automatically replace the contract name with the address for the network you use.

info

Never put private keys in your `flow.json`. Instead, use the [key/location syntax](/build/tools/flow-cli/flow.json/security) to separate your keys into a separate git ignored file.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/configure-fcl.md)

Last updated on **Dec 9, 2025** by **cshannon1218**

[Previous

Authentication](/build/tools/clients/fcl-js/authentication)[Next

Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

###### Rate this page

😞😐😊

Copy as Markdown

* [Configuration](#configuration)* [Set configuration values](#set-configuration-values)* [Get configuration values](#get-configuration-values)* [Common configuration keys](#common-configuration-keys)* [Use contracts in scripts and transactions](#use-contracts-in-scripts-and-transactions)
          + [Address replacement](#address-replacement)+ [Use `flow.json`](#use-flowjson)

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