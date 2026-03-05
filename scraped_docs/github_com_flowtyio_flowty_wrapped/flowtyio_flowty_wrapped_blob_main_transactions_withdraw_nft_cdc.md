# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/withdraw_nft.cdc

```
import "NonFungibleToken"
import "FlowtyWrapped"

transaction(owner: Address, receiver: Address, withdrawID: UInt64) {

  prepare(acct: auth(Storage) &Account){

  let collectionRef = acct.storage.borrow<auth(NonFungibleToken.Withdraw) &FlowtyWrapped.Collection>(from: FlowtyWrapped.CollectionStoragePath)
    ?? panic("Could not borrow a reference to the owner's collection")

  let nft <- collectionRef.withdraw(withdrawID: 42)

  let recipient = getAccount(receiver).capabilities.get<&{NonFungibleToken.CollectionPublic}>(FlowtyWrapped.CollectionPublicPath).borrow() ?? panic("invalid receiver collection")

  recipient.deposit(token: <-nft)
  }
} 
```