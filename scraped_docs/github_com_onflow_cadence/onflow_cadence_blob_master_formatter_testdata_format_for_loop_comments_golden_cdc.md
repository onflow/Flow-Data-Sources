# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/for-loop-comments/golden.cdc

```
access(all) fun test(items: [Int]) {
    for item in items {
        // Check validity
        if item < 0 {
            continue
        }
        // Process item
        let x = item
    }
}

```