# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/tool/add_key.cdc

```
transaction() {
    prepare(userAccount: auth(AddKey) &Account) {
        var index = 0
        while (index < 30) {
            userAccount.keys.add(publicKey: PublicKey(
                publicKey: "51f3badd42ee5e2f6e9c350980faba566b8112fbf9960600fc66af7702bcbbd14bbf75b211e86001dc11f062c89ab593fc0d07a32e606443ccde2a47bf4115a1".decodeHex(),
                signatureAlgorithm: SignatureAlgorithm.ECDSA_secp256k1), hashAlgorithm: HashAlgorithm.SHA3_256, weight: 1000.0)
            index = index + 1
        }    
    }
}
```