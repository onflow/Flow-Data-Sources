# Source: https://academy.ecdao.org/en/cadence-by-example/25-admin-access

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Admin Access

# Admin Access

Sometimes we only want an Admin to be able to execute certain actions, like minting an NFT.

We can simply make a resource that gets saved to the contractâs account upon deployment, and isnât able to be created otherwise.

cadence

```
		
			// Contract file: Test.cdc
// Deployed to 0x01
access(all) contract Test {

   access(all) resource NFT {
      access(all) let id: UInt64
      access(all) let rarity: String
      
      init(rarity: String) {
         self.id = self.uuid
         self.rarity = rarity
      }
   }

   access(all) resource Admin {
      access(all) fun createNFT(rarity: String): @NFT {
         let nft <- create NFT(rarity: rarity)
         return <- nft
      }
   }

   init() {
      // like the `prepare` phase of a transaction where we can 
      // get authorized references on an account, we can access 
      // an authorized reference on the contract's account 
      // by using `self.account` in the contract's init function.
      self.account.storage.save(<- create Admin(), to: /storage/TestAdmin)
   }

}
		 
	
```

cadence

```
		
			// Transaction file: mint_nft.cdc
import Test from 0x01

transaction(rarity: String) {

   let Admin: &Test.Admin

   // the signer is the account with the Admin resource
   prepare(signer: auth(BorrowValue) &Account) {
      self.Admin = signer.storage.borrow<&Test.Admin>(from: /storage/TestAdmin) 
                           ?? panic("This signer is not an Admin.")
   }

   execute {
      let nft <- self.Admin.createNFT(rarity: rarity)

      // do something with nft here...
      destroy nft
   }
}
		 
	
```

[Time](/en/cadence-by-example/24-time)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/25-admin-access.md)



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