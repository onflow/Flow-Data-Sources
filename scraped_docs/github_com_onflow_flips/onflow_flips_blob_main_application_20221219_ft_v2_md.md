# Source: https://github.com/onflow/flips/blob/main/application/20221219-ft-v2.md

---
status: Implemented 
flip: 55
authors: Joshua Hannan (joshua.hannan@flowfoundation.org)
sponsor: Joshua Hannan (joshua.hannan@flowfoundation.org) 
updated: 2024-03-11 
---

# Fungible Token Standard V2

## Objective

This FLIP proposes multiple updates to the Flow Fungible Token
Standard contracts as part of the Cadence 1.0 upgrade,
primarily about adding support for defining multiple token types
in one contract, adding standard events, integrating `ViewResolver`
and adding the `Burner` utility smart contract.

Some of these changes are dependent on other Cadence FLIPs that
made fundamental changes to the language
that have been approved and implemented,
primarily [interface inheritance](https://github.com/onflow/flips/pull/40),
removal of nested type requirements,
[removal of custom destructors](https://github.com/onflow/flips/blob/main/cadence/20230811-destructor-removal.md),
and [allowing interfaces to emit events](https://github.com/onflow/cadence/issues/2069).

The changes proposed here will be breaking for all fungible token implementations
on the Flow blockchain, as well as contracts that utilize tokens based on the standard,
third-party integrations such as event listeners, and apps that interface with the contracts.

## Motivation

The current fungible token standard for Flow
was designed in mid 2019, at a time when Cadence itself was still being designed.
The current standard, though functional, leaves much to be desired.

The current token standard uses contract interfaces and nested type requirements.
They are designed in a way that requires each concrete contract
to provide exactly one Vault type.
This means that any project that needs multiple tokens must deploy multiple contracts.
In the case of very simple tokens, this is a lot of complexity for very little value.

Related to this problem, functionality and metadata associated with some tokens,
such as paths and empty vault creation methods
is only accessible directly through the contract itself, when it should also
be accessible directly through an instance of a token resource and/or interface.

Many contracts also do not implement MetadataViews properly because
there is no requirement for it in the standard.

In the case of events, currently there is no way for the standard to ensure that
implementations are emitting standardized and correct events, which this upgrade will address.

## User Benefit

With these upgrades, users will now be able to:
* Define multiple tokens in a single contract.
* Query all the data about a token directly through the contract as well as the `Vault` resource and core interfaces.
* Have standard events emitted correctly for important operations (`Withdrawn`, `Deposited`, and `Burned`)
* Define a `burnCallback()` method that effectively serves as a custom destructor if used in conjunction with the `Burner` contract.

## Design Proposal

[The original proposal](https://forum.onflow.org/t/streamlined-token-standards-proposal/3075/1)
is on the Flow Forum.
A [pull request with the suggested code changes](https://github.com/onflow/flow-ft/pull/77) 
is in the flow fungible token github repository.

The main code changes and their implications are described here.
The linked proposals provide more context, but the original forum post is somewhat out of date.

### Move Event Definitions and emissions to resource interfaces

Instead of requiring events to be defined in the token implementations contracts,
they will only be [defined in the fungible token standard smart contract](https://github.com/onflow/flow-ft/blob/v2-standard/contracts/FungibleToken.cdc#L50) and will
be [emitted in post-conditions](https://github.com/onflow/flow-ft/blob/v2-standard/contracts/FungibleToken.cdc#L100)
from the correct methods in the resource interfaces defined in the standard.

Ex:

```cadence
access(all) contract interface FungibleToken {
    /// The event that is emitted when tokens are withdrawn from a Vault
    access(all) event Withdrawn(type: String, amount: UFix64, from: Address?, fromUUID: UInt64, withdrawnUUID: UInt64)

    access(all) resource interface Provider {
        access(Withdraw) fun withdraw(amount: UFix64): @{Vault} {
            post {
                // Emit directly in the interface instead of the implementation
                emit Withdrawn(type: self.getType().identifier, amount: amount, from: self.owner?.address, fromUUID: self.uuid, withdrawnUUID: result.uuid)
            }
        }
    }
}
```

This means that the `FungibleToken` events will be the source of truth from now on,
though their types will still contain the name of the implementing contract
when they are emitted, such as:

```cadence
A.0x1654653399040a61.FlowToken.Withdrawn
```

Therefore, all Fungible Token implementations can and probably should remove their
own `TokensWithdrawn` and `TokensDeposited` events, as they are now redundant.


### Add Type, Metadata, and UUID parameters to events

Standard events contain more information about the FT that is being transferred,
such as the type of the FT and important metadata about the FT.
This includes UUIDs of the vaults involved in the token movements
in case this information is useful.

Here is an example of the proposal:

```cadence
/// The event that is emitted when tokens are withdrawn from a Vault
access(all) event Withdrawn(type: String, amount: UFix64, from: Address?, fromUUID: UInt64, withdrawnUUID: UInt64)
```

### Add `getAcceptedTypes()` method to `Receiver` interface

It is useful to be able to query a fungible token receiver to see what types of tokens
it can accept.

```cadence
    pub resource interface Receiver {

        /// getSupportedVaultTypes optionally returns a list of vault types that this receiver accepts
        access(all) view fun getSupportedVaultTypes(): {Type: Bool}

        /// Returns whether or not the given type is accepted by the Receiver
        /// A vault that can accept any type should just return true by default
        access(all) view fun isSupportedVaultType(type: Type): Bool
    }
```

### Add a requirement for a `isAvailableToWithdraw(): Bool` function in `Vault`

Vaults need a way to be able to say if a requested amount of tokens can be withdrawn.
Instead of checking the balance first or risking a panic on a failed withdrawal,
code can call `isAvailableToWithdraw()` to check first to be safe.

This is especially useful in Fungible Token provider implementations
that have the ability to withdraw from multiple different vaults
because it does not necessarily need to iterate through all the vaults 
before finding out if the balance is withdrawable. 

### Add `createEmptyVault()` inside the Vault definition in addition to the contract

It is useful to be able to create a new empty vault directly from a Vault object
instead of having to import the contract and call the method from the contract.

```cadence
pub resource interface Vault {

    /// createEmptyVault allows any user to create a new Vault that has a zero balance
    ///
    pub fun createEmptyVault(): @AnyResource{Vault} {
        post {
            result.getBalance() == 0.0: "The newly created Vault must have zero balance"
        }
    }
}
```

### Add Metadata Views methods to the standard

Metadata Views for fungible tokens should be easily accessible
from interfaces defined by the standard. This proposal enforces
all FungibleToken implementations to also implement `ViewResolver`
and for all Fungible Tokens to implement `ViewResolver.Resolver`.

This way, standard metadata views methods are enforced by default.

### Drawbacks

The main drawback of this upgrade is the breaking changes.
It could cause downtime for some projects who aren't prepared to perform the upgrade
right after stable cadence is enabled,
but that applies to any breaking change in stable cadence.
The updates that developers will have to do are fairly straightforward
and will not require much work.

Please share any other drawbacks that you may discover with these changes.

### Alternatives Considered

1. Keep the standard the same:
    * If nested type requirements are removed, this may not be possible
    * This would avoid the breaking changes, which would be nice in the short term, but would not be setting up cadence developers for success in the long term.
2. Make `FungibleToken` a contract instead of an interface:
    * This would allow the contract to have utility methods to have more fine-grained control
      over how standard events are emitted, but would not allow the standard
      to enforce that implementations use the `ViewResolver` interface
      and have the `createEmptyVault(vaultType: Type)` function.

### Performance Implications

All of the methods in the fungible token interface are expected to be O(1),
so there is no performance requirements to enforce with the methods.

### Dependencies

* Adds the `Burner` contract.
  * Contracts won't have to import the `Burner` contract
    directly because the conformance is handled by
    `FungibleToken.Vault`, so it isn't a direct dependency,
    but important to be aware of
* Dependent projects
    * All fungible tokens on Flow and some projects that utilize them,
    including but not limited to:
        * flow-ft
        * flow-core-contracts
        * NFT Storefront
        * kitty items
        * usdc, fusd, blocto token, incrementfi, duc, etc....

### Engineering Impact

* Build and test time will stay the same. they are relatively small changes.
* The Flow smart contract engineering team will maintain the code
* The code can be tested on its own once a compatible version of cadence is released. 

### Best Practices

* Some of the changes illustrate Cadence best practices, such as encapsulating functionality
within resources, avoiding public fields, and giving developers flexibility to write composable code.

### Tutorials and Examples

* Check out the Cadence 1.0 migration guide for instructions on how to update contracts to the new standards:
  * https://cadence-lang.org/docs/cadence_migration_guide/

### Compatibility

* FCL, emulator, and other such tools should not be affected besides potentially
having to update standard transactions if they aren't compatible.

### User Impact

* The upgrade will go out at the same time as Cadence 1.0 (Crescendo) if approved.

## Related Issues

### Scoped Providers

A critical piece of tooling for fungible tokens would be a struct that contains
a provider capability but restricts the capability to only be able to withdraw
a specified amount of tokens from the underlying vault.
Currently, providers have no limit, but all tokens should be able
to create scoped providers.

This feature is out of the scope of this proposal, but should definitely be a standard
that lives alongside the main fungible token standard.
We hope to shepherd a proposal for these soon.

## Prior Art

In combination with the upgrades to the NFT standard, we'd like for users to
be able to utilize more sophisticated functionality in their tokens, such as
what was enabled with an upgrade like ERC-1155 and other such upgrades in Ethereum.
We would greatly appreciate if any developers with ethereum experience could think
about these upgrades from the perspective of being able to create the same kinds 
of projects that are possible with other token standards in other languages.