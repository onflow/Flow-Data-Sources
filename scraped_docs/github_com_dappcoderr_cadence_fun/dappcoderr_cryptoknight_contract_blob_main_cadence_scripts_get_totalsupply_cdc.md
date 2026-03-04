# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/scripts/get_totalSupply.cdc

```
// Import the CryptoKnight contract
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// This public function returns the total number of CryptoKnight NFTs that have been minted so far
access(all) fun main(): UInt64 {
    // Return the value of the totalSupply variable from the CryptoKnight contract
    return CryptoKnight.totalSupply
}

```