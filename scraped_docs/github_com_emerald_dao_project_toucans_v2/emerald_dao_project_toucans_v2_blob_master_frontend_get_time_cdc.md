# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/get_time.cdc

```
access(all) fun main(): UFix64 {
    return getCurrentBlock().timestamp
}
```