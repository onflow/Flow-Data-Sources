# Source: https://github.com/austinkline/managed-account/blob/main/scripts/get_proposal_approved_weight.cdc

```
import "ManagedAccount"

access(all) fun main(managerAddress: Address, proposalId: UInt64): UFix64 {
    let manager = getAccount(managerAddress).capabilities.get<&ManagedAccount.Manager>(ManagedAccount.ManagerPublicPath)
        .borrow() ?? panic("manager not found")
    let proposal = manager.borrowProposal(proposalId: proposalId)
        ?? panic("proposal not found")

    return proposal.getApprovalWeight()
}
```