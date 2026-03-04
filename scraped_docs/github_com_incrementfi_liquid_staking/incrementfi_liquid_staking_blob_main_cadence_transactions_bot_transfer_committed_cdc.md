# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/bot/transfer_committed.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction(fromNode: String, toNode: String, amount: UFix64) {
    prepare(botAcct: auth(BorrowValue) &Account) {
        
        let bot = botAcct.storage.borrow<&DelegatorManager.DelegationStrategy>(from: DelegatorManager.delegationStrategyPath)!
        
        bot.transferCommittedTokens(fromNodeID: fromNode, toNodeID: toNode, amount: amount)
    }
}
```