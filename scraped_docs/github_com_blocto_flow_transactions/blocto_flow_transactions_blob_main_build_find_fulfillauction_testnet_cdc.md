# Source: https://github.com/blocto/flow-transactions/blob/main/build/Find/fulfillAuction.testnet.cdc

```
import FIND from 0x37a05b1ecacc80f7

transaction(owner: Address, name: String) {
	prepare(account: AuthAccount) {

		let leaseCollection = getAccount(owner).getCapability<&FIND.LeaseCollection{FIND.LeaseCollectionPublic}>(FIND.LeasePublicPath)
		leaseCollection.borrow()!.fulfillAuction(name)

	}
}
```