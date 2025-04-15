# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_qc_enabled.cdc

```
import "FlowClusterQC"

access(all) fun main(): Bool {

    return FlowClusterQC.inProgress

}
```