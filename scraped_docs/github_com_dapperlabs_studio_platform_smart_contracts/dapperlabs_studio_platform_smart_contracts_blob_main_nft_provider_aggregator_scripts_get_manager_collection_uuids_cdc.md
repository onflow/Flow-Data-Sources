# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/nft-provider-aggregator/scripts/get_manager_collection_uuids.cdc

```
import NFTProviderAggregator from "NFTProviderAggregator"

// Get the UUIDs of the collection added to the parent Aggregator resource
access(all) fun main(account: Address): [UInt64] {
    return getAuthAccount<auth(BorrowValue) &Account>(account).storage.borrow<
        &NFTProviderAggregator.Aggregator>(from:
        NFTProviderAggregator.AggregatorStoragePath)!.getCollectionUUIDs()
}

```