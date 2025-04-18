# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/market/purchase_moment.cdc

```
import FungibleToken from 0xFUNGIBLETOKENADDRESS
import DapperUtilityCoin from 0xDUCADDRESS
import TopShot from 0xTOPSHOTADDRESS
import Market from 0xMARKETADDRESS

// This transaction is for a user to purchase a moment that another user
// has for sale in their sale collection

// Parameters
//
// sellerAddress: the Flow address of the account issuing the sale of a moment
// tokenID: the ID of the moment being purchased
// purchaseAmount: the amount for which the user is paying for the moment; must not be less than the moment's price

transaction(sellerAddress: Address, tokenID: UInt64, purchaseAmount: UFix64) {

    // Local variables for the topshot collection object and token provider
    let collectionRef: &TopShot.Collection
    let providerRef: auth(FungibleToken.Withdraw) &DapperUtilityCoin.Vault
    
    prepare(acct: auth(Storage, Capabilities) &Account) {

        // borrow a reference to the signer's collection
        self.collectionRef = acct.storage.borrow<&TopShot.Collection>(from: /storage/MomentCollection)
            ?? panic("Could not borrow reference to the Moment Collection")

        // borrow a reference to the signer's fungible token Vault
        self.providerRef = acct.storage.borrow<auth(FungibleToken.Withdraw) &DapperUtilityCoin.Vault>(from: /storage/dapperUtilityCoinVault)!
    }

    execute {

        // withdraw tokens from the signer's vault
        let tokens <- self.providerRef.withdraw(amount: purchaseAmount) as! @DapperUtilityCoin.Vault

        // get the seller's public account object
        let seller = getAccount(sellerAddress)

        // borrow a public reference to the seller's sale collection
        let topshotSaleCollection = seller.capabilities.borrow<&Market.SaleCollection>(/public/topshotSaleCollection)
            ?? panic("Could not borrow public sale reference")
    
        // purchase the moment
        let purchasedToken <- topshotSaleCollection.purchase(tokenID: tokenID, buyTokens: <-tokens)

        // deposit the purchased moment into the signer's collection
        self.collectionRef.deposit(token: <-purchasedToken)
    }
}
```