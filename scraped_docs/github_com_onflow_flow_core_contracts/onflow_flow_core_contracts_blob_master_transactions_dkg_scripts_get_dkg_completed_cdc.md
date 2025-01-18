# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_completed.cdc

```
import FlowDKG from "FlowDKG"

access(all) fun main(): Bool {
    return FlowDKG.dkgCompleted() != nil
}
```