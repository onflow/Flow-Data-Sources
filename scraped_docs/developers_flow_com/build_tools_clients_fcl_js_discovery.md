# Source: https://developers.flow.com/build/tools/clients/fcl-js/discovery

Wallet Discovery | Flow Developer Portal



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

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                          * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                                * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* Wallet Discovery

On this page

# Wallet Discovery

## Wallet Discovery[​](#wallet-discovery "Direct link to Wallet Discovery")

It's a challenge to know all the wallets available to users on a blockchain. Flow Client Library's (FCL) Discovery mechanism relieves much of the burden of Flow compatible wallet integration and lets developers focus on building their dApp and providing as many options as possible to their users.

There are two ways an app can use Discovery:

1. The **UI version** which can be configured for display via iFrame, Popup, or Tab.
2. The **API version** which allows you to access authentication services directly in your code via `fcl.discovery.authn` method which we'll describe below.

## UI version[​](#ui-version "Direct link to UI version")

When a user authenticates via FCL with Discovery UI, they receive a list of services they can use to login.

![FCL Default Discovery UI](/assets/images/discovery-c2c95d28a66e86c570491a36e37e0afa.png)

This method is the simplest way to integrate Discovery and its wallets and services into your app. All you have to do is configure `discovery.wallet` with the host endpoint for testnet or mainnet.

info

Opt-in wallets, like Ledger and Dapper Wallet, require you to explicitly state you'd like to use them. For more information on how to include opt-in wallets, [see these docs](/build/tools/clients/fcl-js/packages-docs/fcl#configuration).

A [Dapper Wallet](https://meetdapper.com/developers) developer account is required. To turn on Dapper Wallet inside FCL, you need to [follow this guide](https://docs.meetdapper.com/quickstart).

`_10

import { config } from '@onflow/fcl';

_10

_10

config({

_10

'accessNode.api': 'https://rest-testnet.onflow.org',

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn',

_10

});`

Any time you call `fcl.authenticate` the user will be presented with that screen.

To change the default view from iFrame to popup or tab set `discovery.wallet.method` to `POP/RPC` (opens as a popup) or `TAB/RPC` (opens in a new tab). For more info about service methods, see [here](https://github.com/onflow/fcl-js/blob/9bce741d3b32fde18b07084b62ea15f9bbdb85bc/packages/fcl/src/wallet-provider-spec/draft-v3.md).

### Branding Discovery UI[​](#branding-discovery-ui "Direct link to Branding Discovery UI")

As of version 0.0.79-alpha.4, dApps can now display an app title and app icon in the Discovery UI when you a few values in their FCL app config. This branding provides users with messaging that has clear intent before they authenticate to add a layer of trust.

All you have to do is set `app.detail.icon` and `app.detail.title` like this:

`_10

import { config } from '@onflow/fcl';

_10

_10

config({

_10

'app.detail.icon': 'https://placekitten.com/g/200/200',

_10

'app.detail.title': 'Kitten Dapp',

_10

});`

info

If these configuration options aren't set, dApps that use the Discovery API will still display a default icon and "Unknown App" as the title when they attempt to authorize a user who is not logged in. We highly recommended that you set these values accurately before you go live.

## API version[​](#api-version "Direct link to API version")

If you want more control over your authentication UI, the Discovery API is also simple to use as it exposes Discovery directly in your code via `fcl`.

Setup still requires configuration of the Discovery endpoint, but when you use the API, it is set via `discovery.authn.endpoint` as shown below.

`_10

import { config } from '@onflow/fcl';

_10

_10

config({

_10

'accessNode.api': 'https://rest-testnet.onflow.org',

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn',

_10

});`

You can access services in your Dapp from `fcl.discovery`:

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.discovery.authn.subscribe(callback);

_10

_10

// OR

_10

_10

fcl.discovery.authn.snapshot();`

To authenticate with a service (for example, when a user click's "login"), pass the selected service to the `fcl.authenticate` method described in [the API reference](/build/tools/clients/fcl-js/packages-docs/fcl/authenticate):

`_10

fcl.authenticate({ service });`

A simple React component may end up looking like this:

`_24

import './config';

_24

import { useState, useEffect } from 'react';

_24

import * as fcl from '@onflow/fcl';

_24

_24

function Component() {

_24

const [services, setServices] = useState([]);

_24

useEffect(

_24

() => fcl.discovery.authn.subscribe((res) => setServices(res.results)),

_24

[],

_24

);

_24

_24

return (

_24

<div>

_24

{services.map((service) => (

_24

<button

_24

key={service.provider.address}

_24

onClick={() => fcl.authenticate({ service })}

_24

>

_24

Login with {service.provider.name}

_24

</button>

_24

))}

_24

</div>

_24

);

_24

}`

Helpful fields for your UI can be found in the `provider` object inside of the service. Fields include the following:

`_13

{

_13

...,

_13

"provider": {

_13

"address": "0xf086a545ce3c552d",

_13

"name": "Blocto",

_13

"icon": "/images/blocto.png",

_13

"description": "Your entrance to the blockchain world.",

_13

"color": "#afd8f7",

_13

"supportEmail": "support@blocto.app",

_13

"authn_endpoint": "https://flow-wallet-testnet.blocto.app/authn",

_13

"website": "https://blocto.portto.io"

_13

}

_13

}`

## Network configuration[​](#network-configuration "Direct link to Network configuration")

### Discovery UI URLs[​](#discovery-ui-urls "Direct link to Discovery UI URLs")

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Environment Example|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Mainnet `https://fcl-discovery.onflow.org/authn`| Testnet `https://fcl-discovery.onflow.org/testnet/authn`| Local `https://fcl-discovery.onflow.org/local/authn` | | | | | | | |

### Discovery API endpoints[​](#discovery-api-endpoints "Direct link to Discovery API endpoints")

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Environment Example|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Mainnet `https://fcl-discovery.onflow.org/api/authn`| Testnet `https://fcl-discovery.onflow.org/api/testnet/authn`| Local `https://fcl-discovery.onflow.org/api/local/authn` | | | | | | | |

info

Local will return [Dev Wallet](https://github.com/onflow/fcl-dev-wallet) on emulator for local development with the default port of 8701. If you'd like to override the default port, add `?port=0000` and set the port to whatever you'd like to override it to.

## Other configuration[​](#other-configuration "Direct link to Other configuration")

info

Configuration works across both UI and API versions of Discovery.

### Include opt-in wallets[​](#include-opt-in-wallets "Direct link to Include opt-in wallets")

**Start in FCL v0.0.78-alpha.10**

Opt-in wallets are those that don't have support for authentication, authorization, and user signature services. Or, support only a limited set of transactions.

You can include opt-in wallets with either **wallet UIDs** (recommended) or service account addresses:

**Use wallet UIDs (recommended):**

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.config({

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn',

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn',

_10

'discovery.authn.include': ['dapper-wallet', 'ledger'], // Wallet UIDs

_10

});`

**Use service Aacount addresses:**

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.config({

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn',

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn',

_10

'discovery.authn.include': ['0x82ec283f88a62e65', '0x9d2e44203cb13051'], // Testnet addresses

_10

});`

**Opt-In Wallet Identifiers**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wallet Wallet UID Mainnet Address Testnet Address|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Dapper Wallet `dapper-wallet` 0xead892083b3e2c6c 0x82ec283f88a62e65|  |  |  |  | | --- | --- | --- | --- | | Ledger `ledger` 0xe5cd26afebe62781 0x9d2e44203cb13051 | | | | | | | | | | | |

To learn more about other possible configurations, check out the [Discovery Github Repo](https://github.com/onflow/fcl-discovery).

### Exclude wallets[​](#exclude-wallets "Direct link to Exclude wallets")

To exclude wallets from FCL Discovery, you can use the `discovery.authn.exclude` configuration option. You can specify wallets with either **wallet UIDs** (recommended) or service account addresses:

**Use wallet UIDs (recommended):**

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.config({

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn',

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn',

_10

'discovery.authn.exclude': ['nufi'], // Wallet UIDs to exclude

_10

});`

**Use service account addresses:**

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.config({

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn',

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn',

_10

'discovery.authn.exclude': ['0x123', '0x456'], // Service account addresses to exclude

_10

});`

**Available wallet UIDs**

You can use any of the following wallet identifiers with `discovery.authn.include` or `discovery.authn.exclude`:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wallet UID Mainnet Address Testnet Address Type|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Flow Wallet `flow-wallet` 0x33f75ff0b830dcec 0x33f75ff0b830dcec Default|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | NuFi `nufi` 0x95b85a9ef4daabb1 - Default|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Blocto `blocto` 0x55ad22f01ef568a1 0x55ad22f01ef568a1 Default|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Dapper Wallet `dapper-wallet` 0xead892083b3e2c6c 0x82ec283f88a62e65 Opt-in|  |  |  |  |  | | --- | --- | --- | --- | --- | | Ledger `ledger` 0xe5cd26afebe62781 0x9d2e44203cb13051 Opt-in | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

info

Default wallets appear in Discovery by default. Opt-in wallets must be explicitly included with `discovery.authn.include`. You can use either the wallet UID or the service account address to filter.

For the most up-to-date list of available wallets, see the [fcl-discovery wallet data](https://github.com/onflow/fcl-discovery/tree/master/data/wallets) in the official repository.

### WalletConnect configuration[​](#walletconnect-configuration "Direct link to WalletConnect configuration")

To configure WalletConnect, add a WalletConnect project ID to the FCL config:

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.config({

_10

'walletconnect.projectId': 'YOUR_WALLETCONNECT_PROJECT_ID',

_10

});`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/discovery.md)

Last updated on **Dec 9, 2025** by **cshannon1218**

[Previous

FCL Wagmi Adapter](/build/tools/clients/fcl-js/cross-vm/wagmi-adapter)[Next

Installation](/build/tools/clients/fcl-js/installation)

###### Rate this page

😞😐😊

Copy as Markdown

* [Wallet Discovery](#wallet-discovery)* [UI version](#ui-version)
    + [Branding Discovery UI](#branding-discovery-ui)* [API version](#api-version)* [Network configuration](#network-configuration)
        + [Discovery UI URLs](#discovery-ui-urls)+ [Discovery API endpoints](#discovery-api-endpoints)* [Other configuration](#other-configuration)
          + [Include opt-in wallets](#include-opt-in-wallets)+ [Exclude wallets](#exclude-wallets)+ [WalletConnect configuration](#walletconnect-configuration)

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