# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/sets/read_all_set_names.cdc

```
import Golazos from "Golazos"

// This script returns all the names for Set.
// These can be related to Set structs via Golazos.getSetByName() .

access(all) fun main(): [String] {
    return Golazos.getAllSetNames()
}


```