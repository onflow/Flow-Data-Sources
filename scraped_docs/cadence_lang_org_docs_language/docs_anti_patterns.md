# Source: https://cadence-lang.org/docs/anti-patterns




Cadence Anti-Patterns | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
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


* Anti-Patterns
On this page
# Cadence Anti-Patterns

This is an opinionated list of issues that can be improved if they are found in Cadence code intended for production.

## Avoid using fully authorized account references as a function parameter[​](#avoid-using-fully-authorized-account-references-as-a-function-parameter "Direct link to Avoid using fully authorized account references as a function parameter")

### Problem[​](#problem "Direct link to Problem")

A developer may choose to authenticate or perform operations for their users by using the users' account reference or addresses.
In order to do this, they might add a parameter to a function which has an authorized account reference type (`auth(...) &Account`),
as an authorized account reference can only be obtained by signing a transaction.

If it is a fully authorized account reference, this is problematic,
as the fully-authorized account reference allows access to some sensitive operations on the account,
for example, to write to storage, which provides the opportunity for bad actors to take advantage of.

### Example:[​](#example "Direct link to Example:")

 `_39..._39// BAD CODE_39// DO NOT COPY_39_39// Imagine this code is in a contract that uses a `auth(Storage) &Account` parameter_39// to authenticate users to transfer NFTs_39_39// They could deploy the contract with an Ethereum-style access control list functionality_39_39access(all)_39fun transferNFT(id: UInt64, owner: auth(Storage) &Account) {_39 assert(owner(id) == owner.address)_39_39 transfer(id)_39}_39_39// But they could upgrade the function to have the same signature_39// so it looks like it is doing the same thing, but they could also drain a little bit_39// of FLOW from the user's vault, a totally separate piece of the account that_39// should not be accessible in this function_39// BAD_39_39access(all)_39fun transferNFT(id: UInt64, owner: auth(Storage) &Account) {_39 assert(owner(id) == owner.address)_39_39 transfer(id)_39_39 // Sneakily borrow a reference to the user's Flow Token Vault_39 // and withdraw a bit of FLOW_39 // BAD_39 let vaultRef = owner.borrow<&FlowToken.Vault>(/storage/flowTokenVault)!_39 let stolenTokens <- vaultRef.withdraw(amount: 0.1)_39_39 // deposit the stolen funds in the contract owners vault_39 // BAD_39 contractVault.deposit(from: <-stolenTokens)_39}_39...`
### Solution[​](#solution "Direct link to Solution")

Projects should find other ways to authenticate users, such as using resources and capabilities as authentication objects.
They should also expect to perform most storage and linking operations within transaction bodies
rather than inside contract utility functions.

There are some scenarios where using an authorized account reference (`auth(...) &Account`) is necessary,
such as a cold storage multi-sig,
but those cases are rare and should only be used if it is a very restricted subset
of account functionality that is required.

## Public functions and fields should be avoided[​](#public-functions-and-fields-should-be-avoided "Direct link to Public functions and fields should be avoided")

### Problem[​](#problem-1 "Direct link to Problem")

Be sure to keep track of access modifiers when structuring your code, and make public only what should be public.
Accidentally exposed fields can be a security hole.

### Solution[​](#solution-1 "Direct link to Solution")

When writing your smart contract, look at every field and function and make sure
that require access through an [entitlement](/docs/language/access-control#entitlements) (`access(E)`),
or use a non-public [access modifier](/docs/language/access-control) like `access(self)`, `access(contract)`, or `access(account)`,
unless otherwise needed.

## Capability-Typed public fields are a security hole[​](#capability-typed-public-fields-are-a-security-hole "Direct link to Capability-Typed public fields are a security hole")

This is a specific case of "Public Functions And Fields Should Be Avoided", above.

### Problem[​](#problem-2 "Direct link to Problem")

The values of public fields can be copied. Capabilities are value types,
so if they are used as a public field, anyone can copy it from the field
and call the functions that it exposes.
This almost certainly is not what you want if a capability
has been stored as a field on a contract or resource in this way.

### Solution[​](#solution-2 "Direct link to Solution")

For public access to a capability, place it in an accounts public area so this expectation is explicit.

## Public admin resource creation functions are unsafe[​](#public-admin-resource-creation-functions-are-unsafe "Direct link to Public admin resource creation functions are unsafe")

This is a specific case of "Public Functions And Fields Should Be Avoided", above.

### Problem[​](#problem-3 "Direct link to Problem")

A public function on a contract that creates a resource can be called by any account.
If that resource provides access to admin functions then the creation function should not be public.

### Solution[​](#solution-3 "Direct link to Solution")

To fix this, a single instance of that resource should be created in the contract's initializer,
and then a new creation function can be potentially included within the admin resource, if necessary.

### Example[​](#example-1 "Direct link to Example")

 `_48// Pseudo-code_48_48// BAD_48access(all)_48contract Currency {_48_48 access(all)_48 resource Admin {_48_48 access(all)_48 fun mintTokens()_48 }_48_48 // Anyone in the network can call this function_48 // And use the Admin resource to mint tokens_48 access(all)_48 fun createAdmin(): @Admin {_48 return <-create Admin()_48 }_48}_48_48// This contract makes the admin creation private and in the initializer_48// so that only the one who controls the account can mint tokens_48// GOOD_48access(all)_48contract Currency {_48_48 access(all)_48 resource Admin {_48_48 access(all)_48 fun mintTokens()_48_48 // Only an admin can create new Admins_48 access(all)_48 fun createAdmin(): @Admin {_48 return <-create Admin()_48 }_48 }_48_48 init() {_48 // Create a single admin resource_48 let firstAdmin <- create Admin()_48_48 // Store it in private account storage, so only the admin can use it_48 self.account.storage.save(<-firstAdmin, to: /storage/currencyAdmin)_48 }_48}`
## Do not modify smart contract state or emit events in public struct initializers[​](#do-not-modify-smart-contract-state-or-emit-events-in-public-struct-initializers "Direct link to Do not modify smart contract state or emit events in public struct initializers")

This is another example of the risks of having publicly accessible parts to your smart contract.

### Problem[​](#problem-4 "Direct link to Problem")

Data structure definitions in Cadence currently must be declared as public so that they can be used by anyone.
Structs do not have the same restrictions that resources have on them,
which means that anyone can create a new instance of a struct without going through any authorization.

### Solution[​](#solution-4 "Direct link to Solution")

Any contract state-modifying operations related to the creation of structs
should be contained in resources instead of the initializers of structs.

### Example[​](#example-2 "Direct link to Example")

This used to be a bug in the NBA Top Shot smart contract, so we'll use that as an example.
Before, when it created a new play,
[it would initialize the play record with a struct,](https://github.com/dapperlabs/nba-smart-contracts/blob/55645478594858a6830e4ab095034068ef9753e9/contracts/TopShot.cdc#L155-L158)
which increments the number that tracks the play IDs and emits an event:

 `_27// Simplified Code_27// BAD_27//_27access(all)_27contract TopShot {_27_27 // The Record that is used to track every unique play ID_27 access(all)_27 var nextPlayID: UInt32_27_27 access(all)_27 struct Play {_27_27 access(all)_27 let playID: UInt32_27_27 init() {_27_27 self.playID = TopShot.nextPlayID_27_27 // Increment the ID so that it isn't used again_27 TopShot.nextPlayID = TopShot.nextPlayID + 1_27_27 emit PlayCreated(id: self.playID, metadata: metadata)_27 }_27 }_27}`

This is a risk because anyone can create the `Play` struct as many times as they want,
which could increment the `nextPlayID` field to the max `UInt32` value,
effectively preventing new plays from being created. It also would emit bogus events.

This bug was fixed by
[instead updating the contract state in the admin function](https://github.com/dapperlabs/nba-smart-contracts/blob/master/contracts/TopShot.cdc#L682-L685)
that creates the plays.

 `_40// Update contract state in admin resource functions_40// GOOD_40//_40access(all)_40contract TopShot {_40_40 // The Record that is used to track every unique play ID_40 access(all)_40 var nextPlayID: UInt32_40_40 access(all)_40 struct Play {_40_40 access(all)_40 let playID: UInt32_40_40 init() {_40 self.playID = TopShot.nextPlayID_40 }_40 }_40_40 access(all)_40 resource Admin {_40_40 // Protected within the private admin resource_40 access(all)_40 fun createPlay() {_40 // Create the new Play_40 var newPlay = Play()_40_40 // Increment the ID so that it isn't used again_40 TopShot.nextPlayID = TopShot.nextPlayID + UInt32(1)_40_40 emit PlayCreated(id: newPlay.playID, metadata: metadata)_40_40 // Store it in the contract storage_40 TopShot.playDatas[newPlay.playID] = newPlay_40 }_40 }_40}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/anti-patterns.md)[PreviousDesign Patterns](/docs/design-patterns)[NextDevelopment Standards](/docs/project-development-tips)
###### Rate this page

😞😐😊

* [Avoid using fully authorized account references as a function parameter](#avoid-using-fully-authorized-account-references-as-a-function-parameter)
  + [Problem](#problem)
  + [Example:](#example)
  + [Solution](#solution)
* [Public functions and fields should be avoided](#public-functions-and-fields-should-be-avoided)
  + [Problem](#problem-1)
  + [Solution](#solution-1)
* [Capability-Typed public fields are a security hole](#capability-typed-public-fields-are-a-security-hole)
  + [Problem](#problem-2)
  + [Solution](#solution-2)
* [Public admin resource creation functions are unsafe](#public-admin-resource-creation-functions-are-unsafe)
  + [Problem](#problem-3)
  + [Solution](#solution-3)
  + [Example](#example-1)
* [Do not modify smart contract state or emit events in public struct initializers](#do-not-modify-smart-contract-state-or-emit-events-in-public-struct-initializers)
  + [Problem](#problem-4)
  + [Solution](#solution-4)
  + [Example](#example-2)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

