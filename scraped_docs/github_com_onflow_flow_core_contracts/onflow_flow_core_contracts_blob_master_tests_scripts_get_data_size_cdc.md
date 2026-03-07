# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/scripts/get_data_size.cdc

```
import "FlowTransactionScheduler"

access(all) fun main(data: AnyStruct): UFix64 {
    return FlowTransactionScheduler.getSizeOfData(data)
}

```