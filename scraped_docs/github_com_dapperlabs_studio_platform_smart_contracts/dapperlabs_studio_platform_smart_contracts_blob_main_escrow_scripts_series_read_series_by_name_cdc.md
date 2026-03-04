# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/escrow/scripts/series/read_series_by_name.cdc

```
import AllDay from "AllDay"

// This script returns all the names for Set.
// These can be related to Set structs via AllDay.getSetByName() .

access(all) fun main(): [String] {
    return AllDay.getAllSetNames()
}


```