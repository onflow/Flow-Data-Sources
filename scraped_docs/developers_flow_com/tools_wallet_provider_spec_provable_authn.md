# Source: https://developers.flow.com/tools/wallet-provider-spec/provable-authn




Provable Authn | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
  + [Authorization Function](/tools/wallet-provider-spec/authorization-function)
  + [Introduction](/tools/wallet-provider-spec/custodial)
  + [Provable Authn](/tools/wallet-provider-spec/provable-authn)
  + [User Signature](/tools/wallet-provider-spec/user-signature)


* [Wallet Provider Spec](/tools/wallet-provider-spec)
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
3. Wallet prepares and signs the message:
   * Encodes the `appIdentifier`, `nonce`, and `address` along with the `"FCL-ACCOUNT-PROOF-V0.0"` domain separation tag, [using the encoding scheme described below](#account-proof-message-encoding).
   * Signs the message with the `signatureAlgorithm` and `hashAlgorithm` specified on user's key. **It is highly recommended that the wallet display the message data and receive user approval before signing.**
4. Wallet sends back this new service and data along with the other service configuration when completing Authn.

### Account Proof Message Encoding[​](#account-proof-message-encoding "Direct link to Account Proof Message Encoding")

The account proof message is encoded as follows:

 `_10MESSAGE = _10 USER_DOMAIN_TAG ||_10 RLP_ENCODE([_10 APP_IDENTIFIER, _10 ADDRESS, _10 NONCE_10 ])`

with the following values:

* `ACCOUNT_PROOF_DOMAIN_TAG` is the constant `"FCL-ACCOUNT-PROOF-V0.0"`, encoded as UTF-8 byte array and right-padded with zero bytes to a length of 32 bytes.
* `APP_IDENTIFIER` is an arbitrary length string.
* `ADDRESS` is a byte array containing the address bytes, left-padded with zero bytes to a length of 8 bytes.
* `NONCE` is an byte array with a minimum length of 32 bytes.

`RLP_ENCODE` is a function that performs [RLP encoding](https://eth.wiki/fundamentals/rlp) and returns the encoded value as bytes.

### JavaScript Signing Example[​](#javascript-signing-example "Direct link to JavaScript Signing Example")

 `_20// Using WalletUtils_20import {WalletUtils} from "@onflow/fcl"_20_20const message = WalletUtils.encodeAccountProof(_20 appIdentifier, // A human readable string to identify your application during signing_20 address, // Flow address of the user authenticating_20 nonce, // minimum 32-btye nonce_20)_20_20sign(privateKey, message)_20_20// Without using FCL WalletUtils_20const ACCOUNT_PROOF_DOMAIN_TAG = rightPaddedHexBuffer(_20 Buffer.from("FCL-ACCOUNT-PROOF-V0.0").toString("hex"),_20 32_20)_20const message = rlp([appIdentifier, address, nonce])_20const prependUserDomainTag = (message) => ACCOUNT_PROOF_DOMAIN_TAG + message_20_20sign(privateKey, prependUserDomainTag(message))`
 `_17// Authentication Proof Service_17{_17 f_type: "Service", // Its a service!_17 f_vsn: "1.0.0", // Follows the v1.0.0 spec for the service_17 type: "account-proof", // the type of service it is_17 method: "DATA", // Its data!_17 uid: "awesome-wallet#account-proof", // A unique identifier for the service _17 data: {_17 f_type: "account-proof",_17 f_vsn: "1.0.0"_17 // The user's address (8 bytes, i.e 16 hex characters)_17 address: "0xf8d6e0586b0a20c7", _17 // Nonce signed by the current account-proof (minimum 32 bytes in total, i.e 64 hex characters)_17 nonce: "75f8587e5bd5f9dcc9909d0dae1f0ac5814458b2ae129620502cb936fde7120a",_17 signatures: [CompositeSignature],_17 }_17}`[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/wallet-provider-spec/provable-authn.md)Last updated on **Jan 7, 2025** by **Chase Fleming**[PreviousIntroduction](/tools/wallet-provider-spec/custodial)[NextUser Signature](/tools/wallet-provider-spec/user-signature)
###### Rate this page

😞😐😊

* [TL;DR Wallet Provider](#tldr-wallet-provider)
  + [Account Proof Message Encoding](#account-proof-message-encoding)
  + [JavaScript Signing Example](#javascript-signing-example)
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

