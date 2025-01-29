# Source: https://developers.flow.com/build/guides/mobile/ios-quickstart




IOS Development | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
  + [Create a Fungible Token](/build/guides/fungible-token)
  + [Create an NFT Project](/build/guides/nft)
  + [Account Linking (FLIP 72)](/build/guides/account-linking)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Building on Mobile](/build/guides/mobile/overview)
    - [Overview](/build/guides/mobile/overview)
    - [Build a Walletless Mobile App (PWA)](/build/guides/mobile/walletless-pwa)
    - [IOS Development](/build/guides/mobile/ios-quickstart)
    - [React Native Development](/build/guides/mobile/react-native-quickstart)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Guides
* Building on Mobile
* IOS Development
On this page
# Overview

The following documentation aims to educate you on building a native mobile application on Flow. It first presents Monster Maker, a starter project we’ve built to represent simple Flow mobile concepts. Next it presents various developer resources related to building mobile native Flow applications.

# Monster Maker

![monster_maker_logo.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABEAAAAGQCAYAAACu+RXHAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFw2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4yLWMwMDAgNzkuNTY2ZWJjNWI0LCAyMDIyLzA1LzA5LTA4OjI1OjU1ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjMuNCAoTWFjaW50b3NoKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjItMTEtMDhUMDc6Mjc6NDEtMDg6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDIyLTExLTIyVDEzOjM5OjMyLTA4OjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIyLTExLTIyVDEzOjM5OjMyLTA4OjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0NTU2Njc1Ny02YjM5LTQ1MjMtYWQwNC1lNDllODE5NTZkYmMiIHhtcE1NOkRvY3VtZW50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)

Monster Maker is a native iOS app that allows users to connect a wallet, sign a transaction to mint an NFT (a monster) and display their collection of NFTs (their monsters) within the app. It’s meant to be a lightweight sample project to exemplify how to build a mobile native Flow project. If you’re looking to build a native mobile application for Flow, exploring the Monster Maker code base first or even building off of it is a great way to get started.

👉 ***Note** - We currently only have an iOS project for Monster Maker. That said an Android and web version of the same project is in active development.*

## Github Repo[​](#github-repo "Direct link to Github Repo")

The Monster Maker Github Repo can be found here:

<https://github.com/onflow/monster-maker>

## Building to Device[​](#building-to-device "Direct link to Building to Device")

Before you run Monster Maker on your device, please make sure you have installed the [Xcode14](https://apps.apple.com/au/app/xcode/id497799835?mt=12) from Mac App Store. Once you clone the repo, open the [MonsterMaker.xcodeproj](https://github.com/onflow/monster-maker/tree/main/iOS/MonsterMaker.xcodeproj) under the iOS folder.

Xcode should automatically setup the project for you. If you do see any error related to dependencies, run `Xcode Menu -> File -> Packages -> Reset Package Cache` to resolve the issue.

In the meantime, you can choose a simulator or your iPhone to run. For more detail here is the [official doc](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device).
For run in real device, there are a few steps to deal with signing:

1. Add your apple account to the Xcode which can be accessed from `Xcode Menu -> Settings -> Add account`.
2. Change the Team to your Personal Apple account from the **Signing & Capabilities** under the project target menu. For more detail, please check the screenshot below.
   
   ![XCode Target Setup](/assets/images/xcode_setup-a21fd8b008f0fc0f04d4b8b4355f064a.png)

## Connecting to a Wallet[​](#connecting-to-a-wallet "Direct link to Connecting to a Wallet")

To connect with wallets, there is native wallet discovery in the app. Once you click on connect, it will bring out the list of the wallets which support `HTTP/POST` or `WC/RPC` method.

### FCL Config[​](#fcl-config "Direct link to FCL Config")

To make sure, the wallet can recognise your dApp, there is a few field you will need to config before connect to a wallet. The account proof config is optional. In addition, you will need to create a project id from [walletconnect](https://cloud.walletconnect.com/app) cloud before you can connect to the `WC/RPC` compatible wallet such as dapper self custody or lilico wallet.

 `_29import FCL_29_29// Config the App_29let defaultProvider: FCL.Provider = .dapperPro_29let defaultNetwork: Flow.ChainID = .testnet // or .mainnet_29_29// Optinal: Config for account proof_29let accountProof = FCL.Metadata.AccountProofConfig(appIdentifier: "Monster Maker")_29_29// Config for WC/RPC compatible wallet_29let walletConnect = FCL.Metadata.WalletConnectConfig(urlScheme: "monster-maker://", projectID: "12ed93a2aae83134c4c8473ca97d9399")_29_29// Config basic dApp info_29let metadata = FCL.Metadata(appName: "Monster Maker",_29 appDescription: "Monster Maker Demo App for mobile",_29 appIcon: URL(string: "https://i.imgur.com/jscDmDe.png")!,_29 location: URL(string: "https://monster-maker.vercel.app/")!,_29 accountProof: accountProof,_29 walletConnectConfig: walletConnect)_29fcl.config(metadata: metadata,_29 env: defaultNetwork,_29 provider: defaultProvider)_29_29// Import keywords replacement for cadence query and transaction_29fcl.config_29 .put("0xFungibleToken", value: "0x631e88ae7f1d7c20")_29 .put("0xMonsterMaker", value: "0xfd3d8fe2c8056370")_29 .put("0xMetadataViews", value: "0x631e88ae7f1d7c20")_29 .put("0xTransactionGeneration", value: "0x44051d81c4720882")`
### Open wallet discovery[​](#open-wallet-discovery "Direct link to Open wallet discovery")

![In Monster Maker, the Connect button triggers opening of Wallet Discovery](/assets/images/connect-08ebc29173f26df99bcad8a5249451de.png)

In Monster Maker, the Connect button triggers opening of Wallet Discovery

For the wallet support `HTTP/POST`, it will use webview to show the following actions.

For the wallet support `WC/RPC`, it will use deep-link to the wallet for actions.

You can open the native wallet discovery to make the selection, but also you can connect to the specific wallet as well.

Here is the code snippet of it:

 `_10import FCL_10_10// Open discovery view_10fcl.openDiscovery()_10_10// Or manual connect to specific wallet_10try fcl.changeProvider(provider: provider, env: .testnet)_10try await fcl.authenticate()`
## Signing a Transaction[​](#signing-a-transaction "Direct link to Signing a Transaction")

![In Monster Maker, Initializing the NFT collection with the Initialize button triggers a transaction.](/assets/images/initialize-741f992eddc54e2734901a8fe3954b89.png)

In Monster Maker, Initializing the NFT collection with the Initialize button triggers a transaction.

Similar to what we have on fcl-js, native sdk also use `query` and `mutate` for on-chain interactions. To request a signature from user, you can simply use `fcl.mutate` method. By default, the user will be the payer, proposer and authorizer, if you want to add custom authorizer please refer to the code from [Server](https://github.com/onflow/monster-maker/blob/main/server/pages/api/signAsMinter/index.ts) and [iOS](https://github.com/onflow/monster-maker/blob/main/iOS/MonsterMaker/Flow/MintHelper.swift) end.

 `_23guard let user = fcl.currentUser else {_23 // Not signin_23 return_23}_23_23let txId = try await fcl.mutate(_23 cadence: """_23 transaction(test: String, testInt: Int) {_23 prepare(signer: &Account) {_23 log(signer.address)_23 log(test)_23 log(testInt)_23 }_23 }_23 """,_23 args: [_23 .string("Hello"),_23 .int(10)_23 ],_23 gasLimit: 999,_23 authorizors: [user])_23_23print("txId -> \(txId)")`
## View NFT[​](#view-nft "Direct link to View NFT")

![The View page in Monster Maker exemplifies showing Monster Maker NFTs held by the connected wallet](/assets/images/collection-99cddabc5758e782ca038bb6a6451914.png)

The View page in Monster Maker exemplifies showing Monster Maker NFTs held by the connected wallet

During development, you always can query your NFT with `fcl.query`. Here is an example:

* Query cadence
  
   `_79import NonFungibleToken from 0xNonFungibleToken_79 import MonsterMaker from 0xMonsterMaker_79 import MetadataViews from 0xMetadataViews_79 _79 access(all) struct Monster {_79 access(all) let name: String_79 access(all) let description: String_79 access(all) let thumbnail: String_79 access(all) let itemID: UInt64_79 access(all) let resourceID: UInt64_79 access(all) let owner: Address_79 access(all) let component: MonsterMaker.MonsterComponent_79_79 init(_79 name: String,_79 description: String,_79 thumbnail: String,_79 itemID: UInt64,_79 resourceID: UInt64,_79 owner: Address,_79 component: MonsterMaker.MonsterComponent_79 ) {_79 self.name = name_79 self.description = description_79 self.thumbnail = thumbnail_79 self.itemID = itemID_79 self.resourceID = resourceID_79 self.owner = owner_79 self.component = component_79 }_79 }_79_79 access(all) fun getMonsterById(address: Address, itemID: UInt64): Monster? {_79_79 if let collection = getAccount(address).capabilities.get<&MonsterMaker.Collection>(MonsterMaker.CollectionPublicPath).borrow() {_79 _79 if let item = collection.borrowMonsterMaker(id: itemID) {_79 if let view = item.resolveView(Type<MetadataViews.Display>()) {_79 let display = view as! MetadataViews.Display_79 let owner: Address = item.owner!.address!_79 let thumbnail = display.thumbnail as! MetadataViews.HTTPFile_79_79 return Monster(_79 name: display.name,_79 description: display.description,_79 thumbnail: thumbnail.url,_79 itemID: itemID,_79 resourceID: item.uuid,_79 owner: address,_79 component: item.component_79 )_79 }_79 }_79 }_79_79 return nil_79 }_79_79 access(all) fun main(address: Address): [Monster] {_79 let account = getAccount(address)_79 let collectionRef = account.capabilities.get<&{NonFungibleToken.Collection}>(MonsterMaker.CollectionPublicPath).borrow()_79 ?? panic("The account with address "_79 .concat(address.toString)_79 .concat(" does not have a NonFungibleToken Collection at ")_79 .concat(MonsterMaker.CollectionPublicPath.toString())_79 .concat(". Make sure the account address is correct and is initialized their account with a MonsterMaker Collection!"))_79 _79 let ids = collectionRef.getIDs()_79_79 let monsters : [Monster] = []_79_79 for id in ids {_79 if let monster = getMonsterById(address: address, itemID: id) {_79 monsters.append(monster)_79 }_79 }_79_79 return monsters_79 }`

 `_10let nftList = try await fcl.query(script: cadenceScript, _10 args: [.address(address)])_10 .decode([NFTModel].self)`
# External Resources

**FCL Swift**

FCL Swift is the iOS native SDK for FCL. This SDK is integrated into the Monster Maker sample.

<https://github.com/Outblock/fcl-swift>

**FCL Android**

FCL Android is the Android native SDK for FCL.

<https://github.com/Outblock/fcl-android>

**FCL Wallet Connect 2.0**

One of the easiest ways to connect to a wallet via a mobile native dApp is through Flow’s new support for Wallet Connect 2.0. This is the pattern that Monster Maker uses to connect to the Dapper Self Custody wallet and Lilico. For more information on FCL Wallet Connect 2.0, check out this page:

[FCL Wallet Connect](/tools/clients/fcl-js/wallet-connect)

**How to Build a Native iOS Dapp**

The Agile Monkeys has written a very comprehensive guide on how to build a native mobile application on iOS and interface with fcl-swift. Found here:

[How to Build a Native iOS Dapper](https://dev.to/theagilemonkeys/how-to-buid-a-native-ios-dapp-that-uses-the-flow-blockchain-as-the-backend-n9k)
[Source Code](https://github.com/jfsagasti/FlowNotes)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/mobile/ios-quickstart.md)Last updated on **Jan 10, 2025** by **Ali Serag**[PreviousBuild a Walletless Mobile App (PWA)](/build/guides/mobile/walletless-pwa)[NextReact Native Development](/build/guides/mobile/react-native-quickstart)
###### Rate this page

😞😐😊

* [Github Repo](#github-repo)
* [Building to Device](#building-to-device)
* [Connecting to a Wallet](#connecting-to-a-wallet)
  + [FCL Config](#fcl-config)
  + [Open wallet discovery](#open-wallet-discovery)
* [Signing a Transaction](#signing-a-transaction)
* [View NFT](#view-nft)
Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)
Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)
Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)
Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)
More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)
Copyright © 2025 Flow, Inc. Built with Docusaurus.

