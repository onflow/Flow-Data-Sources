# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/sale/public/addPublicKey.cdc

```
transaction(publicKey: String) {
    prepare(account: AuthAccount) {
        let key = PublicKey(
            publicKey: publicKey.decodeHex(),
            signatureAlgorithm: SignatureAlgorithm.ECDSA_secp256k1
        )

        account.keys.add(
            publicKey: key,
            hashAlgorithm: HashAlgorithm.SHA3_256,
            weight: 1000.0
        )
    }
}

```