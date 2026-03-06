# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/packNFT/packNFT_hash.cdc

```
import PackNFT from "PackNFT"
import IPackNFT from "IPackNFT"

access(all) fun main(id: UInt64): String {
    let p = PackNFT.borrowPackRepresentation(id: id)
    return p!.hash
}

```