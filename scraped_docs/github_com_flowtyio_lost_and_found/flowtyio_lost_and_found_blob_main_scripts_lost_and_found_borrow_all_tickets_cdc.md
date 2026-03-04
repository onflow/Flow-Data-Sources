# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/lost-and-found/borrow_all_tickets.cdc

```
import "LostAndFound"
import "LostAndFoundHelper"

access(all) fun main(addr: Address): [LostAndFoundHelper.Ticket] {
    let tickets: [LostAndFoundHelper.Ticket] = []
    for ticket in LostAndFound.borrowAllTickets(addr: addr) {
        tickets.append(LostAndFoundHelper.constructResult(ticket, id: ticket.getNonFungibleTokenID())!)
    }
    
    return tickets
}
```