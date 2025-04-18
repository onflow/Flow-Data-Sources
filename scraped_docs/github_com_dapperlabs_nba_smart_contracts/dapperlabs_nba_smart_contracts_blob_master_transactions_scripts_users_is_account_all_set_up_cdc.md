# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/users/is_account_all_set_up.cdc

```
import NonFungibleToken from "NonFungibleToken"
import PackNFT from "PackNFT"
import TopShot from "TopShot"

/// Check if an account has been set up to hold Pinnacle NFTs.
///
access(all) fun main(address: Address): Bool {
    let account = getAccount(address)
    return account.capabilities.borrow<
        &TopShot.Collection>(/public/MomentCollection) != nil &&
        account.capabilities.borrow<
        &PackNFT.Collection>(PackNFT.CollectionPublicPath) != nil
}

```