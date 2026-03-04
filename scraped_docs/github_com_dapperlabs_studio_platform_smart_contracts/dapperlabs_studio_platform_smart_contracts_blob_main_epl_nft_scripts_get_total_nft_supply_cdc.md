# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/scripts/get_total_nft_supply.cdc

```
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"


pub fun main(): UInt64 {    
    return EnglishPremierLeague.totalSupply
}


```