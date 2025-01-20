# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_candidate_nodes.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the list of candidate nodes
// for the upcoming epoch
access(all) fun main(): {UInt8: {String: Bool}} {
    return FlowIDTableStaking.getCandidateNodeList()
}
```