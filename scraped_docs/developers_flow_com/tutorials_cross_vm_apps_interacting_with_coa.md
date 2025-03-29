# Source: https://developers.flow.com/tutorials/cross-vm-apps/interacting-with-coa

Interacting with COAs from Cadence | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)

  + [Batched Transactions](/tutorials/cross-vm-apps/introduction)
  + [Interacting with COAs](/tutorials/cross-vm-apps/interacting-with-coa)
  + [Direct Calls to Flow EVM](/tutorials/cross-vm-apps/direct-calls)
  + [Batched EVM Transactions](/tutorials/cross-vm-apps/batched-evm-transactions)
  + [Cross-VM Bridge](/tutorials/cross-vm-apps/vm-bridge)
* [FlowtoBooth Tutorials](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

* [Cross-VM Apps](/tutorials/cross-vm-apps)
* Interacting with COAs

On this page

# Interacting with COAs from Cadence

[Cadence Owned Accounts (COAs)](/evm/accounts#cadence-owned-accounts) are EVM accounts owned by a Cadence resource and
are used to interact with Flow EVM from Cadence.

COAs expose two interfaces for interaction: one on the Cadence side and one on the EVM side. In this guide, we will
focus on how to interact with COAs with Cadence.

In this guide we will walk through some basic examples creating and interacting with a COA in Cadence. Your specific
usage of the COA resource will depend on your own application's requirements (e.g. the COA resource may not live
directly in `/storage/evm` as in these examples, but may instead be a part of a more complex resource structure).

## COA Interface[​](#coa-interface "Direct link to COA Interface")

To begin, we can take a look at a simplified version of the `EVM` contract, highlighting parts specific to COAs.

You can learn more about the `EVM` contract [here](/build/core-contracts/evm) and the full contract code can
be found on [GitHub](https://github.com/onflow/flow-go/tree/master/fvm/evm/stdlib/contract.cdc).

EVM.cdc

`_56

access(all)

_56

contract EVM {

_56

//...

_56

access(all)

_56

resource CadenceOwnedAccount: Addressable {

_56

/// The EVM address of the cadence owned account

_56

/// -> could be used to query balance, code, nonce, etc.

_56

access(all)

_56

view fun address(): EVM.EVMAddress

_56

_56

/// Get balance of the cadence owned account

_56

/// This balance

_56

access(all)

_56

view fun balance(): EVM.Balance

_56

_56

/// Deposits the given vault into the cadence owned account's balance

_56

access(all)

_56

fun deposit(from: @FlowToken.Vault)

_56

_56

/// The EVM address of the cadence owned account behind an entitlement, acting as proof of access

_56

access(EVM.Owner | EVM.Validate)

_56

view fun protectedAddress(): EVM.EVMAddress

_56

_56

/// Withdraws the balance from the cadence owned account's balance

_56

/// Note that amounts smaller than 10nF (10e-8) can't be withdrawn

_56

/// given that Flow Token Vaults use UFix64s to store balances.

_56

/// If the given balance conversion to UFix64 results in

_56

/// rounding error, this function would fail.

_56

access(EVM.Owner | EVM.Withdraw)

_56

fun withdraw(balance: EVM.Balance): @FlowToken.Vault

_56

_56

/// Deploys a contract to the EVM environment.

_56

/// Returns the address of the newly deployed contract

_56

access(EVM.Owner | EVM.Deploy)

_56

fun deploy(

_56

code: [UInt8],

_56

gasLimit: UInt64,

_56

value: Balance

_56

): EVM.EVMAddress

_56

_56

/// Calls a function with the given data.

_56

/// The execution is limited by the given amount of gas

_56

access(EVM.Owner | EVM.Call)

_56

fun call(

_56

to: EVMAddress,

_56

data: [UInt8],

_56

gasLimit: UInt64,

_56

value: Balance

_56

): EVM.Result

_56

}

_56

_56

// Create a new CadenceOwnedAccount resource

_56

access(all)

_56

fun createCadenceOwnedAccount(): @EVM.CadenceOwnedAccount

_56

// ...

_56

}`

## Importing the EVM Contract[​](#importing-the-evm-contract "Direct link to Importing the EVM Contract")

The `CadenceOwnedAccount` resource is a part of the `EVM` system contract, so to use any of these functions, you will
need to begin by importing the `EVM` contract into your Cadence code.

To import the `EVM` contract into your Cadence code using the simple import syntax, you can use the following format
(learn more about configuring contracts in `flow.json`
[here](/tools/flow-cli/flow.json/configuration#contracts)):

`_10

// This assumes you are working in the in the Flow CLI, FCL, or another tool that supports this syntax

_10

// The contract address should be configured in your project's `flow.json` file

_10

import "EVM"

_10

// ...`

However, if you wish to use manual address imports instead, you can use the following format:

`_10

// Must use the correct address based on the network you are interacting with

_10

import EVM from 0x1234

_10

// ...`

To find the deployment addresses of the `EVM` contract, you can refer to the [EVM contract
documentation](/build/core-contracts/evm).

## Creating a COA[​](#creating-a-coa "Direct link to Creating a COA")

To create a COA, we can use the `createCadenceOwnedAccount` function from the `EVM` contract. This function takes no
arguments and returns a new `CadenceOwnedAccount` resource which represents this newly created EVM account.

For example, we can create this COA in a transaction, saving it to the user's storage and publishing a public capability
to its reference:

create\_coa.cdc

`_17

import "EVM"

_17

_17

// Note that this is a simplified example & will not handle cases where the COA already exists

_17

transaction() {

_17

prepare(signer: auth(SaveValue, IssueStorageCapabilityController, PublishCapability) &Account) {

_17

let storagePath = /storage/evm

_17

let publicPath = /public/evm

_17

_17

// Create account & save to storage

_17

let coa: @EVM.CadenceOwnedAccount <- EVM.createCadenceOwnedAccount()

_17

signer.storage.save(<-coa, to: storagePath)

_17

_17

// Publish a public capability to the COA

_17

let cap = signer.capabilities.storage.issue<&EVM.CadenceOwnedAccount>(storagePath)

_17

signer.capabilities.publish(cap, at: publicPath)

_17

}

_17

}`

## Getting the EVM Address of a COA[​](#getting-the-evm-address-of-a-coa "Direct link to Getting the EVM Address of a COA")

To get the EVM address of a COA, you can use the `address` function from the `EVM` contract. This function returns the
EVM address of the COA as an `EVM.Address` struct. This struct is used to represent addresses within Flow EVM and can
also be used to query the balance, code, nonce, etc. of an account.

For our example, we could query the address of the COA we just created with the following script:

get\_coa\_address.cdc

`_16

import "EVM"

_16

_16

access(all)

_16

fun main(address: Address): EVM.EVMAddress {

_16

// Get the desired Flow account holding the COA in storage

_16

let account = getAuthAccount<auth(Storage) &Account>(address)

_16

_16

// Borrow a reference to the COA from the storage location we saved it to

_16

let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(

_16

from: /storage/evm

_16

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_16

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_16

_16

// Return the EVM address of the COA

_16

return coa.address()

_16

}`

If you'd prefer the hex representation of the address, you instead return using the `EVMAddress.toString()` function:

`_10

return coa.address().toString()`

The above will return the EVM address as a string; however note that Cadence does not prefix hex strings with `0x`.

## Getting the Flow Balance of a COA[​](#getting-the-flow-balance-of-a-coa "Direct link to Getting the Flow Balance of a COA")

Like any other Flow EVM or Cadence account, COAs possess a balance of FLOW tokens. To get the current balance of our
COA, we can use the COA's `balance` function. It will return a `EVM.Balance` struct for the account - these are used to
represent balances within Flow EVM.

This script will query the current balance of our newly created COA:

get\_coa\_balance.cdc

`_16

import "EVM"

_16

_16

access(all)

_16

fun main(address: Address): EVM.Balance {

_16

// Get the desired Flow account holding the COA in storage

_16

let account = getAuthAccount<auth(Storage) &Account>(address)

_16

_16

// Borrow a reference to the COA from the storage location we saved it to

_16

let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(

_16

from: /storage/evm

_16

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_16

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_16

_16

// Get the current balance of this COA

_16

return coa.balance()

_16

}`

You can also easily get the `UFix64` FLOW balance of any EVM address with this script:

get\_coa\_balance\_as\_ufix64.cdc

`_10

import "EVM"

_10

_10

access(all)

_10

fun main(addressHex: String): UFix64 {

_10

let addr = EVM.addressFromString(addressHex)

_10

return addr.balance().inFLOW()

_10

}`

The above script is helpful if you already know the COA address and can provide the hex representation directly.

## Depositing and Withdrawing Flow Tokens[​](#depositing-and-withdrawing-flow-tokens "Direct link to Depositing and Withdrawing Flow Tokens")

Tokens can be seamlessly transferred between the Flow EVM and Cadence environment using the `deposit` and `withdraw`
functions provided by the COA resource. Anybody with a valid reference to a COA may deposit Flow tokens into a it,
however only someone with the `Owner` or `Withdraw` entitlements can withdraw tokens.

### Depositing Flow Tokens[​](#depositing-flow-tokens "Direct link to Depositing Flow Tokens")

The `deposit` function takes a `FlowToken.Vault` resource as an argument, representing the tokens to deposit. It will
transfer the tokens from the vault into the COA's balance.

This transaction will withdraw Flow tokens from a user's Cadence vault and deposit them into their COA:

deposit\_to\_coa.cdc

`_27

import "EVM"

_27

import "FungibleToken"

_27

import "FlowToken"

_27

_27

transaction(amount: UFix64) {

_27

let coa: &EVM.CadenceOwnedAccount

_27

let sentVault: @FlowToken.Vault

_27

_27

prepare(signer: auth(BorrowValue) &Account) {

_27

// Borrow the public capability to the COA from the desired account

_27

// This script could be modified to deposit into any account with a `EVM.CadenceOwnedAccount` capability

_27

self.coa = signer.capabilities.borrow<&EVM.CadenceOwnedAccount>(/public/evm)

_27

?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_27

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_27

_27

// Withdraw the balance from the COA, we will use this later to deposit into the receiving account

_27

let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_27

from: /storage/flowTokenVault

_27

) ?? panic("Could not borrow reference to the owner's FlowToken Vault")

_27

self.sentVault <- vaultRef.withdraw(amount: amount) as! @FlowToken.Vault

_27

}

_27

_27

execute {

_27

// Deposit the withdrawn tokens into the COA

_27

self.coa.deposit(from: <-self.sentVault)

_27

}

_27

}`

info

This is a basic example which only transfers tokens between a single user's COA & Flow account. It can be easily
modified to transfer these tokens between any arbitrary accounts.

You can also deposit tokens directly into other types of EVM accounts using the `EVM.EVMAddress.deposit` function. See
the [EVM contract documentation](/build/core-contracts/evm) for more information.

### Withdrawing Flow Tokens[​](#withdrawing-flow-tokens "Direct link to Withdrawing Flow Tokens")

The `withdraw` function takes a `EVM.Balance` struct as an argument, representing the amount of Flow tokens to withdraw,
and returns a `FlowToken.Vault` resource with the withdrawn tokens.

We can run the following transaction to withdraw Flow tokens from a user's COA and deposit them into their Flow vault:

withdraw\_from\_coa.cdc

`_32

import "EVM"

_32

import "FungibleToken"

_32

import "FlowToken"

_32

_32

transaction(amount: UFix64) {

_32

let sentVault: @FlowToken.Vault

_32

let receiver: &{FungibleToken.Receiver}

_32

_32

prepare(signer: auth(BorrowValue) &Account) {

_32

// Borrow a reference to the COA from the storage location we saved it to with the `EVM.Withdraw` entitlement

_32

let coa = signer.storage.borrow<auth(EVM.Withdraw) &EVM.CadenceOwnedAccount>(

_32

from: /storage/evm

_32

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_32

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_32

_32

// We must create a `EVM.Balance` struct to represent the amount of Flow tokens to withdraw

_32

let withdrawBalance = EVM.Balance(attoflow: 0)

_32

withdrawBalance.setFLOW(flow: amount)

_32

_32

// Withdraw the balance from the COA, we will use this later to deposit into the receiving account

_32

self.sentVault <- coa.withdraw(balance: withdrawBalance) as! @FlowToken.Vault

_32

_32

// Borrow the public capability to the receiving account (in this case the signer's own Vault)

_32

// This script could be modified to deposit into any account with a `FungibleToken.Receiver` capability

_32

self.receiver = signer.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!

_32

}

_32

_32

execute {

_32

// Deposit the withdrawn tokens into the receiving vault

_32

self.receiver.deposit(from: <-self.sentVault)

_32

}

_32

}`

info

This is a basic example which only transfers tokens between a single user's COA & Flow account. It can be easily
modified to transfer these tokens between any arbitrary accounts.

## Direct Calls to Flow EVM[​](#direct-calls-to-flow-evm "Direct link to Direct Calls to Flow EVM")

To interact with smart contracts on the EVM, you can use the `call` function provided by the COA resource. This function
takes the EVM address of the contract you want to call, the data you want to send, the gas limit, and the value you want
to send. It will return a `EVM.Result` struct with the result of the call - you will need to handle this result in your
Cadence code.

This transaction will use the signer's COA to call a contract method with the defined signature and args at a given EVM
address, executing with the provided gas limit and value:

call.cdc

`_47

import "EVM"

_47

_47

/// Calls the function with the provided signature and args at the target contract address using

_47

/// the defined gas limit and transmitting the provided value.

_47

transaction(evmContractHex: String, signature: String, args: [AnyStruct], gasLimit: UInt64, flowValue: UInt) {

_47

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_47

_47

prepare(signer: auth(BorrowValue) &Account) {

_47

// Borrow an entitled reference to the COA from the storage location we saved it to

_47

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(

_47

from: /storage/evm

_47

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_47

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_47

}

_47

_47

execute {

_47

// Deserialize the EVM address from the hex string

_47

let contractAddress = EVM.addressFromString(evmContractHex)

_47

// Construct the calldata from the signature and arguments

_47

let calldata = EVM.encodeABIWithSignature(

_47

signature,

_47

args

_47

)

_47

// Define the value as EVM.Balance struct

_47

let value = EVM.Balance(attoflow: flowValue)

_47

// Call the contract at the given EVM address with the given data, gas limit, and value

_47

// These values could be configured through the transaction arguments or other means

_47

// however, for simplicity, we will hardcode them here

_47

let result: EVM.Result = self.coa.call(

_47

to: contractAddress,

_47

data: calldata,

_47

gasLimit: gasLimit,

_47

value: value

_47

)

_47

_47

// Revert the transaction if the call was not successful

_47

// Note: a failing EVM call will not automatically revert the Cadence transaction

_47

// and it is up to the developer to use this result however it suits their application

_47

assert(

_47

result.status == EVM.Status.successful,

_47

message: "EVM call to ".concat(evmContractHex)

_47

.concat(" and signature ").concat(signature)

_47

.concat(" failed with error code ").concat(result.errorCode.toString())

_47

.concat(": ").concat(result.errorMessage)

_47

)

_47

}

_47

}`

info

Notice that the calldata is encoded in the scope of the transaction. While developers can encode the calldata
outside the scope of the transaction and pass the encoded data as an argument, doing so compromises the
human-readability of Cadence transactions.

It's encouraged to either define transactions for each COA call and encoded the hardcoded EVM signature and arguments,
or to pass in the human-readable arguments and signature and encode the calldata within the transaction. This ensures a
more interpretable and therefore transparent transaction.

### Transferring FLOW in EVM[​](#transferring-flow-in-evm "Direct link to Transferring FLOW in EVM")

Similar to transferring ETH and other native value in other EVMs, you'll want to call to the target EVM address with
empty calldata and providing the transfer value.

transfer\_evm\_flow.cdc

`_42

import "EVM"

_42

_42

/// Transfers FLOW to another EVM address from the signer's COA

_42

///

_42

/// @param to: the serialized EVM address of the recipient

_42

/// @param amount: the amount of FLOW to send

_42

transaction(to: String, amount: UInt) {

_42

_42

let recipient: EVM.EVMAddress

_42

let recipientPreBalance: UInt

_42

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_42

_42

prepare(signer: auth(BorrowValue) &Account) {

_42

self.recipient = EVM.addressFromString(to)

_42

self.recipientPreBalance = self.recipient.balance().attoflow

_42

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: /storage/evm)

_42

?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_42

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_42

}

_42

_42

execute {

_42

let res = self.coa.call(

_42

to: self.recipient,

_42

data: [],

_42

gasLimit: 100_000,

_42

value: EVM.Balance(attoflow: amount)

_42

)

_42

_42

assert(

_42

res.status == EVM.Status.successful,

_42

message: "Failed to transfer FLOW to EVM address with error code ".concat(res.errorCode.toString())

_42

.concat(": ").concat(res.errorMessage)

_42

)

_42

}

_42

_42

post {

_42

self.recipient.balance().attoflow == self.recipientPreBalance + amount:

_42

"Expected final balance ".concat((self.recipientPreBalance + amount).toString())

_42

.concat(" but found actual balance ").concat(self.recipient.balance().attoflow.toString())

_42

.concat(" after deposit of ").concat(amount.toString())

_42

}

_42

}`

### Transfer ERC20[​](#transfer-erc20 "Direct link to Transfer ERC20")

Below is an example transaction demonstrating the common ERC20 transfer. A similar pattern can be used for other
arbitrary EVM calls.

erc20\_transfer\_from.cdc

`_42

import "EVM"

_42

_42

/// Transfers ERC20 tokens from the signer's COA to the named recipient in the amount provided

_42

///

_42

/// @param erc20AddressHex: the serialized EVM address of the ERC20 contract

_42

/// @param to: the serialized EVM address of the recipient

_42

/// @param amount: the amount of tokens to send

_42

transaction(erc20AddressHex: String, to: String, amount: UInt256) {

_42

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_42

_42

prepare(signer: auth(BorrowValue) &Account) {

_42

// Borrow an entitled reference to the COA from the canonical storage location

_42

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(

_42

from: /storage/evm

_42

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_42

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_42

}

_42

_42

execute {

_42

// Encode the calldata for the ERC20 transfer

_42

let calldata = EVM.encodeABIWithSignature(

_42

"transfer(address,uint256)", // function signature

_42

[EVM.addressFromString(to), amount] // function args

_42

)

_42

// Call the contract at the given ERC20 address with encoded calldata and 0 value

_42

let result: EVM.Result = self.coa.call(

_42

to: EVM.addressFromString(erc20AddressHex), // deserialized address

_42

data: calldata, // encoded calldata

_42

gasLimit: 100_000, // 100k gas should cover most erc20 transfers

_42

value: EVM.Balance(attoflow: UInt(0)) // no value required in most cases

_42

)

_42

_42

// Revert the transaction if the call was not successful

_42

// Note: a failing EVM call will not automatically revert the Cadence transaction

_42

// and it is up to the developer to use this result however it suits their application

_42

assert(

_42

result.status == EVM.Status.successful,

_42

message: "ERC20.transfer call failed with error code: ".concat(result.errorCode.toString())

_42

.concat(": ").concat(result.errorMessage)

_42

)

_42

}

_42

}`

### Transfer ERC721[​](#transfer-erc721 "Direct link to Transfer ERC721")

Following on from above, the example transaction below demonstrates a common ERC721 transfer.

erc721\_transfer.cdc

`_41

import "EVM"

_41

_41

/// Transfers an ERC721 token from the signer's COA to the named recipient

_41

///

_41

/// @param erc721AddressHex: the serialized EVM address of the ERC721 contract

_41

/// @param to: the serialized EVM address of the recipient

_41

/// @param id: the token ID to send from the signer's COA to the recipient

_41

transaction(erc721AddressHex: String, to: String, id: UInt256) {

_41

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_41

_41

prepare(signer: auth(BorrowValue) &Account) {

_41

// Borrow an entitled reference to the COA from the canonical storage location

_41

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(

_41

from: /storage/evm

_41

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_41

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_41

}

_41

_41

execute {

_41

let calldata = EVM.encodeABIWithSignature(

_41

"safeTransferFrom(address,address,uint256)",

_41

[self.coa.address(), EVM.addressFromString(to), id]

_41

)

_41

// Call the contract at the given ERC721 address with encoded calldata and 0 value

_41

let result: EVM.Result = self.coa.call(

_41

to: EVM.addressFromString(erc721AddressHex), // deserialized address

_41

data: calldata // previously encoded calldata

_41

gasLimit: 100_000, // 100k gas should cover most erc721 transfers

_41

value: EVM.Balance(attoflow: UInt(0)) // no value required in most cases

_41

)

_41

_41

// Revert the transaction if the call was not successful

_41

// Note: a failing EVM call will not automatically revert the Cadence transaction

_41

// and it is up to the developer to use this result however it suits their application

_41

assert(

_41

result.status == EVM.Status.successful,

_41

message: "ERC721.safeTransferFrom call failed with error code: ".concat(result.errorCode.toString())

_41

.concat(": ").concat(result.errorMessage)

_41

)

_41

}

_41

}`

#### Bulk Transfer ERC721[​](#bulk-transfer-erc721 "Direct link to Bulk Transfer ERC721")

As covered in the [Batched EVM transactions walkthrough](/tutorials/cross-vm-apps/batched-evm-transactions), you can script multiple EVM
calls in a single Cadence transaction. Compared to the single ERC721 transfer, bulk sending multiple tokens isn't much
more code and allows for greater utility out of a single transaction. Below is an example of a bulk ERC721 token
transfer.

erc721\_bulk\_transfer.cdc

`_48

import "EVM"

_48

_48

/// Bulk transfers ERC721 tokens from the signer's COA to the named recipient. All tokens must be from

_48

/// the same collection and sent to the same recipient.

_48

///

_48

/// @param erc721AddressHex: the serialized EVM address of the ERC721 contract

_48

/// @param to: the serialized EVM address of the recipient

_48

/// @param ids: an array of IDs to send from the signer's COA to the recipient

_48

transaction(erc721AddressHex: String, to: String, ids: [UInt256]) {

_48

let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount

_48

_48

prepare(signer: auth(BorrowValue) &Account) {

_48

// Borrow an entitled reference to the COA from the canonical storage location

_48

self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(

_48

from: /storage/evm

_48

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_48

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_48

}

_48

_48

execute {

_48

// Iterate over provided IDs. Note the whole transaction fails if a single transfer fails,

_48

// so ownership validation is recommended before executing. Alternatively, you could remove

_48

// the assertion on success below and continue iteration on call failure.

_48

for id in ids {

_48

let calldata = EVM.encodeABIWithSignature(

_48

"safeTransferFrom(address,address,uint256)",

_48

[self.coa.address(), EVM.addressFromString(to), id]

_48

)

_48

// Call the contract at the given ERC721 address with encoded calldata and 0 value

_48

let result: EVM.Result = self.coa.call(

_48

to: EVM.addressFromString(erc721AddressHex), // deserialized address

_48

data: calldata // previously encoded calldata

_48

gasLimit: 100_000, // 100k gas should cover most erc721 transfers

_48

value: EVM.Balance(attoflow: UInt(0)) // no value required in most cases

_48

)

_48

_48

// Revert the transaction if the transfer was not successful

_48

// Note: a failing EVM call will not automatically revert the Cadence transaction

_48

// and it is up to the developer to use this result however it suits their application

_48

assert(

_48

result.status == EVM.Status.successful,

_48

message: "ERC721.safeTransferFrom call failed on id ".concat(id.toString())

_48

.concat(" with error code: ").concat(result.errorCode.toString())

_48

.concat(": ").concat(result.errorMessage)

_48

)

_48

}

_48

}

_48

}`

## Deploying a Contract to Flow EVM[​](#deploying-a-contract-to-flow-evm "Direct link to Deploying a Contract to Flow EVM")

To deploy a contract to the EVM, you can use the `deploy` function provided by the COA resource. This function takes the
contract code, gas limit, and value you want to send. It will return the EVM address of the newly deployed contract.

This transaction will deploy a contract with the given code using the signer's COA:

deploy\_evm\_contract.cdc

`_22

import "EVM"

_22

_22

transaction(bytecode: String) {

_22

let coa: auth(EVM.Deploy) &EVM.CadenceOwnedAccount

_22

_22

prepare(signer: auth(BorrowValue) &Account) {

_22

// Borrow an entitled reference to the COA from the storage location we saved it to

_22

self.coa = signer.storage.borrow<auth(EVM.Deploy) &EVM.CadenceOwnedAccount>(

_22

from: /storage/evm

_22

) ?? panic("Could not borrow reference to the signer's CadenceOwnedAccount (COA). "

_22

.concat("Ensure the signer account has a COA stored in the canonical /storage/evm path"))

_22

}

_22

_22

execute {

_22

// Deploy the contract with the given compiled bytecode, gas limit, and value

_22

self.coa.deploy(

_22

code: bytecode.decodeHex(),

_22

gasLimit: 15_000_000, // can be adjusted as needed, hard coded here for simplicity

_22

value: EVM.Balance(attoflow: 0)

_22

)

_22

}

_22

}`

## More Information[​](#more-information "Direct link to More Information")

For more information about Cadence Owned Accounts, see [Flow EVM Accounts](/evm/accounts).

Other useful snippets for interacting with COAs can be found [here](https://fw-internal-doc.gitbook.io/evm).

Check out the [Batched EVM Transactions walkthrough](/tutorials/cross-vm-apps/batched-evm-transactions) for details on transaction batching
using Cadence.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/cross-vm-apps/interacting-with-coa.md)

Last updated on **Mar 26, 2025** by **Brian Doyle**

[Previous

Batched Transactions](/tutorials/cross-vm-apps/introduction)[Next

Direct Calls to Flow EVM](/tutorials/cross-vm-apps/direct-calls)

###### Rate this page

😞😐😊

* [COA Interface](#coa-interface)
* [Importing the EVM Contract](#importing-the-evm-contract)
* [Creating a COA](#creating-a-coa)
* [Getting the EVM Address of a COA](#getting-the-evm-address-of-a-coa)
* [Getting the Flow Balance of a COA](#getting-the-flow-balance-of-a-coa)
* [Depositing and Withdrawing Flow Tokens](#depositing-and-withdrawing-flow-tokens)
  + [Depositing Flow Tokens](#depositing-flow-tokens)
  + [Withdrawing Flow Tokens](#withdrawing-flow-tokens)
* [Direct Calls to Flow EVM](#direct-calls-to-flow-evm)
  + [Transferring FLOW in EVM](#transferring-flow-in-evm)
  + [Transfer ERC20](#transfer-erc20)
  + [Transfer ERC721](#transfer-erc721)
* [Deploying a Contract to Flow EVM](#deploying-a-contract-to-flow-evm)
* [More Information](#more-information)

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