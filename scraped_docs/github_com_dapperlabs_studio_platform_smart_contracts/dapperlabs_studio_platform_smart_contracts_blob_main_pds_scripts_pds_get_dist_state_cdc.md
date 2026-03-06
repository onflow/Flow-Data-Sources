# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/pds/get_dist_state.cdc

```
import PDS from "PDS"

access(all) fun main(distId: UInt64): UInt8 {
    return PDS.getDistInfo(distId: distId)!.state.rawValue
}

```