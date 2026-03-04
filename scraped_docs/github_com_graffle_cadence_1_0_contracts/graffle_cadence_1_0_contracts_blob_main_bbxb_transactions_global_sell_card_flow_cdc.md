# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/global_sell_card_flow.cdc

```
import FlowToken from "FlowToken"
import FungibleToken from "FungibleToken"
import NonFungibleToken from "NonFungibleToken"
import BBxBarbieCard from "BBxBarbieCard"
import MetadataViews from "MetadataViews"
import NFTStorefrontV2 from "NFTStorefrontV2"

/// Transaction used to facilitate the creation of the listing under the signer's owned storefront resource.
/// It accepts the certain details from the signer,i.e. - 
///
/// `saleItemID` - ID of the NFT that is put on sale by the seller.
/// `saleItemPrice` - Amount of tokens (FT) buyer needs to pay for the purchase of listed NFT.
/// `customID` - Optional string to represent identifier of the dapp.
/// `commissionAmount` - Commission amount that will be taken away by the purchase facilitator.
/// `expiry` - Unix timestamp at which created listing become expired.
/// `marketplacesAddress` - List of addresses that are allowed to get the commission.

/// If the given nft has a support of the RoyaltyView then royalties will added as the sale cut.

transaction(
    saleItemID: UInt64
    , saleItemPrice: UFix64
    , customID: String?
    , commissionAmount: UFix64
    , expiry: UInt64
    , marketplacesAddress: [Address]
    ) {
    let ftReceiver: Capability<&AnyResource{FungibleToken.Receiver}>
    let BBxBarbieCardProvider: Capability<&AnyResource{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>
    let storefront: &NFTStorefrontV2.Storefront
    var saleCuts: [NFTStorefrontV2.SaleCut]
    var marketplacesCapability: [Capability<&AnyResource{FungibleToken.Receiver}>]

    prepare(acct: AuthAccount) {
        self.saleCuts = []
        self.marketplacesCapability = []

        // We need a provider capability, but one is not provided by default so we create one if needed.
        let BBxBarbieCardCollectionProviderPrivatePath = /private/BBxBarbieCardCollectionProviderForNFTStorefront

        // Receiver for the sale cut.
        self.ftReceiver = acct.getCapability<&{FungibleToken.Receiver}>(/public/GenericFTReceiver)!
        assert(self.ftReceiver.borrow() != nil, message: "Missing or mis-typed FlowToken receiver")

        // Check if the Provider capability exists or not if `no` then create a new link for the same.
        if !acct.getCapability<&{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>(BBxBarbieCardCollectionProviderPrivatePath)!.check() {
            acct.link<&{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>(BBxBarbieCardCollectionProviderPrivatePath, target: BBxBarbieCard.CollectionStoragePath)
        }

        self.BBxBarbieCardProvider = acct.getCapability<&{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>(BBxBarbieCardCollectionProviderPrivatePath)!
        let collection = acct
            .getCapability(BBxBarbieCard.CollectionPublicPath)
            .borrow<&{BBxBarbieCard.CardCollectionPublic}>()
            ?? panic("Could not borrow a reference to the collection")
        var totalRoyaltyCut = 0.0
        let effectiveSaleItemPrice = saleItemPrice - commissionAmount
        let nft = collection.borrowCard(id: saleItemID)!
        // Check whether the NFT implements the MetadataResolver or not.
        if nft.getViews().contains(Type<MetadataViews.Royalties>()) {
            let royaltiesRef = nft.resolveView(Type<MetadataViews.Royalties>())?? panic("Unable to retrieve the royalties")
            let royalties = (royaltiesRef as! MetadataViews.Royalties).getRoyalties()
            for royalty in royalties {
                // TODO - Verify the type of the vault and it should exists
                self.saleCuts.append(NFTStorefrontV2.SaleCut(receiver: royalty.receiver, amount: royalty.cut * effectiveSaleItemPrice))
                totalRoyaltyCut = totalRoyaltyCut + royalty.cut * effectiveSaleItemPrice
            }
        }
        // Append the cut for the seller.
        self.saleCuts.append(NFTStorefrontV2.SaleCut(
            receiver: self.ftReceiver,
            amount: effectiveSaleItemPrice - totalRoyaltyCut
        ))
        assert(self.BBxBarbieCardProvider.borrow() != nil, message: "Missing or mis-typed BBxBarbieCard.Collection provider")

        self.storefront = acct.borrow<&NFTStorefrontV2.Storefront>(from: NFTStorefrontV2.StorefrontStoragePath)
            ?? panic("Missing or mis-typed NFTStorefront Storefront")

        for marketplace in marketplacesAddress {
            // Here we are making a fair assumption that all given addresses would have
            // the capability to receive the `FlowToken`
            self.marketplacesCapability.append(getAccount(marketplace).getCapability<&{FungibleToken.Receiver}>(/public/GenericFTReceiver))
        }
    }

    execute {
        // Create listing
        self.storefront.createListing(
            nftProviderCapability: self.BBxBarbieCardProvider,
            nftType: Type<@BBxBarbieCard.NFT>(),
            nftID: saleItemID,
            salePaymentVaultType: Type<@FlowToken.Vault>(),
            saleCuts: self.saleCuts,
            marketplacesCapability: self.marketplacesCapability.length == 0 ? nil : self.marketplacesCapability,
            customID: customID,
            commissionAmount: commissionAmount,
            expiry: expiry
        )
    }
}


// - storefrontAddress (Address): 0x56da62d87aaf2736
// - listingResourceID (UInt64): 162772039
// - nftType (Type): Type<A.6d0f55821f6b2dbe.BBxBarbieCard.NFT>()
// - nftUUID (UInt64): 160717594
// - nftID (UInt64): 318
// - salePaymentVaultType (Type): Type<A.7e60df042a9c0868.FlowToken.Vault>()
// - salePrice (UFix64): 10.00000000
// - customID (String?): "CustomID Goes here"
// - commissionAmount (UFix64): 0.03000000
// - commissionReceivers (?): [0xcd859b6480f59dc8]
// - expiry (UInt64): 1689299706
```