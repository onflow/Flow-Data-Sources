# Source: https://github.com/blocto/flow-transactions/blob/main/build/Find/rejectDirectOffer.mainnet.cdc

```
import FIND from 0x097bafa4e0b48eef

transaction(name: String) {
	prepare(account: AuthAccount) {

		let finLeases= account.borrow<&FIND.LeaseCollection>(from:FIND.LeaseStoragePath)!
		finLeases.cancel(name)

	}
}
```