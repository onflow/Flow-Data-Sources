# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/nft/NFTMetadata.cdc

```
import "NonFungibleToken"
import "MetadataViews"

access(all) contract NFTMetadata {
    access(all) entitlement Owner

    access(all) event MetadataFrozen(uuid: UInt64, owner: Address?)

    access(all) struct CollectionInfo {
        access(all) var collectionDisplay: MetadataViews.NFTCollectionDisplay

        access(all) let data: {String: AnyStruct}

        access(all) fun getDisplay(): MetadataViews.NFTCollectionDisplay {
            return self.collectionDisplay
        }

        init(collectionDisplay: MetadataViews.NFTCollectionDisplay) {
            self.collectionDisplay = collectionDisplay

            self.data = {}
        }
    }

    access(all) struct Metadata {
        // these are used to create the display metadata view so that we can concatenate
        // the id onto it.
        access(all) let name: String
        access(all) let description: String
        access(all) let thumbnail: {MetadataViews.File}

        access(all) let traits: MetadataViews.Traits?
        access(all) let editions: MetadataViews.Editions?
        access(all) let externalURL: MetadataViews.ExternalURL?
        access(all) let royalties: MetadataViews.Royalties?

        access(all) let data: {String: AnyStruct}

        access(all) fun getThumbnail(): {MetadataViews.File} {
            return self.thumbnail
        }

        access(all) fun getTraits(): MetadataViews.Traits? {
            return self.traits
        }

        access(all) fun getEditions(): MetadataViews.Editions? {
            return self.editions
        }

        access(all) fun getExternalURL(): MetadataViews.ExternalURL? {
            return self.externalURL
        }

        access(all) fun getRoyalties(): MetadataViews.Royalties? {
            return self.royalties
        }

        init(
            name: String,
            description: String,
            thumbnail: {MetadataViews.File},
            traits: MetadataViews.Traits?,
            editions: MetadataViews.Editions?,
            externalURL: MetadataViews.ExternalURL?,
            royalties: MetadataViews.Royalties?,
            data: {String: AnyStruct}
        ) {
            self.name = name
            self.description = description
            self.thumbnail = thumbnail

            self.traits = traits
            self.editions = editions
            self.externalURL = externalURL
            self.royalties = royalties

            self.data = {}
        }
    }

    access(all) resource Container {
        access(all) var collectionInfo: CollectionInfo
        access(all) let metadata: {UInt64: Metadata}
        access(all) var frozen: Bool

        access(all) let data: {String: AnyStruct}
        access(all) let resources: @{String: AnyResource}

        access(all) fun borrowMetadata(id: UInt64): &Metadata? {
            return &self.metadata[id]
        }

        access(Owner) fun addMetadata(id: UInt64, data: Metadata) {
            pre {
                self.metadata[id] == nil: "id already has metadata assigned"
                !self.frozen: "metadata is frozen and cannot be updated"
            }

            self.metadata[id] = data
        }

        access(Owner) fun freeze() {
            self.frozen = true
            emit MetadataFrozen(uuid: self.uuid, owner: self.owner?.address)
        }

        init(collectionInfo: CollectionInfo) {
            self.collectionInfo = collectionInfo
            self.metadata = {}
            self.frozen = false

            self.data = {}
            self.resources <- {}
        }
    }

    access(all) struct InitializedCaps {
        access(all) let pubCap: Capability<&Container>
        access(all) let ownerCap: Capability<auth(Owner) &Container>

        access(all) let data: {String: AnyStruct}

        init(pubCap: Capability<&Container>, ownerCap: Capability<auth(Owner) &Container>) {
            self.pubCap = pubCap
            self.ownerCap = ownerCap

            self.data = {}
        }
    }

    access(all) fun createContainer(collectionInfo: CollectionInfo): @Container {
        return <- create Container(collectionInfo: collectionInfo)
    }

    access(all) fun initialize(acct: auth(Storage, Capabilities) &Account, collectionInfo: CollectionInfo, nftType: Type): InitializedCaps {
        let storagePath = self.getCollectionStoragePath(type: nftType)
        let container <- self.createContainer(collectionInfo: collectionInfo)
        acct.storage.save(<-container, to: storagePath)
        let pubCap = acct.capabilities.storage.issue<&Container>(storagePath)
        let ownerCap = acct.capabilities.storage.issue<auth(Owner) &Container>(storagePath)
        return InitializedCaps(pubCap: pubCap, ownerCap: ownerCap)
    }

    access(all) struct UriFile: MetadataViews.File {
        access(self) let url: String

        access(all) view fun uri(): String {
            return self.url
        }

        init(_ url: String) {
            self.url = url
        }
    }

    access(all) fun getCollectionStoragePath(type: Type): StoragePath {
        let segments = type.identifier.split(separator: ".")
        return StoragePath(identifier: "NFTMetadataContainer_".concat(segments[2]).concat("_").concat(segments[1]))!
    }
}
```