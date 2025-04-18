# Source: https://github.com/onflow/flips/blob/main/application/20221219-nft-v2.md

---
status: Implemented 
flip: 56
authors: Joshua Hannan (joshua.hannan@flowfoundation.org)
sponsor: Joshua Hannan (joshua.hannan@flowfoundation.org) 
updated: 2024-03-11 
---

# Non-Fungible Token Standard V2

## Objective

This FLIP proposes multiple updates to the Flow Non-Fungible Token
Standard contracts as part of the Cadence 1.0 upgrade,
primarily about adding support for defining multiple token types
in one contract, adding standard events, integrating `ViewResolver`,
adding support for updating NFTs, adding support for sub-NFTs, and adding entitlements

Some of these changes are dependent on other Cadence FLIPs that
made fundamental changes to the language
that have been approved and implemented,
primarily [interface inheritance](https://github.com/onflow/flips/pull/40),
removal of nested type requirements,
[removal of custom destructors](https://github.com/onflow/flips/blob/main/cadence/20230811-destructor-removal.md),
and [allowing interfaces to emit events](https://github.com/onflow/cadence/issues/2069).

The changes proposed here will be breaking for all non-fungible token implementations
on the Flow blockchain, as well as contracts that utilize tokens based on the standard,
third-party integrations such as event listeners, and apps that interface with the contracts.

## Motivation

The current non-fungible token standard for Flow
was designed in mid 2019, at a time when Cadence itself was still being designed.
The current standard, though functional, leaves much to be desired.

The current token standard uses contract interfaces and nested type requirements.
They are designed in a way that requires each concrete contract
to provide exactly one `NFT` and one `Collection` type.
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
* Have standard events emitted correctly for important operations (`Withdrawn`, `Deposited`, `Updated`, and `NonFungibleToken.NFT.ResourceDestroyed`).
* Support querying information about NFTs that an NFT directly owns.
* Check if a `Receiver` accepts a given token type.

## Design Proposal

[The original proposal](https://forum.onflow.org/t/streamlined-token-standards-proposal/3075/1)
is on the Flow Forum.
A [pull request with the suggested code changes](https://github.com/onflow/flow-nft/pull/126) 
is in the flow fungible token github repository.

The main code changes and their implications are described here.
The linked proposals provide more context, though the proposal in the forum post
is quite out of date.

### Add support for multiple token types in a single contract

Now that nested type requirements have been removed, contracts can define
multiple token types. The type information can be accessed by using the built-in
`contract.publicTypes(): [Type]` method. A return value of this is now required
in the `NonFungibleToken.createEmptyCollection(nftType: Type)` method because
the caller needs to specify which type they are looking for.

`ViewResolver` has also been updated to require type information
when querying views from a contract:

```cadence
access(all) contract interface ViewResolver {

    /// Function that returns all the Metadata Views implemented by the resolving contract.
    /// Some contracts may have multiple resource types that support metadata views
    /// so there is an optional parameter for specify which resource type the caller
    /// is looking for views for.
    /// Some contract-level views may be type-agnostic. In that case, the contract
    /// should return the same views regardless of what type is passed in.
    ///
    /// @param resourceType: An optional resource type to return views for
    /// @return An array of Types defining the implemented views. This value will be used by
    ///         developers to know which parameter to pass to the resolveView() method.
    ///
    access(all) view fun getContractViews(resourceType: Type?): [Type]

    /// Function that resolves a metadata view for this token.
    /// Some contracts may have multiple resource types that support metadata views
    /// so there there is an optional parameter to specify which resource type the caller
    /// is requesting views for.
    /// Some contract-level views may be type-agnostic. In that case, the contract
    /// should return the same views regardless of what type is passed in.
    ///
    /// @param resourceType: An optional resource type to return views for
    /// @param view: The Type of the desired view.
    /// @return A structure representing the requested view.
    ///
    access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct?
}
```

While all contracts that implement the `NonFungibleToken` standard
will need to implement these functions, many of them will still
only have a single token type in their contract.
Therefore, they can ignore the `resourceType` parameter.

In addition to these changes to `ViewResolver`, the `MetadataViews.Resolver`
resource interface has been moved to the `ViewResolver` contract because
this is the logical place for it to live and it also avoids a circular dependency.

### Move Event Definitions and emissions to resource interfaces

Instead of requiring events to be defined in the token implementations contracts,
they will only be [defined in the non-fungible token standard smart contract](https://github.com/onflow/flow-nft/blob/standard-v2/contracts/NonFungibleToken.cdc#L86) and will
be [emitted in post-conditions](https://github.com/onflow/flow-nft/blob/standard-v2/contracts/NonFungibleToken.cdc#L185)
from the correct methods in the resource interfaces defined in the standard.

### Add Type and Metadata parameters to events

Standard events contain more information about the NFT that is being transferred,
such as the type of the NFT and important metadata about the transfer.
This includes UUIDs of the collections involved in the token movements
in case this information is useful.

Here is an example of the proposal:

```cadence
/// The event that is emitted when tokens are withdrawn from a Vault
access(all) event Withdrawn(type: String, amount: UFix64, from: Address?, fromUUID: UInt64, withdrawnUUID: UInt64)
```

### Add `getAcceptedTypes()` method to `Receiver` interface

It is useful to be able to query a non-fungible token receiver to see what types of tokens
it can accept.

```cadence
access(all) resource interface Receiver {
    /// getSupportedNFTTypes returns a list of NFT types that this receiver accepts
    /// @return A dictionary of types mapped to booleans indicating if this
    ///         reciever supports it
    access(all) view fun getSupportedNFTTypes(): {Type: Bool}

    /// Returns whether or not the given type is accepted by the collection
    /// A collection that can accept any type should just return true by default
    /// @param type: An NFT type
    /// @return A boolean indicating if this receiver can recieve the desired NFT type
    access(all) view fun isSupportedNFTType(type: Type): Bool
}
```

### Change the return type of `borrowNFT()` to an optional

In the current standard, `borrowNFT()` is meant to panic if the NFT to borrow
is not found in the collection. This is clearly the wrong choice, because 
it is a best practice to have getter functions return `nil` if something goes wrong
instead of panicking and reverting the transaction.

```cadence
access(all) view fun borrowNFT(_ id: UInt64): &{NFT}?
```

### Remove the requirement for the `ownedNFTs` field in `Collection`

The requirement to include an `ownedNFTs: {UInt64: @NFT}` field
in Collection implementations is restrictive because developers may want
to store tokens in a unique way that is different what what could be specified.
This proposal removes `ownedNFTs` and only requires a `getIDs()` method
for the collection to indicate which IDs it contains.

### Move `createEmptyCollection()` to inside the NFT and Collection definitions in addition to the contract

It is useful to be able to create a new empty collection
directly from an `NFT` or a `Collection` object instead of having to import
the contract and call the method from the contract.

```cadence
access(all) resource interface Collection {

    /// createEmptyCollection creates an empty Collection
    /// and returns it to the caller so that they can own NFTs
    access(all) fun createEmptyCollection(): @{Collection} {
        post {
            result.getType() == self.getType(): "The created collection does not have the same type as this collection"
            result.getLength() == 0: "The created collection must be empty!"
        }
    }
}
```

### Add Metadata Views methods to the standard

Metadata Views for non-fungible tokens should be easily accessible
from interfaces defined by the standard. 
This proposal enforces that implementations implement the `ViewResolver` contract interface,
`NFT` implementations implement the `ViewResolver.Resolver` interface,
and `Collection` implementations implement the `ViewResolver.ResolverCollection` interface.

### Add support for getting information about Sub-NFTs

A powerful feature of Cadence is that resources can own other resources.
Many `NonFungibleToken` implementations make it possible for their NFTs to own other
NFTs. The standard is being updated to support
[querying information about these sub-NFTs](https://github.com/onflow/flow-nft/blob/standard-v2/contracts/NonFungibleToken.cdc#L113-L129).

It is not required though, so default implementations
that return empty values are provided.

```cadence
access(all) resource interface NFT {
        /// Gets all the NFTs that this NFT directly owns
        /// @return A dictionary of all subNFTS keyed by type
        access(all) view fun getAvailableSubNFTS(): {Type: UInt64} {
            return {}
        }

        /// Get a reference to an NFT that this NFT owns
        /// Both arguments are optional to allow the NFT to choose
        /// how it returns sub NFTs depending on what arguments are provided
        /// For example, if `type` has a value, but `id` doesn't, the NFT 
        /// can choose which NFT of that type to return if there is a "default"
        /// If both are `nil`, then NFTs that only store a single NFT can just return
        /// that. This helps callers who aren't sure what they are looking for 
        ///
        /// @param type: The Type of the desired NFT
        /// @param id: The id of the NFT to borrow
        ///
        /// @return A structure representing the requested view.
        access(all) fun getSubNFT(type: Type, id: UInt64) : &{NonFungibleToken.NFT}? {
            return nil
        }
}
```

### Add support for emitting an event when an NFT is updated

Many projects support updating metadata or stored fields for their NFTs.
It is important that these projects have a standard way to indicate
that an NFT has been updated. The standard defines an
[`Update` event](https://github.com/onflow/flow-nft/blob/standard-v2/contracts/NonFungibleToken.cdc#L65)
that any project can access to say that an NFT is updated:
```cadence
access(all) event Updated(type: String, id: UInt64, uuid: UInt64, owner: Address?)
access(contract) view fun emitNFTUpdated(_ nftRef: auth(Update | Owner) &{NonFungibleToken.NFT})
{
    emit Updated(type: nftRef.getType().identifier, id: nftRef.id, uuid: nftRef.uuid, owner: nftRef.owner?.address)
}
```

The `emitNFTUpdated` event is used to emit the event and can only be called
with an `Update` or `Owner`-entitled reference to the NFT that has been updated.

Projects should NOT override the default implementation of `emitNFTUpdated()`
or they will lose access to the standard event.

They still will call it using the name of their contract though.
So if Top Shot were to want to emit the event, the syntax would look like this:
```cadence
TopShot.emitNFTUpdated(nftReference)
```

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
2. Make `NonFungibleToken` a contract instead of an interface:
    * This would allow the contract to have utility methods to have more fine-grained control
      over how standard events are emitted, but would not allow the standard
      to enforce that implementations use the `ViewResolver` interface
      and have the `createEmptyCollection(vaultType: Type)` function.

### Performance Implications

Most of the methods in the non-fungible token interface are expected to be O(1),
so there is no performance requirements to enforce with the methods.
That is mostly up to the developers who are implementing the tokens to ensure.

The `getIDs()` method can sometimes return a list that is too large for
the transaction or script to handle. We'd like to have some sort of method
that returns a paginated list of IDs instead of the whole list.
Any proposals for that would be appreciated,
but it will likely require a Cadence language update.

### Dependencies

* Adds no new dependencies
* Dependent projects
    * All non-fungible tokens on Flow and some projects that utilize them.

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

* The upgrade will go out at the same time as stable cadence if approved

## Related Issues

### Scoped Providers

A critical piece of tooling for non-fungible tokens would be a struct that contains
a provider capability but restricts the capability to only be able to withdraw
specified IDs or number of tokens from the underlying collection.
Currently, providers have no limit, but all tokens should be able
to create scoped providers.

This feature is out of the scope of this proposal, but should definitely be a standard
that lives alongside the main fungible token standard.
We hope to shepherd a proposal for these soon.

### Universal Collection

Each NFT implementor also needs to implement their own Collection resource.
The Collection implementation of the Example NFT contract is 5x as long as the NFT implementation itself. Almost all collection code is copied, so it could be
very nice to have a universal collection that can hold any type of NFT.

There is a universal collection implementation in the branch where the new standard is,
but that will be discussed an another place.

## Prior Art

In combination with the upgrades to the FT standard, we'd like for users to
be able to utilize more sophisticated functionality in their tokens, such as
what was enabled with an upgrade like ERC-1155 and other such upgrades in Ethereum.
We would greatly appreciate if any developers with ethereum experience could think
about these upgrades from the perspective of being able to create the same kinds 
of projects that are possible with other token standards in other languages.