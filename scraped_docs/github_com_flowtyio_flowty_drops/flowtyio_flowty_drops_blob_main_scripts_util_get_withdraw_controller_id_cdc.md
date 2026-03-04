# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/util/get_withdraw_controller_id.cdc

```
import "FungibleToken"

access(all) fun main(addr: Address, path: StoragePath): UInt64 {
    let acct = getAuthAccount<auth(Capabilities) &Account>(addr)

    let type = Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>()
    for controller in acct.capabilities.storage.getControllers(forPath: path) {
        if controller.borrowType.isSubtype(of: type) {
            return controller.capabilityID
        }
    }

    panic("no withdraw capability ID found")
}
```