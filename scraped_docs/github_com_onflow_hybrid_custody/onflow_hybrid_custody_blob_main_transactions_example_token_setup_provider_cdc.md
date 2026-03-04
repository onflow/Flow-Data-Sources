# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/example-token/setup_provider.cdc

```
import "FungibleToken"
import "ExampleToken"
import "FungibleTokenMetadataViews"

transaction {
    prepare(acct: auth(Capabilities) &Account) {
        let vaultData = ExampleToken.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
            ?? panic("Could not get the vault data view for ExampleToken")
    
        acct.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(vaultData.storagePath)
    }
}
 
```