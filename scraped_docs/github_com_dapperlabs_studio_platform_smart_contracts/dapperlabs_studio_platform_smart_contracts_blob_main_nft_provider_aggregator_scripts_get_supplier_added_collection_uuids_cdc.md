# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/nft-provider-aggregator/scripts/get_supplier_added_collection_uuids.cdc

```
import NFTProviderAggregator from "NFTProviderAggregator"

// Get the UUIDs of the collection added by the provided account
access(all) fun main(account: Address): [UInt64] {
        return getAccount(account).capabilities.borrow<
        &NFTProviderAggregator.Supplier>(
        NFTProviderAggregator.SupplierPublicPath)!.getSupplierAddedCollectionUUIDs()
}

```