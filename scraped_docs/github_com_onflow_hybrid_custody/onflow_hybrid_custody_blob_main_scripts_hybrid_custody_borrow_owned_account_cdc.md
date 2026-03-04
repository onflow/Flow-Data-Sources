# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/borrow_owned_account.cdc

```
import "HybridCustody"

access(all) fun main(owner: Address, child: Address): Address {
    let m = getAuthAccount<auth(Storage) &Account>(owner).storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("manager could not be borrowed")
    let ownedAcct = m.borrowOwnedAccount(addr: child)
        ?? panic("could not borrow owned account")
        
    let acct = ownedAcct.borrowAccount()
    return acct.address
}
```