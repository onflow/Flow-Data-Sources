# Source: https://developers.flow.com/tools/clients/fcl-js/discovery




Wallet Discovery | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* Wallet Discovery
On this page
# Wallet Discovery

## Wallet Discovery[​](#wallet-discovery "Direct link to Wallet Discovery")

Knowing all the wallets available to users on a blockchain can be challenging. FCL's Discovery mechanism relieves much of the burden of integrating with Flow compatible wallets and let's developers focus on building their dapp and providing as many options as possible to their users.

There are two ways an app can use Discovery:

1. The **UI version** which can be configured for display via iFrame, Popup, or Tab.
2. The **API version** which allows you to access authentication services directly in your code via `fcl.discovery.authn` method which we'll describe below.

## UI Version[​](#ui-version "Direct link to UI Version")

When authenticating via FCL using Discovery UI, a user is shown a list of services they can use to login.

![FCL Default Discovery UI](/assets/images/discovery-c2c95d28a66e86c570491a36e37e0afa.png)

This method is the simplest way to integrate Discovery and its wallets and services into your app. All you have to do is configure `discovery.wallet` with the host endpoint for testnet or mainnet.

> **Note**: Opt-in wallets, like Ledger and Dapper Wallet, require you to explicitly state you'd like to use them. For more information on including opt-in wallets, [see these docs](/tools/clients/fcl-js/api#more-configuration).
> 
> A [Dapper Wallet](https://meetdapper.com/developers) developer account is required. To enable Dapper Wallet inside FCL, you need to [follow this guide](https://docs.meetdapper.com/quickstart).

 `_10import { config } from '@onflow/fcl';_10_10config({_10 'accessNode.api': 'https://rest-testnet.onflow.org',_10 'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn',_10});`

Any time you call `fcl.authenticate` the user will be presented with that screen.

To change the default view from iFrame to popup or tab set `discovery.wallet.method` to `POP/RPC` (opens as a popup) or `TAB/RPC` (opens in a new tab). More info about service methods can be [found here](https://github.com/onflow/fcl-js/blob/9bce741d3b32fde18b07084b62ea15f9bbdb85bc/packages/fcl/src/wallet-provider-spec/draft-v3.md).

### Branding Discovery UI[​](#branding-discovery-ui "Direct link to Branding Discovery UI")

Starting in version 0.0.79-alpha.4, dapps now have the ability to display app a title and app icon in the Discovery UI by setting a few values in their FCL app config. This branding provides users with messaging that has clear intent before authenticating to add a layer of trust.

All you have to do is set `app.detail.icon` and `app.detail.title` like this:

 `_10import { config } from '@onflow/fcl';_10_10config({_10 'app.detail.icon': 'https://placekitten.com/g/200/200',_10 'app.detail.title': 'Kitten Dapp',_10});`

**Note:** If these configuration options aren't set, Dapps using the Discovery API will still display a default icon and "Unknown App" as the title when attempting to authorize a user who is not logged in. It is highly recommended to set these values accurately before going live.

## API Version[​](#api-version "Direct link to API Version")

If you want more control over your authentication UI, the Discovery API is also simple to use as it exposes Discovery directly in your code via `fcl`.

Setup still requires configuration of the Discovery endpoint, but when using the API it is set via `discovery.authn.endpoint` as shown below.

 `_10import { config } from '@onflow/fcl';_10_10config({_10 'accessNode.api': 'https://rest-testnet.onflow.org',_10 'discovery.authn.endpoint':_10 'https://fcl-discovery.onflow.org/api/testnet/authn',_10});`

You can access services in your Dapp from `fcl.discovery`:

 `_10import * as fcl from '@onflow/fcl';_10_10fcl.discovery.authn.subscribe(callback);_10_10// OR_10_10fcl.discovery.authn.snapshot();`

In order to authenticate with a service (for example, when a user click's "login"), pass the selected service to the `fcl.authenticate` method described here [in the API reference](/tools/clients/fcl-js/api#authenticate):

 `_10fcl.authenticate({ service });`

A simple React component may end up looking like this:

 `_24import './config';_24import { useState, useEffect } from 'react';_24import * as fcl from '@onflow/fcl';_24_24function Component() {_24 const [services, setServices] = useState([]);_24 useEffect(_24 () => fcl.discovery.authn.subscribe((res) => setServices(res.results)),_24 [],_24 );_24_24 return (_24 <div>_24 {services.map((service) => (_24 <button_24 key={service.provider.address}_24 onClick={() => fcl.authenticate({ service })}_24 >_24 Login with {service.provider.name}_24 </button>_24 ))}_24 </div>_24 );_24}`

Helpful fields for your UI can be found in the `provider` object inside of the service. Fields include the following:

 `_13{_13 ...,_13 "provider": {_13 "address": "0xf086a545ce3c552d",_13 "name": "Blocto",_13 "icon": "/images/blocto.png",_13 "description": "Your entrance to the blockchain world.",_13 "color": "#afd8f7",_13 "supportEmail": "support@blocto.app",_13 "authn_endpoint": "https://flow-wallet-testnet.blocto.app/authn",_13 "website": "https://blocto.portto.io"_13 }_13}`
## Network Configuration[​](#network-configuration "Direct link to Network Configuration")

### Discovery UI URLs[​](#discovery-ui-urls "Direct link to Discovery UI URLs")

| Environment | Example |
| --- | --- |
| Mainnet | `https://fcl-discovery.onflow.org/authn` |
| Testnet | `https://fcl-discovery.onflow.org/testnet/authn` |
| Local | `https://fcl-discovery.onflow.org/local/authn` |

### Discovery API Endpoints[​](#discovery-api-endpoints "Direct link to Discovery API Endpoints")

| Environment | Example |
| --- | --- |
| Mainnet | `https://fcl-discovery.onflow.org/api/authn` |
| Testnet | `https://fcl-discovery.onflow.org/api/testnet/authn` |
| Local | `https://fcl-discovery.onflow.org/api/local/authn` |

> Note: Local will return [Dev Wallet](https://github.com/onflow/fcl-dev-wallet) on emulator for developing locally with the default port of 8701. If you'd like to override the default port add ?port=0000 with the port being whatever you'd like to override it to.

## Other Configuration[​](#other-configuration "Direct link to Other Configuration")

> Note: Configuration works across both UI and API versions of Discovery.

### Include Opt-In Wallets[​](#include-opt-in-wallets "Direct link to Include Opt-In Wallets")

**Starting in FCL v0.0.78-alpha.10**

Opt-in wallets are those that don't have support for authentication, authorization, and user signature services. Or, support only a limited set of transactions.

To include opt-in wallets from FCL:

 `_10import * as fcl from "@onflow/fcl"_10_10fcl.config({_10 "discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn",_10 "discovery.authn.endpoint": "https://fcl-discovery.onflow.org/api/testnet/authn",_10 "discovery.authn.include": ["0x123"] // Service account address_10})`

**Opt-In Wallet Addresses on Testnet and Mainnet**

| Service | Testnet | Mainnet |
| --- | --- | --- |
| `Dapper Wallet` | 0x82ec283f88a62e65 | 0xead892083b3e2c6c |
| `Ledger` | 0x9d2e44203cb13051 | 0xe5cd26afebe62781 |

To learn more about other possible configurations, check out the following links:

* [Discovery API Docs](/tools/clients/fcl-js/api#discovery-1)
* [Discovery Github Repo](https://github.com/onflow/fcl-discovery)
[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/discovery.md)Last updated on **Jan 22, 2025** by **Chase Fleming**[PreviousHow to Configure FCL](/tools/clients/fcl-js/configure-fcl)[NextInstallation](/tools/clients/fcl-js/installation)
###### Rate this page

😞😐😊

* [Wallet Discovery](#wallet-discovery)
* [UI Version](#ui-version)
  + [Branding Discovery UI](#branding-discovery-ui)
* [API Version](#api-version)
* [Network Configuration](#network-configuration)
  + [Discovery UI URLs](#discovery-ui-urls)
  + [Discovery API Endpoints](#discovery-api-endpoints)
* [Other Configuration](#other-configuration)
  + [Include Opt-In Wallets](#include-opt-in-wallets)
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

