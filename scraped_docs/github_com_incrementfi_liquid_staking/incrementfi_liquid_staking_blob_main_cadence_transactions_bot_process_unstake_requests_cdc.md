# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/bot/process_unstake_requests.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction(requestUnstakeAmount: UFix64, uuid: UInt64) {
    prepare(botAcct: auth(BorrowValue) &Account) {
        
        let bot = botAcct.storage.borrow<&DelegatorManager.DelegationStrategy>(from: DelegatorManager.delegationStrategyPath)!

        bot.processUnstakeRequest(requestUnstakeAmount: requestUnstakeAmount, delegatorUUID: uuid)
    }
}
```