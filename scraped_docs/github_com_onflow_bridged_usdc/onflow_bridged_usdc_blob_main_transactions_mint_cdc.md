# Source: https://github.com/onflow/bridged-usdc/blob/main/transactions/mint.cdc

```
// This script mints token on USDCFlow contract and deposits
// the minted amount to the receiver's Vault

import "FungibleToken"
import "USDCFlow"
import "FlowEVMBridgeHandlerInterfaces"

transaction(recipient: Address, amount: UFix64) {

    /// Reference to the Example Token Minter Resource object
    let tokenMinter: auth(FlowEVMBridgeHandlerInterfaces.Mint) &USDCFlow.Minter

    /// Reference to the Fungible Token Receiver of the recipient
    let tokenReceiver: &{FungibleToken.Receiver}

    prepare(signer: auth(BorrowValue) &Account) {

        // Borrow a reference to the admin object
        self.tokenMinter = signer.storage.borrow<auth(FlowEVMBridgeHandlerInterfaces.Mint) &USDCFlow.Minter>(from: /storage/usdcFlowMinter)
            ?? panic("Could not borrow a reference to the signer's USDCFlow.VaultMinter"
                     .concat(" from the path /storage/usdcFlowMinter")
                     .concat(". Make sure you are signing with the account that stores the minter."))
    
        self.tokenReceiver = getAccount(recipient).capabilities.borrow<&USDCFlow.Vault>(USDCFlow.ReceiverPublicPath)
            ?? panic("Could not borrow a USDCFlow.Vault reference to the USDCFlow Vault in account"
                    .concat(recipient.toString())
                    .concat(". at the path ").concat(USDCFlow.ReceiverPublicPath.toString())
                    .concat(". Make sure the account address is correct and that ")
                    .concat("the account being queried has initialized with ")
                    .concat("a USDCFlow Vault and valid capability."))
    }

    execute {

        // Create mint tokens
        let mintedVault <- self.tokenMinter.mint(amount: amount)

        // Deposit them to the receiever
        self.tokenReceiver.deposit(from: <-mintedVault)
    }
}
```