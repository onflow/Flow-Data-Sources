# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/series/read_all_series_names.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This script returns all the names for Series.
// These can be related to Series structs via DapperSport.getSeriesByName() .

pub fun main(): [String] {
    return DapperSport.getAllSeriesNames()
}


```