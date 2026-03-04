# Source: https://github.com/emerald-dao/emerald-id/blob/main/flow/cadence/transactions/change_field.cdc

```
import EmeraldID from "../EmeraldID.cdc"

transaction(field: String, value: String, acctAddress: Address, message: String, keyIds: [Int], signatures: [String], signatureBlock: UInt64) {

  let Info: &EmeraldID.Info

  prepare(signer: AuthAccount) {
    self.Info = signer.borrow<&EmeraldID.Info>(from: EmeraldID.InfoStoragePath)
                  ?? panic("The signer does not have an EmeraldID.")
  }

  execute {
    self.Info.changeField(
      field: field, 
      value: value, 
      acctAddress: acctAddress, 
      message: message, 
      keyIds: keyIds, 
      signatures: signatures, 
      signatureBlock: signatureBlock
    )
  }
}
```