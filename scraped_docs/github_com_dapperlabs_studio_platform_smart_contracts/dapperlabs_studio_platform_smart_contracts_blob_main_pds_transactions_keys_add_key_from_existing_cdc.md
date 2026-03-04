# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/transactions/keys/add-key-from-existing.cdc

```
transaction {
    prepare(signer: AuthAccount) {
        signer.keys.add(
            publicKey: signer.keys.get(keyIndex: 0)!.publicKey,
            hashAlgorithm: signer.keys.get(keyIndex: 0)!.hashAlgorithm,
            weight: 1000.0
        )
    }
}

```