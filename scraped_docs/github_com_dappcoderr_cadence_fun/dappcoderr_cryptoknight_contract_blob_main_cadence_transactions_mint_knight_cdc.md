# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/transactions/mint_knight.cdc

```
// Import the CryptoKnight contract
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// Transaction to mint a new Knight NFT with a given name and type (power level)
transaction(name: String, power: UInt8) {

    // A reference to the signer's Collection where the new Knight will be deposited
    let collectionRef: &CryptoKnight.Collection

    prepare(signer: auth(Storage, Capabilities) &Account) {
        // Pre-condition: only allow power values of 0, 1, 2, or 3
        pre {
            power <= 3: "Wrong inputValue" // Reject if power exceeds allowed range
        }

        // Borrow a reference to the signer's Collection stored in account storage
        self.collectionRef = signer.storage
            .borrow<&CryptoKnight.Collection>(from: CryptoKnight.CollectionStoragePath)
            ?? panic("Object not found") // Panic if the Collection is not found in storage
    }

    execute {
        // Mint a new Knight NFT using the provided name and power type
        let nft <- CryptoKnight.mintKnight(name: name, type: power)

        // Deposit the newly minted NFT into the user's Collection
        self.collectionRef.deposit(token: <- nft)
    }
}



```