# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/example-token/borrow_all_tickets.cdc

```
import "LostAndFound"
import "LostAndFoundHelper"
import "ExampleToken"

access(all) fun main(addr: Address): [LostAndFoundHelper.Ticket] {
    let tickets: [LostAndFoundHelper.Ticket] = []
    for ticket in LostAndFound.borrowAllTicketsByType(addr: addr, type: Type<@ExampleToken.Vault>()) {
        tickets.append(LostAndFoundHelper.constructResult(ticket, id: ticket.getNonFungibleTokenID())!)
    }

    return tickets
}
```