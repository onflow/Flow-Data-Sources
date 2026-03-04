# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/factory/set_pair_addr.cdc

```
import SwapFactory from "../../contracts/SwapFactory.cdc"

transaction() {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let factoryAdminRef = userAccount.storage.borrow<&SwapFactory.Admin>(from: /storage/swapFactoryAdmin)!
        factoryAdminRef.setPairContractTemplateAddress(newAddr: 0xc20df20fabe06457)
    }
    execute {
    }
}
```