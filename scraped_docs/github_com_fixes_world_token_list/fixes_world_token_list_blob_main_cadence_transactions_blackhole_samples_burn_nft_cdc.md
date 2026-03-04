# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/blackhole/samples/burn-nft.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "BlackHole"

transaction(
    blackHoleAddr: Address,
    nftContractAddress: Address,
    nftContractName: String,
    nftID: UInt64
) {
    let blackHoleColRef: &BlackHole.Collection
    let nft: @{NonFungibleToken.NFT}

    prepare(acct: auth(BorrowValue) &Account) {
        self.blackHoleColRef = BlackHole.borrowBlackHoleCollection(blackHoleAddr)
            ?? panic("Could not borrow a reference to the BlackHole contract!")

        let c = getAccount(nftContractAddress).contracts.borrow<&{NonFungibleToken}>(name: nftContractName)
            ?? panic("Could not borrow a reference to the NFT contract!")
        let nftColData = c.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as? MetadataViews.NFTCollectionData
            ?? panic("Could not get NFT collection data!")

        let nftColRef = acct.storage
            .borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(from: nftColData.storagePath)
            ?? panic("Could not borrow a reference to the NFT collection!")

        self.nft <- nftColRef.withdraw(withdrawID: nftID)
    }

    execute {
        self.blackHoleColRef.deposit(token: <- self.nft)
    }
}

```