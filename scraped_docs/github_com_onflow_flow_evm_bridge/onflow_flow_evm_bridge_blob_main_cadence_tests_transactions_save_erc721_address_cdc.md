# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/transactions/save_erc721_address.cdc

```
import "EVM"

transaction(erc721AddressHex: String) {
    prepare(signer: auth(SaveValue) &Account) {
        let erc721Address = EVM.addressFromString(erc721AddressHex)
        signer.storage.save(erc721Address, to: /storage/erc721ContractAddress)
    }
}
```