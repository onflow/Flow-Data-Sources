# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/locked-nft/scripts/get_locked_token.cdc

```
import NFTLocker from "NFTLocker"
import ExampleNFT from "ExampleNFT"

access(all) fun main(id: UInt64): NFTLocker.LockedData? {
    return NFTLocker.getNFTLockerDetails(id: id, nftType: Type<@ExampleNFT.NFT>())
}
```