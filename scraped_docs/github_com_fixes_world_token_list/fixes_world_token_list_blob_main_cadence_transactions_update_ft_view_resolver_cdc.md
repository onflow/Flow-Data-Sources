# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/update-ft-view-resolver.cdc

```
import "TokenList"

transaction(
    ftAddress: Address,
    ftContractName: String,
) {
    prepare(acct: &Account) {
        TokenList.updateFungibleTokenViewResolver(ftAddress, ftContractName)
    }
}

```