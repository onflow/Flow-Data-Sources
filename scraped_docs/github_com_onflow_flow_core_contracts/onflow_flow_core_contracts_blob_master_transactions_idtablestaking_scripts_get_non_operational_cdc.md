# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_non_operational.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the list of non-operational nodes

access(all) fun main(): [String] {
    return FlowIDTableStaking.getNonOperationalNodesList().keys
}
```