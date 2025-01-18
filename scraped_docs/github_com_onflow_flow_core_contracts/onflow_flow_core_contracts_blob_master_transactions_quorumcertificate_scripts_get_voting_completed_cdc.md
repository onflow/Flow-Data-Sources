# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_voting_completed.cdc

```
import FlowClusterQC from "FlowClusterQC"

// Returns a boolean indicating if a node has submitted a vote for this epoch

access(all) fun main(): Bool {

    return FlowClusterQC.votingCompleted()

}
```