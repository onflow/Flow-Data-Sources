# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Comptroller/config_market.cdc

```
import LendingComptroller from "../../contracts/LendingComptroller.cdc"

transaction(poolAddr: Address, liquidationPenalty: UFix64, collateralFactor: UFix64, borrowCap: UFix64, supplyCap: UFix64, isOpen: Bool, isMining: Bool) {

    let comptrollerAdminRef: &LendingComptroller.Admin

    prepare(comptrollerAccount: auth(BorrowValue) &Account) {
        self.comptrollerAdminRef = comptrollerAccount.storage.borrow<&LendingComptroller.Admin>(from: LendingComptroller.AdminStoragePath) ?? panic("Lost comptroller admin.")
    }

    execute {
        self.comptrollerAdminRef.configMarket(pool: poolAddr, isOpen: isOpen, isMining: isMining, liquidationPenalty: liquidationPenalty, collateralFactor: collateralFactor, borrowCap: borrowCap, supplyCap: supplyCap)
    }
}
```