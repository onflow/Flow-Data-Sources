# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/example-nft/borrow_all_tickets.cdc

```
import "LostAndFound"
import "LostAndFoundHelper"
import "ExampleNFT"

access(all) fun main(addr: Address): [LostAndFoundHelper.Ticket] {
    let tickets: [LostAndFoundHelper.Ticket] = []
    for ticket in LostAndFound.borrowAllTicketsByType(addr: addr, type: Type<@ExampleNFT.NFT>()) {
        tickets.append(LostAndFoundHelper.constructResult(ticket, id: ticket.getNonFungibleTokenID())!)
    }

    return tickets
}
```