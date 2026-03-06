# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/pds/get_dist_title.cdc

```
import PDS from "PDS"

access(all) fun main(distId: UInt64): String {
    return PDS.getDistInfo(distId: distId)!.title
}

```