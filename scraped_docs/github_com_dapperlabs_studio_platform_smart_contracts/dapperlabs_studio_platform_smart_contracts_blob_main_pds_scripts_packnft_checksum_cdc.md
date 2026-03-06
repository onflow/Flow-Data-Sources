# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/scripts/packNFT/checksum.cdc

```
import Crypto
access(all) fun main(toHash: String): String {
    let hashB2 = HashAlgorithm.SHA2_256.hash(toHash.utf8)
    log(String.encodeHex(hashB2))
    return String.encodeHex(hashB2)
}

```