# Source: https://github.com/blocto/flow-transactions/blob/main/build/Find/fulfill.testnet.cdc

```
import FIND from 0x37a05b1ecacc80f7

transaction(name: String) {
	prepare(account: AuthAccount) {

		let finLeases= account.borrow<&FIND.LeaseCollection>(from:FIND.LeaseStoragePath)!
		finLeases.fulfill(name)

	}
}
```