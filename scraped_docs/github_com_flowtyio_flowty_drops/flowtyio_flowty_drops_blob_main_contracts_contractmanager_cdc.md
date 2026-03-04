# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/ContractManager.cdc

```
import "FlowToken"
import "FungibleToken"
import "FungibleTokenRouter"
import "HybridCustody"
import "MetadataViews"
import "ViewResolver"
import "AddressUtils"
import "CapabilityFactory"
import "CapabilityFilter"
import "FungibleTokenMetadataViews"

access(all) contract ContractManager {
    access(all) let StoragePath: StoragePath
    access(all) let PublicPath: PublicPath

    access(all) let OwnerStoragePath: StoragePath
    access(all) let OwnerPublicPath: PublicPath

    access(all) entitlement Manage

    access(all) event ManagerSaved(uuid: UInt64, contractAddress: Address, ownerAddress: Address)

    access(all) resource Manager {
        access(self) let acct: Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>
        access(self) let routerCap: Capability<auth(FungibleTokenRouter.Owner) &FungibleTokenRouter.Router>

        access(all) let data: {String: AnyStruct}
        access(all) let resources: @{String: AnyResource}

        access(Manage) fun borrowContractAccount(): auth(Contracts) &Account {
            return self.acct.borrow()!
        }

        access(Manage) fun addOverride(type: Type, addr: Address) {
            let router = self.routerCap.borrow() ?? panic("fungible token router is not valid")
            router.addOverride(type: type, addr: addr)
        }

        access(Manage) fun getSwitchboard(): auth(FungibleTokenRouter.Owner) &FungibleTokenRouter.Router {
            return self.routerCap.borrow()!
        }

        access(all) fun addFlowTokensToAccount(_ tokens: @FlowToken.Vault) {
            self.acct.borrow()!.storage.borrow<&{FungibleToken.Receiver}>(from: /storage/flowTokenVault)!.deposit(from: <-tokens)
        }

        access(all) fun getAccount(): &Account {
            return getAccount(self.acct.address)
        }

        // Should be called after saving a ContractManager resource to signal that a new address stores (and therefore "owns")
        // this manager resource's acct capability. Without this, it is not possible to track the original creator of a contract
        // when using the ContractManager
        access(Manage) fun onSave() {
            let acct = self.acct.borrow()!

            acct.storage.load<Address>(from: ContractManager.OwnerStoragePath)
            acct.storage.save(self.owner!.address, to: ContractManager.OwnerStoragePath)

            if !acct.capabilities.get<&Address>(ContractManager.OwnerPublicPath).check() {
                acct.capabilities.unpublish(ContractManager.OwnerPublicPath)
                acct.capabilities.publish(
                    acct.capabilities.storage.issue<&Address>(ContractManager.OwnerStoragePath),
                    at: ContractManager.OwnerPublicPath
                )
            }

            self.configureHybridCustody(acct: acct)
            emit ManagerSaved(uuid: self.uuid, contractAddress: self.acct.address, ownerAddress: self.owner!.address)
        }

        init(tokens: @FlowToken.Vault, defaultRouterAddress: Address) {
            pre {
                tokens.balance >= 0.001: "minimum balance of 0.001 required for initialization"
            }

            let acct = Account(payer: ContractManager.account)
            self.acct = acct.capabilities.account.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()
            assert(self.acct.check(), message: "failed to setup account capability")

            acct.storage.borrow<&{FungibleToken.Receiver}>(from: /storage/flowTokenVault)!.deposit(from: <-tokens)

            // setup a provider capability so that tokens are accessible via hybrid custody
            acct.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(/storage/flowTokenVault)

            let router <- FungibleTokenRouter.createRouter(defaultAddress: defaultRouterAddress)
            acct.storage.save(<-router, to: FungibleTokenRouter.StoragePath)

            let receiver = acct.capabilities.storage.issue<&{FungibleToken.Receiver}>(FungibleTokenRouter.StoragePath)
            assert(receiver.check(), message: "invalid switchboard receiver capability")
            acct.capabilities.publish(receiver, at: FungibleTokenRouter.PublicPath)

            self.routerCap = acct.capabilities.storage.issue<auth(FungibleTokenRouter.Owner) &FungibleTokenRouter.Router>(FungibleTokenRouter.StoragePath)

            self.data = {}
            self.resources <- {}
        }

        access(self) fun configureHybridCustody(acct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account) {
            if acct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath) == nil {
                let ownedAccount <- HybridCustody.createOwnedAccount(acct: self.acct)
                acct.storage.save(<-ownedAccount, to: HybridCustody.OwnedAccountStoragePath)
            }

            let owned = acct.storage.borrow<auth(HybridCustody.Owner) &HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)
                ?? panic("owned account not found")

            let thumbnail = MetadataViews.HTTPFile(url: "https://avatars.flowty.io/6.x/thumbs/png?seed=".concat(self.acct.address.toString()))
            let display = MetadataViews.Display(name: "Creator Hub", description: "Created by the Flowty Creator Hub", thumbnail: thumbnail)
            owned.setDisplay(display)

            if !acct.capabilities.get<&{HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountPublicPath).check() {
                acct.capabilities.unpublish(HybridCustody.OwnedAccountPublicPath)
                acct.capabilities.storage.issue<&{HybridCustody.BorrowableAccount, HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath)
                acct.capabilities.publish(
                    acct.capabilities.storage.issue<&{HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath),
                    at: HybridCustody.OwnedAccountPublicPath
                )
            }

            // make sure that only the owner of this resource is a valid parent
            let parents = owned.getParentAddresses()
            let owner = self.owner!.address
            var foundOwner = false
            for parent in parents {
                if parent == owner {
                    foundOwner = true
                    continue
                }

                // found a parent that should not be present
                owned.removeParent(parent: parent)
            }

            if foundOwner {
                return
            }

            // Flow maintains a set of pre-configured filter and factory resources that we will use:
            // https://github.com/onflow/hybrid-custody?tab=readme-ov-file#hosted-capabilityfactory--capabilityfilter-implementations
            var factoryAddress = ContractManager.account.address
            var filterAddress = ContractManager.account.address
            if let network = AddressUtils.getNetworkFromAddress(ContractManager.account.address) {
                switch network {
                    case "TESTNET":
                        factoryAddress = Address(0x1b7fa5972fcb8af5)
                        filterAddress = Address(0xe2664be06bb0fe62)
                        break
                    case "MAINNET":
                        factoryAddress = Address(0x071d382668250606)
                        filterAddress = Address(0x78e93a79b05d0d7d)
                        break
                }
            }

            owned.publishToParent(
                parentAddress: owner,
                factory: getAccount(factoryAddress!).capabilities.get<&CapabilityFactory.Manager>(CapabilityFactory.PublicPath),
                filter: getAccount(filterAddress!).capabilities.get<&{CapabilityFilter.Filter}>(CapabilityFilter.PublicPath)
            )
        }

        // Configure a given fungible token vault so that it can be received by this contract account
        access(Manage) fun configureVault(vaultType: Type) {
            pre {
                vaultType.isSubtype(of: Type<@{FungibleToken.Vault}>()): "vault must be a fungible token"
            }

            let address = AddressUtils.parseAddress(vaultType)!
            let name = vaultType.identifier.split(separator: ".")[2]

            let ftContract = getAccount(address).contracts.borrow<&{FungibleToken}>(name: name)
                ?? panic("vault contract does not implement FungibleToken")
            let data = ftContract.resolveContractView(resourceType: vaultType, viewType: Type<FungibleTokenMetadataViews.FTVaultData>())! as! FungibleTokenMetadataViews.FTVaultData

            let acct = self.acct.borrow()!
            if acct.storage.type(at: data.storagePath) == nil {
                acct.storage.save(<- ftContract.createEmptyVault(vaultType: vaultType), to: data.storagePath)
            }

            if !acct.capabilities.get<&{FungibleToken.Receiver}>(data.receiverPath).check() {
                acct.capabilities.unpublish(data.receiverPath)
                acct.capabilities.publish(
                    acct.capabilities.storage.issue<&{FungibleToken.Receiver}>(data.storagePath),
                    at: data.receiverPath
                )
            }

            if !acct.capabilities.get<&{FungibleToken.Receiver}>(data.metadataPath).check() {
                acct.capabilities.unpublish(data.metadataPath)
                acct.capabilities.publish(
                    acct.capabilities.storage.issue<&{FungibleToken.Vault}>(data.storagePath),
                    at: data.metadataPath
                )
            }

            // is there a valid provider capability for this vault type?
            var foundProvider = false
            for controller in acct.capabilities.storage.getControllers(forPath: data.storagePath) {
                if controller.borrowType.isSubtype(of: Type<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>()) {
                    foundProvider = true
                    break
                }
            }

            if foundProvider {
                return
            }

            // we did not find a provider, issue one so that its parent account is able to access it.
            acct.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(data.storagePath)
        }
    }

    access(all) fun createManager(tokens: @FlowToken.Vault, defaultRouterAddress: Address): @Manager {
        return <- create Manager(tokens: <- tokens, defaultRouterAddress: defaultRouterAddress)
    }

    init() {
        let identifier = "ContractManager_".concat(self.account.address.toString())
        self.StoragePath = StoragePath(identifier: identifier)!
        self.PublicPath = PublicPath(identifier: identifier)!

        let ownerIdentifier = "ContractManager_Owner_".concat(self.account.address.toString())
        self.OwnerStoragePath = StoragePath(identifier: ownerIdentifier)!
        self.OwnerPublicPath = PublicPath(identifier: ownerIdentifier)!
    }
}
```