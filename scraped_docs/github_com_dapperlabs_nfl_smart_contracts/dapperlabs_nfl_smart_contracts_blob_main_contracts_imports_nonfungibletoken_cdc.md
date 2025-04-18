# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/contracts/imports/NonFungibleToken.cdc

```
/**

## The Flow Non-Fungible Token standard

## `NonFungibleToken` contract

The interface that all Non-Fungible Token contracts should conform to.
If a user wants to deploy a new NFT contract, their contract should implement
The types defined here

## `NFT` resource interface

The core resource type that represents an NFT in the smart contract.

## `Collection` Resource interface

The resource that stores a user's NFT collection.
It includes a few functions to allow the owner to easily
move tokens in and out of the collection.

## `Provider` and `Receiver` resource interfaces

These interfaces declare functions with some pre and post conditions
that require the Collection to follow certain naming and behavior standards.

They are separate because it gives developers the ability to define functions
that can use any type that implements these interfaces

By using resources and interfaces, users of NFT smart contracts can send
and receive tokens peer-to-peer, without having to interact with a central ledger
smart contract.

To send an NFT to another user, a user would simply withdraw the NFT
from their Collection, then call the deposit function on another user's
Collection to complete the transfer.

*/

import "ViewResolver"

/// The main NFT contract. Other NFT contracts will
/// import and implement the interfaces defined in this contract
///
access(all) contract interface NonFungibleToken: ViewResolver {

    /// An entitlement for allowing the withdrawal of tokens from a Vault
    access(all) entitlement Withdraw

    /// An entitlement for allowing updates and update events for an NFT
    access(all) entitlement Update

    /// entitlement for owner that grants Withdraw and Update
    access(all) entitlement Owner

    /// Event that contracts should emit when the metadata of an NFT is updated
    /// It can only be emitted by calling the `emitNFTUpdated` function
    /// with an `Updatable` entitled reference to the NFT that was updated
    /// The entitlement prevents spammers from calling this from other users' collections
    /// because only code within a collection or that has special entitled access
    /// to the collections methods will be able to get the entitled reference
    ///
    /// The event makes it so that third-party indexers can monitor the events
    /// and query the updated metadata from the owners' collections.
    ///
    access(all) event Updated(type: String, id: UInt64, uuid: UInt64, owner: Address?)
    access(contract) view fun emitNFTUpdated(_ nftRef: auth(Update | Owner) &{NonFungibleToken.NFT})
    {
        emit Updated(type: nftRef.getType().identifier, id: nftRef.id, uuid: nftRef.uuid, owner: nftRef.owner?.address)
    }


    /// Event that is emitted when a token is withdrawn,
    /// indicating the type, id, uuid, the owner of the collection that it was withdrawn from,
    /// and the UUID of the resource it was withdrawn from, usually a collection.
    ///
    /// If the collection is not in an account's storage, `from` will be `nil`.
    ///
    access(all) event Withdrawn(type: String, id: UInt64, uuid: UInt64, from: Address?, providerUUID: UInt64)

    /// Event that emitted when a token is deposited to a collection.
    /// Indicates the type, id, uuid, the owner of the collection that it was deposited to,
    /// and the UUID of the collection it was deposited to
    ///
    /// If the collection is not in an account's storage, `from`, will be `nil`.
    ///
    access(all) event Deposited(type: String, id: UInt64, uuid: UInt64, to: Address?, collectionUUID: UInt64)

    /// Included for backwards-compatibility
    access(all) resource interface INFT: NFT {}

    /// Interface that the NFTs must conform to
    ///
    access(all) resource interface NFT: ViewResolver.Resolver {

        /// unique ID for the NFT
        access(all) let id: UInt64

        /// Event that is emitted automatically every time a resource is destroyed
        /// The type information is included in the metadata event so it is not needed as an argument
        access(all) event ResourceDestroyed(id: UInt64 = self.id, uuid: UInt64 = self.uuid)

        /// createEmptyCollection creates an empty Collection that is able to store the NFT
        /// and returns it to the caller so that they can own NFTs
        /// @return A an empty collection that can store this NFT
        access(all) fun createEmptyCollection(): @{Collection} {
            post {
                result.getLength() == 0: "The created collection must be empty!"
            }
        }

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

    /// Interface to mediate withdrawals from a resource, usually a Collection
    ///
    access(all) resource interface Provider {

        // We emit withdraw events from the provider interface because conficting withdraw
        // events aren't as confusing to event listeners as conflicting deposit events

        /// withdraw removes an NFT from the collection and moves it to the caller
        /// It does not specify whether the ID is UUID or not
        /// @param withdrawID: The id of the NFT to withdraw from the collection
        access(Withdraw | Owner) fun withdraw(withdrawID: UInt64): @{NFT} {
            post {
                result.id == withdrawID: "The ID of the withdrawn token must be the same as the requested ID"
                emit Withdrawn(type: result.getType().identifier, id: result.id, uuid: result.uuid, from: self.owner?.address, providerUUID: self.uuid)
            }
        }
    }

    /// Interface to mediate deposits to the Collection
    ///
    access(all) resource interface Receiver {

        /// deposit takes an NFT as an argument and adds it to the Collection
        /// @param token: The NFT to deposit
        access(all) fun deposit(token: @{NFT})

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

    /// Kept for backwards-compatibility reasons
    access(all) resource interface CollectionPublic {
        access(all) fun deposit(token: @{NFT})
        access(all) view fun getLength(): Int
        access(all) view fun getIDs(): [UInt64]
        access(all) view fun borrowNFT(_ id: UInt64): &{NFT}?
    }

    /// Requirement for the concrete resource type
    /// to be declared in the implementing contract
    ///
    access(all) resource interface Collection: Provider, Receiver, CollectionPublic, ViewResolver.ResolverCollection {

        /// deposit takes a NFT as an argument and stores it in the collection
        /// @param token: The NFT to deposit into the collection
        access(all) fun deposit(token: @{NonFungibleToken.NFT}) {
            pre {
                // We emit the deposit event in the `Collection` interface
                // because the `Collection` interface is almost always the final destination
                // of tokens and deposit emissions from custom receivers could be confusing
                // and hard to reconcile to event listeners
                emit Deposited(type: token.getType().identifier, id: token.id, uuid: token.uuid, to: self.owner?.address, collectionUUID: self.uuid)
            }
        }

        /// Gets the amount of NFTs stored in the collection
        /// @return An integer indicating the size of the collection
        access(all) view fun getLength(): Int

        /// Borrows a reference to an NFT stored in the collection
        /// If the NFT with the specified ID is not in the collection,
        /// the function should return `nil` and not panic.
        ///
        /// @param id: The desired nft id in the collection to return a referece for.
        /// @return An optional reference to the NFT
        access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
            post {
                (result == nil) || (result?.id == id):
                    "Cannot borrow NFT reference: The ID of the returned reference does not match the ID that was specified"
            }
        }

        /// createEmptyCollection creates an empty Collection of the same type
        /// and returns it to the caller
        /// @return A an empty collection of the same type
        access(all) fun createEmptyCollection(): @{Collection} {
            post {
                result.getType() == self.getType(): "The created collection does not have the same type as this collection"
                result.getLength() == 0: "The created collection must be empty!"
            }
        }
    }

    /// createEmptyCollection creates an empty Collection for the specified NFT type
    /// and returns it to the caller so that they can own NFTs
    /// @param nftType: The desired nft type to return a collection for.
    /// @return An array of NFT Types that the implementing contract defines.
    access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {
        post {
            result.getIDs().length == 0: "The created collection must be empty!"
        }
    }
}
```