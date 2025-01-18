# Source: https://github.com/onflow/flow-nft/blob/master/transactions/scripts/get_collection_data.cdc

```
import MetadataViews from "MetadataViews"
import ExampleNFT from "ExampleNFT"

access(all) fun main(): MetadataViews.NFTCollectionData? {
    return ExampleNFT.getCollectionData(nftType: Type<@ExampleNFT.NFT>()) as MetadataViews.NFTCollectionData?
}
```