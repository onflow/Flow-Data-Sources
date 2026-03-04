# Source: https://github.com/onflow/random-coin-toss/blob/main/tests/scripts/get_evm_balance.cdc

```
import "EVM"

access(all)
fun main(evmAddressHex: String): UFix64 {
    return EVM.addressFromString(evmAddressHex).balance().inFLOW()
}
```