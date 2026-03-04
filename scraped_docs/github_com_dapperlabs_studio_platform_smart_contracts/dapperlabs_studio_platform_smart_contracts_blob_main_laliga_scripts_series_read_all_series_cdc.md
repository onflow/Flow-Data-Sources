# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/series/read_all_series.cdc

```
import Golazos from "Golazos"

// This script returns all the Series structs.
// This will eventually be *long*.

access(all) fun main(): [Golazos.SeriesData] {
    let series: [Golazos.SeriesData] = []
    var id: UInt64 = 1
    // Note < , as nextSeriesID has not yet been used
    while id < Golazos.nextSeriesID {
        series.append(Golazos.getSeriesData(id: id))
        id = id + 1
    }
    return series
}


```