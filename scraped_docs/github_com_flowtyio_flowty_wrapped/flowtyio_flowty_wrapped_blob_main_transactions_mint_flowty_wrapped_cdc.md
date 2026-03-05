# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/mint_flowty_wrapped.cdc

```
import "FungibleToken"
import "FlowtyWrapped"
import "NonFungibleToken"
import "MetadataViews"
import "WrappedEditions"

transaction(address: Address, username: String, ticket: Int, totalNftsOwned: Int, floatCount: Int, favoriteCollections: [String], collections: [String]) {
    // local variable for storing the minter reference
    let minter: auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin

    prepare(acct: auth(Storage) &Account) {
        //borrow a reference to the NFTMinter resource in storage
        self.minter = acct.storage.borrow<auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin>(from: FlowtyWrapped.AdminStoragePath)
            ?? panic("Could not borrow a reference to the NFT minter")
    }

    execute {
        let wrapped2023Data = WrappedEditions.Wrapped2023Data(
            username, 
            ticket,
            totalNftsOwned,
            floatCount,
            favoriteCollections,
            collections
        )
         let data: {String: AnyStruct} = { 
            "wrapped": wrapped2023Data
        }
        let receiver = getAccount(address).capabilities.get<&{NonFungibleToken.CollectionPublic}>(FlowtyWrapped.CollectionPublicPath).borrow()!
        let nft <- self.minter.mintNFT(editionName: "Flowty Wrapped 2023", address: address, data: data )
        receiver.deposit(token: <-nft)

    }
}

```