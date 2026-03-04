# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_timestamp.cdc

```

access(all) fun main(): UFix64 {
    return getCurrentBlock().timestamp
}
```