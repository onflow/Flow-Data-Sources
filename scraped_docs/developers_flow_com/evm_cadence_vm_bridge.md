# Source: https://developers.flow.com/evm/cadence/vm-bridge




Cross-VM Bridge | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using EVM](/evm/using)
* [Networks](/evm/networks)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Data Indexers](/evm/data-indexers)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)
* [Clients](/evm/clients/ethers)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)
  + [Interacting with COAs](/evm/cadence/interacting-with-coa)
  + [Direct Calls to Flow EVM](/evm/cadence/direct-calls)
  + [Batched EVM Transactions](/evm/cadence/batched-evm-transactions)
  + [Cross-VM Bridge](/evm/cadence/vm-bridge)


* Using EVM with Cadence
* Cross-VM Bridge
On this page
# Cross-VM Bridge

Flow provides the [Cross-VM Bridge](https://www.github.com/onflow/flow-evm-bridge) which enables the movement of
fungible and non-fungible tokens between Cadence & EVM. The Cross-VM Bridge is a contract-based protocol enabling the
automated and atomic bridging of tokens from Cadence into EVM with their corresponding ERC-20 and ERC-721 token types.
In the opposite direction, it supports bridging of arbitrary ERC-20 and ERC-721 tokens from EVM to Cadence as their
corresponding FT or NFT token types.

The Cross-VM Bridge internalizes the capabilities to deploy new token contracts in either VM state as needed, resolving
access to, and maintaining links between associated contracts. It additionally automates account and contract calls to
enforce source VM asset burn or lock, and target VM token mint or unlock.

Developers wishing to use the Cross-VM Bridge will be required to use a Cadence transaction. Cross-VM bridging
functionality is not currently available natively in EVM on Flow. By extension, this means that the EVM account bridging
from EVM to Cadence must be a [`CadenceOwnedAccount` (COA)](/evm/cadence/interacting-with-coa) as this is the only EVM account
type that can be controlled from the Cadence runtime.

This [FLIP](https://github.com/onflow/flips/pull/233) outlines the architecture and implementation of the VM bridge.
This document will focus on how to use the Cross-VM Bridge and considerations for fungible and non-fungible token
projects deploying to either Cadence or EVM.

## Deployments[​](#deployments "Direct link to Deployments")

The core bridge contracts can be found at the following addresses:

| Contracts | Testnet | Mainnet |
| --- | --- | --- |
| All Cadence Bridge contracts | [`0xdfc20aee650fcbdf`](https://contractbrowser.com/account/0xdfc20aee650fcbdf/contracts) | [`0x1e4aa0b87d10b141`](https://contractbrowser.com/account/0x1e4aa0b87d10b141/contracts) |
| `FlowEVMBridgeFactory.sol` | [`0xf8146b4aef631853f0eb98dbe28706d029e52c52`](https://evm-testnet.flowscan.io/address/0xF8146B4aEF631853F0eB98DBE28706d029e52c52) | [`0x1c6dea788ee774cf15bcd3d7a07ede892ef0be40`](https://evm.flowscan.io/address/0x1C6dEa788Ee774CF15bCd3d7A07ede892ef0bE40) |
| `FlowEVMBridgeDeploymentRegistry.sol` | [`0x8781d15904d7e161f421400571dea24cc0db6938`](https://evm-testnet.flowscan.io/address/0x8781d15904d7e161f421400571dea24cc0db6938) | [`0x8fdec2058535a2cb25c2f8cec65e8e0d0691f7b0`](https://evm.flowscan.io/address/0x8FDEc2058535A2Cb25C2f8ceC65e8e0D0691f7B0) |
| `FlowEVMBridgedERC20Deployer.sol` | [`0x4d45CaD104A71D19991DE3489ddC5C7B284cf263`](https://evm-testnet.flowscan.io/address/0x4d45CaD104A71D19991DE3489ddC5C7B284cf263) | [`0x49631Eac7e67c417D036a4d114AD9359c93491e7`](https://evm.flowscan.io/address/0x49631Eac7e67c417D036a4d114AD9359c93491e7) |
| `FlowEVMBridgedERC721Deployer.sol` | [`0x1B852d242F9c4C4E9Bb91115276f659D1D1f7c56`](https://evm-testnet.flowscan.io/address/0x1B852d242F9c4C4E9Bb91115276f659D1D1f7c56) | [`0xe7c2B80a9de81340AE375B3a53940E9aeEAd79Df`](https://evm.flowscan.io/address/0xe7c2B80a9de81340AE375B3a53940E9aeEAd79Df) |

And below are the bridge escrow's EVM addresses. These addresses are COAs and are stored stored in the same Flow account
as you'll find the Cadence contracts (see above).

| Network | Address |
| --- | --- |
| Testnet | [`0x0000000000000000000000023f946ffbc8829bfd`](https://evm-testnet.flowscan.io/address/0x0000000000000000000000023f946FFbc8829BFD) |
| Mainnet | [`0x00000000000000000000000249250a5c27ecab3b`](https://evm.flowscan.io/address/0x00000000000000000000000249250a5C27Ecab3B) |

## Interacting With the Bridge[​](#interacting-with-the-bridge "Direct link to Interacting With the Bridge")

info

All bridging activity in either direction is orchestrated via Cadence on COA EVM accounts. This means that all bridging
activity must be initiated via a Cadence transaction, not an EVM transaction regardless of the directionality of the
bridge request. For more information on the interplay between Cadence and EVM, see [How EVM on Flow
Works](/evm/how-it-works).

### Overview[​](#overview "Direct link to Overview")

The Flow EVM bridge allows both fungible and non-fungible tokens to move atomically between Cadence and EVM. In the
context of EVM, fungible tokens are defined as ERC20 tokens, and non-fungible tokens as ERC721 tokens. In Cadence,
fungible tokens are defined by contracts implementing
[the `FungibleToken` interface](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc)
and non-fungible tokens implement
[the `NonFungibleToken` interface](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc).

Like all operations on Flow, there are native fees associated with both computation and storage. To prevent spam and
sustain the bridge account's storage consumption, fees are charged for both onboarding assets and bridging assets. In
the case where storage consumption is expected, fees are charged based on the storage consumed at the current network
storage rate.

### Onboarding[​](#onboarding "Direct link to Onboarding")

Since a contract must define the asset in the target VM, an asset must be "onboarded" to the bridge before requests can
be fulfilled.

Moving from Cadence to EVM, onboarding can occur on the fly, deploying a template contract in the same transaction as
the asset is bridged to EVM if the transaction so specifies.

Moving from EVM to Cadence, however, requires that onboarding occur in a separate transaction due to the fact that a
Cadence contract is initialized at the end of a transaction and isn't available in the runtime until after the
transaction has executed.

Below are transactions relevant to onboarding assets:

onboard\_by\_type.cdconboard\_by\_type.cdc `_56import "FungibleToken"_56import "FlowToken"_56_56import "ScopedFTProviders"_56_56import "EVM"_56_56import "FlowEVMBridge"_56import "FlowEVMBridgeConfig"_56_56/// This transaction onboards the asset type to the bridge, configuring the bridge to move assets between environments_56/// NOTE: This must be done before bridging a Cadence-native asset to EVM_56///_56/// @param type: The Cadence type of the bridgeable asset to onboard to the bridge_56///_56transaction(type: Type) {_56_56 let scopedProvider: @ScopedFTProviders.ScopedFTProvider_56 _56 prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_56_56 /* --- Configure a ScopedFTProvider --- */_56 //_56 // Issue and store bridge-dedicated Provider Capability in storage if necessary_56 if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {_56 let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(_56 /storage/flowTokenVault_56 )_56 signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)_56 }_56 // Copy the stored Provider capability and create a ScopedFTProvider_56 let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(_56 from: FlowEVMBridgeConfig.providerCapabilityStoragePath_56 ) ?? panic("Invalid Provider Capability found in storage.")_56 let providerFilter = ScopedFTProviders.AllowanceFilter(FlowEVMBridgeConfig.onboardFee)_56 self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(_56 provider: providerCapCopy,_56 filters: [ providerFilter ],_56 expiration: getCurrentBlock().timestamp + 1.0_56 )_56 }_56_56 execute {_56 // Onboard the asset Type_56 FlowEVMBridge.onboardByType(_56 type,_56 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_56 )_56 destroy self.scopedProvider_56 }_56_56 post {_56 FlowEVMBridge.typeRequiresOnboarding(type) == false:_56 "Asset ".concat(type.identifier).concat(" was not onboarded to the bridge.")_56 }_56}`
onboard\_by\_evm\_address.cdconboard\_by\_evm\_address.cdc `_55import "FungibleToken"_55import "FlowToken"_55_55import "ScopedFTProviders"_55_55import "EVM"_55_55import "FlowEVMBridge"_55import "FlowEVMBridgeConfig"_55_55/// This transaction onboards the NFT type to the bridge, configuring the bridge to move NFTs between environments_55/// NOTE: This must be done before bridging a Cadence-native NFT to EVM_55///_55/// @param contractAddressHex: The EVM address of the contract defining the bridgeable asset to be onboarded_55///_55transaction(contractAddressHex: String) {_55_55 let contractAddress: EVM.EVMAddress_55 let scopedProvider: @ScopedFTProviders.ScopedFTProvider_55 _55 prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_55 /* --- Construct EVMAddress from hex string (no leading `"0x"`) --- */_55 //_55 self.contractAddress = EVM.addressFromString(contractAddressHex)_55_55 /* --- Configure a ScopedFTProvider --- */_55 //_55 // Issue and store bridge-dedicated Provider Capability in storage if necessary_55 if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {_55 let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(_55 /storage/flowTokenVault_55 )_55 signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)_55 }_55 // Copy the stored Provider capability and create a ScopedFTProvider_55 let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(_55 from: FlowEVMBridgeConfig.providerCapabilityStoragePath_55 ) ?? panic("Invalid Provider Capability found in storage.")_55 let providerFilter = ScopedFTProviders.AllowanceFilter(FlowEVMBridgeConfig.onboardFee)_55 self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(_55 provider: providerCapCopy,_55 filters: [ providerFilter ],_55 expiration: getCurrentBlock().timestamp + 1.0_55 )_55 }_55_55 execute {_55 // Onboard the EVM contract_55 FlowEVMBridge.onboardByEVMAddress(_55 self.contractAddress,_55 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_55 )_55 destroy self.scopedProvider_55 }_55}`
### Bridging[​](#bridging "Direct link to Bridging")

Once an asset has been onboarded, either by its Cadence type or EVM contract address, it can be bridged in either
direction, referred to by its Cadence type. For Cadence-native assets, this is simply its native type. For EVM-native
assets, this is in most cases a templated Cadence contract deployed to the bridge account, the name of which is derived
from the EVM contract address. For instance, an ERC721 contract at address `0x1234` would be onboarded to the bridge as
`EVMVMBridgedNFT_0x1234`, making its type identifier `A.<BRIDGE_ADDRESS>.EVMVMBridgedNFT_0x1234.NFT`.

To get the type identifier for a given NFT, you can use the following code:

 `_10// Where `nft` is either a @{NonFungibleToken.NFT} or &{NonFungibleToken.NFT}_10nft.getType().identifier`

You may also retrieve the type associated with a given EVM contract address using the following script:

get\_associated\_type.cdcget\_associated\_type.cdc `_16import "EVM"_16_16import "FlowEVMBridgeConfig"_16_16/// Returns the Cadence Type associated with the given EVM address (as its hex String)_16///_16/// @param evmAddressHex: The hex-encoded address of the EVM contract as a String_16///_16/// @return The Cadence Type associated with the EVM address or nil if the address is not onboarded. `nil` may also be_16/// returned if the address is not a valid EVM address._16///_16access(all)_16fun main(addressHex: String): Type? {_16 let address = EVM.addressFromString(addressHex)_16 return FlowEVMBridgeConfig.getTypeAssociated(with: address)_16}`

Alternatively, given some onboarded Cadence type, you can retrieve the associated EVM address using the following
script:

get\_associated\_address.cdcget\_associated\_address.cdc `_19import "EVM"_19_19import "FlowEVMBridgeConfig"_19_19/// Returns the EVM address associated with the given Cadence type (as its identifier String)_19///_19/// @param typeIdentifier: The Cadence type identifier String_19///_19/// @return The EVM address as a hex string if the type has an associated EVMAddress, otherwise nil_19///_19access(all)_19fun main(identifier: String): String? {_19 if let type = CompositeType(identifier) {_19 if let address = FlowEVMBridgeConfig.getEVMAddressAssociated(with: type) {_19 return address.toString()_19 }_19 }_19 return nil_19}`
#### NFTs[​](#nfts "Direct link to NFTs")

Any Cadence NFTs bridging to EVM are escrowed in the bridge account and either minted in a bridge-deployed ERC721
contract or transferred from escrow to the calling COA in EVM. On the return trip, NFTs are escrowed in EVM - owned by
the bridge's COA - and either unlocked from escrow if locked or minted from a bridge-owned NFT contract.

Below are transactions relevant to bridging NFTs:

bridge\_nft\_to\_evm.cdcbridge\_nft\_to\_evm.cdc `_122import "FungibleToken"_122import "NonFungibleToken"_122import "ViewResolver"_122import "MetadataViews"_122import "FlowToken"_122_122import "ScopedFTProviders"_122_122import "EVM"_122_122import "FlowEVMBridge"_122import "FlowEVMBridgeConfig"_122import "FlowEVMBridgeUtils"_122_122/// Bridges an NFT from the signer's collection in Cadence to the signer's COA in FlowEVM_122///_122/// NOTE: This transaction also onboards the NFT to the bridge if necessary which may incur additional fees_122/// than bridging an asset that has already been onboarded._122///_122/// @param nftIdentifier: The Cadence type identifier of the NFT to bridge - e.g. nft.getType().identifier_122/// @param id: The Cadence NFT.id of the NFT to bridge to EVM_122///_122transaction(nftIdentifier: String, id: UInt64) {_122 _122 let nft: @{NonFungibleToken.NFT}_122 let coa: auth(EVM.Bridge) &EVM.CadenceOwnedAccount_122 let requiresOnboarding: Bool_122 let scopedProvider: @ScopedFTProviders.ScopedFTProvider_122 _122 prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_122 /* --- Reference the signer's CadenceOwnedAccount --- */_122 //_122 // Borrow a reference to the signer's COA_122 self.coa = signer.storage.borrow<auth(EVM.Bridge) &EVM.CadenceOwnedAccount>(from: /storage/evm)_122 ?? panic("Could not borrow COA signer's account at path /storage/evm")_122 _122 /* --- Construct the NFT type --- */_122 //_122 // Construct the NFT type from the provided identifier_122 let nftType = CompositeType(nftIdentifier)_122 ?? panic("Could not construct NFT type from identifier: ".concat(nftIdentifier))_122 // Parse the NFT identifier into its components_122 let nftContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: nftType)_122 ?? panic("Could not get contract address from identifier: ".concat(nftIdentifier))_122 let nftContractName = FlowEVMBridgeUtils.getContractName(fromType: nftType)_122 ?? panic("Could not get contract name from identifier: ".concat(nftIdentifier))_122_122 /* --- Retrieve the NFT --- */_122 //_122 // Borrow a reference to the NFT collection, configuring if necessary_122 let viewResolver = getAccount(nftContractAddress).contracts.borrow<&{ViewResolver}>(name: nftContractName)_122 ?? panic("Could not borrow ViewResolver from NFT contract with name "_122 .concat(nftContractName).concat(" and address ")_122 .concat(nftContractAddress.toString()))_122 let collectionData = viewResolver.resolveContractView(_122 resourceType: nftType,_122 viewType: Type<MetadataViews.NFTCollectionData>()_122 ) as! MetadataViews.NFTCollectionData?_122 ?? panic("Could not resolve NFTCollectionData view for NFT type ".concat(nftType.identifier))_122 let collection = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(_122 from: collectionData.storagePath_122 ) ?? panic("Could not borrow a NonFungibleToken Collection from the signer's storage path "_122 .concat(collectionData.storagePath.toString()))_122_122 // Withdraw the requested NFT & set a cap on the withdrawable bridge fee_122 self.nft <- collection.withdraw(withdrawID: id)_122 var approxFee = FlowEVMBridgeUtils.calculateBridgeFee(_122 bytes: 400_000 // 400 kB as upper bound on movable storage used in a single transaction_122 )_122 // Determine if the NFT requires onboarding - this impacts the fee required_122 self.requiresOnboarding = FlowEVMBridge.typeRequiresOnboarding(self.nft.getType())_122 ?? panic("Bridge does not support the requested asset type ".concat(nftIdentifier))_122 // Add the onboarding fee if onboarding is necessary_122 if self.requiresOnboarding {_122 approxFee = approxFee + FlowEVMBridgeConfig.onboardFee_122 }_122_122 /* --- Configure a ScopedFTProvider --- */_122 //_122 // Issue and store bridge-dedicated Provider Capability in storage if necessary_122 if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {_122 let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(_122 /storage/flowTokenVault_122 )_122 signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)_122 }_122 // Copy the stored Provider capability and create a ScopedFTProvider_122 let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(_122 from: FlowEVMBridgeConfig.providerCapabilityStoragePath_122 ) ?? panic("Invalid FungibleToken Provider Capability found in storage at path "_122 .concat(FlowEVMBridgeConfig.providerCapabilityStoragePath.toString()))_122 let providerFilter = ScopedFTProviders.AllowanceFilter(approxFee)_122 self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(_122 provider: providerCapCopy,_122 filters: [ providerFilter ],_122 expiration: getCurrentBlock().timestamp + 1.0_122 )_122 }_122_122 pre {_122 self.nft.getType().identifier == nftIdentifier:_122 "Attempting to send invalid nft type - requested: ".concat(nftIdentifier)_122 .concat(", sending: ").concat(self.nft.getType().identifier)_122 }_122_122 execute {_122 if self.requiresOnboarding {_122 // Onboard the NFT to the bridge_122 FlowEVMBridge.onboardByType(_122 self.nft.getType(),_122 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_122 )_122 }_122 // Execute the bridge_122 self.coa.depositNFT(_122 nft: <-self.nft,_122 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_122 )_122 // Destroy the ScopedFTProvider_122 destroy self.scopedProvider_122 }_122}`
bridge\_nft\_from\_evm.cdcbridge\_nft\_from\_evm.cdc `_113import "FungibleToken"_113import "NonFungibleToken"_113import "ViewResolver"_113import "MetadataViews"_113import "FlowToken"_113_113import "ScopedFTProviders"_113_113import "EVM"_113_113import "FlowEVMBridge"_113import "FlowEVMBridgeConfig"_113import "FlowEVMBridgeUtils"_113_113/// This transaction bridges an NFT from EVM to Cadence assuming it has already been onboarded to the FlowEVMBridge_113/// NOTE: The ERC721 must have first been onboarded to the bridge. This can be checked via the method_113/// FlowEVMBridge.evmAddressRequiresOnboarding(address: self.evmContractAddress)_113///_113/// @param nftIdentifier: The Cadence type identifier of the NFT to bridge - e.g. nft.getType().identifier_113/// @param id: The ERC721 id of the NFT to bridge to Cadence from EVM_113///_113transaction(nftIdentifier: String, id: UInt256) {_113_113 let nftType: Type_113 let collection: &{NonFungibleToken.Collection}_113 let scopedProvider: @ScopedFTProviders.ScopedFTProvider_113 let coa: auth(EVM.Bridge) &EVM.CadenceOwnedAccount_113 _113 prepare(signer: auth(BorrowValue, CopyValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {_113 /* --- Reference the signer's CadenceOwnedAccount --- */_113 //_113 // Borrow a reference to the signer's COA_113 self.coa = signer.storage.borrow<auth(EVM.Bridge) &EVM.CadenceOwnedAccount>(from: /storage/evm)_113 ?? panic("Could not borrow COA signer's account at path /storage/evm")_113_113 /* --- Construct the NFT type --- */_113 //_113 // Construct the NFT type from the provided identifier_113 self.nftType = CompositeType(nftIdentifier)_113 ?? panic("Could not construct NFT type from identifier: ".concat(nftIdentifier))_113 // Parse the NFT identifier into its components_113 let nftContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: self.nftType)_113 ?? panic("Could not get contract address from identifier: ".concat(nftIdentifier))_113 let nftContractName = FlowEVMBridgeUtils.getContractName(fromType: self.nftType)_113 ?? panic("Could not get contract name from identifier: ".concat(nftIdentifier))_113_113 /* --- Reference the signer's NFT Collection --- */_113 //_113 // Borrow a reference to the NFT collection, configuring if necessary_113 let viewResolver = getAccount(nftContractAddress).contracts.borrow<&{ViewResolver}>(name: nftContractName)_113 ?? panic("Could not borrow ViewResolver from NFT contract with name "_113 .concat(nftContractName).concat(" and address ")_113 .concat(nftContractAddress.toString()))_113 let collectionData = viewResolver.resolveContractView(_113 resourceType: self.nftType,_113 viewType: Type<MetadataViews.NFTCollectionData>()_113 ) as! MetadataViews.NFTCollectionData?_113 ?? panic("Could not resolve NFTCollectionData view for NFT type ".concat(self.nftType.identifier))_113 if signer.storage.borrow<&{NonFungibleToken.Collection}>(from: collectionData.storagePath) == nil {_113 signer.storage.save(<-collectionData.createEmptyCollection(), to: collectionData.storagePath)_113 signer.capabilities.unpublish(collectionData.publicPath)_113 let collectionCap = signer.capabilities.storage.issue<&{NonFungibleToken.Collection}>(collectionData.storagePath)_113 signer.capabilities.publish(collectionCap, at: collectionData.publicPath)_113 }_113 self.collection = signer.storage.borrow<&{NonFungibleToken.Collection}>(from: collectionData.storagePath)_113 ?? panic("Could not borrow a NonFungibleToken Collection from the signer's storage path "_113 .concat(collectionData.storagePath.toString()))_113_113 /* --- Configure a ScopedFTProvider --- */_113 //_113 // Set a cap on the withdrawable bridge fee_113 var approxFee = FlowEVMBridgeUtils.calculateBridgeFee(_113 bytes: 400_000 // 400 kB as upper bound on movable storage used in a single transaction_113 )_113 // Issue and store bridge-dedicated Provider Capability in storage if necessary_113 if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {_113 let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(_113 /storage/flowTokenVault_113 )_113 signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)_113 }_113 // Copy the stored Provider capability and create a ScopedFTProvider_113 let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(_113 from: FlowEVMBridgeConfig.providerCapabilityStoragePath_113 ) ?? panic("Invalid FungibleToken Provider Capability found in storage at path "_113 .concat(FlowEVMBridgeConfig.providerCapabilityStoragePath.toString()))_113 let providerFilter = ScopedFTProviders.AllowanceFilter(approxFee)_113 self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(_113 provider: providerCapCopy,_113 filters: [ providerFilter ],_113 expiration: getCurrentBlock().timestamp + 1.0_113 )_113 }_113_113 execute {_113 // Execute the bridge_113 let nft: @{NonFungibleToken.NFT} <- self.coa.withdrawNFT(_113 type: self.nftType,_113 id: id,_113 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_113 )_113 // Ensure the bridged nft is the correct type_113 assert(_113 nft.getType() == self.nftType,_113 message: "Bridged nft type mismatch - requested: ".concat(self.nftType.identifier)_113 .concat(", received: ").concat(nft.getType().identifier)_113 )_113 // Deposit the bridged NFT into the signer's collection_113 self.collection.deposit(token: <-nft)_113 // Destroy the ScopedFTProvider_113 destroy self.scopedProvider_113 }_113}`
#### Fungible Tokens[​](#fungible-tokens "Direct link to Fungible Tokens")

Any Cadence fungible tokens bridging to EVM are escrowed in the bridge account only if they are Cadence-native. If the
bridge defines the tokens, they are burned. On the return trip the pattern is similar, with the bridge burning
bridge-defined tokens or escrowing them if they are EVM-native. In all cases, if the bridge has authority to mint on one
side, it must escrow on the other as the native VM contract is owned by an external party.

With fungible tokens in particular, there may be some cases where the Cadence contract is not deployed to the bridge
account, but the bridge still follows a mint/burn pattern in Cadence. These cases are handled via
[`TokenHandler`](https://github.com/onflow/flow-evm-bridge/blob/main/cadence/contracts/bridge/interfaces/FlowEVMBridgeHandlerInterfaces.cdc)
implementations. Also know that moving $FLOW to EVM is built into the `EVMAddress` object so any requests bridging $FLOW
to EVM will simply leverage this interface; however, moving $FLOW from EVM to Cadence must be done through the COA
resource.

Below are transactions relevant to bridging fungible tokens:

bridge\_tokens\_to\_evm.cdcbridge\_tokens\_to\_evm.cdc `_120import "FungibleToken"_120import "ViewResolver"_120import "FungibleTokenMetadataViews"_120import "FlowToken"_120_120import "ScopedFTProviders"_120_120import "EVM"_120_120import "FlowEVMBridge"_120import "FlowEVMBridgeConfig"_120import "FlowEVMBridgeUtils"_120_120/// Bridges a Vault from the signer's storage to the signer's COA in EVM.Account._120///_120/// NOTE: This transaction also onboards the Vault to the bridge if necessary which may incur additional fees_120/// than bridging an asset that has already been onboarded._120///_120/// @param vaultIdentifier: The Cadence type identifier of the FungibleToken Vault to bridge_120/// - e.g. vault.getType().identifier_120/// @param amount: The amount of tokens to bridge from EVM_120///_120transaction(vaultIdentifier: String, amount: UFix64) {_120_120 let sentVault: @{FungibleToken.Vault}_120 let coa: auth(EVM.Bridge) &EVM.CadenceOwnedAccount_120 let requiresOnboarding: Bool_120 let scopedProvider: @ScopedFTProviders.ScopedFTProvider_120_120 prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_120 /* --- Reference the signer's CadenceOwnedAccount --- */_120 //_120 // Borrow a reference to the signer's COA_120 self.coa = signer.storage.borrow<auth(EVM.Bridge) &EVM.CadenceOwnedAccount>(from: /storage/evm)_120 ?? panic("Could not borrow COA signer's account at path /storage/evm")_120_120 /* --- Construct the Vault type --- */_120 //_120 // Construct the Vault type from the provided identifier_120 let vaultType = CompositeType(vaultIdentifier)_120 ?? panic("Could not construct Vault type from identifier: ".concat(vaultIdentifier))_120 // Parse the Vault identifier into its components_120 let tokenContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: vaultType)_120 ?? panic("Could not get contract address from identifier: ".concat(vaultIdentifier))_120 let tokenContractName = FlowEVMBridgeUtils.getContractName(fromType: vaultType)_120 ?? panic("Could not get contract name from identifier: ".concat(vaultIdentifier))_120_120 /* --- Retrieve the funds --- */_120 //_120 // Borrow a reference to the FungibleToken Vault_120 let viewResolver = getAccount(tokenContractAddress).contracts.borrow<&{ViewResolver}>(name: tokenContractName)_120 ?? panic("Could not borrow ViewResolver from FungibleToken contract with name"_120 .concat(tokenContractName).concat(" and address ")_120 .concat(tokenContractAddress.toString()))_120 let vaultData = viewResolver.resolveContractView(_120 resourceType: vaultType,_120 viewType: Type<FungibleTokenMetadataViews.FTVaultData>()_120 ) as! FungibleTokenMetadataViews.FTVaultData?_120 ?? panic("Could not resolve FTVaultData view for Vault type ".concat(vaultType.identifier))_120 let vault = signer.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(_120 from: vaultData.storagePath_120 ) ?? panic("Could not borrow FungibleToken Vault from storage path ".concat(vaultData.storagePath.toString()))_120_120 // Withdraw the requested balance & set a cap on the withdrawable bridge fee_120 self.sentVault <- vault.withdraw(amount: amount)_120 var approxFee = FlowEVMBridgeUtils.calculateBridgeFee(_120 bytes: 400_000 // 400 kB as upper bound on movable storage used in a single transaction_120 )_120 // Determine if the Vault requires onboarding - this impacts the fee required_120 self.requiresOnboarding = FlowEVMBridge.typeRequiresOnboarding(self.sentVault.getType())_120 ?? panic("Bridge does not support the requested asset type ".concat(vaultIdentifier))_120 if self.requiresOnboarding {_120 approxFee = approxFee + FlowEVMBridgeConfig.onboardFee_120 }_120_120 /* --- Configure a ScopedFTProvider --- */_120 //_120 // Issue and store bridge-dedicated Provider Capability in storage if necessary_120 if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {_120 let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(_120 /storage/flowTokenVault_120 )_120 signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)_120 }_120 // Copy the stored Provider capability and create a ScopedFTProvider_120 let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(_120 from: FlowEVMBridgeConfig.providerCapabilityStoragePath_120 ) ?? panic("Invalid FungibleToken Provider Capability found in storage at path "_120 .concat(FlowEVMBridgeConfig.providerCapabilityStoragePath.toString()))_120 let providerFilter = ScopedFTProviders.AllowanceFilter(approxFee)_120 self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(_120 provider: providerCapCopy,_120 filters: [ providerFilter ],_120 expiration: getCurrentBlock().timestamp + 1.0_120 )_120 }_120_120 pre {_120 self.sentVault.getType().identifier == vaultIdentifier:_120 "Attempting to send invalid vault type - requested: ".concat(vaultIdentifier)_120 .concat(", sending: ").concat(self.sentVault.getType().identifier)_120 }_120_120 execute {_120 if self.requiresOnboarding {_120 // Onboard the Vault to the bridge_120 FlowEVMBridge.onboardByType(_120 self.sentVault.getType(),_120 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_120 )_120 }_120 // Execute the bridge_120 self.coa.depositTokens(_120 vault: <-self.sentVault,_120 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_120 )_120 // Destroy the ScopedFTProvider_120 destroy self.scopedProvider_120 }_120}`
bridge\_tokens\_from\_evm.cdcbridge\_tokens\_from\_evm.cdc `_122import "FungibleToken"_122import "FungibleTokenMetadataViews"_122import "ViewResolver"_122import "MetadataViews"_122import "FlowToken"_122_122import "ScopedFTProviders"_122_122import "EVM"_122_122import "FlowEVMBridge"_122import "FlowEVMBridgeConfig"_122import "FlowEVMBridgeUtils"_122_122/// This transaction bridges fungible tokens from EVM to Cadence assuming it has already been onboarded to the_122/// FlowEVMBridge._122///_122/// NOTE: The ERC20 must have first been onboarded to the bridge. This can be checked via the method_122/// FlowEVMBridge.evmAddressRequiresOnboarding(address: self.evmContractAddress)_122///_122/// @param vaultIdentifier: The Cadence type identifier of the FungibleToken Vault to bridge_122/// - e.g. vault.getType().identifier_122/// @param amount: The amount of tokens to bridge from EVM_122///_122transaction(vaultIdentifier: String, amount: UInt256) {_122_122 let vaultType: Type_122 let receiver: &{FungibleToken.Vault}_122 let scopedProvider: @ScopedFTProviders.ScopedFTProvider_122 let coa: auth(EVM.Bridge) &EVM.CadenceOwnedAccount_122_122 prepare(signer: auth(BorrowValue, CopyValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {_122 /* --- Reference the signer's CadenceOwnedAccount --- */_122 //_122 // Borrow a reference to the signer's COA_122 self.coa = signer.storage.borrow<auth(EVM.Bridge) &EVM.CadenceOwnedAccount>(from: /storage/evm)_122 ?? panic("Could not borrow COA signer's account at path /storage/evm")_122_122 /* --- Construct the Vault type --- */_122 //_122 // Construct the Vault type from the provided identifier_122 self.vaultType = CompositeType(vaultIdentifier)_122 ?? panic("Could not construct Vault type from identifier: ".concat(vaultIdentifier))_122 // Parse the Vault identifier into its components_122 let tokenContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: self.vaultType)_122 ?? panic("Could not get contract address from identifier: ".concat(vaultIdentifier))_122 let tokenContractName = FlowEVMBridgeUtils.getContractName(fromType: self.vaultType)_122 ?? panic("Could not get contract name from identifier: ".concat(vaultIdentifier))_122_122 /* --- Reference the signer's Vault --- */_122 //_122 // Borrow a reference to the FungibleToken Vault, configuring if necessary_122 let viewResolver = getAccount(tokenContractAddress).contracts.borrow<&{ViewResolver}>(name: tokenContractName)_122 ?? panic("Could not borrow ViewResolver from FungibleToken contract with name"_122 .concat(tokenContractName).concat(" and address ")_122 .concat(tokenContractAddress.toString()))_122 let vaultData = viewResolver.resolveContractView(_122 resourceType: self.vaultType,_122 viewType: Type<FungibleTokenMetadataViews.FTVaultData>()_122 ) as! FungibleTokenMetadataViews.FTVaultData?_122 ?? panic("Could not resolve FTVaultData view for Vault type ".concat(self.vaultType.identifier))_122 // If the vault does not exist, create it and publish according to the contract's defined configuration_122 if signer.storage.borrow<&{FungibleToken.Vault}>(from: vaultData.storagePath) == nil {_122 signer.storage.save(<-vaultData.createEmptyVault(), to: vaultData.storagePath)_122_122 signer.capabilities.unpublish(vaultData.receiverPath)_122 signer.capabilities.unpublish(vaultData.metadataPath)_122_122 let receiverCap = signer.capabilities.storage.issue<&{FungibleToken.Vault}>(vaultData.storagePath)_122 let metadataCap = signer.capabilities.storage.issue<&{FungibleToken.Vault}>(vaultData.storagePath)_122_122 signer.capabilities.publish(receiverCap, at: vaultData.receiverPath)_122 signer.capabilities.publish(metadataCap, at: vaultData.metadataPath)_122 }_122 self.receiver = signer.storage.borrow<&{FungibleToken.Vault}>(from: vaultData.storagePath)_122 ?? panic("Could not borrow FungibleToken Vault from storage path ".concat(vaultData.storagePath.toString()))_122_122 /* --- Configure a ScopedFTProvider --- */_122 //_122 // Set a cap on the withdrawable bridge fee_122 var approxFee = FlowEVMBridgeUtils.calculateBridgeFee(_122 bytes: 400_000 // 400 kB as upper bound on movable storage used in a single transaction_122 )_122 // Issue and store bridge-dedicated Provider Capability in storage if necessary_122 if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {_122 let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(_122 /storage/flowTokenVault_122 )_122 signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)_122 }_122 // Copy the stored Provider capability and create a ScopedFTProvider_122 let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(_122 from: FlowEVMBridgeConfig.providerCapabilityStoragePath_122 ) ?? panic("Invalid FungibleToken Provider Capability found in storage at path "_122 .concat(FlowEVMBridgeConfig.providerCapabilityStoragePath.toString()))_122 let providerFilter = ScopedFTProviders.AllowanceFilter(approxFee)_122 self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(_122 provider: providerCapCopy,_122 filters: [ providerFilter ],_122 expiration: getCurrentBlock().timestamp + 1.0_122 )_122 }_122_122 execute {_122 // Execute the bridge request_122 let vault: @{FungibleToken.Vault} <- self.coa.withdrawTokens(_122 type: self.vaultType,_122 amount: amount,_122 feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}_122 )_122 // Ensure the bridged vault is the correct type_122 assert(_122 vault.getType() == self.vaultType,_122 message: "Bridged vault type mismatch - requested: ".concat(self.vaultType.identifier)_122 .concat(", received: ").concat(vault.getType().identifier)_122 )_122 // Deposit the bridged token into the signer's vault_122 self.receiver.deposit(from: <-vault)_122 // Destroy the ScopedFTProvider_122 destroy self.scopedProvider_122 }_122}`
## Prep Your Assets for Bridging[​](#prep-your-assets-for-bridging "Direct link to Prep Your Assets for Bridging")

### Context[​](#context "Direct link to Context")

To maximize utility to the ecosystem, this bridge is permissionless and open to any fungible or non-fungible token as
defined by the respective Cadence standards and limited to ERC20 and ERC721 Solidity standards. Ultimately, a project
does not have to do anything for users to be able to bridge their assets between VMs. However, there are some
considerations developers may take to enhance the representation of their assets in non-native VMs. These largely relate
to asset metadata and ensuring that bridging does not compromise critical user assumptions about asset ownership.

### EVMBridgedMetadata[​](#evmbridgedmetadata "Direct link to EVMBridgedMetadata")

Proposed in [@onflow/flow-nft/pull/203](https://github.com/onflow/flow-nft/pull/203), the `EVMBridgedMetadata` view
presents a mechanism to both represent metadata from bridged EVM assets as well as enable Cadence-native projects to
specify the representation of their assets in EVM. Implementing this view is not required for assets to be bridged, but
the bridge does default to it when available as a way to provide projects greater control over their EVM asset
definitions within the scope of ERC20 and ERC721 standards.

The interface for this view is as follows:

 `_20access(all) struct URI: MetadataViews.File {_20 /// The base URI prefix, if any. Not needed for all URIs, but helpful_20 /// for some use cases For example, updating a whole NFT collection's_20 /// image host easily_20 access(all) let baseURI: String?_20 /// The URI string value_20 /// NOTE: this is set on init as a concatenation of the baseURI and the_20 /// value if baseURI != nil_20 access(self) let value: String_20_20 access(all) view fun uri(): String_20 _20}_20_20access(all) struct EVMBridgedMetadata {_20 access(all) let name: String_20 access(all) let symbol: String_20_20 access(all) let uri: {MetadataViews.File}_20}`

This uri value could be a pointer to some offchain metadata if you expect your metadata to be static. Or you could
couple the `uri()` method with the utility contract below to serialize the onchain metadata on the fly. Alternatively,
you may choose to host a metadata proxy which serves the requested token URI content.

### SerializeMetadata[​](#serializemetadata "Direct link to SerializeMetadata")

The key consideration with respect to metadata is the distinct metadata storage patterns between ecosystem. It's
critical for NFT utility that the metadata be bridged in addition to the representation of the NFTs ownership. However,
it's commonplace for Cadence NFTs to store metadata onchain while EVM NFTs often store an onchain pointer to metadata
stored offchain. In order for Cadence NFTs to be properly represented in EVM platforms, the metadata must be bridged in
a format expected by those platforms and be done in a manner that also preserves the atomicity of bridge requests. The
path forward on this was decided to be a commitment of serialized Cadence NFT metadata into formats popular in the EVM
ecosystem.

For assets that do not implement `EVMBridgedMetadata`, the bridge will attempt to serialize the metadata of the asset as
a JSON data URL string. This is done via the [`SerializeMetadata`
contract](https://github.com/onflow/flow-evm-bridge/blob/main/cadence/contracts/utils/SerializeMetadata.cdc) which
serializes metadata values into a JSON blob compatible with the OpenSea metadata standard. The serialized metadata is
then committed as the ERC721 `tokenURI` upon bridging Cadence-native NFTs to EVM. Since Cadence NFTs can easily update
onchain metadata either by field or by the ownership of sub-NFTs, this serialization pattern enables token URI updates
on subsequent bridge requests.

### Opting Out[​](#opting-out "Direct link to Opting Out")

It's also recognized that the logic of some use cases may actually be compromised by the act of bridging, particularly
in such a unique partitioned runtime environment. Such cases might include those that do not maintain ownership
assumptions implicit to ecosystem standards.

For instance, an ERC721 implementation may reclaim a user's assets after a month of inactivity. In such a case, bridging
that ERC721 to Cadence would decouple the representation of ownership of the bridged NFT from the actual ownership in
the defining ERC721 contract after the token had been reclaimed - there would be no NFT in escrow for the bridge to
transfer on fulfillment of the NFT back to EVM. In such cases, projects may choose to opt-out of bridging, but
**importantly must do so before the asset has been onboarded to the bridge**.

For Solidity contracts, opting out is as simple as extending the [`BridgePermissions.sol` abstract
contract](https://github.com/onflow/flow-evm-bridge/blob/main/solidity/src/interfaces/BridgePermissions.sol) which
defaults `allowsBridging()` to `false`. The bridge explicitly checks for the implementation of `IBridgePermissions` and
the value of `allowsBridging()` to validate that the contract has not opted out of bridging.

Similarly, Cadence contracts can implement the [`IBridgePermissions.cdc` contract
interface](https://github.com/onflow/flow-evm-bridge/blob/main/cadence/contracts/bridge/interfaces/IBridgePermissions.cdc).
This contract has a single method `allowsBridging()` with a default implementation returning `false`. Again, the bridge
explicitly checks for the implementation of `IBridgePermissions` and the value of `allowsBridging()` to validate that
the contract has not opted out of bridging. Should you later choose to enable bridging, you can simply override the
default implementation and return `true`.

In both cases, `allowsBridging()` gates onboarding to the bridge. Once onboarded - **a permissionless operation anyone
can execute** - the value of `allowsBridging()` is irrelevant and assets can move between VMs permissionlessly.

## Under the Hood[​](#under-the-hood "Direct link to Under the Hood")

For an in-depth look at the high-level architecture of the bridge, see [FLIP
#237](https://github.com/onflow/flips/blob/main/application/20231222-evm-vm-bridge.md)

### Additional Resources[​](#additional-resources "Direct link to Additional Resources")

For the current state of Flow EVM across various task paths, see the following resources:

* [Flow EVM Equivalence forum post](https://forum.flow.com/t/evm-equivalence-on-flow-proposal-and-path-forward/5478)
* [EVM Integration FLIP #223](https://github.com/onflow/flips/pull/225/files)
* [Gateway & JSON RPC FLIP #235](https://github.com/onflow/flips/pull/235)
[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/cadence/vm-bridge.md)Last updated on **Dec 24, 2024** by **Navid TehraniFar**[PreviousBatched EVM Transactions](/evm/cadence/batched-evm-transactions)
###### Rate this page

😞😐😊

* [Deployments](#deployments)
* [Interacting With the Bridge](#interacting-with-the-bridge)
  + [Overview](#overview)
  + [Onboarding](#onboarding)
  + [Bridging](#bridging)
* [Prep Your Assets for Bridging](#prep-your-assets-for-bridging)
  + [Context](#context)
  + [EVMBridgedMetadata](#evmbridgedmetadata)
  + [SerializeMetadata](#serializemetadata)
  + [Opting Out](#opting-out)
* [Under the Hood](#under-the-hood)
  + [Additional Resources](#additional-resources)
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

