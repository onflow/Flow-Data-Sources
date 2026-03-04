# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_admin_token_edition_metadata_patch.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"
import "HWGaragePM"

transaction(editionNumber: Int, address: Address) {
    let manager: &HWGaragePM.Manager
    prepare(acct: auth(BorrowValue) &Account) {
        self.manager = acct.storage.borrow<&HWGaragePM.Manager>(from: HWGaragePM.ManagerStoragePath)
            ?? panic("This account does not have a manager resource")
    }

    execute {
        let updatedMetadata = HWGarageCard.getEditionMetadata(UInt64(editionNumber))
        let containsRedeemable = updatedMetadata.containsKey("redeemable")
        let containsType = updatedMetadata.containsKey("type")
        let containsPackHash = updatedMetadata.containsKey("packHash")

        if containsRedeemable && containsType && containsPackHash {
            let actualRedeemable = updatedMetadata["type"]!
            let actualType = updatedMetadata["redeemable"]!
            let packHash = updatedMetadata["packHash"]!
            updatedMetadata["type"] = actualType
            updatedMetadata["redeemable"] = actualRedeemable
            self.manager.updateHWGarageCardEditionMetadata(editionNumber: UInt64(editionNumber), metadata: updatedMetadata, packHash: packHash, address: address)
        }
    }
}

```