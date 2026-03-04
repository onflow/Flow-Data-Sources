# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/get_redeemable_types_for_addr.cdc

```
import "LostAndFound"

pub fun main(addr: Address): [Type] {
    let shelfManager = LostAndFound.borrowShelfManager()
    let shelf = shelfManager.borrowShelf(redeemer: addr)
    if shelf == nil {
        return []
    }
    
    return shelf!.getRedeemableTypes()
}

```