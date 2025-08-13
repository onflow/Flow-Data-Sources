# Source: https://cadence-lang.org/docs/language/accounts/inbox

Inbox | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Values and Types](/docs/language/values-and-types/)
  + [Types and Type System](/docs/language/types-and-type-system/)
  + [Operators](/docs/language/operators/)
  + [Accounts](/docs/language/accounts/)

    - [Paths](/docs/language/accounts/paths)
    - [Storage](/docs/language/accounts/storage)
    - [Capabilities](/docs/language/accounts/capabilities)
    - [Keys](/docs/language/accounts/keys)
    - [Contracts](/docs/language/accounts/contracts)
    - [Inbox](/docs/language/accounts/inbox)
  + [Functions](/docs/language/functions)
  + [Pre- and Post-Conditions](/docs/language/pre-and-post-conditions)
  + [Built-in Functions](/docs/language/built-in-functions)
  + [Control Flow](/docs/language/control-flow)
  + [Scope](/docs/language/scope)
  + [Resources](/docs/language/resources)
  + [Access Control](/docs/language/access-control)
  + [Capabilities](/docs/language/capabilities)
  + [Interfaces](/docs/language/interfaces)
  + [Enumerations](/docs/language/enumerations)
  + [References](/docs/language/references)
  + [Imports](/docs/language/imports)
  + [Attachments](/docs/language/attachments)
  + [Contracts](/docs/language/contracts)
  + [Contract Updatability](/docs/language/contract-updatability)
  + [Transactions](/docs/language/transactions)
  + [Events](/docs/language/events)
  + [Core Events](/docs/language/core-events)
  + [Environment Information](/docs/language/environment-information)
  + [Crypto](/docs/language/crypto)
  + [Glossary](/docs/language/glossary)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Language Reference](/docs/language/)
* [Accounts](/docs/language/accounts/)
* Inbox

On this page

# Inbox

Accounts have an inbox, which allows making [capabilities](/docs/language/capabilities) available to specific accounts. The inbox provides a convenient way to *bootstrap* capabilities, which sets up an initial connection between two accounts that the accounts can use to transfer data or perform actions.

An account exposes its inbox through the `inbox` field, which has the type `Account.Inbox`.

## `Account.Inbox`[​](#accountinbox "Direct link to accountinbox")

`` _31

access(all)

_31

struct Inbox {

_31

_31

/// Publishes a new Capability under the given name,

_31

/// to be claimed by the specified recipient.

_31

access(Inbox | PublishInboxCapability)

_31

fun publish(_ value: Capability, name: String, recipient: Address)

_31

_31

/// Unpublishes a Capability previously published by this account.

_31

///

_31

/// Returns `nil` if no Capability is published under the given name.

_31

///

_31

/// Errors if the Capability under that name does not match the provided type.

_31

access(Inbox | UnpublishInboxCapability)

_31

fun unpublish<T: &Any>(_ name: String): Capability<T>?

_31

_31

/// Claims a Capability previously published by the specified provider.

_31

///

_31

/// Returns `nil` if no Capability is published under the given name,

_31

/// or if this account is not its intended recipient.

_31

///

_31

/// Errors if the Capability under that name does not match the provided type.

_31

access(Inbox | ClaimInboxCapability)

_31

fun claim<T: &Any>(_ name: String, provider: Address): Capability<T>?

_31

}

_31

_31

entitlement Inbox

_31

_31

entitlement PublishInboxCapability

_31

entitlement UnpublishInboxCapability

_31

entitlement ClaimInboxCapability ``

## Publishing a capability to the account inbox[​](#publishing-a-capability-to-the-account-inbox "Direct link to Publishing a capability to the account inbox")

An account (the provider) that would like to provide a capability to another account (the recipient) can do so using the `publish` function:

`_10

access(Inbox | PublishInboxCapability)

_10

fun publish(_ value: Capability, name: String, recipient: Address)`

Calling the `publish` function requires access to an account via a reference, which is authorized with the coarse-grained `Inbox` entitlement (`auth(Inbox) &Account`), or the fine-grained `PublishInboxCapability` entitlement (`auth(PublishInboxCapability) &Account`).

The function publishes the specified capability using the provided string as an identifier, to be later claimed by the recipient. Note, however, that until the recipient claims the capability, the provider's account stores it, and the capability contributes towards the provider's account storage usage.

Calling this function emits an event, `InboxValuePublished`, that includes the address of both the provider and the recipient, as well as the name and the type of the published capability. Refer to [Inbox Value Published](/docs/language/core-events#inbox-value-published) for more details on this event.

## Claiming a capability from the account inbox[​](#claiming-a-capability-from-the-account-inbox "Direct link to Claiming a capability from the account inbox")

The intended recipient of a capability can claim a capability from the provider using the `claim` function:

`_10

access(Inbox | ClaimInboxCapability)

_10

fun claim<T: &Any>(_ name: String, provider: Address): Capability<T>?`

Calling the `claim` function requires access to an account via a reference, which is authorized with the coarse-grained `Inbox` entitlement (`auth(Inbox) &Account`), or the fine-grained `ClaimInboxCapability` entitlement (`auth(ClaimInboxCapability) &Account`).

If the provider's inbox has a capability stored under the provided name, the calling recipient is the intended recipient, and it conforms to the provided type argument, then the function removes the capability from the provider's inbox and returns it.

If the provider's inbox has no capability stored under the provided name, or if the calling recipient is not the intended recipient, the function returns `nil`. If the borrow type of the capability is not a subtype of the provided type argument, the program aborts.

tip

It is only possible to claim a capability once.

Calling the `claim` function emits an event, `InboxValueClaimed`, that includes the address of both the provider and the recipient, as well as the name of the claimed capability. Refer to [Inbox Value Claimed](/docs/language/core-events#inbox-value-claimed) for more details on this event.

## Unpublishing a capability from the account inbox[​](#unpublishing-a-capability-from-the-account-inbox "Direct link to Unpublishing a capability from the account inbox")

If the provider no longer wishes to publish a capability for some reason, they can unpublish the capability using the `unpublish` function:

`_10

access(Inbox | UnpublishInboxCapability)

_10

fun unpublish<T: &Any>(_ name: String): Capability<T>?`

Calling the `unpublish` function requires access to an account via a reference, which is authorized with the coarse-grained `Inbox` entitlement (`auth(Inbox) &Account`), or the fine-grained `UnpublishInboxCapability` entitlement (`auth(UnpublishInboxCapability) &Account`).

If the provider's inbox has a capability stored under the provided name, and it conforms to the provided type argument, then the function removes the capability from the inbox and returns it.

If the provider's inbox has no capability stored under the provided name, the function returns `nil`. If the borrow type of the capability is not a subtype of the provided type argument, the program aborts.

Calling the `unpublish` function emits an event, `InboxValueUnpublished`, which includes the address of the provider and the name of the unpublished capability. Refer to [Inbox Value Unpublished](/docs/language/core-events#inbox-value-unpublished) for more details on this event.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/inbox.mdx)

[Previous

Contracts](/docs/language/accounts/contracts)[Next

Functions](/docs/language/functions)

###### Rate this page

😞😐😊

* [`Account.Inbox`](#accountinbox)
* [Publishing a capability to the account inbox](#publishing-a-capability-to-the-account-inbox)
* [Claiming a capability from the account inbox](#claiming-a-capability-from-the-account-inbox)
* [Unpublishing a capability from the account inbox](#unpublishing-a-capability-from-the-account-inbox)