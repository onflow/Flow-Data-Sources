# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/variable-funcall-value/input.cdc

```
access(all) fun test() {
    let entry = KeyListEntry(
        keyIndex: keyIndex,
        publicKey: publicKey,
        hashAlgorithm: hashAlgorithm,
        weight: weight,
        isRevoked: false
    )
}

```