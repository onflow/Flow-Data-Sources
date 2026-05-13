# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/transactions/setup_duc_vault.cdc

```
import "FungibleToken"
import "DapperUtilityCoin"

// Sets up a DapperUtilityCoin vault and a public Receiver capability
// at /public/dapperUtilityCoinReceiver on the signer's account, so that
// the Gaia contract's MetadataViews.Royalties view can resolve a working
// FungibleToken.Receiver for this address.
//
// Idempotent: safe to run more than once.

transaction {
    prepare(signer: auth(Storage, Capabilities) &Account) {
        if signer.storage.borrow<&DapperUtilityCoin.Vault>(from: /storage/dapperUtilityCoinVault) == nil {
            signer.storage.save(
                <-DapperUtilityCoin.createEmptyVault(vaultType: Type<@DapperUtilityCoin.Vault>()),
                to: /storage/dapperUtilityCoinVault
            )
        }

        signer.capabilities.unpublish(/public/dapperUtilityCoinReceiver)
        let cap = signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(/storage/dapperUtilityCoinVault)
        signer.capabilities.publish(cap, at: /public/dapperUtilityCoinReceiver)
    }
}

```