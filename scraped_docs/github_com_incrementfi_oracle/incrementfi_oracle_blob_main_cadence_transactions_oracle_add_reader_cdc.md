# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/oracle/add_reader.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(readerAddr: Address) {
    prepare(oracleAccount: auth(BorrowValue) &Account) {
        let oracleAdminRef = oracleAccount.storage.borrow<&{OracleInterface.Admin}>(from: OracleConfig.OracleAdminPath) ?? panic("Lost medianizer admin resource.")
        oracleAdminRef.addReaderWhiteList(readerAddr: readerAddr)
    }
}
```