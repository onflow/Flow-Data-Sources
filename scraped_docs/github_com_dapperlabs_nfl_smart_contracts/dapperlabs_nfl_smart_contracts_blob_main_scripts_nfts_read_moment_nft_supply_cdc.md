# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/nfts/read_moment_nft_supply.cdc

```
import AllDay from "AllDay"

// This scripts returns the number of AllDay currently in existence.

access(all) fun main(): UInt64 {
    return AllDay.totalSupply
}


```