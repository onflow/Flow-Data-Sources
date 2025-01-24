# Source: https://developers.flow.com/tools/clients/fcl-js/user-signatures




Signing and Verifying Arbitrary Data | Flow Developer Portal





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
* Signing and Verifying Arbitrary Data
On this page
# Signing and Verifying Arbitrary Data

## Signing Arbitrary Data[​](#signing-arbitrary-data "Direct link to Signing Arbitrary Data")

Cryptographic signatures are a key part of the blockchain. They are used to prove ownership of an address without exposing its private key. While primarily used for signing transactions, cryptographic signatures can also be used to sign arbitrary messages.

FCL has a feature that lets you send arbitrary data to a configured wallet/service where the user may approve signing it with their private key/s.

## Verifying User Signatures[​](#verifying-user-signatures "Direct link to Verifying User Signatures")

What makes message signatures more interesting is that we can use Flow blockchain to verify the signatures. Cadence has a built-in function `publicKey.verify` that will verify a signature against a Flow account given the account address.

FCL includes a utility function, `AppUtils.verifyUserSignatures`, for verifying one or more signatures against an account's public key on the Flow blockchain.

You can use both in tandem to prove a user is in control of a private key or keys.

This enables cryptographically-secure login flow using a message-signing-based authentication mechanism with a user’s public address as their identifier.

---

## `currentUser.signUserMessage()`[​](#currentusersignusermessage "Direct link to currentusersignusermessage")

A method to use allowing the user to personally sign data via FCL Compatible Wallets/Services.

> :Note: **Requires authentication/configuration with an authorized signing service.**

### Arguments[​](#arguments "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `message` | string | A hexadecimal string to be signed |

#### Returns[​](#returns "Direct link to Returns")

| Type | Description |
| --- | --- |
| `Array` | An Array of [CompositeSignatures](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/wallet-provider-spec/draft-v2.md#compositesignature): signature |

#### Usage[​](#usage "Direct link to Usage")

 `_10import * as fcl from "@onflow/fcl"_10_10const signMessage = async () => {_10 const MSG = Buffer.from("FOO").toString("hex")_10 try {_10 return await fcl.currentUser.signUserMessage(MSG)_10 } catch (error) {_10 console.log(error)_10 }_10}`

---

## `AppUtils.verifyUserSignatures`[​](#apputilsverifyusersignatures "Direct link to apputilsverifyusersignatures")

#### Note[​](#note "Direct link to Note")

⚠️ `fcl.config.flow.network` or options override is required to use this API. See [FCL Configuration](/tools/clients/fcl-js/configure-fcl).

A method allowing applications to cryptographically verify the ownership of a Flow account by verifying a message was signed by a user's private key/s. This is typically used with the response from `currentUser.signUserMessage`.

### Arguments[​](#arguments-1 "Direct link to Arguments")

| Name | Type | Description |
| --- | --- | --- |
| `message` | string **(required)** | A hexadecimal string |
| `compositeSignatures` | Array **(required)** | An Array of `CompositeSignatures` |
| `opts` | Object **(optional)** | `opts.fclCryptoContract` can be provided to override FCLCryptoContract address for local development |

#### Returns[​](#returns-1 "Direct link to Returns")

| Type | Description |
| --- | --- |
| Boolean | `true` if verified or `false` |

#### Usage[​](#usage-1 "Direct link to Usage")

 `_20/**_20 * Verify a valid signature/s for an account on Flow._20 *_20 * @param {string} msg - A message string in hexadecimal format_20 * @param {Array} compSigs - An array of Composite Signatures_20 * @param {string} compSigs[].addr - The account address_20 * @param {number} compSigs[].keyId - The account keyId_20 * @param {string} compSigs[].signature - The signature to verify_20 * @param {Object} [opts={}] - Options object_20 * @param {string} opts.fclCryptoContract - An optional override of Flow account address where the FCLCrypto contract is deployed_20 * @return {bool}_20 *_20 * @example_20 *_20 * const isValid = await fcl.AppUtils.verifyUserSignatures(_20 * Buffer.from('FOO').toString("hex"),_20 * [{f_type: "CompositeSignature", f_vsn: "1.0.0", addr: "0x123", keyId: 0, signature: "abc123"}],_20 * {fclCryptoContract}_20 * )_20 */`
#### Examples[​](#examples "Direct link to Examples")

Use cases include cryptographic login, message validation, verifiable credentials, and others.

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/user-signatures.md)Last updated on **Jan 3, 2025** by **Brian Doyle**[PreviousTransactions](/tools/clients/fcl-js/transactions)[NextWalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
###### Rate this page

😞😐😊

* [Signing Arbitrary Data](#signing-arbitrary-data)
* [Verifying User Signatures](#verifying-user-signatures)
* [`currentUser.signUserMessage()`](#currentusersignusermessage)
  + [Arguments](#arguments)
* [`AppUtils.verifyUserSignatures`](#apputilsverifyusersignatures)
  + [Arguments](#arguments-1)
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

