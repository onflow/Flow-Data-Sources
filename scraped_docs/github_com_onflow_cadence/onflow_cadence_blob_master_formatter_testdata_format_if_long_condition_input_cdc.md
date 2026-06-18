# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/if-long-condition/input.cdc

```
access(all) fun test() {
    if !key.publicKey.verify(signature: signature.signature, signedData: signedData, domainSeparationTag: domainSeparationTag, hashAlgorithm: key.hashAlgorithm) {
        return false
    }
}

```