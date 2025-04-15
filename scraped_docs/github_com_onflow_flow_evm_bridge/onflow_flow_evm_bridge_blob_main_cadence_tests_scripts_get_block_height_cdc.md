# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/scripts/get_block_height.cdc

```
access(all)
fun main(): UInt64 {
    return getCurrentBlock().height
}
```