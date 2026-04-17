# Source: https://developers.flow.com/tools/flow-dev-wallet

Flow Dev Wallet | Flow Developer Portal



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

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* Flow Dev Wallet

On this page

# Flow Dev Wallet

The Flow Dev Wallet is a mock Flow wallet that simulates the protocols the Flow Client Library ([FCL](/build/tools/clients/fcl-js)) uses to interact with the Flow blockchain on behalf of simulated user accounts.

warning

This project implements an FCL compatible interface, but should **not** be used as a reference to build a production grade wallet.

This project should only be used in aid of local development against a locally run instance of the Flow blockchain like the Flow emulator, and should never be used in conjunction with Flow Mainnet, Testnet, or any other instances of Flow.

info

To see a full list of Flow compatible wallets, visit the [Wallets page](/ecosystem/wallets)

## Get started[​](#get-started "Direct link to Get started")

Before you use the dev wallet, you'll need to start the Flow emulator.

### Install the `flow-cli`[​](#install-the-flow-cli "Direct link to install-the-flow-cli")

The Flow emulator is bundled with the Flow CLI. Instructions for how to install the CLI can be found here: [flow-cli/install/](/build/tools/flow-cli/install)

### Create a `flow.json` file[​](#create-a-flowjson-file "Direct link to create-a-flowjson-file")

Run this command to create `flow.json` file (typically in your project's root directory):

`_10

flow init --config-only`

### Start the Emulator[​](#start-the-emulator "Direct link to Start the Emulator")

To start the Emulator and deploy the contracts, run the following command from the directory that contains `flow.json` in your project:

`_10

flow emulator start

_10

flow project deploy --network emulator`

### Start the dev wallet[​](#start-the-dev-wallet "Direct link to Start the dev wallet")

In a separate terminal session, start the dev wallet service.

`_10

flow dev-wallet`

### Configure your JavaScript application[​](#configure-your-javascript-application "Direct link to Configure your JavaScript application")

The Flow Dev Wallet is designed to be used with [`@onflow/fcl`](https://github.com/onflow/fcl-js) version `1.0.0` or higher. The FCL package can be installed with: `npm install @onflow/fcl` or `yarn add @onflow/fcl`.

To use the dev wallet, configure FCL to point to the address of a locally running [Flow emulator](#start-the-emulator) and the dev wallet endpoint.

`_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl

_10

.config()

_10

// Point App at Emulator REST API

_10

.put('accessNode.api', 'http://localhost:8888')

_10

// Point FCL at dev-wallet (default port)

_10

.put('discovery.wallet', 'http://localhost:8701/fcl/authn');`

info

For a full example refer to [Authenticate using FCL snippet](https://academy.ecdao.org/en/snippets/fcl-authenticate)

### Test harness[​](#test-harness "Direct link to Test harness")

It's easy to use this FCL harness app as a barebones app to interact with the dev-wallet during development:

Navigate to <http://localhost:8701/harness>

### Wallet Discovery[​](#wallet-discovery "Direct link to Wallet Discovery")

[Wallet Discovery](/build/tools/clients/fcl-js/discovery)offers a convenient modal and mechanism to authenticate users and connects to all wallets available in the Flow ecosystem.

The following code from [Emerald Academy](https://academy.ecdao.org/en/snippets/fcl-authenticate) can be added to your React app to turn on Wallet Discovery:

`` _60

import { config, authenticate, unauthenticate, currentUser } from '@onflow/fcl';

_60

import { useEffect, useState } from 'react';

_60

_60

const fclConfigInfo = {

_60

emulator: {

_60

accessNode: 'http://127.0.0.1:8888',

_60

discoveryWallet: 'http://localhost:8701/fcl/authn',

_60

discoveryAuthInclude: [],

_60

},

_60

testnet: {

_60

accessNode: 'https://rest-testnet.onflow.org',

_60

discoveryWallet: 'https://fcl-discovery.onflow.org/testnet/authn',

_60

discoveryAuthnEndpoint:

_60

'https://fcl-discovery.onflow.org/api/testnet/authn',

_60

// Adds in Dapper + Ledger

_60

discoveryAuthInclude: ['0x82ec283f88a62e65', '0x9d2e44203cb13051'],

_60

},

_60

mainnet: {

_60

accessNode: 'https://rest-mainnet.onflow.org',

_60

discoveryWallet: 'https://fcl-discovery.onflow.org/authn',

_60

discoveryAuthnEndpoint: 'https://fcl-discovery.onflow.org/api/authn',

_60

// Adds in Dapper + Ledger

_60

discoveryAuthInclude: ['0xead892083b3e2c6c', '0xe5cd26afebe62781'],

_60

},

_60

};

_60

_60

const network = 'emulator';

_60

_60

config({

_60

'walletconnect.projectId': 'YOUR_PROJECT_ID', // your WalletConnect project ID

_60

'app.detail.title': 'Emerald Academy', // the name of your DApp

_60

'app.detail.icon': 'https://academy.ecdao.org/favicon.png', // your DApps icon

_60

'app.detail.description': 'Emerald Academy is a DApp for learning Flow', // a description of your DApp

_60

'app.detail.url': 'https://academy.ecdao.org', // the URL of your DApp

_60

'flow.network': network,

_60

'accessNode.api': fclConfigInfo[network].accessNode,

_60

'discovery.wallet': fclConfigInfo[network].discoveryWallet,

_60

'discovery.authn.endpoint': fclConfigInfo[network].discoveryAuthnEndpoint,

_60

// adds in opt-in wallets like Dapper and Ledger

_60

'discovery.authn.include': fclConfigInfo[network].discoveryAuthInclude,

_60

'discovery.authn.exclude': ['0x1234567890abcdef'], // excludes chosen wallets by address

_60

});

_60

_60

export default function App() {

_60

const [user, setUser] = useState({ loggedIn: false, addr: '' });

_60

_60

// So that the user stays logged in

_60

// even if the page refreshes

_60

useEffect(() => {

_60

currentUser.subscribe(setUser);

_60

}, []);

_60

_60

return (

_60

<div className="App">

_60

<button onClick={authenticate}>Log In</button>

_60

<button onClick={unauthenticate}>Log Out</button>

_60

<p>{user.loggedIn ? `Welcome, ${user.addr}!` : 'Please log in.'}</p>

_60

</div>

_60

);

_60

} ``

### Account or Address creation[​](#account-or-address-creation "Direct link to Account or Address creation")

You can [create a new account](https://cadence-lang.org/docs/language/accounts#account-creation) with the `&Account` constructor. When you do this, make sure to specify which account will pay for the creation fees. TO do this, set it as the payer.

The account you choose to pay these fees must have enough money to cover the cost. If it doesn't, the process will stop and the account won't be created.

`_14

transaction(publicKey: String) {

_14

prepare(signer: &Account) {

_14

let key = PublicKey(

_14

publicKey: publicKey.decodeHex(),

_14

signatureAlgorithm: SignatureAlgorithm.ECDSA_P256

_14

)

_14

let account = Account(payer: signer)

_14

account.keys.add(

_14

publicKey: key,

_14

hashAlgorithm: HashAlgorithm.SHA3_256,

_14

weight: 1000.0

_14

)

_14

}

_14

}`

To create a new Flow account refer to these resources

* [Create an Account with FCL snippet](https://academy.ecdao.org/en/snippets/fcl-create-account)
* [Create an Account in Cadence snippet](https://academy.ecdao.org/en/snippets/cadence-create-account)

### Get Flow balance[​](#get-flow-balance "Direct link to Get Flow balance")

To retrieve the token balance of a specific account, you must write involves write a script that pulls data from onchain. The user may have both locked tokens as well as unlocked so to retrieve the total balance we would aggregate them together.

`` _34

import * as fcl from '@onflow/fcl';

_34

import * as t from '@onflow/types';

_34

const CODE = `

_34

import "FungibleToken"

_34

import "FlowToken"

_34

import "LockedTokens"

_34

_34

access(all) fun main(address: Address): UFix64 {

_34

let account = getAccount(address)

_34

let unlockedVault = account

_34

.capabilities.get<&FlowToken.Vault>(/public/flowTokenBalance)

_34

.borrow()

_34

?? panic("Could not borrow Balance reference to the Vault"

_34

.concat(" at path /public/flowTokenBalance!")

_34

.concat(" Make sure that the account address is correct ")

_34

.concat("and that it has properly set up its account with a FlowToken Vault."))

_34

_34

let unlockedBalance = unlockedVault.balance

_34

let lockedAccountInfoCap = account

_34

.capabilities.get

_34

<&LockedTokens.TokenHolder>

_34

(LockedTokens.LockedAccountInfoPublicPath)

_34

if !(lockedAccountInfoCap!.check()) {

_34

return unlockedBalance

_34

}

_34

let lockedAccountInfoRef = lockedAccountInfoCap!.borrow()!

_34

let lockedBalance = lockedAccountInfoRef.getLockedAccountBalance()

_34

return lockedBalance + unlockedBalance

_34

}`;

_34

export const getTotalFlowBalance = async (address) => {

_34

return await fcl.decode(

_34

await fcl.send([fcl.script(CODE), fcl.args([fcl.arg(address, t.Address)])]),

_34

);

_34

}; ``

## Contribute[​](#contribute "Direct link to Contribute")

To release a new version of Dev Wallet is as simple as tagging and creating a release, a Github Action will then build a bundle of the Dev Wallet that can be used in other tools (such as CLI). If the update of the Dev Wallet is required in the CLI, create a seperate update PR on the CLI. For more information, visit the [fcl-dev-wallet GitHub repository](https://github.com/onflow/fcl-dev-wallet).

## More[​](#more "Direct link to More")

Additionally, you can explore these resources:

* [Guide to Creating a Fungible Token on Flow](/blockchain-development-tutorials/tokens/fungible-token-cadence)
* [Tutorial on Fungible Tokens](https://cadence-lang.org/docs/tutorial/fungible-tokens)
* [Faucets](/ecosystem/faucets)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-dev-wallet/index.md)

Last updated on **Dec 16, 2025** by **cshannon1218**

[Previous

Cadence VS Code Extension](/build/tools/vscode-extension)[Next

Client Tools](/build/tools/clients)

###### Rate this page

😞😐😊

Copy as Markdown

* [Get started](#get-started)
  + [Install the `flow-cli`](#install-the-flow-cli)+ [Create a `flow.json` file](#create-a-flowjson-file)+ [Start the Emulator](#start-the-emulator)+ [Start the dev wallet](#start-the-dev-wallet)+ [Configure your JavaScript application](#configure-your-javascript-application)+ [Test harness](#test-harness)+ [Wallet Discovery](#wallet-discovery)+ [Account or Address creation](#account-or-address-creation)+ [Get Flow balance](#get-flow-balance)* [Contribute](#contribute)* [More](#more)

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