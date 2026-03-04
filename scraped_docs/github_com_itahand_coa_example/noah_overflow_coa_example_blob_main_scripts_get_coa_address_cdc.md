# Source: https://github.com/Noah-Overflow/COA-Example/blob/main/scripts/get_COA_address.cdc

```
import "EVM"

access(all)
fun main(address: Address, pathId: Int): String {
    let account = getAuthAccount<auth(Storage) &Account>(address)
    // COA should be at "EVM_${pathId}"
    // this setting is done to avoid collition, but is only a simple example
    let coaPath = StoragePath(identifier: address.toString().concat("EVM_").concat(pathId.toString()))!

    let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(
        from: coaPath
    ) ?? panic("Could not borrow reference to the COA!")
    
    let coaAddr = coa.address() 

    let addrByte: [UInt8] = []

    for byte in coaAddr.bytes {
        addrByte.append(byte)
    }
    
    // return 000000000000000000000002ef9b0732eeaa65dc  (hexEncodedAddress)
    return String.encodeHex(addrByte)
}
```