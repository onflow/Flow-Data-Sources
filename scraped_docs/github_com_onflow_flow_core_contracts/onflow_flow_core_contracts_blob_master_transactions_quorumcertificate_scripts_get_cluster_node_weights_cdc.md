# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster_node_weights.cdc

```
import FlowClusterQC from "FlowClusterQC"

access(all) fun main(clusterIndex: UInt16): {String: UInt64} {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex].nodeWeights

}
```