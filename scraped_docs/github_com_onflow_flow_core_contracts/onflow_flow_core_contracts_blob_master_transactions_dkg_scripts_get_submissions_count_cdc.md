# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_submissions_count.cdc

```
import FlowDKG from "FlowDKG"

pub fun main():  {Int: UInt64} {
    return FlowDKG.getFinalSubmissionCount()
}

```