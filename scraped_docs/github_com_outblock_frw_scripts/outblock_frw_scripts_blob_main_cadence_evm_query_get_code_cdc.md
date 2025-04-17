# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/query/get_code.cdc

```
import EVM from 0xEVM

access(all) fun main(hexEncodedAddress: String): String {
  let addressBytes = hexEncodedAddress.decodeHex().toConstantSized<[UInt8; 20]>()!
  let address = EVM.EVMAddress(bytes: addressBytes)

  return String.encodeHex(address.code())
}

```