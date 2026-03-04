# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/lost-and-found/get_shelf_owner.cdc

```
import "LostAndFound"

access(all) fun main(addr: Address): Address {
    let m = LostAndFound.borrowShelfManager()
    let shelf = m.borrowShelf(redeemer: addr)!
    return shelf.getOwner()
}
```