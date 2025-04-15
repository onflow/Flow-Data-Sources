# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster_complete.cdc

```
import "FlowClusterQC"

// Gets the status of a cluster's QC generation

access(all) fun main(clusterIndex: UInt16): Bool {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex].isComplete() != nil

}
```