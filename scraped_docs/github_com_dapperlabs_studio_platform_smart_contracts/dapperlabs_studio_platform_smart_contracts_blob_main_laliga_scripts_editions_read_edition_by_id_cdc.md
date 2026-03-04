# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/editions/read_edition_by_id.cdc

```
import Golazos from "Golazos"

// This script returns an Edition for an id number, if it exists.

access(all) fun main(editionID: UInt64): Golazos.EditionData {
    return Golazos.getEditionData(id: editionID)!
}


```