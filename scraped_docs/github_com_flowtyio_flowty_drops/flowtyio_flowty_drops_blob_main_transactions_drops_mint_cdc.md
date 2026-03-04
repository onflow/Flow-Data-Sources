# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/mint.cdc

```
import "ViewResolver"
import "MetadataViews"
import "NonFungibleToken"
import "FungibleToken"
import "AddressUtils"

import "FlowtyDrops"

transaction(
    nftTypeIdentifier: String,
    numToMint: Int,
    totalCost: UFix64,
    paymentIdentifier: String,
    paymentStoragePath: StoragePath,
    paymentReceiverPath: PublicPath,
    dropID: UInt64,
    dropPhaseIndex: Int,
    commissionAddress: Address
) {
    prepare(acct: auth(Capabilities, Storage) &Account) {
        let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
        let segments = nftTypeIdentifier.split(separator: ".")
        let contractAddress = AddressUtils.parseAddress(nftType)!
        let contractName = segments[2]

        let resolver = getAccount(contractAddress).contracts.borrow<&{ViewResolver}>(name: contractName)
            ?? panic("ViewResolver contract interface not found on contract address + name")
        
        let collectionData = resolver.resolveContractView(resourceType: nftType, viewType: Type<MetadataViews.NFTCollectionData>())! as! MetadataViews.NFTCollectionData
        if acct.storage.borrow<&AnyResource>(from: collectionData.storagePath) == nil {
            acct.storage.save(<- collectionData.createEmptyCollection(), to: collectionData.storagePath)

            acct.capabilities.publish(
                acct.capabilities.storage.issue<&{NonFungibleToken.Collection}>(collectionData.storagePath),
                at: collectionData.publicPath
            )

            acct.capabilities.storage.issue<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection, NonFungibleToken.Provider}>(collectionData.storagePath)
        }
        let receiverCap = acct.capabilities.get<&{NonFungibleToken.CollectionPublic}>(collectionData.publicPath)
        assert(receiverCap.check(), message: "invalid receiver capability")

        let vault = acct.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(from: paymentStoragePath)
            ?? panic("could not borrow token provider")

        let paymentVault <- vault.withdraw(amount: totalCost)

        let dropResolver = resolver.resolveContractView(resourceType: nftType, viewType: Type<FlowtyDrops.DropResolver>())! as! FlowtyDrops.DropResolver
        let dropContainer = dropResolver.borrowContainer()
            ?? panic("unable to borrow drop container")

        let drop = dropContainer.borrowDropPublic(id: dropID) ?? panic("drop not found")

        let commissionReceiver = getAccount(commissionAddress).capabilities.get<&{FungibleToken.Receiver}>(paymentReceiverPath)
        let remainder <- drop.mint(
            payment: <-paymentVault,
            amount: numToMint,
            phaseIndex: dropPhaseIndex,
            expectedType: nftType,
            receiverCap: receiverCap,
            commissionReceiver: commissionReceiver,
            data: {}
        )

        if remainder.balance > 0.0 {
            acct.storage.borrow<&{FungibleToken.Receiver}>(from: paymentStoragePath)!.deposit(from: <-remainder)
        } else {
            destroy remainder
        }
    }
}
```