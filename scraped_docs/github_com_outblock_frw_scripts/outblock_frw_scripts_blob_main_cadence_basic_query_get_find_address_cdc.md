# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/get_find_address.cdc

```
import FIND from 0xFind
//Check the status of a fin user
access(all) fun main(name: String) : Address? {
  let status = FIND.status(name)
  return status.owner
}
```