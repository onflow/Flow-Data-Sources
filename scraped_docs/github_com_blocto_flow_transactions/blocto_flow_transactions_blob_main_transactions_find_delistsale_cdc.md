# Source: https://github.com/blocto/flow-transactions/blob/main/transactions/Find/delistSale.cdc

```
import FIND from 0xFIND_ADDRESS

transaction(name: String) {
	prepare(acct: AuthAccount) {
		let finLeases= acct.borrow<&FIND.LeaseCollection>(from:FIND.LeaseStoragePath)!
		finLeases.delistSale(name)
	}
}


```