# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/escrow/scripts/sets/read_set_by_id.cdc

```
import AllDay from "AllDay"

// This script returns a Set struct for the given id,
// if it exists

access(all) fun main(id: UInt64): AllDay.SetData {
    return AllDay.getSetData(id: id)
}


```