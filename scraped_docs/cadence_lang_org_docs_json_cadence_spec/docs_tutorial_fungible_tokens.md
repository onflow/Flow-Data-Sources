# Source: https://cadence-lang.org/docs/tutorial/fungible-tokens




Fungible Tokens | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
  + [First Steps](/docs/tutorial/first-steps)
  + [Hello World](/docs/tutorial/hello-world)
  + [Resources and the Move (<-) Operator](/docs/tutorial/resources)
  + [Capabilities](/docs/tutorial/capabilities)
  + [Basic NFT](/docs/tutorial/non-fungible-tokens-1)
  + [Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)
  + [Fungible Tokens](/docs/tutorial/fungible-tokens)
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
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Tutorial
* Fungible Tokens
On this page
# Fungible Tokens

Some of the most popular contract classes on blockchains today are fungible tokens.
These contracts create homogeneous tokens that can be transferred to other users and spent as currency (e.g., ERC-20 on Ethereum).

In traditional software and smart contracts, balances for each user are tracked by a central ledger, such as a dictionary:

 `_13// BAD CODE EXAMPLE. DO NOT USE THIS CODE FOR YOUR PROJECT_13contract LedgerToken {_13 // Tracks every user's balance_13 access(contract) let balances: {Address: UFix64}_13_13 // Transfer tokens from one user to the other_13 // by updating their balances in the central ledger_13 access(all)_13 fun transfer(from: Address, to: Address, amount: UFix64) {_13 balances[from] = balances[from] - amount_13 balances[to] = balances[to] + amount_13 }_13}`

With Cadence, we use the new resource-oriented paradigm to implement fungible tokens and avoid using a central ledger, because there are inherent problems with using a central ledger that are detailed in [the Fungible Tokens section below].

warning

This tutorial implements a working fungible token, but it has been simplified for educational purposes and is not what you should use in production.

If you've found this tutorial looking for information on how to implement a real token, see the [Flow Fungible Token standard](https://github.com/onflow/flow-ft) for the standard interface and example implementation, and the [Fungible Token Developer Guide](https://developers.flow.com/build/guides/fungible-token) for a details on creating a production ready version of a Fungible Token contract.

In this tutorial, we're going to deploy, store, and transfer fungible tokens.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Compare and contrast how tokens are stored in Flow Cadence compared to Ethereum.
* Utilize the `UFix64` type to allow decimals without converting back and forth with 10^18.
* Implement a vault [resource](/docs/language/resources) to manage the functionality needed for fungible tokens
* Use [interfaces](/docs/language/interfaces) to enforce the presence of specified functions and fields.
* Write transactions to transfer tokens safely from one account to another.
* Develop scripts to read account balances.
* Use preconditions and postconditions to perform checks before or after a function call completes.

## Flow Network Token[​](#flow-network-token "Direct link to Flow Network Token")

In Flow, the [native network token (FLOW)](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowToken.cdc) is implemented as a normal fungible token smart contract using a smart contract similar to the one you'll build in this tutorial.

There are special transactions and hooks that allow it to be used for transaction execution fees, storage fees, and staking, but besides that, developers and users are able to treat it and use it just like any other token in the network!

## Fungible Tokens on Flow[​](#fungible-tokens-on-flow "Direct link to Fungible Tokens on Flow")

Flow implements fungible tokens differently than other programming languages. As a result:

* Ownership is decentralized and does not rely on a central ledger
* Bugs and exploits present less risk for users and less opportunity for attackers
* There is no risk of integer underflow or overflow
* Assets cannot be duplicated, and it is very hard for them to be lost, stolen, or destroyed
* Code can be composable
* Rules can be immutable
* Code is not unintentionally made public

### Fungible tokens on Ethereum[​](#fungible-tokens-on-ethereum "Direct link to Fungible tokens on Ethereum")

The example below showcases how Solidity (the smart contract language for the Ethereum Blockchain, among others) implements fungible tokens, with only the code for storage and transferring tokens shown for brevity.

ERC20.sol `_15contract ERC20 {_15 // Maps user addresses to balances, similar to a dictionary in Cadence_15 mapping (address => uint256) private _balances;_15_15 function _transfer(address sender, address recipient, uint256 amount) {_15 // ensure the sender has a valid balance_15 require(_balances[sender] >= amount);_15_15 // subtract the amount from the senders ledger balance_15 _balances[sender] = _balances[sender] - amount;_15_15 // add the amount to the recipient's ledger balance_15 _balances[recipient] = _balances[recipient] + amount_15 }_15}`

As you can see, Solidity uses a central ledger system for its fungible tokens. There is one contract that manages the state of the tokens and every time that a user wants to do anything with their tokens, they have to interact with the central ERC20 contract. This contract handles access control for all functionality, implements all of its own correctness checks, and enforces rules for all of its users.

If there's a bug, such as accidentally making the `_transfer` function public, an attacker can immediately exploit the entire contract and the tokens owned by all users.

### Intuiting Ownership with Resources[​](#intuiting-ownership-with-resources "Direct link to Intuiting Ownership with Resources")

Instead of using a central ledger system, Flow utilizes a few different concepts to provide better safety, security, and clarity for smart contract developers and users. Primarily, tokens are stored in each user's vault, which is a [resource](/docs/language/resources) similar to the collection you created to store NFTs in the previous tutorial.

This approach simplifies access control because instead of a central contract having to check the sender of a function call, most function calls happen on resource objects stored in users' accounts, and each user natively has sole control over the resources stored in their accounts.

This approach also helps protect against potential bugs. In a Solidity contract with all the logic and state contained in a central contract, an exploit is likely to affect all users who are involved in the contract.

In Cadence, if there is a bug in the resource logic, an attacker would have to exploit the bug in each token holder's account individually, which is much more complicated and time-consuming than it is in a central ledger system.

## Constructing a Vault[​](#constructing-a-vault "Direct link to Constructing a Vault")

Our vault will be a simplified version of the one found in the [Flow Fungible Token standard](https://github.com/onflow/flow-ft). We'll follow some of the same practices, including using [interfaces](/docs/language/interfaces) to standardize the properties of our vault and make it easier for other contracts to interact with it.

Action

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/359cf1a1-63cc-4774-9c09-1b63ed83379b>](https://play.flow.com/359cf1a1-63cc-4774-9c09-1b63ed83379b)

In `ExampleToken.cdc`, you'll see:

ExampleToken.cdc `_13access(all) contract ExampleToken {_13_13 access(all) entitlement Withdraw_13_13 access(all) let VaultStoragePath: StoragePath_13 access(all) let VaultPublicPath: PublicPath_13_13 _13 init() {_13 self.VaultStoragePath = /storage/CadenceFungibleTokenTutorialVault_13 self.VaultPublicPath = /public/CadenceFungibleTokenTutorialReceiver_13 }_13}`

Before you can add your vault, you'll need to implement the various pieces it will depend on.

### Supply and Balance[​](#supply-and-balance "Direct link to Supply and Balance")

The two most basic pieces of information for a fungible token are a method of tracking the balance of a given user, and the total supply for the token. In Cadence, you'll usually want to use `UFix64` - a [fixed-point number](/docs/language/values-and-types#fixed-point-numbers).

Fixed-point numbers are essentially integers with a scale, represented by a decimal point. They make it much easier to work with money-like numbers as compared to endlessly handling conversions to and from the 10^18 representation of a value.

Action

Implement a contract-level [fixed-point number](/docs/language/values-and-types#fixed-point-numbers) to track the `totalSupply` of the token.


 `_10access(all) var totalSupply: UFix64`
### Interfaces[​](#interfaces "Direct link to Interfaces")

You'll also need a place to store the `balance` of any given user's vault. You **could** simply add a variable in the vault [resource](/docs/language/resources) definition to do this and it would work just fine.

Instead, let's use this opportunity to create some [interface]s.

In Cadence, interfaces are abstract types used to specify behavior in types that *implement* the interface. Using them helps compatibility and composability by breaking larger constructions down into standardized parts that can be used by more than one contract for more than one use case. For example, the interface we'll create for `Receiver` is used by the vault, but it's also something you'd use for any other resource that needs to be able to receive tokens - such as a contract that pools a collection of tokens and splits them between several addresses.

You'll create three interfaces, to handle the three functional areas of the vault:

* A `Balance` interface for the balance of tokens stored in the vault
* A `Provider` interface that can provide tokens by withdrawing them from the vault
* A `Receiver` interface that can safely deposit tokens from one vault into another

Action

First, create a `Balance` interface, requiring a public `UFix64` called `balance`. It should be public.


 `_10access(all) resource interface Balance {_10 access(all) var balance: UFix64_10}`

This one is pretty simple. It just defines the type of variable anything implementing it will need to have to keep track of a token balance.

Action

Next, create the `Provider` `interface`. In it, define a `withdraw` function. It should have the `Withdraw` access [entitlement](/docs/language/access-control), accept an argument for `amount`, and return a `Vault` resource type. This should also be public.

To prevent an error, stub out the `Vault` resource as well.


 `_10access(all) resource interface Provider {_10 access(Withdraw) fun withdraw(amount: UFix64): @Vault {}_10}_10_10access(all) resource Vault {}`

This [interface] will require resources implementing it to have a `withdraw` function, but it doesn't provide any limitations to how that function works. For example, it could be implemented such that the amount of tokens returned is double the withdrawn amount. While there might be a use case for that effect, it's not what you want for a normal token standard.

You can allow for flexibility, such as allowing a `Provider` to select randomly from several vaults to determine the payer, while enforcing that the amount withdrawn is appropriate by adding a `post` condition to the function. [Function preconditions and postconditions](/docs/language/functions#function-preconditions-and-postconditions) can be used to restrict the inputs and outputs of a function.

In a postcondition, the special constant `result` is used to reference the `return` of the function. They're written following the rules of [statements](/docs/language/syntax#semicolons) and can contain multiple conditions. Optionally, a `:` can be added after the last statement, containing an error message to be passed if the postcondition fails.

Action

Add a `post` condition that returns a descriptive and nicely formatted error if the amount returned in the vault from the function doesn't match the `amount` passed into the function.


 `_10access(Withdraw) fun withdraw(amount: UFix64): @Vault {_10 post {_10 result.balance == amount:_10 "ExampleToken.Provider.withdraw: Cannot withdraw tokens!"_10 .concat("The balance of the withdrawn tokens (").concat(result.balance.toString())_10 .concat(") is not equal to the amount requested to be withdrawn (")_10 .concat(amount.toString()).concat(")")_10 }_10}`

This `post` condition will be added automatically to the `withdraw` function in a resource implementing `Provider`.

Action

Finally, implement an [interface] called `Receiver`, containing a function called `deposit` that accepts a `Vault`.

::

 `_10access(all) resource interface Receiver {_10 access(all) fun deposit(from: @Vault)_10}`
## Implementing the Vault[​](#implementing-the-vault "Direct link to Implementing the Vault")

You're finally ready to implement the vault.

Action

Start by declaring a type for a `Vault` that implements `Balance`, `Provider`, and `Receiver`.


 `_10access(all) resource Vault: Balance, Provider, Receiver {_10 // TODO_10}`

You'll get errors:

 `_10resource `ExampleToken.Vault` does not conform to resource interface `ExampleToken.Balance`. `ExampleToken.Vault` is missing definitions for members: Balance`

And similar errors for `Provider` and `Receiver`. Similar to inheriting from a virtual class in other languages, implementing the interfaces requires you to implement the properties from those interfaces in your resource.

Action

Implement `balance`. You'll also need to initialize it. Initialize it with the `balance` passed into the `init` for the resource itself.

The pattern we're setting up here let's us create vaults and give them a `balance` in one go. Doing so is useful for several tasks, as creating a temporary `Vault` to hold a balance during a transaction also creates most of the functionality you need to do complex tasks with that balance.

For example, you might want to set up a conditional transaction that `deposit`s the balance in the vaults in different addresses based on whether or not a part of the transaction is successful.

 `_10access(all) var balance: UFix64_10_10init(balance: UFix64) {_10 self.balance = balance_10}`
Action

Next, implement `withdraw` function. It should contain a precondition that validates that the user actually possesses equal to or greater the number of tokens they are withdrawing.

While this functionality is probably something we'd want in every vault, we can't put the requirement in the [interface], because the interface doesn't have access to the `balance`.

 `_11access(Withdraw) fun withdraw(amount: UFix64): @Vault {_11 pre {_11 self.balance >= amount:_11 "ExampleToken.Vault.withdraw: Cannot withdraw tokens! "_11 .concat("The amount requested to be withdrawn (").concat(amount.toString())_11 .concat(") is greater than the balance of the Vault (")_11 .concat(self.balance.toString()).concat(").")_11 }_11 self.balance = self.balance - amount_11 return <-create Vault(balance: amount)_11}`
Action

Finally, implement the `deposit` function. Depositing should move the entire balance from the provided vault, and then `destroy` it.


 `_10access(all) fun deposit(from: @Vault) {_10 self.balance = self.balance + from.balance_10 destroy from_10}`

You **must** do something with the `Vault` resource after it's moved into the function. You can `destroy` it, because it's now empty, and you don't need it anymore.

## Vault Creation[​](#vault-creation "Direct link to Vault Creation")

We'll need a way to create empty vaults to onboard new users, or to create vaults for a variety of other uses.

Action

Add a function to `create` an empty `Vault`.


 `_10access(all) fun createEmptyVault(): @Vault {_10 return <-create Vault(balance: 0.0)_10}`

We'll use this when we create a transaction to set up new users.

## Error Handling[​](#error-handling "Direct link to Error Handling")

As before, you can anticipate some of the errors that other developers building transactions and scripts that interact with your contract might encounter. At the very least, it's likely that there will be many instances that an attempt is made to borrow a `Vault` that is not present, or lacks a capability for the caller to borrow it.

Action

Add a function to generate a helpful error if an attempt to borrow a `Vault` fails.


 `_10access(all) fun vaultNotConfiguredError(address: Address): String {_10 return "Could not borrow a collection reference to recipient's ExampleToken.Vault"_10 .concat(" from the path ")_10 .concat(ExampleToken.VaultPublicPath.toString())_10 .concat(". Make sure account ")_10 .concat(address.toString())_10 .concat(" has set up its account ")_10 .concat("with an ExampleToken Vault.")_10}`
## Minting[​](#minting "Direct link to Minting")

Next, you need a way to actually create, or mint, tokens. For this example, we'll define a `VaultMinter` resource that has the power to mint and airdrop tokens to any address that possesses a vault, or at least something with the `Receiver` [interface] for this token.
Only the owner of this resource will be able to mint tokens.

To do so, we use [capability](/docs/language/capabilities) with a reference to the resource or interface we want to require as the type: `Capability<&{Receiver}>`

Action

Define a public [resource](/docs/language/resources) with a public function `mintTokens` that accepts an `amount` of tokens to mint, and a `recipient` that must possess the `Receiver` [capability](/docs/language/capabilities).


 `_10access(all) resource VaultMinter {_10 access(all) fun mintTokens(amount: UFix64, recipient: Capability<&{Receiver}>) {_10 let recipientRef = recipient.borrow()_10 ?? panic(ExampleToken.vaultNotConfiguredError(address: recipient.address))_10_10 ExampleToken.totalSupply = ExampleToken.totalSupply + UFix64(amount)_10 recipientRef.deposit(from: <-create Vault(balance: amount))_10 }_10}`
## Final Contract Setup[​](#final-contract-setup "Direct link to Final Contract Setup")

The last task with the contract is to update the `init` function in your contract to save yourself a little bit of time and create and create a `VaultMinter` in your account.

Action

Update the contract `init` function to `create` and `save` an instance of `VaultMinter`:


 `_10self_10.account_10.storage_10.save(<-create VaultMinter(),_10 to: /storage/CadenceFungibleTokenTutorialMinter_10)`

After doing all of this, your contract should be similar to:

 `_103access(all) contract ExampleToken {_103_103 access(all) entitlement Withdraw_103_103 access(all) let VaultStoragePath: StoragePath_103 access(all) let VaultPublicPath: PublicPath_103_103 access(all) var totalSupply: UFix64_103_103 access(all) resource interface Balance {_103 access(all) var balance: UFix64_103 }_103_103 access(all) resource interface Provider {_103 ///_103 /// @param amount the amount of tokens to withdraw from the resource_103 /// @return The Vault with the withdrawn tokens_103 ///_103 access(Withdraw) fun withdraw(amount: UFix64): @Vault {_103 post {_103 // `result` refers to the return value_103 result.balance == amount:_103 "ExampleToken.Provider.withdraw: Cannot withdraw tokens!"_103 .concat("The balance of the withdrawn tokens (").concat(result.balance.toString())_103 .concat(") is not equal to the amount requested to be withdrawn (")_103 .concat(amount.toString()).concat(")")_103 }_103 }_103 }_103_103 access(all) resource interface Receiver {_103_103 /// deposit takes a Vault and deposits it into the implementing resource type_103 ///_103 /// @param from the Vault that contains the tokens to deposit_103 ///_103 access(all) fun deposit(from: @Vault)_103 }_103_103 access(all) resource Vault: Balance, Provider, Receiver {_103_103 access(all) var balance: UFix64_103_103 init(balance: UFix64) {_103 self.balance = balance_103 }_103_103 access(Withdraw) fun withdraw(amount: UFix64): @Vault {_103 pre {_103 self.balance >= amount:_103 "ExampleToken.Vault.withdraw: Cannot withdraw tokens! "_103 .concat("The amount requested to be withdrawn (").concat(amount.toString())_103 .concat(") is greater than the balance of the Vault (")_103 .concat(self.balance.toString()).concat(").")_103 }_103 self.balance = self.balance - amount_103 return <-create Vault(balance: amount)_103 }_103_103 access(all) fun deposit(from: @Vault) {_103 self.balance = self.balance + from.balance_103 destroy from_103 }_103 }_103_103 access(all) fun createEmptyVault(): @Vault {_103 return <-create Vault(balance: 0.0)_103 }_103_103 access(all) resource VaultMinter {_103 access(all) fun mintTokens(amount: UFix64, recipient: Capability<&{Receiver}>) {_103 let recipientRef = recipient.borrow()_103 ?? panicpanic(ExampleToken.vaultNotConfiguredError(address: recipient.address))_103_103 ExampleToken.totalSupply = ExampleToken.totalSupply + UFix64(amount)_103 recipientRef.deposit(from: <-create Vault(balance: amount))_103 }_103 }_103_103 access(all) fun vaultNotConfiguredError(address: Address): String {_103 return "Could not borrow a collection reference to recipient's ExampleToken.Vault"_103 .concat(" from the path ")_103 .concat(ExampleToken.VaultPublicPath.toString())_103 .concat(". Make sure account ")_103 .concat(address.toString())_103 .concat(" has set up its account ")_103 .concat("with an ExampleToken Vault.")_103 }_103_103 init() {_103 self.VaultStoragePath = /storage/CadenceFungibleTokenTutorialVault_103 self.VaultPublicPath = /public/CadenceFungibleTokenTutorialReceiver_103_103 self.totalSupply = 30.0_103_103 self_103 .account_103 .storage_103 .save(<-create VaultMinter(),_103 to: /storage/CadenceFungibleTokenTutorialMinter_103 )_103 }_103}`
## Set Up Account Transaction[​](#set-up-account-transaction "Direct link to Set Up Account Transaction")

We'll now need to create several transactions and scripts to manage interactions with the vault. The first of these is one to set up a user's account. It needs to:

* Create an empty vault
* Save that vault in the caller's storage
* Issue a capability for the vault
* Publish that capability

You've already learned how to do everything you need for this, so you should be able to implement it on your own.

Action

Implement the `Set Up Account` transaction.

You should end up with something similar to:

 `_17import ExampleToken from 0x06_17_17transaction {_17 prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {_17 // You may wish to check if a vault already exists here_17_17 let vaultA <- ExampleToken.createEmptyVault()_17_17 signer.storage.save(<-vaultA, to: ExampleToken.VaultStoragePath)_17_17 let receiverCap = signer.capabilities.storage.issue<&ExampleToken.Vault>(_17 ExampleToken.VaultStoragePath_17 )_17_17 signer.capabilities.publish(receiverCap, at: ExampleToken.VaultPublicPath)_17 }_17}`
## Minting Tokens[​](#minting-tokens "Direct link to Minting Tokens")

The next transaction is another one that you should be able to implement on your own. Give it a try, and check the solution if you need to. Your transaction should:

* Accept an `Address` for the `recipient` and an `amount`
* Store transaction-level references to the `VaultMinter` and `Receiver`
* Borrow a reference to the `VaultMinter` in the caller's storage
* Get the `recipient`'s `Receiver` capability
* Use the above to call the `mintTokens` function in the minter

Action

Implement the `Mint Tokens` transaction.

You should end up with something similar to:

 `_26import ExampleToken from 0x06_26_26transaction(recipient: Address, amount: UFix64) {_26 let mintingRef: &ExampleToken.VaultMinter_26 var receiver: Capability<&{ExampleToken.Receiver}>_26_26 prepare(signer: auth(BorrowValue) &Account) {_26 self.mintingRef = signer.storage.borrow<&ExampleToken.VaultMinter>(from: /storage/CadenceFungibleTokenTutorialMinter)_26 ?? panic(ExampleToken.vaultNotConfiguredError(address: recipient))_26_26 let recipient = getAccount(recipient)_26_26 // Consider further error handling if this fails_26 self.receiver = recipient.capabilities.get<&{ExampleToken.Receiver}>_26 (ExampleToken.VaultPublicPath)_26_26 }_26_26 execute {_26 // Mint 30 tokens and deposit them into the recipient's Vault_26 self.mintingRef.mintTokens(amount: 30.0, recipient: self.receiver)_26_26 log("30 tokens minted and deposited to account "_26 .concat(self.receiver.address.toString()))_26 }_26}`
Action

Test out your minting function by attempting to mint tokens to accounts that do and do not have vaults.

## Checking Account Balances[​](#checking-account-balances "Direct link to Checking Account Balances")

You can mint tokens now. Probably. But it's hard to tell if you have a bug without a way to check an accounts balance. You can do this with a script, using techniques you've already learned.

Action

Write a script to check the balance of an address. It should accept an argument for an `address`. In this script,`get` and `borrow` a reference to that address's `Vault` from the `VaultPublicPath`, and return a nicely formatted string containing the `balance`.

You should end up with something similar to:

 `_15import ExampleToken from 0x06_15_15access(all)_15fun main(address: Address): String {_15 let account = getAccount(address)_15_15 let accountReceiverRef = account.capabilities.get<&{ExampleToken.Balance}>(ExampleToken.VaultPublicPath)_15 .borrow()_15 ?? panic(ExampleToken.vaultNotConfiguredError(address: address))_15_15 return("Balance for "_15 .concat(address.toString())_15 .concat(": ").concat(accountReceiverRef.balance.toString())_15 )_15}`
## Transferring Tokens[​](#transferring-tokens "Direct link to Transferring Tokens")

Transferring tokens from one account to another takes a little more coordination and a more complex contract. When an account wants to send tokens to a different account, the sending account calls their own withdraw function first, which subtracts tokens from their resource's balance and temporarily creates a new resource object that holds this balance.

Action

Initialize a transaction-level variable to hold a temporary vault. Borrow a reference for the sender's vault with the `Withdraw` entitlement and send it to the temporary vault.


 `_13import ExampleToken from 0x06_13_13transaction(recipient: Address, amount: UFix64) {_13 var temporaryVault: @ExampleToken.Vault_13_13 prepare(signer: auth(BorrowValue) &Account) {_13 let vaultRef = signer.storage.borrow<auth(ExampleToken.Withdraw) &ExampleToken.Vault>_13 from: ExampleToken.VaultStoragePath)_13 ?? panic(ExampleToken.vaultNotConfiguredError(address: signer.address))_13_13 self.temporaryVault <- vaultRef.withdraw(amount: amount)_13 }_13}`

The sending account then gets a reference to the recipients published capability and calls the recipient account's deposit function, which literally moves the resource instance to the other account, adds it to their balance, and then destroys the used resource.

Action

Use the `execute` phase to `deposit` the tokens in the `temporaryVault` into the recipient's vault.


 `_12execute{_12 let receiverAccount = getAccount(recipient)_12_12 let receiverRef = receiverAccount_12 .capabilities_12 .borrow<&ExampleToken.Vault>(ExampleToken.VaultPublicPath)_12 ?? panic(ExampleToken.vaultNotConfiguredError(address: recipient))_12_12 receiverRef.deposit(from: <-self.temporaryVault)_12_12 log("Withdraw/Deposit succeeded!")_12}`

The resource is destroyed by the `deposit` function. It needs to be destroyed because Cadence enforces strict rules around resource interactions. A resource can never be left hanging in a piece of code. It either needs to be explicitly destroyed or stored in an account's storage.

This rule ensures that resources, which often represent real value, do not get lost because of a coding error.

You'll notice that the arithmetic operations aren't explicitly protected against overflow or underflow.

 `_10self.balance = self.balance - amount`

Cadence has built-in overflow and underflow protection, so it is not a risk. We are also using unsigned numbers in this example, so as mentioned earlier, the vault`s balance cannot go below 0.

Additionally, the requirement that an account contains a copy of the token's resource type in its storage ensures that funds cannot be lost by being sent to the wrong address.

If an address doesn't have the correct resource type imported, the transaction will revert, ensuring that transactions sent to the wrong address are not lost.

danger

Every Flow account is initialized with a default Flow Token Vault in order to pay for storage fees and transaction [fees](https://developers.flow.com/build/basics/fees.md#fees). If an address is in use, it will be able to accept Flow tokens, without a user or developer needing to take further action. If that account becomes lost, any tokens inside will be lost as well.

## Reviewing Fungible Tokens[​](#reviewing-fungible-tokens "Direct link to Reviewing Fungible Tokens")

In this tutorial, you learned how to create a simplified version of fungible tokens on Flow. You build a vault [resource](/docs/language/resources) to safely store tokens inside the owner's storage, and used [interfaces](/docs/language/interfaces) to define and enforce the properties a vault should have. By using [interfaces](/docs/language/interfaces), your definition is flexible and composable. Other developers can use all or parts of these definitions to build new apps and contracts that are compatible with yours.

You also practiced writing transactions on your own, and learned some new techniques, such as writing error messages more easily, using paths stored in the contract, and separating different parts of the transaction into their appropriate sections - `prepare` and `execute`.

Now that you have completed the tutorial, you should be able to:

* Compare and contrast how tokens are stored in Flow Cadence compared to Ethereum.
* Utilize the `UFix64` type to allow decimals without converting back and forth with 10^18.
* Implement a vault [resource](/docs/language/resources) to manage the functionality needed for fungible tokens
* Use [interfaces](/docs/language/interfaces) to enforce the presence of specified functions and fields.
* Write transactions to transfer tokens safely from one account to another.
* Develop scripts to read account balances.
* Use preconditions and postconditions to perform checks before or after a function call completes.

If you're ready to try your hand at implementing a production-quality token, head over to the [Fungible Token Developer Guide](https://developers.flow.com/build/guides/fungible-token).

In the next tutorial, you'll combine the techniques and patterns you've learned for the classic challenge - building an NFT marketplace!

**Tags:**

* [reference](/docs/tags/reference)
* [Fungible Token](/docs/tags/fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/06-fungible-tokens.md)[PreviousIntermediate NFTs](/docs/tutorial/non-fungible-tokens-2)[Next7. Marketplace Setup](/docs/tutorial/marketplace-setup)
###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Flow Network Token](#flow-network-token)
* [Fungible Tokens on Flow](#fungible-tokens-on-flow)
  + [Fungible tokens on Ethereum](#fungible-tokens-on-ethereum)
  + [Intuiting Ownership with Resources](#intuiting-ownership-with-resources)
* [Constructing a Vault](#constructing-a-vault)
  + [Supply and Balance](#supply-and-balance)
  + [Interfaces](#interfaces)
* [Implementing the Vault](#implementing-the-vault)
* [Vault Creation](#vault-creation)
* [Error Handling](#error-handling)
* [Minting](#minting)
* [Final Contract Setup](#final-contract-setup)
* [Set Up Account Transaction](#set-up-account-transaction)
* [Minting Tokens](#minting-tokens)
* [Checking Account Balances](#checking-account-balances)
* [Transferring Tokens](#transferring-tokens)
* [Reviewing Fungible Tokens](#reviewing-fungible-tokens)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

