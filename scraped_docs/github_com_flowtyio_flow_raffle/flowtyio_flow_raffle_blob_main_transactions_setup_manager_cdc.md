# Source: https://github.com/Flowtyio/flow-raffle/blob/main/transactions/setup_manager.cdc

```
import "FlowtyRaffles"

transaction {
    prepare(acct: auth(Capabilities, Storage) &Account) {
        let manager <- FlowtyRaffles.createManager()
        acct.storage.save(<-manager, to: FlowtyRaffles.ManagerStoragePath)
        acct.capabilities.publish(
            acct.capabilities.storage.issue<&FlowtyRaffles.Manager>(FlowtyRaffles.ManagerStoragePath),
            at: FlowtyRaffles.ManagerPublicPath
        )
    }
}
```