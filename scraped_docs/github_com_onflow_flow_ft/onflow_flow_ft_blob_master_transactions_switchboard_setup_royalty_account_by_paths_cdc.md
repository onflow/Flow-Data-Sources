# Source: https://github.com/onflow/flow-ft/blob/master/transactions/switchboard/setup_royalty_account_by_paths.cdc

```
import "FungibleToken"
import "FungibleTokenSwitchboard"
import "FlowToken"
import "FiatToken"


/// This transaction is a template for a transaction that could be used by 
/// anyone fully setup an account for receiving both Flow and USDC tokens at the same
/// public path (for instance the royalties /public/GenericFTReceiver path)
/// Using the addNewVaultWrappersByPath switchboard method allows anyone to use
/// capability wrappers such as TokenForwarders instead of the actual token vault.

transaction (address: Address) {

    let vaultPaths: [PublicPath]
    let vaultTypes: [Type]    
    let switchboardRef:  auth(FungibleTokenSwitchboard.Owner) &FungibleTokenSwitchboard.Switchboard

    prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) Account) {

        // Prepare the paths and types arrays with the Flow and USDC tokens data
        self.vaultPaths = []
        self.vaultPaths.append(/public/flowTokenReceiver)
        self.vaultPaths.append(FiatToken.VaultReceiverPubPath)
        self.vaultTypes = []
        self.vaultTypes.append(Type<@FlowToken.Vault>())
        self.vaultTypes.append(Type<@FiatToken.Vault>())

        // Check if the account already has a USDC Vault
        if signer.storage.borrow<&FiatToken.Vault>(from: FiatToken.VaultStoragePath) == nil {
            // If not, create a new USDC Vault resource and put it into storage
            signer.storage.save(<-FiatToken.createEmptyVault(vaultType: Type<@FiatToken.Vault>()), 
                                                      to: FiatToken.VaultStoragePath)
        }

        // Check if the receiver capability is linked on the USDC receiver path
        if !signer.capabilities.get<&{FungibleToken.Receiver}>
                                           (FiatToken.VaultReceiverPubPath)!.check() {
            // if it's not, create a public capability to the USDC vault
            let tokenCap = signer.capabilities.storage.issue<&FiatToken.Vault>(FiatToken.VaultStoragePath)
            signer.capabilities.publish(tokenCap, at: FiatToken.VaultReceiverPubPath)
            let receiverCap = signer.capabilities.storage.issue<&FiatToken.Vault>(FiatToken.VaultStoragePath)
            signer.capabilities.publish(receiverCap, at: FiatToken.VaultBalancePubPath)
        }
        self.fiatTokenVaultCapability = signer.capabilities.get<&{FungibleToken.Receiver}>(FiatToken.VaultReceiverPubPath)

        // Check if the account already has a Switchboard resource
        if signer.storage.borrow<&FungibleTokenSwitchboard.Switchboard>
                                (from: FungibleTokenSwitchboard.StoragePath) == nil {
            // If not, create a new Switchboard resource and put it into storage
            signer.storage.save(<- FungibleTokenSwitchboard.createSwitchboard(), 
                                            to: FungibleTokenSwitchboard.StoragePath)
        }
        // Check if the receiver capability is linked on the receiver path
        if !signer.capabilities.get
                      <&FungibleTokenSwitchboard.Switchboard>
                              (FungibleTokenSwitchboard.ReceiverPublicPath)!.check() {
            // if it's not, create a public capability to the Switchboard 
            let receiverCap = signer.capabilities.storage.issue<&FungibleTokenSwitchboard.Switchboard>(FungibleTokenSwitchboard.StoragePath)
            signer.capabilities.publish(receiverCap, at: FungibleTokenSwitchboard.ReceiverPublicPath)
        }
        // Check if the SwitchboardPublic and ft receiver capabilities are linked on
        // the switchboard public path
        if !signer.capabilities.get<
        &FungibleTokenSwitchboard.Switchboard
                                       >(FungibleTokenSwitchboard.ReceiverPublicPath)!
                                                                           .check() {
            // if it's not, create a public capability to the Switchboard
            let switchboardReceiverCap = signer.capabilities.storage.issue<
            &FungibleTokenSwitchboard.Switchboard
                                               >(FungibleTokenSwitchboard.StoragePath)
            signer.capabilities.publish(switchboardReceiverCap, at: FungibleTokenSwitchboard.PublicPath)
        }
        // Get a reference to the switchboard
        self.switchboardRef = signer.storage.borrow<auth(FungibleTokenSwitchboard.Owner) &FungibleTokenSwitchboard.Switchboard>
                                         (from: FungibleTokenSwitchboard.StoragePath) 
			?? panic("The signer does not store a FungibleToken Switchboard object at the path "
                .concat(FungibleTokenSwitchboard.StoragePath.toString())
                .concat(". The signer must initialize their account with this object first!"))
    }

    execute {

      // Add the capabilities to the switchboard using addNewVaultWrappersByPath
      self.switchboardRef.addNewVaultWrappersByPath(paths: self.vaultPaths, 
                                            types: self.vaultTypes, address: address)

    }

}
 
```