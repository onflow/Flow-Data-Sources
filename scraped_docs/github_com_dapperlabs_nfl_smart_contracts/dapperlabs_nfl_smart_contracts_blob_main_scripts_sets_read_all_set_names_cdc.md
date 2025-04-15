# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/sets/read_all_set_names.cdc

```
import AllDay from "AllDay"

// This script returns all the names for Set.
// These can be related to Set structs via AllDay.getSetByName() .

access(all) fun main(): [String] {
    return AllDay.getAllSetNames()
}


```