# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/raffle/draw_from_raffle.cdc

```
import "FlowtyRaffles"

transaction(id: UInt64) {
    prepare(acct: auth(Storage) &Account) { 
        let manager = acct.storage.borrow<auth(FlowtyRaffles.Manage) &FlowtyRaffles.Manager>(from: FlowtyRaffles.ManagerStoragePath)
            ?? panic("raffles manager not found")
        let receiptID = manager.commitDrawing(raffleID: id)

        let ref = manager as &FlowtyRaffles.Manager
        manager.revealDrawing(manager: ref, raffleID: id, receiptID: receiptID)
    }
}
```