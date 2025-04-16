# Source: https://developers.flow.com/tools/clients/fcl-js/configure-fcl

How to Configure FCL | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)

    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Cross VM Packages](/tools/clients/fcl-js/cross-vm)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* How to Configure FCL

On this page

# How to Configure FCL

## Configuration[​](#configuration "Direct link to Configuration")

FCL provides a mechanism to configure various aspects of its behavior. The key principle is that when switching between different Flow Blockchain environments (e.g., Local Emulator → Testnet → Mainnet), the only required change should be your FCL configuration.

## Setting Configuration Values[​](#setting-configuration-values "Direct link to Setting Configuration Values")

Values only need to be set once. We recommend doing this once and as early in the life cycle as possible.
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

## Getting Configuration Values[​](#getting-configuration-values "Direct link to Getting Configuration Values")

The `config` instance has an asynchronous `get` method. You can also pass it a fallback value incase the configuration state does not include what you are wanting.

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

## Common Configuration Keys[​](#common-configuration-keys "Direct link to Common Configuration Keys")

* `accessNode.api` -- Api URL for the Flow Blockchain Access Node you want to be communicating with.
* `app.detail.title` - **(INTRODUCED `@onflow/fcl@0.0.68`)** Your applications title, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service.
* `app.detail.icon` - **(INTRODUCED `@onflow/fcl@0.0.68`)** Url for your applications icon, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service.
* `app.detail.description` - **(INTRODUCED `@onflow/fcl@1.11.0`)** Your applications description, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service.
* `app.detail.url` - **(INTRODUCED `@onflow/fcl@1.11.0`)** Your applications url, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service.
* `challenge.handshake` -- **(DEPRECATED `@onflow/fcl@0.0.68`)** Points FCL at the Wallet or Wallet Discovery mechanism.
* `discovery.wallet` -- **(INTRODUCED `@onflow/fcl@0.0.68`)** Points FCL at the Wallet or Wallet Discovery mechanism.
* `discovery.wallet.method` -- Describes which service strategy a wallet should use: `IFRAME/RPC`, `POP/RPC`, `TAB/RPC`, `HTTP/POST`, `EXT/RPC`
* `env` -- **(DEPRECATED `@onflow/fcl@1.0.0`)** Used in conjunction with stored interactions. Possible values: `local`, `testnet`, `mainnet`
* `fcl.limit` -- Specifies fallback compute limit if not provided in transaction. Provided as integer.
* `flow.network` (recommended) -- **(INTRODUCED `@onflow/fcl@1.0.0`)** Used in conjunction with stored interactions and provides FCLCryptoContract address for `testnet` and `mainnet`. Possible values: `local`, `testnet`, `mainnet`.
* `service.OpenID.scopes` - **(INTRODUCED `@onflow/fcl@0.0.68`)** Open ID Connect claims for Wallets and OpenID services.
* `walletconnect.projectId` -- **(INTRODUCED `@onflow/fcl@1.11.0`)** Your app's WalletConnect project ID. See [WalletConnect Cloud](https://cloud.walletconnect.com/sign-in) to obtain a project ID for your application.
* `walletconnect.disableNotifications` -- **(INTRODUCED `@onflow/fcl@1.13.0`)** Flag to disable pending WalletConnect request notifications within the application's UI. Default is `false`.

## Using Contracts in Scripts and Transactions[​](#using-contracts-in-scripts-and-transactions "Direct link to Using Contracts in Scripts and Transactions")

### Address Replacement[​](#address-replacement "Direct link to Address Replacement")

Configuration keys that start with `0x` will be replaced in FCL scripts and transactions, this allows you to write your script or transaction Cadence code once and not have to change it when you point your application at a difference instance of the Flow Blockchain.

`_27

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

}`

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

### Using `flow.json`[​](#using-flowjson "Direct link to using-flowjson")

A simpler way to import contracts in scripts and transactions is to use the `config.load` method to ingest your contracts from your `flow.json` file. This keeps the import syntax unified across tools and lets FCL figure out which address to use for what network based on the network provided in config. To use `config.load` you must first import your `flow.json` file and then pass it to `config.load` as a parameter.

`_10

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

}).load({ flowJSON });`

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

FCL will automatically replace the contract name with the address for the network you are using.

> Note: never put private keys in your `flow.json`. You should use the [key/location syntax](/tools/flow-cli/flow.json/security) to separate your keys into a separate git ignored file.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/configure-fcl.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

[Previous

Authentication](/tools/clients/fcl-js/authentication)[Next

Cross VM Packages](/tools/clients/fcl-js/cross-vm)

###### Rate this page

😞😐😊

* [Configuration](#configuration)
* [Setting Configuration Values](#setting-configuration-values)
* [Getting Configuration Values](#getting-configuration-values)
* [Common Configuration Keys](#common-configuration-keys)
* [Using Contracts in Scripts and Transactions](#using-contracts-in-scripts-and-transactions)
  + [Address Replacement](#address-replacement)
  + [Using `flow.json`](#using-flowjson)

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
* [Flowscan Mainnet](https://flowscan.io/)
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