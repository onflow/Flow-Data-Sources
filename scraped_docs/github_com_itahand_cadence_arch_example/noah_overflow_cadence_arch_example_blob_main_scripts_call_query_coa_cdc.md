# Source: https://github.com/Noah-Overflow/Cadence-Arch-example/blob/main/scripts/call_query_COA.cdc

```
import "EVM"

access(all)
fun main(hexEncodedData: String, hexEncodedAddress: String, address: Address, pathId: UInt64): String {
    let account = getAuthAccount<auth(Storage) &Account>(address)

    // COA should be at "EVM_${pathId}"
    // this setting is done to avoid collition, but is only a simple example
    let coaPath = StoragePath(identifier: address.toString().concat("EVM_").concat(pathId.toString()))!

    let coa = account.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(
        from: coaPath
    ) ?? panic("Could not borrow reference to the COA!")
    let addressBytes = hexEncodedAddress.decodeHex().toConstantSized<[UInt8; 20]>()!

    let callResult = coa.call(
        to: EVM.EVMAddress(bytes: addressBytes),
        data: hexEncodedData.decodeHex(),
        gasLimit: 15000000, // todo make it configurable, max for now
    value: EVM.Balance(attoflow: 0)
    )

    return String.encodeHex(callResult.data)
}

 
```