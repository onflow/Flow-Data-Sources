# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/hybridCustody/transaction/setup_owned_account.cdc

```
#allowAccountLinking

import ViewResolver from 0xViewResolver
import MetadataViews from 0xMetadataViews
import HybridCustody from 0xHybridCustody

transaction(name: String?, desc: String?, thumbnailURL: String?) {
  prepare(acct: auth(Storage, Capabilities) &Account) {
    let acctCap = acct.capabilities.account.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

    if acct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath) == nil {
      let ownedAccount <- HybridCustody.createOwnedAccount(acct: acctCap)
      acct.storage.save(<-ownedAccount, to: HybridCustody.OwnedAccountStoragePath)
    }

    let owned = acct.storage.borrow<auth(HybridCustody.Owner) &HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)
      ?? panic("owned account not found")
    
    // Set the display metadata for the OwnedAccount
    if name != nil && desc != nil && thumbnailURL != nil {
      let thumbnail = MetadataViews.HTTPFile(url: thumbnailURL!)
      let display = MetadataViews.Display(name: name!, description: desc!, thumbnail: thumbnail)
      owned.setDisplay(display)
    }

    // check that paths are all configured properly
    for c in acct.capabilities.storage.getControllers(forPath: HybridCustody.OwnedAccountStoragePath) {
      c.delete()
    }

    acct.capabilities.storage.issue<&{HybridCustody.BorrowableAccount, HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath)
    acct.capabilities.publish(
      acct.capabilities.storage.issue<&{HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath),
      at: HybridCustody.OwnedAccountPublicPath
    )
  }
}
 
```