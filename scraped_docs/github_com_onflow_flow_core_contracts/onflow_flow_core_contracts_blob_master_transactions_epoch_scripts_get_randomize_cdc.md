# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_randomize.cdc

```
import "FlowEpoch"

access(all) fun main(array: [String]): [String] {
    return FlowEpoch.randomize(array)
}

```