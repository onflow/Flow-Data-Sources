# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/bot/clear_empty_delegator.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction(uuid: UInt64) {
    prepare(botAcct: auth(BorrowValue) &Account) {
        let bot = botAcct.storage.borrow<&DelegatorManager.DelegationStrategy>(from: DelegatorManager.delegationStrategyPath)!

        bot.cleanDelegators(delegatorUUID: uuid)
    }
}
```