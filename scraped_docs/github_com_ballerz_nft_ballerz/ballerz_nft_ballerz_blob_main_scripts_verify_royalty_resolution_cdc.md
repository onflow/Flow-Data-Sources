# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/scripts/verify_royalty_resolution.cdc

```
import "MetadataViews"
import "ViewResolver"
import "FungibleToken"
import "Gaia"

// Resolves MetadataViews.Royalties from a single Gaia NFT in the given
// owner's collection, then verifies the embedded FungibleToken.Receiver
// capability for each Royalty actually resolves to a borrowable receiver.
//
// Returns the resolved royalty receivers + whether each one borrows.

access(all) struct RoyaltyCheck {
    access(all) let receiverAddress: Address
    access(all) let cut: UFix64
    access(all) let description: String
    access(all) let receiverWorks: Bool
    access(all) let receiverType: String

    init(addr: Address, cut: UFix64, desc: String, works: Bool, t: String) {
        self.receiverAddress = addr
        self.cut = cut
        self.description = desc
        self.receiverWorks = works
        self.receiverType = t
    }
}

access(all) fun main(owner: Address, nftID: UInt64): [RoyaltyCheck] {
    let collection = getAccount(owner).capabilities
        .borrow<&{Gaia.CollectionPublic}>(Gaia.CollectionPublicPath)
        ?? panic("could not borrow Gaia public collection at owner address")
    let nft = collection.borrowGaiaNFT(id: nftID)
        ?? panic("owner does not have NFT with that id")

    let resolved = nft.resolveView(Type<MetadataViews.Royalties>())
        ?? panic("resolveView returned nil for Royalties")
    let royalties = (resolved as! MetadataViews.Royalties).getRoyalties()

    let out: [RoyaltyCheck] = []
    for r in royalties {
        let works = r.receiver.check()
        let typeId = r.receiver.borrow()?.getType()?.identifier ?? "<not borrowable>"
        out.append(RoyaltyCheck(
            addr: r.receiver.address,
            cut: r.cut,
            desc: r.description,
            works: works,
            t: typeId
        ))
    }
    return out
}

```