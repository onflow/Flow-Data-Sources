# Source: https://github.com/Flowtyio/flowty-drops/blob/main/tests/ContractManager_tests.cdc

```
import Test
import "./test_helpers.cdc"
import "ContractManager"
import "HybridCustody"
import "FungibleToken"
import "ExampleToken"

access(all) fun setup() {
    deployAll()
}

access(all) fun test_SetupContractManager() {
    let acct = Test.createAccount()
    mintFlowTokens(acct, 10.0)

    txExecutor("contract-manager/setup.cdc", [acct], [1.0])

    let savedEvent = Test.eventsOfType(Type<ContractManager.ManagerSaved>()).removeLast() as! ContractManager.ManagerSaved
    Test.assertEqual(acct.address, savedEvent.ownerAddress)
}

access(all) fun test_SetupContractManager_CanWithdrawTokens() {
    let acct = Test.createAccount()
    mintFlowTokens(acct, 10.0)

    let amount = 5.0
    txExecutor("contract-manager/setup.cdc", [acct], [amount])
    let savedEvent = Test.eventsOfType(Type<ContractManager.ManagerSaved>()).removeLast() as! ContractManager.ManagerSaved
    let contractAddress = savedEvent.contractAddress

    // make sure there is a HybridCustody.AccountUpdated event
    let updatedEvent = Test.eventsOfType(Type<HybridCustody.AccountUpdated>()).removeLast() as! HybridCustody.AccountUpdated
    Test.assertEqual(acct.address, updatedEvent.parent!)
    Test.assertEqual(contractAddress, updatedEvent.child)
    Test.assertEqual(true, updatedEvent.active)

    // withdraw and destroy 1 token to prove we are able to access an account's tokens
    let controllerId = scriptExecutor("util/get_withdraw_controller_id.cdc", [contractAddress, /storage/flowTokenVault])! as! UInt64
    txExecutor("flow-token/withdraw_tokens.cdc", [acct], [amount, contractAddress, controllerId])

    let withdrawEvent = Test.eventsOfType(Type<FungibleToken.Withdrawn>()).removeLast() as! FungibleToken.Withdrawn
    Test.assertEqual(amount, withdrawEvent.amount)
    Test.assertEqual(contractAddress, withdrawEvent.from!)

    let depositEvent = Test.eventsOfType(Type<FungibleToken.Deposited>()).removeLast() as! FungibleToken.Deposited
    Test.assertEqual(amount, depositEvent.amount)
    Test.assertEqual(acct.address, depositEvent.to!)
}

access(all) fun test_ContractManager_ChangedOwned_RevokesChildAccount() {
    let acct = Test.createAccount()
    mintFlowTokens(acct, 10.0)

    let amount = 5.0
    txExecutor("contract-manager/setup.cdc", [acct], [amount])
    let savedEvent = Test.eventsOfType(Type<ContractManager.ManagerSaved>()).removeLast() as! ContractManager.ManagerSaved
    let contractAddress = savedEvent.contractAddress

    let newOwner = Test.createAccount()
    mintFlowTokens(acct, 10.0)
    txExecutor("contract-manager/transfer_ownership.cdc", [acct, newOwner], [])

    // ensure that we do not have access to the withdraw capability from the original owner
    let controllerId = scriptExecutor("util/get_withdraw_controller_id.cdc", [contractAddress, /storage/flowTokenVault])! as! UInt64
    Test.expectFailure(fun() {
        txExecutor("flow-token/withdraw_tokens.cdc", [acct], [amount, contractAddress, controllerId])
    }, errorMessageSubstring: "child account not found")
}

access(all) fun test_ContractManager_SetupExampleToken() {
    let acct = Test.createAccount()
    mintFlowTokens(acct, 10.0)
    txExecutor("contract-manager/setup.cdc", [acct], [1.0])
    let savedEvent = Test.eventsOfType(Type<ContractManager.ManagerSaved>()).removeLast() as! ContractManager.ManagerSaved
    let contractAddress = savedEvent.contractAddress

    // setup ExampleToken
    txExecutor("contract-manager/setup_vault.cdc", [acct], [Type<@ExampleToken.Vault>().identifier])

    // send tokens to newly setup vault
    let amount = 1.11
    txExecutor("example-token/mint.cdc", [flowtyDropsAccount], [contractAddress, amount])

    // ensure that the parent account has access to the deposited tokens
    let controllerId = scriptExecutor("util/get_withdraw_controller_id.cdc", [contractAddress, /storage/exampleTokenVault])! as! UInt64
    txExecutor("example-token/withdraw_tokens.cdc", [acct], [amount, contractAddress, controllerId])

    let withdrawEvent = Test.eventsOfType(Type<FungibleToken.Withdrawn>()).removeLast() as! FungibleToken.Withdrawn
    Test.assertEqual(amount, withdrawEvent.amount)
    Test.assertEqual(contractAddress, withdrawEvent.from!)

    let depositEvent = Test.eventsOfType(Type<FungibleToken.Deposited>()).removeLast() as! FungibleToken.Deposited
    Test.assertEqual(amount, depositEvent.amount)
    Test.assertEqual(acct.address, depositEvent.to!)
}
```