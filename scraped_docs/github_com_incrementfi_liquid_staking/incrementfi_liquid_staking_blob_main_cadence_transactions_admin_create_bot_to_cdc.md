# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/create_bot_to.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction() {
    prepare(nodeMgrAcct: auth(BorrowValue) &Account, botAcct: auth(Storage) &Account) {
        let adminRef = nodeMgrAcct.storage.borrow<&DelegatorManager.Admin>(from: DelegatorManager.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")

        let bot <- adminRef.createStrategy()

        botAcct.storage.save(<-bot, to: DelegatorManager.delegationStrategyPath)
    }
}
```