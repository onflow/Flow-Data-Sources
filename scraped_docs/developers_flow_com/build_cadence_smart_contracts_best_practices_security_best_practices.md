# Source: https://developers.flow.com/build/cadence/smart-contracts/best-practices/security-best-practices

Cadence Security Best Practices | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

    - [Learn Cadence ↗️](/build/cadence/learn-cadence)
    - [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)
    - [Deploying Contracts](/build/cadence/smart-contracts/deploying)
    - [Testing Smart Contracts](/build/cadence/smart-contracts/testing)
    - [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)

      * [Security Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)
      * [Contract Upgrades with Incompatible Changes](/build/cadence/smart-contracts/best-practices/contract-upgrades)
      * [Development Standards](/build/cadence/smart-contracts/best-practices/project-development-tips)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

* Cadence
* Writing and Deploying Smart Contracts
* Best Practices
* Security Best Practices

On this page

# Cadence Security Best Practices

This is an opinionated list of best practices Cadence developers should follow to write more secure Cadence code.

Some practices listed below might overlap with advice in the [Cadence Anti-Patterns](https://cadence-lang.org/docs/design-patterns) section, which is a recommended read as well.

## References[​](#references "Direct link to References")

[References](https://cadence-lang.org/docs/language/references) are ephemeral values and cannot be stored. If persistence is required, store a capability and borrow it when needed.

References allow freely upcasting and downcasting, e.g. a restricted type can be cast to its unrestricted type which will expose all `access(all)` functions and fields of the type.
So even if your capability uses an interface to restrict its functionality, it can
still be downcasted to expose all other public functionality.

Therefore, any privileged functionality in a resource or struct that will have a public
capability needs to have entitled accecss, for example `access(Owner)`.
Then, the only way to access that functionality would be through an entitled reference,
like `<auth(Owner) &MyResource>`.

## Account Storage[​](#account-storage "Direct link to Account Storage")

Don't trust a users' [account storage](https://cadence-lang.org/docs/language/accounts#account-storage). Users have full control over their data and may reorganize it as they see fit. Users may store values in any path, so paths may store values of "unexpected" types. These values may be instances of types in contracts that the user deployed.

Always [borrow](https://cadence-lang.org/docs/language/capabilities) with the specific type that is expected. Or, check if the value is an instance of the expected type.

## Authorized Accounts[​](#authorized-accounts "Direct link to Authorized Accounts")

Access to an `&Account` gives access to whatever is specified in the account entitlements
list when that account reference is created.
Therefore, [avoid using Account references](https://cadence-lang.org/docs/anti-patterns#avoid-using-authaccount-as-a-function-parameter) as a function parameter or field unless absolutely necessary and only use the minimal set of entitlements required
for the specified functionality so that other account functionality cannot be accessed.

It is preferable to use capabilities over direct `&Account` references when exposing account data. Using capabilities allows the revocation of access by unlinking and limits the access to a single value with a certain set of functionality.

## Capabilities[​](#capabilities "Direct link to Capabilities")

Don't store anything under the [public capability storage](https://cadence-lang.org/docs/language/capabilities) unless strictly required. Anyone can access your public capability using `Account.capabilities.get`. If something needs to be stored under `/public/`, make sure only read functionality is provided by restricting privileged functions with entitlements.

When publishing a capability, the capability might already be present at the given `PublicPath`.
In that case, Cadence will panic with a runtime error to not override the already published capability.

It is a good practice to check if the public capability already exists with `account.capabilities.get().check` before creating it. This function will return `nil` if the capability does not exist.

If it is necessary to handle the case where borrowing a capability might fail, the `account.check` function can be used to verify that the target exists and has a valid type.

Ensure capabilities cannot be accessed by unauthorized parties. For example, capabilities should not be accessible through a public field, including public dictionaries or arrays. Exposing a capability in such a way allows anyone to borrow it and perform all actions that the capability allows.

## Transactions[​](#transactions "Direct link to Transactions")

Audits of Cadence code should also include [transactions](https://cadence-lang.org/docs/language/transactions), as they may contain arbitrary code, just, like in contracts. In addition, they are given full access to the accounts of the transaction's signers, i.e. the transaction is allowed to manipulate the signers' account storage, contracts, and keys.

Signing a transaction gives access to the `&Account`, i.e. access to the account's storage, keys, and contracts depending on what entitlements are specified.

Do not blindly sign a transaction. The transaction could for example change deployed contracts by upgrading them with malicious statements, revoking or adding keys, transferring resources from storage, etc.

## Types[​](#types "Direct link to Types")

Use [restricted types and interfaces](https://cadence-lang.org/docs/language/restricted-types). Always use the most specific type possible, following the principle of least privilege. Types should always be as restrictive as possible, especially for resource types.

If given a less-specific type, cast to the more specific type that is expected. For example, when implementing the fungible token standard, a user may deposit any fungible token, so the implementation should cast to the expected concrete fungible token type.

## Access Control[​](#access-control "Direct link to Access Control")

Declaring a field as [`access(all)`](https://cadence-lang.org/docs/language/access-control) only protects from replacing the field's value, but the value itself can still be mutated if it is mutable. Remember that containers, like dictionaries, and arrays, are mutable.

Prefer non-public access to a mutable state. That state may also be nested. For example, a child may still be mutated even if its parent exposes it through a field with non-settable access.

Do not use the `access(all)` modifier on fields and functions unless necessary. Prefer `access(self)`, `acccess(Entitlement)`, or `access(contract)` and `access(account)` when other types in the contract or account need to have access.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/smart-contracts/best-practices/security-best-practices.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Testing Smart Contracts](/build/cadence/smart-contracts/testing)[Next

Contract Upgrades with Incompatible Changes](/build/cadence/smart-contracts/best-practices/contract-upgrades)

###### Rate this page

😞😐😊

Copy as Markdown

* [References](#references)
* [Account Storage](#account-storage)
* [Authorized Accounts](#authorized-accounts)
* [Capabilities](#capabilities)
* [Transactions](#transactions)
* [Types](#types)
* [Access Control](#access-control)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.