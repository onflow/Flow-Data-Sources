# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/contracts/env/OracleConfig.cdc

```
/**

# This contract stores some commonly used paths & library functions for PriceOracle

# Author Increment Labs

*/

access(all) contract OracleConfig {
    // Admin resource stored in every PriceOracle contract
    access(all) let OracleAdminPath: StoragePath
    // Reader public interface exposed in every PriceOracle contract
    access(all) let OraclePublicInterface_ReaderPath: PublicPath
    // Feeder public interface exposed in every PriceOracle contract
    access(all) let OraclePublicInterface_FeederPath: PublicPath
    // Recommended storage path of reader's certificate
    access(all) let ReaderCertificateStoragePath: StoragePath

    init() {
        self.OracleAdminPath = /storage/increment_oracle_admin
        self.OraclePublicInterface_ReaderPath = /public/increment_oracle_reader_public
        self.OraclePublicInterface_FeederPath = /public/increment_oracle_feeder_public
        self.ReaderCertificateStoragePath = /storage/increment_oracle_reader_certificate
    }
}
```