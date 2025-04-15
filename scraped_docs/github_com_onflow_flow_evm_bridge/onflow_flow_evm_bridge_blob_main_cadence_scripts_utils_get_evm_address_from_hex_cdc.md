# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/get_evm_address_from_hex.cdc

```
import "EVM"

access(all)
fun main(hex: String): EVM.EVMAddress? {
    return EVM.addressFromString(hex)
}
```