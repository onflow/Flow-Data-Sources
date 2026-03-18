# Source: https://github.com/blocto/flow-transactions/blob/main/transactions/Find/startAuction.cdc

```
import FIND from 0xFIND_ADDRESS

transaction(name: String) {
	prepare(account: AuthAccount) {

		let finLeases= account.borrow<&FIND.LeaseCollection>(from:FIND.LeaseStoragePath)!
		finLeases.startAuction(name)

	}
}


```