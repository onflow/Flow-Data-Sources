# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/reader/mint_local_price_reader.example.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

transaction(oracleAddr: Address) {
    prepare(readerAccount: auth(Storage) &Account) {
        /// Oracle public interface capability
        let oraclePublicInterface_ReaderRef = getAccount(oracleAddr).capabilities.borrow<&{OracleInterface.OraclePublicInterface_Reader}>(OracleConfig.OraclePublicInterface_ReaderPath)
            ?? panic("Lost oracle public capability at ".concat(oracleAddr.toString()))
        /// Recommended storage path for PriceReader resource
        let priceReaderSuggestedPath = oraclePublicInterface_ReaderRef.getPriceReaderStoragePath()

        /// check if already minted
        if (readerAccount.storage.borrow<&{OracleInterface.PriceReader}>(from: priceReaderSuggestedPath) == nil) {
            let priceReader <- oraclePublicInterface_ReaderRef.mintPriceReader()

            destroy <- readerAccount.storage.load<@AnyResource>(from: priceReaderSuggestedPath)
            readerAccount.storage.save(<- priceReader, to: priceReaderSuggestedPath)
        }
    }
}
```