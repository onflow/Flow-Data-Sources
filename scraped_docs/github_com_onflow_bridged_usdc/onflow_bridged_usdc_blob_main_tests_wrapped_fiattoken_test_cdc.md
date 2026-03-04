# Source: https://github.com/onflow/bridged-usdc/blob/main/tests/wrapped_fiattoken_test.cdc

```
import Test
import BlockchainHelpers
import "test_helpers.cdc"
import "FungibleToken"
import "FungibleTokenMetadataViews"
import "USDCFlow"

access(all) let admin = Test.getAccount(0x0000000000000007)
access(all) let usdcFlowContractAccount = Test.getAccount(0x0000000000000008)
access(all) let recipient = Test.createAccount()

access(all) let VaultStoragePath = StoragePath(identifier: "USDCVault")!
access(all) let VaultBalancePubPath = PublicPath(identifier: "USDCVaultBalance")!
access(all) let VaultReceiverPubPath = PublicPath(identifier: "USDCVaultReceiver")!
access(all) let VaultUUIDPubPath = PublicPath(identifier: "USDCVaultUUID")!
access(all) let MinterStoragePath = StoragePath(identifier: "USDCMinter")!
access(all) let initTotalSupply = 1000.0

access(all)
fun setup() {
    deployWithArgs(
        "FlowEVMBridgeHandlerInterfaces",
        "../contracts/utility/FlowEVMBridgeHandlerInterfaces.cdc",
        args: []
    )

    deployWithArgs(
        "FlowEVMBridgeConfig",
        "../contracts/utility/FlowEVMBridgeConfig.cdc",
        args: []
    )

    // deployWithArgs(
    //     "FlowEVMBridgeHandlers",
    //     "../contracts/utility/FlowEVMBridgeHandlers.cdc",
    //     args: []
    // )

    // var err = Test.deployContract(
    //     name: "FiatToken",
    //     path: "../contracts/utility/FiatToken.cdc",
    //     arguments: [
    //         VaultStoragePath,
    //         VaultBalancePubPath,
    //         VaultReceiverPubPath,
    //         MinterStoragePath,
    //         initTotalSupply
    //     ]
    // )
    // Test.expect(err, Test.beNil())

    var err = Test.deployContract(
        name: "USDCFlow",
        path: "../contracts/USDCFlow.cdc",
        arguments: []
    )
    Test.expect(err, Test.beNil())
}

access(all)
fun testGetTotalSupply() {
    let scriptResult = _executeScript(
        "../transactions/scripts/get_supply.cdc",
        []
    )
    Test.expect(scriptResult, Test.beSucceeded())

    let totalSupply = scriptResult.returnValue! as! UFix64
    Test.assertEqual(0.00000000, totalSupply)
}

access(all)
fun testSetupAccount() {
    let txResult = _executeTransaction(
        "../transactions/setup_account.cdc",
        [],
        recipient
    )
    Test.expect(txResult, Test.beSucceeded())
}

access(all)
fun testMintTokens() {
    let txResult = executeTransaction(
        "../transactions/mint.cdc",
        [recipient.address, 250.0],
        usdcFlowContractAccount
    )
    Test.expect(txResult, Test.beSucceeded())

    // Test that the proper events were emitted
    var typ = Type<USDCFlow.Minted>()
    var events = Test.eventsOfType(typ)
    Test.assertEqual(1, events.length)

    let tokensMintedEvent = events[0] as! USDCFlow.Minted
    Test.assertEqual(250.0, tokensMintedEvent.amount)

    typ = Type<FungibleToken.Deposited>()
    let depositEvents = Test.eventsOfType(typ)

    let tokensDepositedEvent = depositEvents[depositEvents.length - 1] as! FungibleToken.Deposited
    Test.assertEqual(250.0, tokensDepositedEvent.amount)
    Test.assertEqual(recipient.address, tokensDepositedEvent.to!)
    Test.assertEqual("A.0000000000000008.USDCFlow.Vault", tokensDepositedEvent.type)

    // Test that the totalSupply increased by the amount of minted tokens
    var scriptResult = executeScript(
        "../transactions/scripts/get_supply.cdc",
        []
    )
    Test.expect(scriptResult, Test.beSucceeded())
    var totalSupply = scriptResult.returnValue! as! UFix64
    Test.assertEqual(250.0, totalSupply)

    scriptResult = _executeScript(
        "../transactions/scripts/get_balance.cdc",
        [recipient.address]
    )
    Test.expect(scriptResult, Test.beSucceeded())

    var balance = scriptResult.returnValue! as! UFix64
    Test.assertEqual(250.0, balance)
}

access(all)
fun testTransferTokens() {
    let txResult = _executeTransaction(
        "../transactions/safe_generic_transfer.cdc",
        [50.0, usdcFlowContractAccount.address, "usdcFlowVault", "usdcFlowReceiver"],
        recipient
    )
    Test.expect(txResult, Test.beSucceeded())

    var scriptResult = _executeScript(
        "../transactions/scripts/get_balance.cdc",
        [recipient.address]
    )
    Test.expect(scriptResult, Test.beSucceeded())

    var balance = scriptResult.returnValue! as! UFix64
    // 250.0 tokens were previously minted to the recipient
    Test.assertEqual(200.0, balance)

    scriptResult = _executeScript(
        "../transactions/scripts/get_balance.cdc",
        [usdcFlowContractAccount.address]
    )
    Test.expect(scriptResult, Test.beSucceeded())

    // The usdcFlowContractAccount had initially 0.0 tokens so should have 50 now
    balance = scriptResult.returnValue! as! UFix64
    Test.assertEqual(50.0, balance)
}

access(all)
fun testGetViews() {
    let scriptResult = _executeScript(
        "../transactions/scripts/get_views.cdc",
        [recipient.address]
    )
    Test.expect(scriptResult, Test.beSucceeded())

    let supportedViews = scriptResult.returnValue! as! [Type]
    let expectedViews = [
        Type<FungibleTokenMetadataViews.FTView>(),
        Type<FungibleTokenMetadataViews.FTDisplay>(),
        Type<FungibleTokenMetadataViews.FTVaultData>(),
        Type<FungibleTokenMetadataViews.TotalSupply>()
    ]
    Test.assertEqual(expectedViews, supportedViews)
}

// // Not able to be fully tested until the bridge config is available on emulator
// access(all)
// fun testTransferMinterToBridge() {
    // var txResult = _executeTransaction(
    //     "transactions/create_cadence_native_token_handler.cdc",
    //     ["A.0000000000000007.USDCFlow.Vault", "A.0000000000000007.USDCFlow.MinterResource"],
    //     admin
    // )
    // Test.expect(txResult, Test.beSucceeded())

    // txResult = _executeTransaction(
    //     "transactions/enable_token_handler.cdc",
    //     ["A.0000000000000007.USDCFlow.Vault"],
    //     admin
    // )
    // Test.expect(txResult, Test.beSucceeded())

    // deployWithArgs(
    //     "USDCFlowMinterToBridge",
    //     "../contracts/USDCFlowMinterToBridge.cdc",
    //     args: [
    //         admin.address
    //     ]
    // )
// }
```