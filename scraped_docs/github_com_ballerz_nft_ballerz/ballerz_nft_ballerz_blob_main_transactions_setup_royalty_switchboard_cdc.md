# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/transactions/setup_royalty_switchboard.cdc

```
import "FungibleToken"
import "FungibleTokenMetadataViews"
import "FungibleTokenSwitchboard"
import "DapperUtilityCoin"

// gives the signer one receiver that accepts several tokens, at
// /public/GenericFTReceiver, so a royalty can be paid in whatever currency a
// sale used. each identifier in `vaultIdentifiers` gets a vault if the account
// has none (FLOW already exists on every account) and is added to the
// switchboard. the existing Dapper Utility Coin receiver is added as well, so
// DUC keeps arriving the way it does today
//
// idempotent: safe to run more than once, and again later with more tokens

transaction(vaultIdentifiers: [String]) {
    prepare(signer: auth(Storage, Capabilities) &Account) {
        if signer.storage.borrow<&FungibleTokenSwitchboard.Switchboard>(from: FungibleTokenSwitchboard.StoragePath) == nil {
            signer.storage.save(<-FungibleTokenSwitchboard.createSwitchboard(), to: FungibleTokenSwitchboard.StoragePath)
        }
        if !signer.capabilities.get<&{FungibleToken.Receiver}>(FungibleTokenSwitchboard.ReceiverPublicPath).check() {
            signer.capabilities.unpublish(FungibleTokenSwitchboard.ReceiverPublicPath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(FungibleTokenSwitchboard.StoragePath),
                at: FungibleTokenSwitchboard.ReceiverPublicPath
            )
        }
        if !signer.capabilities.get<&{FungibleTokenSwitchboard.SwitchboardPublic}>(FungibleTokenSwitchboard.PublicPath).check() {
            signer.capabilities.unpublish(FungibleTokenSwitchboard.PublicPath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleTokenSwitchboard.SwitchboardPublic}>(FungibleTokenSwitchboard.StoragePath),
                at: FungibleTokenSwitchboard.PublicPath
            )
        }
        let switchboard = signer.storage.borrow<auth(FungibleTokenSwitchboard.Owner) &FungibleTokenSwitchboard.Switchboard>(
                from: FungibleTokenSwitchboard.StoragePath
            ) ?? panic("Could not borrow the switchboard")

        for identifier in vaultIdentifiers {
            let vaultType = CompositeType(identifier) ?? panic("Unknown vault type ".concat(identifier))
            let tokenContract = getAccount(vaultType.address!).contracts.borrow<&{FungibleToken}>(name: vaultType.contractName!)
                ?? panic("Could not borrow the token contract for ".concat(identifier))
            let vaultData = tokenContract.resolveContractView(
                    resourceType: nil,
                    viewType: Type<FungibleTokenMetadataViews.FTVaultData>()
                ) as! FungibleTokenMetadataViews.FTVaultData?
                ?? panic("Token does not expose FTVaultData: ".concat(identifier))

            if signer.storage.borrow<&{FungibleToken.Vault}>(from: vaultData.storagePath) == nil {
                signer.storage.save(<-vaultData.createEmptyVault(), to: vaultData.storagePath)
            }
            if !signer.capabilities.get<&{FungibleToken.Receiver}>(vaultData.receiverPath).check() {
                signer.capabilities.unpublish(vaultData.receiverPath)
                signer.capabilities.publish(
                    signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultData.storagePath),
                    at: vaultData.receiverPath
                )
            }
            if !signer.capabilities.get<&{FungibleToken.Balance}>(vaultData.metadataPath).check() {
                signer.capabilities.unpublish(vaultData.metadataPath)
                signer.capabilities.publish(
                    signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultData.storagePath),
                    at: vaultData.metadataPath
                )
            }
            if !switchboard.isSupportedVaultType(type: vaultType) {
                switchboard.addNewVault(capability: signer.capabilities.get<&{FungibleToken.Receiver}>(vaultData.receiverPath))
            }
        }

        // the DUC receiver is a forwarder to Dapper's merchant account, so its
        // own type is not DUC and it has to be registered under the DUC type
        let ducReceiver = signer.capabilities.get<&{FungibleToken.Receiver}>(/public/dapperUtilityCoinReceiver)
        if ducReceiver.check() {
            switchboard.addNewVaultWrapper(capability: ducReceiver, type: Type<@DapperUtilityCoin.Vault>())
        }
    }
}

```