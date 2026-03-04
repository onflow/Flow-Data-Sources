# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/blackhole/register-any-blackhole.cdc

```
import "BlackHole"

transaction(
    addr: Address
) {
    prepare(acct: &Account) {
        // register the new account as a black hole receiver
        BlackHole.registerAsBlackHole(addr)
    }
}

```