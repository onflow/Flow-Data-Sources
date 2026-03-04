# Source: https://github.com/austinkline/jimbo/blob/main/contracts/PuffPalz.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "ViewResolver"

access(all) contract PuffPalz: NonFungibleToken {

    access(all) entitlement Owner

	//Define Events
	access(all) event ContractInitialized()
	access(all) event Withdraw(id: UInt64, from: Address?)
	access(all) event Deposit(id: UInt64, to: Address?)
	access(all) event ExclusiveMinted(id: UInt64, name: String, description: String, image: String, traits: {String:String})

	//Define Paths
	access(all) let CollectionStoragePath: StoragePath
	access(all) let CollectionPublicPath: PublicPath
	access(all) let CollectionPrivatePath: PrivatePath
	access(all) let AdminStoragePath: StoragePath

	//Difine Total Supply
	access(all) var totalSupply: UInt64

	access(all) struct puffPalzMetadata {
		access(all) let id: UInt64
		access(all) let name: String
		access(all) let description: String
		access(all) let image: String
		access(all) let traits: {String:String}

		init(_id: UInt64, _name: String, _description: String, _image: String, _traits:{String:String}) {
			self.id = _id
			self.name = _name
			self.description = _description
			self.image = _image
			self.traits = _traits
		}
	}

	access(all) resource NFT: NonFungibleToken.NFT {
		access(all) let id: UInt64
		access(all) let name: String
		access(all) let description: String
		access(all) var image: String
		access(all) let traits: {String: String}

		init( _id: UInt64, _name: String, _description: String, _image: String, _traits: {String:String}) {

			self.id = _id
			self.name = _name
			self.description = _description
			self.image = _image
			self.traits = _traits
		}

		access(Owner) fun revealThumbnail() {
            let urlBase = self.image.slice(from: 0, upTo: 47)
            let newImage = urlBase.concat(self.id.toString()).concat(".png")
            self.image = newImage
        }

		access(all) view fun getViews(): [Type] {
			return [
				Type<MetadataViews.NFTView>(),
				Type<MetadataViews.Display>(),
				Type<MetadataViews.ExternalURL>(),
				Type<MetadataViews.NFTCollectionData>(),
				Type<MetadataViews.NFTCollectionDisplay>(),
				Type<PuffPalz.puffPalzMetadata>(),
                Type<MetadataViews.Royalties>(),
				Type<MetadataViews.Traits>()
			]
		}

		access(all) fun resolveView(_ view: Type): AnyStruct? {
			switch view {
				case Type<MetadataViews.Display>():
					return MetadataViews.Display(
                        name: self.name,
                        description: self.description,
                        thumbnail: MetadataViews.IPFSFile(
                            cid: self.image,
                            path: nil
                        )
                    )
                case Type<MetadataViews.ExternalURL>():
         			return MetadataViews.ExternalURL("https://puffpalz.io/")
				case Type<PuffPalz.puffPalzMetadata>():
					return PuffPalz.puffPalzMetadata(
						_id: self.id,
						_name: self.name,
						_description: self.description,
						_image: self.image,
						_traits: self.traits
					)
                case Type<MetadataViews.NFTView>():
                    let viewResolver = &self as &{ViewResolver.Resolver}
                        return MetadataViews.NFTView(
                            id: self.id,
                            uuid: self.uuid,
                            display: MetadataViews.getDisplay(viewResolver),
                            externalURL: MetadataViews.getExternalURL(viewResolver),
                            collectionData: MetadataViews.getNFTCollectionData(viewResolver),
                            collectionDisplay: MetadataViews.getNFTCollectionDisplay(viewResolver),
                            royalties: MetadataViews.getRoyalties(viewResolver),
                            traits: MetadataViews.getTraits(viewResolver)
                        )
                case Type<MetadataViews.Royalties>():
                    return MetadataViews.Royalties([
						MetadataViews.Royalty(
							receiver: getAccount(0xc4b1f4387748f389).capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver),
							cut: 0.01,
							description: "1% Royalty for artist"
						),
						MetadataViews.Royalty(
							receiver: getAccount(0x66b60643244a7738).capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver),
							cut: 0.01,
							description: "1% Royalty for dev"
						),
						MetadataViews.Royalty(
							receiver: getAccount(0xded455fa967d350e).capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver),
							cut: 0.03,
							description: "3% Royalty for treasury"
						)
					])

				case Type<MetadataViews.Traits>():
					let traits: [MetadataViews.Trait] = []
                    for trait in self.traits.keys {
                        traits.append(MetadataViews.Trait(
                            name: trait,
                            value: self.traits[trait]!,
                            displayType: nil,
                            rarity: nil
                        ))
                    }
                    return MetadataViews.Traits(traits)

			}

			return PuffPalz.resolveContractView(resourceType: Type<@NFT>(), viewType: view)
		}

        access(all) fun createEmptyCollection(): @Collection {
            return <- create Collection()
        }
	}

	access(all) resource interface CollectionPublic: NonFungibleToken.Collection {
        access(all) view fun borrowPuffPalz(id: UInt64): &PuffPalz.NFT? {
            post {
                (result == nil) || (result?.id == id):
                    "Cannot borrow PuffPalz reference: The ID of the returned reference is incorrect."
            }
        }
	}

	access(all) resource Collection: CollectionPublic {
		// dictionary of NFT conforming tokens
		// NFT is a resource type with an 'UInt64' ID field
		access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}

		// withdraw removes an NFT from the collection and moves it to the caller
		access(NonFungibleToken.Withdraw) fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {
			let token <- self.ownedNFTs.remove(key: withdrawID) ?? panic("missing NFT")

			emit Withdraw(id: token.id, from: self.owner?.address)

			return <-token
		}

		// deposit takes a NFT and adds it to the collections dictionary
		// and adds the ID to the id array
		access(all) fun deposit(token: @{NonFungibleToken.NFT}) {
			let token <- token as! @PuffPalz.NFT

			let id: UInt64 = token.id

			let oldToken <- self.ownedNFTs[id] <- token

			emit Deposit(id: id, to: self.owner?.address)

            destroy oldToken
		}

		// getIDs returns an array of the IDs that are in the collection
		access(all) view fun getIDs(): [UInt64] {
			return self.ownedNFTs.keys
		}


		// borrowNFT gets a reference to an NFT in the collection
		// so that the caller can read its metadata and call its methods
		access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
			return &self.ownedNFTs[id]
		}

       access(all) view fun borrowPuffPalz(id: UInt64): &PuffPalz.NFT? {
            if let ref: &{NonFungibleToken.NFT} = &self.ownedNFTs[id] {
                return ref as! &PuffPalz.NFT
            }

            return nil
        }

        access(all) view fun getSupportedNFTTypes(): {Type: Bool} {
            return {
                Type<@NFT>(): true
            }
        }

        access(all) view fun isSupportedNFTType(type: Type): Bool {
            return type == Type<@NFT>()
        }

        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            return <- create Collection()
        }

		init () {
			self.ownedNFTs <- {}
		}
	}

	access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {
		return <- create Collection()
	}

	access(all) resource Admin {
		access(Owner) fun mintNFT(
            recipient: &{NonFungibleToken.CollectionPublic},
            name: String,
            description: String,
            image: String,
            traits: {String:String}
            ) {
			    emit ExclusiveMinted(id: PuffPalz.totalSupply, name: name, description: description, image: image, traits: traits)
			    PuffPalz.totalSupply = PuffPalz.totalSupply + 1

			recipient.deposit(token: <- create PuffPalz.NFT(
                    _id: PuffPalz.totalSupply,
                    _name: name,
                    _description: description,
                    _image: image,
                    _traits: traits
                )
			)
		}
	}

    access(all) view fun getContractViews(resourceType: Type?): [Type] {
        return [
            Type<MetadataViews.NFTCollectionData>(),
            Type<MetadataViews.NFTCollectionDisplay>()
        ]
    }

    access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {
        switch viewType {
            case Type<MetadataViews.NFTCollectionData>():
                return MetadataViews.NFTCollectionData(
                    storagePath: PuffPalz.CollectionStoragePath,
                    publicPath: PuffPalz.CollectionPublicPath,
                    publicCollection: Type<&Collection>(),
                    publicLinkedType: Type<&Collection>(),
                    createEmptyCollectionFunction: (fun (): @{NonFungibleToken.Collection} {
                            return <- PuffPalz.createEmptyCollection(nftType: Type<@NFT>())
                    })
                )

            case Type<MetadataViews.NFTCollectionDisplay>():
                let squareMedia = MetadataViews.Media(
                    file: MetadataViews.HTTPFile(
                        url: "https://puffpalz.io/static/media/logo_trans.23a0132ea8d91f699ce0.webp"
                    ),
                    mediaType: "image"
                )
                let bannerMedia = MetadataViews.Media(
                    file: MetadataViews.HTTPFile(
                        url: "https://puffpalz.io/static/media/logo_trans.23a0132ea8d91f699ce0.webp"
                    ),
                    mediaType: "image"
                )
                return MetadataViews.NFTCollectionDisplay(
                    name: "Puff Palz",
                    description: "Puff Palz Collection",
                    externalURL: MetadataViews.ExternalURL("https://puffpalz.io/"),
                    squareImage: squareMedia,
                    bannerImage: bannerMedia,
                    socials: {
                        "twitter": MetadataViews.ExternalURL("https://twitter.com/FlowPartyFavorz"),
                        "discord": MetadataViews.ExternalURL("https://discord.gg/nDxrtnxN")
                    }
                )
        }

        return nil
    }

	init() {

		self.CollectionStoragePath = /storage/PuffPalzCollection
		self.CollectionPublicPath = /public/PuffPalzCollection
		self.CollectionPrivatePath = /private/PuffPalzCollection
		self.AdminStoragePath = /storage/PuffPalzMinter

		self.totalSupply = 0

		let minter <- create Admin()
		self.account.storage.save(<-minter, to: self.AdminStoragePath)

		let collection <- PuffPalz.createEmptyCollection(nftType: Type<@NFT>())
		self.account.storage.save(<- collection, to: self.CollectionStoragePath)

        self.account.capabilities.publish(
            self.account.capabilities.storage.issue<&PuffPalz.Collection>(self.CollectionStoragePath),
            at: self.CollectionPublicPath
        )

		emit ContractInitialized()
	}
}

```