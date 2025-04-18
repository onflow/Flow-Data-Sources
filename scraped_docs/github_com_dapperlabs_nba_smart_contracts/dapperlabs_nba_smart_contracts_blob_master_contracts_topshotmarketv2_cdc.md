# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/contracts/TopShotMarketV2.cdc

```
/*

    TopShotMarketV2.cdc

    Description: Contract definitions for users to sell their moments

    Marketplace is where users can create a sale collection that they
    store in their account storage. In the sale collection, 
    they can put their NFTs up for sale with a price and publish a 
    reference so that others can see the sale.

    If another user sees an NFT that they want to buy,
    they can send fungible tokens that equal or exceed the buy price
    to buy the NFT.  The NFT is transferred to them when
    they make the purchase.

    Each user who wants to sell tokens will have a sale collection 
    instance in their account that contains price information 
    for each node in their collection. The sale holds a capability that 
    links to their main moment collection.

    They can give a reference to this collection to a central contract
    so that it can list the sales in a central place

    When a user creates a sale, they will supply four arguments:
    - A TopShot.Collection capability that allows their sale to withdraw
      a moment when it is purchased.
    - A FungibleToken.Receiver capability as the place where the payment for the token goes.
    - A FungibleToken.Receiver capability specifying a beneficiary, where a cut of the purchase gets sent. 
    - A cut percentage, specifying how much the beneficiary will recieve.
    
    The cut percentage can be set to zero if the user desires and they 
    will receive the entirety of the purchase. TopShot will initialize sales 
    for users with the TopShot admin vault as the vault where cuts get 
    deposited to.
*/

import FungibleToken from 0xFUNGIBLETOKENADDRESS
import NonFungibleToken from 0xNFTADDRESS
import TopShot from 0xTOPSHOTADDRESS

pub contract TopShotMarketV2 {

    // -----------------------------------------------------------------------
    // TopShot Market contract Event definitions
    // -----------------------------------------------------------------------

    // emitted when a TopShot moment is listed for sale
    pub event MomentListed(id: UInt64, price: UFix64, seller: Address?)
    // emitted when the price of a listed moment has changed
    pub event MomentPriceChanged(id: UInt64, newPrice: UFix64, seller: Address?)
    // emitted when a token is purchased from the market
    pub event MomentPurchased(id: UInt64, price: UFix64, seller: Address?)
    // emitted when a moment has been withdrawn from the sale
    pub event MomentWithdrawn(id: UInt64, owner: Address?)
    // emitted when the cut percentage of the sale has been changed by the owner
    pub event CutPercentageChanged(newPercent: UFix64, seller: Address?)

    pub let marketStoragePath: StoragePath

    pub let marketPublicPath: PublicPath

    // SalePublic 
    //
    // The interface that a user can publish a capability to their sale
    // to allow others to access their sale
    pub resource interface SalePublic {
        pub var cutPercentage: UFix64
        pub fun purchase(tokenID: UInt64, buyTokens: @FungibleToken.Vault): @TopShot.NFT {
            post {
                result.id == tokenID: "The ID of the withdrawn token must be the same as the requested ID"
            }
        }
        pub fun getPrice(tokenID: UInt64): UFix64?
        pub fun getIDs(): [UInt64]
        pub fun borrowMoment(id: UInt64): &TopShot.NFT? {
            // If the result isn't nil, the id of the returned reference
            // should be the same as the argument to the function
            post {
                (result == nil) || (result?.id == id): 
                    "Cannot borrow Moment reference: The ID of the returned reference is incorrect"
            }
        }
    }

    // SaleCollection
    //
    // This is the main resource that token sellers will store in their account
    // to manage the NFTs that they are selling. The SaleCollection
    // holds a TopShot Collection resource to store the moments that are for sale.
    // The SaleCollection also keeps track of the price of each token.
    // 
    // When a token is purchased, a cut is taken from the tokens
    // and sent to the beneficiary, then the rest are sent to the seller.
    //
    // The seller chooses who the beneficiary is and what percentage
    // of the tokens gets taken from the purchase
    pub resource SaleCollection: SalePublic {

        // A collection of the moments that the user has for sale
        access(self) var ownerCollection: Capability<&TopShot.Collection>

        // Dictionary of the low low prices for each NFT by ID
        access(self) var prices: {UInt64: UFix64}

        // The fungible token vault of the seller
        // so that when someone buys a token, the tokens are deposited
        // to this Vault
        access(self) var ownerCapability: Capability<&{FungibleToken.Receiver}>

        // The capability that is used for depositing 
        // the beneficiary's cut of every sale
        access(self) var beneficiaryCapability: Capability<&{FungibleToken.Receiver}>

        // The percentage that is taken from every purchase for the beneficiary
        // For example, if the percentage is 15%, cutPercentage = 0.15
        pub var cutPercentage: UFix64

        init (ownerCollection: Capability<&TopShot.Collection>, ownerCapability: Capability<&{FungibleToken.Receiver}>, beneficiaryCapability: Capability<&{FungibleToken.Receiver}>, cutPercentage: UFix64) {
            pre {
                // Check that the owner's moment collection capability is correct
                ownerCollection.borrow() != nil: 
                    "Owner's Moment Collection Capability is invalid!"

                // Check that both capabilities are for fungible token Vault receivers
                ownerCapability.borrow() != nil: 
                    "Owner's Receiver Capability is invalid!"
                beneficiaryCapability.borrow() != nil: 
                    "Beneficiary's Receiver Capability is invalid!" 
            }
            
            // create an empty collection to store the moments that are for sale
            self.ownerCollection = ownerCollection
            self.ownerCapability = ownerCapability
            self.beneficiaryCapability = beneficiaryCapability
            // prices are initially empty because there are no moments for sale
            self.prices = {}
            self.cutPercentage = cutPercentage
        }

        // listForSale lists an NFT for sale in this sale collection
        // at the specified price
        //
        // Parameters: tokenID: The id of the NFT to be put up for sale
        //             price: The price of the NFT
        pub fun listForSale(tokenID: UInt64, price: UFix64) {
            pre {
                self.ownerCollection.borrow()!.borrowMoment(id: tokenID) != nil:
                    "Moment does not exist in the owner's collection"
            }

            // Set the token's price
            self.prices[tokenID] = price

            emit MomentListed(id: tokenID, price: price, seller: self.owner?.address)
        }

        // cancelSale cancels a moment sale and clears its price
        //
        // Parameters: tokenID: the ID of the token to withdraw from the sale
        //
        pub fun cancelSale(tokenID: UInt64) {
            pre {
                self.prices[tokenID] != nil: "Token with the specified ID is not already for sale"
            }

            // Remove the price from the prices dictionary
            self.prices.remove(key: tokenID)

            // Set prices to nil for the withdrawn ID
            self.prices[tokenID] = nil
            
            // Emit the event for withdrawing a moment from the Sale
            emit MomentWithdrawn(id: tokenID, owner: self.owner?.address)
        }

        // purchase lets a user send tokens to purchase an NFT that is for sale
        // the purchased NFT is returned to the transaction context that called it
        //
        // Parameters: tokenID: the ID of the NFT to purchase
        //             buyTokens: the fungible tokens that are used to buy the NFT
        //
        // Returns: @TopShot.NFT: the purchased NFT
        pub fun purchase(tokenID: UInt64, buyTokens: @FungibleToken.Vault): @TopShot.NFT {
            pre {
                self.ownerCollection.borrow()!.borrowMoment(id: tokenID) != nil && self.prices[tokenID] != nil:
                    "No token matching this ID for sale!"           
                buyTokens.balance == (self.prices[tokenID] ?? UFix64(0)):
                    "Not enough tokens to buy the NFT!"
            }

            // Read the price for the token
            let price = self.prices[tokenID]!

            // Set the price for the token to nil
            self.prices[tokenID] = nil

            // Take the cut of the tokens that the beneficiary gets from the sent tokens
            let beneficiaryCut <- buyTokens.withdraw(amount: price*self.cutPercentage)

            // Deposit it into the beneficiary's Vault
            self.beneficiaryCapability.borrow()!
                .deposit(from: <-beneficiaryCut)
            
            // Deposit the remaining tokens into the owners vault
            self.ownerCapability.borrow()!
                .deposit(from: <-buyTokens)

            emit MomentPurchased(id: tokenID, price: price, seller: self.owner?.address)

            // Return the purchased token
            let boughtMoment <- self.ownerCollection.borrow()!.withdraw(withdrawID: tokenID) as! @TopShot.NFT

            return <-boughtMoment
        }

        // changePercentage changes the cut percentage of the tokens that are for sale
        //
        // Parameters: newPercent: The new cut percentage for the sale
        pub fun changePercentage(_ newPercent: UFix64) {
            pre {
                newPercent <= 1.0: "Cannot set cut percentage to greater than 100%"
            }
            self.cutPercentage = newPercent

            emit CutPercentageChanged(newPercent: newPercent, seller: self.owner?.address)
        }

        // changeOwnerReceiver updates the capability for the sellers fungible token Vault
        //
        // Parameters: newOwnerCapability: The new fungible token capability for the account 
        //                                 who received tokens for purchases
        pub fun changeOwnerReceiver(_ newOwnerCapability: Capability<&{FungibleToken.Receiver}>) {
            pre {
                newOwnerCapability.borrow() != nil: 
                    "Owner's Receiver Capability is invalid!"
            }
            self.ownerCapability = newOwnerCapability
        }

        // changeBeneficiaryReceiver updates the capability for the beneficiary of the cut of the sale
        //
        // Parameters: newBeneficiaryCapability the new capability for the beneficiary of the cut of the sale
        //
        pub fun changeBeneficiaryReceiver(_ newBeneficiaryCapability: Capability<&{FungibleToken.Receiver}>) {
            pre {
                newBeneficiaryCapability.borrow() != nil: 
                    "Beneficiary's Receiver Capability is invalid!" 
            }
            self.beneficiaryCapability = newBeneficiaryCapability
        }

        // getPrice returns the price of a specific token in the sale
        // 
        // Parameters: tokenID: The ID of the NFT whose price to get
        //
        // Returns: UFix64: The price of the token
        pub fun getPrice(tokenID: UInt64): UFix64? {
            return self.prices[tokenID]
        }

        // getIDs returns an array of token IDs that are for sale
        pub fun getIDs(): [UInt64] {
            return self.prices.keys
        }

        // borrowMoment Returns a borrowed reference to a Moment for sale
        // so that the caller can read data from it
        //
        // Parameters: id: The ID of the moment to borrow a reference to
        //
        // Returns: &TopShot.NFT? Optional reference to a moment for sale 
        //                        so that the caller can read its data
        //
        pub fun borrowMoment(id: UInt64): &TopShot.NFT? {
            if self.prices[id] != nil {
                let ref = self.ownerCollection.borrow()!.borrowMoment(id: id)
                return ref
            } else {
                return nil
            }
        }
    }

    // createCollection returns a new collection resource to the caller
    pub fun createSaleCollection(ownerCollection: Capability<&TopShot.Collection>, ownerCapability: Capability<&{FungibleToken.Receiver}>, beneficiaryCapability: Capability<&{FungibleToken.Receiver}>, cutPercentage: UFix64): @SaleCollection {
        return <- create SaleCollection(ownerCollection: ownerCollection, ownerCapability: ownerCapability, beneficiaryCapability: beneficiaryCapability, cutPercentage: cutPercentage)
    }

    init() {
        self.marketStoragePath = /storage/topshotSalev2Collection
        self.marketPublicPath = /public/topshotSalev2Collection
    }
}
 
```