# Source: https://github.com/onflow/bridged-usdc/blob/main/tests/test_helpers.cdc

```
import Test

access(all) fun deployWithArgs(_ contractName: String, _ path: String, args: [AnyStruct]) {
    let err = Test.deployContract(
        name: contractName,
        path: path,
        arguments: args,
    )

    Test.expect(err, Test.beNil())
}

/* --- Executors --- */

access(all)
fun _executeScript(_ path: String, _ args: [AnyStruct]): Test.ScriptResult {
    return Test.executeScript(Test.readFile(path), args)
}

access(all)
fun _executeTransaction(_ path: String, _ args: [AnyStruct], _ signer: Test.TestAccount): Test.TransactionResult {
    let txn = Test.Transaction(
        code: Test.readFile(path),
        authorizers: [signer.address],
        signers: [signer],
        arguments: args
    )
    return Test.executeTransaction(txn)
}

/* --- Error Logging --- */

access(all)
fun getErrorMessage(_ res: {Test.Result}): String {
    if res.error != nil {
        return res.error?.message ?? "[ERROR] Unknown error occurred"
    }
    return ""
}
```