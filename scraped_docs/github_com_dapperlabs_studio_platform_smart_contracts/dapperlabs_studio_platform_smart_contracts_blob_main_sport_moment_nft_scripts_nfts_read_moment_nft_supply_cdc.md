# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/nfts/read_moment_nft_supply.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"

// This scripts returns the number of DapperSport currently in existence.

pub fun main(): UInt64 {    
    return DapperSport.totalSupply
}


```