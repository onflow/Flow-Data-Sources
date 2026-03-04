# Source: https://github.com/Flowtyio/flowty-drops/blob/main/tests/test_helpers.cdc

```
import Test

import "NonFungibleToken"
import "FlowToken"
import "FlowtyDrops"
import "OpenEditionNFT"
import "NFTMetadata"
import "MetadataViews"
import "OpenEditionInitializer"

// Helper functions. All of the following were taken from
// https://github.com/onflow/Offers/blob/fd380659f0836e5ce401aa99a2975166b2da5cb0/lib/cadence/test/Offers.cdc
// - deploy
// - scriptExecutor
// - txExecutor

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

access(all) fun expectScriptFailure(_ scriptName: String, _ arguments: [AnyStruct]): String {
    let scriptCode = loadCode(scriptName, "scripts")
    let scriptResult = Test.executeScript(scriptCode, arguments)

    assert(scriptResult.error != nil, message: "script error was expected but there is no error message")
    return scriptResult.error!.message
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
    if txResult.error != nil  {
        panic(txResult.error!.message)
    }

    return txResult
}

access(all) fun loadCode(_ fileName: String, _ baseDirectory: String): String {
    return Test.readFile("../".concat(baseDirectory).concat("/").concat(fileName))
}

access(all) enum ErrorType: UInt8 {
    access(all) case TX_PANIC
    access(all) case TX_ASSERT
    access(all) case TX_PRE
}

// the cadence testing framework allocates 4 addresses for system acounts,
// and 10 pre-created accounts for us to use for deployments:
access(all) let Account0x6 = Address(0x0000000000000006)
access(all) let Account0x7 = Address(0x0000000000000007)
access(all) let Account0x8 = Address(0x0000000000000008)
access(all) let Account0x9 = Address(0x0000000000000009)
access(all) let Account0xa = Address(0x000000000000000a)
access(all) let Account0xb = Address(0x000000000000000b)
access(all) let Account0xc = Address(0x000000000000000c)
access(all) let Account0xd = Address(0x000000000000000d)
access(all) let Account0xe = Address(0x000000000000000e)

// Flow Token constants
access(all) let flowTokenStoragePath = /storage/flowTokenVault
access(all) let flowTokenReceiverPath = /public/flowTokenReceiver

access(all) let serviceAccount = Test.serviceAccount()
access(all) let flowtyDropsAccount = Test.getAccount(Account0x6)
access(all) let openEditionAccount = Test.getAccount(Account0x7)
access(all) let exampleTokenAccount = Test.getAccount(Account0x8)

access(all) fun deployAll() {
    deploy("ExampleToken", "../node_modules/@flowtyio/flow-contracts/contracts/example/ExampleToken.cdc", [])

    deploy("ArrayUtils", "../node_modules/@flowtyio/flow-contracts/contracts/flow-utils/ArrayUtils.cdc", [])
    deploy("StringUtils", "../node_modules/@flowtyio/flow-contracts/contracts/flow-utils/StringUtils.cdc", [])
    deploy("AddressUtils", "../node_modules/@flowtyio/flow-contracts/contracts/flow-utils/AddressUtils.cdc", [])
    deploy("FungibleTokenRouter", "../node_modules/@flowtyio/flow-contracts/contracts/fungible-token-router/FungibleTokenRouter.cdc", [])

    deploy("CapabilityFilter", "../node_modules/@flowtyio/flow-contracts/contracts/hybrid-custody/CapabilityFilter.cdc", [])
    deploy("CapabilityFactory", "../node_modules/@flowtyio/flow-contracts/contracts/hybrid-custody/CapabilityFactory.cdc", [])
    deploy("CapabilityDelegator", "../node_modules/@flowtyio/flow-contracts/contracts/hybrid-custody/CapabilityDelegator.cdc", [])
    deploy("FTAllFactory", "../node_modules/@flowtyio/flow-contracts/contracts/hybrid-custody/factories/FTAllFactory.cdc", [])
    deploy("HybridCustody", "../node_modules/@flowtyio/flow-contracts/contracts/hybrid-custody/HybridCustody.cdc", [])

    deploy("FlowtyDrops", "../contracts/FlowtyDrops.cdc", [])
    deploy("NFTMetadata", "../contracts/nft/NFTMetadata.cdc", [])
    deploy("BaseCollection", "../contracts/nft/BaseCollection.cdc", [])

    deploy("ContractManager", "../contracts/ContractManager.cdc", [])
    deploy("UniversalCollection", "../contracts/nft/UniversalCollection.cdc", [])
    deploy("ContractInitializer", "../contracts/initializers/ContractInitializer.cdc", [])
    deploy("ContractBorrower", "../contracts/initializers/ContractBorrower.cdc", [])
    deploy("OpenEditionInitializer", "../contracts/initializers/OpenEditionInitializer.cdc", [])

    deploy("BaseNFT", "../contracts/nft/BaseNFT.cdc", [])
    deploy("FlowtyActiveCheckers", "../contracts/FlowtyActiveCheckers.cdc", [])
    deploy("FlowtyPricers", "../contracts/FlowtyPricers.cdc", [])
    deploy("FlowtyAddressVerifiers", "../contracts/FlowtyAddressVerifiers.cdc", [])
    deploy("DropFactory", "../contracts/DropFactory.cdc", [])

    // 0x8
    deploy("DropTypes", "../contracts/DropTypes.cdc", [])

    // 0x7
    // OpenEditionNFT requires some setup to be able to actually run fully.
    // its input arguments are: params: {String: AnyStruct}, initializerIdentifier: String
    // params needs to have an instance of NFTMetadata.Data in the "data" key,
    // and an instance of NFTMetadata.CollectionInfo in the "collectionInfo" key
    // 
    // the initializer is OpenEditionInitializer
    let collectionInfo = NFTMetadata.CollectionInfo(
        collectionDisplay: MetadataViews.NFTCollectionDisplay(
            name: "The Open Edition Collection",
            description: "This collection is used as an example to help you develop your next Open Edition Flow NFT",
            externalURL: MetadataViews.ExternalURL("https://flowty.io"),
            squareImage: MetadataViews.Media(
                file: MetadataViews.IPFSFile(
                    cid: "QmWWLhnkPR3ejavNtzeJcdG9fwcBHKwBVEP4pZ9rGbdHEM",
                    path: nil
                ),
                mediaType: "image/png"
            ),
            bannerImage: MetadataViews.Media(
                file: MetadataViews.IPFSFile(
                    cid: "QmYD8e5s59qYFFQXref1YzyqW1WKYUMPxfqVDEis2s23BF",
                    path: nil
                ),
                mediaType: "image/png"
            ),
            socials: {
                "twitter": MetadataViews.ExternalURL("https://twitter.com/flowty_io")
            }
        )
    )

    let data = NFTMetadata.Metadata(
        name: "Fluid",
        description: "This is a description",
        thumbnail: MetadataViews.IPFSFile(
            cid: "QmWWLhnkPR3ejavNtzeJcdG9fwcBHKwBVEP4pZ9rGbdHEM",
            path: nil
        ),
        traits: nil,
        editions: nil,
        externalURL: nil,
        royalties: nil,
        data: {}
    )

    let params: {String: AnyStruct} = {
        "collectionInfo": collectionInfo,
        "data": data
    }
    deploy("OpenEditionNFT", "../contracts/nft/OpenEditionNFT.cdc", [params, Type<OpenEditionInitializer>().identifier])

    txExecutor("setup/configure_hybrid_custody_filter_and_factory.cdc", [flowtyDropsAccount], [])
}

access(all) fun deploy(_ name: String, _ path: String, _ arguments: [AnyStruct]) {
    let err = Test.deployContract(name: name, path: path, arguments: arguments)
    Test.expect(err, Test.beNil()) 
}

access(all) fun heartbeat() {
    txExecutor("util/heartbeat.cdc", [serviceAccount], [])
}

access(all) fun getCurrentTime(): UFix64 {
    return scriptExecutor("util/get_current_time.cdc", [])! as! UFix64
}

access(all) fun mintFromDrop(
    minter: Test.TestAccount,
    nftTypeIdentifier: String,
    numToMint: Int,
    totalCost: UFix64,
    paymentIdentifier: String,
    paymentStoragePath: StoragePath,
    paymentReceiverPath: PublicPath,
    dropID: UInt64,
    dropPhaseIndex: Int,
    nftIdentifier: String,
    commissionReceiver: Address
) {
    let args = [
        nftTypeIdentifier,
        numToMint,
        totalCost,
        paymentIdentifier,
        paymentStoragePath,
        paymentReceiverPath,
        dropID,
        dropPhaseIndex,
        nftIdentifier,
        commissionReceiver
    ]
    txExecutor("drops/mint.cdc", [minter], args)
}

access(all) fun getDropIDs(
    nftTypeIdentifier: String
): [UInt64] {
    return scriptExecutor("get_drop_ids.cdc", [nftTypeIdentifier])! as! [UInt64]
}

access(all) fun createEndlessOpenEditionDrop(
    acct: Test.TestAccount,
    name: String,
    description: String,
    ipfsCid: String,
    ipfsPath: String?,
    price: UFix64,
    paymentIdentifier: String,
    minterControllerID: UInt64,
    nftTypeIdentifier: String
): UInt64 {
    txExecutor("drops/add_endless_open_edition.cdc", [acct], [
        name, description, ipfsCid, ipfsPath, price, paymentIdentifier, minterControllerID, nftTypeIdentifier
    ])
    
    let e = Test.eventsOfType(Type<FlowtyDrops.DropAdded>()).removeLast() as! FlowtyDrops.DropAdded
    return e.id
}

access(all) fun createTimebasedOpenEditionDrop(
    acct: Test.TestAccount,
    name: String,
    description: String,
    ipfsCid: String,
    ipfsPath: String?,
    price: UFix64,
    paymentIdentifier: String,
    startUnix: UInt64?,
    endUnix: UInt64?,
    minterControllerID: UInt64,
    nftTypeIdentifier: String
): UInt64 {
    txExecutor("drops/add_time_based_open_edition.cdc", [acct], [
        name, description, ipfsCid, ipfsPath, price, paymentIdentifier, startUnix, endUnix, minterControllerID, nftTypeIdentifier
    ])

    let e = Test.eventsOfType(Type<FlowtyDrops.DropAdded>()).removeLast() as! FlowtyDrops.DropAdded
    return e.id
}

access(all) fun sendFlowTokens(fromAccount: Test.TestAccount, toAccount: Test.TestAccount, amount: UFix64) {
    txExecutor("util/send_flow_tokens.cdc", [fromAccount], [toAccount.address, amount])
}

access(all) fun mintFlowTokens(_ acct: Test.TestAccount, _ amount: UFix64) {
    txExecutor("flow-token/mint.cdc", [serviceAccount], [acct.address, amount])
}

access(all) fun flowTokenIdentifier(): String {
    return Type<@FlowToken.Vault>().identifier
}

access(all) fun openEditionNftIdentifier(): String {
    return Type<@OpenEditionNFT.NFT>().identifier
}

access(all) fun hasDropPhaseStarted(nftTypeIdentifier: String, dropID: UInt64, phaseIndex: Int): Bool {
    return scriptExecutor("has_phase_started.cdc", [nftTypeIdentifier, dropID, phaseIndex])! as! Bool
}

access(all) fun hasDropPhaseEnded(nftTypeIdentifier: String, dropID: UInt64, phaseIndex: Int): Bool {
    return scriptExecutor("has_phase_ended.cdc", [nftTypeIdentifier, dropID, phaseIndex])! as! Bool
}

access(all) fun canMintAtPhase(nftTypeIdentifier: String, dropID: UInt64, phaseIndex: Int, minter: Address, numToMint: Int, totalMinted: Int, paymentIdentifier: String): Bool {
    return scriptExecutor("can_mint_at_phase.cdc", [
        nftTypeIdentifier, dropID, phaseIndex, minter, numToMint, totalMinted, paymentIdentifier
    ])! as! Bool
}

access(all) fun getMinterControllerID(acct: Test.TestAccount): UInt64? {
    return scriptExecutor("util/get_minter_controller_id.cdc", [acct.address]) as! UInt64?
}
```