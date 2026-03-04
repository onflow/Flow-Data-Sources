# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/AprSnapshot/sample_all_markets_apr.cdc

```

import LendingAprSnapshot from "../../contracts/LendingAprSnapshot.cdc"
import LendingComptroller from "../../contracts/LendingComptroller.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"

// Bot periodically sample all lending markets' apr data and store them on-chain. 
transaction() {
    prepare(bot: &Account) {
        let comptrollerRef = getAccount(LendingComptroller.comptrollerAddress).capabilities.borrow<&{LendingInterfaces.ComptrollerPublic}>(LendingConfig.ComptrollerPublicPath)
            ?? panic("cannot borrow reference to ComptrollerPublic")

        let poolArrays = comptrollerRef.getAllMarkets()
        for poolAddr in poolArrays {
            let sampled = LendingAprSnapshot.sample(poolAddr: poolAddr)
        }
    }
}
```