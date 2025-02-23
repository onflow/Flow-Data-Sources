# Source: https://developers.flow.com/tools/clients/fcl-js/api




Flow Client Library (FCL) API Reference | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
  + [Flow Client Library (FCL)](/tools/clients/fcl-js)
    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* [Clients](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* FCL Reference
On this page
# Flow Client Library (FCL) API Reference

> For release updates, [see the repo](https://github.com/onflow/fcl-js/releases)

## Configuration[​](#configuration "Direct link to Configuration")

FCL has a mechanism that lets you configure various aspects of FCL. When you move from one instance of the Flow Blockchain to another (Local Emulator to Testnet to Mainnet) the only thing you should need to change for your FCL implementation is your configuration.

---

### Setting Configuration Values[​](#setting-configuration-values "Direct link to Setting Configuration Values")

Values only need to be set once. We recommend doing this once and as early in the life cycle as possible. To set a configuration value, the `put` method on the `config` instance needs to be called, the `put` method returns the `config` instance so they can be chained.

Alternatively, you can set the config by passing a JSON object directly.

 `_13import * as fcl from '@onflow/fcl';_13_13fcl_13 .config() // returns the config instance_13 .put('foo', 'bar') // configures "foo" to be "bar"_13 .put('baz', 'buz'); // configures "baz" to be "buz"_13_13// OR_13_13fcl.config({_13 foo: 'bar',_13 baz: 'buz',_13});`
### Getting Configuration Values[​](#getting-configuration-values "Direct link to Getting Configuration Values")

The `config` instance has an **asynchronous** `get` method. You can also pass it a fallback value.

 `_15import * as fcl from '@onflow/fcl';_15_15fcl.config().put('foo', 'bar').put('woot', 5).put('rawr', 7);_15_15const FALLBACK = 1;_15_15async function addStuff() {_15 var woot = await fcl.config().get('woot', FALLBACK); // will be 5 -- set in the config before_15 var rawr = await fcl.config().get('rawr', FALLBACK); // will be 7 -- set in the config before_15 var hmmm = await fcl.config().get('hmmm', FALLBACK); // will be 1 -- uses fallback because this isnt in the config_15_15 return woot + rawr + hmmm;_15}_15_15addStuff().then((d) => console.log(d)); // 13 (5 + 7 + 1)`
### Common Configuration Keys[​](#common-configuration-keys "Direct link to Common Configuration Keys")

| Name | Example | Description |
| --- | --- | --- |
| `accessNode.api` **(required)** | `https://rest-testnet.onflow.org` | API URL for the Flow Blockchain Access Node you want to be communicating with. See all available access node endpoints [here](https://developers.onflow.org/http-api/). |
| `app.detail.title` | `Cryptokitties` | Your applications title, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service. |
| `app.detail.icon` | `https://fcl-discovery.onflow.org/images/blocto.png` | Url for your applications icon, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service. |
| `app.detail.description` | `Cryptokitties is a blockchain game` | Your applications description, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service. |
| `app.detail.url` | `https://cryptokitties.co` | Your applications url, can be requested by wallets and other services. Used by WalletConnect plugin & Wallet Discovery service. |
| `challenge.handshake` | **DEPRECATED** | Use `discovery.wallet` instead. |
| `discovery.authn.endpoint` | `https://fcl-discovery.onflow.org/api/testnet/authn` | Endpoint for alternative configurable Wallet Discovery mechanism. Read more on [discovery](#discovery) |
| `discovery.wallet` **(required)** | `https://fcl-discovery.onflow.org/testnet/authn` | Points FCL at the Wallet or Wallet Discovery mechanism. |
| `discovery.wallet.method` | `IFRAME/RPC`, `POP/RPC`, `TAB/RPC`, `HTTP/POST`, or `EXT/RPC` | Describes which service strategy a wallet should use. |
| `fcl.limit` | `100` | Specifies fallback compute limit if not provided in transaction. Provided as integer. |
| `flow.network` **(recommended)** | `testnet` | Used in conjunction with stored interactions and provides FCLCryptoContract address for `testnet` and `mainnet`. Possible values: `local`, `testnet`, `mainnet`. |
| `walletconnect.projectId` | `YOUR_PROJECT_ID` | Your app's WalletConnect project ID. See [WalletConnect Cloud](https://cloud.walletconnect.com/sign-in) to obtain a project ID for your application. |
| `walletconnect.disableNotifications` | `false` | Optional flag to disable pending WalletConnect request notifications within the application's UI. |

## Using Contracts in Scripts and Transactions[​](#using-contracts-in-scripts-and-transactions "Direct link to Using Contracts in Scripts and Transactions")

### Address Replacement[​](#address-replacement "Direct link to Address Replacement")

Configuration keys that start with `0x` will be replaced in FCL scripts and transactions, this allows you to write your script or transaction Cadence code once and not have to change it when you point your application at a difference instance of the Flow Blockchain.

 `_27import * as fcl from '@onflow/fcl';_27_27fcl.config().put('0xFungibleToken', '0xf233dcee88fe0abe');_27_27async function myScript() {_27 return fcl_27 .send([_27 fcl.script`_27 import FungibleToken from 0xFungibleToken // will be replaced with 0xf233dcee88fe0abe because of the configuration_27_27 access(all) fun main() { /* Rest of the script goes here */ }_27 `,_27 ])_27 .then(fcl.decode);_27}_27_27async function myTransaction() {_27 return fcl_27 .send([_27 fcl.transaction`_27 import FungibleToken from 0xFungibleToken // will be replaced with 0xf233dcee88fe0abe because of the configuration_27_27 transaction { /* Rest of the transaction goes here */ }_27 `,_27 ])_27 .then(fcl.decode);_27}`
#### Example[​](#example "Direct link to Example")

 `_14import * as fcl from '@onflow/fcl';_14_14fcl_14 .config()_14 .put('flow.network', 'testnet')_14 .put('walletconnect.projectId', 'YOUR_PROJECT_ID')_14 .put('accessNode.api', 'https://rest-testnet.onflow.org')_14 .put('discovery.wallet', 'https://fcl-discovery.onflow.org/testnet/authn')_14 .put('app.detail.title', 'Test Harness')_14 .put('app.detail.icon', 'https://i.imgur.com/r23Zhvu.png')_14 .put('app.detail.description', 'A test harness for FCL')_14 .put('app.detail.url', 'https://myapp.com')_14 .put('service.OpenID.scopes', 'email email_verified name zoneinfo')_14 .put('0xFlowToken', '0x7e60df042a9c0868');`
### Using `flow.json` for Contract Imports[​](#using-flowjson-for-contract-imports "Direct link to using-flowjson-for-contract-imports")

A simpler and more flexible way to manage contract imports in scripts and transactions is by using the `config.load` method in FCL. This lets you load contract configurations from a `flow.json` file, keeping your import syntax clean and allowing FCL to pick the correct contract addresses based on the network you're using.

### Setting Up[​](#setting-up "Direct link to Setting Up")

#### 1. Define Your Contracts in `flow.json`[​](#1-define-your-contracts-in-flowjson "Direct link to 1-define-your-contracts-in-flowjson")

Here’s an example of a `flow.json` file with aliases for multiple networks:

 `_11{_11 "contracts": {_11 "HelloWorld": {_11 "source": "./cadence/contracts/HelloWorld.cdc",_11 "aliases": {_11 "testnet": "0x1cf0e2f2f715450",_11 "mainnet": "0xf8d6e0586b0a20c7"_11 }_11 }_11 }_11}`

* **`source`**: Points to the contract file in your project.
* **`aliases`**: Maps each network to the correct contract address.

#### 2. Configure FCL[​](#2-configure-fcl "Direct link to 2. Configure FCL")

Load the `flow.json` file and set up FCL to use it:

 `_10import { config } from '@onflow/fcl';_10import flowJSON from '../flow.json';_10_10config({_10 'flow.network': 'testnet', // Choose your network, e.g., testnet or mainnet_10 'accessNode.api': 'https://rest-testnet.onflow.org', // Access node for the network_10 'discovery.wallet': `https://fcl-discovery.onflow.org/testnet/authn`, // Wallet discovery_10}).load({ flowJSON });`

With this setup, FCL will automatically use the correct contract address based on the selected network (e.g., `testnet` or `mainnet`).

#### 3. Use Contract Names in Scripts and Transactions[​](#3-use-contract-names-in-scripts-and-transactions "Direct link to 3. Use Contract Names in Scripts and Transactions")

After setting up `flow.json`, you can import contracts by name in your Cadence scripts or transactions:

 `_10import "HelloWorld"_10_10access(all) fun main(): String {_10 return HelloWorld.sayHello()_10}`

FCL replaces `"HelloWorld"` with the correct address from the `flow.json` configuration.

> **Note**: Don’t store private keys in your `flow.json`. Instead, use the [key/location syntax](/tools/flow-cli/flow.json/security) to keep sensitive keys in a separate, `.gitignore`-protected file.

## Wallet Interactions[​](#wallet-interactions "Direct link to Wallet Interactions")

These methods allows dapps to interact with FCL compatible wallets in order to authenticate the user and authorize transactions on their behalf.

> ⚠️These methods are **async**.

---

### `authenticate`[​](#authenticate "Direct link to authenticate")

> ⚠️**This method can only be used in web browsers.**

Calling this method will authenticate the current user via any wallet that supports FCL. Once called, FCL will initiate communication with the configured `discovery.wallet` endpoint which lets the user select a wallet to authenticate with. Once the wallet provider has authenticated the user, FCL will set the values on the [current user](#currentuserobject) object for future use and authorization.

#### Note[​](#note "Direct link to Note")

⚠️`discovery.wallet` value **must** be set in the configuration before calling this method. See [FCL Configuration](#configuration).

📣 The default discovery endpoint will open an iframe overlay to let the user choose a supported wallet.

#### Usage[​](#usage "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10fcl_10 .config()_10 .put('accessNode.api', 'https://rest-testnet.onflow.org')_10 .put('discovery.wallet', 'https://fcl-discovery.onflow.org/testnet/authn');_10// anywhere on the page_10fcl.authenticate();`
#### Note[​](#note-1 "Direct link to Note")

⚠️ `authenticate` can also take a service returned from [discovery](#discovery) with `fcl.authenticate({ service })`.

---

### `unauthenticate`[​](#unauthenticate "Direct link to unauthenticate")

> ⚠️**This method can only be used in web browsers.**

Logs out the current user and sets the values on the [current user](#currentuserobject) object to null.

#### Note[​](#note-2 "Direct link to Note")

⚠️The current user must be authenticated first.

#### Usage[​](#usage-1 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10fcl.config().put('accessNode.api', 'https://rest-testnet.onflow.org');_10// first authenticate to set current user_10fcl.authenticate();_10// ... somewhere else & sometime later_10fcl.unauthenticate();_10// fcl.currentUser.loggedIn === null`

---

### `reauthenticate`[​](#reauthenticate "Direct link to reauthenticate")

> ⚠️**This method can only be used in web browsers.**

A **convenience method** that calls [`fcl.unauthenticate()`](#unauthenticate) and then [`fcl.authenticate()`](#authenticate) for the current user.

#### Note[​](#note-3 "Direct link to Note")

⚠️The current user must be authenticated first.

#### Usage[​](#usage-2 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10// first authenticate to set current user_10fcl.authenticate();_10// ... somewhere else & sometime later_10fcl.reauthenticate();_10// logs out user and opens up login/sign-up flow`

---

### `signUp`[​](#signup "Direct link to signup")

> ⚠️**This method can only be used in web browsers.**

A **convenience method** that calls and is equivalent to [`fcl.authenticate()`](#authenticate).

---

### `logIn`[​](#login "Direct link to login")

> ⚠️**This method can only be used in web browsers.**

A **convenience method** that calls and is equivalent to [`fcl.authenticate()`](#authenticate).

---

### `authz`[​](#authz "Direct link to authz")

A **convenience method** that produces the needed authorization details for the current user to submit transactions to Flow. It defines a signing function that connects to a user's wallet provider to produce signatures to submit transactions.

> 📣 You can replace this function with your own [authorization function](#authorization-function) if needed.

#### Returns[​](#returns "Direct link to Returns")

| Type | Description |
| --- | --- |
| [AuthorizationObject](#authorizationobject) | An object containing the necessary details from the current user to authorize a transaction in any role. |

#### Usage[​](#usage-3 "Direct link to Usage")

**Note:** The default values for `proposer`, `payer`, and `authorizations` are already `fcl.authz` so there is no need to include these parameters, it is shown only for example purposes. See more on [signing roles](/build/basics/transactions).

 `_22import * as fcl from '@onflow/fcl';_22// login somewhere before_22fcl.authenticate();_22// once logged in authz will produce values_22console.log(fcl.authz);_22// prints {addr, signingFunction, keyId, sequenceNum} from the current authenticated user._22_22const txId = await fcl.mutate({_22 cadence: `_22 import Profile from 0xba1132bc08f82fe2_22 _22 transaction(name: String) {_22 prepare(account: auth(BorrowValue) &Account) {_22 account.storage.borrow<&{Profile.Owner}>(from: Profile.privatePath)!.setName(name)_22 }_22 }_22 `,_22 args: (arg, t) => [arg('myName', t.String)],_22 proposer: fcl.authz, // optional - default is fcl.authz_22 payer: fcl.authz, // optional - default is fcl.authz_22 authorizations: [fcl.authz], // optional - default is [fcl.authz]_22});`

---

## Current User[​](#current-user "Direct link to Current User")

Holds the [current user](#currentuserobject), if set, and offers a set of functions to manage the authentication and authorization of the user.

> ⚠️**The following methods can only be used in web browsers.**

---

### `currentUser.subscribe`[​](#currentusersubscribe "Direct link to currentusersubscribe")

The callback passed to subscribe will be called when the user authenticates and un-authenticates, making it easy to update the UI accordingly.

#### Arguments[​](#arguments "Direct link to Arguments")

| Name | Type |  |
| --- | --- | --- |
| `callback` | function | The callback will be called with the [current user](#currentuserobject) as the first argument when the current user is set or removed. |

#### Usage[​](#usage-4 "Direct link to Usage")

 `_24import React, { useState, useEffect } from 'react';_24import * as fcl from '@onflow/fcl';_24_24export function AuthCluster() {_24 const [user, setUser] = useState({ loggedIn: null });_24 useEffect(() => fcl.currentUser.subscribe(setUser), []); // sets the callback for FCL to use_24_24 if (user.loggedIn) {_24 return (_24 <div>_24 <span>{user?.addr ?? 'No Address'}</span>_24 <button onClick={fcl.unauthenticate}>Log Out</button> {/* once logged out in setUser(user) will be called */}_24 </div>_24 );_24 } else {_24 return (_24 <div>_24 <button onClick={fcl.logIn}>Log In</button>{' '}_24 {/* once logged in setUser(user) will be called */}_24 <button onClick={fcl.signUp}>Sign Up</button> {/* once signed up, setUser(user) will be called */}_24 </div>_24 );_24 }_24}`

---

### `currentUser.snapshot`[​](#currentusersnapshot "Direct link to currentusersnapshot")

Returns the [current user](#currentuserobject) object. This is the same object that is set and available on [`fcl.currentUser.subscribe(callback)`](#currentusersubscribe).

#### Usage[​](#usage-5 "Direct link to Usage")

 `_10// returns the current user object_10const user = fcl.currentUser.snapshot();_10_10// subscribes to the current user object and logs to console on changes_10fcl.currentUser.subscribe(console.log);`

---

### `currentUser.authenticate`[​](#currentuserauthenticate "Direct link to currentuserauthenticate")

Equivalent to `fcl.authenticate`.

---

### `currentUser.unauthenticate`[​](#currentuserunauthenticate "Direct link to currentuserunauthenticate")

Equivalent to `fcl.unauthenticate`.

---

### `currentUser.authorization`[​](#currentuserauthorization "Direct link to currentuserauthorization")

Equivalent to `fcl.authz`

---

### `currentUser.signUserMessage`[​](#currentusersignusermessage "Direct link to currentusersignusermessage")

A method to use allowing the user to personally sign data via FCL Compatible Wallets/Services.

> ⚠️ This method requires the current user's wallet to support a signing service endpoint. Currently, only Blocto is compatible with this feature by default.

#### Arguments[​](#arguments-1 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `message` | string **(required)** | A hexadecimal string to be signed |

#### Returns[​](#returns-1 "Direct link to Returns")

| Type | Description |
| --- | --- |
| `Array` | An Array of [CompositeSignatures](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/wallet-provider-spec/draft-v2.md#compositesignature): signature |

#### Usage[​](#usage-6 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10export const signMessage = async () => {_10 const MSG = Buffer.from('FOO').toString('hex');_10 try {_10 return await currentUser.signUserMessage(MSG);_10 } catch (error) {_10 console.log(error);_10 }_10};`

---

## Discovery[​](#discovery "Direct link to Discovery")

### `discovery`[​](#discovery-1 "Direct link to discovery-1")

Discovery abstracts away code so that developers don't have to deal with the discovery of Flow compatible wallets, integration, or authentication. Using `discovery` from FCL allows dapps to list and authenticate with wallets while having full control over the UI. Common use cases for this are login or registration pages.

(Alternatively, if you don't need control over your UI you can continue to use the `discovery.wallet` config value documented in the [Quickstart](/build/getting-started/fcl-quickstart) for the simplest configuration.)

> ⚠️**The following methods can only be used in web browsers.**

#### Note[​](#note-4 "Direct link to Note")

⚠️`discovery.authn.endpoint` value **must** be set in the configuration before calling this method. See [FCL Configuration](#configuration).

### Suggested Configuration[​](#suggested-configuration "Direct link to Suggested Configuration")

| Environment | Example |
| --- | --- |
| Mainnet | `https://fcl-discovery.onflow.org/api/authn` |
| Testnet | `https://fcl-discovery.onflow.org/api/testnet/authn` |

If the Discovery endpoint is set in config, then you can iterate through authn services and pass the chosen service to [authenticate](#authenticate) to authenticate a user.

#### Usage[​](#usage-7 "Direct link to Usage")

 `_24import './config';_24import { useState, useEffect } from 'react';_24import * as fcl from '@onflow/fcl';_24_24function Component() {_24 const [wallets, setWallets] = useState([]);_24 useEffect(_24 () => fcl.discovery.authn.subscribe((res) => setWallets(res.results)),_24 [],_24 );_24_24 return (_24 <div>_24 {wallets.map((wallet) => (_24 <button_24 key={wallet.provider.address}_24 onClick={() => fcl.authenticate({ service: wallet })}_24 >_24 Login with {wallet.provider.name}_24 </button>_24 ))}_24 </div>_24 );_24}`
### authn[​](#authn "Direct link to authn")

#### More Configuration[​](#more-configuration "Direct link to More Configuration")

By default, limited functionality services or services that require developer registration, like Ledger or Dapper Wallet, require apps to opt-in in order to display to users. To enable opt-in services in an application, use the `discovery.authn.include` property in your configuration with a value of an array of services you'd like your app to opt-in to displaying for users.

 `_10import { config } from '@onflow/fcl';_10_10config({_10 'discovery.authn.endpoint':_10 'https://fcl-discovery.onflow.org/api/testnet/authn', // Endpoint set to Testnet_10 'discovery.authn.include': ['0x9d2e44203cb13051'], // Ledger wallet address on Testnet set to be included_10});`

**Opt-In Wallet Addresses on Testnet and Mainnet**

| Service | Testnet | Mainnet |
| --- | --- | --- |
| `Dapper Wallet` | 0x82ec283f88a62e65 | 0xead892083b3e2c6c |
| `Ledger` | 0x9d2e44203cb13051 | 0xe5cd26afebe62781 |

For more details on wallets, view the [service list here](https://github.com/onflow/fcl-discovery/blob/87e172db85d185882d9fde007c95f08bc2a1cccb/data/services.json).

---

### `discovery.authn.snapshot()`[​](#discoveryauthnsnapshot "Direct link to discoveryauthnsnapshot")

Return a list of `authn` services.

### `discovery.authn.subscribe(callback)`[​](#discoveryauthnsubscribecallback "Direct link to discoveryauthnsubscribecallback")

The callback sent to `subscribe` will be called with a list of `authn` services.

---

## On-chain Interactions[​](#on-chain-interactions "Direct link to On-chain Interactions")

> 📣 **These methods can be used in browsers and NodeJS.**

These methods allows dapps to interact directly with the Flow blockchain via a set of functions that currently use the [Access Node API](/networks/access-onchain-data).

---

### Query and Mutate Flow with Cadence[​](#query-and-mutate-flow-with-cadence "Direct link to Query and Mutate Flow with Cadence")

If you want to run arbitrary Cadence scripts on the blockchain, these methods offer a convenient way to do so **without having to build, send, and decode interactions**.

### `query`[​](#query "Direct link to query")

Allows you to submit scripts to query the blockchain.

#### Options[​](#options "Direct link to Options")

*Pass in the following as a single object with the following keys.All keys are optional unless otherwise stated.*

| Key | Type | Description |
| --- | --- | --- |
| `cadence` | string **(required)** | A valid cadence script. |
| `args` | [ArgumentFunction](#argumentfunction) | Any arguments to the script if needed should be supplied via a function that returns an array of arguments. |
| `limit` | number | Compute (Gas) limit for query. Read the [documentation about computation cost](/build/basics/fees) for information about how computation cost is calculated on Flow. |

#### Returns[​](#returns-2 "Direct link to Returns")

| Type | Description |
| --- | --- |
| any | A JSON representation of the response. |

#### Usage[​](#usage-8 "Direct link to Usage")

 `_16import * as fcl from '@onflow/fcl';_16_16const result = await fcl.query({_16 cadence: `_16 access(all) fun main(a: Int, b: Int, addr: Address): Int {_16 log(addr)_16 return a + b_16 }_16 `,_16 args: (arg, t) => [_16 arg(7, t.Int), // a: Int_16 arg(6, t.Int), // b: Int_16 arg('0xba1132bc08f82fe2', t.Address), // addr: Address_16 ],_16});_16console.log(result); // 13`
#### Examples[​](#examples "Direct link to Examples")

* [Additional Explanation](https://gist.github.com/orodio/3bf977a0bd45b990d16fdc1459b129a2)

---

### `mutate`[​](#mutate "Direct link to mutate")

Allows you to submit transactions to the blockchain to potentially mutate the state.

⚠️When being used in the browser, `fcl.mutate` uses the built-in `fcl.authz` function to produce the authorization (signatures) for the current user. When calling this method from Node.js, you will need to supply your own custom authorization function.

#### Options[​](#options-1 "Direct link to Options")

*Pass in the following as a single object with the following keys. All keys are optional unless otherwise stated.*

| Key | Type | Description |
| --- | --- | --- |
| `cadence` | string **(required)** | A valid cadence transaction. |
| `args` | [ArgumentFunction](#argumentfunction) | Any arguments to the script if needed should be supplied via a function that returns an array of arguments. |
| `limit` | number | Compute (Gas) limit for query. Read the [documentation about computation cost](/tools/clients/flow-go-sdk#gas-limit) for information about how computation cost is calculated on Flow. |
| `proposer` | [AuthorizationFunction](#authorization-function) | The authorization function that returns a valid [AuthorizationObject](#authorizationobject) for the [proposer role](#transactionrolesobject). |

#### Returns[​](#returns-3 "Direct link to Returns")

| Type | Description |
| --- | --- |
| string | The transaction ID. |

#### Usage[​](#usage-9 "Direct link to Usage")

 `_16import * as fcl from '@onflow/fcl';_16// login somewhere before_16fcl.authenticate();_16_16const txId = await fcl.mutate({_16 cadence: `_16 import Profile from 0xba1132bc08f82fe2_16 _16 transaction(name: String) {_16 prepare(account: auth(BorrowValue) &Account) {_16 account.storage.borrow<&{Profile.Owner}>(from: Profile.privatePath)!.setName(name)_16 }_16 }_16 `,_16 args: (arg, t) => [arg('myName', t.String)],_16});`
#### Examples[​](#examples-1 "Direct link to Examples")

* [Additional explanation](https://gist.github.com/orodio/3bf977a0bd45b990d16fdc1459b129a2)
* [Custom authorization function](#authorization-function)

---

### `verifyUserSignatures` (Deprecated)[​](#verifyusersignatures-deprecated "Direct link to verifyusersignatures-deprecated")

Use `fcl.AppUtils.verifyUserSignatures`

## AppUtils[​](#apputils "Direct link to AppUtils")

### `AppUtils.verifyUserSignatures`[​](#apputilsverifyusersignatures "Direct link to apputilsverifyusersignatures")

A method allowing applications to cryptographically verify a message was signed by a user's private key/s. This is typically used with the response from `currentUser.signUserMessage`.

#### Note[​](#note-5 "Direct link to Note")

⚠️ `fcl.config.flow.network` or options override is required to use this api. See [FCL Configuration](#configuration).

#### Arguments[​](#arguments-2 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `message` | string **(required)** | A hexadecimal string |
| `compositeSignatures` | Array **(required)** | An Array of `CompositeSignatures` |
| `opts` | Object **(optional)** | `opts.fclCryptoContract` can be provided to override FCLCryptoContract address for local development |

#### Returns[​](#returns-4 "Direct link to Returns")

| Type | Description |
| --- | --- |
| Boolean | `true` if verified or `false` |

#### Usage[​](#usage-10 "Direct link to Usage")

 `_15import * as fcl from '@onflow/fcl';_15_15const isValid = await fcl.AppUtils.verifyUserSignatures(_15 Buffer.from('FOO').toString('hex'),_15 [_15 {_15 f_type: 'CompositeSignature',_15 f_vsn: '1.0.0',_15 addr: '0x123',_15 keyId: 0,_15 signature: 'abc123',_15 },_15 ],_15 { fclCryptoContract },_15);`
#### Examples[​](#examples-2 "Direct link to Examples")

* [fcl-next-harness](https://github.com/onflow/fcl-next-harness)

---

### `AppUtils.verifyAccountProof`[​](#apputilsverifyaccountproof "Direct link to apputilsverifyaccountproof")

A method allowing applications to cryptographically prove that a user controls an on-chain account. During user authentication, some FCL compatible wallets will choose to support the FCL `account-proof` service. If a wallet chooses to support this service, and the user approves the signing of message data, they will return `account-proof` data and a signature(s) that can be used to prove a user controls an on-chain account.
See [proving-authentication](https://github.com/onflow/fcl-js/blob/master/docs/reference/proving-authentication.mdx) documentaion for more details.

⚠️ `fcl.config.flow.network` or options override is required to use this api. See [FCL Configuration](#configuration).

#### Arguments[​](#arguments-3 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `appIdentifier` | string **(required)** | A hexadecimal string |
| `accountProofData` | Object **(required)** | Object with properties: `address`: `string` - A Flow account address.  `nonce`: `string` - A random string in hexadecimal format (minimum 32 bytes in total, i.e 64 hex characters)  `signatures`: `Object[]` - An array of composite signatures to verify |
| `opts` | Object **(optional)** | `opts.fclCryptoContract` can be provided to overide FCLCryptoContract address for local development |

#### Returns[​](#returns-5 "Direct link to Returns")

| Type | Description |
| --- | --- |
| Boolean | `true` if verified or `false` |

#### Usage[​](#usage-11 "Direct link to Usage")

 `_13import * as fcl from "@onflow/fcl"_13_13const accountProofData = {_13 address: "0x123",_13 nonce: "F0123"_13 signatures: [{f_type: "CompositeSignature", f_vsn: "1.0.0", addr: "0x123", keyId: 0, signature: "abc123"}],_13}_13_13const isValid = await fcl.AppUtils.verifyAccountProof(_13 "AwesomeAppId",_13 accountProofData,_13 {fclCryptoContract}_13)`
#### Examples[​](#examples-3 "Direct link to Examples")

* [fcl-next-harness](https://github.com/onflow/fcl-next-harness)

---

### Query and mutate the blockchain with Builders[​](#query-and-mutate-the-blockchain-with-builders "Direct link to Query and mutate the blockchain with Builders")

In some cases, you may want to utilize pre-built interactions or build more complex interactions than what the `fcl.query` and `fcl.mutate` interface offer. To do this, FCL uses a pattern of building up an interaction with a combination of builders, resolving them, and sending them to the chain.

> ⚠️**Recommendation:** Unless you have a specific use case that require usage of these builders, you should be able to achieve most cases with `fcl.query({...options}` or `fcl.mutate({...options})`

### `send`[​](#send "Direct link to send")

Sends arbitrary scripts, transactions, and requests to Flow.

This method consumes an array of [builders](#builders) that are to be resolved and sent. The builders required to be included in the array depend on the [interaction](#interaction) that is being built.

#### Note[​](#note-6 "Direct link to Note")

⚠️Must be used in conjuction with [`fcl.decode(response)`](#decode) to get back correct keys and all values in JSON.

#### Arguments[​](#arguments-4 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `builders` | [[Builders](#builders)] | See builder functions. |

#### Returns[​](#returns-6 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [ResponseObject](#responseobject) | An object containing the data returned from the chain. Should always be decoded with `fcl.decode()` to get back appropriate JSON keys and values. |

#### Usage[​](#usage-12 "Direct link to Usage")

 `_18import * as fcl from '@onflow/fcl';_18_18// a script only needs to resolve the arguments to the script_18const response = await fcl.send([fcl.script`${script}`, fcl.args(args)]);_18// note: response values are encoded, call await fcl.decode(response) to get JSON_18_18// a transaction requires multiple 'builders' that need to be resolved prior to being sent to the chain - such as setting the authorizations._18const response = await fcl.send([_18 fcl.transaction`_18 ${transaction}_18 `,_18 fcl.args(args),_18 fcl.proposer(proposer),_18 fcl.authorizations(authorizations),_18 fcl.payer(payer),_18 fcl.limit(9999),_18]);_18// note: response contains several values (Cad)`

---

### `decode`[​](#decode "Direct link to decode")

Decodes the response from `fcl.send()` into the appropriate JSON representation of any values returned from Cadence code.

#### Note[​](#note-7 "Direct link to Note")

📣 To define your own decoder, see [`tutorial`](https://github.com/onflow/fcl-js/tree/master/packages/sdk/src/decode).

#### Arguments[​](#arguments-5 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `response` | [ResponseObject](#responseobject) | Should be the response returned from `fcl.send([...])` |

#### Returns[​](#returns-7 "Direct link to Returns")

| Type | Description |
| --- | --- |
| any | A JSON representation of the raw string response depending on the cadence code executed. The return value can be a single value and type or an object with multiple types. |

#### Usage[​](#usage-13 "Direct link to Usage")

 `_16import * as fcl from '@onflow/fcl';_16_16// simple script to add 2 numbers_16const response = await fcl.send([_16 fcl.script`_16 access(all) fun main(int1: Int, int2: Int): Int {_16 return int1 + int2_16 }_16 `,_16 fcl.args([fcl.arg(1, fcl.t.Int), fcl.arg(2, fcl.t.Int)]),_16]);_16_16const decoded = await fcl.decode(response);_16_16assert(3 === decoded);_16assert(typeof decoded === 'number');`

---

## Builders[​](#builders "Direct link to Builders")

These methods fill out various portions of a transaction or script template in order to
build, resolve, and send it to the blockchain. A valid populated template is referred to as an [Interaction](#interaction).

⚠️**These methods must be used with `fcl.send([...builders]).then(fcl.decode)`**

### Query Builders[​](#query-builders "Direct link to Query Builders")

### `getAccount`[​](#getaccount "Direct link to getaccount")

A builder function that returns the interaction to get an account by address.

⚠️Consider using the pre-built interaction [`fcl.account(address)`](#account) if you do not need to pair with any other builders.

#### Arguments[​](#arguments-6 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `address` | [Address](#address) | Address of the user account with or without a prefix (both formats are supported). |

#### Returns after decoding[​](#returns-after-decoding "Direct link to Returns after decoding")

| Type | Description |
| --- | --- |
| [AccountObject](#account) | A JSON representation of a user account. |

#### Usage[​](#usage-14 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10// somewhere in an async function_10// fcl.account is the same as this function_10const getAccount = async (address) => {_10 const account = await fcl.send([fcl.getAccount(address)]).then(fcl.decode);_10 return account;_10};`

---

### `getBlock`[​](#getblock "Direct link to getblock")

A builder function that returns the interaction to get the latest block.

📣 Use with `fcl.atBlockId()` and `fcl.atBlockHeight()` when building the interaction to get information for older blocks.

⚠️Consider using the pre-built interaction [`fcl.getblock(isSealed)`](#getblock) if you do not need to pair with any other builders.

#### Arguments[​](#arguments-7 "Direct link to Arguments")

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `isSealed` | boolean | false | If the latest block should be sealed or not. See [block states](#interaction). |

#### Returns after decoding[​](#returns-after-decoding-1 "Direct link to Returns after decoding")

| Type | Description |
| --- | --- |
| [BlockObject](#blockobject) | The latest block if not used with any other builders. |

#### Usage[​](#usage-15 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const latestSealedBlock = await fcl_10 .send([_10 fcl.getBlock(true), // isSealed = true_10 ])_10 .then(fcl.decode);`

---

### `atBlockHeight`[​](#atblockheight "Direct link to atblockheight")

A builder function that returns a partial interaction to a block at a specific height.

⚠️Use with other interactions like [`fcl.getBlock()`](#getblock) to get a full interaction at the specified block height.

#### Arguments[​](#arguments-8 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `blockHeight` | number | The height of the block to execute the interaction at. |

#### Returns[​](#returns-8 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [Partial Interaction](#interaction) | A partial interaction to be paired with another interaction such as `fcl.getBlock()` or `fcl.getAccount()`. |

#### Usage[​](#usage-16 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10await fcl.send([fcl.getBlock(), fcl.atBlockHeight(123)]).then(fcl.decode);`

---

### `atBlockId`[​](#atblockid "Direct link to atblockid")

A builder function that returns a partial interaction to a block at a specific block ID.

⚠️Use with other interactions like [`fcl.getBlock()`](#getblock) to get a full interaction at the specified block ID.

#### Arguments[​](#arguments-9 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `blockId` | string | The ID of the block to execute the interaction at. |

#### Returns[​](#returns-9 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [Partial Interaction](#interaction) | A partial interaction to be paired with another interaction such as `fcl.getBlock()` or `fcl.getAccount()`. |

#### Usage[​](#usage-17 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10await fcl.send([fcl.getBlock(), fcl.atBlockId('23232323232')]).then(fcl.decode);`

---

### `getBlockHeader`[​](#getblockheader "Direct link to getblockheader")

A builder function that returns the interaction to get a block header.

📣 Use with `fcl.atBlockId()` and `fcl.atBlockHeight()` when building the interaction to get information for older blocks.

#### Returns after decoding[​](#returns-after-decoding-2 "Direct link to Returns after decoding")

| Type | Description |
| --- | --- |
| [BlockHeaderObject](#blockheaderobject) | The latest block header if not used with any other builders. |

#### Usage[​](#usage-18 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const latestBlockHeader = await fcl_10 .send([fcl.getBlockHeader()])_10 .then(fcl.decode);`
### `getEventsAtBlockHeightRange`[​](#geteventsatblockheightrange "Direct link to geteventsatblockheightrange")

A builder function that returns all instances of a particular event (by name) within a height range.

⚠️The block range provided must be from the current spork.

⚠️The block range provided must be 250 blocks or lower per request.

#### Arguments[​](#arguments-10 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `eventName` | [EventName](#eventname) | The name of the event. |
| `fromBlockHeight` | number | The height of the block to start looking for events (inclusive). |
| `toBlockHeight` | number | The height of the block to stop looking for events (inclusive). |

#### Returns after decoding[​](#returns-after-decoding-3 "Direct link to Returns after decoding")

| Type | Description |
| --- | --- |
| [[EventObject]](#event-object) | An array of events that matched the eventName. |

#### Usage[​](#usage-19 "Direct link to Usage")

 `_11import * as fcl from '@onflow/fcl';_11_11const events = await fcl_11 .send([_11 fcl.getEventsAtBlockHeightRange(_11 'A.7e60df042a9c0868.FlowToken.TokensWithdrawn',_11 35580624,_11 35580624,_11 ),_11 ])_11 .then(fcl.decode);`

---

### `getEventsAtBlockIds`[​](#geteventsatblockids "Direct link to geteventsatblockids")

A builder function that returns all instances of a particular event (by name) within a set of blocks, specified by block ids.

⚠️The block range provided must be from the current spork.

#### Arguments[​](#arguments-11 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `eventName` | [EventName](#eventname) | The name of the event. |
| `blockIds` | number | The ids of the blocks to scan for events. |

#### Returns after decoding[​](#returns-after-decoding-4 "Direct link to Returns after decoding")

| Type | Description |
| --- | --- |
| [[EventObject]](#event-object) | An array of events that matched the eventName. |

#### Usage[​](#usage-20 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const events = await fcl_10 .send([_10 fcl.getEventsAtBlockIds('A.7e60df042a9c0868.FlowToken.TokensWithdrawn', [_10 'c4f239d49e96d1e5fbcf1f31027a6e582e8c03fcd9954177b7723fdb03d938c7',_10 '5dbaa85922eb194a3dc463c946cc01c866f2ff2b88f3e59e21c0d8d00113273f',_10 ]),_10 ])_10 .then(fcl.decode);`

---

### `getCollection`[​](#getcollection "Direct link to getcollection")

A builder function that returns all a collection containing a list of transaction ids by its collection id.

⚠️The block range provided must be from the current spork. All events emitted during past sporks is current unavailable.

#### Arguments[​](#arguments-12 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `collectionID` | string | The id of the collection. |

#### Returns after decoding[​](#returns-after-decoding-5 "Direct link to Returns after decoding")

| Type | Description |
| --- | --- |
| [CollectionObject](#collectionobject) | An object with the id and a list of transactions within the requested collection. |

#### Usage[​](#usage-21 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const collection = await fcl_10 .send([_10 fcl.getCollection(_10 'cccdb0c67d015dc7f6444e8f62a3244ed650215ed66b90603006c70c5ef1f6e5',_10 ),_10 ])_10 .then(fcl.decode);`

---

### `getTransactionStatus`[​](#gettransactionstatus "Direct link to gettransactionstatus")

A builder function that returns the status of transaction in the form of a [TransactionStatusObject](#transactionstatusobject).

⚠️The transactionID provided must be from the current spork.

📣 Considering [subscribing to the transaction from `fcl.tx(id)`](#tx) instead of calling this method directly.

#### Arguments[​](#arguments-13 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `transactionId` | string | The transactionID returned when submitting a transaction. Example: `9dda5f281897389b99f103a1c6b180eec9dac870de846449a302103ce38453f3` |

#### Returns after decoding[​](#returns-after-decoding-6 "Direct link to Returns after decoding")

#### Returns[​](#returns-10 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [TransactionStatusObject](#transactionstatusobject) | Object representing the result/status of a transaction |

#### Usage[​](#usage-22 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const status = await fcl_10 .send([_10 fcl.getTransactionStatus(_10 '9dda5f281897389b99f103a1c6b180eec9dac870de846449a302103ce38453f3',_10 ),_10 ])_10 .then(fcl.decode);`

---

### `getTransaction`[​](#gettransaction "Direct link to gettransaction")

A builder function that returns a [transaction object](#transactionobject) once decoded.

⚠️The transactionID provided must be from the current spork.

📣 Considering using [`fcl.tx(id).onceSealed()`](#tx) instead of calling this method directly.

#### Arguments[​](#arguments-14 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `transactionId` | string | The transactionID returned when submitting a transaction. Example: `9dda5f281897389b99f103a1c6b180eec9dac870de846449a302103ce38453f3` |

#### Returns after decoding[​](#returns-after-decoding-7 "Direct link to Returns after decoding")

#### Returns[​](#returns-11 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [TransactionObject](#transactionobject) | An full transaction object containing a payload and signatures |

#### Usage[​](#usage-23 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const tx = await fcl_10 .send([_10 fcl.getTransaction(_10 '9dda5f281897389b99f103a1c6b180eec9dac870de846449a302103ce38453f3',_10 ),_10 ])_10 .then(fcl.decode);`

---

### `subscribeEvents`[​](#subscribeevents "Direct link to subscribeevents")

info

The subscribeEvents SDK builder is for more advanced use cases where you wish to directly specify a starting block to listen for events. For most use cases, consider using the pre-built interaction [`fcl.events(eventTypes)`](#events).

A build that returns a [event stream connection](#eventstream) once decoded. It will establish a WebSocket connection to the Access Node and subscribe to events with the given parameters.

#### Arguments[​](#arguments-15 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `opts` | `Object` | An object with the following keys: |
| `opts.startBlockId` | string | undefined | The block ID to start listening for events. Example: `9dda5f281897389b99f103a1c6b180eec9dac870de846449a302103ce38453f3` |
| `opts.startHeight` | number | undefined | The block height to start listening for events. Example: `123` |
| `opts.eventTypes` | string[] | undefined | The event types to listen for. Example: `A.7e60df042a9c0868.FlowToken.TokensWithdrawn` |
| `opts.addresses` | string[] | undefined | The addresses to listen for. Example: `0x7e60df042a9c0868` |
| `opts.contracts` | string[] | undefined | The contracts to listen for. Example: `0x7e60df042a9c0868` |
| `opts.heartbeatInterval` | number | undefined | The interval in milliseconds to send a heartbeat to the Access Node. Example: `10000` |

#### Returns after decoding[​](#returns-after-decoding-8 "Direct link to Returns after decoding")

#### Returns[​](#returns-12 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [EventStreamConnection](#eventstream) | A connection to the event stream |

#### Usage[​](#usage-24 "Direct link to Usage")

 `_27import * as fcl from '@onflow/fcl';_27_27const eventStream = await fcl_27 .send([_27 fcl.subscribeEvents({_27 eventTypes: 'A.7e60df042a9c0868.FlowToken.TokensWithdrawn',_27 }),_27 ])_27 .then(fcl.decode);_27_27eventStream.on('heartbeat', (heartbeat) => {_27 console.log(heartbeat);_27});_27_27eventStream.on('events', (event) => {_27 console.log(event);_27});_27_27eventStream.on('error', (error) => {_27 console.log(error);_27});_27_27eventStream.on('end', () => {_27 console.log('Connection closed');_27});_27_27eventStream.close();`

---

### `getEvents` (Deprecated)[​](#getevents-deprecated "Direct link to getevents-deprecated")

Use [`fcl.getEventsAtBlockHeightRange`](#geteventsatblockheightrange) or [`fcl.getEventsAtBlockIds`](#geteventsatblockids).

---

### `getLatestBlock` (Deprecated)[​](#getlatestblock-deprecated "Direct link to getlatestblock-deprecated")

Use [`fcl.getBlock`](#getblock).

---

### `getBlockById` (Deprecated)[​](#getblockbyid-deprecated "Direct link to getblockbyid-deprecated")

Use [`fcl.getBlock`](#getblock) and [`fcl.atBlockId`](#atblockid).

---

### `getBlockByHeight` (Deprecated)[​](#getblockbyheight-deprecated "Direct link to getblockbyheight-deprecated")

Use [`fcl.getBlock`](#getblock) and [`fcl.atBlockHeight`](#atblockheight).

---

### Utility Builders[​](#utility-builders "Direct link to Utility Builders")

These builders are used to compose interactions with other builders such as scripts and transactions.

> ⚠️**Recommendation:** Unless you have a specific use case that require usage of these builders, you should be able to achieve most cases with `fcl.query({...options}` or `fcl.mutate({...options})`

### `arg`[​](#arg "Direct link to arg")

A utility builder to be used with `fcl.args[...]` to create FCL supported arguments for interactions.

#### Arguments[​](#arguments-16 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `value` | any | Any value that you are looking to pass to other builders. |
| `type` | [FType](#ftype) | A type supported by Flow. |

#### Returns[​](#returns-13 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [ArgumentObject](#argumentobject) | Holds the value and type passed in. |

#### Usage[​](#usage-25 "Direct link to Usage")

 `_15import * as fcl from '@onflow/fcl';_15_15await fcl_15 .send([_15 fcl.script`_15 access(all) fun main(a: Int, b: Int): Int {_15 return a + b_15 }_15 `,_15 fcl.args([_15 fcl.arg(5, fcl.t.Int), // a_15 fcl.arg(4, fcl.t.Int), // b_15 ]),_15 ])_15 .then(fcl.decode);`

---

### `args`[​](#args "Direct link to args")

A utility builder to be used with other builders to pass in arguments with a value and supported type.

#### Arguments[​](#arguments-17 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `args` | [[Argument Objects]](#argumentobject) | An array of arguments that you are looking to pass to other builders. |

#### Returns[​](#returns-14 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [Partial Interaction](#interaction) | An interaction that contains the arguments and types passed in. This alone is a partial and incomplete interaction. |

#### Usage[​](#usage-26 "Direct link to Usage")

 `_15import * as fcl from '@onflow/fcl';_15_15await fcl_15 .send([_15 fcl.script`_15 access(all) fun main(a: Int, b: Int): Int {_15 return a + b_15 }_15 `,_15 fcl.args([_15 fcl.arg(5, fcl.t.Int), // a_15 fcl.arg(4, fcl.t.Int), // b_15 ]),_15 ])_15 .then(fcl.decode); // 9`

---

### Template Builders[​](#template-builders "Direct link to Template Builders")

> ⚠️***Recommended:*** The following functionality is simplified by [`fcl.query({...options}`](#query) or [`fcl.mutate({...options})`](#mutate) and is reccomended to use over the functions below.

### `script`[​](#script "Direct link to script")

A template builder to use a Cadence script for an interaction.

📣 Use with `fcl.args(...)` to pass in arguments dynamically.

#### Arguments[​](#arguments-18 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `CODE` | string | Should be valid Cadence script. |

#### Returns[​](#returns-15 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [Interaction](#interaction) | An interaction containing the code passed in. |

#### Usage[​](#usage-27 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const code = `_10 access(all) fun main(): Int {_10 return 5 + 4_10 }_10`;_10const answer = await fcl.send([fcl.script(code)]).then(fcl.decode);_10console.log(answer); // 9`

---

### `transaction`[​](#transaction "Direct link to transaction")

A template builder to use a Cadence transaction for an interaction.

⚠️Must be used with `fcl.payer`, `fcl.proposer`, `fcl.authorizations` to produce a valid interaction before sending to the chain.

📣 Use with `fcl.args[...]` to pass in arguments dynamically.

#### Arguments[​](#arguments-19 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `CODE` | string | Should be valid a Cadence transaction. |

#### Returns[​](#returns-16 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [Partial Interaction](#interaction) | An partial interaction containing the code passed in. Further builders are required to complete the interaction - see warning. |

#### Usage[​](#usage-28 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const code = `_10 access(all) fun main(): Int {_10 return 5 + 4_10 }_10`;_10const answer = await fcl.send([fcl.script(code)]).then(fcl.decode);_10console.log(answer); // 9`

---

## Pre-built Interactions[​](#pre-built-interactions "Direct link to Pre-built Interactions")

These functions are abstracted short hand ways to skip the send and decode steps of sending an interaction to the chain. More pre-built interactions are coming soon.

### `account`[​](#account "Direct link to account")

A pre-built interaction that returns the details of an account from their public address.

#### Arguments[​](#arguments-20 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `address` | [Address](#address) | Address of the user account with or without a prefix (both formats are supported). |

#### Returns[​](#returns-17 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [AccountObject](#accountobject) | A JSON representation of a user account. |

#### Usage[​](#usage-29 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10const account = await fcl.account('0x1d007d755706c469');`

---

### `block`[​](#block "Direct link to block")

A pre-built interaction that returns the latest block (optionally sealed or not), by id, or by height.

#### Arguments[​](#arguments-21 "Direct link to Arguments")

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `sealed` | boolean | false | If the latest block should be sealed or not. See [block states](#interaction). |
| `id` | string |  | ID of block to get. |
| `height` | int |  | Height of block to get. |

#### Returns[​](#returns-18 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [BlockObject](#blockobject) | A JSON representation of a block. |

#### Usage[​](#usage-30 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10await fcl.block(); // get latest finalized block_10await fcl.block({ sealed: true }); // get latest sealed block_10await fcl.block({_10 id: '0b1bdfa9ddaaf31d53c584f208313557d622d1fedee1586ffc38fb5400979faa',_10}); // get block by id_10await fcl.block({ height: 56481953 }); // get block by height`

---

### `latestBlock` (Deprecated)[​](#latestblock-deprecated "Direct link to latestblock-deprecated")

A pre-built interaction that returns the latest block (optionally sealed or not).

#### Arguments[​](#arguments-22 "Direct link to Arguments")

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `isSealed` | boolean | false | If the latest block should be sealed or not. See [block states](#interaction). |

#### Returns[​](#returns-19 "Direct link to Returns")

| Type | Description |
| --- | --- |
| [BlockObject](#blockobject) | A JSON representation of a block. |

#### Usage[​](#usage-31 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10const latestBlock = await fcl.latestBlock();`

---

## Transaction Status Utility[​](#transaction-status-utility "Direct link to Transaction Status Utility")

### `tx`[​](#tx "Direct link to tx")

A utility function that lets you set the transaction to get subsequent status updates (via polling) and the finalized result once available.
⚠️The poll rate is set at `2500ms` and will update at that interval until transaction is sealed.

#### Arguments[​](#arguments-23 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `transactionId` | string | A valid transaction id. |

#### Returns[​](#returns-20 "Direct link to Returns")

| Name | Type | Description |
| --- | --- | --- |
| `snapshot()` | function | Returns the current state of the transaction. |
| `subscribe(cb)` | function | Calls the `cb` passed in with the new transaction on a status change. |
| `onceFinalized()` | function | Provides the transaction once status `2` is returned. See [Tranasaction Statuses](#transaction-statuses). |
| `onceExecuted()` | function | Provides the transaction once status `3` is returned. See [Tranasaction Statuses](#transaction-statuses). |
| `onceSealed()` | function | Provides the transaction once status `4` is returned. See [Tranasaction Statuses](#transaction-statuses). |

#### Usage[​](#usage-32 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10_10const [txStatus, setTxStatus] = useState(null);_10useEffect(() => fcl.tx(txId).subscribe(setTxStatus));`

---

## Event Polling Utility[​](#event-polling-utility "Direct link to Event Polling Utility")

### `events`[​](#events "Direct link to events")

A utility function that lets you set the transaction to get subsequent status updates (via polling) and the finalized result once available.
⚠️The poll rate is set at `10000ms` and will update at that interval for getting new events.

Note:
⚠️`fcl.eventPollRate` value **could** be set to change the polling rate of all events subcribers, check [FCL Configuration](#configuration) for guide.

#### Arguments[​](#arguments-24 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `eventName` | string | A valid event name. |

#### Returns[​](#returns-21 "Direct link to Returns")

| Name | Type | Description |
| --- | --- | --- |
| `subscribe(cb)` | function | Calls the `cb` passed in with the new event. |

#### Usage[​](#usage-33 "Direct link to Usage")

 `_10import * as fcl from '@onflow/fcl';_10// in some react component_10fcl.events(eventName).subscribe((event) => {_10 console.log(event);_10});`
#### Examples[​](#examples-4 "Direct link to Examples")

* [Flow-view-source example](https://github.com/orodio/flow-view-source/blob/master/src/pages/event.comp.js)

---

## Types, Interfaces, and Definitions[​](#types-interfaces-and-definitions "Direct link to Types, Interfaces, and Definitions")

---

### `Builders`[​](#builders-1 "Direct link to builders-1")

Builders are modular functions that can be coupled together with `fcl.send([...builders])` to create an [Interaction](#interaction). The builders needed to create an interaction depend on the script or transaction that is being sent.

---

### `Interaction`[​](#interaction "Direct link to interaction")

An interaction is an object containing the information to perform an action on chain.This object is populated through builders and converted into the approriate access node API call. See the interaction object [here](https://github.com/onflow/fcl-js/blob/master/packages/sdk/src/interaction/interaction.ts). A 'partial' interaction is an interaction object that does not have sufficient information to the intended on-chain action. Multiple partial interactions (through builders) can be coupled to create a complete interaction.

---

### `CurrentUserObject`[​](#currentuserobject "Direct link to currentuserobject")

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `addr` | [Address](#address) | `null` | The public address of the current user |
| `cid` | string | `null` | Allows wallets to specify a [content identifier](https://docs.ipfs.io/concepts/content-addressing/) for user metadata. |
| `expiresAt` | number | `null` | Allows wallets to specify a time-frame for a valid session. |
| `f_type` | string | `'USER'` | A type identifier used internally by FCL. |
| `f_vsn` | string | `'1.0.0'` | FCL protocol version. |
| `loggedIn` | boolean | `null` | If the user is logged in. |
| `services` | `[ServiceObject]` | `[]` | A list of trusted services that express ways of interacting with the current user's identity, including means to further discovery, [authentication, authorization](https://gist.github.com/orodio/a74293f65e83145ec8b968294808cf35#you-know-who-the-user-is), or other kinds of interactions. |

---

### `AuthorizationObject`[​](#authorizationobject "Direct link to authorizationobject")

This type conforms to the interface required for FCL to authorize transaction on behalf o the current user.

| Key | Value Type | Description |
| --- | --- | --- |
| `addr` | [Address](#address) | The address of the authorizer |
| `signingFunction` | function | A function that allows FCL to sign using the authorization details and produce a valid signature. |
| `keyId` | number | The index of the key to use during authorization. (Multiple keys on an account is possible). |
| `sequenceNum` | number | A number that is incremented per transaction using they keyId. |

---

### `SignableObject`[​](#signableobject "Direct link to signableobject")

An object that contains all the information needed for FCL to sign a message with the user's signature.

| Key | Value Type | Description |
| --- | --- | --- |
| `addr` | [Address](#address) | The address of the authorizer |
| `keyId` | number | The index of the key to use during authorization. (Multiple keys on an account is possible). |
| `signature` | function | A [SigningFunction](#signing-function) that can produce a valid signature for a user from a message. |

---

### `AccountObject`[​](#accountobject "Direct link to accountobject")

The JSON representation of an account on the Flow blockchain.

| Key | Value Type | Description |
| --- | --- | --- |
| `address` | [Address](#address) | The address of the account |
| `balance` | number | The FLOW balance of the account in 10^8. |
| `code` | [Code](#code) | The code of any Cadence contracts stored in the account. |
| `contracts` | Object: [Contract](#contract) | An object with keys as the contract name deployed and the value as the the cadence string. |
| `keys` | [[KeyObject]](#keyobject) | Any contracts deployed to this account. |

---

### `Address`[​](#address "Direct link to address")

| Value Type | Description |
| --- | --- |
| string(formatted) | A valid Flow address should be 16 characters in length. A `0x` prefix is optional during inputs. eg. `f8d6e0586b0a20c1` |

---

### `ArgumentObject`[​](#argumentobject "Direct link to argumentobject")

An argument object created by `fcl.arg(value,type)`

| Key | Value Type | Description |
| --- | --- | --- |
| `value` | any | Any value to be used as an argument to a builder. |
| `xform` | [FType](#ftype) | Any of the supported types on Flow. |

---

### `ArgumentFunction`[​](#argumentfunction "Direct link to argumentfunction")

An function that takes the `fcl.arg` function and fcl types `t` and returns an array of `fcl.arg(value,type)`.

`(arg, t) => Array<Arg>`

| Parameter Name | Value Type | Description |
| --- | --- | --- |
| `arg` | function | A function that returns an [ArgumentObject](#argumentobject) - `fcl.arg`. |
| `t` | [FTypes](#ftype) | An object with acccess to all of the supported types on Flow. |

**Returns**

| Value Type | Description |
| --- | --- |
| `[fcl.args]` | Array of `fcl.args`. |

---

### `Authorization Function`[​](#authorization-function "Direct link to authorization-function")

An authorization function must produce the information of the user that is going to sign and a signing function to use the information to produce a signature.

⚠️This function is always async.

📣 By default FCL exposes `fcl.authz` that produces the authorization object for the current user (given they are signed in and only on the browser). Replace this with your own function that conforms to this interface to use it wherever an authorization object is needed.

| Parameter Name | Value Type | Description |
| --- | --- | --- |
| `account` | [AccountObject](#accountobject) | The account of the user that is going to sign. |

**Returns**

| Value Type | Description |
| --- | --- |
| `Promise<[AuthorizationObject](#authorizationobject)>` | The object that contains all the information needed by FCL to authorize a user's transaction. |

#### Usage[​](#usage-34 "Direct link to Usage")

---


 `_19const authorizationFunction = async (account) => {_19 // authorization function need to return an account_19 const { address, keys } = account_19 const tempId = `${address}-${keys[process.env.minterAccountIndex]}`;_19 const keyId = Number(KEY_ID);_19 let signingFunction = async signable => {_19 return {_19 keyId,_19 addr: fcl.withPrefix(address),_19 signature: sign(process.env.FLOW_MINTER_PRIVATE_KEY, signable.message), // signing function, read below_19 }_19 }_19 return {_19 ...account,_19 address,_19 keyId,_19 tempId,_19 signingFunction,_19 }`

* [Detailed explanation](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/wallet-provider-spec/authorization-function.md)

---

### `Signing Function`[​](#signing-function "Direct link to signing-function")

Consumes a payload and produces a signature for a transaction.

⚠️This function is always async.

📣 Only write your own signing function if you are writing your own custom authorization function.

#### Payload[​](#payload "Direct link to Payload")

Note: These values are destructed from the payload object in the first argument.

| Parameter Name | Value Type | Description |
| --- | --- | --- |
| `message` | string | The encoded string which needs to be used to produce the signature. |
| `addr` | string | The encoded string which needs to be used to produce the signature. |
| `keyId` | string | The encoded string which needs to be used to produce the signature. |
| `roles` | string | The encoded string which needs to be used to produce the signature. |
| `voucher` | object | The raw transactions information, can be used to create the message for additional safety and lack of trust in the supplied message. |

**Returns**

| Value Type | Description |
| --- | --- |
| `Promise<[SignableObject](#signableobject)>` | The object that contains all the information needed by FCL to authorize a user's transaction. |

#### Usage[​](#usage-35 "Direct link to Usage")

 `_31import * as fcl from '@onflow/fcl';_31import { ec as EC } from 'elliptic';_31import { SHA3 } from 'sha3';_31const ec: EC = new EC('p256');_31_31const produceSignature = (privateKey, msg) => {_31 const key = ec.keyFromPrivate(Buffer.from(privateKey, 'hex'));_31 const sig = key.sign(this.hashMsg(msg));_31 const n = 32;_31 const r = sig.r.toArrayLike(Buffer, 'be', n);_31 const s = sig.s.toArrayLike(Buffer, 'be', n);_31 return Buffer.concat([r, s]).toString('hex');_31};_31_31const signingFunction = ({_31 message, // The encoded string which needs to be used to produce the signature._31 addr, // The address of the Flow Account this signature is to be produced for._31 keyId, // The keyId of the key which is to be used to produce the signature._31 roles: {_31 proposer, // A Boolean representing if this signature to be produced for a proposer._31 authorizer, // A Boolean representing if this signature to be produced for a authorizer._31 payer, // A Boolean representing if this signature to be produced for a payer._31 },_31 voucher, // The raw transactions information, can be used to create the message for additional safety and lack of trust in the supplied message._31}) => {_31 return {_31 addr, // The address of the Flow Account this signature was produced for._31 keyId, // The keyId for which key was used to produce the signature._31 signature: produceSignature(message), // The hex encoded string representing the signature of the message._31 };_31};`
#### Examples:[​](#examples-5 "Direct link to Examples:")

* [Detailed explanation](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/wallet-provider-spec/authorization-function.md)

---

### `TransactionObject`[​](#transactionobject "Direct link to transactionobject")

| Key | Value Type | Description |
| --- | --- | --- |
| `args` | object | A list of encoded Cadence values passed into this transaction. These have not been decoded by the JS-SDK. |
| `authorizers` | [[Address]](#address) | A list of the accounts that are authorizing this transaction to mutate to their on-chain account state. [See more here](/build/basics/transactions#signer-roles). |
| `envelopeSignatures` | [[SignableObject]](#signableobject) | A list of signatures generated by the payer role. [See more here](/build/basics/transactions#signing-a-transaction). |
| `gasLimit` | number | The maximum number of computational units that can be used to execute this transaction. [See more here](/build/basics/fees). |
| `payer` | [Address](#address) | The account that pays the fee for this transaction. [See more here](/build/basics/transactions#signer-roles). |
| `payloadSignatures` | [[SignableObject]](#signableobject) | A list of signatures generated by the proposer and authorizer roles. [See more here](/build/basics/transactions#signing-a-transaction). |
| `proposalKey` | [[ProposalKey]](#proposalkeyobject) | The account key used to propose this transaction |
| `referenceBlockId` | string | A reference to the block used to calculate the expiry of this transaction. |
| `script` | string | The UTF-8 encoded Cadence source code that defines the execution logic for this transaction |

### `TransactionRolesObject`[​](#transactionrolesobject "Direct link to transactionrolesobject")

| Key Name | Value Type | Description |
| --- | --- | --- |
| proposer | boolean | A Boolean representing if this signature to be produced for a proposer. |
| authorizer | boolean | A Boolean representing if this signature to be produced for an authorizer. |
| payer | boolean | A Boolean representing if this signature to be produced for a payer. |

For more on what each transaction role means, see [singing roles](/build/basics/transactions#signer-roles).

### `TransactionStatusObject`[​](#transactionstatusobject "Direct link to transactionstatusobject")

| Key | Value Type | Description |
| --- | --- | --- |
| `blockId` | string | ID of the block that contains the transaction. |
| `events` | [[EventObject]](#event-object) | An array of events that were emitted during the transaction. |
| `status` | [TransactionStatus](#transaction-statuses) | The status of the transaction on the blockchain. |
| `statusString` | [TransactionStatus](#transaction-statuses) | The `status` as as descriptive text (e.g. "FINALIZED"). |
| `errorMessage` | string | An error message if it exists. Default is an empty string `''`. |
| `statusCode` | number | The pass/fail status. 0 indicates the transaction succeeded, 1 indicates it failed. |

### `EventName`[​](#eventname "Direct link to eventname")

| Value Type | Description |
| --- | --- |
| string(formatted) | A event name in Flow must follow the format `A.{AccountAddress}.{ContractName}.{EventName}` eg. `A.ba1132bc08f82fe2.Debug.Log` |

### `Contract`[​](#contract "Direct link to contract")

| Value Type | Description |
| --- | --- |
| string(formatted) | A formatted string that is a valid cadence contract. |

### `KeyObject`[​](#keyobject "Direct link to keyobject")

This is the JSON representation of a key on the Flow blockchain.

| Key | Value Type | Description |
| --- | --- | --- |
| `index` | number | The address of the account |
| `publicKey` | string | The public portion of a public/private key pair |
| `signAlgo` | number | An index referring to one of `ECDSA_P256` or `ECDSA_secp256k1` |
| `hashAlgo` | number | An index referring to one of `SHA2_256` or `SHA3_256` |
| `weight` | number | A number between 1 and 1000 indicating the relative weight to other keys on the account. |
| `sequenceNumber` | number | This number is incremented for every transaction signed using this key. |
| `revoked` | boolean | If this key has been disabled for use. |

### `ProposalKeyObject`[​](#proposalkeyobject "Direct link to proposalkeyobject")

ProposalKey is the account key used to propose this transaction.

A proposal key references a specific key on an account, along with an up-to-date sequence number for that key. This sequence number is used to prevent replay attacks.

You can find more information about sequence numbers [here](/build/basics/transactions#sequence-numbers)

| Key | Value Type | Description |
| --- | --- | --- |
| `address` | [Address](#address) | The address of the account |
| `keyIndex` | number | The index of the account key being referenced |
| `sequenceNumber` | number | The sequence number associated with this account key for this transaction |

### `BlockObject`[​](#blockobject "Direct link to blockobject")

The JSON representation of a key on the Flow blockchain.

| Key | Value Type | Description |
| --- | --- | --- |
| `id` | string | The id of the block. |
| `parentId` | string | The id of the parent block. |
| `height` | number | The height of the block. |
| `timestamp` | object | Contains time related fields. |
| `collectionGuarantees` | [[CollectionGuaranteeObject](#collectionguaranteeobject)] | Contains the ids of collections included in the block. |
| `blockSeals` | [SealedBlockObject] | The details of which nodes executed and sealed the blocks. |
| `signatures` | Uint8Array([numbers]) | All signatures. |

### `BlockHeaderObject`[​](#blockheaderobject "Direct link to blockheaderobject")

The subset of the [BlockObject](#blockobject) containing only the header values of a block.

| Key | Value Type | Description |
| --- | --- | --- |
| `id` | string | The id of the block. |
| `parentId` | string | The id of the parent block. |
| `height` | number | The height of the block. |
| `timestamp` | object | Contains time related fields. |

### `CollectionGuaranteeObject`[​](#collectionguaranteeobject "Direct link to collectionguaranteeobject")

A collection that has been included in a block.

| Key | Value Type | Description |
| --- | --- | --- |
| `collectionId` | string | The id of the block. |
| `signatures` | [SignatureObject](#SignatureObject) | All signatures. |

### `CollectionObject`[​](#collectionobject "Direct link to collectionobject")

A collection is a list of transactions that are contained in the same block.

| Key | Value Type | Description |
| --- | --- | --- |
| `id` | string | The id of the collection. |
| `transactionIds` | [string] | The ids of the transactions included in the collection. |

### `ResponseObject`[​](#responseobject "Direct link to responseobject")

The format of all responses in FCL returned from `fcl.send(...)`. For full details on the values and descriptions of the keys, view [here](https://github.com/onflow/fcl-js/tree/master/packages/sdk/src/response).

| Key |
| --- |
| `tag` |
| `transaction` |
| `transactionStatus` |
| `transactionId` |
| `encodedData` |
| `events` |
| `account` |
| `block` |
| `blockHeader` |
| `latestBlock` |
| `collection` |

### `Event Object`[​](#event-object "Direct link to event-object")

| Key | Value Type | Description |
| --- | --- | --- |
| `blockId` | string | ID of the block that contains the event. |
| `blockHeight` | number | Height of the block that contains the event. |
| `blockTimestamp` | string | The timestamp of when the block was sealed in a `DateString` format. eg. `'2021-06-25T13:42:04.227Z'` |
| `type` | [EventName](#eventname) | A string containing the event name. |
| `transactionId` | string | Can be used to query transaction information, eg. via a Flow block explorer. |
| `transactionIndex` | number | Used to prevent replay attacks. |
| `eventIndex` | number | Used to prevent replay attacks. |
| `data` | any | The data emitted from the event. |

### `Transaction Statuses`[​](#transaction-statuses "Direct link to transaction-statuses")

The status of a transaction will depend on the Flow blockchain network and which phase it is in as it completes and is finalized.

| Status Code | Description |
| --- | --- |
| `0` | Unknown |
| `1` | Transaction Pending - Awaiting Finalization |
| `2` | Transaction Finalized - Awaiting Execution |
| `3` | Transaction Executed - Awaiting Sealing |
| `4` | Transaction Sealed - Transaction Complete. At this point the transaction result has been committed to the blockchain. |
| `5` | Transaction Expired |

### `GRPC Statuses`[​](#grpc-statuses "Direct link to grpc-statuses")

The access node GRPC implementation follows the standard GRPC Core status code spec. View [here](https://grpc.github.io/grpc/core/md_doc_statuscodes.html).

### `FType`[​](#ftype "Direct link to ftype")

FCL arguments must specify one of the following support types for each value passed in.

| Type | Example |
| --- | --- |
| `UInt` | `fcl.arg(1, t.UInt)` |
| `UInt8` | `fcl.arg(8, t.UInt8)` |
| `UInt16` | `fcl.arg(16, t.UInt16)` |
| `UInt32` | `fcl.arg(32, t.UInt32)` |
| `UInt64` | `fcl.arg(64, t.UInt64)` |
| `UInt128` | `fcl.arg(128, t.UInt128)` |
| `UInt256` | `fcl.arg(256, t.UInt256)` |
| `Int` | `fcl.arg(1, t.Int)` |
| `Int8` | `fcl.arg(8, t.Int8)` |
| `Int16` | `fcl.arg(16, t.Int16)` |
| `Int32` | `fcl.arg(32, t.Int32)` |
| `Int64` | `fcl.arg(64, t.Int64)` |
| `Int128` | `fcl.arg(128, t.Int128)` |
| `Int256` | `fcl.arg(256, t.Int256)` |
| `Word8` | `fcl.arg(8, t.Word8)` |
| `Word16` | `fcl.arg(16, t.Word16)` |
| `Word32` | `fcl.arg(32, t.Word32)` |
| `Word64` | `fcl.arg(64, t.Word64)` |
| `UFix64` | `fcl.arg("64.123", t.UFix64)` |
| `Fix64` | `fcl.arg("64.123", t.Fix64)` |
| `String` | `fcl.arg("Flow", t.String)` |
| `Character` | `fcl.arg("c", t.String)` |
| `Bool` | `fcl.arg(true, t.String)` |
| `Address` | `fcl.arg("0xABC123DEF456", t.Address)` |
| `Optional` | `fcl.arg("Flow", t.Optional(t.String))` |
| `Array` | `fcl.args([ fcl.arg(["First", "Second"], t.Array(t.String)) ])` |
| `Dictionary` | `fcl.args([fcl.arg([{key: 1, value: "one"}, {key: 2, value: "two"}], t.Dictionary({key: t.Int, value: t.String}))])` |
| `Path` | `fcl.arg({ domain: "public", identifier: "flowTokenVault" }, t.Path)` |

---

### `StreamConnection`[​](#streamconnection "Direct link to streamconnection")

A stream connection is an object for subscribing to generic data from any WebSocket data stream. This is the base type for all stream connections. Two channels, `close` and `error`, are always available, as they are used to signal the end of the stream and any errors that occur.

 `_20interface StreamConnection<ChannelMap extends { [name: string]: any }> {_20 // Subscribe to a channel_20 on<C extends keyof ChannelMap>(_20 channel: C,_20 listener: (data: ChannelMap[C]) => void,_20 ): this;_20 on(event: 'close', listener: () => void): this;_20 on(event: 'error', listener: (err: any) => void): this;_20_20 // Unsubscribe from a channel_20 off<C extends keyof ChannelMap>(_20 event: C,_20 listener: (data: ChannelMap[C]) => void,_20 ): this;_20 off(event: 'close', listener: () => void): this;_20 off(event: 'error', listener: (err: any) => void): this;_20_20 // Close the connection_20 close(): void;_20}`
#### Usage[​](#usage-36 "Direct link to Usage")

 `_13import { StreamConnection } from "@onflow/typedefs"_13_13const stream: StreamConnection = ..._13_13stream.on("close", () => {_13 // Handle close_13})_13_13stream.on("error", (err) => {_13 // Handle error_13})_13_13stream.close()`
### `EventStream`[​](#eventstream "Direct link to eventstream")

An event stream is a stream connection that emits events and block heartbeats. Based on the connection parameters, heartbeats will be emitted at least as often as some fixed block height interval. It is a specific variant of a [StreamConnection](#streamconnection).

 `_10type EventStream = StreamConnection<{_10 events: Event[];_10 heartbeat: BlockHeartbeat;_10}>;`
#### Usage[​](#usage-37 "Direct link to Usage")

 `_14import { EventStream } from "@onflow/typedefs"_14_14const stream: EventStream = ..._14_14stream.on("events", (events) => {_14 // Handle events_14})_14_14stream.on("heartbeat", (heartbeat) => {_14 // Handle heartbeat_14})_14_14// Close the stream_14stream.close()`
### `BlockHeartbeat`[​](#blockheartbeat "Direct link to blockheartbeat")

 `_10export interface BlockHeartbeat {_10 blockId: string;_10 blockHeight: number;_10 timestamp: string;_10}`
#### Usage[​](#usage-38 "Direct link to Usage")

 `_10import { BlockHeartbeat } from "@onflow/typedefs"_10_10const heartbeat: BlockHeartbeat = ...`
### SignatureObject[​](#signatureobject "Direct link to SignatureObject")

Signature objects are used to represent a signature for a particular message as well as the account and keyId which signed for this message.

| Key | Value Type | Description |
| --- | --- | --- |
| `addr` | [Address](#address) | the address of the account which this signature has been generated for |
| `keyId` | number | The index of the key to use during authorization. (Multiple keys on an account is possible). |
| `signature` | string | a hexidecimal-encoded string representation of the generated signature |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/api.md)Last updated on **Feb 11, 2025** by **Chase Fleming**[PreviousFlow Client Library (FCL)](/tools/clients/fcl-js)[NextSDK Reference](/tools/clients/fcl-js/sdk-guidelines)
###### Rate this page

😞😐😊

* [Configuration](#configuration)
  + [Setting Configuration Values](#setting-configuration-values)
  + [Getting Configuration Values](#getting-configuration-values)
  + [Common Configuration Keys](#common-configuration-keys)
* [Using Contracts in Scripts and Transactions](#using-contracts-in-scripts-and-transactions)
  + [Address Replacement](#address-replacement)
  + [Using `flow.json` for Contract Imports](#using-flowjson-for-contract-imports)
  + [Setting Up](#setting-up)
* [Wallet Interactions](#wallet-interactions)
  + [`authenticate`](#authenticate)
  + [`unauthenticate`](#unauthenticate)
  + [`reauthenticate`](#reauthenticate)
  + [`signUp`](#signup)
  + [`logIn`](#login)
  + [`authz`](#authz)
* [Current User](#current-user)
  + [`currentUser.subscribe`](#currentusersubscribe)
  + [`currentUser.snapshot`](#currentusersnapshot)
  + [`currentUser.authenticate`](#currentuserauthenticate)
  + [`currentUser.unauthenticate`](#currentuserunauthenticate)
  + [`currentUser.authorization`](#currentuserauthorization)
  + [`currentUser.signUserMessage`](#currentusersignusermessage)
* [Discovery](#discovery)
  + [`discovery`](#discovery-1)
  + [Suggested Configuration](#suggested-configuration)
  + [authn](#authn)
  + [`discovery.authn.snapshot()`](#discoveryauthnsnapshot)
  + [`discovery.authn.subscribe(callback)`](#discoveryauthnsubscribecallback)
* [On-chain Interactions](#on-chain-interactions)
  + [Query and Mutate Flow with Cadence](#query-and-mutate-flow-with-cadence)
  + [`query`](#query)
  + [`mutate`](#mutate)
  + [`verifyUserSignatures` (Deprecated)](#verifyusersignatures-deprecated)
* [AppUtils](#apputils)
  + [`AppUtils.verifyUserSignatures`](#apputilsverifyusersignatures)
  + [`AppUtils.verifyAccountProof`](#apputilsverifyaccountproof)
  + [Query and mutate the blockchain with Builders](#query-and-mutate-the-blockchain-with-builders)
  + [`send`](#send)
  + [`decode`](#decode)
* [Builders](#builders)
  + [Query Builders](#query-builders)
  + [`getAccount`](#getaccount)
  + [`getBlock`](#getblock)
  + [`atBlockHeight`](#atblockheight)
  + [`atBlockId`](#atblockid)
  + [`getBlockHeader`](#getblockheader)
  + [`getEventsAtBlockHeightRange`](#geteventsatblockheightrange)
  + [`getEventsAtBlockIds`](#geteventsatblockids)
  + [`getCollection`](#getcollection)
  + [`getTransactionStatus`](#gettransactionstatus)
  + [`getTransaction`](#gettransaction)
  + [`subscribeEvents`](#subscribeevents)
  + [`getEvents` (Deprecated)](#getevents-deprecated)
  + [`getLatestBlock` (Deprecated)](#getlatestblock-deprecated)
  + [`getBlockById` (Deprecated)](#getblockbyid-deprecated)
  + [`getBlockByHeight` (Deprecated)](#getblockbyheight-deprecated)
  + [Utility Builders](#utility-builders)
  + [`arg`](#arg)
  + [`args`](#args)
  + [Template Builders](#template-builders)
  + [`script`](#script)
  + [`transaction`](#transaction)
* [Pre-built Interactions](#pre-built-interactions)
  + [`account`](#account)
  + [`block`](#block)
  + [`latestBlock` (Deprecated)](#latestblock-deprecated)
* [Transaction Status Utility](#transaction-status-utility)
  + [`tx`](#tx)
* [Event Polling Utility](#event-polling-utility)
  + [`events`](#events)
* [Types, Interfaces, and Definitions](#types-interfaces-and-definitions)
  + [`Builders`](#builders-1)
  + [`Interaction`](#interaction)
  + [`CurrentUserObject`](#currentuserobject)
  + [`AuthorizationObject`](#authorizationobject)
  + [`SignableObject`](#signableobject)
  + [`AccountObject`](#accountobject)
  + [`Address`](#address)
  + [`ArgumentObject`](#argumentobject)
  + [`ArgumentFunction`](#argumentfunction)
  + [`Authorization Function`](#authorization-function)
  + [`Signing Function`](#signing-function)
  + [`TransactionObject`](#transactionobject)
  + [`TransactionRolesObject`](#transactionrolesobject)
  + [`TransactionStatusObject`](#transactionstatusobject)
  + [`EventName`](#eventname)
  + [`Contract`](#contract)
  + [`KeyObject`](#keyobject)
  + [`ProposalKeyObject`](#proposalkeyobject)
  + [`BlockObject`](#blockobject)
  + [`BlockHeaderObject`](#blockheaderobject)
  + [`CollectionGuaranteeObject`](#collectionguaranteeobject)
  + [`CollectionObject`](#collectionobject)
  + [`ResponseObject`](#responseobject)
  + [`Event Object`](#event-object)
  + [`Transaction Statuses`](#transaction-statuses)
  + [`GRPC Statuses`](#grpc-statuses)
  + [`FType`](#ftype)
  + [`StreamConnection`](#streamconnection)
  + [`EventStream`](#eventstream)
  + [`BlockHeartbeat`](#blockheartbeat)
  + [SignatureObject](#signatureobject)
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

