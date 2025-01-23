# Source: https://developers.flow.com/tools/wallet-provider-spec/user-signature




User Signature | Flow Developer Portal





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
* User Signature
On this page
# User Signature

## Status[​](#status "Direct link to Status")

* **Last Updated:** June 1st 2021
* **Stable:** Yes
* **Risk of Breaking Change:** Low
* **Compatibility:** `>= @onflow/fcl@0.0.71`

# Overview and Introduction

**Personally sign data via FCL Compatible Wallets**

**FCL** now incldues **`signUserMessage()`** which allows for the sending of unencrypted message data to a connected wallet provider or service to be signed with a user's private key.

An application or service can verify a signature against a user's public key on the **Flow Blockchain**, providing proof a user controls the account's private key.

**Use Cases**

* **Authentication**: Cryptographically verify the ownership of a **Flow** account by signing a piece of data using a private key
* **Improved Application Login**
  + **Increased security**: Arguably more secure than proof of ownership by email/password
  + **Simplified UX**: No application password required
  + **Increased privacy**: No email or third party authentication service needed
* **Message Validation**: Assuring that a message sent or received has not been tampered with
* **Multisig contracts**
* **Decentralised exchanges**
* **Meta transactions**

# Config and Authentication

As a prerequisite, **FCL** is configured to point to the Wallet Provider's Authentication Endpoint. No additional configuration is required.

> During development (and on mainnet) FCL can be configured to use the wallet directly by
> setting the **Wallet Discovery Url** to the wallet provider's **Authentication Endpoint**
> by configuring fcl like this `config().put("discovery.wallet", "https://my-awesome-wallet-provider.com/fcl/authenticate")`.

Common Configuration Keys and additional info can be found here [How to Configure FCL](/tools/clients/fcl-js/configure-fcl#common-configuration-keys)

1. A user initiates authentication with the wallet provider via application UI
2. The wallet confirms a user's identity and sends back information used to configure **FCL** for future user actions in the application
3. Included in the authentication response should be the provider's [Key Services](#) including a **`user-signature`** service for use with **`signUserMessage()`**

# User Signature Service

A [user-signature service](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/user-signature.js) is a standard service, with methods for **IFRAME/RPC** or **HTTP/POST**.

The `user-signature` service receives a signable message from **FCL** and returns a standard [PollingResponse](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/polling-response.js#L5) with an array of [CompositeSignatures](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/composite-signature.js#L4) or `null` as the data.

A status of **Approved** needs to have an array of composite signatures as data.

A status of **Declined** needs to include a reason why.

A **Pending** status needs to include an updates service and can include a local.
A service using the **`IFRAME/RPC`** method can only respond with approved or declined, as pending is not valid for iframes.

When `signUserMessage()` is called by the application, **FCL** uses the service method to decide how to send the signable to the wallet.

The Wallet is responsible for prepending the signable with the correct `UserDomainTag`, hashing, and signing the message.

# Signing Sequence

1. Application sends message to signing service. **FCL expects a hexadecimal string**
2. Wallet/Service tags the message with required `UserDomainTag` (see below), hashes, and signs using the `signatureAlgorithm` specified on account key
3. Wallet makes available a Composite Signature consisting of `addr`, `keyId`, and `signature` **as a hex string**

### UserDomainTag[​](#userdomaintag "Direct link to UserDomainTag")

The **`UserDomainTag`** is the prefix of all signed user space payloads.

Before hashing and signing the message, the wallet must add a specified DOMAIN TAG.

> currently **"FLOW-V0.0-user"**

A domain tag is encoded as **UTF-8 bytes, right padded to a total length of 32 bytes**, prepended to the message.

The signature can now be verified on the Flow blockchain. The following illustrates an example using `fcl.verifyUserSignatures`

 `_17/**_17 * Verify a valid signature/s for an account on Flow._17 *_17 * @param {string} msg - A message string in hexadecimal format_17 * @param {Array} compSigs - An array of Composite Signatures_17 * @param {string} compSigs[].addr - The account address_17 * @param {number} compSigs[].keyId - The account keyId_17 * @param {string} compSigs[].signature - The signature to verify_17 * @return {bool}_17 *_17 * @example_17 *_17 * const isValid = await fcl.verifyUserSignatures(_17 * Buffer.from('FOO').toString("hex"),_17 * [{f_type: "CompositeSignature", f_vsn: "1.0.0", addr: "0x123", keyId: 0, signature: "abc123"}]_17 * )_17 */`
## TL;DR Wallet Provider[​](#tldr-wallet-provider "Direct link to TL;DR Wallet Provider")

* Register with **FCL** and provide signing service endpoint. No further configuration is needed.
* On receipt of message, prompt user to approve or decline
* Prepend `UserDomainTag`, hash and sign the message with the signatureAlgorithm specified on user's key
* Return a standard `PollingResponse` with an array of `CompositeSignatures` as data or `null` and `reason` if declined
[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/wallet-provider-spec/user-signature.md)Last updated on **Dec 24, 2024** by **Jerome P**[PreviousProvable Authn](/tools/wallet-provider-spec/provable-authn)
###### Rate this page

😞😐😊

* [Status](#status)
  + [UserDomainTag](#userdomaintag)
* [TL;DR Wallet Provider](#tldr-wallet-provider)
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

