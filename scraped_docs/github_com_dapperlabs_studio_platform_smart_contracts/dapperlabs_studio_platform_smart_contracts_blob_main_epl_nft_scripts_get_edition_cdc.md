# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/scripts/get_edition.cdc

```
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"

pub fun main(editionID: UInt64): EnglishPremierLeague.Edition {
    return EnglishPremierLeague.getEdition(id: editionID)!
}
```