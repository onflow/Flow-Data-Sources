# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/nft/get_evm_pointer_from_identifier.cdc

```
import "CrossVMMetadataViews"

import "FlowEVMBridgeUtils"

access(all)
fun main(nftTypeIdentifier: String): CrossVMMetadataViews.EVMPointer? {
    if let nftType = CompositeType(nftTypeIdentifier) {
        return FlowEVMBridgeUtils.getEVMPointerView(forType: nftType)
    }
    return nil
}

```