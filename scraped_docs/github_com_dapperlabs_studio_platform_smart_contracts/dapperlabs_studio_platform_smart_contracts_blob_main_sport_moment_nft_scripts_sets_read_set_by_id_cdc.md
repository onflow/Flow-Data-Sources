# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/sets/read_set_by_id.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This script returns a Set struct for the given id,
// if it exists

pub fun main(id: UInt64): DapperSport.SetData {
    return DapperSport.getSetData(id: id)!
}


```