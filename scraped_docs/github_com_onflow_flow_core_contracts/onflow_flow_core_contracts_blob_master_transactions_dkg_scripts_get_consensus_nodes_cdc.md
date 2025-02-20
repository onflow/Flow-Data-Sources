# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_consensus_nodes.cdc

```
import "FlowDKG"

access(all) fun main(): [String] {
    return FlowDKG.getConsensusNodeIDs()
}
```