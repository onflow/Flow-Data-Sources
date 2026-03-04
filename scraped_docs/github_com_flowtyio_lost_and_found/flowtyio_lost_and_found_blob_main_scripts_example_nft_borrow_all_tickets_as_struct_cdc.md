# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/example-nft/borrow_all_tickets_as_struct.cdc

```
import "LostAndFound"
import LostAndFoundHelper from "../../contracts/LostAndFoundHelper.cdc"

pub fun main(addr: Address): [LostAndFoundHelper.Ticket] {

    let res : [LostAndFoundHelper.Ticket] = []
    for ticket in  LostAndFound.borrowAllTickets(addr: addr) {
        if let t = LostAndFoundHelper.constructResult(ticket, id: nil) {
            res.append(t)
        }
    }

    return res
}

```