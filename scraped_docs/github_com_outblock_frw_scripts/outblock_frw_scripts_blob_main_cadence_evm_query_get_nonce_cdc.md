# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/query/get_nonce.cdc

```
import EVM from 0xEVM

access(all) fun main(hexEncodedAddress: String): UInt64 {
  let addressBytes = hexEncodedAddress.decodeHex().toConstantSized<[UInt8; 20]>()!
  let address = EVM.EVMAddress(bytes: addressBytes)

  return address.nonce()
}

```