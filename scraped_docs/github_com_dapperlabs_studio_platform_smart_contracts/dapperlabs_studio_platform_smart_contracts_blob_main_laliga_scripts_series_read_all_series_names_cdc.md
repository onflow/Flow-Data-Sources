# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/series/read_all_series_names.cdc

```
import Golazos from "Golazos"

// This script returns all the names for Series.
// These can be related to Series structs via Golazos.getSeriesByName() .

access(all) fun main(): [String] {
    return Golazos.getAllSeriesNames()
}


```