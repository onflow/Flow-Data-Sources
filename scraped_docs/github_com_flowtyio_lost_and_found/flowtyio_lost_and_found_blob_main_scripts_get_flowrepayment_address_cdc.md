# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/get_flowRepayment_address.cdc

```
import "LostAndFound"

pub fun main(addr: Address, type: String, ticketID: UInt64): Address? {
    let shelfManager = LostAndFound.borrowShelfManager()
    if let shelf = shelfManager.borrowShelf(redeemer: addr) {
        if let bin = shelf.borrowBin(type: CompositeType(type)!) {
            if let ticket = bin.borrowTicket(id: ticketID) {
                return ticket.getFlowRepaymentAddress()
            }
        }
    }
    return nil
}
 
```