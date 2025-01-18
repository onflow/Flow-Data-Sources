# Source: https://github.com/onflow/flow-ft/blob/master/transactions/tokenForwarder/scripts/is_recipient_valid.cdc

```
import "TokenForwarding"

access(all) fun main(addr: Address, tokenForwardingPath: PublicPath): Bool {
    let forwarderRef = getAccount(addr)
                       .capabilities.borrow<&{TokenForwarding.ForwarderPublic}>(tokenForwardingPath)

    return forwarderRef.check()
}
```