# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/factory/get_supported_types_from_manager.cdc

```
import "CapabilityFactory"

import "NonFungibleToken"

access(all) fun main(address: Address): [Type] {
    let getterRef = getAccount(address).capabilities.get<&CapabilityFactory.Manager>(CapabilityFactory.PublicPath)
        .borrow() ?? panic("CapabilityFactory Getter not found")
    return getterRef.getSupportedTypes()
}
```