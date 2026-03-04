# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/feeder/mint_local_price_feeder.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(oracleAddr: Address) {
    prepare(feederAccount: auth(Storage, Capabilities) &Account) {
        let oraclePublicInterface_FeederRef = getAccount(oracleAddr).capabilities.borrow<&{OracleInterface.OraclePublicInterface_Feeder}>(OracleConfig.OraclePublicInterface_FeederPath)
            ?? panic("Lost oracle public capability at ".concat(oracleAddr.toString()))

        let priceFeeder <- oraclePublicInterface_FeederRef.mintPriceFeeder()

        destroy <- feederAccount.storage.load<@AnyResource>(from: oraclePublicInterface_FeederRef.getPriceFeederStoragePath())
        feederAccount.storage.save(<- priceFeeder, to: oraclePublicInterface_FeederRef.getPriceFeederStoragePath())
        feederAccount.capabilities.publish(
            feederAccount.capabilities.storage.issue<&{OracleInterface.PriceFeeder}>(oraclePublicInterface_FeederRef.getPriceFeederStoragePath()),
            at: oraclePublicInterface_FeederRef.getPriceFeederPublicPath()
        )
    }
}
```