# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/plays/read_play_by_id.cdc

```
import Golazos from "Golazos"

// This script returns a Play struct for the given id,
// if it exists

access(all) fun main(id: UInt64): Golazos.PlayData {
    return Golazos.getPlayData(id: id)!
}


```