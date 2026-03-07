# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/scripts/get_timestamp.cdc

```
access(all) fun main(): UFix64 {
    return getCurrentBlock().timestamp
}

```