# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/init_lp_collection.cdc

```
import SwapFactory from "../../contracts/SwapFactory.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"

transaction() {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let lpTokenCollectionStoragePath = SwapConfig.LpTokenCollectionStoragePath
        let lpTokenCollectionPublicPath = SwapConfig.LpTokenCollectionPublicPath
        var lpTokenCollectionRef = userAccount.storage.borrow<&SwapFactory.LpTokenCollection>(from: lpTokenCollectionStoragePath)
        if lpTokenCollectionRef == nil {
            destroy <- userAccount.storage.load<@AnyResource>(from: lpTokenCollectionStoragePath)
            userAccount.storage.save(<-SwapFactory.createEmptyLpTokenCollection(), to: lpTokenCollectionStoragePath)
            let lpTokenCollectionCap = userAccount.capabilities.storage.issue<&{SwapInterfaces.LpTokenCollectionPublic}>(lpTokenCollectionStoragePath)
            userAccount.capabilities.publish(lpTokenCollectionCap, at: lpTokenCollectionPublicPath)
        }
    }
}
```