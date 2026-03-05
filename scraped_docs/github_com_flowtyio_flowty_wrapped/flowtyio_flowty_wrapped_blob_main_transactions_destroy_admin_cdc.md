# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/destroy_admin.cdc

```
import "FlowtyWrapped"

transaction {
    prepare(acct: auth(Storage) &Account) {
        let admin <- acct.storage.load<@AnyResource>(from: FlowtyWrapped.AdminStoragePath)
        destroy admin

        // borrow the contract admin resource to make sure we haven't destroyed the wrong admin 
        let publicAdmin = getAccount(FlowtyWrapped.getAccountAddress()).capabilities.get<&{FlowtyWrapped.AdminPublic}>(FlowtyWrapped.AdminPublicPath)
        assert(publicAdmin.check(), message: "admin public isn't configured anymore!")
    }
}
```