# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/verify_payer_balance_for_tx_execution.cdc

```
import FlowFees from "FlowFees"

access(all) fun main(payerAcct: Address, inclusionEffort: UFix64, maxExecutionEffort: UFix64): FlowFees.VerifyPayerBalanceResult {
    let authAcct = getAuthAccount<auth(BorrowValue) &Account>(payerAcct)
    return FlowFees.verifyPayersBalanceForTransactionExecution(authAcct, inclusionEffort: inclusionEffort,
        maxExecutionEffort: maxExecutionEffort)
}
```