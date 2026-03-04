# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/reader/get_median_price.example.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(oracleAddr: Address) {
    let priceReaderRef: &{OracleInterface.PriceReader}

    prepare(readerAccount: auth(Storage) &Account) {
        /// Oracle public interface capability
        let oraclePublicInterface_ReaderRef = getAccount(oracleAddr).capabilities.borrow<&{OracleInterface.OraclePublicInterface_Reader}>(OracleConfig.OraclePublicInterface_ReaderPath)
            ?? panic("Lost oracle public capability at ".concat(oracleAddr.toString()))
        /// Recommended storage path for PriceReader resource
        let priceReaderSuggestedPath = oraclePublicInterface_ReaderRef.getPriceReaderStoragePath()
        
        /// Mint PriceReader if non-exist
        if (readerAccount.storage.borrow<&{OracleInterface.PriceReader}>(from: priceReaderSuggestedPath) == nil) {
            let priceReader <- oraclePublicInterface_ReaderRef.mintPriceReader()
            destroy <- readerAccount.storage.load<@AnyResource>(from: priceReaderSuggestedPath)
            readerAccount.storage.save(<- priceReader, to: priceReaderSuggestedPath)
        }
        self.priceReaderRef = readerAccount.storage.borrow<&{OracleInterface.PriceReader}>(from: priceReaderSuggestedPath)
            ?? panic("Lost local price reader resource.")
    }

    execute {
        /// Get median price
        let price = self.priceReaderRef.getMedianPrice()
    }
}
```