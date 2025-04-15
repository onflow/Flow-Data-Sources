# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/series/read_series_by_name.cdc

```
import AllDay from "AllDay"

// This script returns a Series struct for the given name,
// if it exists

access(all) fun main(seriesName: String): AllDay.SeriesData {
    return AllDay.getSeriesDataByName(name: seriesName)
}


```