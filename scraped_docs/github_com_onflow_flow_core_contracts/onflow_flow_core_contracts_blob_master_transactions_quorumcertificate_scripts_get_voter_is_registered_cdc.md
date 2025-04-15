# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_voter_is_registered.cdc

```
import "FlowClusterQC"

// Returns a boolean indicating if a node is registered for voting

access(all) fun main(nodeID: String): Bool {

    return FlowClusterQC.voterIsRegistered(nodeID)

}
```