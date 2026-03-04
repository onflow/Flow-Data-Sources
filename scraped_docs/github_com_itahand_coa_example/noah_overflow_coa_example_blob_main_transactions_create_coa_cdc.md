# Source: https://github.com/Noah-Overflow/COA-Example/blob/main/transactions/create_COA.cdc

```
import "EVM"

// Note that this is just one of many ways of handling multiple COAs inside an account
transaction() {
    prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        // Define n and status
        var n = 0
        var status = "incomplete"

        // While loop while status is incomplete
        // if there's a @EVM.CadenceOwnedAccount in that slot, move to next n
        while status == "incomplete" {
            let evmPath = StoragePath(identifier: signer.address.toString().concat("EVM_").concat(n.toString()))!
            let evmPublicPath = PublicPath(identifier: signer.address.toString().concat("EVM_").concat(n.toString()))!
            let oldCoa = signer.storage.borrow<&EVM.CadenceOwnedAccount>(from: evmPath)

            // if there's no COA in that slot
            if oldCoa == nil {  
               // Create account & save to storage
                let newCoa: @EVM.CadenceOwnedAccount <- EVM.createCadenceOwnedAccount()
                signer.storage.save(<- newCoa, to: evmPath)
                // Publish a public capability to the COA
                let cap = signer.capabilities.storage.issue<&EVM.CadenceOwnedAccount>(evmPath)
                signer.capabilities.publish(cap, at: evmPublicPath)
                // Change status to "completed" to close the while loop
                status = "completed"
                
            } else { // If there is a COA in that slot
                // Change n to n + 1
                n = n + 1
            }
        }
    }
}

```