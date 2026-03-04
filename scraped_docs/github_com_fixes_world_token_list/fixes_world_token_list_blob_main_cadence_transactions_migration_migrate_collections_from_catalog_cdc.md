# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/migration/migrate-collections-from-catalog.cdc

```
import "NFTList"
import "NFTCatalog"

transaction() {

    prepare(acct: &Account) {
        let skipKeys = [
            "0x52acb3b399df11fc.SeedsOfHappinessGenesis"
        ]
        NFTCatalog.forEachCatalogKey(fun (key: String): Bool {
            if let metadata = NFTCatalog.getCatalogEntry(collectionIdentifier: key) {
                if !metadata.nftType.isRecovered {
                    let idKey = metadata.contractAddress.toString().concat(".").concat(metadata.contractName)
                    if skipKeys.contains(idKey) {
                        return true
                    }
                    NFTList.ensureNFTCollectionRegistered(metadata.contractAddress, metadata.contractName)
                }
            }
            return true
        })
    }
}


```