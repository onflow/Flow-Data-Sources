# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/DropTypes.cdc

```
import "FlowtyDrops"
import "MetadataViews"
import "ViewResolver"
import "AddressUtils"
import "ContractManager"

access(all) contract DropTypes {
    access(all) struct Display {
        access(all) let name: String
        access(all) let description: String
        access(all) let url: String

        init(_ display: MetadataViews.Display) {
            self.name = display.name
            self.description = display.description
            self.url = display.thumbnail.uri()
        }
    }

    access(all) struct Media {
        access(all) let url: String
        access(all) let mediaType: String

        init(_ media: MetadataViews.Media) {
            self.url = media.file.uri()
            self.mediaType = media.mediaType
        }
    }

    access(all) struct DropSummary {
        access(all) let id: UInt64
        access(all) let display: Display
        access(all) let medias: [Media]
        access(all) let totalMinted: Int
        access(all) let minterCount: Int
        access(all) let commissionRate: UFix64
        access(all) let nftType: String
        access(all) let creator: Address?
        access(all) let paymentTokenTypes: {String: Bool}

        access(all) let address: Address?
        access(all) let mintedByAddress: Int?

        access(all) let phases: [PhaseSummary]

        access(all) let blockTimestamp: UInt64
        access(all) let blockHeight: UInt64
        access(all) let royaltyRate: UFix64

        init(
            id: UInt64,
            display: MetadataViews.Display,
            medias: MetadataViews.Medias?,
            totalMinted: Int,
            minterCount: Int,
            mintedByAddress: Int?,
            commissionRate: UFix64,
            nftType: Type,
            address: Address?,
            phases: [PhaseSummary],
            royaltyRate: UFix64,
            creator: Address?,
            paymentTokenTypes: {String: Bool}
        ) {
            self.id = id
            self.display = Display(display)
            self.creator = creator
            
            self.medias = []
            for m in medias?.items ?? [] {
                self.medias.append(Media(m))
            }


            self.totalMinted = totalMinted
            self.commissionRate = commissionRate
            self.minterCount = minterCount
            self.mintedByAddress = mintedByAddress
            self.nftType = nftType.identifier
            self.address = address
            self.phases = phases

            let b = getCurrentBlock()
            self.blockHeight = b.height
            self.blockTimestamp = UInt64(b.timestamp)
            self.royaltyRate = royaltyRate
            self.paymentTokenTypes = paymentTokenTypes
        }
    }

    access(all) struct Quote {
        access(all) let price: UFix64
        access(all) let quantity: Int
        access(all) let paymentIdentifier: String
        access(all) let minter: Address?

        init(price: UFix64, quantity: Int, paymentIdentifier: String, minter: Address?) {
            self.price = price
            self.quantity = quantity
            self.paymentIdentifier = paymentIdentifier
            self.minter = minter
        }
    }

    access(all) struct PhaseSummary {
        access(all) let id: UInt64
        access(all) let index: Int

        access(all) let activeCheckerType: String
        access(all) let pricerType: String
        access(all) let addressVerifierType: String

        access(all) let hasStarted: Bool
        access(all) let hasEnded: Bool
        access(all) let start: UInt64?
        access(all) let end: UInt64?

        access(all) let paymentTypes: [String]
        
        access(all) let address: Address?
        access(all) let remainingForAddress: Int?
        access(all) let maxPerMint: Int?

        access(all) let quotes: {String: Quote}

        init(
            index: Int,
            phase: &{FlowtyDrops.PhasePublic},
            address: Address?,
            totalMinted: Int?,
            minter: Address?,
            quantity: Int?,
            paymentIdentifiers: [String]
        ) {
            self.index = index
            self.id = phase.uuid

            let d: FlowtyDrops.PhaseDetails = phase.getDetails()
            self.activeCheckerType = d.activeChecker.getType().identifier
            self.pricerType = d.pricer.getType().identifier
            self.addressVerifierType = d.addressVerifier.getType().identifier

            self.hasStarted = d.activeChecker.hasStarted()
            self.hasEnded = d.activeChecker.hasEnded()
            self.start = d.activeChecker.getStart()
            self.end = d.activeChecker.getEnd()

            self.paymentTypes = []
            for pt in d.pricer.getPaymentTypes() {
                self.paymentTypes.append(pt.identifier)
            }

            if let addr = address {
                self.address = address
                self.remainingForAddress = d.addressVerifier.remainingForAddress(addr: addr, totalMinted: totalMinted ?? 0)
            } else {
                self.address = nil
                self.remainingForAddress = nil
            }

            self.maxPerMint = d.addressVerifier.getMaxPerMint(addr: self.address, totalMinted: totalMinted ?? 0, data: {})
            self.quotes = {}

            for paymentIdentifier in paymentIdentifiers {
                let price = d.pricer.getPrice(num: quantity!, paymentTokenType: CompositeType(paymentIdentifier)!, minter: minter)
                self.quotes[paymentIdentifier] = Quote(price: price, quantity: quantity!, paymentIdentifier: paymentIdentifier, minter: minter)
            }
        }
    }

    access(all) fun getDropSummary(nftTypeIdentifier: String, dropID: UInt64, minter: Address?, quantity: Int?, paymentIdentifiers: [String]): DropSummary? {
        let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
        let segments = nftTypeIdentifier.split(separator: ".")
        let contractAddress = AddressUtils.parseAddress(nftType)!
        let contractName = segments[2]

        let creator = self.getCreatorAddress(contractAddress)

        let resolver = getAccount(contractAddress).contracts.borrow<&{ViewResolver}>(name: contractName)
        if resolver == nil {
            return nil
        }

        let dropResolver = resolver!.resolveContractView(resourceType: nftType, viewType: Type<FlowtyDrops.DropResolver>()) as! FlowtyDrops.DropResolver?
        if dropResolver == nil {
            return nil
        }

        let container = dropResolver!.borrowContainer()
        if container == nil {
            return nil
        }

        let drop = container!.borrowDropPublic(id: dropID)
        if drop == nil {
            return nil
        }

        let dropDetails = drop!.getDetails()

        let phaseSummaries: [PhaseSummary] = []
        for index, phase in drop!.borrowAllPhases() {
            let summary = PhaseSummary(
                index: index,
                phase: phase,
                address: minter,
                totalMinted: minter != nil ? dropDetails.minters[minter!] : nil,
                minter: minter,
                quantity: quantity,
                paymentIdentifiers: paymentIdentifiers.length > 0 ? paymentIdentifiers : dropDetails.paymentTokenTypes.keys
            )
            phaseSummaries.append(summary)
        }

        var royaltyRate = 0.0
        if let tmpRoyalties = resolver!.resolveContractView(resourceType: nftType, viewType: Type<MetadataViews.Royalties>()) {
            let royalties = tmpRoyalties as! MetadataViews.Royalties
            for r in royalties.getRoyalties() {
                royaltyRate = royaltyRate + r.cut
            }
        }

        let dropSummary = DropSummary(
            id: drop!.uuid,
            display: dropDetails.display,
            medias: dropDetails.medias,
            totalMinted: dropDetails.totalMinted,
            minterCount: dropDetails.minters.keys.length,
            mintedByAddress: minter != nil ? dropDetails.minters[minter!] : nil,
            commissionRate: dropDetails.commissionRate,
            nftType: CompositeType(dropDetails.nftType)!,
            address: minter,
            phases: phaseSummaries,
            royaltyRate: royaltyRate,
            creator: creator,
            paymentTokenTypes: dropDetails.paymentTokenTypes
        )

        return dropSummary
    }

    access(all) fun getAllDropSummaries(nftTypeIdentifier: String, minter: Address?, quantity: Int?, paymentIdentifiers: [String]): [DropSummary] {
        let nftType = CompositeType(nftTypeIdentifier) ?? panic("invalid nft type identifier")
        let segments = nftTypeIdentifier.split(separator: ".")
        let contractAddress = AddressUtils.parseAddress(nftType)!
        let contractName = segments[2]

        let creator = self.getCreatorAddress(contractAddress)
        
        let resolver = getAccount(contractAddress).contracts.borrow<&{ViewResolver}>(name: contractName)
        if resolver == nil {
            return []
        }

        let dropResolver = resolver!.resolveContractView(resourceType: nftType, viewType: Type<FlowtyDrops.DropResolver>()) as! FlowtyDrops.DropResolver?
        if dropResolver == nil {
            return []
        }

        let container = dropResolver!.borrowContainer()
        if container == nil {
            return []
        }

        let summaries: [DropSummary] = []
        for id in container!.getIDs() {
            let drop = container!.borrowDropPublic(id: id)
            if drop == nil {
                continue
            }

            let dropDetails = drop!.getDetails()

            let phaseSummaries: [PhaseSummary] = []
            for index, phase in drop!.borrowAllPhases() {
                let summary = PhaseSummary(
                    index: index,
                    phase: phase,
                    address: minter,
                    totalMinted: minter != nil ? dropDetails.minters[minter!] : nil,
                    minter: minter,
                    quantity: quantity,
                    paymentIdentifiers: paymentIdentifiers.length > 0 ? paymentIdentifiers : dropDetails.paymentTokenTypes.keys
                )
                phaseSummaries.append(summary)
            }

            if CompositeType(dropDetails.nftType) == nil {
                continue
            }

            var royaltyRate = 0.0
            if let tmpRoyalties = resolver!.resolveContractView(resourceType: nftType, viewType: Type<MetadataViews.Royalties>()) {
                let royalties = tmpRoyalties as! MetadataViews.Royalties
                for r in royalties.getRoyalties() {
                    royaltyRate = royaltyRate + r.cut
                }
            }

            summaries.append(DropSummary(
                id: drop!.uuid,
                display: dropDetails.display,
                medias: dropDetails.medias,
                totalMinted: dropDetails.totalMinted,
                minterCount: dropDetails.minters.keys.length,
                mintedByAddress: minter != nil ? dropDetails.minters[minter!] : nil,
                commissionRate: dropDetails.commissionRate,
                nftType: CompositeType(dropDetails.nftType)!,
                address: minter,
                phases: phaseSummaries,
                royaltyRate: royaltyRate,
                creator: creator,
                paymentTokenTypes: dropDetails.paymentTokenTypes
            ))
        }

        return summaries
    }

    access(all) fun getCreatorAddress(_ contractAddress: Address): Address? {
        // We look for a two-way relationship between creator and collection. A contract can expose an address at ContractManager.OwnerPublicPath
        // specifying the owning account. If found, we will check that same account for a &ContractManager.Manager resource at ContractManager.PublicPath,
        // which, when borrowed, can return its underlying account address using &Manager.getAccount().
        //
        // If the addresses match, we consider this account to be the creator of a drop
        let tmp = getAccount(contractAddress).capabilities.borrow<&Address>(ContractManager.OwnerPublicPath)
        if tmp == nil {
            return nil
        }

        let creator = *(tmp!)
        let manager = getAccount(creator).capabilities.borrow<&ContractManager.Manager>(ContractManager.PublicPath)
        if manager == nil {
            return nil
        }

        let contractManagerAccount = manager!.getAccount()

        if contractManagerAccount.address != contractAddress {
            return nil
        }
 
        return creator
    }
}
```