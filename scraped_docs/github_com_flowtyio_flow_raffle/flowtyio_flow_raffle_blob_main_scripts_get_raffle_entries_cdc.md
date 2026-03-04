# Source: https://github.com/Flowtyio/flow-raffle/blob/main/scripts/get_raffle_entries.cdc

```
import "FlowtyRaffles"

access(all) fun main(addr: Address, id: UInt64): [AnyStruct] {
    let acct = getAuthAccount<auth(Storage) &Account>(addr)
    let manager = acct.storage.borrow<&{FlowtyRaffles.ManagerPublic}>(from: FlowtyRaffles.ManagerStoragePath)
        ?? panic("raffles manager not found")
    let raffle = manager.borrowRafflePublic(id: id)
        ?? panic("raffle not found")
    let source = raffle.borrowSourcePublic() ?? panic("source is invalid")

    return source.getEntries()
}
```