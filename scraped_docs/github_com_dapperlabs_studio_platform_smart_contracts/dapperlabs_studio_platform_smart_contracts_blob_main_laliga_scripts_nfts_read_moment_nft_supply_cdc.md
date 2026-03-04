# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/laliga/scripts/nfts/read_moment_nft_supply.cdc

```
import Golazos from "Golazos"

// This scripts returns the number of Golazos currently in existence.

access(all) fun main(): UInt64 {    
    return Golazos.totalSupply
}


```