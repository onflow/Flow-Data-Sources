# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/lostAndFound/query/query_unclaimed_number.cdc

```
import LostAndFound from 0xLostAndFound

access(all) fun main(addr: Address): Int {
  let shelfManager = LostAndFound.borrowShelfManager()
  let shelf = shelfManager.borrowShelf(redeemer: addr)
  if shelf == nil {
    return 0
  }
  
  return shelf!.getRedeemableTypes().length
}
```