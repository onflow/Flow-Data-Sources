# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/get_project_specific_nft_treasury_ids.cdc

```
import Toucans from "../Toucans.cdc"
import NFTCatalog from "../utility/NFTCatalog.cdc"

access(all) fun main(projectOwner: Address, projectId: String, collectionIdentifier: String): [UInt64] {
    let catalogEntry = NFTCatalog.getCatalogEntry(collectionIdentifier: collectionIdentifier)
          ?? panic("There is no NFT Catalog entry for this.")
    let contractAddressToString = catalogEntry.contractAddress.toString()
    let collectionType = CompositeType(
      "A."
      .concat(contractAddressToString.slice(from: 2, upTo: contractAddressToString.length))
      .concat(".")
      .concat(catalogEntry.contractName)
      .concat(".Collection")
    )!
    let projectCollection = getAccount(projectOwner).capabilities.borrow<&Toucans.Collection>(Toucans.CollectionPublicPath)
                ?? panic("User does not have a Toucans Collection")
    let project = projectCollection.borrowProjectPublic(projectId: projectId)!

    return project.getNFTIDs(collectionType: collectionType)
    
}

```