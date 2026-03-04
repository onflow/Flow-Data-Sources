# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/dss-collection-nft/scripts/get_collection_group.cdc

```
import DSSCollection from "../../contracts/DSSCollection.cdc"

pub fun main(collectionGroupID: UInt64): DSSCollection.CollectionGroupData {
    return DSSCollection.getCollectionGroupData(id: collectionGroupID)
}
```