# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/nft/get_evm_id_from_evm_nft.cdc

```
import "NonFungibleToken"

import "CrossVMNFT"

access(all)
fun main(ownerAddr: Address, cadenceID: UInt64, collectionStoragePath: StoragePath): UInt256? {
    if let collection = getAuthAccount<auth(BorrowValue) &Account>(ownerAddr).storage.borrow<&{NonFungibleToken.Collection}>(
            from: collectionStoragePath
        ) {
        if let nft = collection.borrowNFT(cadenceID) {
            return CrossVMNFT.getEVMID(from: nft)
        }
    }
    return nil
}

```