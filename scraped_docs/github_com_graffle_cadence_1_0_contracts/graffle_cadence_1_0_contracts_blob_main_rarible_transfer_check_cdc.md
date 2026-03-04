# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/rarible/transfer-check.cdc

```
import NonFungibleToken from "NonFungibleToken"
import BBxBarbiePack from "BBxBarbiePack"

// check BBxBarbiePack collection is available on given address
//
access(all)
fun main(address: Address): Bool {
    return getAccount(address).capabilities.get<&{BBxBarbiePack.PackCollectionPublic}>(BBxBarbiePack.CollectionPublicPath).check()
}

```