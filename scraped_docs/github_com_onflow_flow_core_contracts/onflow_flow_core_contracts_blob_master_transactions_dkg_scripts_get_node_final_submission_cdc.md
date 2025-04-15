# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_node_final_submission.cdc

```
import "FlowDKG"

access(all) fun main(nodeID: String): FlowDKG.ResultSubmission {
    return FlowDKG.getNodeFinalSubmission(nodeID)!
}
```