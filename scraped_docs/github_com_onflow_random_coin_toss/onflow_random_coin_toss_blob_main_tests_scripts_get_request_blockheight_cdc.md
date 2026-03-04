# Source: https://github.com/onflow/random-coin-toss/blob/main/tests/scripts/get_request_blockheight.cdc

```
import "RandomConsumer"

access(all)
fun main(address: Address, storagePath: StoragePath): UInt64 {
    return getAuthAccount<auth(BorrowValue) &Account>(address).storage
        .borrow<&RandomConsumer.Request>(
            from: storagePath
        )?.block
        ?? panic("No Request found")
}

```