# Source: https://academy.ecdao.org/en/snippets/cadence-transfer-nft

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Transfer an NFT in Cadence

# Transfer an NFT in Cadence

Snippet

cadence

```
		
			import NonFungibleToken from 0x1d7e57aa55817448
import Avataaars from 0xcb9a812737bbc679

// The person trasnferring the NFT is the one who signs this

transaction(recipient: Address, nftID: UInt64) {

    // Reference to the withdrawer's collection
    let withdrawRef: auth(NonFungibleToken.Withdraw) &Avataaars.Collection

    // Reference of the collection to deposit the NFT to
    let depositRef: &Avataaars.Collection{NonFungibleToken.Receiver}

    prepare(signer: auth(Storage) &Account) {
        // borrow a reference to the signer's NFT collection
        self.withdrawRef = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &Avataaars.Collection>
                                (from: Avataaars.CollectionStoragePath)
                                ?? panic("Account does not store an object at the specified path")

        self.depositRef = getAccount(recipient).capabilities.borrow<&Avataaars.Collection>(Avataaars.CollectionPublicPath)
                            ?? panic("Could not borrow a reference to the receiver's collection")

    }

    execute {
        // withdraw the NFT from the owner's collection
        let nft <- self.withdrawRef.withdraw(withdrawID: nftID)

        // Deposit the NFT in the recipient's collection
        self.depositRef.deposit(token: <-nft)
    }
}
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://run.ecdao.org?code=aW1wb3J0IE5vbkZ1bmdpYmxlVG9rZW4gZnJvbSAweDFkN2U1N2FhNTU4MTc0NDgKaW1wb3J0IEF2YXRhYWFycyBmcm9tIDB4Y2I5YTgxMjczN2JiYzY3OQoKLy8gVGhlIHBlcnNvbiB0cmFzbmZlcnJpbmcgdGhlIE5GVCBpcyB0aGUgb25lIHdobyBzaWducyB0aGlzCgp0cmFuc2FjdGlvbihyZWNpcGllbnQ6IEFkZHJlc3MsIG5mdElEOiBVSW50NjQpIHsKCiAgICAvLyBSZWZlcmVuY2UgdG8gdGhlIHdpdGhkcmF3ZXIncyBjb2xsZWN0aW9uCiAgICBsZXQgd2l0aGRyYXdSZWY6ICZBdmF0YWFhcnMuQ29sbGVjdGlvbgoKICAgIC8vIFJlZmVyZW5jZSBvZiB0aGUgY29sbGVjdGlvbiB0byBkZXBvc2l0IHRoZSBORlQgdG8KICAgIGxldCBkZXBvc2l0UmVmOiAmQXZhdGFhYXJzLkNvbGxlY3Rpb257Tm9uRnVuZ2libGVUb2tlbi5SZWNlaXZlcn0KCiAgICBwcmVwYXJlKHNpZ25lcjogQXV0aEFjY291bnQpIHsKICAgICAgICAvLyBib3Jyb3cgYSByZWZlcmVuY2UgdG8gdGhlIHNpZ25lcidzIE5GVCBjb2xsZWN0aW9uCiAgICAgICAgc2VsZi53aXRoZHJhd1JlZiA9IHNpZ25lci5ib3Jyb3c8JkF2YXRhYWFycy5Db2xsZWN0aW9uPihmcm9tOiBBdmF0YWFhcnMuQ29sbGVjdGlvblN0b3JhZ2VQYXRoKQogICAgICAgICAgICAgICAgPz8gcGFuaWMoIkFjY291bnQgZG9lcyBub3Qgc3RvcmUgYW4gb2JqZWN0IGF0IHRoZSBzcGVjaWZpZWQgcGF0aCIpCgogICAgICAgIHNlbGYuZGVwb3NpdFJlZiA9IGdldEFjY291bnQocmVjaXBpZW50KS5nZXRDYXBhYmlsaXR5KEF2YXRhYWFycy5Db2xsZWN0aW9uUHVibGljUGF0aCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIC5ib3Jyb3c8JkF2YXRhYWFycy5Db2xsZWN0aW9ue05vbkZ1bmdpYmxlVG9rZW4uQ29sbGVjdGlvblB1YmxpY30%2BKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgID8%2FIHBhbmljKCJDb3VsZCBub3QgYm9ycm93IGEgcmVmZXJlbmNlIHRvIHRoZSByZWNlaXZlcidzIGNvbGxlY3Rpb24iKQoKICAgIH0KCiAgICBleGVjdXRlIHsKICAgICAgICAvLyB3aXRoZHJhdyB0aGUgTkZUIGZyb20gdGhlIG93bmVyJ3MgY29sbGVjdGlvbgogICAgICAgIGxldCBuZnQgPC0gc2VsZi53aXRoZHJhd1JlZi53aXRoZHJhdyh3aXRoZHJhd0lEOiBuZnRJRCkKCiAgICAgICAgLy8gRGVwb3NpdCB0aGUgTkZUIGluIHRoZSByZWNpcGllbnQncyBjb2xsZWN0aW9uCiAgICAgICAgc2VsZi5kZXBvc2l0UmVmLmRlcG9zaXQodG9rZW46IDwtbmZ0KQogICAgfQp9&network=mainnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-transfer-nft/readme.md)



[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow

##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)


##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)


##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)

[Join the community](https://discord.gg/emerald-city-906264258189332541)