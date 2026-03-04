# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/transactions/add_allowed_nft_collections.cdc

```
import Toucans from "../Toucans.cdc"

transaction(
  projectOwner: Address, 
  projectId: String, 
  collectionIdentifiers: [String]
) {

  let Project: auth(Toucans.ProjectOwner) &Toucans.Project
  
  prepare(signer: auth(Storage) &Account) {
    let collection = signer.storage.borrow<auth(Toucans.CollectionOwner) &Toucans.Collection>(from: Toucans.CollectionStoragePath)
                    ?? panic("A DAOTreasury doesn't exist here.")
    self.Project = collection.borrowProject(projectId: projectId) ?? panic("Project does not exist.")
  
  }
  execute {
    self.Project.addAllowedNFTCollections(collectionIdentifiers: collectionIdentifiers)
  }
}
```