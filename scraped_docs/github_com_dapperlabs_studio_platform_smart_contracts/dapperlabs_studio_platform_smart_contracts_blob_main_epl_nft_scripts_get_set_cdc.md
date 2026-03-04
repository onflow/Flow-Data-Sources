# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/scripts/get_set.cdc

```
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"

pub fun main(setID: UInt64): EnglishPremierLeague.Set {
    return EnglishPremierLeague.getSet(id: setID)!
}
```