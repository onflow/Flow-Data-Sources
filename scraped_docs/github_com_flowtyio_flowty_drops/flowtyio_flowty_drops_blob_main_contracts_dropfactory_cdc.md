# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/DropFactory.cdc

```
import "FungibleToken"
import "MetadataViews"

import "FlowtyDrops"
import "FlowtyActiveCheckers"
import "FlowtyAddressVerifiers"
import "FlowtyPricers"

/*
The DropFactory is a contract that helps create common types of drops
*/
access(all) contract DropFactory {
    access(all) fun createEndlessOpenEditionDrop(
        price: UFix64,
        paymentTokenType: Type,
        dropDisplay: MetadataViews.Display,
        minterCap: Capability<&{FlowtyDrops.Minter}>,
        nftTypeIdentifier: String
    ): @FlowtyDrops.Drop {
        pre {
            paymentTokenType.isSubtype(of: Type<@{FungibleToken.Vault}>()): "paymentTokenType must be a FungibleToken"
        }

        // This drop is always on and never ends.
        let activeChecker = FlowtyActiveCheckers.AlwaysOn()

        // All addresses are allowed to participate
        let addressVerifier = FlowtyAddressVerifiers.AllowAll(maxPerMint: 10)

        // The cost of each mint is the same, and only permits one token type as payment
        let pricer = FlowtyPricers.FlatPrice(price: price, paymentTokenType: paymentTokenType)
        
        let phaseDetails = FlowtyDrops.PhaseDetails(activeChecker: activeChecker, display: nil, pricer: pricer, addressVerifier: addressVerifier)
        let phase <- FlowtyDrops.createPhase(details: phaseDetails)


        let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
        let dropDetails = FlowtyDrops.DropDetails(display: dropDisplay, medias: nil, commissionRate: 0.05, nftType: nftTypeIdentifier, paymentTokenTypes: {paymentTokenType.identifier: true})
        let drop <- FlowtyDrops.createDrop(details: dropDetails, minterCap: minterCap, phases: <- [<-phase])

        return <- drop
    }

    access(all) fun createTimeBasedOpenEditionDrop(
        price: UFix64,
        paymentTokenType: Type,
        dropDisplay: MetadataViews.Display,
        minterCap: Capability<&{FlowtyDrops.Minter}>,
        startUnix: UInt64?,
        endUnix: UInt64?,
        nftTypeIdentifier: String
    ): @FlowtyDrops.Drop {
        pre {
            paymentTokenType.isSubtype(of: Type<@{FungibleToken.Vault}>()): "paymentTokenType must be a FungibleToken"
        }

        // This ActiveChecker turns on at a set unix timestamp (or is on by default if nil), and ends at the specified end date if provided
        let activeChecker = FlowtyActiveCheckers.TimestampChecker(start: startUnix, end: endUnix)

        // All addresses are allowed to participate
        let addressVerifier = FlowtyAddressVerifiers.AllowAll(maxPerMint: 10)

        // The cost of each mint is the same, and only permits one token type as payment
        let pricer = FlowtyPricers.FlatPrice(price: price, paymentTokenType: paymentTokenType)
        
        let phaseDetails = FlowtyDrops.PhaseDetails(activeChecker: activeChecker, display: nil, pricer: pricer, addressVerifier: addressVerifier)
        let phase <- FlowtyDrops.createPhase(details: phaseDetails)

        let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
        let dropDetails = FlowtyDrops.DropDetails(display: dropDisplay, medias: nil, commissionRate: 0.05, nftType: nftTypeIdentifier, paymentTokenTypes: {paymentTokenType.identifier: true})
        let drop <- FlowtyDrops.createDrop(details: dropDetails, minterCap: minterCap, phases: <- [<-phase])

        return <- drop
    }
}
```