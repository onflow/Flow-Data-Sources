# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/scripts/borrow_knight.cdc

```
// Import the CryptoKnight contract from the relative path
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// Public script function that returns a reference to a specific CryptoKnight NFT
access(all) fun main(addr: Address, id: UInt64): &CryptoKnight.NFT {
    // Get the account object of the provided address
    let account = getAccount(addr)

    // Borrow a capability to the user's public CryptoKnight collection
    let cap = account.capabilities.borrow<&CryptoKnight.Collection>(CryptoKnight.CollectionPublicPath)!

    // Use the capability to borrow a reference to the specific NFT by ID
    let nft: &CryptoKnight.NFT = cap.borrowCryptoknight(id: id)!

    // Return a reference to the NFT
    return nft
}

// A struct used to package Knight NFT metadata into an easily consumable format
access(all) struct ResultKnight {
    access(all) let id: UInt64?          // Optional ID of the NFT
    access(all) let name: String?        // Optional name of the knight
    access(all) let type: UInt8?         // Optional offensive type (as raw value from enum)
    access(all) let date: UFix64?        // Optional date of birth (block timestamp)
    access(all) let xp: UInt64?          // Optional experience points
    access(all) let winCount: UInt64?    // Optional win count

    // Constructor to initialize all fields of the ResultKnight struct
    init(id: UInt64?, name: String?, type: UInt8?, date: UFix64?, xp: UInt64?, win: UInt64?) {
        self.id = id
        self.name = name
        self.type = type
        self.date = date
        self.xp = xp
        self.winCount = win
    }
}

```