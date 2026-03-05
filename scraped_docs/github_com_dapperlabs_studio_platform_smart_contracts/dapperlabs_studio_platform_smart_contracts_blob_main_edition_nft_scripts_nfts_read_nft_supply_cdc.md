# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/edition-nft/scripts/nfts/read_nft_supply.cdc

```
import EditionNFT from "EditionNFT"

// This scripts returns the number of EditionNFT currently in existence.

access(all) fun main(): UInt64 {    
    return EditionNFT.totalSupply
}


```