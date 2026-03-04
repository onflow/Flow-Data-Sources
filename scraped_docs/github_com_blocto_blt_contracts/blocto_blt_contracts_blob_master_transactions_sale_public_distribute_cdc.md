# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/sale/public/distribute.cdc

```
import BloctoTokenPublicSale from "../../../contracts/flow/sale/BloctoTokenPublicSale.cdc"

transaction(address: Address, allocationAmount: UFix64) {

    // The reference to the Admin Resource
    let adminRef: &BloctoTokenPublicSale.Admin

    prepare(account: AuthAccount) {

        // Get admin reference
        self.adminRef = account.borrow<&BloctoTokenPublicSale.Admin>(from: BloctoTokenPublicSale.SaleAdminStoragePath)
			?? panic("Could not borrow reference to the admin!")
    }

    execute {

        // Distribute BLT purchase
        self.adminRef.distribute(address: address, allocationAmount: allocationAmount)
    }
}

```