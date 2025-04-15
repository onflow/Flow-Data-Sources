# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/series/read_all_series_names.cdc

```
import AllDay from "AllDay"

// This script returns all the names for Series.
// These can be related to Series structs via AllDay.getSeriesByName() .

access(all) fun main(): [String] {
    return AllDay.getAllSeriesNames()
}


```