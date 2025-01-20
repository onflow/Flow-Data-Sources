# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_tx_fee_parameters.cdc

```
import FlowFees from "FlowFees"

access(all) fun main(): FlowFees.FeeParameters {
    return FlowFees.getFeeParameters()
}
```