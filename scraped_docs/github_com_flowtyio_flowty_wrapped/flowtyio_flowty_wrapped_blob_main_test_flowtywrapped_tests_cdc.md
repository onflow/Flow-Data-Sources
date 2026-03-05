# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/test/FlowtyWrapped_tests.cdc

```
import Test
import "test_helpers.cdc"

import "FlowtyWrapped"
import "MetadataViews"
import "WrappedEditions"
import "FlowtyRaffles"

access(all)  let rafflesAcct = Test.getAccount(Address(0x0000000000000007))
access(all)  let minterAccount = Test.getAccount(Address(0x0000000000000007))

access(all) fun setup() {
    var err = Test.deployContract(name: "FlowtyRaffles", path: "../contracts/raffle/FlowtyRaffles.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    err = Test.deployContract(name: "FlowtyRaffleSource", path: "../contracts/raffle/FlowtyRaffleSource.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    err = Test.deployContract(name: "ArrayUtils", path: "../node_modules/@flowtyio/flow-contracts/contracts/flow-utils/ArrayUtils.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    err = Test.deployContract(name: "StringUtils", path: "../node_modules/@flowtyio/flow-contracts/contracts/flow-utils/StringUtils.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    err = Test.deployContract(name: "FlowtyWrapped", path: "../contracts/FlowtyWrapped.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    err = Test.deployContract(name: "WrappedEditions", path: "../contracts/WrappedEditions.cdc", arguments: [])
    Test.expect(err, Test.beNil())

    // register a test wrapped edition
    let removeAfterReveal: Bool = true
    let start: UInt64? = nil
    let end: UInt64? = nil
    let baseImageUrl: String = "https://example.com/image/"
    let baseHtmlUrl: String = "QmRfVR98oe6qxeWFcnY9tfM2CLUJg3rvxbBPS5LjYwp69Z"
    registerEdition(rafflesAcct: Test.getAccount(Address(0x0000000000000007)), removeAfterReveal: removeAfterReveal, start: start, end: end, baseImageUrl: baseImageUrl, baseHtmlUrl: baseHtmlUrl)
    
}

access(all) fun testSetupManager() {
    let acct = Test.createAccount()
    txExecutor("setup_flowty_wrapped.cdc", [acct], [], nil)
}

access(all) fun testGetRaffleManager() {
    scriptExecutor("raffle/borrow_raffle_manager.cdc", [rafflesAcct.address])
}

access(all) fun testSetCollectionExternalUrl() {
    let baseHtmlUrl: String = "https://flowty.io/asset/0x0000000000000007/FlowtyWrappedTEST"

    txExecutor("set_collection_external_url.cdc", [rafflesAcct], [baseHtmlUrl], nil)

    let result = scriptExecutor("get_collection_external_url.cdc", [])
    let castedResult = result! as! String
    assert(castedResult == baseHtmlUrl, message: "baseHtmlUrl does not match expected")
}

access(all) fun testMint() {
    let acct = Test.createAccount()
    let username: String = "user1"
    setupForMint(acct: acct, name: username)   
}

access(all) fun testGetEditions() {
    let acct = Test.createAccount()
    let username: String = "user1"
    setupForMint(acct: acct, name: username)
    let result = scriptExecutor("get_nft_ids.cdc", [acct.address])

    let castedResult = result! as! [UInt64]
    var nftID1 = castedResult[0]

    scriptExecutor("get_editions_flowty_wrapped.cdc", [acct.address, nftID1])
}

access(all) fun testEditionResolveView() {
    let acct = Test.createAccount()

    let currentEditionNumber = getEditionNumber()

    let expectedEditionName = "Flowty Wrapped 2023"
    let expectedEditionNumber: UInt64 = currentEditionNumber + 1
    let expectedEditionMax = nil

    let username: String = "user1"
    setupForMint(acct: acct, name: username)

    let result = scriptExecutor("get_nft_ids.cdc", [acct.address])

    let castedResult = result! as! [UInt64]
    var nftID1 = castedResult[0]

    let res: AnyStruct? = scriptExecutor("get_editions_flowty_wrapped.cdc", [acct.address, nftID1])
    let castedTest = res! as! MetadataViews.Editions
    let Edition = castedTest.infoList[0]

    let name = Edition.name!
    let number = Edition.number
    let max = Edition.max

    assert(name == expectedEditionName, message: "Edition name is not expected result")
    assert(number == expectedEditionNumber, message: "NFT serial is not expected result")
    assert(max == expectedEditionMax, message: "max should be nil")
}

access(all) fun testDepositToWrongAddressFails() {
    let acct = Test.createAccount()
    let wrongAccount = Test.createAccount()
    

    txExecutor("setup_flowty_wrapped.cdc", [acct], [], nil)
    txExecutor("setup_flowty_wrapped.cdc", [wrongAccount], [], nil)


    let username: String = "user1"
    let ticket: Int = 1
    let totalNftsOwned: Int = 1
    let floatCount: Int = 1
    let favoriteCollections: [String] = [""]
    let collections: [String] = [""]

    txExecutor("fail_mint_to_wrong_account.cdc", [minterAccount], [acct.address, wrongAccount.address, username, ticket, totalNftsOwned, floatCount, favoriteCollections, collections], "The NFT must be owned by the collection owner")

}


    
access(all) fun testBorrowNFT() {
    let acct = Test.createAccount()
    let username: String = "user1"
    setupForMint(acct: acct, name: username)

    let result = scriptExecutor("get_nft_ids.cdc", [acct.address])

    let castedResult = result! as! [UInt64]
    var nftID1 = castedResult[0]

    scriptExecutor("borrow_nft.cdc", [acct.address, nftID1])
}

access(all) fun testSingleMint() {
    let acct = Test.createAccount()

    txExecutor("setup_flowty_wrapped.cdc", [acct], [], nil)

    let username: String = "testSingleMint"
    let ticket: Int = 1
    let totalNftsOwned: Int = 1
    let floatCount: Int = 1
    let favoriteCollections: [String] = [""]
    let collections: [String] = [""]

    txExecutor("mint_flowty_wrapped.cdc", [minterAccount], [acct.address, username, ticket, totalNftsOwned, floatCount, favoriteCollections, collections], nil)

    // now try to mint again, this should fail
    txExecutor("mint_flowty_wrapped.cdc", [minterAccount], [acct.address, username, ticket, totalNftsOwned, floatCount, favoriteCollections, collections], "address has already been minted")
}

access(all) fun testWithdrawFails() {
    let acct = Test.createAccount()
    let acct2 = Test.createAccount()
    let username: String = "user1"
    setupForMint(acct: acct, name: username)

    let result = scriptExecutor("get_nft_ids.cdc", [acct.address])

    let castedResult = result! as! [UInt64]
    var nftID1 = castedResult[0]

    txExecutor("withdraw_nft.cdc", [acct], [acct.address, acct2.address, nftID1], "Flowty Wrapped is not transferrable")
}

access(all) fun testMediasIpfsUrl() {
    let acct = Test.createAccount()
    let username: String = "user1"
    setupForMint(acct: acct, name: username)
    let result = scriptExecutor("get_nft_ids.cdc", [acct.address])

    let castedResult = result! as! [UInt64]
    var nftID = castedResult[0]

    let medias = getMedias(addr: acct.address, nftID: nftID)

    let ipfsMedia = medias.items[0]
    let ipfsUrl = ipfsMedia.file.uri()
    assert(ipfsUrl == "ipfs://QmRfVR98oe6qxeWFcnY9tfM2CLUJg3rvxbBPS5LjYwp69Z?username=user1&raffleTickets=1", message: "unexpected ipfs url")
}

access(all) fun testIpfsUrlNoName() {
    let acct = Test.createAccount()
    let username: String = ""
    setupForMint(acct: acct, name: username)
    let result = scriptExecutor("get_nft_ids.cdc", [acct.address])

    let castedResult = result! as! [UInt64]
    var nftID = castedResult[0]

    let medias = getMedias(addr: acct.address, nftID: nftID)

    let ipfsMedia = medias.items[0]
    let ipfsUrl = ipfsMedia.file.uri()
    assert(ipfsUrl == "ipfs://QmRfVR98oe6qxeWFcnY9tfM2CLUJg3rvxbBPS5LjYwp69Z?username=".concat(acct.address.toString()).concat("&raffleTickets=1"), message: "unexpected ipfs url")
}

access(all) fun testDrawRaffle() {
    let acct = Test.createAccount()
    let username: String = "user1"

    let editionName = "Flowty Wrapped 2023"
    let createEvent = (Test.eventsOfType(Type<FlowtyRaffles.RaffleCreated>()).removeLast() as! FlowtyRaffles.RaffleCreated)
    
    setupForMint(acct: acct, name: username)
    let entries: AnyStruct = scriptExecutor("raffle/get_raffle_entries.cdc", [minterAccount.address, createEvent.raffleID])!
    let castedEntries = entries as! [AnyStruct]
    
    assert(castedEntries.length >= 1, message: "no entries")
    assert(castedEntries[castedEntries.length - 1] as! Address == acct.address)

    let drawing = drawFromRaffle(rafflesAcct, createEvent.raffleID)

    var winnerIsFromEntryPool = false
    for e in castedEntries {
        let c = (e as! Address).toString()
        if c == drawing{
            winnerIsFromEntryPool = true
            break
        }
    }
    assert(winnerIsFromEntryPool)
}

access(all) fun registerEdition(rafflesAcct: Test.TestAccount, removeAfterReveal: Bool, start: UInt64?, end: UInt64?, baseImageUrl: String, baseHtmlUrl: String) {
    txExecutor("register_edition.cdc", [rafflesAcct], [removeAfterReveal, start, end, baseImageUrl, baseHtmlUrl], nil)
}

access(all) fun getMedias(addr: Address, nftID: UInt64): MetadataViews.Medias {
    return scriptExecutor("get_medias.cdc", [addr, nftID])! as! MetadataViews.Medias
}

access(all) fun getEditionNumber(): UInt64{
    let editionName = "Flowty Wrapped 2023"
    let res = scriptExecutor("get_total_edition_supply.cdc", [minterAccount.address, editionName])

    let editionNumber = res! as! UInt64
    return editionNumber
}

access(all) fun setupForMint(acct: Test.TestAccount, name: String) {

    txExecutor("setup_flowty_wrapped.cdc", [acct], [], nil)

    let ticket: Int = 1
    let totalNftsOwned: Int = 1
    let floatCount: Int = 1
    let favoriteCollections: [String] = [""]
    let collections: [String] = [""]

    txExecutor("mint_flowty_wrapped.cdc", [minterAccount], [acct.address, name, ticket, totalNftsOwned, floatCount, favoriteCollections, collections], nil)
}

access(all) fun drawFromRaffle(_ signer: Test.TestAccount, _ id: UInt64): String {
    txExecutor("raffle/draw_from_raffle.cdc", [signer], [id], nil)

    let drawingEvent = Test.eventsOfType(Type<FlowtyRaffles.RaffleReceiptRevealed>()).removeLast() as! FlowtyRaffles.RaffleReceiptRevealed
    return drawingEvent.value ?? ""
}
```