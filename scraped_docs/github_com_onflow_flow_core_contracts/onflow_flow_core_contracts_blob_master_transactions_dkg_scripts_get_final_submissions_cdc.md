# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_final_submissions.cdc

```
import "FlowDKG"

access(all) fun main(): [FlowDKG.ResultSubmission] {
    return FlowDKG.getFinalSubmissions()
}
```