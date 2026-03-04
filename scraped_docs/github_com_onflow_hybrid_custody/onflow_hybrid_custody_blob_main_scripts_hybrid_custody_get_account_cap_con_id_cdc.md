# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/get_account_cap_con_id.cdc

```
import "HybridCustody"

access(all) fun main(addr: Address): UInt64? {
    let acct: auth(Capabilities) &Account = getAuthAccount<auth(Capabilities) &Account>(addr)
    let controllers = acct.capabilities.account.getControllers()
    if controllers.length == 0 {
        return nil
    }

    return controllers[0].capabilityID
}
```