# Source: https://github.com/blocto/revv-contracts/blob/master/test/CustodyREVVToken_test.cdc

```
import Test
import "TeleportCustody"

access(all) let admin = Test.getAccount(0x0000000000000007)
access(all) let teleportAdmin = Test.createAccount()
access(all) let receiver = Test.createAccount()
access(all) let feeReceiver = Test.createAccount()

access(all) fun setup() {
    let err = Test.deployContract(
        name: "REVV",
        path: "../contracts/flow/REVV.cdc",
        arguments: [],
    )
    Test.expect(err, Test.beNil())
    let err2 = Test.deployContract(
        name: "TeleportCustody",
        path: "../contracts/flow/TeleportCustody.cdc",
        arguments: [],
    )
    Test.expect(err2, Test.beNil())
}

access(all) fun testCreateTeleportAdmin() {
    let createTeleportAdminCode = Test.readFile("../transactions/teleport/setupTeleportAdmin.cdc")
    let createTeleportAdminTx = Test.Transaction(
        code: createTeleportAdminCode,
        authorizers: [admin.address, teleportAdmin.address],
        signers: [admin, teleportAdmin],
        arguments: [1000.0],
    )
    let createTeleportAdminTxResult = Test.executeTransaction(createTeleportAdminTx)
    Test.expect(createTeleportAdminTxResult, Test.beSucceeded())
}

access(all) fun testDepositAllowance() {
    let depositAllowanceCode = Test.readFile("../transactions/teleport/depositAllowance.cdc")
    let depositAllowanceTx = Test.Transaction(
        code: depositAllowanceCode,
        authorizers: [admin.address],
        signers: [admin],
        arguments: [teleportAdmin.address, 1000.0],
    )
    let depositAllowanceTxResult = Test.executeTransaction(depositAllowanceTx)
    Test.expect(depositAllowanceTxResult, Test.beSucceeded())
}

access(all) fun testAllowance() {
    let getAllowanceScript = Test.readFile("../scripts/getAllowance.cdc")
    let resultBefore = Test.executeScript(getAllowanceScript, [teleportAdmin.address])
    let allowanceBefore = resultBefore.returnValue! as! UFix64
    Test.assertEqual(2000.0, allowanceBefore)

    testDepositAllowance()
    let resultAfter = Test.executeScript(getAllowanceScript, [teleportAdmin.address])
    let allowanceAfter = resultAfter.returnValue! as! UFix64
    Test.assertEqual(3000.0, allowanceAfter)
}

access(all) fun testSetupREVVTokenVault() {
    // create vault for receiver
    let setupVaultCode = Test.readFile("../transactions/setupREVVVault.cdc")
    let setupVaultTx = Test.Transaction(
        code: setupVaultCode,
        authorizers: [receiver.address],
        signers: [receiver],
        arguments: [],
    )
    let setupVaultTxResult = Test.executeTransaction(setupVaultTx)
    Test.expect(setupVaultTxResult, Test.beSucceeded())

    // execute transfer transaction
    let transferAmount = 20.0
    let transferCode = Test.readFile("../transactions/transferRevvToken.cdc")
    let transferTx = Test.Transaction(
        code: transferCode,
        authorizers: [admin.address],
        signers: [admin],
        arguments: [transferAmount, receiver.address],
    )
    let transferTxResult = Test.executeTransaction(transferTx)
    Test.expect(transferTxResult, Test.beSucceeded())
}

access(all) fun testLockTokens() {
    let to = "436f795B64E23E6cE7792af4923A68AFD3967952"
    testSetupREVVTokenVault()
    let lockTokensCode = Test.readFile("../transactions/teleport/teleportOut.cdc")
    let lockTokensTx = Test.Transaction(
        code: lockTokensCode,
        authorizers: [receiver.address],
        signers: [receiver],
        arguments: [teleportAdmin.address, 12.0, to]
    )
    let lockTokenTxResult = Test.executeTransaction(lockTokensTx)
    Test.expect(lockTokenTxResult, Test.beSucceeded())

    let lockedEvents = Test.eventsOfType(Type<TeleportCustody.TokensTeleportedOut>())
    Test.assertEqual(1, lockedEvents.length)
    let lockedEvent = lockedEvents[0] as! TeleportCustody.TokensTeleportedOut
    Test.assertEqual(2.0, lockedEvent.amount)
    Test.assertEqual(to.decodeHex(), lockedEvent.to)
}

access(all) fun testUnlockTokens() {
    let from = "436f795B64E23E6cE7792af4923A68AFD3967952"
    let txHash = "31c76b8b0afbaa7029b3fbed7a2e51b9868254703d707ae98d130d35f4b7767d"
    let unlockTokensCode = Test.readFile("../transactions/teleport/teleportIn.cdc")
    let unlockTokensTx = Test.Transaction(
        code: unlockTokensCode,
        authorizers: [teleportAdmin.address],
        signers: [teleportAdmin],
        arguments: [2.0, receiver.address, from, txHash]
    )
    let unlockTokenTxResult = Test.executeTransaction(unlockTokensTx)
    Test.expect(unlockTokenTxResult, Test.beSucceeded())

    let unlockedEvents = Test.eventsOfType(Type<TeleportCustody.TokensTeleportedIn>())
    Test.assertEqual(1, unlockedEvents.length)
    let unlockedEvent = unlockedEvents[0] as! TeleportCustody.TokensTeleportedIn
    Test.assertEqual(2.0, unlockedEvent.amount)
    Test.assertEqual(from.decodeHex(), unlockedEvent.from)
    Test.assertEqual(txHash, unlockedEvent.hash)
}

access(all) fun testTransferTeleportFees() {
    let setupVaultCode = Test.readFile("../transactions/setupREVVVault.cdc")
    let setupVaultTx = Test.Transaction(
        code: setupVaultCode,
        authorizers: [feeReceiver.address],
        signers: [feeReceiver],
        arguments: [],
    )
    let setupVaultTxResult = Test.executeTransaction(setupVaultTx)
    Test.expect(setupVaultTxResult, Test.beSucceeded())

    let getREVVBalanceScript = Test.readFile("../scripts/getREVVTokenBalance.cdc")
    let result = Test.executeScript(getREVVBalanceScript, [feeReceiver.address])
    let REVVBalance = result.returnValue! as! UFix64
    Test.assertEqual(0.0, REVVBalance)

    let transferTeleportFeesCode = Test.readFile("../transactions/teleport/withdrawTeleportFees.cdc")
    let transferTeleportFeesTx = Test.Transaction(
        code: transferTeleportFeesCode,
        authorizers: [teleportAdmin.address],
        signers: [teleportAdmin],
        arguments: [feeReceiver.address]
    )
    let transferTeleportFeesTxResult = Test.executeTransaction(transferTeleportFeesTx)
    Test.expect(transferTeleportFeesTxResult, Test.beSucceeded())

    let newResult = Test.executeScript(getREVVBalanceScript, [feeReceiver.address])
    let newREVVBalance = newResult.returnValue! as! UFix64
    Test.assertEqual(10.01, newREVVBalance)
}

access(all) fun testUpdateTeleportFees() {
    let teleportFeesScript = Test.readFile("../scripts/getTeleportFees.cdc")
    let result = Test.executeScript(teleportFeesScript, [teleportAdmin.address])
    let teleportFees = result.returnValue! as! [UFix64]
    let lockFee = teleportFees[0]
    let unlockFee = teleportFees[1]
    Test.assertEqual(10.0, lockFee)
    Test.assertEqual(0.01, unlockFee)

    let newLockFee = 5.0
    let newUnlockFee = 0.02
    let updateTeleportFeeCode = Test.readFile("../transactions/teleport/updateTeleportFees.cdc")
    let updateTeleportFeeTx = Test.Transaction(
        code: updateTeleportFeeCode,
        authorizers: [teleportAdmin.address],
        signers: [teleportAdmin],
        arguments: [newUnlockFee, newLockFee]
    )
    let updateTeleportFeeTxResult = Test.executeTransaction(updateTeleportFeeTx)
    Test.expect(updateTeleportFeeTxResult, Test.beSucceeded())

    let newResult = Test.executeScript(teleportFeesScript, [teleportAdmin.address])
    let newTeleportFees = newResult.returnValue! as! [UFix64]
    let newGottenLockFee = newTeleportFees[0]
    let newGottenUnlockFee = newTeleportFees[1]
    Test.assertEqual(newGottenLockFee, newLockFee)
    Test.assertEqual(newGottenUnlockFee, newUnlockFee)
}
```