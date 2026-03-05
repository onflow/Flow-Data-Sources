# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/set_collection_external_url.cdc

```
import "FlowtyWrapped"


transaction(url: String) {
    let admin: auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin

    prepare(acct: auth(Storage) &Account) {
        self.admin = acct.storage.borrow<auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin>(from: FlowtyWrapped.AdminStoragePath)
            ?? panic("Could not borrow a reference to the NFT minter")
    }

    execute {
        self.admin.setCollectionExternalUrl(url)
    }
}
```