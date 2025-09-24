# Source: https://developers.flow.com/build/tools/wallet-provider-spec/provable-authn

Provable Authn | Flow Developer Portal



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
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

    - [Authorization Function](/build/tools/wallet-provider-spec/authorization-function)
    - [Introduction](/build/tools/wallet-provider-spec/custodial)
    - [Provable Authn](/build/tools/wallet-provider-spec/provable-authn)
    - [User Signature](/build/tools/wallet-provider-spec/user-signature)

* [Tools & SDKs](/build/tools)
* [Wallet Provider Spec](/build/tools/wallet-provider-spec)
* Provable Authn

On this page

# Provable Authn

In order to improve UX/DX and encourage seamless integration with App backends and services, `fcl.authenticate` has been upgraded.

Additional data is sent in the body of `FCL:VIEW:READY:RESPONSE`. This data includes what the wallet needs to build a message for signing with the user’s private key/s.
The signature can be returned as part of an optional `account-proof` service with the `FCL:VIEW:RESPONSE`.

When provided by the wallet, this **signature** and additional **account-proof data** is available to the App via `fcl.currentUser` services. The service data can be used to recreate the message, and verify the signature on the Flow Blockchain.

For example, it can be sent to the App’s backend and after validating the signature and the other account-proof data, it can safely associate the included account address to a user and log them in.

---

## TL;DR Wallet Provider[​](#tldr-wallet-provider "Direct link to TL;DR Wallet Provider")

1. Wallet receives Authn `FCL:VIEW:READY:RESPONSE` request and parses out the `appIdentifier`, and `nonce`.
2. The wallet authenticates the user however they choose to do, and determines the user's account `address`
3. The wallet must validate the `appIdentifier` against the RFC 6454 origin of the request if it matches the
   format of a [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI. Requests with a mismatch should be rejected. Some legacy systems may use arbitrary strings as `appIdentifier` and not [RFC 6454](https://www.rfc-editor.org/rfc/rfc6454.html) origins. In this case, wallets should display a warning to the user that the app identifier does not match the origin of the request.
4. Wallet prepares and signs the message:
   * Encodes the `appIdentifier`, `nonce`, and `address` along with the `"FCL-ACCOUNT-PROOF-V0.0"` domain separation tag, [using the encoding scheme described below](#account-proof-message-encoding).
   * Signs the message with the `signatureAlgorithm` and `hashAlgorithm` specified on user's key. **It is highly recommended that the wallet display the message data and receive user approval before signing.**
5. Wallet sends back this new service and data along with the other service configuration when completing Authn.

### Account Proof Message Encoding[​](#account-proof-message-encoding "Direct link to Account Proof Message Encoding")

The account proof message is encoded as follows:

`_10

MESSAGE =

_10

USER_DOMAIN_TAG ||

_10

RLP_ENCODE([

_10

APP_IDENTIFIER,

_10

ADDRESS,

_10

NONCE

_10

])`

with the following values:

* `ACCOUNT_PROOF_DOMAIN_TAG` is the constant `"FCL-ACCOUNT-PROOF-V0.0"`, encoded as UTF-8 byte array and right-padded with zero bytes to a length of 32 bytes.
* `APP_IDENTIFIER` is an arbitrary length string.
* `ADDRESS` is a byte array containing the address bytes, left-padded with zero bytes to a length of 8 bytes.
* `NONCE` is an byte array with a minimum length of 32 bytes.

`RLP_ENCODE` is a function that performs [RLP encoding](https://eth.wiki/fundamentals/rlp) and returns the encoded value as bytes.

### JavaScript Signing Example[​](#javascript-signing-example "Direct link to JavaScript Signing Example")

`_34

// Using WalletUtils

_34

import {WalletUtils} from "@onflow/fcl"

_34

_34

WalletUtils.onMessageFromFcl(

_34

(data, {origin}) => {

_34

const {address, nonce, appIdentifier} = data.data

_34

_34

// Check if the appIdentifier is a valid RFC 3986 URI

_34

if (!isRfc3986Uri(appIdentifier)) {

_34

// Warn the user that the appIdentifier does not match the origin and to proceed with caution

_34

} else if (origin !== appIdentifier) {

_34

// Reject the request if the appIdentifier is a valid RFC 3986 URI but does not match the origin

_34

throw new Error("Invalid appIdentifier")

_34

}

_34

_34

const message = WalletUtils.encodeAccountProof(

_34

appIdentifier, // A human readable string to identify your application during signing

_34

address, // Flow address of the user authenticating

_34

nonce, // minimum 32-btye nonce

_34

)

_34

_34

sign(privateKey, message)

_34

_34

// Without using FCL WalletUtils

_34

const ACCOUNT_PROOF_DOMAIN_TAG = rightPaddedHexBuffer(

_34

Buffer.from("FCL-ACCOUNT-PROOF-V0.0").toString("hex"),

_34

32

_34

)

_34

const message = rlp([appIdentifier, address, nonce])

_34

const prependUserDomainTag = (message) => ACCOUNT_PROOF_DOMAIN_TAG + message

_34

_34

sign(privateKey, prependUserDomainTag(message))

_34

}

_34

)`

`_17

// Authentication Proof Service

_17

{

_17

f_type: "Service", // Its a service!

_17

f_vsn: "1.0.0", // Follows the v1.0.0 spec for the service

_17

type: "account-proof", // the type of service it is

_17

method: "DATA", // Its data!

_17

uid: "awesome-wallet#account-proof", // A unique identifier for the service

_17

data: {

_17

f_type: "account-proof",

_17

f_vsn: "1.0.0"

_17

// The user's address (8 bytes, i.e 16 hex characters)

_17

address: "0xf8d6e0586b0a20c7",

_17

// Nonce signed by the current account-proof (minimum 32 bytes in total, i.e 64 hex characters)

_17

nonce: "75f8587e5bd5f9dcc9909d0dae1f0ac5814458b2ae129620502cb936fde7120a",

_17

signatures: [CompositeSignature],

_17

}

_17

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/wallet-provider-spec/provable-authn.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Introduction](/build/tools/wallet-provider-spec/custodial)[Next

User Signature](/build/tools/wallet-provider-spec/user-signature)

###### Rate this page

😞😐😊

Copy as Markdown

* [TL;DR Wallet Provider](#tldr-wallet-provider)
  + [Account Proof Message Encoding](#account-proof-message-encoding)
  + [JavaScript Signing Example](#javascript-signing-example)

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
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.