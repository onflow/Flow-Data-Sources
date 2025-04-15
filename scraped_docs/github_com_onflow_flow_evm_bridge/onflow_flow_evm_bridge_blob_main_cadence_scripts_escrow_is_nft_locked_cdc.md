# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/escrow/is_nft_locked.cdc

```
import "NonFungibleToken"

import "FlowEVMBridgeNFTEscrow"
import "FlowEVMBridge"

/// Returns true if the NFT is locked in escrow and false otherwise.
///
/// @param nftTypeIdentifier: The type identifier of the NFT
/// @param id: The ID of the NFT
///
/// @return true if the NFT is locked in escrow and false otherwise
///
access(all) fun main(nftTypeIdentifier: String, id: UInt64): Bool {
    let type = CompositeType(nftTypeIdentifier) ?? panic("Malformed NFT type identifier=".concat(nftTypeIdentifier))
    return FlowEVMBridgeNFTEscrow.isLocked(type: type, id: id)
}

```