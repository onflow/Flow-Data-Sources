# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/get_supported_generated_transactions.cdc

```
import "TransactionGeneration"

access(all) fun main() : [String] {
    return TransactionGeneration.getSupportedTx()
}
```