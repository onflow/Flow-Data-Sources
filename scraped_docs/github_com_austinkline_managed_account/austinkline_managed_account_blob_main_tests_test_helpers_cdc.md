# Source: https://github.com/austinkline/managed-account/blob/main/tests/test_helpers.cdc

```
import Test

access(all)let Account0x1 = Address(0x0000000000000001)
access(all)let Account0x2 = Address(0x0000000000000002)
access(all)let Account0x3 = Address(0x0000000000000003)
access(all)let Account0x4 = Address(0x0000000000000004)
access(all)let Account0x5 = Address(0x0000000000000005)
access(all)let Account0x6 = Address(0x0000000000000006)
access(all)let Account0x7 = Address(0x0000000000000007)
access(all)let Account0x8 = Address(0x0000000000000008)
access(all)let Account0x9 = Address(0x0000000000000009)
access(all)let Account0xa = Address(0x000000000000000a)
access(all)let Account0xb = Address(0x000000000000000b)
access(all)let Account0xc = Address(0x000000000000000c)
access(all)let Account0xd = Address(0x000000000000000d)
access(all)let Account0xe = Address(0x000000000000000e)

access(all) fun deployAll() {
    deploy("ManagedAccount", "../contracts/ManagedAccount.cdc", [])
    deploy("ContractUpdateExecutable", "../contracts/ContractUpdateExecutable.cdc", [])
}

access(all) fun deploy(_ name: String, _ path: String, _ arguments: [AnyStruct]) {
    let err = Test.deployContract(name: name, path: path, arguments: arguments)
    Test.expect(err, Test.beNil())
}

access(all) fun scriptExecutor(_ scriptName: String, _ arguments: [AnyStruct]): AnyStruct? {
    let scriptCode = loadCode(scriptName, "scripts")
    let scriptResult = Test.executeScript(scriptCode, arguments)

    if let failureError = scriptResult.error {
        panic(
            "Failed to execute the script because -:  ".concat(failureError.message)
        )
    }

    return scriptResult.returnValue
}

access(all) fun loadCode(_ fileName: String, _ baseDirectory: String): String {
    return Test.readFile("../".concat(baseDirectory).concat("/").concat(fileName))
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
```