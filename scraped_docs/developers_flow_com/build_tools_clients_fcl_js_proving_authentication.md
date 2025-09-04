# Source: https://developers.flow.com/build/tools/clients/fcl-js/proving-authentication

Proving Ownership of a Flow Account | Flow Developer Portal



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
* Proving Ownership of a Flow Account

On this page

# Proving Ownership of a Flow Account

## Proving Ownership of a Flow Account[​](#proving-ownership-of-a-flow-account "Direct link to Proving Ownership of a Flow Account")

A common desire that application developers have is to be able to prove that a
user controls an onchain account. Proving ownership of an onchain account is a
way to authenticate a user with an application backend. Fortunately,
FCL provides a way to achieve this.

During user authentication, some FCL compatible wallets will choose to support
the FCL `account-proof` service. If a wallet chooses to support this service, and
the user approves the signing of message data, they will return `account-proof` data
and a signature(s) that can be used to prove a user controls an onchain account.

We'll walk through how you, an application developer, can use the `account-proof` service to
authenticate a user.

> Are you an FCL Wallet Developer? Check out the wallet provider specific docs
> [here](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/wallet-provider-spec/provable-authn.md)

### Authenticating a user using `account-proof`[​](#authenticating-a-user-using-account-proof "Direct link to authenticating-a-user-using-account-proof")

In order to authenticate your users via a wallet provider's account-proof service, your application needs to
configure FCL by setting `fcl.accountProof.resolver` and providing two pieces of information.

The `fcl.accountProof.resolver` is an async resolver function used by FCL to retrieve account proof data
from your application server. It can be set in your application configuration under the `fcl.accountProof.resolver`
key. The resolved data should include a random `nonce`.
This data will be sent to the wallet for signing by the user. If the user approves and authentication is successfull,
a signature is returned to the client in the data field of an `account-proof` service.

**Random Nonce**

Your application must provide a **minimum 32-byte random nonce** as a hex string.

If for any reason your application backend does not want to request an `account-proof` during authentication,
it should send a response of `null`. If FCL receives a `null` response from the `accountProof.resolver` it will
continue the authentication process with the wallet but will not request an account-proof and no signature will be returned.

> In the case of a network or server error FCL will cancel the authentication process and return a rejected promise.

`_12

import {config} from "@onflow/fcl"

_12

_12

type AccountProofData {

_12

// e.g. "75f8587e5bd5f9dcc9909d0dae1f0ac5814458b2ae129620502cb936fde7120a" - minimum 32-byte random nonce as hex string

_12

nonce: string;

_12

}

_12

_12

type AccountProofDataResolver = () => Promise<AccountProofData | null>;

_12

_12

config({

_12

"fcl.accountProof.resolver": accountProofDataResolver

_12

})`

Here is the suggested order of operations of how your application might use the
`account-proof` service:

* A user would like to authenticate via your application client using FCL. The process is triggered
  by a call to `fcl.authenticate()`. If `fcl.accountProof.resolver` is configured, FCL will attempt
  to retrieve the account proof data (`nonce`) and trigger your server to start a new
  account proof authentication process.
* Your application server generates a **minimum 32-byte random nonce** using a local source of entropy and
  sends it to the client. The server saves the challenge for future look-ups.
* If FCL successfully retrieves the `account-proof` data, it continues the authentication process over a secure channel with the wallet.
  FCL includes the `appIdentifier` and `nonce` as part of the `FCL:VIEW:READY:RESPONSE` or HTTP POST request body. The `appIdentifier`
  is implicitly generated by FCL and corresponds to the application's [RFC 6454](https://datatracker.ietf.org/doc/html/rfc6454) origin.
  If the resolver function call fails to retrieve the nonce, FCL will cancel the authentication process.
* If the wallet supports account proofs and the user approves authentication with the wallet, the wallet will return the `account-proof`
  service with its response.

The data within the `account-proof` service will look like this:

`_19

{

_19

f_type: "Service", // Its a service!

_19

f_vsn: "1.0.0", // Follows the v1.0.0 spec for the service

_19

type: "account-proof", // The type of service it is

_19

method: "DATA", // Its data!

_19

uid: "awesome-wallet#account-proof", // A unique identifier for the service

_19

data: {

_19

f_type: "account-proof",

_19

f_vsn: "2.0.0"

_19

_19

// The user's address (8 bytes, i.e 16 hex characters)

_19

address: "0xf8d6e0586b0a20c7",

_19

_19

// Nonce signed by the current account-proof (minimum 32 bytes in total, i.e 64 hex characters)

_19

nonce: "75f8587e5bd5f9dcc9909d0dae1f0ac5814458b2ae129620502cb936fde7120a",

_19

_19

signatures: [CompositeSignature],

_19

}

_19

}`

* Your application client initiates a secure channel with your application server
  to relay the `account-proof` data and authenticate the user with your server.
  Subsequent exchanges between the client and server will happen over this channel.
* Your application server receives the `account-proof` data structure, and can then
  begin the verification process.

  + The server checks if the Flow address corresponds to an existing application
    account and determines whether it needs to sign in a returning user or create
    a new account. It is up to your application to decide how to manage
    the two cases.
  + The server looks the challenge up. If the nonce is not found or the nonce
    has expired, reject the authentication request, otherwise continue.
  + The server determines whether the `CompositeSignature` in the
    `account-proof` data structure contains valid signatures for the nonce
    and onchain accounts (more details in the section below on how this is done).
  + If the verification is successful, delete the `nonce` or mark it as expired,
    the application account defined by the onchain address is successfully
    logged in. Otherwise the authentication fails and the `nonce` is not deleted.

**Verification**

Your application can verify the signature against the data from `account-proof`
data using FCL's provided utility:

`_13

_13

import { AppUtils } from "@onflow/fcl"

_13

_13

const accountProofData = {

_13

accountProof.address, // address of the user authenticating

_13

accountProof.nonce, // nonce

_13

accountProof.signatures // signatures

_13

}

_13

_13

const isValid = await AppUtils.verifyAccountProof(

_13

origin,

_13

accountProofData

_13

)`

## Implementation considerations:[​](#implementation-considerations "Direct link to Implementation considerations:")

* The authentication assumes the Flow address is the identifier of the user's application account.
  If an existing user doesn't have a Flow address in their profile, or if they decide to authenticate using
  a Flow address different than the one saved in their profile, the user's account won't be found and the
  process would consider a new user creating an account. It is useful for your application to consider
  other authentication methods that allow an existing user to update the Flow address in their profile so
  they are able to use FCL authentication.
* In the `account-proof` flow as described in this document,
  the backend doesn't know the user's account address at the moment of generating a nonce.
  This results in the nonces not being tied to particular Flow addresses. The backend should
  enforce an expiry window for each nonce to avoid the pool of valid nonces from growing indefinitely.
  Your application is encouraged to implement further mitigations against malicious attempts and
  maintain a scalable authentication process.
* FCL `account-proof` provides functionality to prove a user is in control of
  a Flow address. All other aspects of authentication, authorization and session management
  are up to the application. There are many resources available for setting up secure user
  authentication systems. Application developers should carefully consider what's best for their use
  case and follow industry best practices.
* It is important to use a secure source of entropy to generate the random nonces. The source should insure
  nonces are not predictable by looking at previously generated nonces. Moreover, backend should use its own
  local source and not rely on a publicly available source. Using a nonce of at least 32-bytes insures
  it is extremely unlikely to have a nonce collision.
* The origin / `appIdentifier` is a tuple ⟨scheme, host, port⟩ computed per RFC 6454 (i.e. the value returned
  by window.location.origin in conforming user agents). Wallets will embed this origin into the RLP-encoded payload
  which is cryptographically signed. The resulting signature serves as an attestation that the authentication request
  originated from the specified application origin (which is known through verification with supporting Browser APIs)
* A successful FCL authentication proves the user fully controls a Flow account. This means the user
  controls one or many account keys with weights that add up to the full account weight. The authentication
  would fail if the user doesn't control keys that add up to a full weight.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/proving-authentication.mdx)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)[Next

Scripts](/build/tools/clients/fcl-js/scripts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Proving Ownership of a Flow Account](#proving-ownership-of-a-flow-account)
  + [Authenticating a user using `account-proof`](#authenticating-a-user-using-account-proof)
* [Implementation considerations:](#implementation-considerations)

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
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.