# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/query/get_balance.cdc

```
import EVM from 0xEVM

access(all) fun main(hexEncodedAddress: String): UInt {
  let addressBytes = hexEncodedAddress.decodeHex().toConstantSized<[UInt8; 20]>()!
  let address = EVM.EVMAddress(bytes: addressBytes)

  return address.balance().inAttoFLOW()
}

```