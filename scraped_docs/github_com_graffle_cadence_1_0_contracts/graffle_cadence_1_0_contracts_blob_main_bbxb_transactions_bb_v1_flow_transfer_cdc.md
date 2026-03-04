# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_flow_transfer.cdc

```
 // This transaction is a template for a transaction that
// could be used by anyone to send tokens to another account
// that has been set up to receive tokens.
//
// The withdraw amount and the account from getAccount
// would be the parameters to the transaction
import "FungibleToken"
import "FlowToken"
import "FungibleTokenMetadataViews"

transaction(amount: UFix64, to: Address) {

    /// FTVaultData metadata view for the token being used
    let vaultData: FungibleTokenMetadataViews.FTVaultData

    // The Vault resource that holds the tokens that are being transferred
    let sentVault: @{FungibleToken.Vault}

    prepare(signer: auth(BorrowValue) &Account) {

        self.vaultData = FlowToken.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
            ?? panic("ViewResolver does not resolve FTVaultData view")

        // Get a reference to the signer's stored vault
        let vaultRef: auth(FungibleToken.Withdraw) &FlowToken.Vault = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: self.vaultData.storagePath)
            ?? panic("Could not borrow reference to the owner's Vault!")

        // Withdraw tokens from the signer's stored vault
        self.sentVault <- vaultRef.withdraw(amount: amount)
    }

    execute {

        // Get the recipient's public account object
        let recipient: &Account = getAccount(to)

        // Get a reference to the recipient's Receiver
        let receiverRef: &{FungibleToken.Receiver} = recipient.capabilities.borrow<&{FungibleToken.Receiver}>(self.vaultData.receiverPath)
            ?? panic("Could not borrow receiver reference to the recipient's Vault")

        // Deposit the withdrawn tokens in the recipient's receiver
        receiverRef.deposit(from: <-self.sentVault)
    }
}
```