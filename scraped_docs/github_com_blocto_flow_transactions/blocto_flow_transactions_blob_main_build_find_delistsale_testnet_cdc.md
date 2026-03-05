# Source: https://github.com/blocto/flow-transactions/blob/main/build/Find/delistSale.testnet.cdc

```
import FIND from 0x37a05b1ecacc80f7

transaction(name: String) {
	prepare(acct: AuthAccount) {
		let finLeases= acct.borrow<&FIND.LeaseCollection>(from:FIND.LeaseStoragePath)!
		finLeases.delistSale(name)
	}
}
```