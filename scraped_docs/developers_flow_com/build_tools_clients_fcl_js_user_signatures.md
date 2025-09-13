# Source: https://developers.flow.com/build/tools/clients/fcl-js/user-signatures

Signing and Verifying Arbitrary Data | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)

    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)
      * [Authentication](/build/tools/clients/fcl-js/authentication)
      * [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)
      * [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)
      * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)
      * [Installation](/build/tools/clients/fcl-js/installation)
      * [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)
      * [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)
      * [Scripts](/build/tools/clients/fcl-js/scripts)
      * [Transactions](/build/tools/clients/fcl-js/transactions)
      * [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)
      * [WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)
    - [Flow Go SDK](/build/tools/clients/flow-go-sdk)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Client Tools](/build/tools/clients)
* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)
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

`_10

import * as fcl from "@onflow/fcl"

_10

_10

const signMessage = async () => {

_10

const MSG = Buffer.from("FOO").toString("hex")

_10

try {

_10

return await fcl.currentUser.signUserMessage(MSG)

_10

} catch (error) {

_10

console.log(error)

_10

}

_10

}`

---

## `AppUtils.verifyUserSignatures`[​](#apputilsverifyusersignatures "Direct link to apputilsverifyusersignatures")

#### Note[​](#note "Direct link to Note")

⚠️ `fcl.config.flow.network` or options override is required to use this API. See [FCL Configuration](/build/tools/clients/fcl-js/configure-fcl).

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

`_20

/**

_20

* Verify a valid signature/s for an account on Flow.

_20

*

_20

* @param {string} msg - A message string in hexadecimal format

_20

* @param {Array} compSigs - An array of Composite Signatures

_20

* @param {string} compSigs[].addr - The account address

_20

* @param {number} compSigs[].keyId - The account keyId

_20

* @param {string} compSigs[].signature - The signature to verify

_20

* @param {Object} [opts={}] - Options object

_20

* @param {string} opts.fclCryptoContract - An optional override of Flow account address where the FCLCrypto contract is deployed

_20

* @return {bool}

_20

*

_20

* @example

_20

*

_20

* const isValid = await fcl.AppUtils.verifyUserSignatures(

_20

* Buffer.from('FOO').toString("hex"),

_20

* [{f_type: "CompositeSignature", f_vsn: "1.0.0", addr: "0x123", keyId: 0, signature: "abc123"}],

_20

* {fclCryptoContract}

_20

* )

_20

*/`

#### Examples[​](#examples "Direct link to Examples")

Use cases include cryptographic login, message validation, verifiable credentials, and others.

---

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/user-signatures.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Transactions](/build/tools/clients/fcl-js/transactions)[Next

WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)

###### Rate this page

😞😐😊

Copy as Markdown

* [Signing Arbitrary Data](#signing-arbitrary-data)
* [Verifying User Signatures](#verifying-user-signatures)
* [`currentUser.signUserMessage()`](#currentusersignusermessage)
  + [Arguments](#arguments)
* [`AppUtils.verifyUserSignatures`](#apputilsverifyusersignatures)
  + [Arguments](#arguments-1)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.