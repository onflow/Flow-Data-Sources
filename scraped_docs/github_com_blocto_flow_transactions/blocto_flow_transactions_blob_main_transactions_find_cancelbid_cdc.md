# Source: https://github.com/blocto/flow-transactions/blob/main/transactions/Find/cancelBid.cdc

```
import FIND from 0xFIND_ADDRESS

transaction(name: String) {
	prepare(account: AuthAccount) {
		let bids = account.borrow<&FIND.BidCollection>(from: FIND.BidStoragePath)!
		bids.cancelBid(name)
	}
}


```