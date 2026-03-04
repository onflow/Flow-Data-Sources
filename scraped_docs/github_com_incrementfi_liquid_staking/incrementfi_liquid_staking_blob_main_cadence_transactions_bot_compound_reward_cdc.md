# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/bot/compound_reward.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction() {
    prepare(botAcct: auth(BorrowValue) &Account) {
        
        let bot = botAcct.storage.borrow<&DelegatorManager.DelegationStrategy>(from: DelegatorManager.delegationStrategyPath)!

        bot.compoundRewards()
    }
}
```