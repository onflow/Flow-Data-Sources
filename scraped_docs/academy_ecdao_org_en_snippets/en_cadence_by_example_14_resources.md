# Source: https://academy.ecdao.org/en/cadence-by-example/14-resources
















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Resources

# Resources

Resources are much like structs in that they have data and functions inside of them. However, they differ in the following ways:

* They can only ever be created in the contract using the `create` keyword
* They are moved around using the `<-` operator
* Their type is prefixed with a `@`
* They cannot be copied or lost, and must be explicity stored somewhere or destroyed

cadence
```
		
			// Contract file: Test.cdc
// Deployed to 0x01
access(all) contract Test {

   access(all) resource NFT {
      access(all) let id: UInt64
      access(all) var name: String

      access(all) fun changeName(newName: String) {
         self.name = newName
      }
      
      // Will get run when the resource is created
      init(name: String) {
         // every resource has a unique `uuid` field 
         // that will never be the same, even after the resource is destroyed
         self.id = self.uuid
         self.name = name
      }
   }

   // resource types have a `@` in front
   access(all) fun mintNFT(name: String): @NFT {
      let nft <- create NFT(name: name)
      return <- nft
   }

   init() {
      self.totalSupply = 0
   }
}
		 
	
```

cadence
```
		
			// Transaction file: mint_and_destroy_nft.cdc
import Test from 0x01

transaction(name: String) {

   prepare(signer: &Account) {}

   execute {
     let nft: @Test.NFT <- Test.mintNFT(name: name)

     // we must destroy the resource or store it somewhere, 
     // or we will get a `loss of resource` error
     destroy nft

     /*
      ERROR: `nft` no longer exists here
     
      log(nft.name)
     */
   }
}
		 
	
```


[Structs](/en/cadence-by-example/13-structs)
[Interfaces](/en/cadence-by-example/15-interfaces)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/14-resources.md)

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



