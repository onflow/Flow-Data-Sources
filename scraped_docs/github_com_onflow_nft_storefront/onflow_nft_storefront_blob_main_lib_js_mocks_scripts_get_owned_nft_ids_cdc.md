# Source: https://github.com/onflow/nft-storefront/blob/main/lib/js/mocks/scripts/get_owned_nft_ids.cdc

```
import NonFungibleToken from "../../../../contracts/utility/NonFungibleToken.cdc"
import ExampleNFT from "../../../../contracts/utility/ExampleNFT.cdc"

pub fun main(address: Address): [UInt64] {
    let account = getAccount(address)

    let collectionRef = account
        .getCapability(ExampleNFT.CollectionPublicPath)
        .borrow<&{NonFungibleToken.CollectionPublic}>()
        ?? panic("Could not borrow capability from public collection")
    
    return collectionRef.getIDs()
}
```