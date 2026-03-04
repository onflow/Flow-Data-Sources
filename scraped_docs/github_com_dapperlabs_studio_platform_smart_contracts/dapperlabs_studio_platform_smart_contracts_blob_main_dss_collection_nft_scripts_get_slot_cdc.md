# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/dss-collection-nft/scripts/get_slot.cdc

```
import DSSCollection from "../../contracts/DSSCollection.cdc"

pub fun main(slotID: UInt64): DSSCollection.SlotData {
    return DSSCollection.getSlotData(id: slotID)
}
```