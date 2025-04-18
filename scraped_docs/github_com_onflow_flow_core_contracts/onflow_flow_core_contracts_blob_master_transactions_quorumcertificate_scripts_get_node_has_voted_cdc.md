# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_node_has_voted.cdc

```
import "FlowClusterQC"

// Returns a boolean indicating if a node has submitted a vote for this epoch

access(all) fun main(nodeID: String): Bool {

    // If we are in the staking auction phase (voting not in progress), the votes
    // from last epoch are still stored and nodeHasVoted reports True. Since we
    // only want to know whether we have voted for the CURRENT epoch, omit this case.
    return FlowClusterQC.inProgress && FlowClusterQC.nodeHasVoted(nodeID)

}
```