# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster.cdc

```
import "FlowClusterQC"

access(all) fun main(clusterIndex: UInt16): FlowClusterQC.Cluster {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex]

}
```