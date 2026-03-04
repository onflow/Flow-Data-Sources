# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/get_drop_ids.cdc

```
import "FlowtyDrops"
import "ViewResolver"
import "AddressUtils"

access(all) fun main(nftTypeIdentifier: String): [UInt64] {
    let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
    let segments = nftTypeIdentifier.split(separator: ".")
    let contractAddress = AddressUtils.parseAddress(nftType)!
    let contractName = segments[2]

    let resolver = getAccount(contractAddress).contracts.borrow<&{ViewResolver}>(name: contractName)
    if resolver == nil {
        return []
    }

    let tmp = resolver!.resolveContractView(resourceType: nftType, viewType: Type<FlowtyDrops.DropResolver>())
    if tmp == nil {
        return []
    }

    let dropResolver = tmp! as! FlowtyDrops.DropResolver

    if let dropContainer = dropResolver.borrowContainer() {
        return dropContainer.getIDs()
    }

    return []
}
```