# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/series/read_series_by_id.cdc

```
import Golazos from "Golazos"

// This script returns a Series struct for the given id,
// if it exists

access(all) fun main(id: UInt64): Golazos.SeriesData {
    return Golazos.getSeriesData(id: id)
}


```