# Source: https://github.com/emerald-dao/emerald-id/blob/main/flow/cadence/transactions/addPublicKey.cdc

```
transaction(publicKey: String) {
  prepare(signer: AuthAccount) {
    let bytes = publicKey.decodeHex()
    let key = PublicKey(
      publicKey: bytes,
      signatureAlgorithm: SignatureAlgorithm.ECDSA_secp256k1
    )

    var counter = 0

    counter = counter + 1
    signer.keys.add(
      publicKey: key,
      hashAlgorithm: HashAlgorithm.SHA3_256,
      weight: 1000.0
    )
    
  }

  execute {

  }
}
```