# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/initializers/ContractBorrower.cdc

```
import "FlowtyDrops"
import "NFTMetadata"
import "AddressUtils"
import "ContractInitializer"

access(all) contract ContractBorrower {
    access(all) fun borrowInitializer(typeIdentifier: String): &{ContractInitializer} {
        let type = CompositeType(typeIdentifier) ?? panic("invalid type identifier")
        let addr = AddressUtils.parseAddress(type)!

        let contractName = type.identifier.split(separator: ".")[2]
        return getAccount(addr).contracts.borrow<&{ContractInitializer}>(name: contractName)!
    }
}
```