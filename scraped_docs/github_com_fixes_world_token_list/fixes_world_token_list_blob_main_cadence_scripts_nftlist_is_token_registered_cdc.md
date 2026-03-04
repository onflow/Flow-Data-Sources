# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/nftlist/is-token-registered.cdc

```
import "NFTList"

access(all)
fun main(
    address: Address,
    contractName: String,
): Bool {
    return NFTList.isNFTCollectionRegistered(address, contractName)
}

```