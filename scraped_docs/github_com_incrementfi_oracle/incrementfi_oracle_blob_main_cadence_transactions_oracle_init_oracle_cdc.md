# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/oracle/init_oracle.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(
    priceIdentifier: String,
    minFeederNumber: Int,
    feederStoragePath: StoragePath,
    feederPublicPath: PublicPath,
    readerStoragePath: StoragePath
) {
    prepare(oracleAccount: auth(BorrowValue) &Account) {
        let oracleAdminRef = oracleAccount.storage.borrow<&{OracleInterface.Admin}>(from: OracleConfig.OracleAdminPath) ?? panic("Lost oracle admin resource.")
        oracleAdminRef.configOracle(
            priceIdentifier: priceIdentifier,
            minFeederNumber: minFeederNumber,
            feederStoragePath: feederStoragePath,
            feederPublicPath: feederPublicPath,
            readerStoragePath: readerStoragePath
        )
    }
}
```