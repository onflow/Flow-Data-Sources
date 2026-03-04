# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/has_phase_started.cdc

```
import "FlowtyDrops"
import "ViewResolver"
import "AddressUtils"

access(all) fun main(nftTypeIdentifier: String, dropID: UInt64, phaseIndex: Int): Bool {
    let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
    let segments = nftTypeIdentifier.split(separator: ".")
    let contractAddress = AddressUtils.parseAddress(nftType)!
    let contractName = segments[2]

    let resolver = getAccount(contractAddress).contracts.borrow<&{ViewResolver}>(name: contractName)
        ?? panic("contract does not implement ViewResolver interface")

    let dropResolver = resolver.resolveContractView(resourceType: nftType, viewType: Type<FlowtyDrops.DropResolver>())! as! FlowtyDrops.DropResolver

    let container = dropResolver.borrowContainer()
        ?? panic("drop container not found")

    let drop = container.borrowDropPublic(id: dropID)
        ?? panic("drop not found")

    let phase = drop.borrowPhasePublic(index: phaseIndex)

    return phase.getDetails().activeChecker.hasStarted()
}
```