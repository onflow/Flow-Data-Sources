# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/transactions/admin/editions/close_edition.cdc

```
import AllDay from "AllDay"

transaction(editionID: UInt64) {
    // local variable for the admin reference
    let admin: auth(AllDay.Operate) &AllDay.Admin

    prepare(signer: auth(BorrowValue) &Account) {
        // borrow a reference to the Admin resource
        self.admin = signer.storage.borrow<auth(AllDay.Operate) &AllDay.Admin>(from: AllDay.AdminStoragePath)
            ?? panic("Could not borrow a reference to the AllDay Admin capability")
    }

    execute {
        let id = self.admin.closeEdition(id: editionID)

        log("====================================")
        log("Closed Edition:")
        log("EditionID: ".concat(id.toString()))
        log("====================================")
    }
}


```