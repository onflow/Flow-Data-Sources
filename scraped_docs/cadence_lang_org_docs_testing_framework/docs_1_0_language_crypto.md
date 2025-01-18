# Source: https://cadence-lang.org/docs/1.0/language/crypto




Crypto | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
  + [Syntax](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Type Annotations](/docs/language/type-annotations)
  + [Values and Types](/docs/language/values-and-types)
  + [Operators](/docs/language/operators)
  + [Functions](/docs/language/functions)
  + [Control Flow](/docs/language/control-flow)
  + [Scope](/docs/language/scope)
  + [Type Safety](/docs/language/type-safety)
  + [Type Inference](/docs/language/type-inference)
  + [Composite Types](/docs/language/composite-types)
  + [Resources](/docs/language/resources)
  + [Access control](/docs/language/access-control)
  + [Capabilities](/docs/language/capabilities)
  + [Interfaces](/docs/language/interfaces)
  + [Enumerations](/docs/language/enumerations)
  + [Intersection Types](/docs/language/intersection-types)
  + [References](/docs/language/references)
  + [Imports](/docs/language/imports)
  + [Accounts](/docs/language/accounts/)
  + [Attachments](/docs/language/attachments)
  + [Contracts](/docs/language/contracts)
  + [Contract Updatability](/docs/language/contract-updatability)
  + [Transactions](/docs/language/transactions)
  + [Events](/docs/language/events)
  + [Core Events](/docs/language/core-events)
  + [Run-time Types](/docs/language/run-time-types)
  + [Built-in Functions](/docs/language/built-in-functions)
  + [Environment Information](/docs/language/environment-information)
  + [Crypto](/docs/language/crypto)
  + [Type Hierarchy](/docs/language/type-hierarchy)
  + [Glossary](/docs/language/glossary)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Crypto
On this page
# Crypto

## Hash algorithms[​](#hash-algorithms "Direct link to Hash algorithms")

The built-in [enumeration](/docs/language/enumerations) `HashAlgorithm`
provides the set of supported hashing algorithms.

 `_41access(all)_41enum HashAlgorithm: UInt8 {_41 /// SHA2_256 is SHA-2 with a 256-bit digest (also referred to as SHA256)._41 access(all)_41 case SHA2_256 = 1_41_41 /// SHA2_384 is SHA-2 with a 384-bit digest (also referred to as SHA384)._41 access(all)_41 case SHA2_384 = 2_41_41 /// SHA3_256 is SHA-3 with a 256-bit digest._41 access(all)_41 case SHA3_256 = 3_41_41 /// SHA3_384 is SHA-3 with a 384-bit digest._41 access(all)_41 case SHA3_384 = 4_41_41 /// KMAC128_BLS_BLS12_381 is an instance of KECCAK Message Authentication Code (KMAC128) mac algorithm._41 /// Although this is a MAC algorithm, KMAC is included in this list as it can be used hash_41 /// when the key is used a non-public customizer._41 /// KMAC128_BLS_BLS12_381 is used in particular as the hashing algorithm for the BLS signature scheme on the curve BLS12-381._41 /// It is a customized version of KMAC128 that is compatible with the hashing to curve_41 /// used in BLS signatures._41 /// It is the same hasher used by signatures in the internal Flow protocol._41 access(all)_41 case KMAC128_BLS_BLS12_381 = 5_41_41 /// KECCAK_256 is the legacy Keccak algorithm with a 256-bits digest, as per the original submission to the NIST SHA3 competition._41 /// KECCAK_256 is different than SHA3 and is used by Ethereum._41 access(all)_41 case KECCAK_256 = 6_41_41 /// Returns the hash of the given data_41 access(all)_41 view fun hash(_ data: [UInt8]): [UInt8]_41_41 /// Returns the hash of the given data and tag_41 access(all)_41 view fun hashWithTag(_ data: [UInt8], tag: string): [UInt8]_41}`

The hash algorithms provide two ways to hash input data into digests, `hash` and `hashWithTag`.

## Hashing[​](#hashing "Direct link to Hashing")

`hash` hashes the input data using the chosen hashing algorithm.
`KMAC` is the only MAC algorithm on the list
and configured with specific parameters (detailed in [KMAC128 for BLS](#KMAC128-for-BLS))

For example, to compute a SHA3-256 digest:

 `_10let data: [UInt8] = [1, 2, 3]_10let digest = HashAlgorithm.SHA3_256.hash(data)`
## Hashing with a domain tag[​](#hashing-with-a-domain-tag "Direct link to Hashing with a domain tag")

`hashWithTag` hashes the input data along with an input tag.
It allows instantiating independent hashing functions customized with a domain separation tag (DST).
For most of the hashing algorithms, mixing the data with the tag is done by pre-fixing the data with the tag and
hashing the result.

* `SHA2_256`, `SHA2_384`, `SHA3_256`, `SHA3_384`, `KECCAK_256`:
  If the tag is non-empty, the hashed message is `bytes(tag) || data` where `bytes()` is the UTF-8 encoding of the input string,
  padded with zeros till 32 bytes.
  Therefore tags must not exceed 32 bytes.
  If the tag used is empty, no data prefix is applied, and the hashed message is simply `data` (same as `hash` output).
* `KMAC128_BLS_BLS12_381`: refer to [KMAC128 for BLS](#KMAC128-for-BLS) for details.

### KMAC128 for BLS[​](#kmac128-for-bls "Direct link to KMAC128 for BLS")

`KMAC128_BLS_BLS12_381` is an instance of the cSHAKE-based KMAC128.
Although this is a MAC algorithm, KMAC can be used as a hash when the key is used as a non-private customizer.
`KMAC128_BLS_BLS12_381` is used in particular as the hashing algorithm for the BLS signature scheme on the curve BLS12-381.
It is a customized instance of KMAC128 and is compatible with the hashing to curve used by BLS signatures.
It is the same hasher used by the internal Flow protocol, and can be used to verify Flow protocol signatures on Cadence.

To define the MAC instance, `KMAC128(customizer, key, data, length)` is instantiated with the following parameters
(as referred to by the NIST [SHA-3 Derived Functions](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-185.pdf)):

* `customizer` is the UTF-8 encoding of `"H2C"`.
* `key` is the UTF-8 encoding of `"FLOW--V00-CS00-with-BLS_SIG_BLS12381G1_XOF:KMAC128_SSWU_RO_POP_"` when `hash` is used. It includes the input `tag`
  when `hashWithTag` is used and key becomes the UTF-8 encoding of `"FLOW-" || tag || "-V00-CS00-with-BLS_SIG_BLS12381G1_XOF:KMAC128_SSWU_RO_POP_"`.
* `data` is the input data to hash.
* `length` is 1024 bytes.

## Signature algorithms[​](#signature-algorithms "Direct link to Signature algorithms")

The built-in [enumeration](/docs/language/enumerations) `SignatureAlgorithm`
provides the set of supported signature algorithms.

 `_16access(all)_16enum SignatureAlgorithm: UInt8 {_16 /// ECDSA_P256 is ECDSA on the NIST P-256 curve._16 access(all)_16 case ECDSA_P256 = 1_16_16 /// ECDSA_secp256k1 is ECDSA on the secp256k1 curve._16 access(all)_16 case ECDSA_secp256k1 = 2_16_16 /// BLS_BLS12_381 is BLS signature scheme on the BLS12-381 curve._16 /// The scheme is set-up so that signatures are in G_1 (subgroup of the curve over the prime field)_16 /// while public keys are in G_2 (subgroup of the curve over the prime field extension)._16 access(all)_16 case BLS_BLS12_381 = 3_16}`
## Public keys[​](#public-keys "Direct link to Public keys")

`PublicKey` is a built-in structure that represents a cryptographic public key of a signature scheme.

 `_30access(all)_30struct PublicKey {_30_30 access(all)_30 let publicKey: [UInt8]_30_30 access(all)_30 let signatureAlgorithm: SignatureAlgorithm_30_30 /// Verifies a signature under the given tag, data and public key._30 /// It uses the given hash algorithm to hash the tag and data._30 access(all)_30 view fun verify(_30 signature: [UInt8],_30 signedData: [UInt8],_30 domainSeparationTag: String,_30 hashAlgorithm: HashAlgorithm_30 ): Bool_30_30 /// Verifies the proof of possession of the private key._30 /// This function is only implemented if the signature algorithm_30 /// of the public key is BLS (BLS_BLS12_381)._30 /// If called with any other signature algorithm, the program aborts_30 access(all)_30 view fun verifyPoP(_ proof: [UInt8]): Bool_30_30 // creating a PublicKey is a view operation_30 access(all)_30 view init()_30}`

`PublicKey` supports two methods `verify` and `verifyPoP`.
`verify` is the [signature verification](#signature-verification) function, while `verifyPoP` is covered under [BLS multi-signature](#proof-of-possession-pop).

### Public Key construction[​](#public-key-construction "Direct link to Public Key construction")

A `PublicKey` can be constructed using the raw key and the signing algorithm.

 `_10let publicKey = PublicKey(_10 publicKey: "010203".decodeHex(),_10 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_10)`

The raw key value depends on the supported signature scheme:

* `ECDSA_P256` and `ECDSA_secp256k1`:
  The public key is an uncompressed curve point `(X,Y)` where `X` and `Y` are two prime field elements.
  The raw key is represented as `bytes(X) || bytes(Y)`, where `||` is the concatenation operation,
  and `bytes()` is the bytes big-endian encoding left padded by zeros to the byte-length of the field prime.
  The raw public key is 64-bytes long.
* `BLS_BLS_12_381`:
  The public key is a G\_2 element (on the curve over the prime field extension).
  The encoding follows the compressed serialization defined in the
  [IETF draft-irtf-cfrg-pairing-friendly-curves-08](https://www.ietf.org/archive/id/draft-irtf-cfrg-pairing-friendly-curves-08.html#name-point-serialization-procedu).
  A public key is 96-bytes long.

### Public Key validation[​](#public-key-validation "Direct link to Public Key validation")

A public key is validated at the time of creation. Only valid public keys can be created.
The validation of the public key depends on the supported signature scheme:

* `ECDSA_P256` and `ECDSA_secp256k1`:
  The given `X` and `Y` coordinates are correctly serialized, represent valid prime field elements, and the resulting
  point is on the correct curve (no subgroup check needed since the cofactor of both supported curves is 1).
* `BLS_BLS_12_381`:
  The given key is correctly serialized following the compressed serialization in [IETF draft-irtf-cfrg-pairing-friendly-curves-08](https://www.ietf.org/archive/id/draft-irtf-cfrg-pairing-friendly-curves-08.html#name-point-serialization-procedu).
  The coordinates represent valid prime field extension elements. The resulting point is on the curve, and is on the correct subgroup G\_2.
  Note that the point at infinity is accepted and yields the identity public key. Such identity key can be useful when aggregating multiple keys.

Since the validation happens only at the time of creation, public keys are immutable.

 `_10publicKey.signatureAlgorithm = SignatureAlgorithm.ECDSA_secp256k1 // Not allowed_10publicKey.publicKey = [] // Not allowed_10_10publicKey.publicKey[2] = 4 // No effect`

Invalid public keys cannot be constructed so public keys are always valid.

### Signature verification[​](#signature-verification "Direct link to Signature verification")

A signature can be verified using the `verify` function of the `PublicKey`:

 `_15let pk = PublicKey(_15 publicKey: "96142CE0C5ECD869DC88C8960E286AF1CE1B29F329BA4964213934731E65A1DE480FD43EF123B9633F0A90434C6ACE0A98BB9A999231DB3F477F9D3623A6A4ED".decodeHex(),_15 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_15)_15_15let signature = "108EF718F153CFDC516D8040ABF2C8CC7AECF37C6F6EF357C31DFE1F7AC79C9D0145D1A2F08A48F1A2489A84C725D6A7AB3E842D9DC5F8FE8E659FFF5982310D".decodeHex()_15let message : [UInt8] = [1, 2, 3]_15_15let isValid = pk.verify(_15 signature: signature,_15 signedData: message,_15 domainSeparationTag: "",_15 hashAlgorithm: HashAlgorithm.SHA2_256_15)_15// `isValid` is false`

The inputs to `verify` depend on the signature scheme used:

* ECDSA (`ECDSA_P256` and `ECDSA_secp256k1`):
  + `signature` expects the couple `(r,s)`. It is serialized as `bytes(r) || bytes(s)`, where `||` is the concatenation operation,
    and `bytes()` is the bytes big-endian encoding left padded by zeros to the byte-length of the curve order.
    The signature is 64 bytes-long for both curves.
  + `signedData` is the arbitrary message to verify the signature against.
  + `domainSeparationTag` is the expected domain tag, i.e, the value that a correctly generated signature is expected to use.
    The domain tag prefixes the message during the signature generation or verification before the hashing step (more details in [`hashWithTag`](#hashing-with-a-domain-tag)).
    The tag's purpose is to separate different contexts or domains so that a signature can't be re-used for a different context other than its original one.
    An application should define its own arbitrary domain tag value to distance its user's signatures from other applications.
    The application tag should be enforced for valid signature generations and verifications.
    Check [Hashing with a domain tag](#hashing-with-a-domain-tag) for requirements on the string value.
  + `hashAlgorithm` is either `SHA2_256`, `SHA3_256` or `KECCAK_256`. It is the algorithm used to hash the message along with the given tag (check [hashing with a tag](#hashing-with-a-domain-tag)).

As noted in [`hashWithTag`](#hashing-with-a-domain-tag) for `SHA2_256`, `SHA3_256` and `KECCAK_256`, using an empty `tag` results in hashing the input data only. If a signature verification
needs to be computed against data without any domain tag, an empty domain tag `""` should be passed.

ECDSA verification is implemented as defined in ANS X9.62 (also referred by [FIPS 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf) and [SEC 1, Version 2.0](https://www.secg.org/sec1-v2.pdf)).
A valid signature would be generated using the expected `signedData`, `domainSeparationTag` and `hashAlgorithm` used to verify.

* BLS (`BLS_BLS_12_381`):
  + `signature` expects a G\_1 point (on the curve over the prime field).
    The encoding follows the compressed serialization defined in the [IETF draft-irtf-cfrg-pairing-friendly-curves-08](https://www.ietf.org/archive/id/draft-irtf-cfrg-pairing-friendly-curves-08.html#name-point-serialization-procedu).
    A signature is 48-bytes long.
  + `signedData` is the arbitrary message to verify the signature against.
  + `domainSeparationTag` is the expected domain tag, i.e, the value that a correctly generated signature is expected to use.
    The domain tag is mixed with the message during the signature generation or verification as specified in [KMAC128 for BLS](#KMAC128-for-BLS).
    The tag's purpose is to separate different contexts or domains so that a signature can't be re-used for a different context other than its original one.
    An application should define its own arbitrary domain tag value to distance its user's signatures from other applications.
    The application tag should be enforced for valid signature generations and verifications.
    All string values are valid as tags in BLS (check [KMAC128 for BLS](#KMAC128-for-BLS)).
  + `hashAlgorithm` only accepts `KMAC128_BLS_BLS12_381`. It is the algorithm used to hash the message along with the given tag (check [KMAC128 for BLS](#KMAC128-for-BLS)).

BLS verification performs the necessary membership check on the signature while the membership check of the public key is performed at the creation of the `PublicKey` object
and is not repeated during the signature verification.
In order to prevent equivocation issues, a verification under the identity public key always returns `false`.

The verification uses a hash-to-curve algorithm to hash the `signedData` into a `G_1` point, following the `hash_to_curve` method described in [draft-irtf-cfrg-hash-to-curve-14](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-hash-to-curve-14#section-3).
While KMAC128 is used as a hash-to-field method resulting in two field elements, the mapping to curve is implemented using the [simplified SWU](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-hash-to-curve-14#section-6.6.3).

A valid signature should be generated using the expected `signedData` and `domainSeparationTag`, as well the same hashing to curve process.

## BLS multi-signature[​](#bls-multi-signature "Direct link to BLS multi-signature")

BLS signature scheme allows efficient multi-signature features. Multiple signatures can be aggregated
into a single signature which can be verified against an aggregated public key. This allows authenticating
multiple signers with a single signature verification.
While BLS provides multiple aggregation techniques,
Cadence supports basic aggregation tools that cover a wide list of use-cases.
These tools are defined in the built-in `BLS` contract, which does not need to be imported.

### Proof of Possession (PoP)[​](#proof-of-possession-pop "Direct link to Proof of Possession (PoP)")

Multi-signature verification in BLS requires a defense against rogue public-key attacks. Multiple ways are
available to protect BLS verification. Cadence provides the proof of possession of private key as a defense tool.
The proof of possession of private key is a BLS signature over the public key itself.
The PoP signature follows the same requirements of a BLS signature (detailed in [Signature verification](#signature-verification)),
except it uses a special domain separation tag. The key expected to be used in KMAC128 is the UTF-8 encoding of `"BLS_POP_BLS12381G1_XOF:KMAC128_SSWU_RO_POP_"`.
The expected message to be signed by the PoP is the serialization of the BLS public key corresponding to the signing private key ([serialization details](#public-key-construction)).
The PoP can only be verified using the `PublicKey` method `verifyPoP`.

### BLS signature aggregation[​](#bls-signature-aggregation "Direct link to BLS signature aggregation")

 `_10view fun aggregateSignatures(_ signatures: [[UInt8]]): [UInt8]?`

Aggregates multiple BLS signatures into one.
Signatures could be generated from the same or distinct messages, they
could also be the aggregation of other signatures.
The order of the signatures in the slice does not matter since the aggregation is commutative.
There is no subgroup membership check performed on the input signatures.
If the array is empty or if decoding one of the signatures fails, the program aborts.

The output signature can be verified against an aggregated public key to authenticate multiple
signers at once. Since the `verify` method accepts a single data to verify against, it is only possible to
verify multiple signatures of the same message.

### BLS public key aggregation[​](#bls-public-key-aggregation "Direct link to BLS public key aggregation")

 `_10view fun aggregatePublicKeys(_ publicKeys: [PublicKey]): PublicKey?`

Aggregates multiple BLS public keys into one.

The order of the public keys in the slice does not matter since the aggregation is commutative.
The input keys are guaranteed to be in the correct subgroup since subgroup membership is checked
at the key creation time.
If the array is empty or any of the input keys is not a BLS key, the program aborts.
Note that the identity public key is a valid input to this function and it represents the
identity element of aggregation.

The output public key can be used to verify aggregated signatures to authenticate multiple
signers at once. Since the `verify` method accepts a single data to verify against, it is only possible to
verify multiple signatures of the same message.
The identity public key is a possible output of the function, though signature verifications
against identity result in `false`.

In order to prevent rogue key attacks when verifying aggregated signatures, it is important to verify the
PoP of each individual key involved in the aggregation process.

## Crypto Contract[​](#crypto-contract "Direct link to Crypto Contract")

The built-in contract `Crypto` can be used to perform cryptographic operations.
The contract can be imported using `import Crypto`.

### Key Lists[​](#key-lists "Direct link to Key Lists")

The crypto contract allows creating key lists to be used for multi-signature verification.

A key list is basically a list of public keys where each public key is assigned a key index,
a hash algorithm and a weight. A list of `KeyListSignature` can be verified against a key list where each signature
entry specifies the public key index to be used against. The list verification is successful if all signatures from
the list are valid, each public key is used at most once, and the used keys weights add up to at least `1`.

The verification of each signature uses the Cadence single signature verification function with the key entry
hash algorithm and the input domain separation tag (check [signature verification](#signature-verification) for details).

It is possible to disable a public key by revoking it.
The revoked keys remain in the list and retain the same index. Only signatures against non-revoked keys
are considered valid.

For example, to verify two signatures with equal weights for some signed data:

 `_50import Crypto_50_50access(all)_50fun test main() {_50 let keyList = Crypto.KeyList()_50_50 let publicKeyA = PublicKey(_50 publicKey:_50 "db04940e18ec414664ccfd31d5d2d4ece3985acb8cb17a2025b2f1673427267968e52e2bbf3599059649d4b2cce98fdb8a3048e68abf5abe3e710129e90696ca".decodeHex(),_50 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_50 )_50 keyList.add(_50 publicKeyA,_50 hashAlgorithm: HashAlgorithm.SHA3_256,_50 weight: 0.5_50 )_50_50 let publicKeyB = PublicKey(_50 publicKey:_50 "df9609ee588dd4a6f7789df8d56f03f545d4516f0c99b200d73b9a3afafc14de5d21a4fc7a2a2015719dc95c9e756cfa44f2a445151aaf42479e7120d83df956".decodeHex(),_50 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_50 )_50 keyList.add(_50 publicKeyB,_50 hashAlgorithm: HashAlgorithm.SHA3_256,_50 weight: 0.5_50 )_50_50 let signatureSet = [_50 Crypto.KeyListSignature(_50 keyIndex: 0,_50 signature:_50 "8870a8cbe6f44932ba59e0d15a706214cc4ad2538deb12c0cf718d86f32c47765462a92ce2da15d4a29eb4e2b6fa05d08c7db5d5b2a2cd8c2cb98ded73da31f6".decodeHex()_50 ),_50 Crypto.KeyListSignature(_50 keyIndex: 1,_50 signature:_50 "bbdc5591c3f937a730d4f6c0a6fde61a0a6ceaa531ccb367c3559335ab9734f4f2b9da8adbe371f1f7da913b5a3fdd96a871e04f078928ca89a83d841c72fadf".decodeHex()_50 )_50 ]_50_50 // "foo", encoded as UTF-8, in hex representation_50 let signedData = "666f6f".decodeHex()_50_50 let isValid = keyList.verify(_50 signatureSet: signatureSet,_50 signedData: signedData,_50 domainSeparationTag: "FLOW-V0.0-user",_50 )_50}`

Below are the implementation details of the key list and the signature list:

 `_72access(all)_72struct KeyListEntry {_72_72 access(all)_72 let keyIndex: Int_72_72 access(all)_72 let publicKey: PublicKey_72_72 access(all)_72 let hashAlgorithm: HashAlgorithm_72_72 access(all)_72 let weight: UFix64_72_72 access(all)_72 let isRevoked: Bool_72_72 init(_72 keyIndex: Int,_72 publicKey: PublicKey,_72 hashAlgorithm: HashAlgorithm,_72 weight: UFix64,_72 isRevoked: Bool_72 )_72}_72_72access(all)_72struct KeyList {_72_72 init()_72_72 /// Adds a new key with the given weight_72 access(all)_72 fun add(_72 _ publicKey: PublicKey,_72 hashAlgorithm: HashAlgorithm,_72 weight: UFix64_72 )_72_72 /// Returns the key at the given index, if it exists._72 /// Revoked keys are always returned, but they have `isRevoked` field set to true_72 access(all)_72 fun get(keyIndex: Int): KeyListEntry?_72_72 /// Marks the key at the given index revoked, but does not delete it_72 access(all)_72 fun revoke(keyIndex: Int)_72_72 /// Returns true if the given signatures are valid for the given signed data_72 /// `domainSeparationTag` is used to specify a scope for each signature,_72 /// and is implemented the same way as `PublicKey`'s verify function._72 access(all)_72 fun verify(_72 signatureSet: [KeyListSignature],_72 signedData: [UInt8],_72 domainSeparationTag: String_72 ): Bool_72}_72_72access(all)_72struct KeyListSignature {_72_72 access(all)_72 let keyIndex: Int_72 _72 access(all)_72 let signature: [UInt8]_72_72 access(all)_72 init(keyIndex: Int, signature: [UInt8])_72}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/crypto.mdx)[PreviousEnvironment Information](/docs/language/environment-information)[NextType Hierarchy](/docs/language/type-hierarchy)
###### Rate this page

😞😐😊

* [Hash algorithms](#hash-algorithms)
* [Hashing](#hashing)
* [Hashing with a domain tag](#hashing-with-a-domain-tag)
  + [KMAC128 for BLS](#kmac128-for-bls)
* [Signature algorithms](#signature-algorithms)
* [Public keys](#public-keys)
  + [Public Key construction](#public-key-construction)
  + [Public Key validation](#public-key-validation)
  + [Signature verification](#signature-verification)
* [BLS multi-signature](#bls-multi-signature)
  + [Proof of Possession (PoP)](#proof-of-possession-pop)
  + [BLS signature aggregation](#bls-signature-aggregation)
  + [BLS public key aggregation](#bls-public-key-aggregation)
* [Crypto Contract](#crypto-contract)
  + [Key Lists](#key-lists)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

