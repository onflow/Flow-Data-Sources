# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_node_weight.cdc

```
import FlowClusterQC from "FlowClusterQC"

access(all) fun main(clusterIndex: UInt16, nodeID: String): UInt64 {

    let clusters = FlowClusterQC.getClusters()

    if clusters[clusterIndex].nodeWeights[nodeID] != nil {
        return clusters[clusterIndex].nodeWeights[nodeID]!
    } else {
        return 0 as UInt64
    }

}
```