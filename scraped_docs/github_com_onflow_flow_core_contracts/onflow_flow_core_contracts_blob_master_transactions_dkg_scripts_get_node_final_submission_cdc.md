# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_node_final_submission.cdc

```
import FlowDKG from "FlowDKG"

access(all) fun main(nodeID: String): [String?] {
    return FlowDKG.getNodeFinalSubmission(nodeID)!
}
```