# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/FlowtyDrops.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "MetadataViews"
import "AddressUtils"
import "FungibleTokenMetadataViews"
import "FungibleTokenRouter"

// FlowtyDrops is a contract to help collections manage their primary sale needs on flow.
// Multiple drops can be made for a single contract (like how TopShot has had lots of pack drops),
// and can be split into phases to represent different behaviors over the course of a drop
access(all) contract FlowtyDrops {
    // The total number of nfts minted by this contract
    access(all) var TotalMinted: UInt64

    access(all) let ContainerStoragePath: StoragePath
    access(all) let ContainerPublicPath: PublicPath

    access(all) event DropAdded(address: Address, id: UInt64, name: String, description: String, imageUrl: String, start: UInt64?, end: UInt64?, nftType: String)
    access(all) event DropRemoved(address: Address, id: UInt64)
    access(all) event Minted(address: Address, dropID: UInt64, phaseID: UInt64, nftID: UInt64, nftType: String, totalMinted: UInt64)
    access(all) event PhaseAdded(dropID: UInt64, dropAddress: Address, id: UInt64, index: Int, activeCheckerType: String, pricerType: String, addressVerifierType: String)
    access(all) event PhaseRemoved(dropID: UInt64, dropAddress: Address, id: UInt64)

    access(all) entitlement Owner
    access(all) entitlement EditPhase

    // Interface to expose all the components necessary to participate in a drop
    // and to ask questions about a drop.
    access(all) resource interface DropPublic {
        access(all) view fun borrowPhasePublic(index: Int): &{PhasePublic}
        access(all) view fun borrowActivePhases(): [&{PhasePublic}]
        access(all) view fun borrowAllPhases(): [&{PhasePublic}]
        access(all) fun mint(
            payment: @{FungibleToken.Vault},
            amount: Int,
            phaseIndex: Int,
            expectedType: Type,
            receiverCap: Capability<&{NonFungibleToken.CollectionPublic}>,
            commissionReceiver: Capability<&{FungibleToken.Receiver}>?,
            data: {String: AnyStruct}
        ): @{FungibleToken.Vault} {
            pre {
                self.getDetails().paymentTokenTypes[payment.getType().identifier] == true: "unsupported payment token type"
                receiverCap.check(): "unvalid nft receiver capability"
                commissionReceiver == nil || commissionReceiver!.check(): "commission receiver must be nil or a valid capability"
                self.getType() == Type<@Drop>(): "unsupported type implementing DropPublic"
                expectedType.isSubtype(of: Type<@{NonFungibleToken.NFT}>()): "expected type must be an NFT"
                expectedType.identifier == self.getDetails().nftType: "expected type does not match drop details type"
                receiverCap.check(): "receiver capability is not valid"
            }
        }
        access(all) view fun getDetails(): DropDetails
    }

    // A phase represents a stage of a drop. Some drops will only have one
    // phase, while others could have many. For example, a drop with an allow list
    // and a public mint would likely have two phases.
    access(all) resource Phase: PhasePublic {
        access(all) event ResourceDestroyed(uuid: UInt64 = self.uuid)

        access(all) let details: PhaseDetails

        access(all) let data: {String: AnyStruct}
        access(all) let resources: @{String: AnyResource}

        // returns whether this phase of a drop has started.
        access(all) view fun isActive(): Bool {
            return self.details.activeChecker.hasStarted() && !self.details.activeChecker.hasEnded()
        }

        access(all) view fun getDetails(): PhaseDetails {
            return self.details
        }

        access(EditPhase) view fun borrowActiveCheckerAuth(): auth(Mutate) &{ActiveChecker} {
            return &self.details.activeChecker
        }

        access(EditPhase) view fun borrowPricerAuth(): auth(Mutate) &{Pricer} {
            return &self.details.pricer
        }

        access(EditPhase) view fun borrowAddressVerifierAuth(): auth(Mutate) &{AddressVerifier} {
            return &self.details.addressVerifier
        }

        init(details: PhaseDetails) {
            self.details = details

            self.data = {}
            self.resources <- {}
        }
    }

    // The primary resource of this contract. A drop has some top-level details, and some phase-specific details which are encapsulated
    // by each phase.
    access(all) resource Drop: DropPublic {
        access(all) event ResourceDestroyed(
            uuid: UInt64 = self.uuid,
            minterAddress: Address = self.minterCap.address,
            nftType: String = self.details.nftType,
            totalMinted: Int = self.details.totalMinted
        )

        // phases represent the stages of a drop. For example, a drop might have an allowlist and a public mint phase.
        access(self) let phases: @[Phase]
        // the details of a drop. This includes things like display information and total number of mints
        access(self) let details: DropDetails
        // capability to mint nfts with. Regardless of where a drop is hosted, the minter itself is what is responsible for creating nfts
        // and is used by the drop's mint method.
        access(self) let minterCap: Capability<&{Minter}>

        // general-purpose property bags which are needed to ensure extensibility of this resource
        access(all) let data: {String: AnyStruct}
        access(all) let resources: @{String: AnyResource}

        access(all) fun mint(
            payment: @{FungibleToken.Vault},
            amount: Int,
            phaseIndex: Int,
            expectedType: Type,
            receiverCap: Capability<&{NonFungibleToken.CollectionPublic}>,
            commissionReceiver: Capability<&{FungibleToken.Receiver}>?,
            data: {String: AnyStruct}
        ): @{FungibleToken.Vault} {
            pre {
                self.phases.length > phaseIndex: "phase index is too high"
            }

            // validate the payment vault amount and type
            let phase: &Phase = &self.phases[phaseIndex]
            assert(
                phase.details.addressVerifier.canMint(addr: receiverCap.address, num: amount, totalMinted: self.details.minters[receiverCap.address] ?? 0, data: {}),
                message: "receiver address has exceeded their mint capacity"
            )

            let paymentAmount = phase.details.pricer.getPrice(num: amount, paymentTokenType: payment.getType(), minter: receiverCap.address)
            assert(payment.balance >= paymentAmount, message: "payment balance is lower than payment amount")
            let withdrawn <- payment.withdraw(amount: paymentAmount) // make sure that we have a fresh vault resource

            // take commission
            if commissionReceiver != nil && commissionReceiver!.check() {
                let commission <- withdrawn.withdraw(amount: self.details.commissionRate * withdrawn.balance)
                commissionReceiver!.borrow()!.deposit(from: <-commission)
            }

            // The balance of the payment sent to the creator is equal to the paymentAmount - fees
            assert(paymentAmount * (1.0 - self.details.commissionRate) == withdrawn.balance, message: "incorrect payment amount")
            assert(phase.details.pricer.getPaymentTypes().contains(withdrawn.getType()), message: "unsupported payment type")
            assert(phase.details.activeChecker.hasStarted() && !phase.details.activeChecker.hasEnded(), message: "phase is not active")

            // mint the nfts
            let minter = self.minterCap.borrow() ?? panic("minter capability could not be borrowed")
            let mintedNFTs: @[{NonFungibleToken.NFT}] <- minter.mint(payment: <-withdrawn, amount: amount, phase: phase, data: data)
            assert(mintedNFTs.length == amount, message: "incorrect number of items returned")

            // distribute to receiver
            let receiver = receiverCap.borrow() ?? panic("could not borrow receiver capability")
            self.details.addMinted(num: mintedNFTs.length, addr: receiverCap.address)

            while mintedNFTs.length > 0 {
                let nft <- mintedNFTs.removeFirst()

                let nftType = nft.getType()
                FlowtyDrops.TotalMinted = FlowtyDrops.TotalMinted + 1
                emit Minted(address: receiverCap.address, dropID: self.uuid, phaseID: phase.uuid, nftID: nft.id, nftType: nftType.identifier, totalMinted: FlowtyDrops.TotalMinted)

                // validate that every nft is the right type
                assert(nftType == expectedType, message: "unexpected nft type was minted")
    
                receiver.deposit(token: <-nft)
            }

            // cleanup
            destroy mintedNFTs

            // return excess payment
            return <- payment
        }

        access(Owner) view fun borrowPhase(index: Int): auth(EditPhase) &Phase {
            return &self.phases[index]
        }


        access(all) view fun borrowPhasePublic(index: Int): &{PhasePublic} {
            return &self.phases[index]
        }

        access(all) view fun borrowActivePhases(): [&{PhasePublic}] {
            var arr: [&{PhasePublic}] = []
            var count = 0
            while count < self.phases.length {
                let ref = self.borrowPhasePublic(index: count)
                let activeChecker = ref.getDetails().activeChecker
                if activeChecker.hasStarted() && !activeChecker.hasEnded() {
                    arr = arr.concat([ref])
                }

                count = count + 1
            }

            return arr
        }

        access(all) view fun borrowAllPhases(): [&{PhasePublic}] {
            var arr: [&{PhasePublic}] = []
            var index = 0
            while index < self.phases.length {
                let ref = self.borrowPhasePublic(index: index)
                arr = arr.concat([ref])
                index = index + 1
            }

            return arr
        }

        access(Owner) fun addPhase(_ phase: @Phase) {
            emit PhaseAdded(
                dropID: self.uuid,
                dropAddress: self.owner!.address,
                id: phase.uuid,
                index: self.phases.length,
                activeCheckerType: phase.details.activeChecker.getType().identifier,
                pricerType: phase.details.pricer.getType().identifier,
                addressVerifierType: phase.details.addressVerifier.getType().identifier
            )
            self.phases.append(<-phase)
        }

        access(Owner) fun removePhase(index: Int): @Phase {
            pre {
                self.phases.length > index: "index is greater than length of phases"
            }

            let phase <- self.phases.remove(at: index)
            emit PhaseRemoved(dropID: self.uuid, dropAddress: self.owner!.address, id: phase.uuid)

            return <- phase
        }

        access(all) view fun getDetails(): DropDetails {
            return self.details
        }

        init(details: DropDetails, minterCap: Capability<&{Minter}>, phases: @[Phase]) {
            pre {
                minterCap.check(): "minter capability is not valid"
            }

            self.phases <- phases
            self.details = details
            self.minterCap = minterCap

            self.data = {}
            self.resources <- {}
        }
    }

    access(all) struct DropDetails {
        access(all) let display: MetadataViews.Display
        access(all) let medias: MetadataViews.Medias?
        access(all) var totalMinted: Int
        access(all) var minters: {Address: Int}
        access(all) let commissionRate: UFix64
        access(all) let nftType: String
        access(all) let paymentTokenTypes: {String: Bool}

        access(all) let data: {String: AnyStruct}

        access(contract) fun addMinted(num: Int, addr: Address) {
            self.totalMinted = self.totalMinted + num
            if self.minters[addr] == nil {
                self.minters[addr] = 0
            }

            self.minters[addr] = self.minters[addr]! + num
        }

        init(display: MetadataViews.Display, medias: MetadataViews.Medias?, commissionRate: UFix64, nftType: String, paymentTokenTypes: {String: Bool}) {
            pre {
                nftType != "": "nftType should be a composite type identifier"
            }

            self.display = display
            self.medias = medias
            self.totalMinted = 0
            self.commissionRate = commissionRate
            self.minters = {}
            self.nftType = nftType
            self.paymentTokenTypes = paymentTokenTypes

            self.data = {}
        }
    }

    // An ActiveChecker represents a phase being on or off, and holds information
    // about whether a phase has started or not.
    access(all) struct interface ActiveChecker {
        // Signal that a phase has started. If the phase has not ended, it means that this activeChecker's phase
        // is active
        access(all) view fun hasStarted(): Bool
        // Signal that a phase has ended. If an ActiveChecker has ended, minting will not work. That could mean
        // the drop is over, or it could mean another phase has begun.
        access(all) view fun hasEnded(): Bool

        access(all) view fun getStart(): UInt64?
        access(all) view fun getEnd(): UInt64?
    }

    access(all) resource interface PhasePublic {
        // What does a phase need to be able to answer/manage?
        // - What are the details of the phase being interactive with?
        // - How many items are left in the current phase?
        // - Can Address x mint on a phase?
        // - What is the cost to mint for the phase I am interested in (for address x)?
        access(all) view fun getDetails(): PhaseDetails
        access(all) view fun isActive(): Bool
    }

    access(all) struct PhaseDetails {
        // handles whether a phase is on or not
        access(all) let activeChecker: {ActiveChecker}

        // display information about a phase
        access(all) let display: MetadataViews.Display?

        // handles the pricing of a phase
        access(all) let pricer: {Pricer}

        // verifies whether an address is able to mint
        access(all) let addressVerifier: {AddressVerifier}

        // placecholder data dictionary to allow new fields to be accessed
        access(all) let data: {String: AnyStruct}

        init(activeChecker: {ActiveChecker}, display: MetadataViews.Display?, pricer: {Pricer}, addressVerifier: {AddressVerifier}) {
            self.activeChecker = activeChecker
            self.display = display
            self.pricer = pricer
            self.addressVerifier = addressVerifier

            self.data = {}
        }
    }

    // The AddressVerifier interface is responsible for determining whether an address is permitted to mint or not
    access(all) struct interface AddressVerifier {
        access(all) fun canMint(addr: Address, num: Int, totalMinted: Int, data: {String: AnyStruct}): Bool {
            return true
        }

        access(all) fun remainingForAddress(addr: Address, totalMinted: Int): Int? {
            return nil
        }

        access(all) view fun getMaxPerMint(addr: Address?, totalMinted: Int, data: {String: AnyStruct}): Int? {
            return nil
        }
    }

    // The pricer interface is responsible for the cost of a mint. It can vary by phase
    access(all) struct interface Pricer {
        access(all) fun getPrice(num: Int, paymentTokenType: Type, minter: Address?): UFix64
        access(all) fun getPaymentTypes(): [Type]
    }

    access(all) resource interface Minter {
        // mint is only able to be called either by this contract (FlowtyDrops) or the implementing contract.
        // In its default implementation, it is assumed that the receiver capability for payment is the FungibleTokenRouter
        access(contract) fun mint(payment: @{FungibleToken.Vault}, amount: Int, phase: &FlowtyDrops.Phase, data: {String: AnyStruct}): @[{NonFungibleToken.NFT}] {
            let resourceAddress = AddressUtils.parseAddress(self.getType())!
            let receiver = getAccount(resourceAddress).capabilities.get<&{FungibleToken.Receiver}>(FungibleTokenRouter.PublicPath).borrow()
                ?? panic("missing receiver at fungible token router path")
            receiver.deposit(from: <-payment)

            let nfts: @[{NonFungibleToken.NFT}] <- []

            var count = 0
            while count < amount {
                count = count + 1
                nfts.append(<- self.createNextNFT())
            }

            return <- nfts
        }

        // required so that the minter interface has a way to create NFTs on its implementing resource
        access(contract) fun createNextNFT(): @{NonFungibleToken.NFT}
    }
    
    // Struct to wrap obtaining a Drop container. Intended for use with the ViewResolver contract interface
    access(all) struct DropResolver {
        access(self) let cap: Capability<&{ContainerPublic}>

        access(all) fun borrowContainer(): &{ContainerPublic}? {
            return self.cap.borrow()
        }

        init(cap: Capability<&{ContainerPublic}>) {
            pre {
                cap.check(): "container capability is not valid"
            }

            self.cap = cap
        }
    }

    access(all) resource interface ContainerPublic {
        access(all) fun borrowDropPublic(id: UInt64): &{DropPublic}?
        access(all) fun getIDs(): [UInt64]
    }

    // Container holds drops so that one address can host more than one drop at once
    access(all) resource Container: ContainerPublic {
        access(self) let drops: @{UInt64: Drop}

        access(all) let data: {String: AnyStruct}
        access(all) let resources: @{String: AnyResource}

        access(Owner) fun addDrop(_ drop: @Drop) {
            let details = drop.getDetails()

            let phases = drop.borrowAllPhases()
            assert(phases.length > 0, message: "drops must have at least one phase to be added to a container")

            let firstPhaseDetails = phases[0].getDetails()

            emit DropAdded(
                address: self.owner!.address,
                id: drop.uuid,
                name: details.display.name,
                description: details.display.description,
                imageUrl: details.display.thumbnail.uri(),
                start: firstPhaseDetails.activeChecker.getStart(),
                end: firstPhaseDetails.activeChecker.getEnd(),
                nftType: details.nftType
            )
            destroy self.drops.insert(key: drop.uuid, <-drop)
        }

        access(Owner) fun removeDrop(id: UInt64): @Drop {
            pre {
                self.drops.containsKey(id): "drop was not found"
            }

            emit DropRemoved(address: self.owner!.address, id: id)
            return <- self.drops.remove(key: id)!
        }

        access(Owner) fun borrowDrop(id: UInt64): auth(Owner) &Drop? {
            return &self.drops[id]
        }

        access(all) fun borrowDropPublic(id: UInt64): &{DropPublic}? {
            return &self.drops[id]
        }

        access(all) fun getIDs(): [UInt64] {
            return self.drops.keys
        }

        init() {
            self.drops <- {}

            self.data = {}
            self.resources <- {}
        }
    }

    access(all) fun createPhase(details: PhaseDetails): @Phase {
        return <- create Phase(details: details)
    }

    access(all) fun createDrop(details: DropDetails, minterCap: Capability<&{Minter}>, phases: @[Phase]): @Drop {
        return <- create Drop(details: details, minterCap: minterCap, phases: <- phases)
    }

    access(all) fun createContainer(): @Container {
        return <- create Container()
    }

    access(all) fun getMinterStoragePath(type: Type): StoragePath {
        let segments = type.identifier.split(separator: ".")
        let identifier = "FlowtyDrops_Minter_".concat(segments[1]).concat("_").concat(segments[2])
        return StoragePath(identifier: identifier)!
    }

    init() {
        let identifier = "FlowtyDrops_".concat(self.account.address.toString())
        let containerIdentifier = identifier.concat("_Container")
        let minterIdentifier = identifier.concat("_Minter")

        self.ContainerStoragePath = StoragePath(identifier: containerIdentifier)!
        self.ContainerPublicPath = PublicPath(identifier: containerIdentifier)!

        self.TotalMinted = 0
    }
}
```