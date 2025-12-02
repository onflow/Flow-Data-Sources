# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/account-management

Account Linking | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                - [Building Walletless Applications Using Child Accounts](/blockchain-development-tutorials/cadence/account-management/child-accounts)- [Working With Parent Accounts](/blockchain-development-tutorials/cadence/account-management/parent-accounts)- [Account Linking With NBA Top Shot](/blockchain-development-tutorials/cadence/account-management/account-linking-with-dapper)+ [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* Account Linking

On this page

# Account Linking

Account linking is a unique Flow concept that allows sharing ownership over [accounts](/build/cadence/basics/accounts). To understand how we can achieve that, we must first understand how to access accounts on Flow.

You can access accounts on flow in Cadence through two types, `PublicAccount` and `Account`. As the name implies, the
`PublicAccount` type gives access to all public account information such as address, balance, storage capacity, etc.,
but doesn't allow changes to the account. The `Account` type (or more specifically, an
[entitled](https://cadence-lang.org/docs/language/access-control#entitlements) `&Account`) allows the same access as
`PublicAccount` but also allows changes to the account, which includes adding or revoking account keys, managing the deployed
contracts, as well as linking and publishing Capabilities.

![Flow account structure](/assets/images/account-structure-835ec18016e0f43c6b4a4fea2e54934f.png)

## Accessing Account[​](#accessing-account "Direct link to Accessing Account")

Accessing `Account` allows for modification to account storage, so it's essential to mandate that the account being accessed signs all transactions, which safeguards this access.
[Account
entitlements](https://cadence-lang.org/docs/language/accounts/#performing-write-operations) allow for more granular
access control over the specific parts of the account that you can access from within the signed transaction. A
transaction can list multiple authorizing account it wants to access as part of the `prepare` section of the
transaction. Read more about transaction signing in the [transaction documentation](/build/cadence/basics/transactions).

Since access to the `Account` object allows state change, the idea of account ownership actually translates to the
ability to access the underlying account. Traditionally, you might consider this the same as having key access on an
account, but we'll see in just a minute how programmatic, ownership-level access is unlocked with [Capabilities on
Flow](https://cadence-lang.org/docs/language/capabilities).

## Account Capabilities[​](#account-capabilities "Direct link to Account Capabilities")

Before you continue with this section, you'll need a clear understanding of [Cadence
capabilities](https://cadence-lang.org/docs/language/capabilities). Advanced features such as
Account Capabilities are powerful, but they can put your app or users at risk if used incorrectly.

Cadence allows for Capabilities creation to delegate access to account storage, which means any account that obtains a valid
Ccapability to another account object in the storage can access it. This is a powerful feature on its own - accessing
another account programmatically without the need for an active key on the accessible account. You can limit the access to the object when you create a Capability so your users can only access intended functions or fields.

Account linking is made possible by the extension of Capabilities on the `Account` object itself. Similar to how storage
capabilities allow access to a value stored in an account's storage, `&Account` Capabilities allow delegated access to
the issuing `Account`. These Capabilities allow for access to key assignment, contract deployment, and other privileged
actions on the delegating `Account` - effectively sharing ownership of the account without ever adding or sharing a key.
This Capability can of course be revoked at any time by the delegating account.

### Creating Account Links[​](#creating-account-links "Direct link to Creating Account Links")

When we refer to 'account linking,' we mean that the parent account creates an `&Account` Capability and published
to another account. The account that owns the `&Account` Capability which was made available to another account is the child
account. The account in possession of the Capability given by the child account becomes its parent account.

![Account linking on Flow relational diagram](/assets/images/account-linking-relational-diagram-9ea0dedfb84460d27a1e78e2a6c40b65.png)

You can create a link between two existing accounts on Flow in two steps:

1. A child account creates an `&Account` Capability and publishes it to the parent account.
2. The parent account, claims that Capability and can access the child's account through it.

![Account linking steps on Flow](/assets/images/account-linking-steps-high-level-9c15a8877e4e8133713cf05807c9624a.png)

These two steps are implemented in Cadence as two transactions:

**\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***Create capability\*\*\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\*\*\*

The account B creates and publishes the `&Account` Capability to the account A at the address `0x01`

`_12

#allowAccountLinking

_12

_12

transaction {

_12

prepare(signer: auth(IssueAccountCapabilityController, PublishInboxCapability) &Account) {

_12

// Issue a fully-entitled account capability

_12

let capability = signer.capabilities

_12

.account

_12

.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

_12

// Publish the capability for the specified recipient

_12

signer.inbox.publish(capability, name: "accountCapA", recipient: 0x1)

_12

}

_12

}`

\***\*\*\*\*\*\*\***\*\*\*\*\***\*\*\*\*\*\*\***Claim capability\***\*\*\*\*\*\*\***\*\*\*\*\***\*\*\*\*\*\*\***

The account A claims the Capability published by account B.

`_18

transaction {

_18

prepare(signer: auth(ClaimInboxCapability) &Account) {

_18

let capabilityName = "accountCapB"

_18

let providerAddress = 0x2

_18

// Claim the capability published by the account 0x2

_18

let capability = signer.inbox

_18

.claim<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>(

_18

capabilityName,

_18

provider: providerAddress

_18

) ?? panic(

_18

"Capability with name ".concat(capabilityName)

_18

.concat(" from provider ").concat(providerAddress.toString())

_18

.concat(" not found")

_18

)

_18

// Simply borrowing an Account reference here for demonstration purposes

_18

let accountRef = capability.borrow()!

_18

}

_18

}`

## What is account linking most useful for?[​](#what-is-account-linking-most-useful-for "Direct link to What is account linking most useful for?")

Account linking was specifically designed to allow smooth and seamless custodial onboarding of users to your Flow based
application without them first requiring a wallet to do so. This pattern overcomes both the technical hurdle, as well as
user's reluctance to install a wallet, which opens access to Flow applications to every user. Users can experience an app
without any delay while still offering a path to self-sovreign ownership.

Naturally, users may expect to use their account with another application, or otherwise move assets stored in that
account elsewhere - at minimum from their wallet. When an app initially leverages account linking, the app creates the
account instead of the user and stores that user's specific state in the app-created account. At a later point, users
can take ownership of the app account providing they possess a full [Flow account](/build/cadence/basics/accounts), typically
by installing a wallet app.

Account linking allows users to possess multiple linked child accounts from different apps. Complexities associated
with accessing those child accounts are eliminated by abstracting access to them through the user's parent account.

info

Simply put, child accounts are accessed and can be treated as a seamless part of the parent account.

All assets in the app account can now jump the walled garden to play in the rest of the Flow ecosystem. The user does
not need to rely on the custodial app to execute transactions moving assets from the child account as the parent account
already has access to the assets in the child account.

![Multiple parent-child accounts on Flow](/assets/images/account-linking-multiple-accounts-19cad9db0d1f1abdde126848033b3e43.png)

This shared control over the digital items in the in-app account allows users to establish real ownership of the items
beyond the context of the app, where they can use their parent account to view inventory, take the items to other apps
in the ecosystem, such as a marketplace or a game.

Most importantly, users can do this without the need to transfer the digital items between accounts, which makes it
seamless to continue using the original app and enjoy their assets in other contexts.

## Security Considerations[​](#security-considerations "Direct link to Security Considerations")

Account linking is a *very* powerful Cadence feature, and thus it must be treated with care. So far in this document,
we've discussed account linking between two accounts we own, even if a third-party
application manages the child account. But, we can't make the same trust assumptions about custodial accounts in the real world.

If we create an `&Account` Capability and publish it to an account we don't own, we give that account full
access to our account. This should be seen as an anti-pattern.

warning

If you create an `&Account` Capability and share it with a third-party account, you effectively give that person your
account's private keys.

Because unfiltered account linking can be dangerous, Flow introduces the [`HybridCustody`
contract](/blockchain-development-tutorials/cadence/account-management/parent-accounts) that helps custodial applications regulate access and allows parent accounts to
manage their many child accounts and assets within them.

## Hybrid Custody and Account Linking[​](#hybrid-custody-and-account-linking "Direct link to Hybrid Custody and Account Linking")

Apps need assurances that their own resources are safe from malicious actors, so to permit full access might not be what they want. Hybrid custody contracts will allow the app to maintain control of their managed accounts, but they can:

1. Share capabilities freely, with a few built-in controls over the types of capabilities that can be retrieved by
   parent accounts via helper contracts (the `CapabilityFactory`, and `CapabilityFilter`).
2. Share additional capabilities (public or private) with a parent account via a `CapabilityDelegator` resource.

Learn more about it in the [Hybrid Custody documentation](/blockchain-development-tutorials/cadence/account-management/parent-accounts).

### Guides[​](#guides "Direct link to Guides")

* [Building Walletless Applications Using Child Accounts](/blockchain-development-tutorials/cadence/account-management/child-accounts) covers how apps can leverage Account
  Linking to create a seamless user experience and allow future self-custody.
* [Working With Parent Accounts](/blockchain-development-tutorials/cadence/account-management/parent-accounts) covers features enabled by the core `HybridCustody` contract to
  access child account assets from parent accounts. This is useful for apps like marketplaces or wallets that are
  working with accounts that have potential child accounts.

### Resources[​](#resources "Direct link to Resources")

* [Forum Post](https://forum.flow.com/t/hybrid-custody/4016) where core concepts were introduced and discussed.
* [GitHub repository](https://github.com/onflow/hybrid-custody) where `HybridCustody` core contracts and scripts are
  maintained. Check out the repository for more advanced script or transaction examples.
* [Example](https://github.com/jribbink/magic-link-hc-sample/) Account Linking project with
  [Magic](https://magic.link/).
* [Starter template](https://github.com/Niftory/niftory-samples/tree/main/walletless-onboarding) for
  [Niftory](https://niftory.com/) Account Linking API.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/account-management/index.md)

Last updated on **Nov 3, 2025** by **cshannon1218**

[Previous

Upgrading Cadence Contracts](/blockchain-development-tutorials/cadence/cadence-advantages/upgrading-cadence-contracts)[Next

Building Walletless Applications Using Child Accounts](/blockchain-development-tutorials/cadence/account-management/child-accounts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Accessing Account](#accessing-account)* [Account Capabilities](#account-capabilities)
    + [Creating Account Links](#creating-account-links)* [What is account linking most useful for?](#what-is-account-linking-most-useful-for)* [Security Considerations](#security-considerations)* [Hybrid Custody and Account Linking](#hybrid-custody-and-account-linking)
          + [Guides](#guides)+ [Resources](#resources)

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