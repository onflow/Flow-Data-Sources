# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/initializers/OpenEditionInitializer.cdc

```
import "ContractInitializer"
import "NFTMetadata"
import "FlowtyDrops"
import "NonFungibleToken"
import "UniversalCollection"

access(all) contract OpenEditionInitializer: ContractInitializer {
    access(all) fun initialize(contractAcct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account, params: {String: AnyStruct}): NFTMetadata.InitializedCaps {
        pre {
            params["data"] != nil: "missing param data"
            params["data"]!.getType() == Type<NFTMetadata.Metadata>(): "data param must be of type NFTMetadata.Metadata"
            params["collectionInfo"] != nil: "missing param collectionInfo"
            params["collectionInfo"]!.getType() == Type<NFTMetadata.CollectionInfo>(): "collectionInfo param must be of type NFTMetadata.CollectionInfo"
            params["type"] != nil: "missing param type"
            params["type"]!.getType() == Type<Type>(): "type param must be of type Type"
        }

        let data = params["data"]! as! NFTMetadata.Metadata
        let collectionInfo = params["collectionInfo"]! as! NFTMetadata.CollectionInfo

        let nftType = params["type"]! as! Type
        let contractName = nftType.identifier.split(separator: ".")[2]

        // do we have information to setup a drop as well?
        if params.containsKey("dropDetails") && params.containsKey("phaseDetails") && params.containsKey("minterController") {
            // extract expected keys
            let minterCap = params["minterController"]! as! Capability<&{FlowtyDrops.Minter}>
            let dropDetails = params["dropDetails"]! as! FlowtyDrops.DropDetails
            let phaseDetails = params["phaseDetails"]! as! [FlowtyDrops.PhaseDetails]

            assert(minterCap.check(), message: "invalid minter capability")
            assert(CompositeType(dropDetails.nftType) != nil, message: "dropDetails.nftType must be a valid CompositeType")

            let phases: @[FlowtyDrops.Phase] <- []
            for p in phaseDetails {
                phases.append(<- FlowtyDrops.createPhase(details: p))
            }

            let drop <- FlowtyDrops.createDrop(details: dropDetails, minterCap: minterCap, phases: <- phases)
            if contractAcct.storage.borrow<&AnyResource>(from: FlowtyDrops.ContainerStoragePath) == nil {
                contractAcct.storage.save(<- FlowtyDrops.createContainer(), to: FlowtyDrops.ContainerStoragePath)

                contractAcct.capabilities.unpublish(FlowtyDrops.ContainerPublicPath)
                contractAcct.capabilities.publish(
                    contractAcct.capabilities.storage.issue<&{FlowtyDrops.ContainerPublic}>(FlowtyDrops.ContainerStoragePath),
                    at: FlowtyDrops.ContainerPublicPath
                )
            }

            let container = contractAcct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath)
                ?? panic("drops container not found")
            container.addDrop(<- drop)
        }
        
        let caps = NFTMetadata.initialize(acct: contractAcct, collectionInfo: collectionInfo, nftType: nftType)
        caps.ownerCap.borrow()!.addMetadata(id: 0, data: data)

        return caps
    }
}
```