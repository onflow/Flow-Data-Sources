# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/sets/read_set_by_id.cdc

```
import Golazos from "Golazos"

// This script returns a Set struct for the given id,
// if it exists

access(all) fun main(id: UInt64): Golazos.SetData {
    return Golazos.getSetData(id: id)!
}


```