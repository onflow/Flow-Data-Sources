# Source: https://github.com/onflow/flow-ft/blob/master/transactions/privateForwarder/deploy_forwarder_contract.cdc

```
/// Deploys the TokenForwarding contract with the specified init parameters

transaction(contractName: String,
            code: [UInt8],
            senderStoragePath: StoragePath,
            storagePath: StoragePath,
            publicPath: PublicPath) {

  prepare(signer: auth(AddContract) &Account) {

    signer.contracts.add(name: contractName, code: code, senderStoragePath, storagePath, publicPath)

  }
}
 

```