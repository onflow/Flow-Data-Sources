# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/market/create_start_sale.cdc

```
import FungibleToken from 0xFUNGIBLETOKENADDRESS
import Market from 0xMARKETADDRESS
import TopShot from 0xTOPSHOTADDRESS
import NonFungibleToken from 0xNFTADDRESS

// This transaction puts a moment owned by the user up for sale

// Parameters:
//
// tokenReceiverPath: token capability for the account who will receive tokens for purchase
// beneficiaryAccount: the Flow address of the account where a cut of the purchase will be sent
// cutPercentage: how much in percentage the beneficiary will receive from the sale
// momentID: ID of moment to be put on sale
// price: price of moment

transaction(tokenReceiverPath: PublicPath, beneficiaryAccount: Address, cutPercentage: UFix64, momentID: UInt64, price: UFix64) {

    // Local variables for the topshot collection and market sale collection objects
    let collectionRef: auth(NonFungibleToken.Withdraw) &TopShot.Collection
    let marketSaleCollectionRef: auth(Market.Create) &Market.SaleCollection
    
    prepare(acct: auth(Storage, Capabilities) &Account) {

        // check to see if a sale collection already exists
        if acct.storage.borrow<&Market.SaleCollection>(from: /storage/topshotSaleCollection) == nil {

            // get the fungible token capabilities for the owner and beneficiary

            let ownerCapability = acct.capabilities.get<&{FungibleToken.Receiver}>(tokenReceiverPath)!

            let beneficiaryCapability = getAccount(beneficiaryAccount).capabilities.get<&{FungibleToken.Receiver}>(tokenReceiverPath)!

            // create a new sale collection
            let topshotSaleCollection <- Market.createSaleCollection(ownerCapability: ownerCapability, beneficiaryCapability: beneficiaryCapability, cutPercentage: cutPercentage)
            
            // save it to storage
            acct.storage.save(<-topshotSaleCollection, to: /storage/topshotSaleCollection)
        
            // create a public link to the sale collection
            acct.capabilities.publish(
                acct.capabilities.storage.issue<&Market.SaleCollection>(/storage/topshotSaleCollection),
                at: /public/topshotSaleCollection
            )
        }
        
        // borrow a reference to the seller's moment collection
        self.collectionRef = acct.storage.borrow<auth(NonFungibleToken.Withdraw) &TopShot.Collection>(from: /storage/MomentCollection)
            ?? panic("Could not borrow from MomentCollection in storage")

        // borrow a reference to the sale
        self.marketSaleCollectionRef = acct.storage.borrow<auth(Market.Create) &Market.SaleCollection>(from: /storage/topshotSaleCollection)
            ?? panic("Could not borrow from sale in storage")
    }

    execute {

        // withdraw the moment to put up for sale
        let token <- self.collectionRef.withdraw(withdrawID: momentID) as! @TopShot.NFT
        
        // the the moment for sale
        self.marketSaleCollectionRef.listForSale(token: <-token, price: UFix64(price))
    }
}
```