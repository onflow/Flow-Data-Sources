# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/factory/set_pair_key.cdc

```
import SwapFactory from "../../contracts/SwapFactory.cdc"

transaction() {
    prepare(userAccount: AuthAccount) {
        let factoryAdminRef = userAccount.borrow<&SwapFactory.Admin>(from: /storage/swapFactoryAdmin)!
        factoryAdminRef.setPairAccountPublicKey(publicKey: "95efe052cc2e1be2162cb4c273ab86a4602369536fac60e835c63ee5fc856ad7f6f4d17eb505af54482caac0addeb9b2b24e7b44eb79cb02e19be106c1cbfd4f")
    }
}

```