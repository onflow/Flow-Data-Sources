# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/transactions/setup_account.cdc

```
// Import your main contract where the Collection and NFT types are defined
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// Transaction to create and store an empty NFT Collection in the user's account
transaction() {

  prepare(signer: auth(Storage, Capabilities) &Account) {

    // Check if the user already has a Collection stored at the expected path
    if signer.storage.borrow<&CryptoKnight.NFT>(from: CryptoKnight.CollectionStoragePath) != nil {
      // If the collection already exists, do nothing and exit early
      return 
    }

    // Save a new, empty NFT Collection into the account's storage
    signer.storage.save(
      <- CryptoKnight.createEmptyCollection(nftType: Type<@CryptoKnight.NFT>()),
      to: CryptoKnight.CollectionStoragePath
    )

    // Create a capability for the Collection so it can be accessed externally
    let collectionCap = signer.capabilities.storage.issue<&CryptoKnight.Collection>(
      CryptoKnight.CollectionStoragePath
    )

    // Publish the capability at a public path so others can borrow it
    signer.capabilities.publish(collectionCap, at: CryptoKnight.CollectionPublicPath)
  }
}

```