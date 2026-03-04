# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/scripts/get_series.cdc

```
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"

pub fun main(seriesID: UInt64): EnglishPremierLeague.Series {
    return EnglishPremierLeague.getSeries(id: seriesID)!
}
```