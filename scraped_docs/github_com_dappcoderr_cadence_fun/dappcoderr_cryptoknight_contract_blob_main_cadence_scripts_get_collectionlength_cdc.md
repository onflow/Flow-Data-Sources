# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/scripts/get_collectionLength.cdc

```
// Import the CryptoKnight contract
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// This public function returns the total number of CryptoKnight NFTs owned by the given account
access(all) fun main(addr: Address): Int {
    // Retrieve the account object for the given address
    let account = getAccount(addr)

    // Borrow a reference to the user's CryptoKnight NFT collection using the public capability path
    let capRef = account.capabilities.borrow<&CryptoKnight.Collection>(CryptoKnight.CollectionPublicPath)!
    
    // Return the number of NFTs currently in the collection
    return capRef.getLength()
}

```