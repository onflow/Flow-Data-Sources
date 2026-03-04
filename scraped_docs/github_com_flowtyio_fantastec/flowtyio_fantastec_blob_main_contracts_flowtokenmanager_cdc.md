# Source: https://github.com/Flowtyio/fantastec/blob/main/contracts/FlowTokenManager.cdc

```
import "FungibleToken"
import "FlowStorageFees"

access(all) contract FlowTokenManager {
  access(all) fun TopUpFlowTokens(account: &Account, flowTokenProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}) {
    if (account.storage.used > account.storage.capacity) {
      var extraStorageRequiredBytes = account.storage.used - account.storage.capacity

      var extraStorageRequiredMb = FlowStorageFees.convertUInt64StorageBytesToUFix64Megabytes(extraStorageRequiredBytes)
      var flowRequired = FlowStorageFees.storageCapacityToFlow(extraStorageRequiredMb)

      let vault: @{FungibleToken.Vault} <- flowTokenProvider.withdraw(amount: flowRequired)
      account
        .capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!
        .borrow()!
        .deposit(from: <- vault)
    }
  }
}
```