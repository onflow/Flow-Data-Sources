# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/hybridCustody/edit_child_account.cdc

```
import HybridCustody from 0xHybridCustody
import MetadataViews from 0xMetadataViews

transaction(childAddress: Address, name: String, description: String, thumbnail: String) {
    prepare(acct: AuthAccount) {
        let m = acct.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("manager not found")
        
        let d = MetadataViews.Display(
            name: name,
            description: description,
            thumbnail: MetadataViews.HTTPFile(url: thumbnail)
        )

        m.setChildAccountDisplay(address: childAddress, d)
    }
}
```