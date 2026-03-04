# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/test/create_new_delegator.cdc

```
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"

transaction(nodeID: String, amount: UFix64) {
    prepare(account: auth(Storage) &Account) {
        let flowVault = account.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!

        let delegator <- FlowIDTableStaking.registerNewDelegator(nodeID: nodeID, tokensCommitted: <-flowVault.withdraw(amount: amount))

        account.storage.save(<-delegator, to: FlowIDTableStaking.DelegatorStoragePath)
    }
}
```