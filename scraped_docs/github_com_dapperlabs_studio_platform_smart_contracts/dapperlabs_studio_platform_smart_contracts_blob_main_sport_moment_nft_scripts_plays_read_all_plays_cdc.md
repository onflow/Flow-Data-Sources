# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/plays/read_all_plays.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This script returns all the Set structs.
// This will eventually be *long*.

pub fun main(): [DapperSport.PlayData] {
    let plays: [DapperSport.PlayData] = []
    var id: UInt64 = 1
    // Note < , as nextPlayID has not yet been used
    while id < DapperSport.nextPlayID {
        plays.append(DapperSport.getPlayData(id: id)!)
        id = id + 1
    }
    return plays
}


```