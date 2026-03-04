# Source: https://github.com/Flowtyio/fungible-token-router/blob/main/contracts/FungibleTokenRouter.cdc

```
/*
FungibleTokenRouter forwards tokens from one account to another using
FungibleToken metadata views. If a token is not configured to be received,
any deposits will panic like they would a deposit that it attempt to a
non-existent receiver

https://github.com/Flowtyio/fungible-token-router
*/

import "FungibleToken"
import "FungibleTokenMetadataViews"
import "FlowToken"

access(all) contract FungibleTokenRouter {
    access(all) let StoragePath: StoragePath
    access(all) let PublicPath: PublicPath

    access(all) entitlement Owner

    access(all) event RouterCreated(uuid: UInt64, defaultAddress: Address)
    access(all) event OverrideAdded(uuid: UInt64, owner: Address?, overrideAddress: Address, tokenType: String)
    access(all) event OverrideRemoved(uuid: UInt64, owner: Address?, overrideAddress: Address?, tokenType: String)
    access(all) event TokensRouted(tokenType: String, amount: UFix64, to: Address)

    access(all) resource Router: FungibleToken.Receiver {
        // a default address that is used for any token type that is not overridden
        access(all) var defaultAddress: Address

        // token type identifier -> destination address
        access(all) var addressOverrides: {String: Address}

        access(Owner) fun setDefaultAddress(_ addr: Address) {
            self.defaultAddress = addr
        }

        access(Owner) fun addOverride(type: Type, addr: Address) {
            emit OverrideAdded(uuid: self.uuid, owner: self.owner?.address, overrideAddress: addr, tokenType: type.identifier)
            self.addressOverrides[type.identifier] = addr
        }

        access(Owner) fun removeOverride(type: Type): Address? {
            let removedAddr = self.addressOverrides.remove(key: type.identifier)
            emit OverrideRemoved(uuid: self.uuid, owner: self.owner?.address, overrideAddress: removedAddr, tokenType: type.identifier)
            return removedAddr
        }

        access(all) fun deposit(from: @{FungibleToken.Vault}) {
            let tokenType = from.getType()
            let destination = self.addressOverrides[tokenType.identifier] ?? self.defaultAddress

            var vaultDataOpt: FungibleTokenMetadataViews.FTVaultData? = nil

            if tokenType == Type<@FlowToken.Vault>() {
                vaultDataOpt = FungibleTokenMetadataViews.FTVaultData(
                    storagePath: /storage/flowTokenVault,
                    receiverPath: /public/flowTokenReceiver,
                    metadataPath: /public/flowTokenReceiver,
                    receiverLinkedType: Type<&FlowToken.Vault>(),
                    metadataLinkedType: Type<&FlowToken.Vault>(),
                    createEmptyVaultFunction: fun(): @{FungibleToken.Vault} {
                        return <- FlowToken.createEmptyVault(vaultType: tokenType)   
                    }
                )
            } else if let md = from.resolveView(Type<FungibleTokenMetadataViews.FTVaultData>()) {
                vaultDataOpt = md as! FungibleTokenMetadataViews.FTVaultData
            }

            let vaultData = vaultDataOpt ?? panic("vault data could not be retrieved for type ".concat(tokenType.identifier))
            let receiver = getAccount(destination).capabilities.get<&{FungibleToken.Receiver}>(vaultData.receiverPath)
            assert(receiver.check(), message: "no receiver found at path: ".concat(vaultData.receiverPath.toString()))

            emit TokensRouted(tokenType: tokenType.identifier, amount: from.balance, to: destination)
            receiver.borrow()!.deposit(from: <-from)
        }

        access(all) view fun getSupportedVaultTypes(): {Type: Bool} {
            // theoretically any token is supported, it depends on the defaultAddress
            return {}
        }

        access(all) view fun isSupportedVaultType(type: Type): Bool {
            // theoretically any token is supported, it depends on the defaultAddress
            return true
        }

        init(defaultAddress: Address) {
            self.defaultAddress = defaultAddress
            self.addressOverrides = {}

            emit RouterCreated(uuid: self.uuid, defaultAddress: defaultAddress)
        }
    }

    access(all) fun createRouter(defaultAddress: Address): @Router {
        return <- create Router(defaultAddress: defaultAddress)
    }

    init() {
        let identifier = "FungibleTokenRouter_".concat(self.account.address.toString())
        self.StoragePath = StoragePath(identifier: identifier)!
        self.PublicPath = PublicPath(identifier: identifier)!
    }
}
```