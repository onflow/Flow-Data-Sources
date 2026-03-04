# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/nft/OpenEditionNFT.cdc

```
import "NonFungibleToken"
import "FlowtyDrops"
import "BaseNFT"
import "NFTMetadata"
import "UniversalCollection"
import "ContractBorrower"
import "BaseCollection"

access(all) contract OpenEditionNFT: BaseCollection {
    access(all) var MetadataCap: Capability<&NFTMetadata.Container>
    access(all) var totalSupply: UInt64

    access(all) resource NFT: BaseNFT.NFT {
        access(all) let id: UInt64
        access(all) let metadataID: UInt64

        init() {
            OpenEditionNFT.totalSupply = OpenEditionNFT.totalSupply + 1
            self.id = OpenEditionNFT.totalSupply
            self.metadataID = 0
        }
    }

    access(all) resource NFTMinter: FlowtyDrops.Minter {
        access(contract) fun createNextNFT(): @{NonFungibleToken.NFT} {
            return <- create NFT()
        }
    }

    access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {
        return <- UniversalCollection.createCollection(nftType: Type<@NFT>())
    }

    init(params: {String: AnyStruct}, initializeIdentifier: String) {
        self.totalSupply = 0
        self.account.storage.save(<- create NFTMinter(), to: FlowtyDrops.getMinterStoragePath(type: self.getType()))
        params["minterController"] = self.account.capabilities.storage.issue<&{FlowtyDrops.Minter}>(FlowtyDrops.getMinterStoragePath(type: self.getType()))
        params["type"] = Type<@NFT>()

        self.MetadataCap = ContractBorrower.borrowInitializer(typeIdentifier: initializeIdentifier).initialize(contractAcct: self.account, params: params).pubCap
    }
}
```