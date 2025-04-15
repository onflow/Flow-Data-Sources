# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/hybridCustody/unlink_child_account.cdc

```
import HybridCustody from 0xHybridCustody

transaction(child: Address) {
    prepare (acct: AuthAccount) {
        let manager = acct.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("manager not found")
        manager.removeChild(addr: child)
    }
}
```