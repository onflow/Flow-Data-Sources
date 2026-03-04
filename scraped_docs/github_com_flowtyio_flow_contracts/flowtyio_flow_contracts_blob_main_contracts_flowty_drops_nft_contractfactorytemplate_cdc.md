# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/nft/ContractFactoryTemplate.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "ViewResolver"

import "FlowtyDrops"
import "BaseNFT"
import "BaseCollection"
import "NFTMetadata"
import "UniversalCollection"
import "ContractBorrower"

import "AddressUtils"

access(all) contract interface ContractFactoryTemplate {
    access(all) fun createContract(acct: auth(Contracts) &Account, name: String, params: {String: AnyStruct}, initializeIdentifier: String)

    access(all) fun getContractAddresses(): {String: Address} {
        let d: {String: Address} = {
            "NonFungibleToken": AddressUtils.parseAddress(Type<&{NonFungibleToken}>())!,
            "MetadataViews": AddressUtils.parseAddress(Type<&MetadataViews>())!,
            "ViewResolver": AddressUtils.parseAddress(Type<&{ViewResolver}>())!,
            "FlowtyDrops": AddressUtils.parseAddress(Type<&FlowtyDrops>())!,
            "BaseNFT": AddressUtils.parseAddress(Type<&{BaseNFT}>())!,
            "BaseCollection": AddressUtils.parseAddress(Type<&{BaseCollection}>())!,
            "NFTMetadata": AddressUtils.parseAddress(Type<&NFTMetadata>())!,
            "UniversalCollection": AddressUtils.parseAddress(Type<&UniversalCollection>())!,
            "BaseCollection": AddressUtils.parseAddress(Type<&{BaseCollection}>())!,
            "AddressUtils": AddressUtils.parseAddress(Type<&AddressUtils>())!,
            "ContractBorrower": AddressUtils.parseAddress(Type<ContractBorrower>())!
        }

        return d
    }

    access(all) fun importLine(name: String, addr: Address): String {
        return "import ".concat(name).concat(" from ").concat(addr.toString()).concat("\n")
    }

    access(all) fun generateImports(names: [String]): String {
        let addresses = self.getContractAddresses()
        var imports = ""
        for n in names {
            imports = imports.concat(self.importLine(name: n, addr: addresses[n] ?? panic("missing contract import address: ".concat(n))))
        }

        return imports
    }
}
```