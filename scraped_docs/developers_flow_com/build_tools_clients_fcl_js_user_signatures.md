# Source: https://developers.flow.com/build/tools/clients/fcl-js/user-signatures

Signing and Verifying Arbitrary Data | Flow Developer Portal



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

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                          * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                                * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* Signing and Verifying Arbitrary Data

On this page

# Signing and Verifying Arbitrary Data

## Signing and Verifying Arbitrary Data[​](#signing-and-verifying-arbitrary-data "Direct link to Signing and Verifying Arbitrary Data")

Cryptographic signatures are a key part of the blockchain. They prove ownership of an address without exposing its private key. While primarily used to sign transactions, you can also use cryptographic signatures to sign arbitrary messages.

FCL has a feature that lets you send arbitrary data to a configured wallet or service. The user may approve signing it with their private keys.

## Verify user signatures[​](#verify-user-signatures "Direct link to Verify user signatures")

What makes message signatures more interesting is that we can use Flow blockchain to verify the signatures. Cadence has a built-in function `publicKey.verify` that will verify a signature against a Flow account given the account address.

FCL includes a utility function, `AppUtils.verifyUserSignatures`, that verifies one or more signatures against an account's public key on the Flow blockchain.

You can use both in tandem to prove a user is in control of a private key or keys.

This allows cryptographically-secure login flow with a message-signing-based authentication mechanism with a user’s public address as their identifier.

---

## `currentUser.signUserMessage()`[​](#currentusersignusermessage "Direct link to currentusersignusermessage")

A method that allows the user to personally sign data via FCL Compatible Wallets or Services.

info

> **Requires authentication/configuration with an authorized signing service.**

### Arguments[​](#arguments "Direct link to Arguments")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | `message` string A hexadecimal string to be signed | | | | | |

#### Returns[​](#returns "Direct link to Returns")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Description|  |  | | --- | --- | | `Array` An Array of [CompositeSignatures](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/wallet-provider-spec/draft-v2.md#compositesignature): signature | | | |

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

info

⚠️ `fcl.config.flow.network` or options override is required to use this API. See [FCL Configuration](/build/tools/clients/fcl-js/configure-fcl).

A method to verify that a user's private keys signed a message, which allows applications to cryptographically verify Flow account ownership. This is typically used with the response from `currentUser.signUserMessage`.

### Arguments[​](#arguments-1 "Direct link to Arguments")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `message` string **(required)** A hexadecimal string|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `compositeSignatures` Array **(required)** An Array of `CompositeSignatures`| `opts` Object **(optional)** `opts.fclCryptoContract` can be provided to override FCLCryptoContract address for local development | | | | | | | | | | | |

#### Returns[​](#returns-1 "Direct link to Returns")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Description|  |  | | --- | --- | | Boolean `true` if verified or `false` | | | |

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

Last updated on **Dec 9, 2025** by **cshannon1218**

[Previous

Transactions](/build/tools/clients/fcl-js/transactions)[Next

Flow Go SDK](/build/tools/clients/flow-go-sdk)

###### Rate this page

😞😐😊

Copy as Markdown

* [Signing and Verifying Arbitrary Data](#signing-and-verifying-arbitrary-data)* [Verify user signatures](#verify-user-signatures)* [`currentUser.signUserMessage()`](#currentusersignusermessage)
      + [Arguments](#arguments)* [`AppUtils.verifyUserSignatures`](#apputilsverifyusersignatures)
        + [Arguments](#arguments-1)

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