# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/scripts/get_tag.cdc

```
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"

pub fun main(tagID: UInt64): EnglishPremierLeague.Tag {
    return EnglishPremierLeague.getTag(id: tagID)!
}
```