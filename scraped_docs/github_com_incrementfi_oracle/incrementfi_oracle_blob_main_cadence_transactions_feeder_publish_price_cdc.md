# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/feeder/publish_price.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(oracleAddr: Address, price: UFix64) {
    prepare(feederAccount: auth(Storage, Capabilities) &Account) {
        let oraclePublicInterface_FeederRef = getAccount(oracleAddr).capabilities.borrow<&{OracleInterface.OraclePublicInterface_Feeder}>(OracleConfig.OraclePublicInterface_FeederPath)
            ?? panic("Lost oracle public capability at ".concat(oracleAddr.toString()))
        // mint PriceFeeder if non-exist
        if (feederAccount.storage.borrow<&{OracleInterface.PriceFeeder}>(from: oraclePublicInterface_FeederRef.getPriceFeederStoragePath()) == nil) {
            let priceFeeder <- oraclePublicInterface_FeederRef.mintPriceFeeder()

            destroy <- feederAccount.storage.load<@AnyResource>(from: oraclePublicInterface_FeederRef.getPriceFeederStoragePath())
            feederAccount.storage.save(<- priceFeeder, to: oraclePublicInterface_FeederRef.getPriceFeederStoragePath())
            feederAccount.capabilities.publish(
                feederAccount.capabilities.storage.issue<&{OracleInterface.PriceFeeder}>(oraclePublicInterface_FeederRef.getPriceFeederStoragePath()),
                at: oraclePublicInterface_FeederRef.getPriceFeederPublicPath()
            )
        }
        let priceFeederRef = feederAccount.storage.borrow<auth(OracleInterface.FeederAuth) &{OracleInterface.PriceFeeder}>(from: oraclePublicInterface_FeederRef.getPriceFeederStoragePath()) ?? panic("Lost feeder resource.")
        priceFeederRef.publishPrice(price: price)
    }
}
```