# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/transactions/treasury-actions/withdraw_tokens.cdc

```
import Toucans from "../../Toucans.cdc"
import ToucansTokens from "../../ToucansTokens.cdc"
import FungibleToken from "../../utility/FungibleToken.cdc"

// An example of proposing an action.
//
// Proposed ACTION: Withdraw `amount` `tokenSymbol` from the treasury
// at `projectOwner` to `recipientAddr`

transaction(tokenSymbol: String, recipientAddr: Address, amount: UFix64, projectOwner: Address, projectId: String) {

  let Project: &Toucans.Project
  
  prepare(signer: &Account) {
    let projectCollection = getAccount(projectOwner).capabilities.borrow<&Toucans.Collection>(Toucans.CollectionPublicPath)
                  ?? panic("This is an incorrect address for project owner.")
    self.Project = projectCollection.borrowProjectPublic(projectId: projectId) ?? panic("Project does not exist.")
  }

  execute {
    var tokenInfo = ToucansTokens.getTokenInfoFromSymbol(symbol: tokenSymbol)
    if tokenInfo == nil && tokenSymbol == self.Project.projectTokenInfo.symbol {
      tokenInfo = self.Project.getProjectTokenInfo()
    }
    assert(tokenInfo != nil, message: "Didn't find token info.")

    let recipientVault = getAccount(recipientAddr).capabilities.get<&{FungibleToken.Receiver}>(tokenInfo!.receiverPath)
    assert(recipientVault != nil, message: "Capability is nil for ".concat(recipientAddr.toString()).concat("!"))
    assert(recipientVault!.check(), message: "Invalid capability for ".concat(recipientAddr.toString()).concat("!"))
    self.Project.proposeWithdraw(vaultType: tokenInfo!.tokenType, recipientVault: recipientVault!, amount: amount)
  }
}
```