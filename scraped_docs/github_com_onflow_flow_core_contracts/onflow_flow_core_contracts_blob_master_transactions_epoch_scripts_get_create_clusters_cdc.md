# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_create_clusters.cdc

```
import "FlowEpoch"
import "FlowClusterQC"

access(all) fun main(array: [String]): [FlowClusterQC.Cluster] {
    return FlowEpoch.createCollectorClusters(nodeIDs: array)
}

```