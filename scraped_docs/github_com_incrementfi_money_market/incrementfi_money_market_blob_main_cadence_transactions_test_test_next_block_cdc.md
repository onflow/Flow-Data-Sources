# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Test/test_next_block.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"

transaction() {
    prepare(signer: &Account) {
        log("Next block --------------- pre block id: ".concat(getCurrentBlock().height.toString()))
        let poolAddrs = signer.capabilities.borrow<&{LendingInterfaces.ComptrollerPublic}>(LendingConfig.ComptrollerPublicPath)!.getAllMarkets()
        for poolAddr in poolAddrs {
            getAccount(poolAddr).capabilities.borrow<&{LendingInterfaces.PoolPublic}>(LendingConfig.PoolPublicPublicPath)!.accrueInterest()
        }
        log("End ---------------------- aft block id: ".concat(getCurrentBlock().height.toString()))
    }

    execute {
    }
}
```