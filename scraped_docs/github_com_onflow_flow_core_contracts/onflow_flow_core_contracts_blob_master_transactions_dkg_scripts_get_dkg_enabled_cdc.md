# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_enabled.cdc

```
import "FlowDKG"

access(all) fun main(): Bool {
    return FlowDKG.dkgEnabled
}
```