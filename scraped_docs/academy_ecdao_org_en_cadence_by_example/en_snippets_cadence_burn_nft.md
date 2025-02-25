# Source: https://academy.ecdao.org/en/snippets/cadence-burn-nft

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Burn an NFT in Cadence

# Burn an NFT in Cadence

Snippet

cadence

```
		
			import Avataaars from 0xcb9a812737bbc679

transaction(nftID: UInt64) {

  let Collection: auth(NonFungibleToken.Withdraw) &Avataaars.Collection

  prepare(signer: auth(Storage) &Account) {
    // borrow a reference to the signer's collection
    self.Collection = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &Avataaars.Collection>
                        (from: Avataaars.CollectionStoragePath)
                        ?? panic("The signer does not have an Avataaars collection set up, and therefore no NFTs to burn.")
  }

  execute {
    // withdraw the nft from the collection
    let nft <- self.Collection.withdraw(withdrawID: nftID)

    // destroy, or "burn", the nft
    destroy nft
  }
}
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://run.ecdao.org?code=aW1wb3J0IEF2YXRhYWFycyBmcm9tIDB4Y2I5YTgxMjczN2JiYzY3OQoKdHJhbnNhY3Rpb24obmZ0SUQ6IFVJbnQ2NCkgewoKICBsZXQgQ29sbGVjdGlvbjogJkF2YXRhYWFycy5Db2xsZWN0aW9uCgogIHByZXBhcmUoc2lnbmVyOiBBdXRoQWNjb3VudCkgewogICAgLy8gYm9ycm93IGEgcmVmZXJlbmNlIHRvIHRoZSBzaWduZXIncyBjb2xsZWN0aW9uCiAgICBzZWxmLkNvbGxlY3Rpb24gPSBzaWduZXIuYm9ycm93PCZBdmF0YWFhcnMuQ29sbGVjdGlvbj4oZnJvbTogQXZhdGFhYXJzLkNvbGxlY3Rpb25TdG9yYWdlUGF0aCkKICAgICAgICAgICAgICAgICAgICAgICAgPz8gcGFuaWMoIlRoZSBzaWduZXIgZG9lcyBub3QgaGF2ZSBhbiBBdmF0YWFhcnMgY29sbGVjdGlvbiBzZXQgdXAsIGFuZCB0aGVyZWZvcmUgbm8gTkZUcyB0byBidXJuLiIpCiAgfQoKICBleGVjdXRlIHsKICAgIC8vIHdpdGhkcmF3IHRoZSBuZnQgZnJvbSB0aGUgY29sbGVjdGlvbgogICAgbGV0IG5mdCA8LSBzZWxmLkNvbGxlY3Rpb24ud2l0aGRyYXcod2l0aGRyYXdJRDogbmZ0SUQpCiAgICAKICAgIC8vIGRlc3Ryb3ksIG9yICJidXJuIiwgdGhlIG5mdAogICAgZGVzdHJveSBuZnQKICB9Cn0%3D&network=mainnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-burn-nft/readme.md)



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