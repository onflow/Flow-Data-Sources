# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/escrow/scripts/editions/read_edition_by_id.cdc

```
import AllDay from "AllDay"

// This script returns an Edition for an id number, if it exists.

access(all) fun main(editionID: UInt64): AllDay.EditionData {
    return AllDay.getEditionData(id: editionID)
}


```