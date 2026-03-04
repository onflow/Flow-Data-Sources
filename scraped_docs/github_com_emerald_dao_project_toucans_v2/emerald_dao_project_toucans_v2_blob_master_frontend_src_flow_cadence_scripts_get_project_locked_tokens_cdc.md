# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/get_project_locked_tokens.cdc

```
import Toucans from "../Toucans.cdc"
import ToucansLockTokens from "../ToucansLockTokens.cdc"

access(all) fun main(projectOwner: Address, projectId: String): [ToucansLockTokens.LockedVaultDetails] {
  let projectCollection = getAccount(projectOwner).capabilities.borrow<&Toucans.Collection>(Toucans.CollectionPublicPath)
                ?? panic("User does not have a Toucans Collection")
  
  let info = projectCollection.borrowProjectPublic(projectId: projectId)!

  return info.borrowLockTokensManagerPublic()?.getLockedVaultInfos() ?? []
}
```