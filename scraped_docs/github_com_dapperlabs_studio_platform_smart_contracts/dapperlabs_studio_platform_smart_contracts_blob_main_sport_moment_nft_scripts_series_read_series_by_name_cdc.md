# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/series/read_series_by_name.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This script returns a Series struct for the given name,
// if it exists

pub fun main(seriesName: String): DapperSport.SeriesData {
    return DapperSport.getSeriesDataByName(name: seriesName)!
}


```