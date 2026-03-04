# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_NFT_pack_totalSupply.cdc

```
import "HWGaragePack"

access(all) fun main(): UInt64 {
    return HWGaragePack.getTotalSupply()
}
 
```