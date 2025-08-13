# Source: https://cadence-lang.org/docs/solidity-to-cadence

Cadence Guide for Solidity Developers | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
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

* Cadence Guide for Solidity Developers

On this page

# Cadence Guide for Solidity Developers

Cadence introduces a different way to approach smart contract development, which may feel unfamiliar to Solidity developers. There are fundamental mindset and platform differences, and also several new language features that have no real equivalent in Solidity. As a result, while you can make similar programs in Cadence as you could in Solidity, a direct translation from one to the other isn't possible - similar to how you could make a note-taking app in C or in JavaScript, but it wouldn't be possible to directly translate the C code into JavaScript. You'd have to write an entirely new program for a new paradigm.

This guide outlines high level design and conceptual aspects of Flow and Cadence that are essential to understand, platform and integration differences, as well as detailed guidance on how to perform certain common Solidity development tasks using Cadence idioms. We also provide details on how to best leverage Cadence's unique features and how to avoid common pitfalls that may come up while transitioning.

## Conceptual foundations for Cadence[​](#conceptual-foundations-for-cadence "Direct link to Conceptual foundations for Cadence")

A fundamental difference to get used to when adjusting to Cadence from Solidity is **mindset**. Security and interoperability on Ethereum are designed around addresses (or more specifically, the account associated with an address), resulting in all contracts having to carefully track and evaluate access and authorizations.

![Ethereum Ownership](/assets/images/ethereum-ownership-e99f5e9b44f2cc0f7507da34abb5a74f.png)

Transactions are based on who authorized them, which is provided as `msg.sender` in the transaction context. User-to-contract, or contract-to-contract interactions, must be explicitly coded **in the contract and in advance** to ensure the appropriate approvals have been made before interacting with a contract. The contract-based nature of storage means that user ownership in Ethereum is represented in a mapping (e.g., from owner to balance or token ID to owner). Put another way, ownership is tracked in ledger records similar to a person's bank balance. Crypto wallets help combine balances from multiple token types into a convenient view for the user.

Cadence introduces new primitives and distinct functionalities, namely [Resources](/docs/language/resources) and [Capabilities](/docs/language/capabilities), that are designed around Flow's account model. Resources are first-class language types, which are unique, non-copyable, and cannot be discarded. These properties make resources ideal for representing digital assets like currency or tokens that are always limited in number. Resources are always stored in account storage, and contracts control access to them using capabilities. Capabilities are another special type that secures protected resources without the need for tracking addresses. Cadence makes working with these straightforward and intuitive to those familiar with object-oriented programming languages.

### Scripts and transactions[​](#scripts-and-transactions "Direct link to Scripts and transactions")

One of the most important (and powerful!) difference between Cadence and Solidity is that deployed contracts are not the only code being executed in the VM. Cadence offers scripts and transactions, which are written in Cadence and always exist offchain. However, they are the top-level code payload being executed by the execution runtime. Clients send scripts and transactions through the Flow Access API gRPC or REST endpoints, returning results to clients when applicable.

Scripts and transactions enable more efficient and powerful ways to integrate dapps with the underlying blockchain, where contracts can more purely be thought of as services or components, with scripts or transactions becoming the dapp-specific API interface for chain interactions.

What this means is that you **don't have to predict the future** when writing your contracts and your **views aren't limited to functions in the contract**. Even more importantly, you can **write transactions that call multiple functions with multiple deployed contracts that you don't need to own** and are signed with one signature.

Scripts are read-only in nature, requiring only a `main` function declaration that performs [queries](https://github.com/onflow/flow-ft/blob/master/transactions/scripts/get_balance.cdc) against a chain state. For example:

`_13

// This script reads the balance field of an account's ExampleToken Balance

_13

import FungibleToken from "../../contracts/FungibleToken.cdc"

_13

import ExampleToken from "../../contracts/ExampleToken.cdc"

_13

_13

access(all)

_13

fun main(account: Address): UFix64 {

_13

let acct = getAccount(account)

_13

let vaultRef = acct.capabilities

_13

.borrow<&ExampleToken.Vault>(ExampleToken.VaultPublicPath)

_13

?? panic("Could not borrow Balance reference to the Vault")

_13

_13

return vaultRef.balance

_13

}`

[Transactions](https://github.com/onflow/flow-ft/tree/master/transactions) are an Atomic, Consistent, Isolated, and Durable (ACID) version of scripts having only `prepare` and `execute` functions that either succeed in full and mutate the chain state as described, or otherwise fail and mutate nothing. They also support a setting of `pre` and `post` conditions. In the following transaction example, `ExampleToken`s are deposited into multiple `receiver` vaults for each address in the input map:

`` _40

import FungibleToken from "../contracts/FungibleToken.cdc"

_40

import ExampleToken from "../contracts/ExampleToken.cdc"

_40

_40

/// Transfers tokens to a list of addresses specified in the `addressAmountMap` parameter

_40

transaction(addressAmountMap: {Address: UFix64}) {

_40

_40

// The Vault resource that holds the tokens that are being transferred

_40

let vaultRef: auth(FungibleToken.Withdraw) &ExampleToken.Vault

_40

_40

prepare(signer: auth(BorrowValue) &Account) {

_40

_40

// Get a reference to the signer's stored ExampleToken vault

_40

self.vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &ExampleToken.Vault>(

_40

from: ExampleToken.VaultStoragePath

_40

) ?? panic("The signer does not store an ExampleToken.Vault object at the path "

_40

.concat(ExampleToken.VaultStoragePath.toString())

_40

.concat(". The signer must initialize their account with this vault first!"))

_40

}

_40

_40

execute {

_40

_40

for address in addressAmountMap.keys {

_40

_40

// Withdraw tokens from the signer's stored vault

_40

let sentVault <- self.vaultRef.withdraw(amount: addressAmountMap[address]!)

_40

_40

// Get the recipient's public account object

_40

let recipient = getAccount(address)

_40

_40

// Get a reference to the recipient's Receiver

_40

let receiverRef = recipient.capabilities

_40

.borrow<&{FungibleToken.Receiver}>(ExampleToken.ReceiverPublicPath)

_40

?? panic("Could not borrow receiver reference to the recipient's Vault")

_40

_40

// Deposit the withdrawn tokens in the recipient's receiver

_40

receiverRef.deposit(from: <-sentVault)

_40

_40

}

_40

}

_40

} ``

Transactions can encompass an arbitrary number of withdrawals/deposits across multiple FTs, sending to multiple addresses or other more complex variations, all of which will succeed or fail in their entirety given their ACID properties.

## Flow account model[​](#flow-account-model "Direct link to Flow account model")

The [Flow account model](https://developers.flow.com/build/basics/accounts.md) in Cadence combines storage for the keys and code ("smart contracts") associated with an account with storage for the assets owned by that account. That's right — in Cadence, your tokens are stored in your account, and not in a smart contract. Of course, smart contracts still define these assets and how they behave, but those assets can be securely stored in a user's account through the magic of Resources:

![Account Structure](data:image/png;base64,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)

There is only one account type in Cadence that uses an account address, similar to an Externally-Owned-Account (EOA) address in Ethereum. Unlike Ethereum contracts, Cadence accounts directly store contract code. Accounts realize ownership on Flow by being the container where keys, resources, and contracts are stored onchain.

## Account[​](#account "Direct link to Account")

`Account` is the type that provides access to an account.

The `getAccount` function allows you to get access to the publicly available functions and fields of an account. For example, this allows querying an account's balance.

An authorized `Account` reference provides access and allows the management of the account's storage, key configuration, and contract code. An authorized `Account` reference can only be acquired by signing a transaction. Capabilities ensure that resources held in an account can be safely shared and accessed.

## Resources[​](#resources "Direct link to Resources")

Resources are unique, [linear types](https://en.wikipedia.org/wiki/Substructural_type_system#Linear_type_systems) that can never be copied or implicitly discarded, and can only be moved between accounts. Static checks during development flag an error for a failure to store a resource moved from an account if that resource is not appropriately moved back into storage for a same or new account, or explicitly destroyed. The run-time enforces the same strict rules in terms of allowed operations. Therefore, contract functions that do not properly handle resources in scope before exiting will abort, reverting the resource to the original storage. These features of resources make them perfect for representing tokens, both fungible and non-fungible. Ownership is tracked by where they are stored, and the assets can't be duplicated or accidentally lost since the language itself enforces correctness.

Flow encourages the storage of data and compute onchain and resource-types makes this easier than ever. Since resources are always stored in accounts, any data and code that exists in resource instances is seamlessly managed onchain without any explicit handling needed.

## Capability-based access[​](#capability-based-access "Direct link to Capability-based access")

Remote access to stored objects is managed via [Capabilities](/docs/language/capabilities). This means that if an account wants to be able to access another account's stored objects, it must have been provided with a valid capability to that object. Capabilities can be either public or private. An account can share a public capability if it wants to give all other accounts access. For example, it's common for an account to accept fungible token deposits from all sources via a public capability. Alternatively, an account can grant private capabilities to specific accounts in order to provide access to restricted functionality. For example, a non-fungible token (NFT) project often controls minting through an "administrator capability" that grants specific accounts the power to mint new tokens.

## Contract standards[​](#contract-standards "Direct link to Contract standards")

There are numerous widely-used contract standards established to benefit the ecosystem. For example, [Fungible Token](https://developers.flow.com/build/flow.md#flow-token) (FT) and [Non-Fungible Token](https://developers.flow.com/build/flow.md#overview) (NFT) are standards that are conceptually equivalent to Ethereum's ERC-20 and ERC-721 standards. Cadence's object-oriented design means standards apply through contract sub-types such as resources, resource interfaces, or other types declared in the contract standard. Standards can define and limit behavior and/or set conditions that implementations of the standard cannot violate.

Detailed information about available standards and other core contracts can be found in the [Introduction to Flow](https://developers.flow.com/build/flow.md).

### NFT standard and metadata[​](#nft-standard-and-metadata "Direct link to NFT standard and metadata")

Solidity must manage NFT metadata offchain, and NFTs frequently link to IPFS-hosted JSON from onchain.

The Cadence NFT standard provides built-in support for metadata with specific types called [views](https://developers.flow.com/build/flow.md). Views can be added to NFTs when minted and will always be available as part of the NFT. While metadata is stored onchain, graphics and video content are stored offchain. Cadence provides [utility views](https://developers.flow.com/build/flow.md) for both HTTP- and IPFS-based media storage, which remain linked to your NFT.

Using NFT metadata views is a requirement to get listed in the [Flow NFT Catalog](https://www.flow-nft-catalog.com/). Projects are encouraged to leverage the NFT catalog since wallets and other ecosystem partners can seamlessly integrate new collections added there with no input from project creators.

NFT metadata on Flow opens the door to exciting new possibilities that help builders innovate. Check out this recent [case study](https://flow.com/post/flovatar-nft-flow-blockchain-case-study) where a community partner leveraged SVG-based metadata to make combined 2D + 3D versions of their PFPs, all onchain inside the NFTs' metadata!

Under most circumstances, NFTs bridged via the [Cross-VM Bridge](https://developers.flow.com/tutorials/cross-vm-apps/vm-bridge) from Flow Cadence to Flow EVM will automatically be provided with

## Security and access control[​](#security-and-access-control "Direct link to Security and access control")

Decentralized application development places significant focus on security and access, which can fairly be described as security engineering. Understanding how resources, capabilities, and the account model solve this may not be obvious when viewed from a Solidity perspective.

### msg.sender considered harmful[​](#msgsender-considered-harmful "Direct link to msg.sender considered harmful")

The first question that every Solidity developer asks when they start programming in Cadence is:

***How do I get the account that authorized the transaction?***

In Ethereum, this account is referred to as `msg.sender` and it informs the program flow in a function depending on who authorized it. Doing so is key to access and security, and is the basis of identity and ownership on Ethereum.

Cadence does not support `msg.sender`, and there is no transaction-level way for Cadence code to uniquely identify the calling account. Even if there was a way to access it, Cadence supports [multi-sig](#multi-key-multi-signature-support) transactions, meaning that a list of all the signers' accounts would be returned, making it impossible to identify a single authorizer.

The reason `msg.sender` is both unsupported and strongly advised against is that Cadence uses capabilities for access rather than addresses. The mindset change that developers need to adjust to is that a capability must first be obtained by the authorizing account (called the provider or signer in Cadence) from the contract that will require it, which then enables the requesting account to access the protected function or resource. This means the contract never needs to know who the signer is before proceeding because the capability **IS** the authorization.

In EVM, the contract grants access to an address or addresses, thus it must know and operate based on the address of the signer:

![Access-Based Security](data:image/png;base64,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)

The [capability-based security](https://en.wikipedia.org/wiki/Capability-based_security) model of Cadence frames access in the opposite direction from the [access-based security](https://en.wikipedia.org/wiki/Access-control_list) model. Accounts are granted and store the capability to access and use functionality on the contract:

![Capability-Based Security](/assets/images/capability-based-security-4046a36bf7b697f21defdb290ce27eb8.png)

### Access control using capabilities[​](#access-control-using-capabilities "Direct link to Access control using capabilities")

Solidity lacks specific types or other primitives to aid with permission management. Developers must inline guards to `require` at every function entry point, thus validating the `msg.sender` of the transaction.

[Capabilities](/docs/language/capabilities) are defined by linking storage paths (namespaces for contract storage) to protected objects and then making that linked capability available to other accounts.

Any account can get access to an account's public capabilities. Public capabilities are created using public paths (i.e., they have the domain `public`). For example, all accounts have a default public capability linked to the `FlowToken.Vault` resource. This vault is exposed as a public [unentitled](/docs/language/access-control#entitlements) capability, allowing any account to `borrow()` a reference to the Vault to make a `deposit()`. Since only the unentitled functions defined under the [`FungibleToken.Vault`](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc#L167) interface are exposed, the borrower of the vault reference cannot call `withdraw()`, since the method requires a `Withdraw` entitled reference on the underlying vault.

Accounts can share private capabilities, but must be specifically issued by the authorizing account. After [issuing](/docs/language/accounts/capabilities#issuing-capabilities), they can be obtained from authorized account objects (`Account`) but not public accounts (`PublicAccount`). To share a private capability with another account, the owning account must `publish` it to another account, which places it in the [account inbox](/docs/language/accounts/inbox) (not to be mistaken with `capabilities publish`). The recipient can later claim the capability from the account inbox using the `claim` function.

Public Capabilities can be `unpublished` and any capability can also be [revoked](/docs/design-patterns#capability-revocation) by the creating account.

To aid automation, events are emitted for completed `publish`, `claim`, and `unpublish` actions for a Capability.

Detailed information can be found in [Capabilities](/docs/language/capabilities).

### Hygiene factors for protecting value[​](#hygiene-factors-for-protecting-value "Direct link to Hygiene factors for protecting value")

While capabilities grant account access to a protected resource, it's still necessary to impose controls on the value accessed through them. For example, if your use case requires delegating access to a `FlowToken.Vault` to `withdraw()` funds, it's important to limit the amount. Tokens implementing FT/NFT standards are the primary type of value being exchanged by accounts on Flow. The standard provides the primitives needed to implement capability-limiting best practices.

**Token isolation**

All FTs reside in a `Vault` resource, and each different FT will exist as a separate `Vault` in an account. Similarly, all NFTs implement a `Collection` resource, in which those NFTs held by an account for that collection are stored.

Whenever access to the `withdraw()` function has to be delegated to another account, the simplest way to limit how many tokens of a given type can be withdrawn is to create a new `Vault` resource for that token type and move a smaller amount of the tokens in the main token `Vault`. A capability is then linked to that `Vault` instance before being made available to another account.

A similar pattern can be used for NFTs, where a new `Collection` resource can be created into which only those NFTs that should be exposed are moved. A capability is then linked to that `Collection` instance before being made available to another account.

**Bespoke control strategies**

For more complex use cases, you can create a new resource that implements the relevant interfaces to match those of the protected resource(s) that it wraps. The code for the new resource can then enforce limits as required and control how and when a delegation to the underlying resource occurs. One such example is the community-developed [`ScopedFTProviders`](https://github.com/green-goo-dao/flow-utils/blob/main/contracts/ScopedFTProviders.cdc) and [`ScoptedNFTProviders`](https://github.com/green-goo-dao/flow-utils/blob/main/contracts/ScopedNFTProviders.cdc) utility contracts.

### Admin roles[​](#admin-roles "Direct link to Admin roles")

Compared to Solidity, creating an admin role in Cadence requires a little more code, all of which is encapsulated within a resource. The admin object design can be highly customized and employ capabilities and [entitlements](/docs/language/access-control#entitlements) for fine-grained control, such as limiting access to individual functions, on a per-account basis if required. The complexity needed for admin roles may vary — for example, larger organizations may require more complex role-based-access schemes. The use of a resource in this context is key — the instance can't be copied, and the account with the first edition mint of the admin serves as the root admin. The admin can be implemented to mint additional admin resource instances, which only the root-admin can grant to selected user accounts via a capability. Conveniently, because the admin role is only accessible via a capability, it's easy to manage with [Capability Revocation](/docs/design-patterns#capability-revocation).

The admin role originates from the [init singleton pattern](/docs/design-patterns#init-singleton) and uses the [Capability Bootstrapping](/docs/design-patterns#capability-bootstrapping) pattern for making the Capability available to other accounts.

An example admin role implementation is available in the [Cadence cookbook](https://cookbook.onflow.org/?preview=13).

### Role-based access[​](#role-based-access "Direct link to Role-based access")

Implementing role-based access can be achieved by defining roles as resources managed by the root-admin account. Roles can provide limited access to functions, which guard other protected resources that include access levels and/or what is exposed, varying from role to role. The root admin can grant accounts access to individual roles through a private capability. Functions that the roles are permitted to invoke may be scoped as `access(contract)` to enforce that they can only be called by code paths in the root-admin contract.

## Other best practices and conventions[​](#other-best-practices-and-conventions "Direct link to Other best practices and conventions")

Certain well-established best practices for Solidity may not apply or are handled differently.

### Check effects interactions[​](#check-effects-interactions "Direct link to Check effects interactions")

Solidity contracts must use the [check effect interaction](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html) because functions are public by default and address-based access means that guards must exist when program flow concedes control to an external contract. There are two reasons why this is significantly less of a problem in Cadence. Functions are private by default, and the language provides a range of [access scopes](/docs/language/access-control). More importantly, *risks associated with ceding control to an external contract* is an Ethereum phenomenon; the risk no longer applies. This is primarily because Cadence contracts are not static singletons, so control is never lost to another contract during the scope of a transaction.

### Guard check[​](#guard-check "Direct link to Guard check")

Solidity uses `revert`, `require`, and `assert` to validate inputs. `require` is a product of the address-based nature of Solidity, which capabilities replace. `revert` is similar to Cadence's `panic` in that a transaction is aborted. Cadence provides an `assert` operator, which mirrors `assert` in Solidity.

### Modifiers[​](#modifiers "Direct link to Modifiers")

Modifiers are extensively used in Solidity when enforcing pre-checks within a function. This is a powerful language feature. However, modifiers can also mutate a state, which introduces risks to the program control flow.

Cadence uses `pre` and `post` blocks to validate input values or the function execution outputs. Notably, a `pre` and `post` block prohibits the changing of a state and may only enforce conditions.

Another difference is that modifiers in Solidity can be reused within the contract multiple times. Cadence `pre` and `post` blocks are associated with individual functions only, reducing the likelihood of errors but resulting in a small amount of code duplication.

### Error handling[​](#error-handling "Direct link to Error handling")

Solidity offers a try/catch block to handle errors; however, there is presently no equivalent in Cadence.

## Integration differences[​](#integration-differences "Direct link to Integration differences")

There are a few notable integration differences between Cadence and Solidity, which are described in the following sections.

### Contract imports and dynamic contract borrowing[​](#contract-imports-and-dynamic-contract-borrowing "Direct link to Contract imports and dynamic contract borrowing")

Contracts in Ethereum are similar to static singletons in that interactions happen directly between users and the functions declared on the contract instance itself. The object-oriented nature of Cadence means that contracts are more accurately viewed as imported dependencies. The imported contract makes its object graph available for the code at runtime. Rather than interacting with a contract singleton instance, account interactions to access capabilities are the primary integration entry point, allowing the user to interact with the returned objects.

Dynamic borrowing of a contract inlines the loading of a contract based on its contract address. The loaded contract can be cast to the contract standard interface to which it conforms to (e.g., NFT standard) and then interacted with in the same way if it were statically imported. Consider the implications of this for the composability of contracts.

Detailed information about deploying, updating, removing, or borrowing contracts can be found in [Contracts](/docs/language/contracts).

### Multi-key, multi-signature support[​](#multi-key-multi-signature-support "Direct link to Multi-key, multi-signature support")

Solidity supports only one kind of multi-signature scheme where `n` out of `m` (assuming `m >= n`) approvals need to be obtained to execute the transaction from the multi-signature smart contract. The most used multi-signature smart contract in the Ethereum ecosystem is the Gnosis [safe contract](https://github.com/safe-global/safe-contracts/blob/main/contracts/Safe.sol). However, Solidity lacks support for signature aggregation or BLS signature schemes.

Cadence offers a wide range of options to implement various multi-signature schemes, including:

* Inherent support for multi-sign transactions.
* Resource transfer scheme.
* Inherent support of the BLS signature scheme.

Flow account keys have assigned weights, where a 1000 unit weight is the cumulative weight needed from signing keys to execute a transaction successfully. One can divide weights arbitrarily across multiple keys and distribute those partial weighted keys to authorized signers. When signing the transaction, all signers must sign the transaction together in a short period of time in order for the cumulative weight to reach 1000 units.

See the [BLS Signature scheme](/docs/language/crypto#bls-multi-signature) for a detailed overview of the inherent support of BLS signatures.

**Resource transfer scheme**

The main limitation of multi-signature transactions is that signatures must all be made for the transaction within a relatively short time window. If this window is missed, the transaction will abort. The resource transfer scheme is very similar to the Solidity multi-signature smart contract. A resource is created that has the functionality to proxy the execution of a fund transfer. This resource is handed from one signer to the next to collect signatures. Once the threshold of required signatures is met, the transaction is executed. The main drawback with this approach is that it does not support the execution of arbitrary functionality.

## Other platform differences[​](#other-platform-differences "Direct link to Other platform differences")

The following differences, which are unrelated to implementing Cadence contracts, are useful to understand in the context of application design.

### Events[​](#events "Direct link to Events")

Flow uses [events](/docs/language/events) extensively to provide real-time signals to offchain systems about particular actions that occurred during a transaction. The main difference in Flow is that events remain part of the history and are not purged from storage. Events can be populated with arbitrary data that will assist consumers of the event. Builders are encouraged to leverage events for seamless UX as users perform transactions.

### Contract upgradeability[​](#contract-upgradeability "Direct link to Contract upgradeability")

Flow supports limited upgradability of Cadence contracts, which is most helpful during development. The following function shows how an account owner can update a contract:

`_10

fun update(name: String, code: [UInt8]): DeployedContract`

Upgrades are analyzed for prohibited changes once uploaded for an upgrade. Upgradeability is still an early-phase feature, which will continue to improve over time.

To enforce immutability once a contract is tested and ready to deploy, account owners can optionally revoke keys from the account containing the contract.

Detailed information about the cadence upgradeability is available in [Contract Updatability](/docs/language/contract-updatability).

### Account key formulation[​](#account-key-formulation "Direct link to Account key formulation")

In EVM-based chains, an address is derived from a cryptographically generated public key and can have a single private key, supporting one type of signature curve (i.e., ECDSA). They are not verifiable offchain and typos/truncation in an address may result in funds being lost.

Flow account addresses have a special format and are verifiable offchain. Verifying address format validity can be done using an error detection algorithm based on linear code. While this does not also confirm that an address is active onchain, the extra verifiability is a useful safeguard.

### Contract size constraints[​](#contract-size-constraints "Direct link to Contract size constraints")

Solidity developers will be well aware of the [EIP-170](https://eips.ethereum.org/EIPS/eip-170) deployable contract bytecode size limit of 24KB. This can burden builders who need to optimize contract bytecode size, sometimes even requiring a re-design of contracts to break it into smaller contract parts.

By contrast, Cadence has no inherent or defined smart contract size limit. However, it is restricted by the transaction size limit, which is 1.5MB. With very rare exceptions, it's unlikely that this limit would pose a problem to those developing Cadence contracts. Should it be needed, there is a known way to deploy a contract exceeding 1.5MB, which we will document at a later time.

## Low-level language differences[​](#low-level-language-differences "Direct link to Low-level language differences")

There are several language differences between Solidity and Cadence, which are described in the following sections.

### Arithmetic[​](#arithmetic "Direct link to Arithmetic")

Historically, Solidity, smart contracts lost millions of dollars because of improper handling of arithmetic under/overflows. Contemporary Solidity versions offer inbuilt handling of under/overflow for arithmetic operations.

Cadence implements [saturating math](https://en.wikipedia.org/wiki/Saturation_arithmetic), which avoids overflow/underflow.

### Optional support[​](#optional-support "Direct link to Optional support")

[Optional binding](/docs/language/control-flow#optional-binding) provides built-in conditional handling of nil values. Regular data types in Cadence must always have a value and cannot be nil. Optionals enable variables or constants that might contain a certain type or a nil value. Optional bindings have two cases: either there is a value or there is nothing — they fork program flow similar to `if nil; else; end;`.

### Iterable dictionaries[​](#iterable-dictionaries "Direct link to Iterable dictionaries")

Solidity offers the mapping type, however it is not iterable. Because of that, dapp developers have to maintain offchain tracking to have access to keys. This also pushes builders to create custom data types like `EnumerableMap`, which adds to gas costs.

Cadence offers the [Dictionary](/docs/language/control-flow) type, an unordered collection of key-value associations, which is iterable.

### Rich support for type utility functions[​](#rich-support-for-type-utility-functions "Direct link to Rich support for type utility functions")

Cadence offers numerous native-type utility functions to simplify development. For example, the String type provides:

* `utf8`
* `length`
* `concat()`
* `slice()`
* `split()`
* `replaceAll()`
* `join()`
* `decodeHex()`
* `encodeHex()`
* `fromCharacters()`
* `fromUTF8()`
* `toLower()`

### Argument labelling[​](#argument-labelling "Direct link to Argument labelling")

Argument labels in Cadence help to disambiguate input values. They make code more readable and explicit. They also eliminate confusion around the order of arguments when working with the same type. They must be included in the function call, but this restriction can be skipped if the label is preceded by `_`  on its declaration.

For example:

* if `fun foo(balance: UFix64)`, which is called as `self.foo(balance: 30.0)`
* then, `fun foo( _balance: UFix64)` can be called as `self.foo(balance: 30.0)` or as `self.foo(30.0)`.

One thing to note about argument labelling is that function overloading is not currently supported in Cadence. This means that functions with the same name but different argument labels are not allowed, which is an available feature in Solidity.

### Additional resources[​](#additional-resources "Direct link to Additional resources")

* [On-Chain Token Transfer Deep Dive](https://flow.com/engineering-blogs/flow-blockchain-programming-language-smart-contract-cadence-solidity-comparison-ethereum) — Cadence or Solidity
* [Bored Ape Yacht Club](https://flow.com/post/implementing-the-bored-ape-yacht-club-smart-contract-in-cadence) — Implementing a smart contract in Cadence
* [Comparing AA on Ethereum vs Flow](https://www.quicknode.com/guides/other-chains/flow/account-abstraction-on-flow#account-abstraction-on-ethereum-vs-flow) — Quicknode's account abstraction on the Flow blockchain

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/solidity-to-cadence.md)

[Previous

Why Use Cadence?](/docs/why)[Next

First Steps](/docs/tutorial/first-steps)

###### Rate this page

😞😐😊

* [Conceptual foundations for Cadence](#conceptual-foundations-for-cadence)
  + [Scripts and transactions](#scripts-and-transactions)
* [Flow account model](#flow-account-model)
* [Account](#account)
* [Resources](#resources)
* [Capability-based access](#capability-based-access)
* [Contract standards](#contract-standards)
  + [NFT standard and metadata](#nft-standard-and-metadata)
* [Security and access control](#security-and-access-control)
  + [msg.sender considered harmful](#msgsender-considered-harmful)
  + [Access control using capabilities](#access-control-using-capabilities)
  + [Hygiene factors for protecting value](#hygiene-factors-for-protecting-value)
  + [Admin roles](#admin-roles)
  + [Role-based access](#role-based-access)
* [Other best practices and conventions](#other-best-practices-and-conventions)
  + [Check effects interactions](#check-effects-interactions)
  + [Guard check](#guard-check)
  + [Modifiers](#modifiers)
  + [Error handling](#error-handling)
* [Integration differences](#integration-differences)
  + [Contract imports and dynamic contract borrowing](#contract-imports-and-dynamic-contract-borrowing)
  + [Multi-key, multi-signature support](#multi-key-multi-signature-support)
* [Other platform differences](#other-platform-differences)
  + [Events](#events)
  + [Contract upgradeability](#contract-upgradeability)
  + [Account key formulation](#account-key-formulation)
  + [Contract size constraints](#contract-size-constraints)
* [Low-level language differences](#low-level-language-differences)
  + [Arithmetic](#arithmetic)
  + [Optional support](#optional-support)
  + [Iterable dictionaries](#iterable-dictionaries)
  + [Rich support for type utility functions](#rich-support-for-type-utility-functions)
  + [Argument labelling](#argument-labelling)
  + [Additional resources](#additional-resources)