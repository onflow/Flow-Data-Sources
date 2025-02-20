# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_node_is_registered.cdc

```
import "FlowDKG"

access(all) fun main(nodeID: String): Bool {
    return FlowDKG.participantIsRegistered(nodeID)
}
```