# Source: https://developers.flow.com/build/cadence/smart-contracts/best-practices/security-best-practices

Cadence Security Best Practices | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            - [Learn Cadence ↗️](/build/cadence/learn-cadence)- [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)- [Deploying Contracts](/build/cadence/smart-contracts/deploying)- [Testing Smart Contracts](/build/cadence/smart-contracts/testing-strategy)- [Cadence Testing Framework](/build/cadence/smart-contracts/testing)- [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)

                        * [Security Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)* [Contract Upgrades with Incompatible Changes](/build/cadence/smart-contracts/best-practices/contract-upgrades)* [Development Standards](/build/cadence/smart-contracts/best-practices/project-development-tips)+ [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Writing and Deploying Smart Contracts* Best Practices* Security Best Practices

On this page

# Cadence Security Best Practices

This is an opinionated list of best practices Cadence developers should follow to write more secure Cadence code.

Some practices listed below might overlap with advice in the [Cadence Anti-Patterns](https://cadence-lang.org/docs/design-patterns) section, which is a recommended read as well.

## References[​](#references "Direct link to References")

[References](https://cadence-lang.org/docs/language/references) are ephemeral values and cannot be stored. If persistence is required, store a capability and borrow it when needed.

References allow free upcasting and downcasting. For example, a restricted type can cast to its unrestricted type, which exposes all `access(all)` functions and fields of the type. So, even if your capability uses an interface to restrict its functionality, it can still downcast to expose all other public functionality.

Therefore, any privileged functionality in a resource or struct that will have a public capability needs to have entitled accecss, for example `access(Owner)`. Then, the only way to access that functionality would be through an entitled reference, like `<auth(Owner) &MyResource>`.

## Account Storage[​](#account-storage "Direct link to Account Storage")

Don't trust a users' [account storage](https://cadence-lang.org/docs/language/accounts#account-storage). Users have full control over their data and may reorganize it as they see fit. Users may store values in any path, so paths may store values of "unexpected" types. These values may be instances of types in contracts that the user deployed.

Always [borrow](https://cadence-lang.org/docs/language/capabilities) with the specific type that is expected. Or, check if the value is an instance of the expected type.

## Authorized Accounts[​](#authorized-accounts "Direct link to Authorized Accounts")

Access to an `&Account` gives access to whatever is specified in the account entitlements list when that account reference is created. Therefore, [don't use Account references](https://cadence-lang.org/docs/anti-patterns#avoid-using-authaccount-as-a-function-parameter) as a function parameter or field unless absolutely necessary and only use the minimum set of entitlements required for the specified functionality so that other account functionality cannot be accessed.

It is preferable to use capabilities over direct `&Account` references when you expose account data. Capabilities revoke access by unlinking and limits the access to a single value with a certain set of functionality.

## Capabilities[​](#capabilities "Direct link to Capabilities")

Don't store anything under the [public capability storage](https://cadence-lang.org/docs/language/capabilities) unless strictly required. Anyone can access your public capability with `Account.capabilities.get`. If something needs to be stored under `/public/`, restrict privileged functions with entitlements to make sure only read functionality is provided.

When you publish a capability, the capability might already be present at the given `PublicPath`. In that case, Cadence will panic with a runtime error to not override the already published capability.

It is a good practice to check if the public capability already exists with `account.capabilities.get().check` before you create it. This function will return `nil` if the capability does not exist.

If there's a case where borrowing a capability might fail, use the `account.check` function to verify that the target exists and has a valid type.

Ensure that unauthorized parties cannot access capabilities. For example, capabilities should not be accessible through a public field, such as public dictionaries or arrays. When you expose a capability in such a way, anyone can borrow it and perform all actions that the capability allows.

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

Last updated on **Dec 4, 2025** by **cshannon1218**

[Previous

Cadence Testing Framework](/build/cadence/smart-contracts/testing)[Next

Contract Upgrades with Incompatible Changes](/build/cadence/smart-contracts/best-practices/contract-upgrades)

###### Rate this page

😞😐😊

Copy as Markdown

* [References](#references)* [Account Storage](#account-storage)* [Authorized Accounts](#authorized-accounts)* [Capabilities](#capabilities)* [Transactions](#transactions)* [Types](#types)* [Access Control](#access-control)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.