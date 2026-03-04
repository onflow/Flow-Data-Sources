# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/migration/get-invalid-fts.cdc

```
import "TokenList"

access(all)
fun main(): [String] {
    let invalidFTs: [String] = []
    let registry = TokenList.borrowRegistry()
    let tokenTypes = registry.getAllFTEntries()
    for tokenType in tokenTypes {
        if tokenType.isRecovered {
            invalidFTs.append(tokenType.identifier)
        }
    }
    return invalidFTs
}

```