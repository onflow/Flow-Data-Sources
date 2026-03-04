# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/scripts/getId.cdc

```
// Import the CryptoKnight contract
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// This public function returns a list of all NFT IDs owned by the given address
access(all) fun main(addr: Address): [UInt64] {
    // Get the account object for the provided address
    let account = getAccount(addr)

    // Borrow a reference to the user's CryptoKnight NFT collection using the public capability
    let cap = account.capabilities.borrow<&CryptoKnight.Collection>(CryptoKnight.CollectionPublicPath)!
    
    // Return an array of all the NFT IDs owned by this collection
    return cap.getIDs()
}

```