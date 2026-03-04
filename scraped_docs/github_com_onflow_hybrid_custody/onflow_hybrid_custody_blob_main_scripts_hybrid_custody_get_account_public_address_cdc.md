# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/get_account_public_address.cdc

```
import "HybridCustody"

access(all) fun main(parent: Address, child: Address): Address {
    let cap = getAccount(parent).capabilities.get<&{HybridCustody.ManagerPublic}>(HybridCustody.ManagerPublicPath)
    let manager = cap.borrow()
        ?? panic("unable to borrow manager")

    let acct = manager.borrowAccountPublic(addr: child)
        ?? panic("child account not found")

    return acct.getAddress()
}
```