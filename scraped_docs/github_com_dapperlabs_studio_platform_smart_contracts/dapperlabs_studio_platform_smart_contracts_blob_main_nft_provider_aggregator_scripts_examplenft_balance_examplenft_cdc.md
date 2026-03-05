# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/nft-provider-aggregator/scripts/exampleNFT/balance_exampleNFT.cdc

```
import NonFungibleToken from "NonFungibleToken"
import ExampleNFT from "ExampleNFT"

access(all) fun main(account: Address): [UInt64] {
    return getAccount(account)
        .capabilities.borrow<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)!.getIDs()
}

```