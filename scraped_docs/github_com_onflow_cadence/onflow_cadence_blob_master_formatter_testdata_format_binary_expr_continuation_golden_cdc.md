# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/binary-expr-continuation/golden.cdc

```
access(all) fun test() {
    while index < arrayLength && RandomBeaconHistory.randomSourceHistory[index].length > 0 {
        index = index + 1
    }
    let short = a && b
}

```