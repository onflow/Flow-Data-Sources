# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/nft-provider-aggregator/transactions/destroy_aggregator.cdc

```
import NonFungibleToken from "NonFungibleToken"
import NFTProviderAggregator from "NFTProviderAggregator"

/// Transaction signed by a manager account to destroy their Aggregator resource
///
transaction() {

    prepare(
        manager: auth(LoadValue) &Account,
    ) {
        // Load and destroy the Aggregator resource
        destroy <- manager.storage.load<@NFTProviderAggregator.Aggregator>(
            from: NFTProviderAggregator.AggregatorStoragePath
            )
    }
}

```