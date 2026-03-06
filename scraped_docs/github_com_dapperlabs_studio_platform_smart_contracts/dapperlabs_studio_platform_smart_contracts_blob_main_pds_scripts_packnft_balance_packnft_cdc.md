# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/packNFT/balance_packNFT.cdc

```
import NonFungibleToken from "NonFungibleToken"
import PackNFT from "PackNFT"

access(all) fun main(account: Address): [UInt64] {
    let collectionRef = getAccount(account).capabilities.borrow<
        &PackNFT.Collection>(PackNFT.CollectionPublicPath)!

    return collectionRef.getIDs()
}

```