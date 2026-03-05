# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/get_total_edition_supply.cdc

```
import "FlowtyWrapped"
import "WrappedEditions"

access(all) fun main(addr: Address, editionName: String): UInt64 {
    let acct = getAuthAccount<auth(Storage) &Account>(addr)
    let admin = acct.storage.borrow<auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin>(from: FlowtyWrapped.AdminStoragePath)!
    

    let edition = admin.getEdition(editionName: editionName) as! &{FlowtyWrapped.WrappedEdition}

    let editionSupply = edition.getEditionSupply()

    return editionSupply
}
```