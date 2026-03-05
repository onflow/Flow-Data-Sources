# Source: https://github.com/blocto/flow-transactions/blob/main/build/Find/cancelBid.testnet.cdc

```
import FIND from 0x37a05b1ecacc80f7

transaction(name: String) {
	prepare(account: AuthAccount) {
		let bids = account.borrow<&FIND.BidCollection>(from: FIND.BidStoragePath)!
		bids.cancelBid(name)
	}
}
```