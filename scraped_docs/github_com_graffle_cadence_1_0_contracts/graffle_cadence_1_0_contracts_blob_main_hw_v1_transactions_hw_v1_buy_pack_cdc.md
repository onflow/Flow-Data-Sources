# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_buy_pack.cdc

```
import FiatToken from "../contracts/utility/FiatToken.cdc"
import FungibleToken from "../contracts/utility/FungibleToken.cdc"
import NonFungibleToken from "../contracts/utility/NonFungibleToken.cdc"
import NFTStorefrontV2 from "../contracts/utility/NFTStorefrontV2.cdc"

import HWGaragePack from "../contracts/HWGaragePack.cdc"

/// Transaction facilitates the purcahse of listed NFT.
/// It takes the storefront address, listing resource that need
/// to be purchased & a address that will takeaway the commission.
///
/// Buyer of the listing (,i.e. underling NFT) would authorize and sign the
/// transaction and if purchase happens then transacted NFT would store in
/// buyer's collection.

transaction(listingResourceID: UInt64, storefrontAddress: Address, commissionRecipient: Address?) {
    let paymentVault: @FungibleToken.Vault
    let HWGaragePackCollection: &HWGaragePack.Collection{NonFungibleToken.Receiver}
    let storefront: &NFTStorefrontV2.Storefront{NFTStorefrontV2.StorefrontPublic}
    let listing: &NFTStorefrontV2.Listing{NFTStorefrontV2.ListingPublic}
    var commissionRecipientCap: Capability<&{FungibleToken.Receiver}>?

    prepare(acct: AuthAccount) {
        //self.commissionRecipientCap = nil // if nil then anyone can get commission
        self.commissionRecipientCap = getAccount(commissionRecipient!).getCapability<&{FungibleToken.Receiver}>(FiatToken.VaultReceiverPubPath)
        // Access the storefront public resource of the seller to purchase the listing.
        self.storefront = getAccount(storefrontAddress)
            .getCapability<&NFTStorefrontV2.Storefront{NFTStorefrontV2.StorefrontPublic}>(
                NFTStorefrontV2.StorefrontPublicPath
            )
            .borrow()
            ?? panic("Could not borrow Storefront from provided address")

        // Borrow the listing
        self.listing = self.storefront.borrowListing(listingResourceID: listingResourceID)
                    ?? panic("No Offer with that ID in Storefront")
        let price = self.listing.getDetails().salePrice

        // Access the vault of the buyer to pay the sale price of the listing.
        let mainFiatVault = acct.borrow<&FiatToken.Vault>(from: FiatToken.VaultStoragePath)
            ?? panic("Cannot borrow FlowToken vault from acct storage")
        self.paymentVault <- mainFiatVault.withdraw(amount: price)

        // Access the buyer's NFT collection to store the purchased NFT.
        self.HWGaragePackCollection = acct.borrow<&HWGaragePack.Collection{NonFungibleToken.Receiver}>(
            from: HWGaragePack.CollectionStoragePath
        ) ?? panic("Cannot borrow buyers Pack collection receiver")

        // Fetch the commission amt.
        let commissionAmount = self.listing.getDetails().commissionAmount

        if commissionRecipient != nil && commissionAmount != 0.0 {
            // Access the capability to receive the commission.
            let _commissionRecipientCap = getAccount(commissionRecipient!).getCapability<&{FungibleToken.Receiver}>(FiatToken.VaultReceiverPubPath)
            assert(_commissionRecipientCap.check(), message: "Commission Recipient doesn't have FiatToken receiving capability")
            self.commissionRecipientCap = _commissionRecipientCap
        } else if commissionAmount == 0.0 {
            self.commissionRecipientCap = nil
        } else {
            panic("Commission recipient can not be empty when commission amount is non zero")
        }
    }

    execute {
        // Purchase the NFT
        let item <- self.listing.purchase(
            payment: <-self.paymentVault,
            commissionRecipient: self.commissionRecipientCap
        )
        // Deposit the NFT in the buyer's collection.
        self.HWGaragePackCollection.deposit(token: <-item)
    }
}
 
```