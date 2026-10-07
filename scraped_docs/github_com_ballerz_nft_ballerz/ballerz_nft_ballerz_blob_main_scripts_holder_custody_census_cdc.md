# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/scripts/holder_custody_census.cdc

```
// a custody census for a list of holder addresses. for each one it returns:
//   [address, has a Dapper Utility Coin receiver, is a linked (child) account,
//    number of parents, a parent-usable controller exists for the Gaia
//    collection, a parent can get a withdraw capability, FLOW balance, key count]
//
// a DUC receiver together with 20 or more keys marks a Dapper Wallet account.
// run in batches of about 150 addresses to stay under the script limit
//
// on 2026-10-05, over the 3,288 wallets in the April holders snapshot: 2,992
// were Dapper accounts holding 9,367 of 9,759 Ballerz, and 284 were linked to
// a parent wallet

import HybridCustody from 0xd8a7e05a7ac670c0
import NonFungibleToken from 0x1d7e57aa55817448
import Gaia from 0x8b148183c28ff88f

access(all) fun main(addrs: [Address]): [[AnyStruct]] {
  let out: [[AnyStruct]] = []
  let providerType = Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()
  for a in addrs {
    let acct = getAuthAccount<auth(Storage) &Account>(a)
    let hasDuc = acct.storage.type(at: /storage/dapperUtilityCoinReceiver) != nil
    var linked = false
    var parents = 0
    var ctrl = false
    var canProvide = false
    if let owned = acct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath) {
      linked = true
      let ps = owned.getParentAddresses()
      parents = ps.length
      for p in ps {
        if let child = acct.storage.borrow<auth(HybridCustody.Child) &HybridCustody.ChildAccount>(from: StoragePath(identifier: HybridCustody.getChildAccountIdentifier(p))!) {
          if let id = child.getControllerIDForType(type: providerType, forPath: Gaia.CollectionStoragePath) {
            ctrl = true
            if let cap = child.getCapability(controllerID: id, type: providerType) {
              if cap.check<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>() { canProvide = true }
            }
          }
        }
      }
    }
    out.append([a, hasDuc, linked, parents, ctrl, canProvide, acct.balance, acct.keys.count])
  }
  return out
}

```