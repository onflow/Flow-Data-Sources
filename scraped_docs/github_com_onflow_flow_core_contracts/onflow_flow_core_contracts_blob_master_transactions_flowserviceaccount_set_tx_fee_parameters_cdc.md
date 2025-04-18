# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/set_tx_fee_parameters.cdc

```
import "FlowFees"

// This transaction sets the FlowFees parameters
transaction(surgeFactor: UFix64, inclusionEffortCost: UFix64, executionEffortCost: UFix64) {
	let flowFeesAccountAdmin: &FlowFees.Administrator

	prepare(signer: auth(BorrowValue) &Account) {
		self.flowFeesAccountAdmin = signer.storage.borrow<&FlowFees.Administrator>(from: /storage/flowFeesAdmin)
			?? panic("Unable to borrow reference to administrator resource")
	}
	execute {
		self.flowFeesAccountAdmin.setFeeParameters(surgeFactor: surgeFactor, inclusionEffortCost: inclusionEffortCost, executionEffortCost: executionEffortCost)
	}
}
```