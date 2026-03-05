# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/claim_admin.cdc

```
import "FlowtyWrapped"

transaction(name: String, provider: Address) {
    prepare(acct: auth(Inbox, Storage) &Account) {
        let providerAdmin = acct.inbox.claim<auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin>(name, provider: provider)
            ?? panic("capabiltiy not found")

        let admin <- providerAdmin.borrow()!.createAdmin()
        acct.storage.save(<-admin, to: FlowtyWrapped.AdminStoragePath)
    }
}
```