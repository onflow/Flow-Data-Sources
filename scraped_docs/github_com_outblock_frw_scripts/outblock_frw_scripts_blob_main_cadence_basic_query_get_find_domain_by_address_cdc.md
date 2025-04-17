# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/get_find_domain_by_address.cdc

```
import FIND from 0xFind

access(all) fun main(address: Address) : String?{
  return FIND.reverseLookup(address)
}
```