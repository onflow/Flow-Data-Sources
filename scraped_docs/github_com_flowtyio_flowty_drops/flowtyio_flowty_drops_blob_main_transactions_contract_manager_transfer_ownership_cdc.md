# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/contract-manager/transfer_ownership.cdc

```
import "ContractManager"

transaction {
    prepare(acct: auth(Storage, Capabilities) &Account, receiver: auth(Storage, Capabilities) &Account) {
        if let cap = acct.capabilities.unpublish(ContractManager.PublicPath) {
            acct.capabilities.storage.getController(byCapabilityID: cap.id)?.delete()
        }

        let manager <- acct.storage.load<@ContractManager.Manager>(from: ContractManager.StoragePath)
            ?? panic("manager not found")

        receiver.storage.save(<- manager, to: ContractManager.StoragePath)
        receiver.storage.borrow<auth(ContractManager.Manage) &ContractManager.Manager>(from: ContractManager.StoragePath)!.onSave()
        receiver.capabilities.publish(
            receiver.capabilities.storage.issue<&ContractManager.Manager>(ContractManager.StoragePath),
            at: ContractManager.PublicPath
        )

        receiver.storage.borrow<auth(ContractManager.Manage) &ContractManager.Manager>(from: ContractManager.StoragePath)!.onSave()
    }
}
```