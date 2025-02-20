# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_clusters.cdc

```
import "FlowClusterQC"

// Script to return an array of Collector Clusters with all of their metadata

access(all) fun main(clusterIndex: UInt16): [FlowClusterQC.Cluster] {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex]

}
```