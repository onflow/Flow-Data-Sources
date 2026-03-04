# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/util/get_current_time.cdc

```
access(all) fun main(): UFix64 {
    return getCurrentBlock().timestamp
}
```