# Source: https://github.com/onflow/random-coin-toss/blob/main/tests/scripts/request_can_fulfill.cdc

```
import "RandomConsumer"

access(all)
fun main(address: Address, storagePath: StoragePath): Bool {
    return getAuthAccount<auth(BorrowValue) &Account>(address).storage
        .borrow<&RandomConsumer.Request>(
            from: storagePath
        )?.canFullfill()
        ?? panic("No Request found")
}

```