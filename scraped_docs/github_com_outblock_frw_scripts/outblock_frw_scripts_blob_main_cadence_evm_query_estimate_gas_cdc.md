# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/query/estimate_gas.cdc

```
import EVM from 0xEVM

access(all)
fun main(hexEncodedTx: String, address: Address): [UInt64; 2] {
  let account = getAuthAccount<auth(Storage) &Account>(address)

  let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(
    from: /storage/evm
  ) ?? panic("Could not borrow reference to the COA!")
  let txResult = EVM.run(tx: hexEncodedTx.decodeHex(), coinbase: coa.address())

  assert(
    txResult.status == EVM.Status.failed || txResult.status == EVM.Status.successful,
    message: "evm_error=".concat(txResult.errorMessage).concat("\n")
  )

  return [txResult.errorCode, txResult.gasUsed]
}

```