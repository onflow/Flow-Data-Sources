# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_NFT_pack_metadata.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"
import "HWGaragePack"

access(all) fun main(): AnyStruct {
    return HWGaragePack.getPackMetadata()
}
 
```