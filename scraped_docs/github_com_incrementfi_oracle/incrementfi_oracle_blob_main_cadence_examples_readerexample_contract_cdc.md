# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/examples/readerExample.contract.cdc

```
import OracleInterface from "../contracts/OracleInterface.cdc"
import OracleConfig from "../contracts/OracleConfig.cdc"

/// Steps for being PriceReader
/// 1. Apply for joining reader whitelist for your contract address (contact@increment.fi)
/// 2. Mint the PriceReader resource and save it in your local storage
/// 3. Read price via PriceReader resource

access(all) contract OraclePriceUseContract {
    access(all) fun usecase() {
        /// testnet oracle address
        /// hard code for test
        var oracleAddr_flow: Address = 0xcbdb5a7b89c3c844
        var oracleAddr_fusd: Address = 0x3b220a3372190656
        var oracleAddr_blt: Address  = 0x2d766f00eb1d0c37

        let flowPrice = self.getPrice(oracleAddr: oracleAddr_flow)
        let fusdPrice = self.getPrice(oracleAddr: oracleAddr_fusd)
        let bltPrice  = self.getPrice(oracleAddr: oracleAddr_blt)
    }

    access(all) fun getPrice(oracleAddr: Address): UFix64 {
        /// Recommended storage path for PriceReader resource
        let priceReaderSuggestedPath = getAccount(oracleAddr).capabilities.borrow<&{OracleInterface.OraclePublicInterface_Reader}>(OracleConfig.OraclePublicInterface_ReaderPath)!.getPriceReaderStoragePath()
        ///
        let priceReaderRef  = self.account.storage.borrow<&{OracleInterface.PriceReader}>(from: priceReaderSuggestedPath)
        if priceReaderRef == nil {
            self.mintPriceReader(oracleAddr: oracleAddr)
        }
        ///
        let price = priceReaderRef!.getMedianPrice()

        return price
    }

    access(all) fun mintPriceReader(oracleAddr: Address) {
        /// Oracle contract's interface
        let oracleRef = getAccount(oracleAddr).capabilities.borrow<&{OracleInterface.OraclePublicInterface_Reader}>(OracleConfig.OraclePublicInterface_ReaderPath)
            ?? panic("Lost oracle public capability at ".concat(oracleAddr.toString()))
        /// Recommended storage path for PriceReader resource
        let priceReaderSuggestedPath = oracleRef.getPriceReaderStoragePath()

        /// check if already minted
        if (self.account.storage.borrow<&{OracleInterface.PriceReader}>(from: priceReaderSuggestedPath) == nil) {
            /// price reader resource
            let priceReader <- oracleRef.mintPriceReader()

            destroy <- self.account.storage.load<@AnyResource>(from: priceReaderSuggestedPath)
            self.account.storage.save(<- priceReader, to: priceReaderSuggestedPath)
        }
    }

    init() {}
}
```