# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/token/admin/setupBloctoPassMinterPublic.cdc

```
import "BloctoPass"

transaction {
    prepare(signer: auth(BorrowValue, SaveValue, Capabilities) &Account) {
        // create a public capability to mint Blocto Pass
        let balanceCapability = signer.capabilities.storage.issue<&{BloctoPass.MinterPublic}>(BloctoPass.MinterStoragePath)
        signer.capabilities.publish(balanceCapability, at: BloctoPass.MinterPublicPath)
    }
}

```