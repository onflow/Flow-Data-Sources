# Source: https://cadence-lang.org/docs/tutorial/fungible-tokens




6. Fungible Token Tutorial | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
  + [1. First Steps](/docs/tutorial/first-steps)
  + [2. Hello World](/docs/tutorial/hello-world)
  + [3. Resource Contract Tutorial](/docs/tutorial/resources)
  + [4. Capability Tutorial](/docs/tutorial/capabilities)
  + [5.1 Non-Fungible Token Tutorial Part 1](/docs/tutorial/non-fungible-tokens-1)
  + [5.2 Non-Fungible Token Tutorial Part 2](/docs/tutorial/non-fungible-tokens-2)
  + [6. Fungible Token Tutorial](/docs/tutorial/fungible-tokens)
  + [7. Marketplace Setup](/docs/tutorial/marketplace-setup)
  + [8. Marketplace](/docs/tutorial/marketplace-compose)
  + [9. Voting Contract](/docs/tutorial/voting)
  + [10. Composable Resources](/docs/tutorial/resources-compose)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Tutorial
* 6. Fungible Token Tutorial
On this page
# 6. Fungible Token Tutorial

In this tutorial, we're going to deploy, store, and transfer fungible tokens.

---


tip

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/65b44962-32c8-49c4-8a69-e96475d5a780>](https://play.flow.com/65b44962-32c8-49c4-8a69-e96475d5a780)

The tutorial will ask you to take various actions to interact with this code.


Action

Instructions that require you to take action are always included in a callout
box like this one. These highlighted actions are all that you need to do to
get your code running, but reading the rest is necessary to understand the
language's design.

Some of the most popular contract classes on blockchains today are fungible tokens.
These contracts create homogeneous tokens that can be transferred to other users and spent as currency (e.g., ERC-20 on Ethereum).

In traditional software and smart contracts, balances for each user are tracked by a central ledger, such as a dictionary:

 `_13// DO NOT USE THIS CODE FOR YOUR PROJECT_13contract LedgerToken {_13 // Tracks every user's balance_13 access(contract) let balances: {Address: UFix64}_13_13 // Transfer tokens from one user to the other_13 // by updating their balances in the central ledger_13 access(all)_13 fun transfer(from: Address, to: Address, amount: UFix64) {_13 balances[from] = balances[from] - amount_13 balances[to] = balances[to] + amount_13 }_13}`

With Cadence, we use the new resource-oriented paradigm
to implement fungible tokens and avoid using a central ledger
because there are inherent problems with using a central ledger
that are detailed in [the Fungible Tokens section below.](#fungible-tokens-an-in-depth-exploration)

### Flow Network Token[​](#flow-network-token "Direct link to Flow Network Token")

In Flow, the native network token
[(FLOW) is implemented as a normal fungible token smart contract](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowToken.cdc)
using a smart contract similar to the one in this tutorial.

There are special transactions and hooks that allow it to be used for transaction execution fees, storage fees, and staking,
but besides that, developers and users are able to treat it and use it just like any other token in the network!

warning

It is important to remember that while this tutorial implements a working
fungible token, it has been simplified for educational purposes and is not
what any project should use in production. See the
[Flow Fungible Token standard](https://github.com/onflow/flow-ft)
for the standard interface and example implementation. You can also see the
[Fungible Token Developer Guide](https://developers.flow.com/build/guides/fungible-token)
for a guide for how to create a production ready version of a Fungible Token contract.

We're going to take you through these steps to get comfortable with the fungible token:

1. Deploy the fungible token contract to account `0x06`
2. Create a fungible token object and store it in your account storage.
3. Create a reference to your tokens that others can use to send you tokens.
4. Set up another account the same way.
5. Transfer tokens from one account to another.
6. Use a script to read the accounts' balances.

**Before proceeding with this tutorial**, we recommend following the instructions in [Getting Started](/docs/tutorial/first-steps)
and [Hello, World!](/docs/tutorial/hello-world) to learn the basics of the language and the playground.

# Fungible Tokens on the Flow Emulator

---


Action

First, you'll need to follow this link to open a playground session with the
Fungible Token contracts, transactions, and scripts pre-loaded:

[<https://play.flow.com/65b44962-32c8-49c4-8a69-e96475d5a780>](https://play.flow.com/65b44962-32c8-49c4-8a69-e96475d5a780)
Action

Open the account `0x06` tab to see the file named
`BasicToken.cdc`. `BasicToken.cdc` should contain the full code for the
fungible token, which provides the core functionality to store fungible tokens
in your account and transfer to and accept tokens from other users.

The concepts involved in implementing a fungible token in Cadence can be unfamiliar at first.
If you haven't completed and understood the previous tutorials,
please go back and complete those first because this tutorial will assume that you
understand a lot of the concepts explored in those tutorials.

For an in-depth explanation of this functionality and code, continue reading the next section.

Or, if you'd like to go immediately into deploying it and using it in the playground,
you can skip to the [Interacting with the Fungible Token](#interacting-with-the-fungible-token-in-the-flow-playground) section of this tutorial.

# Fungible Tokens: An In-Depth Exploration

---

How Flow implements fungible tokens is different from other programming languages. As a result:

* Ownership is decentralized and does not rely on a central ledger
* Bugs and exploits present less risk for users and less opportunity for attackers
* There is no risk of integer underflow or overflow
* Assets cannot be duplicated, and it is very hard for them to be lost, stolen, or destroyed
* Code can be composable
* Rules can be immutable
* Code is not unintentionally made public

## Decentralizing Ownership[​](#decentralizing-ownership "Direct link to Decentralizing Ownership")

---

Instead of using a central ledger system, Flow ties ownership to each account via a new paradigm for asset ownership.
The example below showcases how Solidity (the smart contract language for the Ethereum Blockchain, among others)
implements fungible tokens, with only the code for storage and transferring tokens shown for brevity.

ERC20.sol `_15contract ERC20 {_15 // Maps user addresses to balances, similar to a dictionary in Cadence_15 mapping (address => uint256) private _balances;_15_15 function _transfer(address sender, address recipient, uint256 amount) {_15 // ensure the sender has a valid balance_15 require(_balances[sender] >= amount);_15_15 // subtract the amount from the senders ledger balance_15 _balances[sender] = _balances[sender] - amount;_15_15 // add the amount to the recipient’s ledger balance_15 _balances[recipient] = _balances[recipient] + amount_15 }_15}`

As you can see, Solidity uses a central ledger system for its fungible tokens. There is one contract that manages the state of the tokens
and every time that a user wants to do anything with their tokens, they have to interact with the central ERC20 contract,
calling its functions to update their balance. This contract handles access control for all functionality, implements all of its own correctness checks,
and enforces rules for all of its users.

Instead of using a central ledger system, Flow utilizes a few different concepts
to provide better safety, security, and clarity for smart contract developers and users.
In this section, we'll show how Flow's resources, interfaces, and other features are employed via a fungible token example.

## Intuiting Ownership with Resources[​](#intuiting-ownership-with-resources "Direct link to Intuiting Ownership with Resources")

---

An important concept in Cadence is **Resources**, which are linear types.
A resource is a composite type (like a struct) that has its own defined fields and functions.
The difference is that resource objects have special rules that keep them from being copied or lost.
Resources are a new paradigm for asset ownership. Instead of representing token ownership in a central ledger smart contract,
each account owns its own resource object in its account storage that records the number of tokens they own.
This way, when users want to transact with each other, they can do so peer-to-peer without having to interact with a central token contract.
To transfer tokens to each other, they call a `transfer` function (or something equivalent)
on their own resource object and other users' resources, instead of a central `transfer` function.

This approach simplifies access control because instead of a central contract having to check the sender of a function call,
most function calls happen on resource objects stored in users' account,
and each user controls who is able to call the functions on resources in their account.
This concept, called Capability-based security, will be explained more in a later section.

This approach also helps protect against potential bugs. In a Solidity contract with all the logic and state contained in a central contract,
an exploit is likely to affect all users who are involved in the contract.

In Cadence, if there is a bug in the resource logic, an attacker would have to exploit the bug in each token holder's account individually,
which is much more complicated and time-consuming than it is in a central ledger system.

Below is an example of a resource for a fungible token vault. Every user who owns these tokens would have this resource stored in their account.
It is important to remember that each account stores only a copy of the `Vault` resource, and not a copy of the entire `ExampleToken` contract.
The `ExampleToken` contract only needs to be stored in the initial account that manages the token definitions.

Token.cdc `_22access(all)_22resource Vault: Provider, Receiver {_22_22 // Balance of a user's Vault_22 // we use unsigned fixed point numbers for balances_22 // because they can represent decimals and do not allow negative values_22 access(all) var balance: UFix64_22_22 init(balance: UFix64) {_22 self.balance = balance_22 }_22_22 access(Withdraw) fun withdraw(amount: UFix64): @Vault {_22 self.balance = self.balance - amount_22 return <-create Vault(balance: amount)_22 }_22_22 access(all) fun deposit(from: @Vault) {_22 self.balance = self.balance + from.balance_22 destroy from_22 }_22}`

This piece of code is for educational purposes and is not comprehensive. However, it still showcases how a resource for a token works.

### Token Balances and Initialization[​](#token-balances-and-initialization "Direct link to Token Balances and Initialization")

Each token resource object has a balance and associated functions (e.g., `deposit`, `withdraw`, etc).
When a user wants to use these tokens, they instantiate a zero-balance copy of this resource in their account storage.
The language requires that the initialization function `init`, which is only run once, must initialize all member variables.

 `_10// Balance of a user's Vault_10// we use unsigned fixed-point integers for balances because they do not require the_10// concept of a negative number and allow for more clear precision_10access(all) var balance: UFix64_10_10init(balance: UFix64) {_10 self.balance = balance_10}`

If you remove the `init` function from your `ExampleToken` contract, it will cause an error because
the balance field is no longer initialized.

### Deposit[​](#deposit "Direct link to Deposit")

Then, the deposit function is available for any account to transfer tokens to.

 `_10access(all) fun deposit(from: @Vault) {_10 self.balance = self.balance + from.balance_10 destroy from_10}`
### Transferring Tokens[​](#transferring-tokens "Direct link to Transferring Tokens")

When an account wants to send tokens to a different account, the sending account calls their own withdraw function first,
which subtracts tokens from their resource’s balance and temporarily creates a new resource object that holds this balance:

 `_10// Withdraw tokens from the signer's stored vault_10let sentVault <- vaultRef.withdraw(amount: amount)`

The sending account then calls the recipient account’s deposit function, which literally moves the resource instance to the other account,
adds it to their balance, and then destroys the used resource:

 `_10// Deposit the withdrawn tokens in the recipient's receiver_10receiverRef.deposit(from: <-sentVault)`

The resource needs to be destroyed because Cadence enforces strict rules around resource interactions.
A resource can never be left hanging in a piece of code. It either needs to be explicitly destroyed or stored in an account's storage.

When interacting with resources, you use the `@` symbol to specify the type, and a special “move operator” `<-`
when moving the resource, such as assigning the resource, when passing it as an argument to a function, or when returning it from a function.

 `_10access(all) fun withdraw(amount: UInt64): @Vault {`

This `@` symbol is required when specifying a resource **type** for a field, an argument, or a return value.
The move operator `<-` makes it clear that when a resource is used in an **assignment**, parameter, or return value,
it is moved to a new location and the old location is invalidated. This ensures that the resource only ever exists in one location at a time.

If a resource is moved out of an account's storage, it either needs to be moved to an account’s storage or explicitly destroyed.

 `_10destroy from`

This rule ensures that resources, which often represent real value, do not get lost because of a coding error.

You’ll notice that the arithmetic operations aren't explicitly protected against overflow or underflow.

 `_10self.balance = self.balance - amount`

In Solidity, this could be a risk for integer overflow or underflow, but Cadence has built-in overflow and underflow protection, so it is not a risk.
We are also using unsigned numbers in this example, so as mentioned earlier, the vault`s balance cannot go below 0.

Additionally, the requirement that an account contains a copy of the token’s resource type in its storage
ensures that funds cannot be lost by being sent to the wrong address.

If an address doesn’t have the correct resource type imported, the transaction will revert, ensuring that transactions sent to the wrong address are not lost.

**Important note: This protection is not in place for the Flow network currency,**
**because every Flow account is initialized with a default Flow Token Vault**
**in order to pay for [storage fees and transaction fees](https://developers.flow.com/build/basics/fees.md#fees).**

### Function Parameters[​](#function-parameters "Direct link to Function Parameters")

The line in `withdraw` that creates a new `Vault` has the parameter name `balance` specified in the function call.

 `_10return <-create Vault(balance: amount)`

This is another feature that Cadence uses to improve the clarity of code.
All function calls are required to specify the names of the arguments they are sending
unless the developer has specifically overridden the requirement in the funtion declaration.

## Interacting with the Fungible Token in the Flow Playground[​](#interacting-with-the-fungible-token-in-the-flow-playground "Direct link to Interacting with the Fungible Token in the Flow Playground")

Now that you have read about how the Fungible Token works,
we can deploy a basic version of it to your account and send some transactions to interact with it.

Action

Make sure that you have opened the Fungible Token templates in the playground
by following the link at the top of this page. You should have Account `0x06`
open and should see the code below.


 `_101/// BasicToken.cdc_101///_101/// The BasicToken contract is a sample implementation of a fungible token on Flow._101///_101/// Fungible tokens behave like everyday currencies -- they can be minted, transferred or_101/// traded for digital goods._101///_101/// This is a basic implementation of a Fungible Token and is NOT meant to be used in production_101/// See the Flow Fungible Token standard for real examples: https://github.com/onflow/flow-ft_101_101access(all) contract BasicToken {_101_101 access(all) entitlement Withdraw_101_101 access(all) let VaultStoragePath: StoragePath_101 access(all) let VaultPublicPath: PublicPath_101_101 /// Vault_101 ///_101 /// Each user stores an instance of only the Vault in their storage_101 /// The functions in the Vault are governed by the pre and post conditions_101 /// in the interfaces when they are called._101 /// The checks happen at runtime whenever a function is called._101 ///_101 /// Resources can only be created in the context of the contract that they_101 /// are defined in, so there is no way for a malicious user to create Vaults_101 /// out of thin air. A special Minter resource or constructor function needs to be defined to mint_101 /// new tokens._101 ///_101 access(all) resource Vault {_101_101 /// keeps track of the total balance of the account's tokens_101 access(all) var balance: UFix64_101_101 /// initialize the balance at resource creation time_101 init(balance: UFix64) {_101 self.balance = balance_101 }_101_101 /// withdraw_101 ///_101 /// Function that takes an integer amount as an argument_101 /// and withdraws that amount from the Vault._101 ///_101 /// It creates a new temporary Vault that is used to hold_101 /// the money that is being transferred. It returns the newly_101 /// created Vault to the context that called so it can be deposited_101 /// elsewhere._101 ///_101 access(Withdraw) fun withdraw(amount: UFix64): @Vault {_101 pre {_101 self.balance >= amount:_101 "BasicToken.Vault.withdraw: Cannot withdraw tokens! "_101 .concat("The amount requested to be withdrawn (").concat(amount.toString())_101 .concat(") is greater than the balance of the Vault (")_101 .concat(self.balance.toString()).concat(").")_101 }_101 self.balance = self.balance - amount_101 return <-create Vault(balance: amount)_101 }_101_101 /// deposit_101 ///_101 /// Function that takes a Vault object as an argument and adds_101 /// its balance to the balance of the owners Vault._101 ///_101 /// It is allowed to destroy the sent Vault because the Vault_101 /// was a temporary holder of the tokens. The Vault's balance has_101 /// been consumed and therefore can be destroyed._101 access(all) fun deposit(from: @Vault) {_101 self.balance = self.balance + from.balance_101 destroy from_101 }_101 }_101_101 /// createVault_101 ///_101 /// Function that creates a new Vault with an initial balance_101 /// and returns it to the calling context. A user must call this function_101 /// and store the returned Vault in their storage in order to allow their_101 /// account to be able to receive deposits of this token type._101 ///_101 access(all) fun createVault(): @Vault {_101 return <-create Vault(balance: 30.0)_101 }_101_101 /// The init function for the contract. All fields in the contract must_101 /// be initialized at deployment. This is just an example of what_101 /// an implementation could do in the init function. The numbers are arbitrary._101 init() {_101 self.VaultStoragePath = /storage/CadenceFungibleTokenTutorialVault_101 self.VaultPublicPath = /public/CadenceFungibleTokenTutorialReceiver_101 // create the Vault with the initial balance and put it in storage_101 // account.save saves an object to the specified `to` path_101 // The path is a literal path that consists of a domain and identifier_101 // The domain must be `storage`, `private`, or `public`_101 // the identifier can be any name_101 let vault <- self.createVault()_101 self.account.storage.save(<-vault, to: self.VaultStoragePath)_101 }_101}`
Action

Click the `Deploy` button at the top right of the editor to deploy the code.

![Deploy BasicToken on 0x06](/assets/images/deploy_basic_token-f95819cd399997e6a7f70bd0d9290a45.png)

This deployment stores the contract for the basic fungible token
in the selected account (account `0x06`) so that it can be imported into transactions.

A contract's `init` function runs at contract creation, and never again afterwards.
In our example, this function stores an instance of the `Vault` object with an initial balance of 30.

 `_10// create the Vault with the initial balance and put it in storage_10// account.save saves an object to the specified `to` path_10// The path is a literal path that consists of a domain and identifier_10// The domain must be `storage` or `public`_10// the identifier can be any string_10let vault <- self.createVault()_10self.account.save(<-vault, to: self.VaultStoragePath)`

This line saves the new `@Vault` object to storage.
Account storage is indexed with [paths](/docs/language/accounts/paths),
which consist of a domain and identifier. `/domain/identifier`.
Only two domains are allowed for paths:

* `storage`: The place where all objects are stored. Only accessible by the owner of the account.
* `public`: Stores links to objects in storage: Accessible by anyone in the network.

Contracts have access to the private `&Account` object of the account it is deployed to, using `self.account`.
This object has methods that can modify storage in many ways.
See the [account](/docs/language/accounts) documentation for a list of all the methods it can call.

In this line, we call the `storage.save` method to store an object in storage.
The first argument is the value to store, and the second argument is the path where the value is being stored.
For `storage.save` the path has to be in the `/storage/` domain.

You are now ready to run transactions that use the fungible tokens!

### Perform a Basic Transfer[​](#perform-a-basic-transfer "Direct link to Perform a Basic Transfer")

As we talked about above, a token transfer with resources is not a simple update to a ledger.
In Cadence, you have to first withdraw tokens from your vault, then deposit them to the vault
that you want to transfer to. We'll start a simple transaction that withdraws tokens from a vault
and deposits them back into the same vault.

Action

Open the transaction named `Basic Transfer`.

`Basic Transfer` should contain the following code for withdrawing and depositing with a stored Vault:


BasicTransfer.cdc `_28// Basic Transfer_28_28import BasicToken from 0x06_28_28// This transaction is used to withdraw and deposit tokens with a Vault_28_28transaction(amount: UFix64) {_28_28 prepare(signer: auth(BorrowValue) &Account) {_28_28 // Get a reference to the signer's stored vault_28 let vaultRef = signer.storage.borrow<auth(BasicToken.Withdraw) &BasicToken.Vault>_28 (from: BasicToken.VaultStoragePath)_28 ?? panic("Could not borrow a vault reference to 0x06's BasicToken.Vault"_28 .concat(" from the path ")_28 .concat(BasicToken.VaultStoragePath.toString())_28 .concat(". Make sure account 0x06 has set up its account ")_28 .concat("with an BasicToken Vault."))_28_28 // Withdraw tokens from the signer's stored vault_28 sentVault <- vaultRef.withdraw(amount: amount)_28_28 // Deposit the withdrawn tokens in the recipient's receiver_28 vaultRef.deposit(from: <-sentVault)_28_28 log("Withdraw/Deposit succeeded!")_28 }_28}`
Action

Select account `0x06` as the only signer.

You can enter any number less than 30.0 for the amount of tokens to transfer.

Click the `Send` button to submit the transaction.

This transaction withdraws tokens from the main vault and deposits them back
to it.

This transaction is a basic example of a transfer within an account.
It withdraws tokens from the main vault and deposits back to the main vault.
It is simply to illustrate the basic functionality of how transfers work.

You'll see in this transaction that
you can borrow a reference directly from an object in storage.

 `_10// Borrow a Withdraw reference to the signer's vault_10// Remember to always have descriptive error messages!_10let vaultRef = signer.storage.borrow<auth(BasicToken.Withdraw) &BasicToken.Vault>_10 (from: ExampleToken.VaultStoragePath)_10 ?? panic("Could not borrow a vault reference to 0x06's BasicToken.Vault"_10 .concat(" from the path ")_10 .concat(BasicToken.VaultStoragePath.toString())_10 .concat(". Make sure account 0x06 has set up its account ")_10 .concat("with an BasicToken Vault."))`

This allows you to efficiently access objects in storage without having to load them,
which is a much more costly interaction.

This code also uses entitlements (`auth(BasicToken.Withdraw)`)
to access the withdraw functionality through a reference.
Without entitlements, any privileged functionality would be able to be accessed
via a public capability because reference can be downcasted to their concrete reference types.
Therefore, functions with privileged functionality, like `withdraw()` here,
should have entitlements in order to be secure.

In production code, you'll likely be transferring tokens to other accounts.
Capabilities allow us to accomplish this safely.

## Ensuring Security in Public: Capability Security[​](#ensuring-security-in-public-capability-security "Direct link to Ensuring Security in Public: Capability Security")

---

Another important feature in Cadence is its utilization of [**Capability-Based Security.**](/docs/language/capabilities)

Cadence's security model ensures that objects stored in an account's storage can only be accessed by the account that owns them.
If a user wants to give another user access to their stored objects, they can link a public capability,
which is like an "API" that allows others to call specified functions on their objects.

An account only has access to the fields and methods of an object in a different account if they hold a capability to that object
that explicitly allows them to access those fields and methods with entitlements.

Only the owner of an object can create a capability for it and only the owner
can add entitlements to a capability.

Therefore, when a user creates a Vault in their account, they publish a capability
that exposes the `access(all)` fields and functions on the resource.
Here, those are `balance` and `deposit()`.

The withdraw function can remain hidden as a function that only the owner can call.

This removes the need to check the address of the account that made the function call
(`msg.sender` in Ethereum) for access control purposes, because this functionality
is handled by the protocol and the language's strong static type system.
If you aren't the owner of an object or don't have a valid reference to it
that was created by the owner, you cannot access the object at all!

### Using Pre and Post-Conditions to Secure Implementations[​](#using-pre-and-post-conditions-to-secure-implementations "Direct link to Using Pre and Post-Conditions to Secure Implementations")

---

The next important concept in Cadence is design-by-contract,
which uses pre-conditions and post-conditions to document and programmatically assert the change in state caused by a piece of a program.
These conditions are usually specified in [interfaces](/docs/language/interfaces) that enforce rules about how types are defined and behave.
They can be stored on-chain in an immutable fashion so that certain pieces of code
can import and implement them to ensure that they meet certain standards.

In our example, we don't use interfaces for simplicity,
but here is an example of how interfaces for the `Vault` resource we defined above would look.

Interfaces.cdc `_32// Interface that enforces the requirements for withdrawing_32// tokens from the implementing type_32//_32access(all) resource interface Provider {_32 access(Withdraw) fun withdraw(amount: UFix64): @Vault {_32 post {_32 // `result` refers to the return value_32 result.balance == amount:_32 "FungibleToken.Provider.withdraw: Cannot withdraw tokens!"_32 .concat("The balance of the withdrawn tokens (").concat(result.balance.toString())_32 .concat(") is not equal to the amount requested to be withdrawn (")_32 .concat(amount.toString()).concat(")")_32 }_32 }_32}_32// Interface that enforces the requirements for depositing_32// tokens into the implementing type_32//_32access(all) resource interface Receiver {_32_32 // There aren't any meaningful requirements for only a deposit function_32 // but this still shows that the deposit function is required in an implementation._32 access(all) fun deposit(from: @Vault)_32}_32_32// Balance_32//_32// Interface that specifies a public `balance` field for the vault_32//_32access(all) resource interface Balance {_32 access(all) var balance: UFix64_32}`

In production code, the `Vault` resource implements all three of these interfaces.
The interfaces ensure that specific fields and functions are present in the resource implementation
and that the function arguments, fields of the resource,
and any return value are in a valid state before and/or after execution.

These interfaces can be deployed on-chain and imported into other contracts or resources
so that these requirements are enforced by an immutable source of truth that is not susceptible to human error.

See the [Flow Fungible Token standard](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc)
for the interfaces that are used for real Fungible Token implementations!

## Adding Interfaces to Our Fungible Token[  ​](#adding-interfaces-to-our-fungible-token "Direct link to Adding Interfaces to Our Fungible Token")

Now, we are going to add these interfaces to our Fungible token along with a minter resource.

Open the `ExampleToken` contract.
In addition to everything that is in the `BasicToken` contract,
we have also added the `Provider`, `Receiver`, and `Balance` interfaces described above.

Now that our `ExampleToken.Vault` type has declared that it implements these interfaces,
it is required to have their fields and functions, and their pre and post-conditions will also
be evaluated every time their respective functions are called.

Additionally, `ExampleToken` changes `createVault()` to `createEmptyVault()`
so that token minting is restricted to the newly added `VaultMinter` resource.
This illustrates another powerful feature of Cadence resources.
Instead of the contract maintaining a list of minter addresses,
accounts that the owner wants to be minters can be giving a special resource
that directly gives them the authority to mint tokens.
This method for authorization can be used in many different ways
and further decentralizes the control of the contract.

We also store the `VaultMinter` object to `/storage/`
in the `init()` function in the same way as the vault, but in a different storage path:

 `_10self.account.storage.save(<-create VaultMinter(), to: /storage/CadenceFungibleTokenTutorialMinter)`

Now is an important time to remind you that account storage is not namespaced by contract,
meaning that path names could potentially conflict. This is why it is important to
choose unique names for your paths like we have done here so there is a very low chance
of them conflicting with other projects' paths.

## Create, Store, and Publish Capabilities and References to a Vault[​](#create-store-and-publish-capabilities-and-references-to-a-vault "Direct link to Create, Store, and Publish Capabilities and References to a Vault")

---

Capabilities are kind of like pointers in other languages.
They are a link to an object in an account's storage
and can be used to read fields or call functions on the object they reference.
They cannot move or modify the object directly.

There are many different situations in which you would create a capability to your fungible token vault.
You might want a simple way to call methods on your `Vault` from anywhere in a transaction.
You could also send a capability that only exposes withdraw function in your `Vault` so that others can transfer tokens for you.

There could also be a function that takes a capability to a `Vault` as an argument, borrows a reference to the capability,
makes a single function call on the reference, then finishes and destroys the reference.

We already use this pattern in the `VaultMinter` resource in the `mintTokens` function, shown here:

 `_14 // Function that mints new tokens and deposits into an account's vault_14 // using their `{Receiver}` reference._14 // We say `&{Receiver}` to say that the recipient can be any resource_14 // as long as it implements the Receiver interface_14 access(all) fun mintTokens(amount: UFix64, recipient: Capability<&{Receiver}>) {_14 let recipientRef = recipient.borrow()_14 ?? panic("ExampleToken.VaultMinter.mintTokens: Could not borrow a receiver reference to "_14 .concat("the specified recipient's ExampleToken.Vault"))_14 .concat(". Make sure the account has set up its account ")_14 .concat("with an ExampleToken Vault and valid capability."))_14_14 ExampleToken.totalSupply = ExampleToken.totalSupply + UFix64(amount)_14 recipientRef.deposit(from: <-create Vault(balance: amount))_14 }`

The function takes a capability as an argument.
This syntax might be unclear to you:

 `_10recipient: Capability<&{Receiver}>`

This means that `recipient` has to be a Capability that was created as the type contained in `<>`.
The type outside of the curly braces `{}` has to be a concrete type
and the type in the curly braces has to be an interface type.
Here we are saying that the type can be any resource that implements the `ExampleToken.Receiver` interface.
If that is true, this function borrows a reference from this capability
and uses the reference to call the `deposit` function of that resource because we know that
the `deposit` function will be there since it is in the `ExampleToken.Receiver` interface.

Let's create capabilities to your `Vault` so that a separate account can send tokens to you.

Action

Before we submit a transaction interacting with ExampleToken resources, we'll need to deploy the contract to account `0x07`:

1. Select `ExampleToken` in the playground sidebar
2. Make sure that signer `0x07` is selected as the deploying address
3. Click "Deploy"

![Deploy ExampleToken to 0x07](/assets/images/deploy_example_token-865486e839ca3c95db9e970f3477342d.png)

Now we can continue on to configure Capabilities on the ExampleToken Vault.

Action

Open the transaction named `Issue Capability`.

`Issue Capability` should contain the following code for creating a reference to the stored Vault:


issue\_capability.cdc `_31import ExampleToken from 0x07_31_31// This transaction creates a capability_31// that is linked to the account's token vault._31// The capability is restricted to the fields in the `Receiver` interface,_31// so it can only be used to deposit funds into the account._31transaction {_31 prepare(signer: auth(IssueStorageCapabilityController, PublishCapability) &Account) {_31_31 // Create a link to the Vault in storage that is restricted to the_31 // fields and functions in `Receiver` and `Balance` interfaces,_31 // this only exposes the balance field_31 // and deposit function of the underlying vault._31 let receiverCap = signer.capabilities.storage.issue<&{ExampleToken.Receiver, ExampleToken.Balance}>(_31 ExampleToken.VaultStoragePath_31 )_31 signer.capabilities.publish(receiverCap, at: ExampleToken.VaultPublicPath)_31_31 log("Public Receiver reference created!")_31 }_31_31 post {_31 // Check that the capabilities were created correctly_31 // by getting the public capability and checking_31 // that it points to a valid `Vault` object_31 // that implements the `Receiver` interface_31 getAccount(0x07).capabilities.get<&{ExampleToken.Receiver}>(ExampleToken.VaultPublicPath)_31 .check():_31 "Vault Receiver Reference was not created correctly"_31 }_31}`

In order to use a capability, we have to first issue a link to that object in storage.
A reference can then be created from a capability, and references cannot be stored.
They need to be lost at the end of a transaction execution.

To create a capability, we use the `account.capabilities.issue` function.

 `_10// Create a capability to the Vault in storage that is restricted to the_10// fields and functions in `Receiver` and `Balance` interfaces,_10// this only exposes the balance field_10// and deposit function of the underlying vault._10//_10let receiverCap = signer.capabilities.storage.issue<&ExampleToken.Vault>(_10 ExampleToken.VaultStoragePath_10)_10signer.capabilities.publish(receiverCap, at: ExampleToken.VaultPublicPath)`

`issue` creates a new capability that is targeting the storage `target` in the second argument.
The type restriction for the link is specified in the `<>`. We use `&{ExampleToken.Receiver, ExampleToken.Balance}`
to say that the link can be any resource as long as it implements and is cast as the Receiver interface.
This is the common format for describing references.
You first have a `&` followed by the concrete type, then the interface in curly braces to ensure that
it is a reference that implements that interface and only includes the fields specified in that interface.

We publish the capability in `ExampleToken.VaultPublicPath` because we want it to be publicly accessible.
The `public` domain of an account is accessible to anyone in the network via an account's
public `&Account` reference, which is fetched by using the `getAccount(address)` function.

Next is the `post` phase of the transaction.

 `_10post {_10// Check that the capabilities were created correctly_10// by getting the public capability and checking_10// that it points to a valid `Vault` object_10// that implements the `Receiver` interface_10getAccount(0x07).capabilities.get<&{ExampleToken.Receiver}>(ExampleToken.VaultPublicPath)_10 .check():_10 "Vault Receiver Reference was not created correctly"_10}`

The `post` phase is for ensuring that certain conditions are met after the transaction has been executed.
Here, we are getting the capability from its public path and calling its `check` function to ensure
that the capability contains a valid link to a valid object in storage that is the specified type.

Action

Now that we understand the transaction, time to submit it:

1. Select account `0x07` as the only signer.
2. Click the `Send` button to submit the transaction.
3. This transaction creates a new public capability to your `Vault`
   and checks that it was created correctly.
## Transfer Tokens to Another User[​](#transfer-tokens-to-another-user "Direct link to Transfer Tokens to Another User")

---

Now, we are going to run a transaction that sends 10 tokens to account `0x08`.
We will do this by calling the `withdraw` function on account `0x07`'s Vault,
which creates a temporary Vault object for moving the tokens,
then deposits those tokens into account `0x08`'s vault by calling the `deposit` function on their vault.

Action

Account `0x08` has not been set up to receive tokens, so we will do that now:

1. Open the transaction `Setup Account`.
2. Select account `0x08` as the only signer.
3. Click the `Send` button to set up account `0x08` so that it can receive tokens.

SetupAccount.cdc `_31// Setup Account_31_31import ExampleToken from 0x07_31_31// This transaction configures an account to store and receive tokens defined by_31// the ExampleToken contract._31transaction {_31 prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_31 // Create a new empty Vault object_31 let vaultA <- ExampleToken.createEmptyVault()_31_31 // Create a new ExampleToken Vault and put it in storage_31 signer.storage.save(<-vaultA, to: ExampleToken.VaultStoragePath)_31_31 log("Empty Vault stored")_31_31 // Create a public Receiver capability to the Vault_31 let receiverCap = signer.capabilities.storage.issue<&ExampleToken.Vault>(_31 ExampleToken.VaultStoragePath_31 )_31 signer.capabilities.publish(receiverCap, at: ExampleToken.VaultPublicPath)_31_31 log("References created")_31 }_31_31 post {_31 getAccount(0x08).capabilities.get<&{ExampleToken.Receiver}>(ExampleToken.VaultPublicPath)_31 .check():_31 "Vault Receiver Reference was not created correctly"_31 } _31}`

Here we perform the same actions that account `0x07` did to set up its `Vault`, but all in one transaction.
Account `0x08` is ready to start building its fortune! As you can see, when we created the Vault for account `0x08`,
we had to create one with a balance of zero by calling the `createEmptyVault()` function.
Resource creation is restricted to the contract where it is defined, so in this way, the Fungible Token smart contract can ensure that
nobody is able to create new tokens out of thin air.

As part of the initial deployment process for the ExampleToken contract, account `0x07` created a `VaultMinter` object.
By using this object, the account that owns it can mint new tokens.
Right now, account `0x07` owns it, so it has sole power to mint new tokens.
We could have had a `mintTokens` function defined in the contract,
but then we would have to check the sender of the function call to make sure that they are authorized,
which is not the recommended way to perform access control in Cadence.

As we explained before, the resource model plus capability security
handles this access control for us as a built in language construct
instead of having to be defined in the code.
If account `0x07` wanted to authorize another account to mint tokens,
they could either move the `VaultMinter` object to the other account,
or give the other account a private capability to the single `VaultMinter`.
Or, if they didn't want minting to be possible after deployment,
they would simply mint all the tokens at contract initialization
and not even include the `VaultMinter` in the contract.

In the next transaction, account `0x07` will mint 30 new tokens and deposit them into account `0x08`'s newly created Vault.

Action

1. Open the `Mint Tokens` transaction.
2. Select only account `0x07` as a signer and send `Mint Tokens` to mint 30 tokens for account `0x08`.

`Mint Tokens` should contain the code below.

mint\_tokens.cdc `_38// Mint Tokens_38_38import ExampleToken from 0x07_38_38// This transaction mints tokens and deposits them into account 3's vault_38transaction {_38_38 // Local variable for storing the reference to the minter resource_38 let mintingRef: &ExampleToken.VaultMinter_38_38 // Local variable for storing the reference to the Vault of_38 // the account that will receive the newly minted tokens_38 var receiver: Capability<&{ExampleToken.Receiver}>_38_38 prepare(signer: auth(BorrowValue) &Account) {_38 // Borrow a reference to the stored, private minter resource_38 self.mintingRef = signer.storage.borrow<&ExampleToken.VaultMinter>(from: /storage/CadenceFungibleTokenTutorialMinter)_38 ?? panic("Could not borrow a reference to the signer's ExampleToken.VaultMinter"_38 .concat(" from the path /storage/CadenceFungibleTokenTutorialMinter")_38 .concat(". Make sure you have deployed ExampleToken to 0x07 ")_38 .concat("and are signing with account 0x07."))_38_38 // Get the public account object for account 0x08_38 let recipient = getAccount(0x08)_38_38 // Get their public receiver capability_38 self.receiver = recipient.capabilities.get<&{ExampleToken.Receiver}>_38(ExampleToken.VaultPublicPath)_38_38 }_38_38 execute {_38 // Mint 30 tokens and deposit them into the recipient's Vault_38 self.mintingRef.mintTokens(amount: 30.0, recipient: self.receiver)_38_38 log("30 tokens minted and deposited to account 0x08")_38 }_38}`

This is an example of a transaction where we utilize local transaction variables
that span different stages in the transaction.
We declare the `mintingRef` and `receiverRef` variables outside of the prepare stage
but must initialize them in `prepare`.
We can then use them in later stages in the transaction.

Then we borrow a reference to the `VaultMinter`. We specify the borrow as a `VaultMinter` reference
and have the reference point to `/storage/CadenceFungibleTokenTutorialMinter`.
The reference is borrowed as an optional so we use the nil-coalescing operator (`??`) to make sure the value isn't `nil`.
If the value is `nil`, the transaction will execute the code after the `??`.
The code is a panic, so it will revert and print the descriptive error message.

You can use the `getAccount()` built-in function to get any account's public account object.
The public account object lets you get capabilities from the `public` domain of an account, where public capabilities are stored.

We use the `account.capabilities.get` function to get the public capability from a public path.

 `_10// Get the public receiver capability_10let cap = recipient.capabilities.get(ExampleToken.VaultPublicPath)`

In the execute phase, we simply use the reference to mint 30 tokens and deposit them into the `Vault` of account `0x08`.

## Check Account Balances[​](#check-account-balances "Direct link to Check Account Balances")

Now, both account `0x07` and account `0x08` should have a `Vault` object in their storage that has a balance of 30 tokens.
They both should also have a `Receiver` capability stored in their `/public/` domains that links to their stored `Vault`.

![](https://storage.googleapis.com/flow-resources/documentation-assets/cadence-tuts/account-balances.png)

An account cannot receive any token type unless it is specifically configured to accept those tokens.
As a result, it is difficult to send tokens to the wrong address accidentally.
But, if you make a mistake setting up the `Vault` in the new account, you won't be able to send tokens to it.

Let's run a script to make sure we have our vaults set up correctly.

You can use scripts to access an account's public state. Scripts aren't signed by any account and cannot modify state.

In this example, we will query the balance of each account's vault. The following will print out the balance of each account in the emulator.

Action

Open the script named `Get Balances` in the scripts pane.

`Get Balances` should contain the following code:

get\_balances.cdc `_34// Get Balances_34_34import ExampleToken from 0x07_34_34// This script reads the Vault balances of two accounts._34access(all)_34fun main() {_34 // Get the accounts' public account objects_34 let acct7 = getAccount(0x07)_34 let acct8 = getAccount(0x08)_34_34 // Get references to the account's receivers_34 // by getting their public capability_34 // and borrowing a reference from the capability_34 let acct7ReceiverRef = acct7.capabilities.get<&{ExampleToken.Balance}>(ExampleToken.VaultPublicPath)_34 .borrow()_34 ?? panic("Could not borrow a balance reference to "_34 .concat("0x07's ExampleToken.Vault")_34 .concat(". Make sure 0x07 has set up its account ")_34 .concat("with an ExampleToken Vault and valid capability."))_34_34 let acct8ReceiverRef = acct8.capabilities.get<&{ExampleToken.Balance}>(ExampleToken.VaultPublicPath)_34 .borrow()_34 ?? panic("Could not borrow a balance reference to "_34 .concat("0x08's ExampleToken.Vault")_34 .concat(". Make sure 0x08 has set up its account ")_34 .concat("with an ExampleToken Vault and valid capability."))_34_34 // Use optional chaining to read and log balance fields_34 log("Account 0x07 Balance")_34 log(acct7ReceiverRef.balance)_34 log("Account 0x08 Balance")_34 log(acct8ReceiverRef.balance)_34}`
Action

Execute `Get Balances` by clicking the Execute button.

This should ensure the following:

* Account `0x07`'s balance is 30
* Account `0x08`'s balance is 30

If correct, you should see the following lines:

 `_10"Account 1 Balance"_1030_10"Account 2 Balance"_1030_10Result > "void"`

If there is an error, this probably means that you missed a step earlier
and might need to restart from the beginning.

To restart the playground, close your current session and open the link at the top of the tutorial.

Now that we have two accounts, each with a `Vault`, we can see how they transfer tokens to each other!

Action

1. Open the transaction named `Transfer Tokens`.
2. Select account `0x08` as a signer and send the transaction.
3. `Transfer Tokens` should contain the following code for sending tokens to another user:

transfer\_tokens.cdc `_44// Transfer Tokens_44_44import ExampleToken from 0x07_44_44// This transaction is a template for a transaction that_44// could be used by anyone to send tokens to another account_44// that owns a Vault_44transaction {_44_44 // Temporary Vault object that holds the balance that is being transferred_44 var temporaryVault: @ExampleToken.Vault_44_44 prepare(signer: auth(BorrowValue) &Account) {_44 // withdraw tokens from your vault by borrowing a reference to it_44 // and calling the withdraw function with that reference_44 let vaultRef = signer.storage.borrow<auth(ExampleToken.Withdraw) &ExampleToken.Vault>(from: ExampleToken.VaultStoragePath)_44 ?? panic("Could not borrow a vault reference to 0x08's ExampleToken.Vault"_44 .concat(" from the path ")_44 .concat(ExampleToken.VaultStoragePath.toString())_44 .concat(". Make sure account 0x06 has set up its account ")_44 .concat("with an ExampleToken Vault."))_44_44 self.temporaryVault <- vaultRef.withdraw(amount: 10.0)_44 }_44_44 execute {_44 // get the recipient's public account object_44 let recipient = getAccount(0x07)_44_44 // get the recipient's Receiver reference to their Vault_44 // by borrowing the reference from the public capability_44 let receiverRef = recipient.capabilities.get<&{ExampleToken.Receiver}>(ExampleToken.VaultPublicPath)_44 .borrow()_44 ?? panic("Could not borrow a receiver reference to "_44 .concat("0x07's ExampleToken.Vault")_44 .concat(". Make sure 0x07 has set up its account ")_44 .concat("with an ExampleToken Vault and valid capability."))_44_44 // deposit your tokens to their Vault_44 receiverRef.deposit(from: <-self.temporaryVault)_44_44 log("Transfer succeeded!")_44 }_44}`

In this example, the signer withdraws tokens from their `Vault` using an **entitled reference**,
which creates and returns a temporary `Vault` resource object with `balance=10`
that is used for transferring the tokens. In the execute phase,
the transaction moves that resource to another user's `Vault` using their `deposit` method.
The temporary `Vault` is destroyed after its balance is added to the recipient's `Vault`.

You might be wondering why we have to use two function calls to complete a token transfer when it is possible to do it in one.
This is because of the way resources work in Cadence.
In a ledger-based model, you would just call transfer, which just updates the ledger,
but in Cadence, the location of the tokens matters,
and therefore most token transfer situations will not just be a direct account-to-account transfer.

Most of the time, tokens will be used for a different purpose first,
like purchasing something, and that requires the `Vault` to be separately sent
and verified before being deposited to the storage of an account.

Separating the two also allows us to take advantage of being able
to statically verify which parts of accounts can be modified in the `prepare` section of a transaction,
which will help users have peace of mind when getting fed transactions to sign from an app.

Action

Execute `Get Balances` again.

If correct, you should see the following lines indicating that account `0x07`'s balance is 40 and account `0x08`'s balance is 20:

 `_10"Account 2 Balance"_1040_10"Account 3 Balance"_1020_10Result > "void"`

You now know how a basic fungible token is used in Cadence and Flow!

From here, you could try to extend the functionality of fungible tokens by making:

* A faucet for these tokens
* An escrow that can be deposited to (but only withdrawn when the balance reaches a certain point)
* A function to the resource that mints new tokens!

## Create a Flow Marketplace[​](#create-a-flow-marketplace "Direct link to Create a Flow Marketplace")

---

Now that you have an understanding of how fungible tokens work on Flow and have a working NFT, you can learn how to create
a marketplace that uses both fungible tokens and NFTs. Move on to the next tutorial to learn about Marketplaces in Cadence!

**Tags:**

* [reference](/docs/tags/reference)
* [Fungible Token](/docs/tags/fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/06-fungible-tokens.md)[Previous5.2 Non-Fungible Token Tutorial Part 2](/docs/tutorial/non-fungible-tokens-2)[Next7. Marketplace Setup](/docs/tutorial/marketplace-setup)
###### Rate this page

😞😐😊

* [Flow Network Token](#flow-network-token)
* [Decentralizing Ownership](#decentralizing-ownership)
* [Intuiting Ownership with Resources](#intuiting-ownership-with-resources)
  + [Token Balances and Initialization](#token-balances-and-initialization)
  + [Deposit](#deposit)
  + [Transferring Tokens](#transferring-tokens)
  + [Function Parameters](#function-parameters)
* [Interacting with the Fungible Token in the Flow Playground](#interacting-with-the-fungible-token-in-the-flow-playground)
  + [Perform a Basic Transfer](#perform-a-basic-transfer)
* [Ensuring Security in Public: Capability Security](#ensuring-security-in-public-capability-security)
  + [Using Pre and Post-Conditions to Secure Implementations](#using-pre-and-post-conditions-to-secure-implementations)
* [Adding Interfaces to Our Fungible Token](#adding-interfaces-to-our-fungible-token)
* [Create, Store, and Publish Capabilities and References to a Vault](#create-store-and-publish-capabilities-and-references-to-a-vault)
* [Transfer Tokens to Another User](#transfer-tokens-to-another-user)
* [Check Account Balances](#check-account-balances)
* [Create a Flow Marketplace](#create-a-flow-marketplace)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

