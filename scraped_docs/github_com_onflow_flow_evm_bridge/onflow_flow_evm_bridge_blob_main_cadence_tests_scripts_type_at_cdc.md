# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/scripts/type_at.cdc

```
access(all)
fun main(addr: Address, sp: StoragePath): Type? {
    return getAuthAccount<auth(BorrowValue) &Account>(addr).storage.type(at: sp)
}

```