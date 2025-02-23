# Source: https://developers.flow.com/build/guides/fungible-token




Creating a Fungible Token | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
  + [Account Linking (FLIP 72)](/build/guides/account-linking)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Creating an NFT Contract](/build/guides/nft)
  + [Creating a Fungible Token](/build/guides/fungible-token)
  + [Building on Mobile](/build/guides/mobile/overview)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Guides
* Creating a Fungible Token
On this page
# Creating a Fungible Token


info

This guide is an in-depth tutorial on launching a Fungible Token contract from scratch. To launch in 2 minutes using a tool check out [Toucans](https://toucans.ecdao.org/)

## What are Fungible Tokens?[​](#what-are-fungible-tokens "Direct link to What are Fungible Tokens?")

Fungible tokens are digital assets that are interchangeable and indistinguishable with other tokens of the same type. This means that each token is identical in specification to every other token in circulation. Think of them like traditional money; every dollar bill has the same value as every other dollar bill. Fungible tokens play a crucial role in web3 ecosystems, serving as both a means of payment and an incentive for network participation. They can take on various roles including currencies, structured financial instruments, shares of index funds, and even voting rights in decentralized autonomous organizations.

## Vaults on Flow[​](#vaults-on-flow "Direct link to Vaults on Flow")

On the Flow blockchain and in the Cadence programming language,
fungible tokens are stored in structures called resources.
Resources are objects in Cadence that store data,
but have special restrictions about how they can be stored and transferred,
making them perfect for representing digital objects with real value.

You can learn more about resources in the Cadence [documentation](https://cadence-lang.org/docs/language/resources)
and [tutorials](https://cadence-lang.org/docs/tutorial/resources).

For fungible tokens specifically, tokens are represented by a resource type called a `Vault`:

 `_10access(all) resource interface Vault {_10_10 /// Field that tracks the balance of a vault_10 access(all) var balance: UFix64_10_10}`

Think of a `Vault` as a digital piggy bank.
Users who own fungible tokens store vault objects that track their balances
directly in their account storage. This is opposed to languages
that track user balances in a central ledger smart contract.

When you transfer tokens from one vault to another:

1. The transferor's vault creates a temporary vault holding the transfer amount.
2. The original vault's balance decreases by the transfer amount.
3. The recipient's vault receives the tokens from the temporary vault
   and adds the temporary vault's balance to the its own balance.
4. The temporary vault is then destroyed.

This process ensures secure and accurate token transfers on the Flow blockchain.

## Fungible Token Standard[​](#fungible-token-standard "Direct link to Fungible Token Standard")

The [Fungible Token Standard](https://github.com/onflow/flow-ft) defines how a fungible token should behave on Flow.
Wallets and other platforms need to recognize these tokens,
so they adhere to a specific interface, which defines fields like balance,
totalSupply, withdraw functionality, and more.
This interface ensures that all fungible tokens on Flow have a consistent structure and behavior.
Clink the link to the fungible token standard to see the full standard
and learn about specific features and requirements.

[Learn more about interfaces here](https://developers.flow.com/cadence/language/interfaces).

## Setting Up a Project[​](#setting-up-a-project "Direct link to Setting Up a Project")

To start creating a Fungible Token on the Flow blockchain, you'll first need some tools and configurations in place.

### Installing Flow CLI[​](#installing-flow-cli "Direct link to Installing Flow CLI")

The **Flow CLI** (Command Line Interface) provides a suite of tools that allow developers to interact seamlessly with the Flow blockchain.

If you haven't installed the Flow CLI yet and have [Homebrew](https://brew.sh/) installed,
you can run `brew install flow-cli`. If you don't have Homebrew,
please follow [the installation guide here](https://developers.flow.com/tools/flow-cli/install).

### Initializing a New Project[​](#initializing-a-new-project "Direct link to Initializing a New Project")

> 💡 Note: Here is [a link to the completed code](https://github.com/chasefleming/FooToken) if you want to skip ahead or reference as you follow along.

Once you have the Flow CLI installed, you can set up a new project using the `flow init` command. This command initializes the necessary directory structure and a `flow.json` configuration file (a way to configure your project for contract sources, deployments, accounts, and more):

 `_10flow init FooToken`
> Note: Select "No" when it asks you to install core contracts for the purposes of this tutorial.

Upon execution, the command will generate the following directory structure:

 `_10/cadence_10 /contracts_10 /scripts_10 /transactions_10 /tests_10flow.json`

Now, navigate into the project directory:

 `_10cd FooToken`

In our configuration file, called `flow.json`, for the network we want to use,
we are going to state the address the `FungibleToken` contract is deployed
to via `aliases` in a new `contracts` section. Since it is a standard contract,
it has already been deployed to the emulator, a tool that runs and emulates
a local development version of the Flow Blockchain, for us.
You can find addresses for other networks, like Testnet and Mainnet, on the [Fungible Token Standard repo](https://github.com/onflow/flow-ft).

We'll also need to add the addresses for `ViewResolver`, `MetadataViews`,
and `FungibleTokenMetadataViews`, which are other important contracts to use.
These contracts are deployed to the Flow emulator by default,
so there is not need to copy their code into your repo.
The addresses below are the addresses in the emulator that your contract
will import them from.

 `_22"contracts": {_22 "FungibleToken": {_22 "aliases": {_22 "emulator": "0xee82856bf20e2aa6"_22 }_22 },_22 "FungibleTokenMetadataViews": {_22 "aliases": {_22 "emulator": "0xee82856bf20e2aa6"_22 }_22 },_22 "ViewResolver": {_22 "aliases": {_22 "emulator": "0xf8d6e0586b0a20c7"_22 }_22 },_22 "MetadataViews": {_22 "aliases": {_22 "emulator": "0xf8d6e0586b0a20c7"_22 }_22 }_22}`
## Writing Our Token Contract[​](#writing-our-token-contract "Direct link to Writing Our Token Contract")

Next let's create a `FooToken` contract at `cadence/contract/FooToken.cdc` using the boilerplate `generate` command from the Flow CLI:

 `_10flow generate contract FooToken`

This will create a new file called `FooToken.cdc` in the `contracts` directory. Let's open it up and add some code.

In this contract file, we want to import our `FungibleToken` contract that we've defined in `flow.json`.

 `_10import "FungibleToken"`

In this same file, let's create our contract which implements the `FungibleToken` contract interface (it does so by setting it following the `FooToken:`).
We'll also include fields for standard storage and public paths
for our resource definitions.
In our `init` — which runs on the contract's first deployment and is used to set initial values — let's set an starting total supply of 1,000 tokens for this example.

 `_16// ...previous code_16_16access(all) contract FooToken: FungibleToken {_16 access(all) var totalSupply: UFix64_16_16 access(all) let VaultStoragePath: StoragePath_16 access(all) let VaultPublicPath: PublicPath_16 access(all) let MinterStoragePath: StoragePath_16_16 init() {_16 self.totalSupply = 1000.0_16 self.VaultStoragePath = /storage/fooTokenVault_16 self.VaultPublicPath = /public/fooTokenVault_16 self.MinterStoragePath = /storage/fooTokenMinter_16 }_16}`
### Creating a Vault[​](#creating-a-vault "Direct link to Creating a Vault")

Inside of this contract, we'll need to create a resource for a `Vault`.
The `FungibleToken` standard requires that your vault implements the `FungibleToken.Vault` interface.
This interface inherits from [many other interfaces](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc#L140)
which enforce different functionality that you can learn about in the standard.

 `_16import "FungibleToken"_16_16access(all) contract FooToken: FungibleToken {_16 // ...totalSupply and path code_16_16 access(all) resource Vault: FungibleToken.Vault {_16_16 access(all) var balance: UFix64_16_16 init(balance: UFix64) {_16 self.balance = balance_16 }_16 }_16_16 // ...init code_16}`

In order to give an account a vault, we need to create a function
that creates a vault of our FooToken type and returns it to the account.
This function takes a `vaultType: Type` argument that allows the caller
to specify which type of `Vault` they want to create.
Contracts that implement multiple `Vault` types can use this argument,
but since your contract is only implementing one `Vault` type,
it can ignore the argument.

A simpler version of this function with no parameter
should also be added to your `Vault` implementation.

 `_24import "FungibleToken"_24_24access(all) contract FooToken: FungibleToken {_24 // ...other code_24_24 access(all) resource Vault: FungibleToken.Vault {_24_24 // ...other vault code_24_24 access(all) fun createEmptyVault(): @FooToken.Vault {_24 return <-create Vault(balance: 0.0)_24 }_24_24 // ...vault init code_24 }_24_24 // ...other code_24_24 access(all) fun createEmptyVault(vaultType: Type): @FooToken.Vault {_24 return <- create Vault(balance: 0.0)_24 }_24_24 // ...FooToken.init() code_24}`

Inside our `Vault` resource, we also need a way to withdraw balances.
To do that, we need to add a `withdraw()` function that returns a new vault
with the transfer amount and decrements the existing balance.

 `_20import "FungibleToken"_20_20access(all) contract FooToken: FungibleToken {_20_20 // ...previous code_20_20 access(all) resource Vault: FungibleToken.Vault {_20_20 // ...other vault code_20_20 access(FungibleToken.Withdraw) fun withdraw(amount: UFix64): @FooToken.Vault {_20 self.balance = self.balance - amount_20 return <-create Vault(balance: amount)_20 }_20_20 // ...vault init code_20 }_20_20 // ...additional code_20}`

As you can see, this function has an `access(FungibleToken.Withdraw)` access modifier.
This is an example of entitlements in Cadence.
[Entitlements](https://cadence-lang.org/docs/language/access-control#entitlements)
are a way for developers to restrict access to privileged fields and functions
in a composite type like a resource when a reference is created for it.
In this example, the `withdraw()` function is always accessible to code that
controls the full `Vault` object, but if a reference is created for it,
the `withdraw()` function can only be called if the reference
is authorized by the owner with `FungibleToken.Withdraw`,
which is [a standard entitlement](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc#L53)
defined by the FungibleToken contract:

 `_10// Example of an authorized entitled reference to a FungibleToken.Vault_10<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>`

Entitlements are important to understand because they are what protects
privileged functionality in your resource objects from being accessed by third-parties.
It is recommended to read the [entitlements documentation](https://cadence-lang.org/docs/language/access-control#entitlements)
to understand how to use the feature properly.

[References](https://cadence-lang.org/docs/language/references) can be freely up-casted and down-casted in Cadence, so it is important
for privileged functionality to be protected by an entitlement so that it can
only be accessed if it is authorized.

In addition to withdrawing, the vault also needs a way to deposit.
We'll [typecast](https://cadence-lang.org/docs/language/operators#casting-operators)
to make sure we are dealing with the correct token, update the vault balance,
and destroy the vault. Add this code to your resource:

 `_22import "FungibleToken"_22_22access(all) contract FooToken: FungibleToken {_22_22 // ...previous code_22_22 access(all) resource Vault: FungibleToken.Vault {_22_22 // ...other vault code_22_22 access(all) fun deposit(from: @{FungibleToken.Vault}) {_22 let vault <- from as! @FooToken.Vault_22 self.balance = self.balance + vault.balance_22 destroy vault_22 }_22_22 // ...vault init_22_22 }_22_22 // ...additional code_22}`

Many projects rely on events the signal when withdrawals, deposits, or burns happen.
Luckily, the `FungibleToken` standard handles the definition and emission
of events for projects, so there is no need for you to add any events
to your implementation for withdraw, deposit, and burn.

Here are the `FungibleToken` event definitions:

 `_10/// The event that is emitted when tokens are withdrawn from a Vault_10access(all) event Withdrawn(type: String, amount: UFix64, from: Address?, fromUUID: UInt64, withdrawnUUID: UInt64, balanceAfter: UFix64)_10_10/// The event that is emitted when tokens are deposited to a Vault_10access(all) event Deposited(type: String, amount: UFix64, to: Address?, toUUID: UInt64, depositedUUID: UInt64, balanceAfter: UFix64)_10_10/// Event that is emitted when the global burn method is called with a non-zero balance_10access(all) event Burned(type: String, amount: UFix64, fromUUID: UInt64)`

These events are [emitted by the `Vault` interface](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc#L198)
in the `FungibleToken` contract whenever the relevant function is called on any implementation.

One important piece to understand about the `Burned` event in particular
is that in order for it to be emitted when a `Vault` is burned, it needs to
be burnt via [the `Burner` contract's `burn()` method](https://github.com/onflow/flow-ft/blob/master/contracts/utility/Burner.cdc#L23).

The [`Burner` contract](/build/core-contracts/burner) defines a standard
that all projects should use for handling the destruction of any resource.
It allows projects to define custom logic that can be executed when a resource is destroyed,
like emitting events, or updating a field in the contract to show that the resource was destroyed.

This will call the resource's `burnCallback()` function, which emits the event.
You'll need to also add this function to your token contract now:

 `_24import "FungibleToken"_24_24access(all) contract FooToken: FungibleToken {_24_24 // ...previous code_24_24 access(all) resource Vault: FungibleToken.Vault {_24_24 // ...other vault code_24_24 /// Called when a fungible token is burned via the `Burner.burn()` method_24 access(contract) fun burnCallback() {_24 if self.balance > 0.0 {_24 FooToken.totalSupply = FooToken.totalSupply - self.balance_24 }_24 self.balance = 0.0_24 }_24_24 // ...vault init_24_24 }_24_24 // ...additional code_24}`

If you ever need to destroy a `Vault` with a non-zero balance,
you should destroy it via the `Burner.burn` method so this important function can be called.

There are three other utility methods that need to be added to your `Vault`
to get various information:

 `_33import "FungibleToken"_33_33access(all) contract FooToken: FungibleToken {_33_33 // ...previous code_33_33 access(all) resource Vault: FungibleToken.Vault {_33_33 // ...other vault code_33_33 /// getSupportedVaultTypes optionally returns a list of vault types that this receiver accepts_33 access(all) view fun getSupportedVaultTypes(): {Type: Bool} {_33 let supportedTypes: {Type: Bool} = {}_33 supportedTypes[self.getType()] = true_33 return supportedTypes_33 }_33_33 /// Says if the Vault can receive the provided type in the deposit method_33 access(all) view fun isSupportedVaultType(type: Type): Bool {_33 return self.getSupportedVaultTypes()[type] ?? false_33 }_33_33 /// Asks if the amount can be withdrawn from this vault_33 access(all) view fun isAvailableToWithdraw(amount: UFix64): Bool {_33 return amount <= self.balance_33 }_33_33 // ...vault init_33_33 }_33_33 // ...additional code_33}`
### Adding Support for Metadata Views[​](#adding-support-for-metadata-views "Direct link to Adding Support for Metadata Views")

The Fungible Token standard also enforces that implementations
provide functionality to return a set of standard views about the tokens
via the [ViewResolver](https://github.com/onflow/flow-nft/blob/master/contracts/ViewResolver.cdc)
and [FungibleTokenMetadataViews](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleTokenMetadataViews.cdc) definitions.
(You will need to add these imports to your contract now)
These provide developers with standard ways of representing metadata
about a given token such as supply, token symbols, website links, and standard
account paths and types that third-parties can access in a standard way.
You can see the [metadata views documentation](/build/advanced-concepts/metadata-views)
for a more thorough guide using a NFT contract as an example.

For now, you can add this code to your contract to support the important metadata views:

 `_83import "FungibleToken"_83_83// Add these imports_83import "MetadataViews"_83import "FungibleTokenMetadataViews"_83_83access(all) contract FooToken: FungibleToken {_83 // ...other code_83_83 access(all) view fun getContractViews(resourceType: Type?): [Type] {_83 return [_83 Type<FungibleTokenMetadataViews.FTView>(),_83 Type<FungibleTokenMetadataViews.FTDisplay>(),_83 Type<FungibleTokenMetadataViews.FTVaultData>(),_83 Type<FungibleTokenMetadataViews.TotalSupply>()_83 ]_83 }_83_83 access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {_83 switch viewType {_83 case Type<FungibleTokenMetadataViews.FTView>():_83 return FungibleTokenMetadataViews.FTView(_83 ftDisplay: self.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTDisplay>()) as! FungibleTokenMetadataViews.FTDisplay?,_83 ftVaultData: self.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?_83 )_83 case Type<FungibleTokenMetadataViews.FTDisplay>():_83 let media = MetadataViews.Media(_83 file: MetadataViews.HTTPFile(_83 // Change this to your own SVG image_83 url: "https://assets.website-files.com/5f6294c0c7a8cdd643b1c820/5f6294c0c7a8cda55cb1c936_Flow_Wordmark.svg"_83 ),_83 mediaType: "image/svg+xml"_83 )_83 let medias = MetadataViews.Medias([media])_83 return FungibleTokenMetadataViews.FTDisplay(_83 // Change these to represent your own token_83 name: "Example Foo Token",_83 symbol: "EFT",_83 description: "This fungible token is used as an example to help you develop your next FT #onFlow.",_83 externalURL: MetadataViews.ExternalURL("https://developers.flow.com/build/guides/fungible-token"),_83 logos: medias,_83 socials: {_83 "twitter": MetadataViews.ExternalURL("https://twitter.com/flow_blockchain")_83 }_83 )_83 case Type<FungibleTokenMetadataViews.FTVaultData>():_83 return FungibleTokenMetadataViews.FTVaultData(_83 storagePath: self.VaultStoragePath,_83 receiverPath: self.VaultPublicPath,_83 metadataPath: self.VaultPublicPath,_83 receiverLinkedType: Type<&FooToken.Vault>(),_83 metadataLinkedType: Type<&FooToken.Vault>(),_83 createEmptyVaultFunction: (fun(): @{FungibleToken.Vault} {_83 return <-FooToken.createEmptyVault(vaultType: Type<@FooToken.Vault>())_83 })_83 )_83 case Type<FungibleTokenMetadataViews.TotalSupply>():_83 return FungibleTokenMetadataViews.TotalSupply(_83 totalSupply: FooToken.totalSupply_83 )_83 }_83 return nil_83 }_83_83 // ...other code_83_83 access(all) resource Vault: FungibleToken.Vault {_83_83 // ...other vault code_83_83 access(all) view fun getViews(): [Type] {_83 return FooToken.getContractViews(resourceType: nil)_83 }_83_83 access(all) fun resolveView(_ view: Type): AnyStruct? {_83 return FooToken.resolveContractView(resourceType: nil, viewType: view)_83 }_83_83 // ...other vault code_83 }_83_83 // ...other FooToken code_83}`
### Creating a Minter[​](#creating-a-minter "Direct link to Creating a Minter")

Let's create a minter resource which is used to mint vaults that have tokens in them. We can keep track of tokens we are minting with totalSupply

If we want the ability to create new tokens, we'll need a way to mint them. To do that, let's create another resource on the `FooToken` contract. This will have a `mintToken`function which can increase the total supply of the token.

 `_31import "FungibleToken"_31import "MetadataViews"_31import "FungibleTokenMetadataViews"_31_31access(all) contract FooToken: FungibleToken {_31_31 // ...additional contract code_31_31 // Add this event_31 access(all) event TokensMinted(amount: UFix64, type: String)_31_31 /// Minter_31 ///_31 /// Resource object that token admin accounts can hold to mint new tokens._31 ///_31 access(all) resource Minter {_31 /// mintTokens_31 ///_31 /// Function that mints new tokens, adds them to the total supply,_31 /// and returns them to the calling context._31 ///_31 access(all) fun mintTokens(amount: UFix64): @FooToken.Vault {_31 FooToken.totalSupply = FooToken.totalSupply + amount_31 let vault <-create Vault(balance: amount)_31 emit TokensMinted(amount: amount, type: vault.getType().identifier)_31 return <-vault_31 }_31 }_31_31 // ...additional contract code_31}`

We also want to decide which account/s we want to give this ability to.
In our example, we'll give it to the account where the contract is deployed.
We can set this in the contract init function below the setting of total supply
so that when the contract is created the minter is stored on the same account.

 `_13import "FungibleToken"_13import "MetadataViews"_13import "FungibleTokenMetadataViews"_13_13access(all) contract FooToken: FungibleToken {_13_13 // ...additional contract code_13_13 init() {_13 self.totalSupply = 1000.0 // existed before_13 self.account.save(<- create Minter(), to: self.MinterStoragePath)_13 }_13}`

After each of these steps, your `FooToken.cdc` contract file should now look like this:

 `_172import "FungibleToken"_172import "MetadataViews"_172import "FungibleTokenMetadataViews"_172_172access(all) contract FooToken: FungibleToken {_172_172 /// The event that is emitted when new tokens are minted_172 access(all) event TokensMinted(amount: UFix64, type: String)_172_172 /// Total supply of FooTokens in existence_172 access(all) var totalSupply: UFix64_172_172 /// Storage and Public Paths_172 access(all) let VaultStoragePath: StoragePath_172 access(all) let VaultPublicPath: PublicPath_172 access(all) let ReceiverPublicPath: PublicPath_172 access(all) let MinterStoragePath: StoragePath_172_172 access(all) view fun getContractViews(resourceType: Type?): [Type] {_172 return [_172 Type<FungibleTokenMetadataViews.FTView>(),_172 Type<FungibleTokenMetadataViews.FTDisplay>(),_172 Type<FungibleTokenMetadataViews.FTVaultData>(),_172 Type<FungibleTokenMetadataViews.TotalSupply>()_172 ]_172 }_172_172 access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {_172 switch viewType {_172 case Type<FungibleTokenMetadataViews.FTView>():_172 return FungibleTokenMetadataViews.FTView(_172 ftDisplay: self.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTDisplay>()) as! FungibleTokenMetadataViews.FTDisplay?,_172 ftVaultData: self.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?_172 )_172 case Type<FungibleTokenMetadataViews.FTDisplay>():_172 let media = MetadataViews.Media(_172 file: MetadataViews.HTTPFile(_172 // Change this to your own SVG image_172 url: "https://assets.website-files.com/5f6294c0c7a8cdd643b1c820/5f6294c0c7a8cda55cb1c936_Flow_Wordmark.svg"_172 ),_172 mediaType: "image/svg+xml"_172 )_172 let medias = MetadataViews.Medias([media])_172 return FungibleTokenMetadataViews.FTDisplay(_172 // Change these to represent your own token_172 name: "Example Foo Token",_172 symbol: "EFT",_172 description: "This fungible token is used as an example to help you develop your next FT #onFlow.",_172 externalURL: MetadataViews.ExternalURL("https://developers.flow.com/build/guides/fungible-token"),_172 logos: medias,_172 socials: {_172 "twitter": MetadataViews.ExternalURL("https://twitter.com/flow_blockchain")_172 }_172 )_172 case Type<FungibleTokenMetadataViews.FTVaultData>():_172 return FungibleTokenMetadataViews.FTVaultData(_172 storagePath: self.VaultStoragePath,_172 receiverPath: self.VaultPublicPath,_172 metadataPath: self.VaultPublicPath,_172 receiverLinkedType: Type<&FooToken.Vault>(),_172 metadataLinkedType: Type<&FooToken.Vault>(),_172 createEmptyVaultFunction: (fun(): @{FungibleToken.Vault} {_172 return <-FooToken.createEmptyVault(vaultType: Type<@FooToken.Vault>())_172 })_172 )_172 case Type<FungibleTokenMetadataViews.TotalSupply>():_172 return FungibleTokenMetadataViews.TotalSupply(_172 totalSupply: FooToken.totalSupply_172 )_172 }_172 return nil_172 }_172_172 access(all) resource Vault: FungibleToken.Vault {_172_172 /// The total balance of this vault_172 access(all) var balance: UFix64_172_172 // initialize the balance at resource creation time_172 init(balance: UFix64) {_172 self.balance = balance_172 }_172_172 /// Called when a fungible token is burned via the `Burner.burn()` method_172 access(contract) fun burnCallback() {_172 if self.balance > 0.0 {_172 FooToken.totalSupply = FooToken.totalSupply - self.balance_172 }_172 self.balance = 0.0_172 }_172_172 access(all) view fun getViews(): [Type] {_172 return FooToken.getContractViews(resourceType: nil)_172 }_172_172 access(all) fun resolveView(_ view: Type): AnyStruct? {_172 return FooToken.resolveContractView(resourceType: nil, viewType: view)_172 }_172_172 access(all) view fun getSupportedVaultTypes(): {Type: Bool} {_172 let supportedTypes: {Type: Bool} = {}_172 supportedTypes[self.getType()] = true_172 return supportedTypes_172 }_172_172 access(all) view fun isSupportedVaultType(type: Type): Bool {_172 return self.getSupportedVaultTypes()[type] ?? false_172 }_172_172 access(all) view fun isAvailableToWithdraw(amount: UFix64): Bool {_172 return amount <= self.balance_172 }_172_172 access(FungibleToken.Withdraw) fun withdraw(amount: UFix64): @FooToken.Vault {_172 self.balance = self.balance - amount_172 return <-create Vault(balance: amount)_172 }_172_172 access(all) fun deposit(from: @{FungibleToken.Vault}) {_172 let vault <- from as! @FooToken.Vault_172 self.balance = self.balance + vault.balance_172 vault.balance = 0.0_172 destroy vault_172 }_172_172 access(all) fun createEmptyVault(): @FooToken.Vault {_172 return <-create Vault(balance: 0.0)_172 }_172 }_172_172 access(all) resource Minter {_172 /// mintTokens_172 ///_172 /// Function that mints new tokens, adds them to the total supply,_172 /// and returns them to the calling context._172 ///_172 access(all) fun mintTokens(amount: UFix64): @FooToken.Vault {_172 FooToken.totalSupply = FooToken.totalSupply + amount_172 let vault <-create Vault(balance: amount)_172 emit TokensMinted(amount: amount, type: vault.getType().identifier)_172 return <-vault_172 }_172 }_172_172 access(all) fun createEmptyVault(vaultType: Type): @FooToken.Vault {_172 return <- create Vault(balance: 0.0)_172 }_172_172 init() {_172 self.totalSupply = 1000.0_172_172 self.VaultStoragePath = /storage/fooTokenVault_172 self.VaultPublicPath = /public/fooTokenVault_172 self.MinterStoragePath = /storage/fooTokenMinter_172_172 // Create the Vault with the total supply of tokens and save it in storage_172 //_172 let vault <- create Vault(balance: self.totalSupply)_172 emit TokensMinted(amount: vault.balance, type: vault.getType().identifier)_172 self.account.storage.save(<-vault, to: self.VaultStoragePath)_172_172 // Create a public capability to the stored Vault that exposes_172 // the `deposit` method and getAcceptedTypes method through the `Receiver` interface_172 // and the `balance` method through the `Balance` interface_172 //_172 let fooTokenCap = self.account.capabilities.storage.issue<&FooToken.Vault>(self.VaultStoragePath)_172 self.account.capabilities.publish(fooTokenCap, at: self.VaultPublicPath)_172_172 let minter <- create Minter()_172 self.account.storage.save(<-minter, to: self.MinterStoragePath)_172 }_172}`
## Deploying the Contract[​](#deploying-the-contract "Direct link to Deploying the Contract")

In order to use the contract, we need to deploy it to the network we want to use it on.
In our case we are going to deploy it to emulator while developing.

Back in our `flow.json`, let's add our `FooToken` to the `contracts` after `FungibleToken` with the path of the source code:

 `_10"FooToken": "cadence/contracts/FooToken.cdc"`

Let's also add a new `deployments` section to `flow.json` with the network
we want to deploy it to, `emulator`, the account we want it deployed to `emulator-account`,
and the list of contracts we want deployed in the array.

 `_10"deployments": {_10 "emulator": {_10 "emulator-account": ["FooToken"]_10 }_10}`

Next, using the Flow CLI, we will start the emulator. As mentioned,
this will give us a local development environment for the Flow Blockchain.

 `_10flow emulator start`

Open a new terminal and run the following to deploy your project:

 `_10flow project deploy`

Congrats, you've deployed your contract to the Flow Blockchain emulator.
To read more about deploying your project to other environments,
see the [CLI docs](https://developers.flow.com/tools/flow-cli/deployment/deploy-project-contracts).

## Reading the Token's Total Supply[​](#reading-the-tokens-total-supply "Direct link to Reading the Token's Total Supply")

Let's now check that our total supply was initialized with 1,000 FooTokens. Go ahead and create a script called `get_total_supply.cdc` using the `generate` command.

 `_10flow generate script get_total_supply`

In `cadence/scripts/get_total_supply.cdc` (which was just created), let's add this code which will log the `totalSupply` value from the `FooToken` contract:

 `_10import "FooToken"_10_10access(all) fun main(): UFix64 {_10 return FooToken.totalSupply_10}`

To run this using the CLI, enter this in your terminal:

 `_10flow scripts execute cadence/scripts/get_total_supply.cdc`

In the terminal where you started the emulator, you should see `Result: 1000.0`

To learn more about running scripts using Flow CLI, [see the docs](https://developers.flow.com/tools/flow-cli/scripts/execute-scripts).

## Giving Accounts the Ability to Receive Tokens[​](#giving-accounts-the-ability-to-receive-tokens "Direct link to Giving Accounts the Ability to Receive Tokens")

On Flow, newly created accounts cannot receive arbitrary assets.
They need to be initialized to receive resources.
In our case, we want to give accounts tokens and we'll need to create
a `Vault` (which acts as a receiver) on each account that we want
to have the ability to receive tokens. To do this, we'll need to run a transaction
which will create the vault and set it in their storage
using the `createEmptyVault()` function we created earlier on the contract.

Let's first create the file at `cadence/transactions/setup_ft_account.cdc` using the `generate` command:

 `_10flow generate transaction setup_ft_account`

Then add this code to it.
This will call the `createEmptyVault` function, save it in storage,
and create a capability for the vault which will later allow us to read from it
(To learn more about capabilities, see [the Cadence docs here](https://developers.flow.com/cadence/language/capabilities)).

 `_24import "FungibleToken"_24import "FooToken"_24_24transaction () {_24_24 prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_24_24 // Return early if the account already stores a FooToken Vault_24 if signer.storage.borrow<&FooToken.Vault>(from: FooToken.VaultStoragePath) != nil {_24 return_24 }_24_24 let vault <- FooToken.createEmptyVault(vaultType: Type<@FooToken.Vault>())_24_24 // Create a new FooToken Vault and put it in storage_24 signer.storage.save(<-vault, to: FooToken.VaultStoragePath)_24_24 // Create a public capability to the Vault that exposes the Vault interfaces_24 let vaultCap = signer.capabilities.storage.issue<&FooToken.Vault>(_24 FooToken.VaultStoragePath_24 )_24 signer.capabilities.publish(vaultCap, at: FooToken.VaultPublicPath)_24 }_24}`

There are also examples of [generic transactions](https://github.com/onflow/flow-ft/blob/master/transactions/metadata/setup_account_from_address.cdc)
that you can use to setup an account for ANY fungible token using metadata views!
You should check those out and try to use generic transactions whenever it is possible.

Next let's create a new emulator account using the CLI. We'll use this account to create a new vault and mint tokens into it. Run:

 `_10flow accounts create`

Let's call it `test-acct` and select "Emulator" for the network:

 `_10test-acct`

This will have added a new account, called `test-acct` to your `flow.json`.

To call our setup account transaction from the CLI, we'll run the following:

 `_10flow transactions send ./cadence/transactions/setup_ft_account.cdc --signer test-acct --network emulator`

To learn more about running transactions using CLI, [see the docs](https://developers.flow.com/tools/flow-cli/transactions/send-transactions).

## Reading a Vault's Balance[​](#reading-a-vaults-balance "Direct link to Reading a Vault's Balance")

Let's now read the balance of the newly created account (`test-acct`) to check it's zero.

Create this new script file `cadence/scripts/get_footoken_balance.cdc`:

 `_10flow generate script get_footoken_balance`

Add this code which attempts to borrow the capability from the account requested and logs the vault balance if permitted:

 `_15import "FungibleToken"_15import "FooToken"_15import "FungibleTokenMetadataViews"_15_15access(all) fun main(address: Address): UFix64 {_15 let vaultData = FooToken.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?_15 ?? panic("Could not get FTVaultData view for the FooToken contract")_15_15 return getAccount(address).capabilities.borrow<&{FungibleToken.Balance}>(_15 vaultData.metadataPath_15 )?.balance_15 ?? panic("Could not borrow a reference to the FooToken Vault in account "_15 .concat(address.toString()).concat(" at path ").concat(vaultData.metadataPath.toString())_15 .concat(". Make sure you are querying an address that has an FooToken Vault set up properly."))_15}`

To run this script using the CLI, enter the following in your terminal.
Note: you'll need to replace `123` with the address created by CLI
in your `flow.json` for the `test-acct` address.

 `_10flow scripts execute cadence/scripts/get_footoken_balance.cdc 123 // change "123" to test-acct address`

You should see a balance of zero logged.

## Minting More Tokens[​](#minting-more-tokens "Direct link to Minting More Tokens")

Now that we have an account with a vault, let's mint some tokens into it
using the Minter we created on the contract account.

To do this, let's create a new transaction file `cadence/transactions/mint_footoken.cdc`:

 `_10flow generate transaction mint_footoken`

Next, let's add the following code to the `mint_footoken.cdc` file.
This code will attempt to borrow the minting capability
and mint 20 new tokens into the receivers account.

 `_33import "FungibleToken"_33import "FooToken"_33_33transaction(recipient: Address, amount: UFix64) {_33_33 /// Reference to the Example Token Minter Resource object_33 let tokenMinter: &FooToken.Minter_33_33 /// Reference to the Fungible Token Receiver of the recipient_33 let tokenReceiver: &{FungibleToken.Receiver}_33_33 prepare(signer: auth(BorrowValue) &Account) {_33_33 // Borrow a reference to the admin object_33 self.tokenMinter = signer.storage.borrow<&FooToken.Minter>(from: FooToken.MinterStoragePath)_33 ?? panic("Cannot mint: Signer does not store the FooToken Minter in their account!")_33_33 self.tokenReceiver = getAccount(recipient).capabilities.borrow<&{FungibleToken.Receiver}>(FooToken.VaultPublicPath)_33 ?? panic("Could not borrow a Receiver reference to the FungibleToken Vault in account "_33 .concat(recipient.toString()).concat(" at path ").concat(FooToken.VaultPublicPath.toString())_33 .concat(". Make sure you are sending to an address that has ")_33 .concat("a FungibleToken Vault set up properly at the specified path."))_33 }_33_33 execute {_33_33 // Create mint tokens_33 let mintedVault <- self.tokenMinter.mintTokens(amount: amount)_33_33 // Deposit them to the receiever_33 self.tokenReceiver.deposit(from: <-mintedVault)_33 }_33}`

To run this transaction, enter this in your terminal.
Note: `123` should be replaced with address of `test-acct` found in your `flow.json`.
This command also states to sign with our `emulator-account` on the Emulator network.

 `_10flow transactions send ./cadence/transactions/mint_footoken.cdc 123 20.0 --signer emulator-account --network emulator`

Let's go ahead and read the vault again. Remember to replace `123` with the correct address.

 `_10flow scripts execute cadence/scripts/get_footoken_balance.cdc 123`

It should now say 20 tokens are in the vault.

## Transferring Tokens Between Accounts[​](#transferring-tokens-between-accounts "Direct link to Transferring Tokens Between Accounts")

The final functionality we'll add is the ability to transfer tokens from one account to another.

To do that, create a new `cadence/transactions/transfer_footoken.cdc` transaction file:

 `_10flow generate transaction transfer_footoken`

Let's add the code which states that the signer of the transaction
will withdraw from their vault and put it into the receiver's vault
which will be passed as a transaction argument.

 `_36import "FungibleToken"_36import "FooToken"_36_36transaction(to: Address, amount: UFix64) {_36_36 // The Vault resource that holds the tokens that are being transferred_36 let sentVault: @{FungibleToken.Vault}_36_36 prepare(signer: auth(BorrowValue) &Account) {_36_36 // Get a reference to the signer's stored vault_36 let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FooToken.Vault>(from: FooToken.VaultStoragePath)_36 ?? panic("The signer does not store an FooToken.Vault object at the path "_36 .concat(FooToken.VaultStoragePath.toString())_36 .concat(". The signer must initialize their account with this vault first!"))_36_36 // Withdraw tokens from the signer's stored vault_36 self.sentVault <- vaultRef.withdraw(amount: amount)_36 }_36_36 execute {_36_36 // Get the recipient's public account object_36 let recipient = getAccount(to)_36_36 // Get a reference to the recipient's Receiver_36 let receiverRef = recipient.capabilities.borrow<&{FungibleToken.Receiver}>(FooToken.VaultPublicPath)_36 ?? panic("Could not borrow a Receiver reference to the FooToken Vault in account "_36 .concat(recipient.toString()).concat(" at path ").concat(FooToken.VaultPublicPath.toString())_36 .concat(". Make sure you are sending to an address that has ")_36 .concat("a FooToken Vault set up properly at the specified path."))_36_36 // Deposit the withdrawn tokens in the recipient's receiver_36 receiverRef.deposit(from: <-self.sentVault)_36 }_36}`

To send our tokens, we'll need to create a new account to send them to. Let's make one more account on emulator. Run:

 `_10flow accounts create`

And pick the name:

 `_10test-acct-2`

Make sure to select Emulator as the network.

Don't forget the new account will need a vault added, so let's run the following transaction to add one:

 `_10flow transactions send ./cadence/transactions/setup_ft_account.cdc --signer test-acct-2 --network emulator`

Now, let's send 1 token from our earlier account to the new account. Remember to replace `123` with account address of `test-acct-2`.

 `_10flow transactions send ./cadence/transactions/transfer_footoken.cdc 123 1.0 --signer test-acct --network emulator`

After that, read the balance of `test-acct-2` (replace the address `123`).

 `_10flow scripts execute cadence/scripts/get_footoken_balance.cdc 123`

You should now see 1 token in `test-acct-2` account!

The transfer transaction also has a [generic version](https://github.com/onflow/flow-ft/blob/master/transactions/generic_transfer_with_address.cdc) that developers are encouraged to use!

## More[​](#more "Direct link to More")

* [View a repo of this example code](https://github.com/chasefleming/FooToken)
* [Review an `ExampleToken` contract implementing all of the remaining FungibleToken interface](https://github.com/onflow/flow-ft/blob/master/contracts/ExampleToken.cdc)
* [View the Flow Token Standard](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc)
[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/fungible-token.md)Last updated on **Feb 11, 2025** by **Chase Fleming**[PreviousCreating an NFT Contract](/build/guides/nft)[NextOverview](/build/guides/mobile/overview)
###### Rate this page

😞😐😊

* [What are Fungible Tokens?](#what-are-fungible-tokens)
* [Vaults on Flow](#vaults-on-flow)
* [Fungible Token Standard](#fungible-token-standard)
* [Setting Up a Project](#setting-up-a-project)
  + [Installing Flow CLI](#installing-flow-cli)
  + [Initializing a New Project](#initializing-a-new-project)
* [Writing Our Token Contract](#writing-our-token-contract)
  + [Creating a Vault](#creating-a-vault)
  + [Adding Support for Metadata Views](#adding-support-for-metadata-views)
  + [Creating a Minter](#creating-a-minter)
* [Deploying the Contract](#deploying-the-contract)
* [Reading the Token's Total Supply](#reading-the-tokens-total-supply)
* [Giving Accounts the Ability to Receive Tokens](#giving-accounts-the-ability-to-receive-tokens)
* [Reading a Vault's Balance](#reading-a-vaults-balance)
* [Minting More Tokens](#minting-more-tokens)
* [Transferring Tokens Between Accounts](#transferring-tokens-between-accounts)
* [More](#more)
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

