# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/packNFT/packNFT_total_supply.cdc

```
import PackNFT from "PackNFT"

access(all) fun main(): UInt64{
    return PackNFT.totalSupply
}

```