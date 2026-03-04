# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/lost-and-found/get_ticket_ft_balance.cdc

```
import "LostAndFound"

access(all) fun main(addr: Address, ticketID: UInt64, ticketTypeIdentifier: String): UFix64? {
    let composite = CompositeType(ticketTypeIdentifier)!

    let manager = LostAndFound.borrowShelfManager()
    let shelf = manager.borrowShelf(redeemer: addr) ?? panic("no shelf found for given address")
    let bin = shelf.borrowBin(type: composite) ?? panic("bin not found")
    let ticket = bin.borrowTicket(id: ticketID) ?? panic("ticket not found")
    return ticket.getFungibleTokenBalance()
}
```