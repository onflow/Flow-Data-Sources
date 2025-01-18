# Source: https://academy.ecdao.org/en/snippets/storefront-buy-nft-from-catalog


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Buy an NFT in Cadence

# Buy an NFT in Cadence


Snippet



cadence
```
		
			import "ExampleToken"
import "FungibleToken"
import "NonFungibleToken"
import "ExampleNFT"
import "NFTStorefront"
import "MetadataViews"

transaction(listingResourceID: UInt64, storefrontAddress: Address) {

    let paymentVault: @{FungibleToken.Vault}
    let exampleNFTReceiver: &{NonFungibleToken.Receiver}
    let storefront: &{NFTStorefront.StorefrontPublic}
    let listing: &{NFTStorefront.ListingPublic}

    prepare(acct: auth(BorrowValue) &Account) {
        self.storefront = getAccount(storefrontAddress).capabilities.borrow<&{NFTStorefront.StorefrontPublic}>(
                NFTStorefront.StorefrontPublicPath
            ) ?? panic("Could not borrow StorefrontPublic from provided address")

        self.listing = self.storefront.borrowListing(listingResourceID: listingResourceID)
                    ?? panic("No Offer with that ID in Storefront")
        let price = self.listing.getDetails().salePrice

        let mainVault = acct.storage.borrow<auth(FungibleToken.Withdraw) &ExampleToken.Vault>(from: /storage/exampleTokenVault)
            ?? panic("Cannot borrow ExampleToken vault from acct storage")
        self.paymentVault <- mainVault.withdraw(amount: price)

        let collectionDataOpt = ExampleNFT.resolveContractView(resourceType: Type<@ExampleNFT.NFT>(), viewType: Type<MetadataViews.NFTCollectionData>())
            ?? panic("Missing collection data")
        let collectionData = collectionDataOpt as! MetadataViews.NFTCollectionData


        self.exampleNFTReceiver = acct.capabilities.borrow<&{NonFungibleToken.Receiver}>(collectionData.publicPath)
            ?? panic("Cannot borrow NFT collection receiver from account")
    }

    execute {
        let item <- self.listing.purchase(
            payment: <-self.paymentVault
        )

        self.exampleNFTReceiver.deposit(token: <-item)

        /*
        error: Execution failed:
        computation limited exceeded: 100
        */
        // Be kind and recycle
        self.storefront.cleanup(listingResourceID: listingResourceID)
    }

    //- Post to check item is in collection?
}
		 
	
```


![User avatar](https://flowverse.myfilebase.com/ipfs/bafybeige6rafun3hfyhamxxl44q6yqox4krrlyvjvr2k2ktiulnevdf74e?img-width=400&img-height=400)

Author

[Brian Min](https://twitter.com/BrianMin_)




[Run Code](https://github.com/bymi15/flow-code-snippets/blob/main/storefront-buy-nft-from-catalog.cdc)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/storefront-buy-nft-from-catalog/readme.md)


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow


##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)
##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)
##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)
[Join the community](https://discord.gg/emerald-city-906264258189332541)



