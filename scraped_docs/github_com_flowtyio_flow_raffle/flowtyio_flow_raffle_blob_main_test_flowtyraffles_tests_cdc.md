# Source: https://github.com/Flowtyio/flow-raffle/blob/main/test/FlowtyRaffles_tests.cdc

```
import Test
import "test_helpers.cdc"

import "FlowtyRaffles"
import "MetadataViews"

access(all) let FlowtyRafflesContractAddress = Address(0x0000000000000007)
access(all) let FlowtyRaffleSourceContractAddress = Address(0x0000000000000008)
access(all) let Xorshift128plusContractAddress = Address(0x0000000000000008)

access(all) let GenericRaffleSourceIdentifier = "A.0000000000000008.FlowtyRaffleSource.AnyStructRaffleSource"

access(all) fun setup() {
    var err = Test.deployContract(name: "FlowtyRaffles", path: "../contracts/FlowtyRaffles.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    err = Test.deployContract(name: "FlowtyRaffleSource", path: "../contracts/FlowtyRaffleSource.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    // err = Test.deployContract(name: "Xorshift128plus", path: "../contracts/standard/Xorshift128plus.cdc", arguments: [])
    // Test.expect(err, Test.beNil())
}

access(all) fun testSetupManager() {
    let acct = Test.createAccount()
    txExecutor("setup_manager.cdc", [acct], [], nil)
    scriptExecutor("borrow_manager.cdc", [acct.address])
}

access(all) fun testCreateRaffleSource() {
    let acct = Test.createAccount()
    let path = StoragePath(identifier: "testCreateRaffleSource")!
    txExecutor("create_raffle_source.cdc", [acct], [Type<Address>(), path], nil)
    let res = scriptExecutor("get_raffle_source_identifier.cdc", [acct.address, path])
    assert(res! as! String == GenericRaffleSourceIdentifier, message: "unexpected raffle source identifier")
}

access(all) fun testCreateRaffle() {
    let acct = Test.createAccount()
    let name = "testCreateRaffle"
    let description = "testCreateRaffle desc"
    let thumbnail = "https://example.com/thumbnail"
    let start: UInt64? = nil
    let end: UInt64? = nil
    let externalURL = "example.com"
    let commitBlocksAhead = 0 as UInt64

    txExecutor("create_raffle.cdc", [acct], [Type<Address>(), start, end, name, description, thumbnail, externalURL, commitBlocksAhead, nil], nil)
    let createEvent = (Test.eventsOfType(Type<FlowtyRaffles.RaffleCreated>()).removeLast() as! FlowtyRaffles.RaffleCreated)
    assert(acct.address == createEvent.address)

    let details = getRaffleDetails(acct, createEvent.raffleID) ?? panic("raffle not found")

    assert(name == details.display!.name)
    assert(description == details.display!.description)
    assert(thumbnail == details.display!.thumbnail.uri())
    assert(start == details.start)
    assert(end == details.end)
}

access(all) fun testAddToRaffle() {
    let acct = Test.createAccount()
    let id = createAddressRaffle(acct)
    let beforeEntries = getRaffleEntries(acct, id)!
    assert(beforeEntries.length == 0)

    addEntryToRaffle(acct, id, acct.address)

    
    let afterEntries = getRaffleEntries(acct, id)!
    assert(afterEntries.length == 1)
    assert(afterEntries[0] as! Address == acct.address)
}

access(all) fun testDrawFromRaffle() {
    let acct = Test.createAccount()
    let id = createAddressRaffle(acct)
    let beforeEntries = getRaffleEntries(acct, id)!
    addEntryToRaffle(acct, id, acct.address)

    // make sure we can draw an entry from the raffle, even when it only has a single item in it
    let drawing = drawFromRaffle(acct, acct.address, id)
    assert(drawing == acct.address.toString())

    // now let's add lots of additional entries
    let accounts: {String: Test.TestAccount} = {
        acct.address.toString(): acct
    }
    var count = 0
    while count < 10 {
        count = count + 1
        let a = Test.createAccount()
        accounts[a.address.toString()] = a
    }

    // draw again, making sure that the winner is in our dictionary
    let drawing2 = drawFromRaffle(acct, acct.address, id)
    assert(accounts[drawing2] != nil)
}

access(all) fun getRaffleDetails(_ acct: Test.TestAccount, _ id: UInt64): FlowtyRaffles.Details? {
    if let res = scriptExecutor("get_raffle_details.cdc", [acct.address, id]) {
        return res as! FlowtyRaffles.Details
    }
    return nil
}

access(all) fun getRaffleEntries(_ acct: Test.TestAccount, _ id: UInt64): [AnyStruct]? {
    if let res = scriptExecutor("get_raffle_entries.cdc", [acct.address, id]) {
        return res as! [AnyStruct]
    }
    return nil
}

access(all) fun getRaffleEntriesCount(_ acct: Test.TestAccount, _ id: UInt64): Int? {
    if let res = scriptExecutor("get_num_raffle_entries.cdc", [acct.address, id]) {
        return res as! Int
    }
    return nil
}

access(all) fun addEntryToRaffle(_ acct: Test.TestAccount, _ id: UInt64, _ entry: AnyStruct) {
    txExecutor("add_entry_to_raffle.cdc", [acct], [id, entry], nil)
}

access(all) fun addEntriesToRaffle(_ acct: Test.TestAccount, _ id: UInt64, _ entries: [AnyStruct]) {
    txExecutor("add_entries_to_raffle.cdc", [acct], [id, entries], nil)
}

access(all) fun createAddressRaffle(_ acct: Test.TestAccount): UInt64 {
    let name = "address raffle"
    let description = "address raffle desc"
    let thumbnail = "https://example.com/thumbnail"
    let start: UInt64? = nil
    let end: UInt64? = nil
    let externalURL = "example.com"
    let commitBlocksAhead = 0 as UInt64

    txExecutor("create_raffle.cdc", [acct], [Type<Address>(), start, end, name, description, thumbnail, externalURL, commitBlocksAhead, nil], nil)
    let createEvent = (Test.eventsOfType(Type<FlowtyRaffles.RaffleCreated>()).removeLast() as! FlowtyRaffles.RaffleCreated)
    return createEvent.raffleID
}

access(all) fun drawFromRaffle(_ signer: Test.TestAccount, _ addr: Address, _ id: UInt64): String {
    txExecutor("draw_from_raffle.cdc", [signer], [addr, id], nil)

    let drawingEvent = Test.eventsOfType(Type<FlowtyRaffles.RaffleReceiptRevealed>()).removeLast() as! FlowtyRaffles.RaffleReceiptRevealed
    return drawingEvent.value ?? ""
}
```