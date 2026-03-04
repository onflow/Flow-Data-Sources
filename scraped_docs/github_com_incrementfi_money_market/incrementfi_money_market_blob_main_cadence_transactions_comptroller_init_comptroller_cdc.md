# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Comptroller/init_comptroller.cdc

```

import LendingComptroller from "../../contracts/LendingComptroller.cdc"

transaction(oracleAddr: Address, closeFactor: UFix64) {

    let comptrollerAdminRef: &LendingComptroller.Admin

    prepare(comptrollerAccount: auth(BorrowValue) &Account) {
        self.comptrollerAdminRef = comptrollerAccount.storage.borrow<&LendingComptroller.Admin>(from: LendingComptroller.AdminStoragePath) ?? panic("Lost comptroller admin.")
    }

    execute {
        self.comptrollerAdminRef.configOracle(oracleAddress: oracleAddr)
        self.comptrollerAdminRef.setCloseFactor(closeFactor: closeFactor)
    }
}
```