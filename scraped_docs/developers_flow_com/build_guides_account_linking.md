# Source: https://developers.flow.com/build/guides/account-linking




Account Linking (FLIP 72) | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
  + [Create a Fungible Token](/build/guides/fungible-token)
  + [Create an NFT Project](/build/guides/nft)
  + [Account Linking (FLIP 72)](/build/guides/account-linking)
    - [Building Walletless Applications Using Child Accounts](/build/guides/account-linking/child-accounts)
    - [Working With Parent Accounts](/build/guides/account-linking/parent-accounts)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Building on Mobile](/build/guides/mobile/overview)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Guides
* Account Linking (FLIP 72)
On this page
# Account Linking

Account linking is a unique Flow concept that enables sharing ownership over [accounts](/build/basics/accounts). In
order to understand how we can achieve that we must first understand how accounts on Flow are accessed.

Accounts on flow can be accessed in Cadence through two types, `PublicAccount` and `Account`. As the name implies the
`PublicAccount` type gives access to all public account information such as address, balance, storage capacity, etc.,
but doesn't allow changes to the account. The `Account` type (or more specifically, an
[entitled](https://cadence-lang.org/docs/language/access-control#entitlements) `&Account`) allows the same access as
`PublicAccount` but also allows changes to the account, including adding/revoking account keys, managing the deployed
contracts, as well as linking and publishing Capabilities.

![Flow account structure](/assets/images/account-structure-835ec18016e0f43c6b4a4fea2e54934f.png)

## Accessing Account[​](#accessing-account "Direct link to Accessing Account")

Accessing `Account` allows for modification to account storage, so it's essential to safeguard this access by mandating
that transactions are signed by the account being accessed. [Account
entitlements](https://cadence-lang.org/docs/language/accounts/#performing-write-operations) enable for more granular
access control over the specific parts of the account that can be accessed from within the signed transaction. A
transaction can list multiple authorizing account it wants to access as part of the `prepare` section of the
transaction. Read more about transaction signing in the [transaction documentation](/build/basics/transactions).

Since access to the `Account` object enables state change, the idea of account ownership actually translates to the
ability to access the underlying account. Traditionally, you might consider this the same as having key access on an
account, but we'll see in just a minute how programmatic, ownership-level access is unlocked with [Capabilities on
Flow](https://cadence-lang.org/docs/language/capabilities).

## Account Capabilities[​](#account-capabilities "Direct link to Account Capabilities")

Before proceeding the reader will need a clear understanding of [Cadence
capabilities](https://cadence-lang.org/docs/language/capabilities) to follow this section. Advanced features such as
Account Capabilities are powerful but if used incorrectly can put your app or users at risk.

Cadence allows the creation of Capabilities to delegate access to account storage, meaning any account obtaining a valid
Ccapability to another account object in the storage can access it. This is a powerful feature on its own - accessing
another account programmatically without the need for an active key on the accessible account. The access to the object
can be limited when creating a Capability so only intended functions or fields can be accessed.

Account linking is made possible by the extension of Capabilities on the `Account` object itself. Similar to how storage
capabilities allow access to a value stored in an account's storage, `&Account` Capabilities allow delegated access to
the issuing `Account`. These Capabilities allow for access to key assignment, contract deployment, and other privileged
actions on the delegating `Account` - effectively sharing ownership of the account without ever adding or sharing a key.
This Capability can of course be revoked at any time by the delegating account.

### Creating Account Links[​](#creating-account-links "Direct link to Creating Account Links")

When referring to 'account linking' we mean that an `&Account` Capability is created by the parent account and published
to another account. The account owning the `&Account` Capability which was made available to another account is the child
account. The account in possession of the Capability given by the child account becomes its parent account.

![Account linking on Flow relational diagram](/assets/images/account-linking-relational-diagram-9ea0dedfb84460d27a1e78e2a6c40b65.png)

A link between two existing accounts on Flow can be created in two steps:

1. A child account creates an `&Account` Capability and publishes it to the parent account.
2. The parent account, claims that Capability and can access the child's account through it.

![Account linking steps on Flow](/assets/images/account-linking-steps-high-level-9c15a8877e4e8133713cf05807c9624a.png)

These two steps are implemented in Cadence as two transactions:

************************************Create capability************************************

The account B creates and publishes the `&Account` Capability to the account A at the address `0x01`

 `_12#allowAccountLinking_12_12transaction {_12 prepare(signer: auth(IssueAccountCapabilityController, PublishInboxCapability) &Account) {_12 // Issue a fully-entitled account capability_12 let capability = signer.capabilities_12 .account_12 .issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()_12 // Publish the capability for the specified recipient_12 signer.inbox.publish(capability, name: "accountCapA", recipient: 0x1)_12 }_12}`

****************************Claim capability****************************

The account A claims the Capability published by account B.

 `_18transaction {_18 prepare(signer: auth(ClaimInboxCapability) &Account) {_18 let capabilityName = "accountCapB"_18 let providerAddress = 0x2_18 // Claim the capability published by the account 0x2_18 let capability = signer.inbox_18 .claim<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>(_18 capabilityName,_18 provider: providerAddress_18 ) ?? panic(_18 "Capability with name ".concat(capabilityName)_18 .concat(" from provider ").concat(providerAddress.toString())_18 .concat(" not found")_18 )_18 // Simply borrowing an Account reference here for demonstration purposes_18 let accountRef = capability.borrow()!_18 }_18}`
## What is account linking most useful for?[​](#what-is-account-linking-most-useful-for "Direct link to What is account linking most useful for?")

Account linking was specifically designed to enable smooth and seamless custodial onboarding of users to your Flow based
application without them first requiring a wallet to do so. This pattern overcomes both the technical hurdle, as well as
user's reluctance to install a wallet, opening access to Flow applications to every user. Users can experience an app
without any delay while still offering a path to self-sovreign ownership.

Naturally, users may expect to use their account with another application, or otherwise move assets stored in that
account elsewhere - at minimum from their wallet. When an app initially leverages account linking, the app creates the
account instead of the user and stores that user's specific state in the app-created account. At a later point, users
can take ownership of the app account providing they possess a full [Flow account](/build/basics/accounts), typically
by installing a wallet app.

Account linking enables users to possess multiple linked child accounts from different apps. Complexities associated
with accessing those child accounts are eliminated by abstracting access to them through the user's parent account.

info

Simply put, child accounts are accessed and can be treated as a seamless part of the parent account.

All assets in the app account can now jump the walled garden to play in the rest of the Flow ecosystem. The user does
not need to rely on the custodial app to execute transactions moving assets from the child account as the parent account
already has access to the assets in the child account.

![Multiple parent-child accounts on Flow](/assets/images/account-linking-multiple-accounts-19cad9db0d1f1abdde126848033b3e43.png)

This shared control over the digital items in the in-app account enables users to establish real ownership of the items
beyond the context of the app, where they can use their parent account to view inventory, take the items to other apps
in the ecosystem, such as a marketplace or a game.

Most importantly, users are able to do this without the need to transfer the digital items between accounts, making it
seamless to continue using the original app while also enjoying their assets in other contexts.

## Security Considerations[​](#security-considerations "Direct link to Security Considerations")

Account linking is a *very* powerful Cadence feature, and thus it must be treated with care. So far in this document,
we’ve discussed account linking between two accounts we own, even if the child account is managed by a third-party
application. But, we can't make the same trust assumptions about custodial accounts in the real world.

Creating an `&Account` Capability and publishing it to an account we don’t own means we are giving that account full
access to our account. This should be seen as an anti-pattern.

warning

Creating an `&Account` Capability and sharing it with third-party account effectually the same as giving that person your
account's private keys.

Because unfiltered account linking can be dangerous, Flow introduces the [`HybridCustody`
contract](/build/guides/account-linking/parent-accounts) that helps custodial applications regulate access while enabling parent accounts to
manage their many child accounts and assets within them.

## Hybrid Custody and Account Linking[​](#hybrid-custody-and-account-linking "Direct link to Hybrid Custody and Account Linking")

Apps need assurances that their own resources are safe from malicious actors, so giving out full access might not be the
form they want. Using hybrid custody contracts, the app still maintains control of their managed accounts, but they can:

1. Share capabilities freely, with a few built-in controls over the types of capabilities that can be retrieved by
   parent accounts via helper contracts (the `CapabilityFactory`, and `CapabilityFilter`)
2. Share additional capabilities (public or private) with a parent account via a `CapabilityDelegator` resource

Learn more about it in the [Hybrid Custody documentation](/build/guides/account-linking/parent-accounts).

### Guides[​](#guides "Direct link to Guides")

* [Building Walletless Applications Using Child Accounts](/build/guides/account-linking/child-accounts) covers how apps can leverage Account
  Linking to create a seamless user experience and enable future self-custody.
* [Working With Parent Accounts](/build/guides/account-linking/parent-accounts) covers features enabled by the core `HybridCustody` contract to
  access child account assets from parent accounts. This is useful for apps like marketplaces or wallets that are
  working with accounts that have potential child accounts.

### Resources[​](#resources "Direct link to Resources")

* [Forum Post](https://forum.onflow.org/t/hybrid-custody/4016) where core concepts were introduced and discussed.
* [GitHub repository](https://github.com/onflow/hybrid-custody) where `HybridCustody` core contracts and scripts are
  maintained. Check out the repository for more advanced script or transaction examples.
* [Example](https://github.com/jribbink/magic-link-hc-sample/) Account Linking project with
  [Magic](https://magic.link/).
* [Starter template](https://github.com/Niftory/niftory-samples/tree/main/walletless-onboarding) for
  [Niftory](https://niftory.com/) Account Linking API.
[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/account-linking/index.md)Last updated on **Jan 10, 2025** by **Ali Serag**[PreviousCreate an NFT Project](/build/guides/nft)[NextBuilding Walletless Applications Using Child Accounts](/build/guides/account-linking/child-accounts)
###### Rate this page

😞😐😊

* [Accessing Account](#accessing-account)
* [Account Capabilities](#account-capabilities)
  + [Creating Account Links](#creating-account-links)
* [What is account linking most useful for?](#what-is-account-linking-most-useful-for)
* [Security Considerations](#security-considerations)
* [Hybrid Custody and Account Linking](#hybrid-custody-and-account-linking)
  + [Guides](#guides)
  + [Resources](#resources)
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

