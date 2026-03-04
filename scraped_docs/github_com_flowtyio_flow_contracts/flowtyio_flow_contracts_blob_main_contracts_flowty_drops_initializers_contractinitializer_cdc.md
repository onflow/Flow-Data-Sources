# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/initializers/ContractInitializer.cdc

```
import "FlowtyDrops"
import "NFTMetadata"
import "AddressUtils"

access(all) contract interface ContractInitializer {
    access(all) fun initialize(contractAcct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account, params: {String: AnyStruct}): NFTMetadata.InitializedCaps
}
```