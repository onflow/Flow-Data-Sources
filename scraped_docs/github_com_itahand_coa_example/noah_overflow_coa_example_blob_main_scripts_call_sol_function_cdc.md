# Source: https://github.com/Noah-Overflow/COA-Example/blob/main/scripts/call_sol_function.cdc

```
import "EVM"

access(all)
fun main(hexEncodedAddress: String, address: Address, pathId: UInt64): [AnyStruct] {
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
        data: EVM.encodeABIWithSignature(
                "awardItem(address,string)",
                [EVM.addressFromString("000000000000000000000002A16A68E971e4670B"), "{name: gamerz}"]
            ),
        gasLimit: 15000000, // todo make it configurable, max for now
    value: EVM.Balance(attoflow: 0)
    )

    return EVM.decodeABI(types: [Type<UInt256>()], data: callResult.data)
}

  
```