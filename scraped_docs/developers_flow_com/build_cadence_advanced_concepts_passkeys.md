# Source: https://developers.flow.com/build/cadence/advanced-concepts/passkeys

Passkeys | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              - [Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)- [Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions)- [Passkeys](/build/cadence/advanced-concepts/passkeys)- [FLIX (Flow Interaction Templates)](/build/cadence/advanced-concepts/flix)- [NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)- [VRF (Randomness) in Cadence](/build/cadence/advanced-concepts/randomness)- [Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)+ [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Advanced Concepts* Passkeys

On this page

# Passkeys

This is a wallet‑centric, high‑level guide (per [FLIP 264: WebAuthn Credential Support](https://github.com/onflow/flips/blob/cfaaf5f6b7c752e8db770e61ec9c180dc0eb6543/protocol/20250203-webauthn-credential-support.md)) with code snippets covering passkey registration and signing on Flow, focusing on nuances for passkey signing and account keys:

1. Create a passkey and add a Flow account key
2. Sign a transaction with the user's passkey (includes conversion, extension, and submission)

It accompanies the [PoC demo](https://github.com/onflow/passkey-wallet-demo) for reference and cites the FLIP where behavior is normative.

Platform-specific APIs

This tutorial focuses on the **Web Authentication API** (WebAuthn) for browser-based applications. Other platforms such as iOS, Android, and desktop applications will require platform-specific APIs (such as Apple's [Authentication Services](https://developer.apple.com/documentation/authenticationservices,) or Android's [Credential Manager](https://developer.android.com/identity/sign-in/credential-manager)), but the underlying concepts—credential creation, challenge signing, and signature formatting—remain the same across all platforms.

## What you'll learn[​](#what-youll-learn "Direct link to What you'll learn")

After you complete this guide, you'll be able to:

* Create a passkey and derive a Flow‑compatible public key.
* Generate the correct challenge for signing transactions (wallet sets SHA2‑256(signable)).
* Convert a WebAuthn ECDSA DER signature into Flow's raw `r||s` format and attach the transaction signature extension.

## Passkey benefits[​](#passkey-benefits "Direct link to Passkey benefits")

**Sign transactions securely**  
Users can sign Flow transactions with passkeys while the private key stays securely stored within the authenticator. This reduces the risk of key extraction attacks and phishing attempts.

**Authenticate across devices**  
Users can scan a QR code displayed on a desktop browser with a mobile device to approve transactions. Cloud-synchronized passkeys (such as those stored in Apple iCloud or Google Password Manager) allow authentication across multiple devices without manual key transfers.

**Authenticate with platform-based security**  
Users can sign transactions directly on devices with built-in authenticators, such as Face ID on iPhones or Windows Hello on Windows PCs. This approach allows native transaction signing without the need for an external security key.

**Recover access with cloud-synced passkeys**  
Cloud-synced passkeys help users recover access if they lose a device, though this introduces trade-offs between convenience and self-custody (see [Limitations of passkeys](#limitations-of-passkeys).

**Work with multi-key accounts**  
Combine passkeys with other authentication types with Flow's native [multi-key account support](/build/cadence/basics/accounts#account-keys) to build secure recovery options and shared access patterns with weighted keys.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Working knowledge of modern frontend (React/Next.js) and basic backend.
* Familiarity with WebAuthn/Passkeys concepts and platform constraints.
* Flow Command Line (FCL) installed and configured for your app.
* Flow accounts and keys: [Signature and Hash Algorithms](/build/cadence/basics/accounts).

## Registration[​](#registration "Direct link to Registration")

When a user generates a passkey via [navigator.credentials.create()](https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer/create) with `{ publicKey }`, the authenticator returns an attestation that contains the new credential's public key. On Flow, you can register that public key on an account if the algorithm of the requested passkey is either `ES256` or `ES256k`. This guide demonstrates an `ES256` passkey which translates to an `ECDSA_P256` Flow key paired with `SHA2_256` hashing. Alternatively, an `ES256k` passkey translates to an `ECDSA_secp256k1` Flow key paired with `SHA2_256` hashing.

High‑level steps:

1. On the client, generate `PublicKeyCredentialCreationOptions` with:

* `pubKeyCredParams`'s `alg` equal to `ES256` (`-7`)
* the RP id is derived from to the web origin
* the challenge equal to an arbitrary constant

2. On the client, call `navigator.credentials.create()`.
3. Verify attestation if necessary and extract the public key (P‑256 in this guide). Convert it to raw uncompressed 64‑byte `X||Y` hex string as expected by Flow.
4. Submit a transaction to add the key to the Flow account with weight and algorithms:
   * Signature algorithm: `ECDSA_P256`
   * Hash algorithm: `SHA2_256`

info

Libraries like SimpleWebAuthn can parse the COSE key and produce the raw public key bytes required for onchain registration. Ensure you normalize into the exact raw byte format Flow expects before it writes to the account key.

### Build creation options and create credential[​](#build-creation-options-and-create-credential "Direct link to Build creation options and create credential")

Minimum example — wallet‑mode registration:

This builds `PublicKeyCredentialCreationOptions` for a wallet RP with a constant registration challenge and ES256 (P‑256) so you can register the newly-created public key on a Flow account.

`_28

// In a wallet (RP = wallet origin). The challenge satisfies API & correlates request/response.

_28

// Use a stable, opaque user.id per wallet user (do not randomize per request).

_28

_28

const rp = { name: "Passkey Wallet", id: window.location.hostname } as const

_28

const user = {

_28

id: getStableUserIdBytes(), // Uint8Array (16–64 bytes) stable per user

_28

name: "flow-user",

_28

displayName: "Flow User",

_28

} as const

_28

_28

const creationOptions: PublicKeyCredentialCreationOptions = {

_28

challenge: new TextEncoder().encode("flow-wallet-register"), // constant is acceptable in wallet-mode; wallet providers may choose and use a constant value as needed for correlation

_28

rp,

_28

user,

_28

pubKeyCredParams: [

_28

{ type: "public-key", alg: -7 }, // ES256 (ECDSA on P-256 with SHA-256)

_28

// Optionally ES256K (ECDSA on secp256k1 with SHA-256) if the device supports secp256k1 keys:

_28

// { type: "public-key", alg: -47 },

_28

],

_28

authenticatorSelection: { userVerification: "preferred" },

_28

timeout: 60_000,

_28

attestation: "none",

_28

}

_28

_28

const credential = await navigator.credentials.create({ publicKey: creationOptions })

_28

_28

// Send to wallet-core (or local) to extract COSE ECDSA P-256 public key (verify attestation if necessary)

_28

// Then register the raw uncompressed key bytes on the Flow account as ECDSA_P256/SHA2_256 (this guide's choice)`

RP ID for non-browser platforms

For web applications, `rpId` is set to `window.location.hostname`. For native mobile and desktop applications, use your app's identifier instead:

* **iOS**: Use your app's bundle identifier (such as `com.example.wallet`) or an associated domain.
* **Android**: Use your app's package name (such as `com.example.wallet`) or an associated domain.
* **Desktop**: Use your application identifier or registered domain.

The `rpId` should remain consistent across credential creation and assertion for the same user account. However, Flow does not validate or enforce this consistency.

### Extract and normalize public key[​](#extract-and-normalize-public-key "Direct link to Extract and normalize public key")

Client-side example — extract COSE ECDSA public key (no verification) and derive raw uncompressed 64-byte `X||Y` hex suitable for Flow key registration:

This parses the `attestationObject` to locate the COSE EC2 `credentialPublicKey`, reads the x/y coordinates, and returns raw uncompressed 64-byte `X||Y` hex suitable for Flow key registration. Attestation verification is intentionally omitted here.

`_44

// Uses a small CBOR decoder (e.g., 'cbor' or 'cbor-x') to parse attestationObject

_44

import * as CBOR from 'cbor'

_44

_44

function toHex(bytes: Uint8Array): string {

_44

return Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('')

_44

}

_44

_44

function extractCosePublicKeyFromAttestation(attObj: Uint8Array): Uint8Array {

_44

// attestationObject is a CBOR map with 'authData'

_44

const decoded: any = CBOR.decode(attObj)

_44

const authData = new Uint8Array(decoded.authData)

_44

_44

// Parse authData (WebAuthn spec):

_44

// rpIdHash(32) + flags(1) + signCount(4) = 37 bytes header

_44

let offset = 37

_44

// aaguid (16)

_44

offset += 16

_44

// credentialId length (2 bytes, big-endian)

_44

const credIdLen = (authData[offset] << 8) | authData[offset + 1]

_44

offset += 2

_44

// credentialId (credIdLen bytes)

_44

offset += credIdLen

_44

// The next CBOR structure is the credentialPublicKey (COSE key)

_44

return authData.slice(offset)

_44

}

_44

_44

function coseEcP256ToUncompressedXYHex(coseKey: Uint8Array): string {

_44

// COSE EC2 key is a CBOR map; for P-256, x = -2, y = -3

_44

const m: Map<number, any> = CBOR.decode(coseKey)

_44

const x = new Uint8Array(m.get(-2))

_44

const y = new Uint8Array(m.get(-3))

_44

if (x.length > 32 || y.length > 32) throw new Error('Invalid P-256 coordinate lengths')

_44

const xy = new Uint8Array(64)

_44

xy.set(x, 32 - x.length)

_44

xy.set(y, 64 - y.length)

_44

return toHex(xy) // 64-byte X||Y hex, no 0x or 0x04 prefix

_44

}

_44

_44

// Usage

_44

const cred = (await navigator.credentials.create({ publicKey: creationOptions })) as PublicKeyCredential

_44

const att = cred.response as AuthenticatorAttestationResponse

_44

const attObj = new Uint8Array(att.attestationObject as ArrayBuffer)

_44

const cosePubKey = extractCosePublicKeyFromAttestation(attObj)

_44

const publicKeyHex = coseEcP256ToUncompressedXYHex(cosePubKey)`

### Add key to account[​](#add-key-to-account "Direct link to Add key to account")

Now that you have the user's public key, provision a Flow account with that key. Account creation (or to add key to an account) requires payment. In practice, account instantiation typically occurs on the wallet provider's backend service.

In the PoC demo, we used a test API to provision an account with the public key:

`` _22

const ACCOUNT_API = "https://wallet.example.com/api/accounts/provision"

_22

_22

export async function createAccountWithPublicKey(

_22

publicKeyHex: string,

_22

_opts?: {signAlgo?: number; hashAlgo?: number; weight?: number}

_22

): Promise<string> {

_22

const trimmed = publicKeyHex

_22

const body: ProvisionAccountRequest = {

_22

publicKey: trimmed,

_22

signatureAlgorithm: "ECDSA_P256",

_22

hashAlgorithm: "SHA2_256",

_22

}

_22

const res = await fetch(ACCOUNT_API, {

_22

method: "POST",

_22

headers: {Accept: "application/json", "Content-Type": "application/json"},

_22

body: JSON.stringify(body),

_22

})

_22

if (!res.ok) throw new Error(`Account API error: ${res.status}`)

_22

const json = (await res.json()) as ProvisionAccountResponse

_22

if (!json?.address) throw new Error("Account API missing address in response")

_22

return json.address

_22

} ``

note

In production, this would be a service owned by the wallet provider that creates the account and attaches the user's public key, for reasons like payment handling, abuse prevention, telemetry, and correlation as needed.

## Signing[​](#signing "Direct link to Signing")

### Generate the challenge[​](#generate-the-challenge "Direct link to Generate the challenge")

* Assertion (transaction signing): Wallet sets `challenge` to the SHA2‑256 of the signable transaction message (payload or envelope per signer role). No server‑sent or random challenge is used. Flow includes a domain‑separation tag in the signable bytes.

Minimal example — derive signable message and hash (per FLIP):

Compute the signer‑specific signable message and hash it with SHA2‑256 to produce the WebAuthn `challenge` (no server‑generated nonce is used in wallet mode).

`_23

// Imports for helpers used to build the signable message

_23

import { encodeMessageFromSignable, encodeTransactionPayload } from '@onflow/fcl'

_23

// Hash/encoding utilities (example libs)

_23

import { sha256 } from '@noble/hashes/sha256'

_23

import { hexToBytes } from '@noble/hashes/utils'

_23

_23

// Inputs:

_23

// - signable: object containing the voucher/payload bytes (e.g., from a ready payload)

_23

// - address: the signing account address (hex string)

_23

_23

declare const signable: any

_23

declare const address: string

_23

_23

// 1) Encode the signable message for this signer (payload vs envelope)

_23

const msgHex = encodeMessageFromSignable(signable, address)

_23

const payloadMsgHex = encodeTransactionPayload(signable.voucher)

_23

const role = msgHex === payloadMsgHex ? "payload" : "envelope"

_23

_23

// 2) Compute SHA2-256(msgHex) -> 32-byte challenge

_23

const signableHash: Uint8Array = sha256(hexToBytes(msgHex))

_23

_23

// 3) Call navigator.credentials.get with challenge = signableHash

_23

// (see next subsection for a full getAssertion example)`

info

`encodeMessageFromSignable` and `encodeTransactionPayload` are FCL‑specific helpers. If you don't use FCL, construct the Flow signable transaction message yourself (payload for proposer/authorizer, envelope for payer, prepended by the transaction domain tag), then compute `SHA2‑256(messageBytes)` for the challenge. The payload encoding shown here applies regardless of wallet implementation; the helper calls are simply conveniences from FCL.

### Request assertion[​](#request-assertion "Direct link to Request assertion")

Minimal example — wallet assertion:

Build [PublicKeyCredentialRequestOptions](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredentialRequestOptions) and request an assertion with the transaction hash as `challenge`. `rpId` must match the wallet domain. When the wallet has mapped the active account to a credential, include `allowCredentials` with that credential ID to avoid extra prompts. You can omit it, which is permissible for discoverable credentials. You will invoke [navigator.credentials.get()](https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer/get).

`_23

// signableHash is SHA2-256(signable message: payload or envelope)

_23

declare const signableHash: Uint8Array

_23

declare const credentialId: Uint8Array // Credential ID for the active account (from prior auth)

_23

_23

const requestOptions: PublicKeyCredentialRequestOptions = {

_23

challenge: signableHash,

_23

rpId: window.location.hostname,

_23

userVerification: "preferred",

_23

timeout: 60_000,

_23

allowCredentials: [

_23

{

_23

type: "public-key",

_23

id: credentialId,

_23

},

_23

],

_23

}

_23

_23

const assertion = (await navigator.credentials.get({

_23

publicKey: requestOptions,

_23

})) as PublicKeyCredential

_23

_23

const { authenticatorData, clientDataJSON, signature } =

_23

assertion.response as AuthenticatorAssertionResponse`

info

* **Credential selection**: Wallets typically know which credential corresponds to the user's active account (selected during authentication/authorization), so they should pass that credential via `allowCredentials` to scope selection and minimize prompts. For discoverable credentials, you can omit `allowCredentials`, which lets the authenticator surface available credentials. See [WebAuthn specifications](https://www.w3.org/TR/webauthn-3) for guidance.
* **RP ID consistency**: The `rpId` used here should match what was used during credential creation. However, Flow does not validate or enforce this (transactions would still pass even if different). For non-browser platforms, use the same app identifier (bundle ID, package name, and so on.) as in registration.

### Convert and attach signature[​](#convert-and-attach-signature "Direct link to Convert and attach signature")

WebAuthn assertion signatures in this guide are ECDSA P‑256 over SHA‑256 and are typically returned in ASN.1/DER form. Flow expects raw 64‑byte signatures: `r` and `s` each 32 bytes, concatenated (`r || s`).

* Convert the DER `signature` to Flow raw `r||s` (64 bytes) and attach with `addr` and `keyId`.
* Build the transaction signature extension as specified: `extension_data = 0x01 || RLP([authenticatorData, clientDataJSON])`.

Minimal example — convert and attach for submission:

Convert the DER signature to Flow raw `r||s` and build `signatureExtension = 0x01 || RLP([authenticatorData, clientDataJSON])` per the FLIP, then compose the Flow transaction signature object for inclusion in your transaction.

`_27

import { encode as rlpEncode } from 'rlp'

_27

import { bytesToHex } from '@noble/hashes/utils'

_27

_27

// Inputs from previous steps

_27

declare const address: string // 0x-prefixed Flow address

_27

declare const keyId: number // Account key index used for signing

_27

declare const signature: Uint8Array // DER signature from WebAuthn assertion

_27

declare const clientDataJSON: Uint8Array

_27

declare const authenticatorData: Uint8Array

_27

_27

// 1) DER -> raw r||s (64 bytes), implementation below or similar

_27

const rawSig = derToRawRS(signature)

_27

_27

// 2) Build extension_data per FLIP: 0x01 || RLP([authenticatorData, clientDataJSON])

_27

const rlpPayload = rlpEncode([authenticatorData, clientDataJSON]) as Uint8Array | Buffer

_27

const rlpBytes = rlpPayload instanceof Uint8Array ? rlpPayload : new Uint8Array(rlpPayload)

_27

const extension_data = new Uint8Array(1 + rlpBytes.length)

_27

extension_data[0] = 0x01

_27

extension_data.set(rlpBytes, 1)

_27

_27

// 3) Compose Flow signature object

_27

const flowSignature = {

_27

addr: address, // e.g., '0x1cf0e2f2f715450'

_27

keyId, // integer key index

_27

signature: '0x' + bytesToHex(rawSig),

_27

signatureExtension: extension_data,

_27

}`

#### Submit the signature[​](#submit-the-signature "Direct link to Submit the signature")

Return the signature data to the application that initiated signing. The application should attach it to the user transaction for the signer (`addr`, `keyId`) and submit the transaction to the network.

See [Transactions](/build/cadence/basics/transactions) for how signatures are attached per signer role (payload vs envelope) and how submissions are finalized.

#### Helper: derToRawRS[​](#helper-dertorawrs "Direct link to Helper: derToRawRS")

`_38

// Minimal DER ECDSA (r,s) -> raw 64-byte r||s

_38

function derToRawRS(der: Uint8Array): Uint8Array {

_38

let offset = 0

_38

if (der[offset++] !== 0x30) throw new Error("Invalid DER sequence")

_38

const seqLen = der[offset++] // assumes short form

_38

if (seqLen + 2 !== der.length) throw new Error("Invalid DER length")

_38

_38

if (der[offset++] !== 0x02) throw new Error("Missing r INTEGER")

_38

const rLen = der[offset++]

_38

let r = der.slice(offset, offset + rLen)

_38

offset += rLen

_38

if (der[offset++] !== 0x02) throw new Error("Missing s INTEGER")

_38

const sLen = der[offset++]

_38

let s = der.slice(offset, offset + sLen)

_38

_38

// Strip leading zeros and left-pad to 32 bytes

_38

r = stripLeadingZeros(r)

_38

s = stripLeadingZeros(s)

_38

const r32 = leftPad32(r)

_38

const s32 = leftPad32(s)

_38

const raw = new Uint8Array(64)

_38

raw.set(r32, 0)

_38

raw.set(s32, 32)

_38

return raw

_38

}

_38

_38

function stripLeadingZeros(bytes: Uint8Array): Uint8Array {

_38

let i = 0

_38

while (i < bytes.length - 1 && bytes[i] === 0x00) i++

_38

return bytes.slice(i)

_38

}

_38

_38

function leftPad32(bytes: Uint8Array): Uint8Array {

_38

if (bytes.length > 32) throw new Error("Component too long")

_38

const out = new Uint8Array(32)

_38

out.set(bytes, 32 - bytes.length)

_38

return out

_38

}`

## Notes from the PoC[​](#notes-from-the-poc "Direct link to Notes from the PoC")

* The [PoC demo](https://github.com/onflow/passkey-wallet-demo) demonstrates reference flows for passkey creation and assertion, such as:
  + Extract and normalize the ECDSA P‑256 public key for Flow.
  + Build the correct challenge .
  + Convert DER signatures to raw `r||s`.
  + Package WebAuthn fields as signature extension data.

> Align your implementation with the FLIP to ensure your extension payloads and verification logic match network expectations.

## Security and UX considerations[​](#security-and-ux-considerations "Direct link to Security and UX considerations")

* Use `ES256` or `ES256k` as algorithms to create Flow account compatible keys.
* Clearly communicate platform prompts and recovery paths; passkeys UX can differ across OS/browsers.
* Replay protection: Flow uses on‑chain proposal‑key sequence numbers; see [Replay attacks](https://github.com/onflow/flips/blob/cfaaf5f6b7c752e8db770e61ec9c180dc0eb6543/protocol/20250203-webauthn-credential-support.md#replay-attacks).
* Optional wallet backend: store short‑lived correlation data or rate‑limits as needed (not required).

## Limitations of passkeys[​](#limitations-of-passkeys "Direct link to Limitations of passkeys")

**Functionality varies by authenticator**  
Some security keys do not support biometric authentication, which requires users to enter a PIN instead. Because WebAuthn does not provide access to private keys, users must either store their passkey securely or turn on cloud synchronization for recovery.

**Cloud synchronization introduces risks**  
Cloud-synced passkeys improve accessibility but also create risks if a cloud provider is compromised or if a user loses access to their cloud account. Users who prefer full self-custody can use hardware-based passkeys that do not rely on cloud synchronization.

**Passkeys cannot be exported**  
Users cannot transfer a passkey between different authenticators. For example, a passkey created on a security key cannot move to another device unless it syncs through a cloud provider. To avoid losing access, users should set up authentication on multiple devices or combine passkeys with [multi-key account configurations](/build/cadence/basics/accounts#account-keys) for additional recovery options.

## Credential management (wallet responsibilities)[​](#credential-management-wallet-responsibilities "Direct link to Credential management (wallet responsibilities)")

Wallet providers should persist credential metadata to support seamless signing, rotation, and recovery:

* Map `credentialId` ↔ Flow `addr` (and `keyId`) for the active account.
* Store `rpId`, user handle, and (optionally) `aaguid`/attestation info for risk decisions.
* Support multiple credentials per account and revocation/rotation workflows.
* Enforce nonce/sequence semantics and rate limits server-side as needed.

See [WebAuthn Credential Support (FLIP)](https://github.com/onflow/flips/blob/cfaaf5f6b7c752e8db770e61ec9c180dc0eb6543/protocol/20250203-webauthn-credential-support.md) for rationale and wallet‑mode guidance.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you integrated passkeys (WebAuthn) with Flow for both registration and signing.

Now that you have completed the tutorial, you should be able to:

* Create a WebAuthn credential and derive a Flow‑compatible public key.
* Generate the correct challenge for signing transactions (wallet sets SHA2‑256(signable)).
* Convert a WebAuthn ECDSA DER signature into Flow's raw `r||s` format and attach the transaction signature extension.

### Further reading[​](#further-reading "Direct link to Further reading")

* Review signing flows and roles: [Transactions](/build/cadence/basics/transactions)
* Account keys: [Signature and Hash Algorithms](/build/cadence/basics/accounts)
* Web Authentication API (MDN): [Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API)
* Flow Client Library (FCL): [Flow Client Library](/build/tools/clients/fcl-js)
* Wallet Provider Spec: [Wallet Provider Spec](/build/tools/wallet-provider-spec)
* Track updates: [FLIP 264: WebAuthn Credential Support](https://github.com/onflow/flips/blob/cfaaf5f6b7c752e8db770e61ec9c180dc0eb6543/protocol/20250203-webauthn-credential-support.md)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/advanced-concepts/passkeys.md)

Last updated on **Dec 1, 2025** by **cshannon1218**

[Previous

Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions)[Next

FLIX (Flow Interaction Templates)](/build/cadence/advanced-concepts/flix)

###### Rate this page

😞😐😊

Copy as Markdown

* [What you'll learn](#what-youll-learn)* [Passkey benefits](#passkey-benefits)* [Prerequisites](#prerequisites)* [Registration](#registration)
        + [Build creation options and create credential](#build-creation-options-and-create-credential)+ [Extract and normalize public key](#extract-and-normalize-public-key)+ [Add key to account](#add-key-to-account)* [Signing](#signing)
          + [Generate the challenge](#generate-the-challenge)+ [Request assertion](#request-assertion)+ [Convert and attach signature](#convert-and-attach-signature)* [Notes from the PoC](#notes-from-the-poc)* [Security and UX considerations](#security-and-ux-considerations)* [Limitations of passkeys](#limitations-of-passkeys)* [Credential management (wallet responsibilities)](#credential-management-wallet-responsibilities)* [Conclusion](#conclusion)
                    + [Further reading](#further-reading)

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