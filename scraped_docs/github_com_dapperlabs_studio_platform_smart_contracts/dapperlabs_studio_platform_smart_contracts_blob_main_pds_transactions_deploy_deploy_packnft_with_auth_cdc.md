# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/transactions/deploy/deploy-packNFT-with-auth.cdc

```
// This transactions deploys a contract with init args
//
transaction(
    contractName: String,
    code: String,
    CollectionStoragePath: StoragePath,
    CollectionPublicPath: PublicPath,
    CollectionIPackNFTPublicPath: PublicPath,
    OperatorStoragePath: StoragePath,
    version: String,
) {
    prepare(owner: auth(AddContract, UpdateContract) &Account) {
        let existingContract = owner.contracts.get(name: contractName)

        if (existingContract == nil) {
            log("no contract")
            owner.contracts.add(
                name: contractName,
                code: code.decodeHex(),
                CollectionStoragePath: CollectionStoragePath,
                CollectionPublicPath: CollectionPublicPath,
                CollectionIPackNFTPublicPath: CollectionIPackNFTPublicPath,
                OperatorStoragePath: OperatorStoragePath,
                version: version,
            )
        } else {
            log("has contract")
            owner.contracts.update(name: contractName, code: code.decodeHex())
        }
    }
}

```