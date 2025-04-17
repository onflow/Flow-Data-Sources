# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/lostAndFound/query/query_unclaimed_fts.cdc

```
import LostAndFound from 0xLostAndFound
import MetadataViews from 0xMetadataViews
import FungibleToken from 0xFungibleToken

access(all) fun main(addr: Address): [AnyStruct?] {
  let tickets = LostAndFound.borrowAllTickets(addr: addr)
  
  let displayArr: [AnyStruct?]  = []
  for ticket in tickets {
    if ticket.type.isSubtype(of: Type<@{FungibleToken.Vault}>()) { 
      displayArr.append({"display": ticket.display, "balance": ticket.getFungibleTokenBalance()})
    }
  }
  return displayArr
}
```