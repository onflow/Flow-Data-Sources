# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/nft-provider-aggregator/scripts/get_aggregator_uuid.cdc

```
import NFTProviderAggregator from "NFTProviderAggregator"

// Get the UUIDs of the parent Aggregator resource
access(all) fun main(account: Address): UInt64 {
    return getAccount(account).capabilities.borrow<
        &NFTProviderAggregator.Supplier>(
        NFTProviderAggregator.SupplierPublicPath)!.getAggregatorUUID()
}

```