# Source: https://developers.flow.com/tools/clients/fcl-js/interaction-templates




Interaction Templates | Flow Developer Portal





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
* Interaction Templates
On this page
# Interaction Templates

> Interaction Templates are a concept established in FLIP-934. Read the FLIP [here](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md)

> "Interaction" in this context refers to the higher order term establised in FLIP-934 that encompases a transaction and script, things that *interact* with the blockchain.

## Overview[​](#overview "Direct link to Overview")

Interaction Templates establish a format for metadata that exists about an interaction. Interaction Templates can include:

* Human readable, internationalized messages about the interaction
* The Cadence code to carry out the interaction
* Information about arguments such as internationalized human readable messages and what the arguments act upon
* Contract dependencies the Interaction engages with, pinned to a version of them and their dependency tree

Applications and Wallets can use Interaction Templates and it's interaction metadata.

For example Applications and Wallets can extract the internationalized human readable messaging from an Interaction Template to display to their users prior to execution of the interaction.

## For Applications[​](#for-applications "Direct link to For Applications")

FCL `mutate` and `query` can accept an Interaction Template. FCL `mutate` and `query` will use the Interaction Template to:

* Extract the Cadence code to carry out the interaction
* Extract dependency configuration for the interaction (eg: Information about contract import addresses)

Here is an example of using `mutate` with an Interaction Template:

 `_10import * as fcl from "@onflow/fcl"_10import myTransactionTemplate from "./my-transaction-template.template.json"_10_10const txId = await fcl.mutate({_10 template: myTransactionTemplate_10})`

An Interaction Template can also be used with `query`:

 `_10import * as fcl from "@onflow/fcl"_10import myScriptTemplate from "./my-script-template.template.json"_10_10const info = await fcl.query({_10 template: myScriptTemplate_10})`

Interaction Templates can be resolved from remote locations:

 `_10import * as fcl from "@onflow/fcl"_10_10const txId = await fcl.mutate({_10 template: "http://interactions.awesome-crypto-project.com/buy-nft"_10})_10_10const nftInfo = await fcl.query({_10 template: "http://interactions.awesome-crypto-project.com/read-nft",_10 args: (arg, t) => [arg("nft-id", t.String)]_10})`

FCL will resolve the template from the remote location before using it to execute its underlying transaction or script.

> 💡 By requesting an Interaction Template from an external location, applications have a mechanism to always retrieve the most up to date way of accomplishing an interaction.

By default FCL supports resolving Interaction Templates over http/https, but FCL can also be configured with various other ways to resolve Interaction Templates:

 `_10import * as fcl from "@onflow/fcl"_10_10await fcl.config().put("document.resolver.ipfs", async ({ url }) => {_10 const jsonTemplate = getDocumentFromIPFS(url) // resolve interaction template from ipfs_10 return jsonTemplate_10})_10_10const txId = await fcl.mutate({_10 template: "ipfs://IPFSHASHGOESHERE"_10})`
## For Wallets[​](#for-wallets "Direct link to For Wallets")

Wallets can use Interaction Templates to:

* Display internationalized human readable information about a transaction to their users during signing
* Verify the dependencies of an Interaction Template have not changed since when the Interaction Template was created
* Using Interaction Template Audits, gain confidence in the correctness and safety of an Interaction Template and it's underlying transaction

When recieving a transaction to sign, wallets can query for an Interaction Template that corresponds to it.

Flow operates an "Interaction Template Discovery Service" which wallets can use to query for Interaction Templates. Anyone can run an "Interaction Template Discovery Service" and wallets can choose to query from any of them.

 `_18const cadence = cadenceFromTransactionToSign_18const network = "mainnet" // "mainnet" | "testnet"_18_18const cadence_base64 = btoa(cadence)_18_18const interactionTemplate = await fetch(_18 "https://flix.flow.com/v1/templates/search",_18 {_18 method: "POST",_18 headers: {_18 "Content-Type": "application/json"_18 }_18 body: JSON.stringify({_18 cadence_base64,_18 network_18 })_18 }_18)`
> 📖 For more on the "Interaction Template Discovery Service" that Flow operates, see [here](https://github.com/onflow/flow-interaction-template-service)

> ❗️ Not all transactions will have a corresponding Interaction Template. Wallets are encouraged to always support signing transactions that do not have a corresponding Interaction Template, or if they fail to discover one.

Once a wallet has a corresponding Interaction Template for a given transaction, they may also may wish to verify that the transaction it represents is safe to sign, and that the Interaction Template is accurate for that transaction.

To do so, wallets can rely on themselves, along with external Interaction Template Auditors to gain confidence in the Interaction Template and it's underlying transaction. Interaction Template Auditors are entities that audit Interaction Templates for correctness and safety.

> 💡 Anyone can be an Interaction Template Auditor. Wallets can choose auditors they trust, if any.

Wallets can specify auditors it trusts to FCL by configuring FCL with the address of each auditor:

 `_11import * as fcl from "@onflow/fcl"_11_11await fcl.config().put("flow.network", "mainnet")_11_11const auditorA_FlowAddress = "0xABC123DEF456"_11const auditorB_FlowAddress = "0xFFAA1212DEFF"_11_11await fcl.config().put("flow.auditors", [_11 auditorA_FlowAddress,_11 auditorB_FlowAddress_11])`

Wallets can check if the auditors they configured FCL with have audited a given Interaction Template:

 `_14import * as fcl from "@onflow/fcl"_14import myTransactionTemplate from "./my-transaction-template.template.json"_14_14const audits = await fcl.InteractionTemplateUtils_14 .getInteractionTemplateAudits({_14 template: myTransactionTemplate_14 })_14_14/**_14 * audits = {_14 * "0xABC123DEF456": true,_14 * "0xFFAA1212DEFF": false_14 * }_14 ** /`

The Flow team operates these auditor accounts:

| Flow Team Auditor Accounts | Address |
| --- | --- |
| TestNet | 0xf78bfc12d0a786dc |
| MainNet | 0xfd100e39d50a13e6 |

Since not all auditors that a wallet trusts may have audited a given Interaction Template, trusting multiple auditors can increase the chance that at least one of the trusted auditors has audited the Interaction Template.

> ❗️ Auditors can revoke audits at any time, so be sure to always check an Interaction Template's audit status.

Since contracts on Flow are mutable, wallets may additionally wish to verify that none of the dependency tree for the transaction an Interaction Template represents has changed since when it was created and of what it was audited against.

 `_10import * as fcl from "@onflow/fcl"_10import myTransactionTemplate from "./my-transaction-template.template.json"_10_10const hasDependencyTreeChanged = await fcl.InteractionTemplateUtils_10 .verifyDependencyPinsSameAtLatestSealedBlock({_10 template: myTransactionTemplate_10 })`

If the dependency tree has changed, wallets may choose to disregard the Interaction Template (and it's audits).

Once the Interaction Template has been sufficiently audited by auditors the wallet trusts, and it's dependency tree determined unchanged since the interaction was created and audited against, then the wallet can use the Interaction Template with greater confidence in it's correctness and safety.

The wallet may then decide to render human readable information about the transaction such as:

* Internationalized 'title' and 'description' of the transaction
* Internationalized 'title' for each of the transactions arguments alongside the arguments value

The wallet may then also make the status of it's audits known to the user in their UI. This allows the user to have greater confidence in the safety of the transaction.

## Data Structure[​](#data-structure "Direct link to Data Structure")

The following is an example Interaction Template that corresponds to a "Transfer FLOW" transaction:

 `_66{_66 "f_type": "InteractionTemplate",_66 "f_version": "1.0.0",_66 "id": "290b6b6222b2a77b16db896a80ddf29ebd1fa3038c9e6625a933fa213fce51fa",_66 "data": {_66 "type": "transaction",_66 "interface": "",_66 "messages": {_66 "title": {_66 "i18n": {_66 "en-US": "Transfer Tokens"_66 }_66 },_66 "description": {_66 "i18n": {_66 "en-US": "Transfer tokens from one account to another"_66 }_66 }_66 },_66 "cadence": "import FungibleToken from 0xFUNGIBLETOKENADDRESS\ntransaction(amount: UFix64, to: Address) {\nlet vault: @FungibleToken.Vault\nprepare(signer: &Account) {\nself.vault <- signer\n.borrow<&{FungibleToken.Provider}>(from: /storage/flowTokenVault)!\n.withdraw(amount: amount)\n}\nexecute {\ngetAccount(to)\n.capabilities.get(/public/flowTokenReceiver)!\n.borrow<&{FungibleToken.Receiver}>()!\n.deposit(from: <-self.vault)\n}\n}",_66 "dependencies": {_66 "0xFUNGIBLETOKENADDRESS": {_66 "FungibleToken": {_66 "mainnet": {_66 "address": "0xf233dcee88fe0abe",_66 "fq_address": "A.0xf233dcee88fe0abe.FungibleToken",_66 "contract": "FungibleToken",_66 "pin": "83c9e3d61d3b5ebf24356a9f17b5b57b12d6d56547abc73e05f820a0ae7d9cf5",_66 "pin_block_height": 34166296_66 },_66 "testnet": {_66 "address": "0x9a0766d93b6608b7",_66 "fq_address": "A.0x9a0766d93b6608b7.FungibleToken",_66 "contract": "FungibleToken",_66 "pin": "83c9e3d61d3b5ebf24356a9f17b5b57b12d6d56547abc73e05f820a0ae7d9cf5",_66 "pin_block_height": 74776482_66 }_66 }_66 }_66 },_66 "arguments": {_66 "amount": {_66 "index": 0,_66 "type": "UFix64",_66 "messages": {_66 "title": {_66 "i18n": {_66 "en-US": "The amount of FLOW tokens to send"_66 }_66 }_66 }_66 },_66 "to": {_66 "index": 1,_66 "type": "Address",_66 "messages": {_66 "title": {_66 "i18n": {_66 "en-US": "The Flow account the tokens will go to"_66 }_66 }_66 }_66 }_66 }_66 }_66}`[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/interaction-templates.mdx)Last updated on **Dec 20, 2024** by **Brian Doyle**[PreviousInstallation](/tools/clients/fcl-js/installation)[NextProving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
###### Rate this page

😞😐😊

* [Overview](#overview)
* [For Applications](#for-applications)
* [For Wallets](#for-wallets)
* [Data Structure](#data-structure)
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
* [Flowdiver Mainnet](https://flowdiver.io/)
* [Flowdiver Testnet](https://testnet.flowdiver.io/)
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

