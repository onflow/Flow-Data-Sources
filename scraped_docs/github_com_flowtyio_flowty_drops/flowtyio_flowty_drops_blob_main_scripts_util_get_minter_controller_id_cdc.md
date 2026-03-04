# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/util/get_minter_controller_id.cdc

```
import "FlowtyDrops"

access(all) fun main(addr: Address): UInt64? {
    let acct = getAuthAccount<auth(Capabilities, Storage) &Account>(addr)

    var path: StoragePath? = nil
    acct.storage.forEachStored(fun (p: StoragePath, type: Type): Bool {
        if type.isSubtype(of: Type<@{FlowtyDrops.Minter}>()) {
            path = p
            return false
        }

        return true
    })

    assert(path != nil, message: "no minters found in account storage")

    let controllers = acct.capabilities.storage.getControllers(forPath: path!)

    for c in controllers {
        if c.borrowType == Type<&{FlowtyDrops.Minter}>() {
            return c.capabilityID
        }
    }

    return nil
}
```