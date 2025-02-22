# Source: https://github.com/onflow/flow-ft/blob/master/transactions/switchboard/batch_add_vault_capabilities.cdc

```
import "FungibleTokenSwitchboard"
import "ExampleToken"
import "FungibleTokenMetadataViews"

/// This transaction is a template for a transaction that could be used by anyone to add several new fungible token
/// vaults, belonging to a certain `Address` to their switchboard resource.
///
transaction (address: Address) {

    let exampleTokenVaultPath: PublicPath
    let vaultPaths: [PublicPath]
    let switchboardRef:  auth(FungibleTokenSwitchboard.Owner) &FungibleTokenSwitchboard.Switchboard

    prepare(signer: auth(BorrowValue) &Account) {

        let vaultData = ExampleToken.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
            ?? panic("Could not resolve FTVaultData view. The ExampleToken"
                .concat(" contract needs to implement the FTVaultData Metadata view in order to execute this transaction."))

        // Get the example token vault path from the contract
        self.exampleTokenVaultPath = vaultData.receiverPath
      
        // And store it in the array of public paths that will be passed to the
        // switchboard method
        self.vaultPaths = []
        self.vaultPaths.append(self.exampleTokenVaultPath)
      
        // Get a reference to the signers switchboard
        self.switchboardRef = signer.storage.borrow<auth(FungibleTokenSwitchboard.Owner) &FungibleTokenSwitchboard.Switchboard>(
            from: FungibleTokenSwitchboard.StoragePath)
			?? panic("The signer does not store a FungibleToken Switchboard object at the path "
                .concat(FungibleTokenSwitchboard.StoragePath.toString())
                .concat(". The signer must initialize their account with this object first!"))
    
    }

    execute {

        // Add the capability to the switchboard using addNewVault method
        self.switchboardRef.addNewVaultsByPath(paths: self.vaultPaths, address: address)

    }

}

```