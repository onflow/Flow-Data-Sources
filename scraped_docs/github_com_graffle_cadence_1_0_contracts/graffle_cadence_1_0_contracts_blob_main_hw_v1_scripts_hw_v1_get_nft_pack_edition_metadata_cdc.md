# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_NFT_pack_edition_metadata.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"
import "HWGaragePack"

access(all) fun main(edition: UInt64): {String: String} {
    return HWGaragePack.getEditionMetadata(edition)
}
 
```