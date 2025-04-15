# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/editions/read_edition_by_id.cdc

```
import AllDay from "AllDay"

// This script returns an Edition for an id number, if it exists.

access(all) fun main(editionID: UInt64): AllDay.EditionData {
    return AllDay.getEditionData(id: editionID)
}


```