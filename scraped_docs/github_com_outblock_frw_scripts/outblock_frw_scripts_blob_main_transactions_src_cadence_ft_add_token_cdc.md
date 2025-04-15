# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/ft/add_token.cdc

```
import FungibleToken from 0xFungibleToken
import <Token> from <TokenAddress>

transaction {

    prepare(signer: auth(Storage, Capabilities) &Account) {

        if signer.storage.borrow<&<Token>.Vault>(from: <TokenStoragePath> ) == nil {
            signer.storage.save(<- <Token>.createEmptyVault(vaultType: Type<@<Token>.Vault>()), to: <TokenStoragePath>)
        }

        if signer.capabilities.exists(<TokenReceiverPath>) == false {
            let receiverCapability = signer.capabilities.storage.issue<&<Token>.Vault>(<TokenStoragePath>)
            signer.capabilities.publish(receiverCapability, at: <TokenReceiverPath>)
        
        }
       
        if signer.capabilities.exists(<TokenBalancePath>) == false {
            let balanceCapability = signer.capabilities.storage.issue<&<Token>.Vault>(<TokenStoragePath>)
            signer.capabilities.publish(balanceCapability, at: <TokenBalancePath>)
        }
    
    }
}
```