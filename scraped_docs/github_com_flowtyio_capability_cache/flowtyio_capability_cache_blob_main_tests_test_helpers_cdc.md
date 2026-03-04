# Source: https://github.com/Flowtyio/capability-cache/blob/main/tests/test_helpers.cdc

```
import Test

access(all) let cacheAccount = Test.getAccount(0x0000000000000007)

access(all) fun scriptExecutor(_ scriptName: String, _ arguments: [AnyStruct]): AnyStruct? {
    let scriptCode = loadCode(scriptName, "scripts")
    let scriptResult = Test.executeScript(scriptCode, arguments)

    if scriptResult.error != nil {
        panic(scriptResult.error!.message)
    }

    return scriptResult.returnValue
}

access(all) fun txExecutor(_ txName: String, _ signers: [Test.TestAccount], _ arguments: [AnyStruct]): Test.TransactionResult {
    let txCode = loadCode(txName, "transactions")

    let authorizers: [Address] = []
    for signer in signers {
        authorizers.append(signer.address)
    }

    let tx = Test.Transaction(
        code: txCode,
        authorizers: authorizers,
        signers: signers,
        arguments: arguments,
    )

    let txResult = Test.executeTransaction(tx)
    if let err = txResult.error {
        panic(err.message)
    }

    return txResult
}

access(all) fun loadCode(_ fileName: String, _ baseDirectory: String): String {
    return Test.readFile("../".concat(baseDirectory).concat("/").concat(fileName))
}

access(all) fun deployAll() {
    deploy("CapabilityCache", "../contracts/CapabilityCache.cdc", [])
}

access(all) fun deploy(_ name: String, _ path: String, _ arguments: [AnyStruct]) {
    let err = Test.deployContract(name: name, path: path, arguments: arguments)
    Test.expect(err, Test.beNil()) 
}

access(all) fun getNewAccount(): Test.TestAccount {
    let acct = Test.createAccount()
    return acct
}

access(all) fun mintFlow(_ receiver: Test.TestAccount, _ amount: UFix64) {
    let code = loadCode("flow/mint_flow.cdc", "transactions")
    let tx = Test.Transaction(
        code: code,
        authorizers: [Test.serviceAccount().address],
        signers: [],
        arguments: [receiver.address, amount]
    )
    let txResult = Test.executeTransaction(tx)
    if txResult.error != nil {
        panic(txResult.error!.message)
    }
}
```