# Source: https://github.com/onflow/flow-nft/blob/master/transactions/scripts/get_contract_views.cdc

```
/// This script checks all the supported views from
/// the ExampleNFT contract. Used for testing only.

import "ExampleNFT"
import "MetadataViews"

access(all) fun main(): [Type] {
    return ExampleNFT.getContractViews(resourceType: nil)
}

```