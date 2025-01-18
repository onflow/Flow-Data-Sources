# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_current_view.cdc

```
// Returns the view of the current block

access(all) fun main(): UInt64 {
    let currentBlock = getCurrentBlock()
    return currentBlock.view
}

```