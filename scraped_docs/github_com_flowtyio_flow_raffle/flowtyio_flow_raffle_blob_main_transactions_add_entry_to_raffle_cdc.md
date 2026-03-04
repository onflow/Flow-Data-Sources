# Source: https://github.com/Flowtyio/flow-raffle/blob/main/transactions/add_entry_to_raffle.cdc

```
import "FlowtyRaffles"

transaction(raffleID: UInt64, entry: AnyStruct) {
    prepare(acct: auth(Capabilities, Storage) &Account) {
        let manager = acct.storage.borrow<auth(FlowtyRaffles.Manage, FlowtyRaffles.Add) &FlowtyRaffles.Manager>(from: FlowtyRaffles.ManagerStoragePath)
            ?? panic("raffles manager not found")
        let raffle = manager.borrowRaffle(id: raffleID)
            ?? panic("raffle not found")
        raffle.addEntry(entry)
    }
}
```