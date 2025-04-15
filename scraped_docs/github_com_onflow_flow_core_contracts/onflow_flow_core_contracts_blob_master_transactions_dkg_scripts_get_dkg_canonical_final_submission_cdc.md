# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_canonical_final_submission.cdc

```
import "FlowDKG"

access(all) fun main(): FlowDKG.ResultSubmission? {
    return FlowDKG.dkgCompleted()
}
```