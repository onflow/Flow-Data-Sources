# Source: https://academy.ecdao.org/en/snippets/cadence-bulk-transfer-nft

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Bulk Transfer NFTs in Cadence

# Bulk Transfer NFTs in Cadence

Snippet

cadence

```
		
			import NonFungibleToken from 0x1d7e57aa55817448
import Avataaars from 0xcb9a812737bbc679

// The person trasnferring the NFT is the one who signs this

transaction(nftIDs: [UInt64], recipients: [Address]) {

    // Reference to the withdrawer's collection
    let withdrawRef: auth(NonFungibleToken.Withdraw) &Avataaars.Collection

    prepare(signer: auth(Storage) &Account) {
        // borrow a reference to the signer's NFT collection
        self.withdrawRef = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &Avataaars.Collection>
                            (from: Avataaars.CollectionStoragePath)
                            ?? panic("Account does not store an object at the specified path")
    }

    execute {
        for i, nftID in nftIDs {
            // get recipient address for this nftID
            let recipient: Address = recipients[i]

            // Reference of the collection to deposit the NFT to
            let depositRef = getAccount(recipient).capabilities.borrow<&Avataaars.Collection>(Avataaars.CollectionPublicPath)
                                ?? panic("Could not borrow a reference to the receiver's collection")

            // withdraw the NFT from the owner's collection
            let nft <- self.withdrawRef.withdraw(withdrawID: nftID)

            // Deposit the NFT in the recipient's collection
            depositRef.deposit(token: <- nft)
        }
    }
}
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://run.ecdao.org?code=aW1wb3J0IE5vbkZ1bmdpYmxlVG9rZW4gZnJvbSAweDFkN2U1N2FhNTU4MTc0NDgKaW1wb3J0IEF2YXRhYWFycyBmcm9tIDB4Y2I5YTgxMjczN2JiYzY3OQoKLy8gVGhlIHBlcnNvbiB0cmFzbmZlcnJpbmcgdGhlIE5GVCBpcyB0aGUgb25lIHdobyBzaWducyB0aGlzCgp0cmFuc2FjdGlvbihuZnRJRHM6IFtVSW50NjRdLCByZWNpcGllbnRzOiBbQWRkcmVzc10pIHsKCiAgICAvLyBSZWZlcmVuY2UgdG8gdGhlIHdpdGhkcmF3ZXIncyBjb2xsZWN0aW9uCiAgICBsZXQgd2l0aGRyYXdSZWY6ICZBdmF0YWFhcnMuQ29sbGVjdGlvbgoKICAgIHByZXBhcmUoc2lnbmVyOiBBdXRoQWNjb3VudCkgewogICAgICAgIC8vIGJvcnJvdyBhIHJlZmVyZW5jZSB0byB0aGUgc2lnbmVyJ3MgTkZUIGNvbGxlY3Rpb24KICAgICAgICBzZWxmLndpdGhkcmF3UmVmID0gc2lnbmVyLmJvcnJvdzwmQXZhdGFhYXJzLkNvbGxlY3Rpb24%2BKGZyb206IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpCiAgICAgICAgICAgICAgICA%2FPyBwYW5pYygiQWNjb3VudCBkb2VzIG5vdCBzdG9yZSBhbiBvYmplY3QgYXQgdGhlIHNwZWNpZmllZCBwYXRoIikKICAgIH0KCiAgICBleGVjdXRlIHsKICAgICAgICBmb3IgaSwgbmZ0SUQgaW4gbmZ0SURzIHsKICAgICAgICAgICAgLy8gZ2V0IHJlY2lwaWVudCBhZGRyZXNzIGZvciB0aGlzIG5mdElECiAgICAgICAgICAgIGxldCByZWNpcGllbnQ6IEFkZHJlc3MgPSByZWNpcGllbnRzW2ldCgogICAgICAgICAgICAvLyBSZWZlcmVuY2Ugb2YgdGhlIGNvbGxlY3Rpb24gdG8gZGVwb3NpdCB0aGUgTkZUIHRvCiAgICAgICAgICAgIGxldCBkZXBvc2l0UmVmID0gZ2V0QWNjb3VudChyZWNpcGllbnQpLmdldENhcGFiaWxpdHkoQXZhdGFhYXJzLkNvbGxlY3Rpb25QdWJsaWNQYXRoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC5ib3Jyb3c8JkF2YXRhYWFycy5Db2xsZWN0aW9ue05vbkZ1bmdpYmxlVG9rZW4uQ29sbGVjdGlvblB1YmxpY30%2BKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA%2FPyBwYW5pYygiQ291bGQgbm90IGJvcnJvdyBhIHJlZmVyZW5jZSB0byB0aGUgcmVjZWl2ZXIncyBjb2xsZWN0aW9uIikKCiAgICAgICAgICAgIC8vIHdpdGhkcmF3IHRoZSBORlQgZnJvbSB0aGUgb3duZXIncyBjb2xsZWN0aW9uCiAgICAgICAgICAgIGxldCBuZnQgPC0gc2VsZi53aXRoZHJhd1JlZi53aXRoZHJhdyh3aXRoZHJhd0lEOiBuZnRJRCkKCiAgICAgICAgICAgIC8vIERlcG9zaXQgdGhlIE5GVCBpbiB0aGUgcmVjaXBpZW50J3MgY29sbGVjdGlvbgogICAgICAgICAgICBkZXBvc2l0UmVmLmRlcG9zaXQodG9rZW46IDwtIG5mdCkKICAgICAgICB9CiAgICB9Cn0%3D&network=mainnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-bulk-transfer-nft/readme.md)



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