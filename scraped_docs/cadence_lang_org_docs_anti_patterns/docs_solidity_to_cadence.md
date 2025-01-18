# Source: https://cadence-lang.org/docs/solidity-to-cadence




Guide for Solidity Developers | Cadence




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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Guide for Solidity Developers
On this page

Cadence introduces a different way to approach smart contract development which may feel unfamiliar to Solidity
developers. There are fundamental mindset and platform differences, and also several new language features that have no
real equivalent in Solidity. This guide outlines high level design and conceptual aspects of Flow and Cadence that are
essential to understand, platform and integration differences, as well as detailed guidance on how to perform certain
common Solidity development tasks using Cadence idioms. We also provide details on how best to leverage Cadence's unique
features and how to avoid common pitfalls that may come up while transitioning.

# Conceptual foundations for Cadence

A fundamental difference to get used to when adjusting to Cadence from Solidity is mindset. Security and
interoperability on Ethereum are designed around addresses (or more specifically the account associated with an
address), resulting in all contracts having to carefully track and evaluate access and authorizations.

![](https://storage.googleapis.com/flow-resources/documentation-assets/solidity-to-cadence/ethereum-ownership.png)

Transactions are based on who authorized them, which is provided as `msg.sender` in the transaction context. User to
contract, or contract to contract interactions must be explicitly coded to ensure the appropriate approvals have been
made before interacting with a contract. The contract based nature of storage means that user ownership in Ethereum is
represented in a mapping, for example from owner to balance, or token ID to owner. Put another way, ownership is tracked
in ledger records similar to a person's bank balance. Crypto wallets help combine balances from multiple token types
into a convenient view for the user.

Cadence introduces new primitives and distinct functionalities, namely Resources and Capabilities, that are designed
around Flow's account model. Resources are first-class language types which are unique, non-copyable, and which cannot
be discarded. These properties make Resources ideal for representing digital assets like currency or tokens that are
always limited in numbers. Resources are always stored in account storage and contracts control access to them using
Capabilities. Capabilities are another special type that secure protected resources without the need for tracking
addresses. Cadence makes working with these straightforward and intuitive to those familiar with object-oriented
programming languages.

Newcomers to Cadence should ensure they understand the following major concepts before development.

## Flow account model[​](#flow-account-model "Direct link to Flow account model")

![](https://storage.googleapis.com/flow-resources/documentation-assets/solidity-to-cadence/account-structure.png)

The [Flow account model](https://developers.flow.com/build/basics/accounts.md) in Cadence combines storage for the keys
and code (”smart contracts”) associated with an account with storage for the assets owned by that account. That’s right:
In Cadence, your tokens are stored in your account, and not in a smart contract. Of course, smart contracts still define
these assets and how they behave, but those assets can be securely stored in a user’s account through the magic of
Resources.

There is only one account type in Cadence also with an account address, similar to an Externally-Owned-Account (EOA)
address in Ethereum. However, unlike Ethereum contract-accounts, accounts in Cadence also store contract code. Accounts
realize ownership on Flow in being the container where keys, Resources, and contracts are stored on-chain.

## Account[​](#account "Direct link to Account")

`Account` is the type that provides access to an account.

The `getAccount` function allows getting access to the publicly available functions and fields of an account. For
example, this allows querying an accounts balance.

An authorized `Account` reference provides access and allows the management of, for instance, the account's storage,
keys configuration, and contract code. An authorized `Account` reference can only be acquired by signing a transaction.
Capabilities ensure that resources held in an account can be safely shared/accessed.

## Resources[​](#resources "Direct link to Resources")

Resources are unique, [linear-types](https://en.wikipedia.org/wiki/Substructural_type_system#Linear_type_systems) which
can never be copied or implicitly discarded, only moved between accounts. If, during development, a function fails to
store a Resource obtained from an account in the function scope, semantic checks will flag an error. The run-time
enforces the same strict rules in terms of allowed operations. Therefore, contract functions which do not properly
handle Resources in scope before exiting will abort, reverting them to the original storage. These features of Resources
make them perfect for representing tokens, both fungible and non-fungible. Ownership is tracked by where they are
stored, and the assets can’t be duplicated or accidentally lost since the language itself enforces correctness.

Flow encourages storing of data and compute on-chain and Resource-types makes this easier than ever. Since Resources are
always stored in accounts, any data and code that exists in Resource instances is seamlessly managed on-chain without
any explicit handling needed.

## Capability-based access[​](#capability-based-access "Direct link to Capability-based access")

Remote access to stored objects can be managed via [Capabilities](/docs/language/capabilities). This means that if an
account wants to be able to access another account's stored objects, it must have been provided with a valid Capability
to that object. Capabilities can be either public or private. An account can share a public Capability if it wants to
give all other accounts access. (For example, it’s common for an account to accept fungible token deposits from all
sources via a public Capability.) Alternatively, an account can grant private Capabilities to specific accounts in order
to provide access to restricted functionality. For example, an NFT project often controls minting through an
“administrator Capability” that grants specific accounts with the power to mint new tokens.

## Contract standards[​](#contract-standards "Direct link to Contract standards")

There are numerous widely-used contract standards established to benefit the ecosystem, for example [Fungible
Token](https://developers.flow.com/build/flow.md#flow-token)(FT) and [Non-Fungible
Token](https://developers.flow.com/build/flow#overview)(NFT) standards which are conceptually equivalent to Ethereum's
ERC-20 and ERC-721 standards. Cadence's object-oriented design means standards apply through contract sub-types such as
Resources, Resource interfaces, or other types declared in the contract standard. Standards can define and limit
behaviour and/or set conditions which implementations of the standard cannot violate.

Detailed information about available standards and other core contracts can be found in [Introduction to
Flow](https://developers.flow.com/build/flow.md).

### NFT standard and metadata[​](#nft-standard-and-metadata "Direct link to NFT standard and metadata")

Solidity must manage NFT metadata off-chain and NFTs typically link to IPFS JSON from on-chain.

The Cadence NFT standard provides in-built support for metadata with specific types called
[views](https://developers.flow.com/build/flow.md#flow-nft#overview#nft-metadata). Views can be added to NFTs when
minted and will always be available as part of the NFT. While metadata is stored on-chain, graphics and video content
are stored off-chain. Cadence provides [utility
views](https://developers.flow.com/build/flow.md#flow-nft#overview#list-of-common-views) for both HTTP and IPFS based
media storage which remain linked to your NFT.

Using NFT metadata views is a requirement to get listed in the [Flow NFT Catalog](https://www.flow-nft-catalog.com/).
Projects are encouraged leverage the NFT catalog since wallets and other ecosystem partners can seamlessly integrate new
collections added there with no input from project creators.

NFT metadata on Flow opens the door to exciting new possibilities that help builders innovate. Check out this recent
[case study](https://flow.com/post/flovatar-nft-flow-blockchain-case-study) where a community partner leveraged SVG
based metadata to make combined 2D + 3D versions of their PFPs, all on-chain inside the NFTs metadata!

# Security and access control

Decentralized application development places significant focus on security and access and can fairly be described as
security engineering. Understanding how Resources, Capabilities and the account model solve this may not be obvious when
viewed from a Solidity perspective.

## msg.sender considered harmful[​](#msgsender-considered-harmful "Direct link to msg.sender considered harmful")

The first question that every Solidity developer asks when they start programming in Cadence is:

**"How do I get the account who authorized the transaction?"**

In Ethereum this account is referred to as `msg.sender` and informs the program flow in a function depending on who
authorized it. Doing so is key to access and security, and is the basis of identity and ownership on Ethereum.

Cadence does not have `msg.sender` and there is no transaction-level way for Cadence code to uniquely identify the
calling account. Even if there was a way to access it, Cadence supports [multi-sig](#multi-key-multi-signature-support)
transactions, meaning that a list of all the signers' accounts would be returned, making it impossible to identify a
single authorizer.

![Solidity access applies to the subject and possessed and validated by the protected
resource](https://storage.googleapis.com/flow-resources/documentation-assets/solidity-to-cadence/access-based-security.png)

The reason `msg.sender` is both unsupported and strongly advised against is because Cadence uses Capabilities for access
rather than addresses. The mindset change that developers need to adjust to is that a capability must first be obtained
by the authorizing account (called provider or signer in Cadence) from the contract that will require it, which then
enables the requesting account to access the protected function or Resource. This means the contract never needs to know
who the signer is before proceeding because the capability **IS** the authorization.

![In Cadence, the subject must possess the Capability to access the protected
resource](https://storage.googleapis.com/flow-resources/documentation-assets/solidity-to-cadence/capability-based-security.png)

The [capability-based security](https://en.wikipedia.org/wiki/Capability-based_security) model frames access in the
opposite direction than the [access-based security](https://en.wikipedia.org/wiki/Access-control_list) model.

## Access control using Capabilities[​](#access-control-using-capabilities "Direct link to Access control using Capabilities")

Solidity lacks specific types or other primitives to aid with permission management. Developers have to inline guards to
`require` at every function entry-point, thus validating the `msg.sender` of the transaction.

[Capabilities](/docs/language/capabilities) are defined by linking storage paths (namespaces for contract storage) to
protected objects and then making that linked capability available to other accounts.

Any account can get access to an account's public Capabilities. Public capabilities are created using public paths, i.e.
they have the domain `public`. For example, all accounts have a default public capability linked to the
`FlowToken.Vault` Resource. This vault is exposed as a public [unentitled](/docs/language/access-control#entitlements)
capability allowing any account to `borrow()` a
reference to the Vault to make a `deposit()`. Since only the unentitled functions defined under the
[`FungibleToken.Vault`](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc#L167) interface are
interface are exposed, the borrower of the vault reference cannot call `withdraw()` since the method requires a `Withdraw` entitled
reference on the underlying vault.

Accounts can share private capabilities but must be specifically issued by the authorizing account. After
[issuing](/docs/language/accounts/capabilities#issuing-capabilities), they can be obtained from authorised account
objects (`Account`) but not public accounts (`PublicAccount`). To share a private Capability with another account, the
owning account must `publish` it to another account which places in the [account inbox](/docs/language/accounts/inbox)
(not to be mistaken with `capabilities.publish`). The recipient can later claim the Capability from the account inbox
using then `claim` function.

Public Capabilities can be `unpublished` and any Capability can also be
[revoked](/docs/design-patterns#capability-revocation) by the creating account.

To aid automation, events are emitted for `publish`, `claim` and `unpublish` actions completed for a Capability.

Detailed information can be found in [Capabilities](/docs/language/capabilities).

## Hygiene factors for protecting value[​](#hygiene-factors-for-protecting-value "Direct link to Hygiene factors for protecting value")

While capabilities grant account access to a protected resource, it's still necessary to impose controls on value
accessed through them. For example, if your use-case requires delegating access to a `FlowToken.Vault` to `withdraw()`
funds, it's important to limit the amount. Tokens implementing FT/NFT standards are the primary type of value being
exchanged by accounts on Flow. The standard provides the primitives needed to implement capability limiting
best-practices.

### Token isolation[​](#token-isolation "Direct link to Token isolation")

All FTs reside in a `Vault` Resource and each different FT will exist as a separate `Vault` in an account. Similarly,
all NFTs implement a `Collection` Resource, in which those NFTs held by an account for that collection are stored.

Whenever access to the `withdraw()` function has to be delegated to another account, the simplest way to limit how many
tokens of a given type can be withdrawn is to create a new `Vault` Resource for that token type and move a smaller
amount of the tokens in the main token `Vault`. A capability is then linked to that `Vault` instance before being made
available to another account.

A similar pattern can be used for NFTs, where a new `Collection` Resource can be created into which only those NFTs
which should be exposed are moved. A capability is then linked to that `Collection` instance before being made available
to another account.

### Bespoke control strategies[​](#bespoke-control-strategies "Direct link to Bespoke control strategies")

For more complex use-cases one might create a new Resource that implements the relevant interfaces to match those of the
protected Resource(s) which it wraps. The code for the new Resource can then enforce limits as required and control how
and when delegation to the underlying resource occurs. One such example is the community-developed
[`ScopedFTProviders`](https://github.com/green-goo-dao/flow-utils/blob/main/contracts/ScopedFTProviders.cdc) and
[`ScoptedNFTProviders`](https://github.com/green-goo-dao/flow-utils/blob/main/contracts/ScopedNFTProviders.cdc) utility
contracts.

## Admin roles[​](#admin-roles "Direct link to Admin roles")

Compared to Solidity, creating an admin role in Cadence requires a little more code, all of which is encapsulated within
a Resource. The admin object design can be highly customized and employ Capabilities and
[entitlements](/docs/language/access-control#entitlements) for fine-grained control such as limiting access to
individual functions, on a per-account basis if required. The complexity needed for admin roles may vary, for example,
larger organizations may require more complex role-based-access schemes. The use of a Resource in this context is key -
the instance can't be copied and the account with the first edition mint of the admin serves as the root-admin. The
admin can be implemented to mint additional admin Resource instances, which only the root-admin can grant to selected
user accounts via a Capability. Conveniently, because the admin role is only accessible via a Capability it's easy to
manage with [Capability Revocation](/docs/design-patterns#capability-revocation).

The admin role originates from the [init singleton pattern](/docs/design-patterns#init-singleton) and uses the
[Capability Bootstrapping](/docs/design-patterns#capability-bootstrapping) pattern for making the Capability available to
other accounts.

An example admin role implementation is available in [Cadence cookbook](https://cookbook.onflow.org/?preview=13).

### Role-based access[​](#role-based-access "Direct link to Role-based access")

Implementing role-based-access can be achieved by defining roles as Resources managed by the root-admin account. Roles
can provide limited access to functions which guard other protected resources, with access levels and/or what is exposed
varying from role to role. The root-admin can grant accounts access to individual roles through a private capability.
Functions that the roles are permitted to invoke may be scoped as `access(contract)` to enforce that they can only be
called by code paths in the root-admin contract.

# Other best practices and conventions

Certain well established best practices for Solidity may not apply or are handled differently.

## Check effects interactions[​](#check-effects-interactions "Direct link to Check effects interactions")

Solidity contracts must use the [check effect
interaction](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html) because functions are public
by default and address-based access means that guards must exist when program flow concedes control to an external
contract. There are two reasons why this is significantly less of a problem in Cadence. Functions are private by default
and the language provides a range of [access scopes](/docs/language/access-control). More importantly, 'risks associated
with ceding control to an external contract' is an Ethereum phenomenon; the risk no longer applies. This is primarily
because Cadence contracts are not static singletons, so control is never lost to another contract during the scope of a
transaction.

## Guard Check[​](#guard-check "Direct link to Guard Check")

Solidity uses `revert`, `require` & `assert` to validate inputs. `require` is a product of the address-based nature of
Solidity which Capabilities replace. `revert` is similar to Cadence's `panic` in that a transaction is aborted. Cadence
provides an `assert` operator which mirrors `assert` in Solidity.

## Modifiers[​](#modifiers "Direct link to Modifiers")

Modifiers are extensively used in Solidity when enforcing pre-checks within a function. This is a powerful language
feature. However, modifiers can also mutate state which introduces risks to program control flow.

Cadence uses `pre` and `post` blocks to validate input values or the function execution outputs. Notably, `pre` and
`post` block prohibit changing of state and may only enforce conditions.

Another difference is that modifiers in Solidity can be re-used within the contract multiple times. Cadence `pre` &
`post` blocks are associated to individual functions only, reducing the likelihood of errors but which results in a
small amount of code duplication.

## Error handling[​](#error-handling "Direct link to Error handling")

Solidity offers try/catch block to handle errors, however, there is presently no equivalent in Cadence.

# Integration differences

## Scripts and transactions[​](#scripts-and-transactions "Direct link to Scripts and transactions")

Another major difference between Cadence and Solidity is that deployed contracts are not the only code being executed in
the VM. Cadence offers scripts, of which a subset are transactions, and both permit arbitrary code. Scripts or
transactions are not deployed on-chain and always exist off-chain, however, they are the top-level code payload being
executed by the execution runtime. Clients send scripts and transactions through the Flow Access API gRPC or REST
endpoints, returning results to clients when applicable. Scripts and transactions enable more efficient and powerful
ways to integrate dapps with the underlying blockchain, where contracts can more purely be thought of as services or
components, with scripts or transactions becoming the dapp-specific API interface for chain interactions.

Scripts are read-only in nature, requiring only a `main` function declaration and which perform
[queries](https://github.com/onflow/flow-ft/blob/master/transactions/scripts/get_balance.cdc) against chain state, eg:

 `_13// This script reads the balance field of an account's ExampleToken Balance_13import FungibleToken from "../../contracts/FungibleToken.cdc"_13import ExampleToken from "../../contracts/ExampleToken.cdc"_13_13access(all)_13fun main(account: Address): UFix64 {_13 let acct = getAccount(account)_13 let vaultRef = acct.capabilities_13 .borrow<&ExampleToken.Vault>(ExampleToken.VaultPublicPath)_13 ?? panic("Could not borrow Balance reference to the Vault")_13_13 return vaultRef.balance_13}`

[Transactions](https://github.com/onflow/flow-ft/tree/master/transactions) are an ACID (Atomic, Consistent, Isolated and
Durable) version of scripts having only `prepare` and `execute` functions that either succeed in full and mutate chain
state as described, or otherwise fail and mutate nothing. They also support setting of `pre` and `post` conditions. In
the example transaction below `ExampleToken`s are deposited into multiple `receiver` vaults for each address in the
input map.

 `_40import FungibleToken from "../contracts/FungibleToken.cdc"_40import ExampleToken from "../contracts/ExampleToken.cdc"_40_40/// Transfers tokens to a list of addresses specified in the `addressAmountMap` parameter_40transaction(addressAmountMap: {Address: UFix64}) {_40_40 // The Vault resource that holds the tokens that are being transferred_40 let vaultRef: auth(FungibleToken.Withdraw) &ExampleToken.Vault_40_40 prepare(signer: auth(BorrowValue) &Account) {_40_40 // Get a reference to the signer's stored ExampleToken vault_40 self.vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &ExampleToken.Vault>(_40 from: ExampleToken.VaultStoragePath_40 ) ?? panic("The signer does not store an ExampleToken.Vault object at the path "_40 .concat(ExampleToken.VaultStoragePath.toString())_40 .concat(". The signer must initialize their account with this vault first!"))_40 }_40_40 execute {_40_40 for address in addressAmountMap.keys {_40_40 // Withdraw tokens from the signer's stored vault_40 let sentVault <- self.vaultRef.withdraw(amount: addressAmountMap[address]!)_40_40 // Get the recipient's public account object_40 let recipient = getAccount(address)_40_40 // Get a reference to the recipient's Receiver_40 let receiverRef = recipient.capabilities_40 .borrow<&{FungibleToken.Receiver}>(ExampleToken.ReceiverPublicPath)_40 ?? panic("Could not borrow receiver reference to the recipient's Vault")_40_40 // Deposit the withdrawn tokens in the recipient's receiver_40 receiverRef.deposit(from: <-sentVault)_40_40 }_40 }_40}`

Transactions can encompass an arbitrary number withdrawals/deposits, across multiple FTs, sending to multiple addresses,
or other more complex variations, all of which will succeed or fail in their entirety given their ACID properties.

## Contract imports and dynamic contract borrowing[​](#contract-imports-and-dynamic-contract-borrowing "Direct link to Contract imports and dynamic contract borrowing")

Contracts in Ethereum are similar to static singletons in that interactions happen directly between users and the
functions declared on the contract instance itself. The object-oriented nature of Cadence means that contracts are more
accurately viewed as imported dependencies. The imported contract makes its object graph available for the code at
runtime. Rather than interacting with a contract singleton instance, account interactions to access capabilities are the
primary integration entry point, allowing the user to interact with the returned objects.

Dynamic borrowing of a contract inlines the loading of a contract based on its contract address. The loaded contract can
be cast to the contract standard interface to which it conforms to (eg: NFT standard) and then interacted with in the
same way were it statically imported. Consider the implications of this for composability of contracts..

Detailed information about deploying, updating, removing or borrowing contracts can be found in
[Contracts](/docs/language/contracts)

## Multi-key, multi-signature support[​](#multi-key-multi-signature-support "Direct link to Multi-key, multi-signature support")

Solidity supports only one kind of multi-signature scheme where n out of m (assuming m >= n) approvals need to be
obtained to execute the transaction from the multi-signature smart contract. The most used multi-signature smart
contract in the Ethereum ecosystem is the gnosis [safe
contract](https://github.com/safe-global/safe-contracts/blob/main/contracts/Safe.sol). However, Solidity lacks support
for signature aggregation or BLS signature schemes.

Cadence offers a wide range of options to implement various multi-signature schemes.

* Inherent support for multi-sign transactions.
* Resource transfer scheme.
* Inherent support of the BLS signature scheme.

Flow account keys have assigned weights, where a 1000 unit weight is the cumulative weight needed from signing keys to
execute a transaction successfully. One can divide weights arbitrarily across multiple keys and distribute those partial
weighted keys to authorized signers. When signing the transaction, all signers must sign the transaction together in a
short period of time in order for the cumulative weight to reach 1000 units.

See [BLS Signature scheme](/docs/language/crypto#bls-multi-signature) for a detailed overview of the inherent support of
BLS signatures.

### Resource transfer scheme[​](#resource-transfer-scheme "Direct link to Resource transfer scheme")

The main limitation of multi-sig transactions is that signatures must all be made for the transaction within a
relatively short time window. If this window is missed, the transaction will abort. The resource transfer scheme is very
similar to the Solidity multi-signature smart contract. A Resource is created that has the functionality to proxy the
execution of a fund transfer. This Resource is handed from one signer to the next to collect signatures. Once the
threshold of required signatures is met the transaction is executed. The main drawback with this approach is that does
not support execution of arbitrary functionality.

# Other platform differences

The following differences unrelated to implementing Cadence contracts are useful to understand in the context of
application design.

## Events[​](#events "Direct link to Events")

Flow uses [events](/docs/language/events) extensively to provide real-time signals to off-chain systems about particular
actions that occurred during a transaction. The main difference on Flow is that events remain part of the history and
are not purged from storage. Events can be populated with arbitrary data that will assist consumers of the event.
Builders are encouraged to leverage events for seamless UX as users perform transactions.

## Contract upgradeability[​](#contract-upgradeability "Direct link to Contract upgradeability")

Flow supports limited upgradability of Cadence contracts which is most helpful during development. The following
function shows how an account owner can update a contract. Upgrades are analyzed for prohibited changes once uploaded
for upgrade. Upgradeability is still an early phase feature, which will continue to improve over time.

 `_10fun update(name: String, code: [UInt8]): DeployedContract`

To enforce immutability once a contract is tested and ready to deploy, account owners can optionally revoke keys from
the account containing the contract.

Detailed information about the cadence upgradeability is available in [Contract
updatability](/docs/language/contract-updatability).

## Account key formulation[​](#account-key-formulation "Direct link to Account key formulation")

In EVM-based chains, an address is derived from a cryptographically generated public key and can have a single private
key, supporting one type of signature curve, i.e. ECDSA. They are not verifiable off-chain and typos/truncation in an
address may result in funds being lost.

Flow account addresses have a special format and are verifiable off-chain. Verifying address format validity can be done
using an error detection algorithm based on linear code. While this does not also confirm that an address is active
on-chain the extra verifiability is a useful safeguard.

## Contract size constraints[​](#contract-size-constraints "Direct link to Contract size constraints")

Solidity developers will be well aware of the [EIP-170](https://eips.ethereum.org/EIPS/eip-170) deployable contract
bytecode size limit of 24KB. This can burden builders who need to optimize contract bytecode size, sometimes even
requiring a re-design of contracts to break it into smaller contract parts.

By contrast, Cadence has no inherent or defined smart contract size limit. However, it is restricted by the transaction
size limit which is 1.5MB. With very rare exceptions, it’s unlikely that this limit would pose a problem to those
developing Cadence contracts. Should it be needed, there is a known way to deploy a contract exceeding 1.5 MB which we
will document at a later time.

# Low level language differences

## Arithmetic[​](#arithmetic "Direct link to Arithmetic")

Historically, Solidity, smart contracts lost millions of dollars because of improper handling of arithmetic
under/overflows. Contemporary Solidity versions offer inbuilt handling of under/overflow for arithmetic operations.

Cadence implements [saturating math](https://en.wikipedia.org/wiki/Saturation_arithmetic) that avoids
overflow/underflow.

## Optional support[​](#optional-support "Direct link to Optional support")

[Optional bindings](/docs/language/control-flow) provide in-built conditional handling of nil values. Regular data types
in Cadence must always have a value and cannot be nil. Optionals enable variables / constants that might contain a
certain type or a nil value Optionals have two cases: either there is a value, or there is nothing; they fork program
flow similar to `if nil; else; end;`.

## Iterable Dictionaries[​](#iterable-dictionaries "Direct link to Iterable Dictionaries")

Solidity offers the mapping type, however, it is not iterable. Because of that dApp developers have to maintain
off-chain tracking to have access to keys. This also pushes builders to create custom datatypes like `EnumerableMap`
which adds to gas costs.

Cadence offers the [Dictionary](/docs/language/control-flow) type, an unordered collection of key-value associations
which is iterable.

## Rich support for type utility functions[​](#rich-support-for-type-utility-functions "Direct link to Rich support for type utility functions")

Cadence offers numerous native-type utility functions to simplify development. For example, the String type provides:

* utf8
* length
* concat()
* slice()
* split()
* replaceAll()
* join()
* decodeHex()
* encodeHex()
* fromCharacters()
* fromUTF8()
* toLower()

## Argument labelling[​](#argument-labelling "Direct link to Argument labelling")

Argument labels in Cadence help to disambiguate input values. They make code more readable and explicit. They also
eliminate confusion around the order of arguments when working with the same type. They must be included in the function
call. This restriction can be skipped if the label is preceded by `_`  on its declaration.

Eg: `fun foo(balance: UFix64)` called as `self.foo(balance: 30.0)`

`fun foo( _balance: UFix64)` can be called as `self.foo(balance: 30.0)` or as `self.foo(30.0)`

One thing to note about argument labelling is that function overloading is not currently supported in Cadence. This
means that functions with the same name but different argument labels are not allowed, a feature which is available in
Solidity.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

* Cadence or Solidity: [On-Chain Token Transfer Deep
  Dive](https://flow.com/engineering-blogs/flow-blockchain-programming-language-smart-contract-cadence-solidity-comparison-ethereum)
* Implementing the [Bored Ape Yacht
  Club](https://flow.com/post/implementing-the-bored-ape-yacht-club-smart-contract-in-cadence) smart contract in Cadence
* Quicknode's Account Abstraction on the Flow Blockchain: [Comparing AA on Ethereum vs
  Flow](https://www.quicknode.com/guides/other-chains/flow/account-abstraction-on-flow#account-abstraction-on-ethereum-vs-flow)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/solidity-to-cadence.md)[PreviousSecurity Best Practices](/docs/security-best-practices)[NextContract Upgrades with Incompatible Changes](/docs/contract-upgrades)
###### Rate this page

😞😐😊

* [Flow account model](#flow-account-model)
* [Account](#account)
* [Resources](#resources)
* [Capability-based access](#capability-based-access)
* [Contract standards](#contract-standards)
  + [NFT standard and metadata](#nft-standard-and-metadata)
* [msg.sender considered harmful](#msgsender-considered-harmful)
* [Access control using Capabilities](#access-control-using-capabilities)
* [Hygiene factors for protecting value](#hygiene-factors-for-protecting-value)
  + [Token isolation](#token-isolation)
  + [Bespoke control strategies](#bespoke-control-strategies)
* [Admin roles](#admin-roles)
  + [Role-based access](#role-based-access)
* [Check effects interactions](#check-effects-interactions)
* [Guard Check](#guard-check)
* [Modifiers](#modifiers)
* [Error handling](#error-handling)
* [Scripts and transactions](#scripts-and-transactions)
* [Contract imports and dynamic contract borrowing](#contract-imports-and-dynamic-contract-borrowing)
* [Multi-key, multi-signature support](#multi-key-multi-signature-support)
  + [Resource transfer scheme](#resource-transfer-scheme)
* [Events](#events)
* [Contract upgradeability](#contract-upgradeability)
* [Account key formulation](#account-key-formulation)
* [Contract size constraints](#contract-size-constraints)
* [Arithmetic](#arithmetic)
* [Optional support](#optional-support)
* [Iterable Dictionaries](#iterable-dictionaries)
* [Rich support for type utility functions](#rich-support-for-type-utility-functions)
* [Argument labelling](#argument-labelling)
* [Additional resources](#additional-resources)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

