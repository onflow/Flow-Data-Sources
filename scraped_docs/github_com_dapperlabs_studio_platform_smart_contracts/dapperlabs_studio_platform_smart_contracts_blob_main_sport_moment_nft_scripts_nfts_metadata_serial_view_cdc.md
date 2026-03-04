# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/scripts/nfts/metadata_serial_view.cdc

```
import DapperSport from "../../contracts/DapperSport.cdc"
import MetadataViews from 0xMETADATAVIEWSADDRESS


pub fun main(address: Address, id: UInt64): UInt64 {
    let account = getAccount(address)

    let collectionRef = account.getCapability(DapperSport.CollectionPublicPath)
                            .borrow<&{DapperSport.MomentNFTCollectionPublic}>()!

    let nft = collectionRef.borrowMomentNFT(id: id)!
    
    // Get the basic display information for this NFT
    let view = nft.resolveView(Type<MetadataViews.Serial>())!

    let serial = view as! MetadataViews.Serial

    return serial.number
}


```