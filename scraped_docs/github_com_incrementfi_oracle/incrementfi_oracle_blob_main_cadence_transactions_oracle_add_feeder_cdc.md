# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/oracle/add_feeder.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(feederAddr: Address) {
    prepare(oracleAccount: auth(BorrowValue) &Account) {
        let oracleAdminRef = oracleAccount.storage.borrow<&{OracleInterface.Admin}>(from: OracleConfig.OracleAdminPath) ?? panic("Lost medianizer admin resource.")
        oracleAdminRef.addFeederWhiteList(feederAddr: feederAddr)
    }
}
```