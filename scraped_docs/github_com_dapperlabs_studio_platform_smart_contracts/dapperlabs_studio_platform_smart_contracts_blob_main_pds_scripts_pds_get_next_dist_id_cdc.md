# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/pds/get_next_dist_id.cdc

```
import PDS from "PDS"

access(all) fun main(): UInt64 {
    return PDS.nextDistId
}

```