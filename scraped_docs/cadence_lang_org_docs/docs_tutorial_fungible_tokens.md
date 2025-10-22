# Source: https://cadence-lang.org/docs/tutorial/fungible-tokens

Fungible Tokens | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)

  + [First Steps](/docs/tutorial/first-steps)
  + [Hello World](/docs/tutorial/hello-world)
  + [Resources and the Move (<-) Operator](/docs/tutorial/resources)
  + [Capabilities and Entitlements](/docs/tutorial/capabilities)
  + [Basic NFT](/docs/tutorial/non-fungible-tokens-1)
  + [Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)
  + [Fungible Tokens](/docs/tutorial/fungible-tokens)
  + [Marketplace Setup](/docs/tutorial/marketplace-setup)
  + [Marketplace](/docs/tutorial/marketplace-compose)
  + [Voting Contract](/docs/tutorial/voting)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Tutorial
* Fungible Tokens

On this page

# Fungible Tokens

Some of the most popular contract classes on blockchains today are fungible tokens. These contracts create homogeneous tokens that can be transferred to other users and spent as currency (e.g., ERC-20 on Ethereum).

In traditional software and smart contracts, balances for each user are tracked by a central ledger, such as a dictionary:

`_12

// Solidity Example

_12

// SIMPLIFIED ERC20 EXAMPLE. DO NOT USE THIS CODE FOR YOUR PROJECT

_12

contract LedgerToken {

_12

mapping (address => uint) public balances;

_12

uint public supply;

_12

_12

function transfer(address _to, uint _amount) public {

_12

require(_balances[msg.sender] >= amount, "Insufficent funds");

_12

balances[msg.sender] -= _amount;

_12

balances[_to] += _amount;

_12

}

_12

}`

`_14

// Cadence Example

_14

// BAD CODE EXAMPLE. DO NOT USE THIS CODE FOR YOUR PROJECT

_14

contract LedgerToken {

_14

// Tracks every user's balance

_14

access(contract) let balances: {Address: UFix64}

_14

_14

// Transfer tokens from one user to the other

_14

// by updating their balances in the central ledger

_14

access(all)

_14

fun transfer(from: Address, to: Address, amount: UFix64) {

_14

balances[from] = balances[from] - amount

_14

balances[to] = balances[to] + amount

_14

}

_14

}`

This is an **immensely dangerous** pattern — all the funds are stored in one account, the contract itself, which means that they can all be stolen at once if a vulnerability is found.

With Cadence, we use the new resource-oriented paradigm to implement fungible tokens and avoid using a central ledger, because there are inherent problems with using a central ledger that are detailed in the [Fungible Tokens section below](#fungible-tokens-on-flow).

warning

This tutorial implements a working fungible token, but it has been simplified for educational purposes and is not what you should use in production.

If you've found this tutorial looking for information on how to implement a real token, see the [Flow Fungible Token standard](https://github.com/onflow/flow-ft) for the standard interface and example implementation, and the [Fungible Token Developer Guide](https://developers.flow.com/build/guides/fungible-token) for details on creating a production-ready version of a Fungible Token contract.

In this tutorial, we're going to deploy, store, and transfer fungible tokens.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Compare and contrast how tokens are stored in Flow Cadence compared to Ethereum.
* Utilize the `UFix64` type to allow decimals without converting back and forth with 10^18.
* Implement a vault [resource](/docs/language/resources) to manage the functionality needed for fungible tokens.
* Use [interfaces](/docs/language/interfaces) to enforce the presence of specified functions and fields.
* Write transactions to transfer tokens safely from one account to another.
* Develop scripts to read account balances.
* Use preconditions and postconditions to perform checks before or after a function call completes.

## Flow network token[​](#flow-network-token "Direct link to Flow network token")

In Flow, the [native network token (FLOW)](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowToken.cdc) is implemented as a normal fungible token smart contract using a smart contract similar to the one you'll build in this tutorial - with all the features and properties found in the [Fungible Token Developer Guide](https://developers.flow.com/build/guides/fungible-token).

There are special transactions and hooks that allow it to be used for transaction execution fees, storage fees, and staking, but besides that, developers and users are able to treat it and use it just like any other token in the network!

## Fungible tokens on Flow[​](#fungible-tokens-on-flow "Direct link to Fungible tokens on Flow")

Flow Cadence implements fungible tokens differently than other blockchains. As a result:

* Ownership is decentralized and does not rely on a central ledger.
* Bugs and exploits present less risk for users and less opportunity for attackers.
* There is no risk of integer underflow or overflow.
* Assets cannot be duplicated, and it is very hard for them to be lost, stolen, or destroyed.
* Code can be composable.

### Fungible tokens on Ethereum[​](#fungible-tokens-on-ethereum "Direct link to Fungible tokens on Ethereum")

The following example showcases how Solidity (the smart contract language for the Ethereum Blockchain, among others) implements fungible tokens, with only the code for storage and transferring tokens shown for brevity.

ERC20.sol

`_12

// Solidity Example

_12

// SIMPLIFIED ERC20 EXAMPLE. DO NOT USE THIS CODE FOR YOUR PROJECT

_12

contract LedgerToken {

_12

mapping (address => uint) public balances;

_12

uint public supply;

_12

_12

function transfer(address _to, uint _amount) public {

_12

require(_balances[msg.sender] >= amount, "Insufficent funds");

_12

balances[msg.sender] -= _amount;

_12

balances[_to] += _amount;

_12

}

_12

}`

As you can see, Solidity uses a central ledger system for its fungible tokens. There is one contract that manages the state of the tokens, and every time that a user wants to do anything with their tokens, they must interact with the central ERC20 contract. This contract handles access control for all functionality, implements all of its own correctness checks, and enforces rules for all of its users.

If there's a bug, such as accidentally making the `_transfer` function accessible to the wrong user, a [reentrancy](https://docs.soliditylang.org/en/latest/security-considerations.html#reentrancy) issue, or another bug, an attacker can immediately exploit the entire contract and the tokens owned by all users.

`_10

// BAD CODE - DO NOT USE

_10

// Anyone can transfer funds out of any account!

_10

function exploitableTransfer(address, _from, address _to, uint _amount) public {

_10

balances[_from] -= _amount;

_10

balances[_to] += _amount;

_10

}`

### Intuiting ownership with resources[​](#intuiting-ownership-with-resources "Direct link to Intuiting ownership with resources")

Instead of using a central ledger system, Flow utilizes a few different concepts to provide better safety, security, and clarity for smart contract developers and users. Primarily, tokens are stored in each user's vault, which is a [resource](/docs/language/resources) similar to the collection you created to store NFTs in the previous tutorial.

This approach simplifies access control because instead of a central contract having to check the sender of a function call, most function calls happen on resource objects stored in users' accounts, and each user natively has sole control over the resources stored in their accounts.

This approach also helps protect against potential bugs. In a Solidity contract with all the logic and state contained in a central contract, an exploit is likely to affect all users who are involved in the contract.

In Cadence, if there is a bug in the resource logic, an attacker would have to exploit the bug in each token holder's account individually, which is much more complicated and time-consuming than it is in a central ledger system.

## Constructing a vault[​](#constructing-a-vault "Direct link to Constructing a vault")

Our vault will be a simplified version of the one found in the [Flow Fungible Token standard](https://github.com/onflow/flow-ft). We'll follow some of the same practices, including using [interfaces](/docs/language/interfaces) to standardize the properties of our vault and make it easier for other contracts to interact with it.

Open the starter code for this tutorial in the Flow Playground: [play.flow.com/359cf1a1-63cc-4774-9c09-1b63ed83379b](https://play.flow.com/359cf1a1-63cc-4774-9c09-1b63ed83379b)

In `ExampleToken.cdc`, you'll see:

ExampleToken.cdc

`_13

access(all) contract ExampleToken {

_13

_13

access(all) entitlement Withdraw

_13

_13

access(all) let VaultStoragePath: StoragePath

_13

access(all) let VaultPublicPath: PublicPath

_13

_13

_13

init() {

_13

self.VaultStoragePath = /storage/CadenceFungibleTokenTutorialVault

_13

self.VaultPublicPath = /public/CadenceFungibleTokenTutorialReceiver

_13

}

_13

}`

Before you can add your vault, you'll need to implement the various pieces it will depend on.

### Supply and balance[​](#supply-and-balance "Direct link to Supply and balance")

The two most basic pieces of information for a fungible token are a method of tracking the balance of a given user and the total supply for the token. In Cadence, you'll usually want to use `UFix64` — a [fixed-point number](/docs/language/values-and-types/fixed-point-nums-ints#fixed-point-numbers).

Fixed-point numbers are essentially integers with a scale, represented by a decimal point. They make it much easier to work with money-like numbers as compared to endlessly handling conversions to and from the 10^18 or 10^9 representation of a value.

Implement a contract-level [fixed-point number](/docs/language/values-and-types/fixed-point-nums-ints#fixed-point-numbers) to track the `totalSupply` of the token, and `init` it:

`_10

access(all) var totalSupply: UFix64`

`_10

self.totalSupply = 0.0;`

### Creating interfaces[​](#creating-interfaces "Direct link to Creating interfaces")

You'll also need a place to store the `balance` of any given user's vault. You **could** simply add a variable in the vault [resource](/docs/language/resources) definition to do this, *and it would work*, but it's not the best option for composability.

Instead, let's use this opportunity to create some [interfaces](/docs/language/interfaces).

In Cadence, interfaces are abstract types used to specify behavior in types that *implement* the interface. Using them helps compatibility and composability by breaking larger constructions down into standardized parts that can be used by more than one contract for more than one use case. For example, the interface we'll create for `Receiver` is used by the vault, but it's also something you'd use for any other resource that needs to be able to receive tokens, such as a contract that pools a collection of tokens and splits them between several addresses.

In the following steps, you'll create three interfaces to handle the three functional areas of the vault:

* A `Balance` interface for the balance of tokens stored in the vault.
* A `Provider` interface that can provide tokens by withdrawing them from the vault.
* A `Receiver` interface that can safely deposit tokens from one vault into another.

1. Create a `Balance` interface, requiring a public `UFix64` called `balance`. It should be public:

   `_10

   access(all) resource interface Balance {

   _10

   access(all) var balance: UFix64

   _10

   }`

   * This one is pretty simple. It just defines the type of variable that anything implementing it will need to have to keep track of a token balance.
2. Create the `Provider` `interface`. In it, define a `withdraw` function. It should have the `Withdraw` access [entitlement](/docs/language/access-control), accept an argument for `amount`, and return a `Vault` resource type. This should also be public.
3. To prevent an error, stub out the `Vault` resource as well:

   `_10

   access(all) resource interface Provider {

   _10

   access(Withdraw) fun withdraw(amount: UFix64): @Vault

   _10

   }

   _10

   _10

   access(all) resource Vault {}`

   This [interface](/docs/language/interfaces) will require resources implementing it to have a `withdraw` function, but it doesn't provide any limitations to how that function works. For example, it could be implemented such that the amount of tokens returned is double the withdrawn amount. While there might be a use case for that effect, it's not what you want for a normal token standard.

   You can allow for flexibility, such as allowing a `Provider` to select randomly from several vaults to determine the payer, while enforcing that the amount withdrawn is appropriate by adding a `post` condition to the function. [Function preconditions and postconditions](/docs/language/functions#function-preconditions-and-postconditions) can be used to restrict the inputs and outputs of a function.

   In a postcondition, the special constant `result` is used to reference the `return` of the function. They're written following the rules of [statements](/docs/language/syntax#semicolons) and can contain multiple conditions. Optionally, a `:` can be added after the last statement, containing an error message to be passed if the postcondition fails.
4. Add a `post` condition that returns a descriptive and nicely formatted error if the amount returned in the vault from the function doesn't match the `amount` passed into the function:

   `_10

   access(Withdraw) fun withdraw(amount: UFix64): @Vault {

   _10

   post {

   _10

   result.balance == amount:

   _10

   "ExampleToken.Provider.withdraw: Cannot withdraw tokens!"

   _10

   .concat("The balance of the withdrawn tokens (").concat(result.balance.toString())

   _10

   .concat(") is not equal to the amount requested to be withdrawn (")

   _10

   .concat(amount.toString()).concat(")")

   _10

   }

   _10

   }`

   * This `post` condition will be added automatically to the `withdraw` function in a resource implementing `Provider`.
5. Implement an [interface](/docs/language/interfaces) called `Receiver`, containing a function called `deposit` that accepts a `Vault`:

   `_10

   access(all) resource interface Receiver {

   _10

   access(all) fun deposit(from: @Vault)

   _10

   }`

## Implementing the vault[​](#implementing-the-vault "Direct link to Implementing the vault")

You're finally ready to implement the vault:

1. Start by updating the stub for a `Vault` to implement `Balance`, `Provider`, and `Receiver`.

   `_10

   access(all) resource Vault: Balance, Provider, Receiver {

   _10

   // TODO

   _10

   }`

   *You'll get errors:*

   `` _10

   resource `ExampleToken.Vault` does not conform to resource interface `ExampleToken.Balance`. `ExampleToken.Vault` is missing definitions for members: Balance ``

   And similar errors for `Provider` and `Receiver`. Similar to inheriting from a virtual class in other languages, implementing the interfaces requires you to implement the properties from those interfaces in your resource.
2. Implement `balance` in the `vault`. You'll also need to initialize it.
3. Initialize it with the `balance` passed into the `init` for the resource itself:

   `_10

   access(all) var balance: UFix64

   _10

   _10

   init(balance: UFix64) {

   _10

   self.balance = balance

   _10

   }`

   The pattern we're setting up here lets us create vaults and give them a `balance` in one go. Doing so is useful for several tasks — creating a temporary `Vault` to hold a balance during a transaction also creates most of the functionality you need to do complex tasks with that balance.

   For example, you might want to set up a conditional transaction that `deposit`s the balance in the vaults in different addresses based on whether or not a part of the transaction is successful.
4. Implement `withdraw` function for the `vault`. It should contain a precondition that validates that the user actually possesses equal to or greater than the number of tokens they are withdrawing.

   * While this functionality is probably something we'd want in every vault, we can't put the requirement in the [interface](/docs/language/interfaces) because the interface doesn't have access to the `balance`.

   `_11

   access(Withdraw) fun withdraw(amount: UFix64): @Vault {

   _11

   pre {

   _11

   self.balance >= amount:

   _11

   "ExampleToken.Vault.withdraw: Cannot withdraw tokens! "

   _11

   .concat("The amount requested to be withdrawn (").concat(amount.toString())

   _11

   .concat(") is greater than the balance of the Vault (")

   _11

   .concat(self.balance.toString()).concat(").")

   _11

   }

   _11

   self.balance = self.balance - amount

   _11

   return <-create Vault(balance: amount)

   _11

   }`
5. Implement the `deposit` function for the `vault`. Depositing should move the entire balance from the provided vault, and then `destroy` that `vault`. Remember, we're transferring tokens by creating a vault and funding it with the amount to transfer. It's not needed once the deposit has emptied it.

   `_10

   access(all) fun deposit(from: @Vault) {

   _10

   self.balance = self.balance + from.balance

   _10

   destroy from

   _10

   }`

You **must** do something with the `Vault` resource after it's moved into the function. Again, you can safely `destroy` it, because it's now empty, and you don't need it anymore.

## Creating vaults[​](#creating-vaults "Direct link to Creating vaults")

We'll also need a way to create empty vaults to onboard new users, or to create vaults for a variety of other uses.

Add a function to the contract to `create` an empty `Vault`:

`_10

access(all) fun createEmptyVault(): @Vault {

_10

return <-create Vault(balance: 0.0)

_10

}`

We'll use this when we create a transaction to set up new users.

## Error handling[​](#error-handling "Direct link to Error handling")

As before, you can anticipate some of the errors that other developers building transactions and scripts that interact with your contract might encounter. At the very least, it's likely that there will be many instances when an attempt is made to borrow a `Vault` that is not present or lacks a capability for the caller to borrow it.

Add a function to generate a helpful error if an attempt to borrow a `Vault` fails:

`_10

access(all) fun vaultNotConfiguredError(address: Address): String {

_10

return "Could not borrow a collection reference to recipient's ExampleToken.Vault"

_10

.concat(" from the path ")

_10

.concat(ExampleToken.VaultPublicPath.toString())

_10

.concat(". Make sure account ")

_10

.concat(address.toString())

_10

.concat(" has set up its account ")

_10

.concat("with an ExampleToken Vault.")

_10

}`

## Minting[​](#minting "Direct link to Minting")

Next, you need a way to actually create, or mint, tokens. For this example, we'll define a `VaultMinter` resource that has the power to mint and airdrop tokens to any address that possesses a vault, or at least something with the `Receiver` [interface](/docs/language/interfaces) for this token.

Only the owner of this resource will be able to mint tokens.

To do so, we use a [capability](/docs/language/capabilities) with a reference to the resource or interface we want to require as the type: `Capability<&{Receiver}>`.

Define a public [resource](/docs/language/resources) with a public function `mintTokens` that accepts an `amount` of tokens to mint, and a `recipient` that must possess the `Receiver` [capability](/docs/language/capabilities):

`_10

access(all) resource VaultMinter {

_10

access(all) fun mintTokens(amount: UFix64, recipient: Capability<&{Receiver}>) {

_10

let recipientRef = recipient.borrow()

_10

?? panic(ExampleToken.vaultNotConfiguredError(address: recipient.address))

_10

_10

ExampleToken.totalSupply = ExampleToken.totalSupply + UFix64(amount)

_10

recipientRef.deposit(from: <-create Vault(balance: amount))

_10

}

_10

}`

tip

Don't be misled by the `access(all)` [entitlement](/docs/language/access-control) for this resource. This entitlement only allows public access to the `VaultMinter` **type**. It does **not** give access to the **instance** we'll create in a moment. That instance will be owned by the publisher of the contract and is the only one that can be created since there isn't a function to create more and `VaultMinter` does **not** have a public `init` function.

## Final contract setup[​](#final-contract-setup "Direct link to Final contract setup")

The last task with the contract is to update the `init` function in your contract, which saves yourself a little bit of time by creating a `VaultMinter` in your account.

Update the contract `init` function to `create` and `save` an instance of `VaultMinter`:

`_10

self

_10

.account

_10

.storage

_10

.save(<-create VaultMinter(),

_10

to: /storage/CadenceFungibleTokenTutorialMinter

_10

)`

After doing all of this, your contract should be similar to:

`_92

access(all) contract ExampleToken {

_92

_92

access(all) entitlement Withdraw

_92

_92

access(all) let VaultStoragePath: StoragePath

_92

access(all) let VaultPublicPath: PublicPath

_92

_92

access(all) var totalSupply: UFix64

_92

_92

access(all) resource interface Balance {

_92

access(all) var balance: UFix64

_92

}

_92

_92

access(all) resource interface Provider {

_92

access(Withdraw) fun withdraw(amount: UFix64): @Vault {

_92

post {

_92

result.balance == amount:

_92

"ExampleToken.Provider.withdraw: Cannot withdraw tokens!"

_92

.concat("The balance of the withdrawn tokens (").concat(result.balance.toString())

_92

.concat(") is not equal to the amount requested to be withdrawn (")

_92

.concat(amount.toString()).concat(")")

_92

}

_92

}

_92

}

_92

_92

access(all) resource interface Receiver {

_92

access(all) fun deposit(from: @Vault)

_92

}

_92

_92

access(all) resource Vault: Balance, Provider, Receiver {

_92

access(all) var balance: UFix64

_92

_92

init(balance: UFix64) {

_92

self.balance = balance

_92

}

_92

_92

access(Withdraw) fun withdraw(amount: UFix64): @Vault {

_92

pre {

_92

self.balance >= amount:

_92

"ExampleToken.Vault.withdraw: Cannot withdraw tokens! "

_92

.concat("The amount requested to be withdrawn (").concat(amount.toString())

_92

.concat(") is greater than the balance of the Vault (")

_92

.concat(self.balance.toString()).concat(").")

_92

}

_92

self.balance = self.balance - amount

_92

return <-create Vault(balance: amount)

_92

}

_92

_92

access(all) fun deposit(from: @Vault) {

_92

self.balance = self.balance + from.balance

_92

destroy from

_92

}

_92

}

_92

_92

access(all) fun createEmptyVault(): @Vault {

_92

return <-create Vault(balance: 0.0)

_92

}

_92

_92

access(all) fun vaultNotConfiguredError(address: Address): String {

_92

return "Could not borrow a collection reference to recipient's ExampleToken.Vault"

_92

.concat(" from the path ")

_92

.concat(ExampleToken.VaultPublicPath.toString())

_92

.concat(". Make sure account ")

_92

.concat(address.toString())

_92

.concat(" has set up its account ")

_92

.concat("with an ExampleToken Vault.")

_92

}

_92

_92

access(all) resource VaultMinter {

_92

access(all) fun mintTokens(amount: UFix64, recipient: Capability<&{Receiver}>) {

_92

let recipientRef = recipient.borrow()

_92

?? panic(ExampleToken.vaultNotConfiguredError(address: recipient.address))

_92

_92

ExampleToken.totalSupply = ExampleToken.totalSupply + UFix64(amount)

_92

recipientRef.deposit(from: <-create Vault(balance: amount))

_92

}

_92

}

_92

_92

init() {

_92

self.VaultStoragePath = /storage/CadenceFungibleTokenTutorialVault

_92

self.VaultPublicPath = /public/CadenceFungibleTokenTutorialReceiver

_92

_92

self

_92

.account

_92

.storage

_92

.save(<-create VaultMinter(),

_92

to: /storage/CadenceFungibleTokenTutorialMinter

_92

)

_92

_92

self.totalSupply = 0.0;

_92

}

_92

}`

Deploy the `ExampleToken` contract with account `0x06`.

## Setting up an account transaction[​](#setting-up-an-account-transaction "Direct link to Setting up an account transaction")

We'll now need to create several transactions and scripts to manage interactions with the vault. The first step is to set up a user's account. It needs to:

* Create an empty vault.
* Save that vault in the caller's storage.
* Issue a capability for the vault.
* Publish that capability.

You've already learned how to do everything you need for this, so you should be able to implement it on your own.

Implement the `Set Up Account` transaction. You should end up with something similar to:

`_17

import ExampleToken from 0x06

_17

_17

transaction {

_17

prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {

_17

// You may wish to check if a vault already exists here

_17

_17

let vaultA <- ExampleToken.createEmptyVault()

_17

_17

signer.storage.save(<-vaultA, to: ExampleToken.VaultStoragePath)

_17

_17

let receiverCap = signer.capabilities.storage.issue<&ExampleToken.Vault>(

_17

ExampleToken.VaultStoragePath

_17

)

_17

_17

signer.capabilities.publish(receiverCap, at: ExampleToken.VaultPublicPath)

_17

}

_17

}`

## Minting tokens[​](#minting-tokens "Direct link to Minting tokens")

The next transaction is another one that you should be able to implement on your own. Give it a try, and check the solution if you need to. Your transaction should:

* Accept an `Address` for the `recipient` and an `amount`.
* Store transaction-level references to the `VaultMinter` and `Receiver`.
* Borrow a reference to the `VaultMinter` in the caller's storage.
* Get the `recipient`'s `Receiver` capability.
* Use the above to call the `mintTokens` function in the minter.

Implement the `Mint Tokens` transaction. You should end up with something similar to:

`_26

import ExampleToken from 0x06

_26

_26

transaction(recipient: Address, amount: UFix64) {

_26

let mintingRef: &ExampleToken.VaultMinter

_26

var receiver: Capability<&{ExampleToken.Receiver}>

_26

_26

prepare(signer: auth(BorrowValue) &Account) {

_26

self.mintingRef = signer.storage.borrow<&ExampleToken.VaultMinter>(from: /storage/CadenceFungibleTokenTutorialMinter)

_26

?? panic(ExampleToken.vaultNotConfiguredError(address: recipient))

_26

_26

let recipient = getAccount(recipient)

_26

_26

// Consider further error handling if this fails

_26

self.receiver = recipient.capabilities.get<&{ExampleToken.Receiver}>

_26

(ExampleToken.VaultPublicPath)

_26

_26

}

_26

_26

execute {

_26

// Mint 30 tokens and deposit them into the recipient's Vault

_26

self.mintingRef.mintTokens(amount: 30.0, recipient: self.receiver)

_26

_26

log("30 tokens minted and deposited to account "

_26

.concat(self.receiver.address.toString()))

_26

}

_26

}`

Test out your minting function by attempting to mint tokens to accounts that do and do not have vaults.

## Checking account balances[​](#checking-account-balances "Direct link to Checking account balances")

You can mint tokens now. Probably. But it's hard to tell if you have a bug without a way to check an account's balance. You can do this with a script, using techniques you've already learned.

Write a script to check the balance of an address. It should accept an argument for an `address`. In this script, `get` and `borrow` a reference to that address's `Vault` from the `VaultPublicPath`, and return a nicely formatted string containing the `balance`.

You should end up with something similar to:

`_15

import ExampleToken from 0x06

_15

_15

access(all)

_15

fun main(address: Address): String {

_15

let account = getAccount(address)

_15

_15

let accountReceiverRef = account.capabilities.get<&{ExampleToken.Balance}>(ExampleToken.VaultPublicPath)

_15

.borrow()

_15

?? panic(ExampleToken.vaultNotConfiguredError(address: address))

_15

_15

return("Balance for "

_15

.concat(address.toString())

_15

.concat(": ").concat(accountReceiverRef.balance.toString())

_15

)

_15

}`

## Transferring tokens[​](#transferring-tokens "Direct link to Transferring tokens")

Transferring tokens from one account to another takes a little more coordination and a more complex transaction. When an account wants to send tokens to a different account, the sending account calls their own withdraw function first, which subtracts tokens from their resource's balance and temporarily creates a new resource object that holds this balance.

1. Initialize a transaction-level variable to hold a temporary vault. Borrow a reference for the sender's vault with the `Withdraw` entitlement and send it to the temporary vault:

   `_13

   import ExampleToken from 0x06

   _13

   _13

   transaction(recipient: Address, amount: UFix64) {

   _13

   var temporaryVault: @ExampleToken.Vault

   _13

   _13

   prepare(signer: auth(BorrowValue) &Account) {

   _13

   let vaultRef = signer.storage.borrow<auth(ExampleToken.Withdraw) &ExampleToken.Vault>(

   _13

   from: ExampleToken.VaultStoragePath)

   _13

   ?? panic(ExampleToken.vaultNotConfiguredError(address: signer.address))

   _13

   _13

   self.temporaryVault <- vaultRef.withdraw(amount: amount)

   _13

   }

   _13

   }`

   The sending account then gets a reference to the recipient's published capability and calls the recipient account's deposit function, which literally moves the resource instance to the other account, adds the temporary vault's balance to their balance, and then destroys the used resource.
2. Use the `execute` phase to `deposit` the tokens in the `temporaryVault` into the recipient's vault:

`_12

execute{

_12

let receiverAccount = getAccount(recipient)

_12

_12

let receiverRef = receiverAccount

_12

.capabilities

_12

.borrow<&ExampleToken.Vault>(ExampleToken.VaultPublicPath)

_12

?? panic(ExampleToken.vaultNotConfiguredError(address: recipient))

_12

_12

receiverRef.deposit(from: <-self.temporaryVault)

_12

_12

log("Withdraw/Deposit succeeded!")

_12

}`

The resource is destroyed by the `deposit` function. It needs to be destroyed because Cadence enforces strict rules around resource interactions. A resource can never be left hanging in a piece of code. It either needs to be explicitly destroyed or stored in an account's storage.

This rule ensures that resources, which often represent real value, do not get lost because of a coding error.

You'll notice that the arithmetic operations aren't explicitly protected against overflow or underflow:

`_10

self.balance = self.balance - amount`

Cadence has built-in overflow and underflow protection, so it is not a risk. We are also using unsigned numbers in this example, so as mentioned earlier, the vault`s balance cannot go below 0.

Additionally, the requirement that an account contains a copy of the token's resource type in its storage ensures that funds cannot be lost by being sent to the wrong address.

If an address doesn't have the correct resource type imported, the transaction will revert, ensuring that transactions sent to the wrong address are not lost.

danger

Every Flow account is initialized with a default Flow Token Vault in order to pay for storage fees and transaction [fees](https://developers.flow.com/build/basics/fees.md#fees). If an address is in use, it will be able to accept Flow tokens, without a user or developer needing to take further action. If that account becomes lost, any tokens inside will be lost as well.

## Reviewing fungible tokens[​](#reviewing-fungible-tokens "Direct link to Reviewing fungible tokens")

In this tutorial, you learned how to create a simplified version of fungible tokens on Flow. You build a vault [resource](/docs/language/resources) to safely store tokens inside the owner's storage, and use [interfaces](/docs/language/interfaces) to define and enforce the properties a vault should have. By using [interfaces](/docs/language/interfaces), your definition is flexible and composable. Other developers can use all or parts of these definitions to build new apps and contracts that are compatible with yours.

You also practiced writing transactions on your own, and learned some new techniques, such as writing error messages more easily, using paths stored in the contract, and separating different parts of the transaction into their appropriate sections — `prepare` and `execute`.

Now that you have completed the tutorial, you should be able to:

* Compare and contrast how tokens are stored in Flow Cadence compared to Ethereum.
* Utilize the `UFix64` type to allow decimals without converting back and forth with 10^18.
* Implement a vault [resource](/docs/language/resources) to manage the functionality needed for fungible tokens.
* Use [interfaces](/docs/language/interfaces) to enforce the presence of specified functions and fields.
* Write transactions to transfer tokens safely from one account to another.
* Develop scripts to read account balances.
* Use preconditions and postconditions to perform checks before or after a function call completes.

If you're ready to try your hand at implementing a production-quality token, head over to the [Fungible Token Developer Guide](https://developers.flow.com/build/guides/fungible-token).

In the next tutorial, you'll combine the techniques and patterns you've learned for the classic challenge — building an NFT marketplace!

## Reference solution[​](#reference-solution "Direct link to Reference solution")

warning

You are **not** saving time by skipping the reference implementation. You'll learn much faster by doing the tutorials as presented!

Reference solutions are functional, but may not be optimal.

* [Reference Solution](https://play.flow.com/b0f19641-0831-4192-ae25-ae745b1cab55)

**Tags:**

* [reference](/docs/tags/reference)
* [Fungible Token](/docs/tags/fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/06-fungible-tokens.md)

[Previous

Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)[Next

Marketplace Setup](/docs/tutorial/marketplace-setup)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Flow network token](#flow-network-token)
* [Fungible tokens on Flow](#fungible-tokens-on-flow)
  + [Fungible tokens on Ethereum](#fungible-tokens-on-ethereum)
  + [Intuiting ownership with resources](#intuiting-ownership-with-resources)
* [Constructing a vault](#constructing-a-vault)
  + [Supply and balance](#supply-and-balance)
  + [Creating interfaces](#creating-interfaces)
* [Implementing the vault](#implementing-the-vault)
* [Creating vaults](#creating-vaults)
* [Error handling](#error-handling)
* [Minting](#minting)
* [Final contract setup](#final-contract-setup)
* [Setting up an account transaction](#setting-up-an-account-transaction)
* [Minting tokens](#minting-tokens)
* [Checking account balances](#checking-account-balances)
* [Transferring tokens](#transferring-tokens)
* [Reviewing fungible tokens](#reviewing-fungible-tokens)
* [Reference solution](#reference-solution)