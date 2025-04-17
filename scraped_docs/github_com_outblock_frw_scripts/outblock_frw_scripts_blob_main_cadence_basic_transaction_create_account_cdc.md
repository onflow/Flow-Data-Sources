# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/transaction/create_account.cdc

```
import Crypto
import FlowToken from 0x1654653399040a61
import FungibleToken from 0xf233dcee88fe0abe

transaction(publicKeys: [Crypto.KeyListEntry], contracts: {String: String}, fundAmount: UFix64) {
  let tokenReceiver: &{FungibleToken.Receiver}
  let sentVault: @FungibleToken.Vault

  prepare(signer: auth(BorrowValue | Storage) &Account) {
    let account = Account(payer: signer)
    for key in publicKeys {
      account.keys.add(publicKey: key.publicKey, hashAlgorithm: key.hashAlgorithm, weight: key.weight)
    }
    for contract in contracts.keys {
      account.contracts.add(name: contract, code: contracts[contract]!.decodeHex())
    }
    self.tokenReceiver = account.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver) ?? panic("Unable to borrow receiver reference")
    let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault) ?? panic("Could not borrow reference to the owner''s Vault!")
    self.sentVault <- vaultRef.withdraw(amount: fundAmount)
  }
  execute {
    self.tokenReceiver.deposit(from: <-self.sentVault)
  }
}
```