# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/locked-nft/scripts/is_account_setup.cdc

```
import NonFungibleToken from "NonFungibleToken"
import NFTLocker from "NFTLocker"

access(all) fun main(address: Address): Bool {
    return getAccount(address).capabilities.get<&{NFTLocker.LockedCollection}>(NFTLocker.CollectionPublicPath).check()
}
```