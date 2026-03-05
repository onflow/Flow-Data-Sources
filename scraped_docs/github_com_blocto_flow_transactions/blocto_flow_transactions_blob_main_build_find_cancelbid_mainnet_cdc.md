# Source: https://github.com/blocto/flow-transactions/blob/main/build/Find/cancelBid.mainnet.cdc

```
import FIND from 0x097bafa4e0b48eef

transaction(name: String) {
	prepare(account: AuthAccount) {
		let bids = account.borrow<&FIND.BidCollection>(from: FIND.BidStoragePath)!
		bids.cancelBid(name)
	}
}
```