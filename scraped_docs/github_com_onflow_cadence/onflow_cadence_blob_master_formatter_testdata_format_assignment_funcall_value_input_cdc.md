# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/assignment-funcall-value/input.cdc

```
access(all) fun test() {
    var entries: [Entry] = []
    entries[0] = Entry(keyIndex: 0, publicKey: key, hashAlgorithm: algo, weight: 1.0, isRevoked: true)
}

```