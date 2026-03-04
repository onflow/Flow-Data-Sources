# Source: https://github.com/austinkline/managed-account/blob/main/tests/ManagedAccount_tests.cdc

```
import Test
import "test_helpers.cdc"
import "ManagedAccount"
import "ContractUpdateExecutable"

access(all) fun setup() {
    deployAll()
}

access(all) fun test() {
    Test.assert(scriptExecutor("import.cdc", [])! as! Bool, message: "failed to import contract in script")
}

access(all) fun test_SetupManager() {
    let acct = Test.createAccount()

    let voter1 = Test.createAccount()
    let voter2 = Test.createAccount()
    let voters: {Address: UFix64} = {
        voter1.address: 500.0,
        voter2.address: 500.0
    }
    
    txExecutor("setup_manager.cdc", [acct], [voters])

    let managerEvent = Test.eventsOfType(Type<ManagedAccount.ManagerCreated>()).removeLast() as! ManagedAccount.ManagerCreated
    Test.assertEqual(managerEvent.managerAddress, acct.address)
    Test.assertEqual(managerEvent.voters[voter1.address]!, 500.0)
    Test.assertEqual(managerEvent.voters[voter2.address]!, 500.0)
}

access(all) fun test_Manager_AddExecutableType() {
    let accounts = setupDefaultManager()
    let manager = accounts[0]
    let voter1 = accounts[1]
    let voter2 = accounts[2]

    let executableIdentifier = getContractUpdateExecutableIdentifier()
    txExecutor("proposals/add_executable_type.cdc", [voter1], [manager.address, executableIdentifier, true])

    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    Test.assertEqual(proposal.executableType, getChangeApprovedTypeExecutableIdentifier())
    Test.assertEqual(proposal.proposer, voter1.address)
}

access(all) fun test_Voter_VoteOnProposal() {
    let accounts = setupDefaultManager()
    let manager = accounts[0]
    let voter1 = accounts[1]
    let voter2 = accounts[2]

    let executableIdentifier = getContractUpdateExecutableIdentifier()
    txExecutor("proposals/add_executable_type.cdc", [voter1], [manager.address, executableIdentifier, true])

    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    Test.assertEqual(proposal.executableType, getChangeApprovedTypeExecutableIdentifier())
    Test.assertEqual(proposal.proposer, voter1.address)

    txExecutor("vote.cdc", [voter1], [manager.address, proposal.uuid, true])
    let voter1Event = Test.eventsOfType(Type<ManagedAccount.VoteCast>()).removeLast() as! ManagedAccount.VoteCast
    Test.assertEqual(voter1Event.managerAddress, manager.address)
    Test.assertEqual(voter1Event.approved, true)
    Test.assertEqual(voter1Event.proposalId, proposal.uuid)
    Test.assertEqual(voter1Event.weight, 500.0)

    txExecutor("vote.cdc", [voter2], [manager.address, proposal.uuid, false])
    let voter2Event = Test.eventsOfType(Type<ManagedAccount.VoteCast>()).removeLast() as! ManagedAccount.VoteCast
    Test.assertEqual(voter2Event.managerAddress, manager.address)
    Test.assertEqual(voter2Event.approved, false)
    Test.assertEqual(voter2Event.proposalId, proposal.uuid)
    Test.assertEqual(voter2Event.weight, 500.0)
}

access(all) fun test_Manager_AddExecutableType_Run() {
    let accounts = setupDefaultManager()
    let manager = accounts[0]
    let voter1 = accounts[1]
    let voter2 = accounts[2]

    let executableIdentifier = getContractUpdateExecutableIdentifier()
    txExecutor("proposals/add_executable_type.cdc", [voter1], [manager.address, executableIdentifier, true])
    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    txExecutor("vote.cdc", [voter1], [manager.address, proposal.uuid, true])
    txExecutor("vote.cdc", [voter2], [manager.address, proposal.uuid, true])

    let runner = Test.createAccount()
    txExecutor("run.cdc", [runner], [manager.address, proposal.uuid])

    let proposalRunEvent = Test.eventsOfType(Type<ManagedAccount.ProposalRun>()).removeLast() as! ManagedAccount.ProposalRun
    Test.assertEqual(proposalRunEvent.managerAddress, manager.address)
    Test.assertEqual(proposalRunEvent.proposalId, proposal.uuid)

    let executableTypes = scriptExecutor("get_executable_types.cdc", [manager.address])! as! [String]
    Test.assert(executableTypes.contains(executableIdentifier), message: "missing ContractUpdateExecutable identifier")
}

access(all) fun test_ContractUpdateExecutable_AddContract() {
    let accounts = initializeWithContractUpdateManager()
    let aCode = loadCode("samples/A.cdc", "contracts")

    txExecutor("proposals/update_contracts.cdc", [accounts.voter1], [accounts.manager.address, ["A"], [aCode], [false]])
    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    txExecutor("vote.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid, true])
    txExecutor("vote.cdc", [accounts.voter2], [accounts.manager.address, proposal.uuid, true])

    txExecutor("run.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid])

    // can we run the `foo` method on A?
    let script = "import A from ".concat(accounts.manager.address.toString()).concat("\n")
    .concat("access(all) fun main(): String { return A.foo() }")
    
    let scriptResult = Test.executeScript(script, []).returnValue! as! String
    Test.assertEqual("hello, world!", scriptResult)
}

access(all) fun test_ContractUpdateExecutable_UpdateContract() {
    let accounts = initializeWithContractUpdateManager()
    let aCode = loadCode("samples/A.cdc", "contracts")
    txExecutor("deploy.cdc", [accounts.manager], ["A", aCode.utf8])


    let aCodeUpdate = loadCode("samples/A_updated.cdc", "contracts")
    txExecutor("proposals/update_contracts.cdc", [accounts.voter1], [accounts.manager.address, ["A"], [aCodeUpdate], [true]])
    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    txExecutor("vote.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid, true])
    txExecutor("vote.cdc", [accounts.voter2], [accounts.manager.address, proposal.uuid, true])

    txExecutor("run.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid])

    // can we run the `foo` method on A?
    let script = "import A from ".concat(accounts.manager.address.toString()).concat("\n")
    .concat("access(all) fun main(): String { return A.foo() }")
    
    let scriptResult = Test.executeScript(script, []).returnValue! as! String
    Test.assertEqual("updated!", scriptResult)
}

access(all) fun test_ContractUpdateExecutable_Multiple() {
    let accounts = initializeWithContractUpdateManager()
    let aCode = loadCode("samples/A.cdc", "contracts")
    txExecutor("deploy.cdc", [accounts.manager], ["A", aCode.utf8])


    let aCodeUpdate = loadCode("samples/A_updated.cdc", "contracts")
    let bCode = loadCode("samples/B.cdc", "contracts")
    txExecutor("proposals/update_contracts.cdc", [accounts.voter1], [accounts.manager.address, ["A", "B"], [aCodeUpdate, bCode], [true, false]])
    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    txExecutor("vote.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid, true])
    txExecutor("vote.cdc", [accounts.voter2], [accounts.manager.address, proposal.uuid, true])

    txExecutor("run.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid])
    txExecutor("run.cdc", [accounts.voter1], [accounts.manager.address, proposal.uuid])

    // can we run the `foo` method on A?
    let script = "import A from ".concat(accounts.manager.address.toString()).concat("\n")
        .concat("access(all) fun main(): String { return A.foo() }")
    
    let scriptResult = Test.executeScript(script, []).returnValue! as! String
    Test.assertEqual("updated!", scriptResult)

    // can we run the `echo` method on B?
    let bInput = "this is an input"

    let bScript = "import B from ".concat(accounts.manager.address.toString()).concat("\n")
        .concat("access(all) fun main(s: String): String { return B.echo(s) }")
    let bScriptResult = Test.executeScript(bScript, [bInput]).returnValue! as! String
    Test.assertEqual(bInput, bScriptResult)
}

// ------------------------------------------------------------------------
// -------------------------  HELPER TRANSACTIONS -------------------------

access(all) struct ManagerAndVoters {
    access(all) let manager: Test.TestAccount
    access(all) let voter1: Test.TestAccount
    access(all) let voter2: Test.TestAccount

    init(accounts: [Test.TestAccount]) {
        self.manager = accounts[0]
        self.voter1 = accounts[1]
        self.voter2 = accounts[2]
    }
}

access(all) fun setupDefaultManager(): [Test.TestAccount] {
    let acct = Test.createAccount()
    let voter1 = Test.createAccount()
    let voter2 = Test.createAccount()
    let voters: {Address: UFix64} = {
        voter1.address: 500.0,
        voter2.address: 500.0
    }
    
    txExecutor("setup_manager.cdc", [acct], [voters])

    return [acct, voter1, voter2]
}

access(all) fun getContractUpdateExecutableIdentifier(): String {
    return Type<@ContractUpdateExecutable.Executable>().identifier
}

access(all) fun getChangeApprovedTypeExecutableIdentifier(): String {
    return Type<@ManagedAccount.ChangeApprovedTypeExecutable>().identifier
}

access(all) fun initializeWithContractUpdateManager(): ManagerAndVoters {
    let accounts = setupDefaultManager()
    let manager = accounts[0]
    let voter1 = accounts[1]
    let voter2 = accounts[2]

    let m = ManagerAndVoters(accounts: accounts)
    
    let executableIdentifier = getContractUpdateExecutableIdentifier()
    txExecutor("proposals/add_executable_type.cdc", [voter1], [manager.address, executableIdentifier, true])
    let proposal = Test.eventsOfType(Type<ManagedAccount.ProposalAdded>()).removeLast() as! ManagedAccount.ProposalAdded

    txExecutor("vote.cdc", [voter1], [manager.address, proposal.uuid, true])
    txExecutor("vote.cdc", [voter2], [manager.address, proposal.uuid, true])

    txExecutor("run.cdc", [voter1], [manager.address, proposal.uuid])

    return m
}
```