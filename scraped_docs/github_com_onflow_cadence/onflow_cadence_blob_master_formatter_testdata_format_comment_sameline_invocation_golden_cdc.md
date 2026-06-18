# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/comment-sameline-invocation/golden.cdc

```
access(all) fun test() {
    let x = Metadata(
        counter: epochCounter,
        seed: randomSource,
        totalRewards: 0.0,  // will be overwritten in calculateRewards
        clusters: [],
        keys: []
    )
    process(x)
}

```