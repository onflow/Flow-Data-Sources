# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/nft-provider-aggregator/scripts/get_ids.cdc

```
import NFTProviderAggregator from "NFTProviderAggregator"

// Get the NFT IDs of all the NFTs contained in the collections added to the Aggregator resource
access(all) fun main(account: Address): [UInt64] {
    return getAccount(account).capabilities.borrow<
        &NFTProviderAggregator.Supplier>(
        NFTProviderAggregator.SupplierPublicPath)!.getIDs()
}

```