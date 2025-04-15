# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster_votes.cdc

```
import "FlowClusterQC"

// Returns an array of Votes for the specified cluster

access(all) fun main(clusterIndex: UInt16): [FlowClusterQC.Vote] {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex].votes

}
```