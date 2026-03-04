# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/general/getTimestamp.cdc

```
pub fun main(): UFix64 {
    return getCurrentBlock().timestamp
}

```