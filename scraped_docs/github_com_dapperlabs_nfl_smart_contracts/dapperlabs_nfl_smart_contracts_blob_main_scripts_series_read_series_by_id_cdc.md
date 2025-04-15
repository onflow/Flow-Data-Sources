# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/series/read_series_by_id.cdc

```
import AllDay from "AllDay"

// This script returns a Series struct for the given id,
// if it exists

access(all) fun main(id: UInt64): AllDay.SeriesData {
    return AllDay.getSeriesData(id: id)
}


```