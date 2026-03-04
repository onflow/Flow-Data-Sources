# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/is-token-registered.cdc

```
import "TokenList"

access(all)
fun main(
    ftAddress: Address,
    ftContractName: String,
): Bool {
    return TokenList.isFungibleTokenRegistered(ftAddress, ftContractName)
}

```