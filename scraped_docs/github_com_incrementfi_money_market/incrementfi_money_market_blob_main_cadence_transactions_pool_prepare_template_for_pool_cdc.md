# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Pool/prepare_template_for_pool.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"

transaction() {
    prepare(poolAccount: auth(Storage, Capabilities) &Account) {
        let preUnderlyingVault <- poolAccount.storage.load<@{FungibleToken.Vault}>(from: /storage/poolUnderlyingAssetVault)
        if preUnderlyingVault != nil {
            let flowTokenStoragePath = /storage/flowTokenVault
            if (poolAccount.storage.borrow<&FlowToken.Vault>(from: flowTokenStoragePath) == nil) {
                poolAccount.storage.save(<-FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>()), to: flowTokenStoragePath)
                poolAccount.capabilities.publish(
                    poolAccount.capabilities.storage.issue<&{FungibleToken.Receiver}>(flowTokenStoragePath),
                    at: /public/flowTokenReceiver
                )
                poolAccount.capabilities.publish(
                    poolAccount.capabilities.storage.issue<&{FungibleToken.Balance}>(flowTokenStoragePath),
                    at: /public/flowTokenBalance
                )
            }
            let receiverRef =  poolAccount.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)
                ?? panic("There is no local FlowToken vault in public/flowTokenReceiver, may lost the pre pool's vault in poolUnderlyingAssetVault")
            receiverRef.deposit(from: <-preUnderlyingVault!)
        } else {
            destroy preUnderlyingVault
        }
        poolAccount.storage.save(<- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>()), to: /storage/poolUnderlyingAssetVault)
    }
}
```