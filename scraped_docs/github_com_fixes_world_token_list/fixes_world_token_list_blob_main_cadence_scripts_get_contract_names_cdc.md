# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-contract-names.cdc

```

access(all)
fun main(
    addr: Address
): [String] {
    let names = getAccount(addr).contracts.names
    let ret: [String] = []
    for name in names {
        log(name)
        ret.append(name)
    }
    return ret
}

```