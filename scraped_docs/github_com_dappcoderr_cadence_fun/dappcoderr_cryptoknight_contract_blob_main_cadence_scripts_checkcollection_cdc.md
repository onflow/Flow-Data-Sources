# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/scripts/checkCollection.cdc

```
// Import the CryptoKnight contract
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// This public function checks whether a user has linked the CryptoKnight collection capability
access(all) fun main(addr: Address): Bool {
    // Retrieve the account object for the given address
    let account = getAccount(addr)

    // Try to get a reference to the capability for the user's CryptoKnight collection
    let capRef = account.capabilities.get<&CryptoKnight.Collection>(CryptoKnight.CollectionPublicPath)

    // Return true if the capability exists and is properly linked, false otherwise
    return capRef.check()
}

```