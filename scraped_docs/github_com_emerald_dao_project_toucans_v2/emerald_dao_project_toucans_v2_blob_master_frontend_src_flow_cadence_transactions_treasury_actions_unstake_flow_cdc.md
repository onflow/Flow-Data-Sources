# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/transactions/treasury-actions/unstake_flow.cdc

```
import Toucans from "../../Toucans.cdc"

transaction(projectId: String, projectOwner: Address, stFlowAmount: UFix64, flowAmountOutMin: UFix64) {

    let Project: &Toucans.Project

    prepare(signer: &Account) {
        let projectCollection = getAccount(projectOwner).capabilities.borrow<&Toucans.Collection>(Toucans.CollectionPublicPath)
                  ?? panic("This is an incorrect address for project owner.")
        self.Project = projectCollection.borrowProjectPublic(projectId: projectId)
                  ?? panic("Project does not exist, at least in this collection.")
    }

    execute {
        self.Project.proposeUnstakeFlow(stFlowAmount: stFlowAmount, flowAmountOutMin: flowAmountOutMin)
    }
}
```