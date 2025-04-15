# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/set_execution_memory_weights.cdc

```
// This transactions sets new execution memory weights.
transaction(newWeights: {UInt64: UInt64}) {
    prepare(signer: auth(Storage) &Account) {
        signer.storage.load<{UInt64: UInt64}>(from: /storage/executionMemoryWeights)
        signer.storage.save(newWeights, to: /storage/executionMemoryWeights)
    }
}
```