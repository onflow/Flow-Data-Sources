# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/get_project_nft_treasury_ids.cdc

```
import Toucans from "../Toucans.cdc"

access(all) fun main(projectOwner: Address, projectId: String): {String: [UInt64]} {
    let res: {String: [UInt64]} = {}
    let projectCollection = getAccount(projectOwner).capabilities.borrow<&Toucans.Collection>(Toucans.CollectionPublicPath)
                ?? panic("User does not have a Toucans Collection")
    let project = projectCollection.borrowProjectPublic(projectId: projectId)!

    for collectionType in project.getCollectionTypesInTreasury() {
        let collectionIds = project.getNFTIDs(collectionType: collectionType)
        res[collectionType.identifier] = collectionIds
    }
    return res
}
```