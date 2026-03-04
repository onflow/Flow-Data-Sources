# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/dss-collection-nft/scripts/get_collection_group_nft_count.cdc

```
import DSSCollection from "../../contracts/DSSCollection.cdc"

pub fun main(collectionGroupId: UInt64): UInt64 {
    let count = DSSCollection.collectionGroupNFTCount[collectionGroupId] ?? 0
    return count
}

```