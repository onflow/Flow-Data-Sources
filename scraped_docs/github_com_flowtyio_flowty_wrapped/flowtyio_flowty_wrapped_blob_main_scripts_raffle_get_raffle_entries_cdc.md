# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/raffle/get_raffle_entries.cdc

```
import "FlowtyRaffles"
access(all) fun main(addr: Address, id: UInt64): [AnyStruct] {
    let acct = getAuthAccount<auth(Storage) &Account>(addr)
    let manager = acct.storage.borrow<&FlowtyRaffles.Manager>(from: FlowtyRaffles.ManagerStoragePath)
        ?? panic("raffles manager not found")
    let raffle = manager.borrowRafflePublic(id: id)
        ?? panic("raffle not found")
    let source: &{FlowtyRaffles.RaffleSourcePublic} = raffle.borrowSourcePublic() ?? panic("source is invalid")

    return source.getEntries()
}
```