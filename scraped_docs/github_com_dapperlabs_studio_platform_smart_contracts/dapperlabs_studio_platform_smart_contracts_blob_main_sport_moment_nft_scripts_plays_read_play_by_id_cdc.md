# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/plays/read_play_by_id.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This script returns a Play struct for the given id,
// if it exists

pub fun main(id: UInt64): DapperSport.PlayData {
    return DapperSport.getPlayData(id: id)!
}


```