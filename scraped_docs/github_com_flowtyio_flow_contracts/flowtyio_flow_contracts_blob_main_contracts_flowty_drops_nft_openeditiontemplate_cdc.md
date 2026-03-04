# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/nft/OpenEditionTemplate.cdc

```
import "ContractFactoryTemplate"
import "MetadataViews"
import "NFTMetadata"

access(all) contract OpenEditionTemplate: ContractFactoryTemplate {
    access(all) fun createContract(acct: auth(Contracts) &Account, name: String, params: {String: AnyStruct}, initializeIdentifier: String) {
        let code = self.generateImports(names: [
            "NonFungibleToken",
            "FlowtyDrops",
            "BaseNFT",
            "NFTMetadata",
            "UniversalCollection",
            "ContractBorrower",
            "BaseCollection",
            "ViewResolver"
        ]).concat("\n\n")
        .concat("access(all) contract ").concat(name).concat(": BaseCollection, ViewResolver {\n")
        .concat("    access(all) var MetadataCap: Capability<&NFTMetadata.Container>\n")
        .concat("    access(all) var totalSupply: UInt64\n")
        .concat("\n\n")
        .concat("    access(all) resource NFT: BaseNFT.NFT {\n")
        .concat("        access(all) let id: UInt64\n")
        .concat("        access(all) let metadataID: UInt64\n")
        .concat("\n\n")
        .concat("        init() {\n")
        .concat("            ").concat(name).concat(".totalSupply = ").concat(name).concat(".totalSupply + 1\n")
        .concat("            self.id = ").concat(name).concat(".totalSupply\n")
        .concat("            self.metadataID = 0\n")
        .concat("        }\n")
        .concat("    }\n")
        .concat("    access(all) resource NFTMinter: FlowtyDrops.Minter {\n")
        .concat("        access(contract) fun createNextNFT(): @{NonFungibleToken.NFT} {\n")
        .concat("            return <- create NFT()\n")
        .concat("        }\n")
        .concat("    }\n")
        .concat("\n")
        .concat("    access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {\n")
        .concat("        return <- UniversalCollection.createCollection(nftType: Type<@NFT>())\n")
        .concat("    }\n")
        .concat("\n")
        .concat("    init(params: {String: AnyStruct}, initializeIdentifier: String) {\n")
        .concat("        self.totalSupply = 0\n")
        .concat("        let minter <- create NFTMinter()\n")
        .concat("        self.account.storage.save(<-minter, to: FlowtyDrops.getMinterStoragePath(type: self.getType()))\n")
        .concat("        params[\"minterController\"] = self.account.capabilities.storage.issue<&{FlowtyDrops.Minter}>(FlowtyDrops.getMinterStoragePath(type: self.getType()))\n")
        .concat("        params[\"type\"] = Type<@NFT>()\n")
        .concat("\n\n")
        .concat("        self.MetadataCap = ContractBorrower.borrowInitializer(typeIdentifier: initializeIdentifier).initialize(contractAcct: self.account, params: params).pubCap\n")
        .concat("    }\n")
        .concat("}\n")

        acct.contracts.add(name: name, code: code.utf8, params, initializeIdentifier)
    }
}

```