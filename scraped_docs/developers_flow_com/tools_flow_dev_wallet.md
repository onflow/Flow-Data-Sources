# Source: https://developers.flow.com/tools/flow-dev-wallet




Flow Dev Wallet | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* Flow Dev Wallet
On this page
# Flow Dev Wallet

The Flow Dev Wallet is a mock Flow wallet that simulates the protocols used by [FCL](/tools/clients/fcl-js) to interact with the Flow blockchain on behalf of simulated user accounts.

IMPORTANT

This project implements an FCL compatible
interface, but should **not** be used as a reference for
building a production grade wallet.

This project should only be used in aid of local
development against a locally run instance of the Flow
blockchain like the Flow emulator, and should never be used in
conjunction with Flow Mainnet, Testnet, or any
other instances of Flow.


info

To see a full list of Flow compatible wallets visit [Wallets page](/ecosystem/wallets)

## Getting Started[​](#getting-started "Direct link to Getting Started")

Before using the dev wallet, you'll need to start the Flow emulator.

### Install the `flow-cli`[​](#install-the-flow-cli "Direct link to install-the-flow-cli")

The Flow emulator is bundled with the Flow CLI. Instructions for installing the CLI can be found here: [flow-cli/install/](/tools/flow-cli/install)

### Create a `flow.json` file[​](#create-a-flowjson-file "Direct link to create-a-flowjson-file")

Run this command to create `flow.json` file (typically in your project's root directory):

 `_10flow init --config-only`
### Start the Emulator[​](#start-the-emulator "Direct link to Start the Emulator")

Start the Emulator and deploy the contracts by running the following command from the directory containing `flow.json` in your project:

 `_10flow emulator start_10flow project deploy --network emulator`
## Configuring Your JavaScript Application[​](#configuring-your-javascript-application "Direct link to Configuring Your JavaScript Application")

The Flow Dev Wallet is designed to be used with [`@onflow/fcl`](https://github.com/onflow/fcl-js) version `1.0.0` or higher. The FCL package can be installed with: `npm install @onflow/fcl` or `yarn add @onflow/fcl`.

To use the dev wallet, configure FCL to point to the address of a locally running [Flow emulator](#start-the-emulator) and the dev wallet endpoint.

 `_10import * as fcl from '@onflow/fcl';_10_10fcl_10 .config()_10 // Point App at Emulator REST API_10 .put('accessNode.api', 'http://localhost:8888')_10 // Point FCL at dev-wallet (default port)_10 .put('discovery.wallet', 'http://localhost:8701/fcl/authn');`
info

For a full example refer to [Authenticate using FCL snippet](https://academy.ecdao.org/en/snippets/fcl-authenticate)

### Test harness[​](#test-harness "Direct link to Test harness")

It's easy to use this FCL harness app as a barebones
app to interact with the dev-wallet during development:

Navigate to <http://localhost:8701/harness>

### Wallet Discovery[​](#wallet-discovery "Direct link to Wallet Discovery")

[Wallet Discovery](/tools/clients/fcl-js/discovery) offers a convenient modal and mechanism to authenticate users and connects to all wallets available in the Flow ecosystem.

The following code from [Emerald Academy](https://academy.ecdao.org/en/snippets/fcl-authenticate) can be added to your React app to enable Wallet Discovery:

 `_59import { config, authenticate, unauthenticate, currentUser } from '@onflow/fcl';_59import { useEffect, useState } from 'react';_59_59const fclConfigInfo = {_59 emulator: {_59 accessNode: 'http://127.0.0.1:8888',_59 discoveryWallet: 'http://localhost:8701/fcl/authn',_59 discoveryAuthInclude: [],_59 },_59 testnet: {_59 accessNode: 'https://rest-testnet.onflow.org',_59 discoveryWallet: 'https://fcl-discovery.onflow.org/testnet/authn',_59 discoveryAuthnEndpoint:_59 'https://fcl-discovery.onflow.org/api/testnet/authn',_59 // Adds in Dapper + Ledger_59 discoveryAuthInclude: ['0x82ec283f88a62e65', '0x9d2e44203cb13051'],_59 },_59 mainnet: {_59 accessNode: 'https://rest-mainnet.onflow.org',_59 discoveryWallet: 'https://fcl-discovery.onflow.org/authn',_59 discoveryAuthnEndpoint: 'https://fcl-discovery.onflow.org/api/authn',_59 // Adds in Dapper + Ledger_59 discoveryAuthInclude: ['0xead892083b3e2c6c', '0xe5cd26afebe62781'],_59 },_59};_59_59const network = 'emulator';_59_59config({_59 'walletconnect.projectId': 'YOUR_PROJECT_ID', // your WalletConnect project ID_59 'app.detail.title': 'Emerald Academy', // the name of your DApp_59 'app.detail.icon': 'https://academy.ecdao.org/favicon.png', // your DApps icon_59 'app.detail.description': 'Emerald Academy is a DApp for learning Flow', // a description of your DApp_59 'app.detail.url': 'https://academy.ecdao.org', // the URL of your DApp_59 'flow.network': network,_59 'accessNode.api': fclConfigInfo[network].accessNode,_59 'discovery.wallet': fclConfigInfo[network].discoveryWallet,_59 'discovery.authn.endpoint': fclConfigInfo[network].discoveryAuthnEndpoint,_59 // adds in opt-in wallets like Dapper and Ledger_59 'discovery.authn.include': fclConfigInfo[network].discoveryAuthInclude,_59});_59_59export default function App() {_59 const [user, setUser] = useState({ loggedIn: false, addr: '' });_59_59 // So that the user stays logged in_59 // even if the page refreshes_59 useEffect(() => {_59 currentUser.subscribe(setUser);_59 }, []);_59_59 return (_59 <div className="App">_59 <button onClick={authenticate}>Log In</button>_59 <button onClick={unauthenticate}>Log Out</button>_59 <p>{user.loggedIn ? `Welcome, ${user.addr}!` : 'Please log in.'}</p>_59 </div>_59 );_59}`
### Account/Address creation[​](#accountaddress-creation "Direct link to Account/Address creation")

You can [create a new account](https://cadence-lang.org/docs/language/accounts#account-creation) by using the `&Account` constructor. When you do this, make sure to specify which account will pay for the creation fees by setting it as the payer.

The account you choose to pay these fees must have enough money to cover the cost. If it doesn't, the process will stop and the account won't be created.

 `_14transaction(publicKey: String) {_14 prepare(signer: &Account) {_14 let key = PublicKey(_14 publicKey: publicKey.decodeHex(),_14 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_14 )_14 let account = Account(payer: signer)_14 account.keys.add(_14 publicKey: key,_14 hashAlgorithm: HashAlgorithm.SHA3_256,_14 weight: 1000.0_14 )_14 }_14}`

To create a new Flow account refer to these resources

* [Create an Account with FCL snippet](https://academy.ecdao.org/en/snippets/fcl-create-account)
* [Create an Account in Cadence snippet](https://academy.ecdao.org/en/snippets/cadence-create-account)

### Get Flow Balance[​](#get-flow-balance "Direct link to Get Flow Balance")

Retrieving the token balance of a specific account involves writing a script to pull data from onchain. The user may have both locked tokens as well as unlocked so to retrieve the total balance we would aggregate them together.

 `_34import * as fcl from '@onflow/fcl';_34import * as t from '@onflow/types';_34const CODE = `_34import "FungibleToken"_34import "FlowToken"_34import "LockedTokens"_34_34access(all) fun main(address: Address): UFix64 {_34 let account = getAccount(address)_34 let unlockedVault = account_34 .capabilities.get<&FlowToken.Vault>(/public/flowTokenBalance)_34 .borrow()_34 ?? panic("Could not borrow Balance reference to the Vault"_34 .concat(" at path /public/flowTokenBalance!")_34 .concat(" Make sure that the account address is correct ")_34 .concat("and that it has properly set up its account with a FlowToken Vault."))_34_34 let unlockedBalance = unlockedVault.balance_34 let lockedAccountInfoCap = account_34 .capabilities.get_34 <&LockedTokens.TokenHolder>_34 (LockedTokens.LockedAccountInfoPublicPath)_34 if !(lockedAccountInfoCap!.check()) {_34 return unlockedBalance_34 }_34 let lockedAccountInfoRef = lockedAccountInfoCap!.borrow()!_34 let lockedBalance = lockedAccountInfoRef.getLockedAccountBalance()_34 return lockedBalance + unlockedBalance_34}`;_34export const getTotalFlowBalance = async (address) => {_34 return await fcl.decode(_34 await fcl.send([fcl.script(CODE), fcl.args([fcl.arg(address, t.Address)])]),_34 );_34};`
## Contributing[​](#contributing "Direct link to Contributing")

Releasing a new version of Dev Wallet is as simple as tagging and creating a release, a Github Action will then build a bundle of the Dev Wallet that can be used in other tools (such as CLI). If the update of the Dev Wallet is required in the CLI, a seperate update PR on the CLI should be created. For more information, please visit the [fcl-dev-wallet GitHub repository](https://github.com/onflow/fcl-dev-wallet).

## More[​](#more "Direct link to More")

Additionally, consider exploring these resources:

* [Guide to Creating a Fungible Token on Flow](/build/guides/fungible-token)
* [Tutorial on Fungible Tokens](https://cadence-lang.org/docs/tutorial/fungible-tokens)
* [Faucets](/ecosystem/faucets)
[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-dev-wallet/index.md)Last updated on **Feb 6, 2025** by **Brian Doyle**[PreviousMigration Guide v0.25.0](/tools/clients/flow-go-sdk/migration-v0.25.0)[NextCadence VS Code Extension](/tools/vscode-extension)
###### Rate this page

😞😐😊

* [Getting Started](#getting-started)
  + [Install the `flow-cli`](#install-the-flow-cli)
  + [Create a `flow.json` file](#create-a-flowjson-file)
  + [Start the Emulator](#start-the-emulator)
* [Configuring Your JavaScript Application](#configuring-your-javascript-application)
  + [Test harness](#test-harness)
  + [Wallet Discovery](#wallet-discovery)
  + [Account/Address creation](#accountaddress-creation)
  + [Get Flow Balance](#get-flow-balance)
* [Contributing](#contributing)
* [More](#more)
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

