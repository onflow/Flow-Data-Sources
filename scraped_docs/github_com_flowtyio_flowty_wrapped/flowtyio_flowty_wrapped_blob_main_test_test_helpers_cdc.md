# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/test/test_helpers.cdc

```
import Test

/*
    Most of this was taken from:
    https://github.com/onflow/hybrid-custody/blob/main/test/test_helpers.cdc
*/

access(all) fun loadCode(_ fileName: String, _ baseDirectory: String): String {
    return Test.readFile("../".concat(baseDirectory).concat("/").concat(fileName))
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

access(all) fun txExecutor(
    _ txName: String,
    _ signers: [Test.TestAccount],
    _ arguments: [AnyStruct],
    _ expectedError: String?
): Bool {
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
        if let expectedErrorMessage = expectedError {
            Test.assertError(
                txResult,
                errorMessage: expectedErrorMessage
            )
            return true
        }
    } else {
        if let expectedErrorMessage = expectedError {
            panic("Expecting error - ".concat(expectedErrorMessage).concat(". While no error triggered"))
        }
    }

    Test.expect(txResult, Test.beSucceeded())
    return true
}
```