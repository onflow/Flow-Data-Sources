# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Test/mint_fusd_for_user.cdc

```
import FUSD from "../../contracts/tokens/FUSD.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"

transaction(mintAmount: UFix64) {

    prepare(signer: auth(Storage, Capabilities) &Account) {
        log("Transaction Start ---------------")
        log("user add fusd".concat(mintAmount.toString()))
        let fusdStoragePath = /storage/fusdVault
        var fusdVault = signer.storage.borrow<&FUSD.Vault>(from: fusdStoragePath)
        if fusdVault == nil {
            signer.storage.save(<-FUSD.createEmptyVault(vaultType: Type<@FUSD.Vault>()), to: fusdStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(fusdStoragePath),
                at: /public/fusdReceiver
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(fusdStoragePath),
                at: /public/fusdBalance
            )
        }
        fusdVault = signer.storage.borrow<&FUSD.Vault>(from: fusdStoragePath)
        fusdVault!.deposit(from: <-FUSD.test_minter.mintTokens(amount: mintAmount))
        log("End -----------------------------")
    }
}
```