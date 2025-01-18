# Source: https://academy.ecdao.org/en/snippets/cadence-mint-nft


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Mint an NFT in Cadence

# Mint an NFT in Cadence


Snippet



cadence
```
		
			import Avataaars from 0xcb9a812737bbc679
import NonFungibleToken from 0x1d7e57aa55817448
import MetadataViews from 0x1d7e57aa55817448

transaction() {

  let Collection: &Avataaars.Collection

  prepare(signer: auth(Storage, Capabilities) &Account) {
    // if the signer does not have an Avataaars collection set up, then do that here
    if signer.storage.borrow<&Avataaars.Collection>(from: Avataaars.CollectionStoragePath) == nil {
      // save the Avataaars collection to storage
      signer.storage.save(
        <- Avataaars.createEmptyCollection(nftType: Type<@Avataaars.NFT>()),
        to: Avataaars.CollectionStoragePath
      )

      // publish a public capability
      let cap = signer.capabilities.storage.issue<&Avataaars.Collection>(Avataaars.CollectionStoragePath)
      signer.capabilities.publish(cap, at: Avataaars.CollectionPublicPath)
    }

    self.Collection = signer.storage.borrow<&Avataaars.Collection>(from: Avataaars.CollectionStoragePath)!
  }

  execute {
    // borrow the public minter, which allows anyone to mint
    let minter: &{Avataaars.MinterPublic} = Avataaars.borrowMinter()
    // mint the NFT
    minter.mintNFT(recipient: self.Collection)
  }
}
		 
	
```


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Run Code](https://run.ecdao.org?code=aW1wb3J0IEF2YXRhYWFycyBmcm9tIDB4Y2I5YTgxMjczN2JiYzY3OQppbXBvcnQgTm9uRnVuZ2libGVUb2tlbiBmcm9tIDB4MWQ3ZTU3YWE1NTgxNzQ0OAppbXBvcnQgTWV0YWRhdGFWaWV3cyBmcm9tIDB4MWQ3ZTU3YWE1NTgxNzQ0OAoKdHJhbnNhY3Rpb24oKSB7CgogIGxldCBDb2xsZWN0aW9uOiAmQXZhdGFhYXJzLkNvbGxlY3Rpb24KCiAgcHJlcGFyZShzaWduZXI6IEF1dGhBY2NvdW50KSB7CiAgICAvLyBpZiB0aGUgc2lnbmVyIGRvZXMgbm90IGhhdmUgYW4gQXZhdGFhYXJzIGNvbGxlY3Rpb24gc2V0IHVwLCB0aGVuIGRvIHRoYXQgaGVyZQogICAgaWYgc2lnbmVyLmJvcnJvdzwmQXZhdGFhYXJzLkNvbGxlY3Rpb24%2BKGZyb206IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpID09IG5pbCB7CiAgICAgIC8vIHNhdmUgdGhlIEF2YXRhYWFycyBjb2xsZWN0aW9uIHRvIHN0b3JhZ2UKICAgICAgc2lnbmVyLnNhdmUoPC0gQXZhdGFhYXJzLmNyZWF0ZUVtcHR5Q29sbGVjdGlvbigpLCB0bzogQXZhdGFhYXJzLkNvbGxlY3Rpb25TdG9yYWdlUGF0aCkKICAgICAgLy8gbGluayBpdCB0byB0aGUgcHVibGljIHNvIHBlb3BsZSBjYW4gcmVhZCBkYXRhIGZyb20gaXQKICAgICAgc2lnbmVyLmxpbms8JkF2YXRhYWFycy5Db2xsZWN0aW9ue0F2YXRhYWFycy5BdmF0YWFhcnNDb2xsZWN0aW9uUHVibGljLCBOb25GdW5naWJsZVRva2VuLlJlY2VpdmVyLCBOb25GdW5naWJsZVRva2VuLkNvbGxlY3Rpb25QdWJsaWMsIE1ldGFkYXRhVmlld3MuUmVzb2x2ZXJDb2xsZWN0aW9ufT4oQXZhdGFhYXJzLkNvbGxlY3Rpb25QdWJsaWNQYXRoLCB0YXJnZXQ6IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpCiAgICB9CgogICAgc2VsZi5Db2xsZWN0aW9uID0gc2lnbmVyLmJvcnJvdzwmQXZhdGFhYXJzLkNvbGxlY3Rpb24%2BKGZyb206IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpIQogIH0KCiAgZXhlY3V0ZSB7CiAgICAvLyBib3Jyb3cgdGhlIHB1YmxpYyBtaW50ZXIsIHdoaWNoIGFsbG93cyBhbnlvbmUgdG8gbWludAogICAgbGV0IG1pbnRlcjogJntBdmF0YWFhcnMuTWludGVyUHVibGljfSA9IEF2YXRhYWFycy5ib3Jyb3dNaW50ZXIoKQogICAgLy8gbWludCB0aGUgTkZUCiAgICBtaW50ZXIubWludE5GVChyZWNpcGllbnQ6IHNlbGYuQ29sbGVjdGlvbikKICB9Cn0%3D&network=mainnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-mint-nft/readme.md)


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow


##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)
##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)
##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)
[Join the community](https://discord.gg/emerald-city-906264258189332541)



