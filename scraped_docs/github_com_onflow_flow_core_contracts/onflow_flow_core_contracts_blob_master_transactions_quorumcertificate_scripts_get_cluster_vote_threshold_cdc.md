# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster_vote_threshold.cdc

```
import "FlowClusterQC"

access(all) fun main(clusterIndex: UInt16): UInt64 {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex].voteThreshold()

}
```