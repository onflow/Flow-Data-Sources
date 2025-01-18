# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_node_is_claimed.cdc

```
import FlowDKG from "FlowDKG"

access(all) fun main(nodeID: String): Bool {
    if FlowDKG.participantIsClaimed(nodeID) != nil {
        return FlowDKG.participantIsClaimed(nodeID)!
    } else {
        return false
    }
}
```