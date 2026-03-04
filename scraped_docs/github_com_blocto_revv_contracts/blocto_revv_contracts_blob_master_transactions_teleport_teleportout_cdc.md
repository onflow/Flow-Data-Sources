# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/teleportOut.cdc

```
import "FungibleToken"
import "REVV"
import "TeleportCustody"

transaction(teleportAdminAddress: Address, amount: UFix64, target: String) {
  prepare(signer: auth(BorrowValue) &Account) {
    let teleportUserRef = getAccount(teleportAdminAddress).capabilities.borrow<&{TeleportCustody.TeleportUser}>(TeleportCustody.TeleportUserPublicPath)
        ?? panic("Could not borrow a reference to TeleportUser")

    let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &REVV.Vault>(from: REVV.RevvVaultStoragePath)
        ?? panic("Could not borrow a reference to the vault resource")

    let vault <- vaultRef.withdraw(amount: amount) as! @REVV.Vault
    
    teleportUserRef.teleportOut(from: <- vault, to: target.decodeHex())
  }
}

```