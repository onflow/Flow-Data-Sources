# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/editions/read_edition_by_id.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This script returns an Edition for an id number, if it exists.

pub fun main(editionID: UInt64): DapperSport.EditionData {
    return DapperSport.getEditionData(id: editionID)!
}


```