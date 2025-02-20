# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/generate_quorum_certificate.cdc

```
import "FlowClusterQC"

// Gets the status of a cluster's QC generation

access(all) fun main(clusterIndex: UInt16): FlowClusterQC.ClusterQC {

    let clusters = FlowClusterQC.getClusters()

    return clusters[clusterIndex].generateQuorumCertificate()
        ?? panic("Could not generate quorum certificate")

}
```